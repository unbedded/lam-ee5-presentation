#!/usr/bin/env python3
"""
Extract trade-off data from YAML sources into JSON

This script reads architectures.yaml and decision-logic.yaml and extracts
all data needed for trade-off analysis charts into a clean JSON format.

Purpose: Separate data extraction from plotting for easier debugging

Usage:
    python3 scripts/extract_tradeoff_data.py

Outputs:
    data/tradeoff-data.json (intermediate data for plotting)
"""

import yaml
import json
import csv
from pathlib import Path

# Configuration
ARCHITECTURES_YAML = Path("source/architectures.yaml")
DECISION_LOGIC_YAML = Path("source/decision-logic.yaml")
PARTS_CSV = Path("source/parts.csv")
BOM_DIR = Path("artifacts/bom")
OUTPUT_JSON = Path("data/tradeoff-data.json")
OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)

# BOM file mapping
BOM_FILES = {
    "ARCH_PIEZO_ECO": BOM_DIR / "arch-piezo-eco-bom.csv",
    "ARCH_SOL_ECO": BOM_DIR / "arch-sol-eco-bom.csv",
    "ARCH_PIEZO_DLX": BOM_DIR / "arch-piezo-dlx-bom.csv",
}

# Architecture color scheme (for plotting)
ARCH_COLORS = {
    "ARCH_PIEZO_ECO": "#2E86AB",  # Blue
    "ARCH_SOL_ECO": "#A23B72",    # Purple
    "ARCH_PIEZO_DLX": "#F18F01",  # Orange
}

# Qualitative rating mapping (simplified 3 levels)
RATING_MAP = {
    "EXCELLENT": 10,
    "BEST": 10,
    "GOOD": 7,
    "FAIR": 5,
    "POOR": 3,
    "WORST": 3,
}


def parse_qualitative_rating(rating_data):
    """
    Parse qualitative rating - handles strings and dicts

    Examples:
        "BEST" → 10
        {"setup": "BEST", "convenience": "FAIR"} → 7.5 (average)

    Returns:
        float: Score 0-10
    """
    if not rating_data:
        return 5.0

    # Handle dict ratings (average of sub-ratings)
    if isinstance(rating_data, dict):
        scores = []
        for value in rating_data.values():
            if isinstance(value, (str, dict)):
                scores.append(parse_qualitative_rating(value))
        return sum(scores) / len(scores) if scores else 5.0

    # Handle string ratings
    if not isinstance(rating_data, str):
        return 5.0

    rating_str = rating_data.upper()

    # Check RATING_MAP keywords
    for keyword, score in RATING_MAP.items():
        if keyword in rating_str:
            return float(score)

    # Additional keyword mappings from YAML
    keyword_map = {
        "NONE": 10,  # e.g., battery_anxiety: "NONE" is best
        "LOW": 9,
        "MEDIUM-LOW": 7,
        "MEDIUM": 6,
        "MEDIUM-HIGH": 5,
        "HIGH": 4,
        "VERY-HIGH": 3,
        "SMALL": 9,
        "LARGE": 4,
        "LIGHT": 9,
        "HEAVY": 4,
    }

    for keyword, score in keyword_map.items():
        if keyword in rating_str:
            return float(score)

    return 5.0  # Default middle rating


def normalize_to_scale(value, min_val, max_val, lower_is_better=False):
    """
    Normalize value to 0-10 scale

    Args:
        value: Raw value
        min_val: Minimum in dataset
        max_val: Maximum in dataset
        lower_is_better: If True, invert scale (cost, timeline)

    Returns:
        float: Normalized score 0-10
    """
    if max_val == min_val:
        return 5.0

    normalized = (value - min_val) / (max_val - min_val) * 10

    if lower_is_better:
        normalized = 10 - normalized

    return normalized


