#!/usr/bin/env python3
"""
Generate trade-off analysis charts from architectures.yaml

This script reads architecture data and generates presentation-ready visualizations:
- Spider/radar chart showing relative strengths across 8 dimensions
- Bar charts for quantitative comparisons (cost, timeline, weight, power)
- Decision tree diagram showing "When X Wins" scenarios

Usage:
    python3 scripts/generate_tradeoff_charts.py

Outputs:
    source/images/architecture-radar-comparison.png
    source/images/architecture-cost-comparison.png
    source/images/architecture-timeline-comparison.png
    source/images/architecture-decision-tree.png
"""

import yaml
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Configuration
ARCHITECTURES_YAML = Path("source/architectures.yaml")
OUTPUT_DIR = Path("source/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Color scheme for each architecture (presentation-friendly)
ARCH_COLORS = {
    "ARCH_PIEZO_ECO": "#2E86AB",  # Blue - economy/standard
    "ARCH_SOL_ECO": "#A23B72",    # Purple - mechanical innovation
    "ARCH_PIEZO_DLX": "#F18F01",  # Orange - premium/deluxe
}

# Qualitative rating mapping (simplified to 3 levels)
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
    Parse qualitative rating data - handles both strings and dicts

    Examples:
        "BEST" → 10
        {"setup": "BEST", "convenience": "FAIR"} → 7.5 (average)
    """
    if not rating_data:
        return 5  # Default to middle if missing

    # Handle dict ratings (compute average of sub-ratings)
    if isinstance(rating_data, dict):
        scores = []
        for value in rating_data.values():
            # Recursively parse each sub-rating
            if isinstance(value, (str, dict)):
                scores.append(parse_qualitative_rating(value))
        return sum(scores) / len(scores) if scores else 5

    # Handle string ratings
    if not isinstance(rating_data, str):
        return 5  # Unknown type

    rating_str = rating_data.upper()

    # Extract rating keyword (EXCELLENT, GOOD, FAIR, POOR, etc.)
    for keyword, score in RATING_MAP.items():
        if keyword in rating_str:
            return score

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
            return score

    # Fallback: map emojis (if present)
    if "💚" in rating_data:  # Green = excellent
        return 9
    elif "💛" in rating_data:  # Yellow = good
        return 7
    elif "🟠" in rating_data or "🧡" in rating_data:  # Orange = fair
        return 5
    elif "🔴" in rating_data or "❤️" in rating_data:  # Red = poor
        return 3

    return 5  # Default middle rating


def normalize_to_scale(value, min_val, max_val, lower_is_better=False):
    """
    Normalize a value to 0-10 scale

    Args:
        value: Raw value to normalize
        min_val: Minimum value in dataset
        max_val: Maximum value in dataset
        lower_is_better: If True, invert scale (e.g., for cost, timeline)

    Returns:
        Normalized score 0-10
    """
    if max_val == min_val:
        return 5  # All same, return middle

    normalized = (value - min_val) / (max_val - min_val) * 10

    if lower_is_better:
        normalized = 10 - normalized  # Invert: lower cost = higher score

    return normalized


def load_architectures():
    """Load and parse architectures.yaml"""
    with open(ARCHITECTURES_YAML, 'r') as f:
        data = yaml.safe_load(f)

    architectures_dict = data.get('architectures', {})

    # Convert dictionary to list and extract relevant architectures
    active_archs = []
    for arch_id, arch_data in architectures_dict.items():
        if arch_id in ARCH_COLORS:  # Only process architectures we have colors for
            # Add 'id' field to arch_data if not present
            arch_data['id'] = arch_id
            active_archs.append(arch_data)

    return active_archs


def extract_spider_data(architectures):
    """
    Extract 8 dimensions for spider chart from architectures

    Dimensions:
    1. Cost (lower is better - inverted)
    2. Timeline (lower is better - inverted)
    3. UX/Usability (qualitative)
    4. Manufacturability (qualitative)
    5. Robustness/Reliability (qualitative)
    6. Supply Chain Risk (qualitative - inverted)
    7. Power Efficiency (lower is better - inverted)
    8. Complexity (lower is better - inverted)

    Returns:
        dict: {arch_id: [8 scores on 0-10 scale]}
    """
    # Collect raw data
    costs = []
    timelines = []
    powers = []

    for arch in architectures:
        quant = arch.get('quantitative', {})

        # Parse cost (e.g., "$420" → 420)
        cost_str = quant.get('bom_cost_pilot', '0')
        cost = float(cost_str.replace('$', '').replace(',', ''))
        costs.append(cost)

        # Parse timeline (e.g., "8-10" → 9 average)
        timeline_str = quant.get('timeline_weeks', '8')
        if '-' in timeline_str:
            low, high = timeline_str.split('-')
            timeline = (float(low) + float(high)) / 2
        else:
            timeline = float(timeline_str)
        timelines.append(timeline)

        # Parse power (e.g., "1.47" → 1.47)
        power = float(quant.get('power_avg_w', 0))
        powers.append(power)

    # Find min/max for normalization
    cost_min, cost_max = min(costs), max(costs)
    timeline_min, timeline_max = min(timelines), max(timelines)
    power_min, power_max = min(powers), max(powers)

    # Build spider data for each architecture
    spider_data = {}

    for i, arch in enumerate(architectures):
        arch_id = arch.get('id')
        quant = arch.get('quantitative', {})
        qual = arch.get('qualitative', {})

        # Extract raw values
        cost = costs[i]
        timeline = timelines[i]
        power = powers[i]

        # Normalize quantitative (lower is better - invert)
        cost_score = normalize_to_scale(cost, cost_min, cost_max, lower_is_better=True)
        timeline_score = normalize_to_scale(timeline, timeline_min, timeline_max, lower_is_better=True)
        power_score = normalize_to_scale(power, power_min, power_max, lower_is_better=True)

        # Parse qualitative ratings
        ux_score = parse_qualitative_rating(qual.get('ux', ''))
        mfg_score = parse_qualitative_rating(qual.get('manufacturability', ''))
        robust_score = parse_qualitative_rating(qual.get('robustness', ''))
        supply_score = 10 - parse_qualitative_rating(qual.get('supply_chain_risk', ''))  # Invert: low risk = high score
        complexity_score = 10 - parse_qualitative_rating(qual.get('complexity', ''))  # Invert: low complexity = high score

        # Build 8-dimension array
        spider_data[arch_id] = [
            cost_score,
            timeline_score,
            ux_score,
            mfg_score,
            robust_score,
            supply_score,
            power_score,
            complexity_score,
        ]

    return spider_data


def generate_spider_chart(spider_data, output_path):
    """
    Generate spider/radar chart comparing architectures across 8 dimensions
    """
    # Dimension labels
    dimensions = [
        'Cost\n(lower better)',
        'Timeline\n(faster better)',
        'UX/Usability',
        'Manufacturability',
        'Robustness',
        'Supply Chain\n(lower risk)',
        'Power Efficiency\n(lower better)',
        'Simplicity\n(lower complexity)',
    ]

    num_vars = len(dimensions)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

    # Plot each architecture
    for arch_id, scores in spider_data.items():
        scores_plot = scores + scores[:1]  # Complete the circle
        color = ARCH_COLORS[arch_id]
        ax.plot(angles, scores_plot, 'o-', linewidth=2, label=arch_id, color=color)
        ax.fill(angles, scores_plot, alpha=0.15, color=color)

    # Styling
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, size=10)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], size=8)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Title and legend
    plt.title('Architecture Trade-off Comparison\n(8 Key Dimensions)',
              size=16, weight='bold', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11)

    # Save
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Generated spider chart: {output_path}")


def generate_cost_chart(architectures, output_path):
    """
    Generate bar chart comparing BOM costs across architectures
    """
    arch_names = []
    costs = []

    for arch in architectures:
        arch_id = arch.get('id')
        # Shorten names for chart
        short_name = arch_id.replace('ARCH_', '').replace('_', ' ')
        arch_names.append(short_name)

        # Parse cost
        cost_str = arch.get('quantitative', {}).get('bom_cost_pilot', '0')
        cost = float(cost_str.replace('$', '').replace(',', ''))
        costs.append(cost)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar chart
    colors = [ARCH_COLORS[arch['id']] for arch in architectures]
    bars = ax.bar(arch_names, costs, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels on bars
    for bar, cost in zip(bars, costs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'${cost:.0f}',
                ha='center', va='bottom', fontsize=12, weight='bold')

    # Styling
    ax.set_ylabel('Pilot BOM Cost (USD)', fontsize=12, weight='bold')
    ax.set_xlabel('Architecture', fontsize=12, weight='bold')
    ax.set_title('BOM Cost Comparison (Pilot Quantity)', fontsize=14, weight='bold', pad=15)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)

    # Format y-axis as currency
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:.0f}'))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Generated cost chart: {output_path}")


def generate_timeline_chart(architectures, output_path):
    """
    Generate bar chart comparing timeline to pilot production
    """
    arch_names = []
    timelines_low = []
    timelines_high = []

    for arch in architectures:
        arch_id = arch.get('id')
        short_name = arch_id.replace('ARCH_', '').replace('_', ' ')
        arch_names.append(short_name)

        # Parse timeline range (e.g., "8-10" → low=8, high=10)
        timeline_str = arch.get('quantitative', {}).get('timeline_weeks', '8')
        if '-' in timeline_str:
            low, high = timeline_str.split('-')
            timelines_low.append(float(low))
            timelines_high.append(float(high))
        else:
            val = float(timeline_str)
            timelines_low.append(val)
            timelines_high.append(val)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar chart with error bars showing range
    colors = [ARCH_COLORS[arch['id']] for arch in architectures]
    timelines_avg = [(low + high) / 2 for low, high in zip(timelines_low, timelines_high)]
    timelines_err = [(high - low) / 2 for low, high in zip(timelines_low, timelines_high)]

    bars = ax.bar(arch_names, timelines_avg, yerr=timelines_err,
                   color=colors, alpha=0.8, edgecolor='black', linewidth=1.5,
                   capsize=10, error_kw={'linewidth': 2, 'ecolor': 'black'})

    # Add value labels on bars
    for i, (bar, low, high) in enumerate(zip(bars, timelines_low, timelines_high)):
        height = bar.get_height()
        if low == high:
            label = f'{low:.0f} wks'
        else:
            label = f'{low:.0f}-{high:.0f} wks'
        ax.text(bar.get_x() + bar.get_width()/2., height,
                label,
                ha='center', va='bottom', fontsize=12, weight='bold')

    # Styling
    ax.set_ylabel('Timeline to Pilot Production (Weeks)', fontsize=12, weight='bold')
    ax.set_xlabel('Architecture', fontsize=12, weight='bold')
    ax.set_title('Timeline Comparison (Excluding Actuator Sourcing)', fontsize=14, weight='bold', pad=15)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Generated timeline chart: {output_path}")


def generate_decision_tree(architectures, output_path):
    """
    Generate decision tree diagram showing "When X Wins" scenarios

    This creates a text-based decision tree suitable for presentation slides
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.axis('off')

    # Decision tree structure (manually defined based on architecture strengths)
    tree_text = """
    WHICH ARCHITECTURE SHOULD YOU CHOOSE?
    ═════════════════════════════════════════

    START: What are your constraints?
         │
         ├─── Wireless REQUIRED? ────────────────────► ARCH_PIEZO_DLX
         │                                               (Only BLE option)
         │
         ├─── Cost < $300 target? ───► YES ───────────► ARCH_SOL_ECO
         │                               │                ($277 lowest BOM)
         │                               │
         │                               └─► NO ───────► Continue...
         │
         ├─── Timeline < 8 weeks? ──► YES ───────────► ARCH_PIEZO_ECO
         │                               │                (Fastest to market)
         │                               │
         │                               └─► NO ───────► Continue...
         │
         ├─── Volume > 10K units? ──► YES ───────────► ARCH_SOL_ECO
         │                               │                (Best scaling)
         │                               │
         │                               └─► NO ───────► Continue...
         │
         └─── DEFAULT ────────────────────────────────► ARCH_PIEZO_ECO
                                                         (Most robust)


    KEY INSIGHT: No single "best" architecture
    ═══════════════════════════════════════════════════
    Selection depends on YOUR specific constraints:
    • Wireless requirement → Only PIEZO_DLX has BLE
    • Cost-constrained → SOL_ECO wins ($277 vs $420-442)
    • Time-constrained → PIEZO_ECO fastest (8-10 wks)
    • Volume scaling → SOL_ECO mechanical cost-down potential
    """

    # Display tree text
    ax.text(0.05, 0.95, tree_text,
            transform=ax.transAxes,
            fontsize=11,
            verticalalignment='top',
            fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    # Add color-coded architecture labels
    y_pos = 0.02
    for arch_id, color in ARCH_COLORS.items():
        short_name = arch_id.replace('ARCH_', '')
        patch = mpatches.Patch(color=color, label=short_name)
        ax.add_artist(plt.legend(handles=[patch], loc='lower left',
                                bbox_to_anchor=(0.05 + list(ARCH_COLORS.keys()).index(arch_id) * 0.3, y_pos),
                                fontsize=10, framealpha=0.9))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Generated decision tree: {output_path}")


def main():
    """Main execution"""
    print("\n" + "="*60)
    print("TRADE-OFF ANALYSIS CHART GENERATOR")
    print("="*60 + "\n")

    # Load data
    print(f"Loading architectures from: {ARCHITECTURES_YAML}")
    architectures = load_architectures()
    print(f"Found {len(architectures)} active architectures: {[a['id'] for a in architectures]}\n")

    # Generate charts
    print("Generating charts...\n")

    # 1. Spider/radar chart
    spider_data = extract_spider_data(architectures)
    generate_spider_chart(spider_data, OUTPUT_DIR / "architecture-radar-comparison.png")

    # 2. Cost comparison
    generate_cost_chart(architectures, OUTPUT_DIR / "architecture-cost-comparison.png")

    # 3. Timeline comparison
    generate_timeline_chart(architectures, OUTPUT_DIR / "architecture-timeline-comparison.png")

    # 4. Decision tree
    generate_decision_tree(architectures, OUTPUT_DIR / "architecture-decision-tree.png")

    print("\n" + "="*60)
    print("✓ ALL CHARTS GENERATED SUCCESSFULLY")
    print("="*60)
    print(f"\nOutput directory: {OUTPUT_DIR.absolute()}")
    print("\nFiles created:")
    print(f"  • architecture-radar-comparison.png   (Spider chart - 8 dimensions)")
    print(f"  • architecture-cost-comparison.png    (Bar chart - BOM costs)")
    print(f"  • architecture-timeline-comparison.png (Bar chart - timelines)")
    print(f"  • architecture-decision-tree.png      (Decision framework)")
    print("\n")


if __name__ == "__main__":
    main()