def load_parts_database(use_pilot_leadtime=True):
    """
    Load parts.csv to get leadtime data for all subsystems

    Args:
        use_pilot_leadtime: If True, use Leadtime_Weeks_Pilot (distributor stock for 200 units)
                           If False, use Leadtime_Weeks (production, factory direct for 1000+ units)

    Returns:
        dict: {subsystem_id: {"leadtime_weeks": float, "mfr": str, "mfr_pn": str}}
    """
    print(f"Loading parts database: {PARTS_CSV}")
    leadtime_column = 'Leadtime_Weeks_Pilot' if use_pilot_leadtime else 'Leadtime_Weeks'
    print(f"  Using: {leadtime_column} ({'pilot quantity ~200 units' if use_pilot_leadtime else 'production 1000+ units'})")

    parts_db = {}

    with open(PARTS_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            subsystem = row.get('Subsystem', '').strip()
            if subsystem:
                # Try pilot leadtime first, fallback to production leadtime
                leadtime_str = row.get(leadtime_column, row.get('Leadtime_Weeks', '0'))
                leadtime = float(leadtime_str) if leadtime_str else 0.0
                parts_db[subsystem] = {
                    "leadtime_weeks": leadtime,
                    "leadtime_pilot": float(row.get('Leadtime_Weeks_Pilot', leadtime_str)),
                    "leadtime_production": float(row.get('Leadtime_Weeks', leadtime_str)),
                    "mfr": row.get('MFR', ''),
                    "mfr_pn": row.get('MFR_PN', ''),
                }

    print(f"  Loaded {len(parts_db)} parts definitions")
    return parts_db


def calculate_timeline_from_bom(arch_id, quant, parts_db):
    """
    Calculate timeline to pilot production from parts leadtime + assembly + certification

    Timeline = max(parts leadtime) + assembly + certification

    Returns:
        tuple: (timeline_low, timeline_high, max_leadtime_weeks, cert_weeks)
    """
    # Load BOM CSV for this architecture
    bom_file = BOM_FILES.get(arch_id)
    if not bom_file or not bom_file.exists():
        # Fallback to YAML if BOM not found
        timeline_data = quant.get('timeline', {})
        total = float(timeline_data.get('total_weeks', 8))
        return total, total, 0, 0

    # Read BOM to get list of subsystems
    with open(bom_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find max leadtime from parts database
    max_leadtime = 0
    max_leadtime_part = ""
    for row in rows:
        subsystem_id = row.get('Subsystem_ID', '').strip()
        if subsystem_id and subsystem_id != '---' and not subsystem_id.startswith('---'):
            # Look up in parts database
            if subsystem_id in parts_db:
                leadtime = parts_db[subsystem_id]['leadtime_weeks']
                if leadtime > max_leadtime:
                    max_leadtime = leadtime
                    max_leadtime_part = subsystem_id

    # Get certification time and assembly time from architectures.yaml
    timeline_data = quant.get('timeline', {})
    cert_weeks = float(timeline_data.get('certification_weeks', 0))
    assembly_weeks = float(timeline_data.get('pilot_production_weeks', 2))

    # Timeline calculation:
    # - timeline_low = max(leadtime) + assembly (certification can happen in parallel)
    # - timeline_high = max(leadtime) + assembly + certification (if serial)
    timeline_low = max_leadtime + assembly_weeks
    timeline_high = max_leadtime + assembly_weeks + cert_weeks

    print(f"    Critical path: {max_leadtime_part} ({max_leadtime} wks) + assembly ({assembly_weeks} wks) + cert ({cert_weeks} wks)")
    print(f"    Timeline: {timeline_low:.0f}-{timeline_high:.0f} weeks")

    return timeline_low, timeline_high, max_leadtime, cert_weeks


def load_bom_data(arch_id):
    """
    Load BOM CSV file and extract cost data + actuator assumptions + subsystem breakdown

    Returns:
        dict: {
            "total_cost": float,
            "actuator_cost": float,
            "actuator_qty": int,
            "actuator_unit_price": float,
            "actuator_notes": str,
            "cost_breakdown": {
                "Actuators": float,
                "Control": float,
                "Power": float,
                "Communication": float,
                "Mechanical": float,
                "EMI": float
            }
        }
    """
    bom_file = BOM_FILES.get(arch_id)
    if not bom_file or not bom_file.exists():
        print(f"  Warning: BOM file not found for {arch_id}")
        return None

    with open(bom_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Extract total cost (last row with "TOTAL")
    total_cost = 0.0
    for row in reversed(rows):
        if row.get('Description', '').strip() == 'TOTAL':
            total_cost = float(row.get('Line_Total', 0))
            break

    # Initialize cost breakdown by category
    cost_breakdown = {
        "Actuators": 0.0,
        "Control": 0.0,
        "Power": 0.0,
        "Communication": 0.0,
        "Mechanical": 0.0,
        "EMI": 0.0,
        "Misc": 0.0  # Passives, connectors (15% overhead)
    }

    # Extract actuator data and categorize costs
    actuator_data = {
        "cost": 0.0,
        "qty": 0,
        "unit_price": 0.0,
        "notes": ""
    }

    for row in rows:
        subsystem_id = row.get('Subsystem_ID', '').strip()
        description = row.get('Description', '').strip()

        # Handle special rows
        if subsystem_id.startswith('---'):
            # Check for Misc 15% row
            if 'Misc' in description and '%' in description:
                misc_cost = float(row.get('Line_Total', 0))
                cost_breakdown["Misc"] = misc_cost
            continue

        line_total = float(row.get('Line_Total', 0))

        # Categorize by subsystem prefix
        if subsystem_id.startswith('SS-ACTUATOR'):
            cost_breakdown["Actuators"] += line_total
            # Save primary actuator details
            if not subsystem_id.endswith('-DRIVER') and actuator_data["cost"] == 0:
                actuator_data = {
                    "cost": line_total,
                    "qty": int(row.get('Qty', 0)),
                    "unit_price": float(row.get('Unit_Price_1000', 0)),
                    "notes": row.get('Notes', '').strip()
                }
        elif subsystem_id.startswith('SS-CONTROL') or subsystem_id.startswith('SS-IO-EXPAND'):
            cost_breakdown["Control"] += line_total
        elif subsystem_id.startswith('SS-POWER'):
            cost_breakdown["Power"] += line_total
        elif subsystem_id.startswith('SS-COMM'):
            cost_breakdown["Communication"] += line_total
        elif subsystem_id.startswith('SS-PCB') or subsystem_id.startswith('SS-ENCLOSURE') or subsystem_id.startswith('SS-USER-IO'):
            cost_breakdown["Mechanical"] += line_total
        elif subsystem_id.startswith('SS-EMI'):
            cost_breakdown["EMI"] += line_total

    return {
        "total_cost": total_cost,
        "actuator_cost": actuator_data["cost"],
        "actuator_qty": actuator_data["qty"],
        "actuator_unit_price": actuator_data["unit_price"],
        "actuator_notes": actuator_data["notes"],
        "cost_breakdown": cost_breakdown
    }


def load_architectures():
    """Load architectures.yaml"""
    print(f"Loading: {ARCHITECTURES_YAML}")
    with open(ARCHITECTURES_YAML, 'r') as f:
        data = yaml.safe_load(f)

    architectures_dict = data.get('architectures', {})

    # Convert to list, add id field
    active_archs = []
    for arch_id, arch_data in architectures_dict.items():
        if arch_id in ARCH_COLORS:
            arch_data['id'] = arch_id
            active_archs.append(arch_data)

    print(f"  Found {len(active_archs)} architectures: {[a['id'] for a in active_archs]}")
    return active_archs


def load_decision_logic():
    """Load decision-logic.yaml"""
    print(f"Loading: {DECISION_LOGIC_YAML}")
    with open(DECISION_LOGIC_YAML, 'r') as f:
        data = yaml.safe_load(f)

    print(f"  Found {len(data.get('decision_tree', []))} decision nodes")
    return data


def extract_quantitative_data(architectures):
    """
    Extract quantitative metrics from architectures

    Returns:
        dict: {
            "costs": [...],
            "timelines": [...],
            "weights": [...],
            "powers": [...]
        }
    """
    print("\nExtracting quantitative data...")

    costs = []
    timelines = []
    weights = []
    powers = []

    for arch in architectures:
        quant = arch.get('quantitative', {})

        # Extract cost from nested structure
        cost_data = quant.get('cost', {})
        cost = float(cost_data.get('bom_total', 0))
        costs.append(cost)

        # Extract timeline from nested structure
        timeline_data = quant.get('timeline', {})
        timeline = float(timeline_data.get('total_weeks', 8))
        timelines.append(timeline)

        # Extract weight from nested structure
        size_data = quant.get('size', {})
        weight = float(size_data.get('weight_lbs', 0))
        weights.append(weight)

        # Extract power from nested structure
        power = float(size_data.get('power_consumption_watts', 0))
        powers.append(power)

    print(f"  Costs:     {costs}")
    print(f"  Timelines: {timelines}")
    print(f"  Weights:   {weights}")
    print(f"  Powers:    {powers}")

    return {
        "costs": costs,
        "timelines": timelines,
        "weights": weights,
        "powers": powers,
    }


def extract_spider_data(architectures, quant_data):
    """
    Extract 8-dimension spider chart data

    Dimensions:
    1. Cost (lower better - inverted)
    2. Timeline (lower better - inverted)
    3. UX/Usability (qualitative)
    4. Manufacturability (qualitative)
    5. Robustness/Reliability (qualitative)
    6. Supply Chain Risk (qualitative - inverted)
    7. Power Efficiency (lower better - inverted)
    8. Complexity (lower better - inverted)

    Returns:
        dict: {arch_id: [8 normalized scores]}
    """
    print("\nExtracting spider chart data (8 dimensions)...")

    costs = quant_data["costs"]
    timelines = quant_data["timelines"]
    powers = quant_data["powers"]

    # Find min/max for normalization
    cost_min, cost_max = min(costs), max(costs)
    timeline_min, timeline_max = min(timelines), max(timelines)
    power_min, power_max = min(powers), max(powers)

    spider_data = {}

    for i, arch in enumerate(architectures):
        arch_id = arch['id']
        qual = arch.get('qualitative', {})

        # Normalize quantitative (lower is better - invert)
        cost_score = normalize_to_scale(costs[i], cost_min, cost_max, lower_is_better=True)
        timeline_score = normalize_to_scale(timelines[i], timeline_min, timeline_max, lower_is_better=True)
        power_score = normalize_to_scale(powers[i], power_min, power_max, lower_is_better=True)

        # Parse qualitative ratings
        ux_score = parse_qualitative_rating(qual.get('ux', {}))
        mfg_score = parse_qualitative_rating(qual.get('manufacturing', {}))
        robust_score = parse_qualitative_rating(qual.get('risk', {}))  # Use risk as proxy for robustness
        supply_score = 10 - parse_qualitative_rating(qual.get('risk', {}).get('supply_chain', 'MEDIUM') if isinstance(qual.get('risk'), dict) else {})
        complexity_score = 10 - parse_qualitative_rating(qual.get('complexity', {}))

        # Build 8-dimension array
        scores = [
            cost_score,
            timeline_score,
            ux_score,
            mfg_score,
            robust_score,
            supply_score,
            power_score,
            complexity_score,
        ]

        spider_data[arch_id] = [round(s, 2) for s in scores]
        print(f"  {arch_id}: {spider_data[arch_id]}")

    return spider_data


def extract_chart_data(architectures):
    """
    Extract data for bar charts (cost from BOM CSV, timeline from parts leadtime)

    Returns:
        dict: {
            "cost_chart": [...],
            "timeline_chart": [...],
            "actuator_assumptions": {...}
        }
    """
    print("\nExtracting bar chart data (from BOM CSV files)...")

    cost_chart = []
    timeline_chart = []
    actuator_assumptions = {}

    # Load parts database for timeline calculations (use pilot leadtimes for realistic delivery)
    parts_db = load_parts_database(use_pilot_leadtime=True)

    # Define order: SOL_ECO (left), PIEZO_ECO (middle), PIEZO_DLX (right)
    arch_order = ["ARCH_SOL_ECO", "ARCH_PIEZO_ECO", "ARCH_PIEZO_DLX"]

    for arch in architectures:
        arch_id = arch['id']
        quant = arch.get('quantitative', {})

        # Cost data from BOM CSV file
        bom_data = load_bom_data(arch_id)
        if bom_data:
            cost = bom_data["total_cost"]
            cost_chart.append({
                "arch_id": arch_id,
                "name": arch.get('name', arch_id),
                "cost": cost,
                "breakdown": bom_data["cost_breakdown"],
                "order": arch_order.index(arch_id) if arch_id in arch_order else 99
            })

            # Store actuator assumptions
            actuator_assumptions[arch_id] = {
                "unit_price": bom_data["actuator_unit_price"],
                "qty": bom_data["actuator_qty"],
                "total_cost": bom_data["actuator_cost"],
                "notes": bom_data["actuator_notes"]
            }

            print(f"  {arch_id}: ${cost:.2f} (actuator: ${bom_data['actuator_unit_price']:.2f} × {bom_data['actuator_qty']})")
            print(f"    Breakdown: Actuators=${bom_data['cost_breakdown']['Actuators']:.0f}, Control=${bom_data['cost_breakdown']['Control']:.0f}, Power=${bom_data['cost_breakdown']['Power']:.0f}, Comm=${bom_data['cost_breakdown']['Communication']:.0f}")
        else:
            # Fallback to YAML if BOM not found
            cost_data = quant.get('cost', {})
            cost = float(cost_data.get('bom_total', 0))
            cost_chart.append({
                "arch_id": arch_id,
                "name": arch.get('name', arch_id),
                "cost": cost,
                "order": arch_order.index(arch_id) if arch_id in arch_order else 99
            })
            print(f"  {arch_id}: ${cost:.2f} (from YAML - BOM not found)")

        # Timeline data from parts leadtime + assembly + certification
        print(f"\n  Calculating timeline for {arch_id}:")
        timeline_low, timeline_high, max_leadtime, cert_weeks = calculate_timeline_from_bom(
            arch_id, quant, parts_db
        )
        timeline_chart.append({
            "arch_id": arch_id,
            "name": arch.get('name', arch_id),
            "timeline_low": timeline_low,
            "timeline_high": timeline_high,
            "max_leadtime_weeks": max_leadtime,
            "certification_weeks": cert_weeks,
            "order": arch_order.index(arch_id) if arch_id in arch_order else 99
        })

    # Sort by order (SOL_ECO, PIEZO_ECO, PIEZO_DLX)
    cost_chart.sort(key=lambda x: x["order"])
    timeline_chart.sort(key=lambda x: x["order"])

    print(f"  Cost chart: {len(cost_chart)} entries (sorted by technology)")
    print(f"  Timeline chart: {len(timeline_chart)} entries")

    return {
        "cost_chart": cost_chart,
        "timeline_chart": timeline_chart,
        "actuator_assumptions": actuator_assumptions,
    }


def main():
    """Main execution"""
    print("\n" + "="*60)
    print("TRADE-OFF DATA EXTRACTION")
    print("="*60 + "\n")

    # Load source files
    architectures = load_architectures()
    decision_logic = load_decision_logic()

    # Extract data
    quant_data = extract_quantitative_data(architectures)
    spider_data = extract_spider_data(architectures, quant_data)
    chart_data = extract_chart_data(architectures)

    # Build output JSON
    output = {
        "metadata": {
            "version": "1.1.0",
            "generated": "2025-10-15",
            "source_files": [
                str(ARCHITECTURES_YAML),
                str(DECISION_LOGIC_YAML),
                "artifacts/bom/*.csv"
            ],
            "note": "Costs from BOM CSV files. Timelines = max(parts leadtime) + assembly + certification from parts.csv and architectures.yaml."
        },
        "architectures": {
            arch['id']: {
                "id": arch['id'],
                "name": arch.get('name', arch['id']),
                "nickname": arch.get('nickname', ''),
                "color": ARCH_COLORS[arch['id']],
            }
            for arch in architectures
        },
        "spider_chart": {
            "dimensions": [
                "Cost (lower better)",
                "Timeline (faster better)",
                "UX/Usability",
                "Manufacturability",
                "Robustness",
                "Supply Chain (lower risk)",
                "Power Efficiency (lower better)",
                "Simplicity (lower complexity)",
            ],
            "data": spider_data,
        },
        "cost_chart": chart_data["cost_chart"],
        "timeline_chart": chart_data["timeline_chart"],
        "actuator_assumptions": chart_data["actuator_assumptions"],
        "decision_tree": decision_logic.get('decision_tree', []),
        "architecture_win_conditions": decision_logic.get('architecture_win_conditions', {}),
        "key_insight": decision_logic.get('key_insight', {}),
    }

    # Write JSON
    print(f"\nWriting output: {OUTPUT_JSON}")
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(output, f, indent=2)

    print("\n" + "="*60)
    print("✓ DATA EXTRACTION COMPLETE")
    print("="*60)
    print(f"\nOutput file: {OUTPUT_JSON.absolute()}")
    print(f"Size: {OUTPUT_JSON.stat().st_size} bytes")
    print("\nNext step: python3 scripts/generate_tradeoff_charts.py")
    print()


if __name__ == "__main__":
    main()
