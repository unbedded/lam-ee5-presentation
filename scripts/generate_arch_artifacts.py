#!/usr/bin/env python3
"""
Generate architecture artifacts from YAML/CSV sources
Part of /arch-gen slash command
"""

import yaml
import csv
from pathlib import Path
from datetime import datetime

# Load source files
def load_sources():
    with open('source/architectures.yaml', 'r') as f:
        archs = yaml.safe_load(f)
    with open('source/subsystems.yaml', 'r') as f:
        subsys = yaml.safe_load(f)
    with open('source/parts.csv', 'r') as f:
        parts = list(csv.DictReader(f))
    return archs, subsys, parts

def get_part_details(subsystem_id, parts_db):
    """Look up part details from parts.csv"""
    # Handle special mappings for subsystems with alternative part numbers
    subsystem_map = {
        'SS-USER-IO': 'SS-USER-IO-BUTTON',
        'SS-PCB': 'SS-PCB-4LAYER',
        'SS-ENCLOSURE': 'SS-ENCLOSURE-3DP',
        'SS-ACTUATOR-DRIVER-2CH': 'SS-ACTUATOR-DRIVER-2CH',  # Keep same
        'SS-ACTUATOR-SOLENOID': 'SS-ACTUATOR-SOLENOID',  # Keep same
        'SS-ACTUATOR-LATCH': 'SS-ACTUATOR-LATCH'  # Keep same
    }

    # Use mapped ID if available
    search_id = subsystem_map.get(subsystem_id, subsystem_id)

    for part in parts_db:
        if part['Subsystem'] == search_id:
            return part
    return None

def calculate_pcb_layers(arch_data, subsys_db):
    """Calculate required PCB layers based on subsystems used"""
    max_layers = 2
    layer_drivers = []

    # Check all subsystems (core + unique)
    all_subsystems = arch_data['subsystems']['core'] + arch_data['subsystems']['unique']

    for ss_id in all_subsystems:
        # Look in both core and unique subsystems
        ss = subsys_db['subsystems_core'].get(ss_id) or subsys_db['subsystems_unique'].get(ss_id)
        if ss and 'pcb_specs' in ss:
            layers = ss['pcb_specs'].get('layers_required', 2)
            if layers >= 4:
                layer_drivers.append(f"{ss_id}: {ss['name']}")
            max_layers = max(max_layers, layers)

    return max_layers, layer_drivers

def calculate_bom_total(arch, subsys, parts):
    """Calculate BOM total by summing parts from subsystems (SSOT from parts.csv)"""
    subtotal = 0

    # Core subsystems
    for ss_id in arch['subsystems']['core']:
        ss = subsys['subsystems_core'].get(ss_id) or subsys['subsystems_unique'].get(ss_id)
        part = get_part_details(ss_id, parts)
        if ss and part:
            qty = ss['quantity']
            unit_price = float(part['Unit_Price_1000'])
            line_total = qty * unit_price
            subtotal += line_total

    # Unique subsystems
    for ss_id in arch['subsystems']['unique']:
        ss = subsys['subsystems_unique'].get(ss_id)
        part = get_part_details(ss_id, parts)
        if ss and part:
            qty = ss['quantity']
            unit_price = float(part['Unit_Price_1000'])
            line_total = qty * unit_price
            subtotal += line_total

    # Add 15% misc overhead
    misc_15pct = subtotal * 0.15
    total = subtotal + misc_15pct

    return {
        'subtotal': subtotal,
        'misc_15pct': misc_15pct,
        'total': total
    }

def format_qualitative(value):
    """Format qualitative ratings with emoji"""
    mapping = {
        'BEST': '💚 BEST',
        'EXCELLENT': '💚 EXCELLENT',
        'LOW': '💚 LOW',
        'SIMPLE': '💚 SIMPLE',
        'TRIVIAL': '💚 TRIVIAL',
        'FASTEST': '💚 FASTEST',
        'SHORT': '💚 SHORT',
        'FAST': '💚 FAST',
        'GOOD': '🟡 GOOD',
        'MEDIUM': '🟡 MEDIUM',
        'MODERATE': '🟡 MODERATE',
        'FAIR': '🟠 FAIR',
        'LOW-MEDIUM': '🟡 LOW-MEDIUM',
        'MEDIUM-HIGH': '🟠 MEDIUM-HIGH',
        'POOR': '🔴 POOR',
        'HIGH': '🔴 HIGH',
        'COMPLEX': '🔴 COMPLEX',
        'SLOW': '🔴 SLOW',
        'NONE': '💚 NONE',
        'SMALL': '💚 SMALL',
        'LIGHT': '💚 LIGHT',
        'LARGE': '🟠 LARGE',
        'VERY LARGE': '🔴 VERY LARGE',
        'HEAVY': '🔴 HEAVY',
        'VERY COMPLEX': '🔴 VERY COMPLEX'
    }
    return mapping.get(value, value)

def generate_architecture_md(archs, subsys, parts):
    """Generate artifacts/architecture.md"""

    output = []
    output.append("# Braille Display - Solution Architectures\n")
    output.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}\n")
    output.append(f"**Source:** source/architectures.yaml v{archs['metadata']['version']}\n\n")

    # Executive Summary
    output.append("## Executive Summary\n\n")
    arch_ids = list(archs['architectures'].keys())
    output.append(f"This document presents {len(arch_ids)} alternative architectures for a 32-character braille display device:\n\n")
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        output.append(f"- **{arch['name']} ({arch_id}):** {arch['market_position']} - Target BOM ${arch['quantitative']['cost']['bom_target']}\n")
    output.append("\n")

    # Architecture Overview Table
    output.append("## Architecture Overview\n\n")
    output.append("| Architecture | Nickname | Market Position | BOM Target | BOM Actual | Timeline |\n")
    output.append("|--------------|----------|-----------------|------------|------------|----------|\n")
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        q = arch['quantitative']
        name = arch['name']
        nickname = arch['nickname']
        market = arch['market_position'].split('/')[0].strip()
        bom_target = f"${q['cost']['bom_target']}"
        # Calculate BOM actual from parts.csv (SSOT)
        bom_calc = calculate_bom_total(arch, subsys, parts)
        bom_actual = f"${bom_calc['total']:.2f}"
        timeline = f"{q['timeline']['total_weeks']} weeks"
        output.append(f"| {arch_id} | {nickname} | {market} | {bom_target} | {bom_actual} | {timeline} |\n")
    output.append("\n---\n\n")

    # Detailed architecture sections
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        output.append(f"## {arch_id}: {arch['name']} - \"{arch['nickname']}\"\n\n")

        # Market Position
        output.append(f"### Market Position\n\n{arch['market_position']}\n\n")

        # Requirements Traceability
        output.append("### Requirements Traceability\n\n")
        for req in arch['driven_by_requirements']:
            output.append(f"- **{req['id']}:** {req.get('scenario', req.get('target', req.get('note', '')))}\n")
        output.append("\n")

        # Subsystem Breakdown
        output.append("### Subsystem Breakdown\n\n")
        output.append("**Core Subsystems (Shared):**\n\n")
        for ss_id in arch['subsystems']['core']:
            ss = subsys['subsystems_core'].get(ss_id) or subsys['subsystems_unique'].get(ss_id)
            part = get_part_details(ss_id, parts)
            if ss and part:
                output.append(f"- **{ss_id}:** {ss['name']} → {part['Digikey_PN']} ({part['MFR']} {part['MFR_PN']})\n")
                output.append(f"  - {ss['description']}\n")
                output.append(f"  - Qty: {part['Qty_Per_Unit']} × {ss['quantity']} = {int(part['Qty_Per_Unit']) * ss['quantity']}\n")
        output.append("\n")

        output.append("**Unique Subsystems (Architecture-Specific):**\n\n")
        for ss_id in arch['subsystems']['unique']:
            ss = subsys['subsystems_unique'].get(ss_id)
            part = get_part_details(ss_id, parts)
            if ss and part:
                output.append(f"- **{ss_id}:** {ss['name']} → {part['Digikey_PN']} ({part['MFR']} {part['MFR_PN']})\n")
                output.append(f"  - {ss['description']}\n")
                output.append(f"  - Qty: {part['Qty_Per_Unit']} × {ss['quantity']}\n")
        output.append("\n")

        # Qualitative Assessment
        output.append("### Qualitative Assessment\n\n")
        qual = arch['qualitative']

        # Cost Profile
        output.append("**Cost Profile:**\n\n")
        for key, val in qual['cost'].items():
            output.append(f"- {key.replace('_', ' ').title()}: {format_qualitative(val)}\n")
        output.append("\n")

        # User Experience
        output.append("**User Experience:**\n\n")
        for key, val in qual['ux'].items():
            output.append(f"- {key.replace('_', ' ').title()}: {format_qualitative(val)}\n")
        output.append("\n")

        # Complexity
        output.append("**Complexity:**\n\n")
        for key, val in qual['complexity'].items():
            output.append(f"- {key.replace('_', ' ').title()}: {format_qualitative(val)}\n")
        output.append("\n")

        # Timeline
        output.append("**Timeline:**\n\n")
        for key, val in qual['timeline'].items():
            output.append(f"- {key.replace('_', ' ').title()}: {format_qualitative(val)}\n")
        output.append("\n")

        # Manufacturing
        output.append("**Manufacturing:**\n\n")
        for key, val in qual['manufacturing'].items():
            output.append(f"- {key.replace('_', ' ').title()}: {format_qualitative(val)}\n")
        output.append("\n")

        # Risk
        output.append("**Risk:**\n\n")
        for key, val in qual['risk'].items():
            output.append(f"- {key.replace('_', ' ').title()}: {format_qualitative(val)}\n")
        output.append("\n")

        # Market Fit
        output.append("**Market Fit:**\n\n")
        for key, val in qual['market_fit'].items():
            output.append(f"- {key.replace('_', ' ').title()}: {format_qualitative(val)}\n")
        output.append("\n")

        # Quantitative Metrics
        output.append("### Quantitative Metrics\n\n")
        quant = arch['quantitative']

        output.append("**Cost:**\n\n")
        c = quant['cost']
        # Calculate BOM from parts.csv (SSOT)
        bom_calc = calculate_bom_total(arch, subsys, parts)
        output.append(f"- BOM Subtotal: ${bom_calc['subtotal']:.2f}\n")
        output.append(f"- Misc 15%: ${bom_calc['misc_15pct']:.2f}\n")
        output.append(f"- **BOM Total: ${bom_calc['total']:.2f}** (Target: ${c['bom_target']}, Range: ${c['bom_range_min']}-${c['bom_range_max']})\n")
        gap = bom_calc['total'] - c['bom_target']
        gap_pct = (gap / c['bom_target']) * 100
        output.append(f"- **Cost Gap: ${gap:.2f} ({gap_pct:.0f}% over target)** ⚠️\n")
        output.append(f"- Certification: ${c['certification_cost']:,}\n")
        output.append(f"- NRE Total: ${c['nre_total']:,}\n\n")

        output.append("**Size & Weight:**\n\n")
        s = quant['size']
        output.append(f"- Dimensions: {s['length_mm']}×{s['width_mm']}×{s['height_mm']} mm ({s['length_mm']/25.4:.1f}×{s['width_mm']/25.4:.1f}×{s['height_mm']/25.4:.1f} in)\n")
        output.append(f"- Weight: {s['weight_lbs']:.2f} lbs ({s['weight_grams']}g)\n\n")

        output.append("**Performance:**\n\n")
        p = quant['performance']
        output.append(f"- Refresh Speed: {p['refresh_speed_sec']} seconds\n")
        if p['battery_life_hrs']:
            output.append(f"- Battery Life: {p['battery_life_hrs']} hours\n")
        else:
            output.append(f"- Battery Life: N/A (bus-powered)\n")
        output.append(f"- Power Consumption: {p['power_consumption_watts']} watts\n\n")

        output.append("**Timeline:**\n\n")
        t = quant['timeline']
        output.append(f"- Design: {t['design_weeks']} weeks | Prototype: {t['prototype_weeks']} weeks | Pilot: {t['pilot_production_weeks']} weeks\n")
        output.append(f"- **Total: {t['total_weeks']} weeks** | Certification: {t['certification_weeks']} weeks\n\n")

        output.append("**Manufacturing:**\n\n")
        m = quant['manufacturing']
        output.append(f"- Component Count: {m['component_count']}\n")
        output.append(f"- Assembly Time: {m['assembly_time_min']} min/unit\n")
        output.append(f"- Yield Estimate: {m['yield_estimate']*100:.0f}%\n\n")

        # Trade-offs (if present, like ARCH-D)
        if 'trade_offs' in arch:
            output.append("### Trade-offs\n\n")
            to = arch['trade_offs']
            output.append("**Pros:**\n\n")
            for pro in to['pros']:
                output.append(f"- {pro}\n")
            output.append("\n**Cons:**\n\n")
            for con in to['cons']:
                output.append(f"- {con}\n")
            output.append(f"\n**Recommendation:** {to['recommendation']}\n\n")

        output.append("---\n\n")

    # Architecture Comparison Matrix
    output.append("## Architecture Comparison Matrix\n\n")

    # Precompute BOM totals for all architectures
    bom_totals = {}
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        bom_calc = calculate_bom_total(arch, subsys, parts)
        bom_totals[arch_id] = bom_calc['total']

    # Cost Comparison
    output.append("### Cost Comparison\n\n")
    header = "| Metric | " + " | ".join(arch_ids) + " |\n"
    sep = "|--------|" + "|".join(["---------" for _ in arch_ids]) + "|\n"
    output.append(header)
    output.append(sep)

    # BOM Target row
    row_values = []
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        c = arch['quantitative']['cost']
        row_values.append(f"${c['bom_target']}")
    output.append(f"| BOM Target | {' | '.join(row_values)} |\n")

    # BOM Actual row
    row_values = []
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        c = arch['quantitative']['cost']
        bom_total = bom_totals[arch_id]
        gap_pct = ((bom_total - c['bom_target']) / c['bom_target']) * 100
        row_values.append(f"${bom_total:.2f} ({gap_pct:.0f}% over) ⚠️")
    output.append(f"| BOM Actual | {' | '.join(row_values)} |\n")

    # Certification row
    row_values = []
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        c = arch['quantitative']['cost']
        row_values.append(f"${c['certification_cost']/1000:.0f}K")
    output.append(f"| Certification | {' | '.join(row_values)} |\n")

    # NRE Total row
    row_values = []
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        c = arch['quantitative']['cost']
        row_values.append(f"${c['nre_total']/1000:.0f}K")
    output.append(f"| NRE Total | {' | '.join(row_values)} |\n")

    output.append("\n")

    # Cost Gap Analysis
    output.append("## Cost Gap Analysis\n\n")
    output.append("**All architectures currently OVER BOM target:**\n\n")
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        c = arch['quantitative']['cost']
        bom_total = bom_totals[arch_id]
        gap = bom_total - c['bom_target']
        gap_pct = (gap / c['bom_target']) * 100
        output.append(f"- **{arch_id}:** ${bom_total:.2f} actual vs ${c['bom_target']} target → **${gap:.2f} gap ({gap_pct:.0f}% over)**\n")
    output.append("\n")

    # Find actuator cost from parts database
    actuator_cost = 0
    for part in parts:
        if part['Subsystem'] == 'SS-ACTUATOR':
            actuator_cost = float(part['Unit_Price_100']) * 192
            break

    output.append(f"**Primary cost driver:** SS-ACTUATOR (${actuator_cost:.2f} for 192× actuators)\n\n")
    output.append("**Cost reduction strategies (for v1.4.0 Trade-off Analysis):**\n\n")
    output.append("1. Negotiate actuator volume pricing (currently using 100-qty, need 1K+ quotes)\n")
    output.append("2. Reduce cell count (32→24 cells = 25% actuator savings)\n")
    output.append("3. Alternative actuator technologies (solenoid + latch = $96 vs piezo $288, see ARCH-D)\n")
    output.append("4. Value engineering (2-layer PCB where possible, simpler enclosure)\n\n")

    # PCB Design Requirements
    output.append("---\n\n")
    output.append("## PCB Design Requirements by Architecture\n\n")
    output.append("| Architecture | Layers | Key Drivers | Min Trace | HV Clearance | Max Emissions |\n")
    output.append("|--------------|--------|-------------|-----------|--------------|---------------|\n")
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        layers, drivers = calculate_pcb_layers(arch, subsys)

        # Determine HV voltage based on subsystems
        hv_voltage = "30V" if any('30V' in d for d in drivers) else ("12V" if any('12V' in d for d in drivers) else "5V")
        hv_clearance = "50 mil" if hv_voltage == "30V" else "20 mil"

        # Determine max emissions
        has_ble = any('BLE' in ss_id for ss_id in arch['subsystems']['unique'])
        max_freq = "2440 MHz" if has_ble else "168 MHz"

        # Get driver summary
        driver_summary = []
        if any('STM32' in d for d in drivers):
            driver_summary.append("STM32F4 (168 MHz)")
        if any('DRIVER' in d for d in drivers):
            driver_summary.append(f"{hv_voltage} drivers")
        if any('USB' in d for d in drivers):
            driver_summary.append("USB")
        if has_ble:
            driver_summary.append("BLE (2.4 GHz)")
        if any('BOOST' in d for d in drivers):
            driver_summary.append("boost conv")

        driver_str = ", ".join(driver_summary) if driver_summary else "basic logic"

        output.append(f"| {arch_id} ({arch['name']}) | {layers}-layer | {driver_str} | 6 mil | {hv_clearance} | {max_freq} |\n")

    output.append("\n**Layer Stack (all 4-layer architectures):**\n\n")
    output.append("- Layer 1 (Top): Signal routing (6 mil min trace/space for MCU fanout)\n")
    output.append("- Layer 2 (GND): Continuous ground plane (FCC Part 15B requirement)\n")
    output.append("- Layer 3 (Power): Isolated planes for 30V / 12V / 5V / 3.3V\n")
    output.append("- Layer 4 (Bottom): Signal routing\n\n")
    output.append("**Cost Impact:** 4-layer PCB ~$15 vs 2-layer ~$8 (but 2-layer would fail FCC emissions)\n\n")

    # Block Diagrams
    output.append("---\n\n")
    output.append("## Block Diagrams\n\n")
    for arch_id in arch_ids:
        arch = archs['architectures'][arch_id]
        if 'block_diagram_path' in arch:
            output.append(f"- **{arch_id}:** {arch['block_diagram_path']}\n")
    output.append("\n")

    # Next Steps
    output.append("---\n\n")
    output.append("## Next Steps (v1.4.0 Trade-off Analysis)\n\n")
    output.append("1. **Cost optimization:** Address $200-300 BOM gap across all architectures\n")
    output.append("2. **Vendor quotes:** Get real pricing for piezo actuators (TBD-PIEZO-01) and solenoids (TBD-SOLENOID-01)\n")
    output.append("3. **Trade-off analysis:** Document decision rationale for final recommendation\n")
    output.append("4. **Risk mitigation:** Plan for supply chain, certification timeline risks\n")
    output.append("5. **Prototype validation:** Validate ARCH-D latch mechanism (Week 3-4)\n\n")

    return ''.join(output)

def generate_bom_csv(arch_id, arch, subsys, parts):
    """Generate BOM CSV for a specific architecture"""

    rows = []
    rows.append(['Line', 'Subsystem_ID', 'Subsystem_Name', 'Digikey_PN', 'MFR', 'MFR_PN', 'Description',
                 'Qty', 'Unit_Price_1000', 'Line_Total', 'Leadtime_Weeks', 'ROHS', 'Notes'])

    line_num = 1
    subtotal = 0

    # Core subsystems (check both subsystems_core and subsystems_unique)
    for ss_id in arch['subsystems']['core']:
        ss = subsys['subsystems_core'].get(ss_id) or subsys['subsystems_unique'].get(ss_id)
        part = get_part_details(ss_id, parts)
        if ss and part:
            qty = ss['quantity']
            # Use production volume pricing (Unit_Price_1000) instead of pilot (Unit_Price_100)
            unit_price = float(part['Unit_Price_1000'])
            unit_price_pilot = float(part['Unit_Price_100'])
            line_total = qty * unit_price
            subtotal += line_total

            rows.append([
                str(line_num),
                ss_id,
                ss['name'],
                part['Digikey_PN'],
                part['MFR'],
                part['MFR_PN'],
                part['Description'],
                str(qty),
                f"{unit_price:.2f}",
                f"{line_total:.2f}",
                part['Leadtime_Weeks'],
                part['ROHS'],
                part.get('Notes', '')
            ])
            line_num += 1

    # Unique subsystems
    for ss_id in arch['subsystems']['unique']:
        ss = subsys['subsystems_unique'].get(ss_id)
        part = get_part_details(ss_id, parts)
        if ss and part:
            qty = ss['quantity']
            # Use production volume pricing (Unit_Price_1000) instead of pilot (Unit_Price_100)
            unit_price = float(part['Unit_Price_1000'])
            unit_price_pilot = float(part['Unit_Price_100'])
            line_total = qty * unit_price
            subtotal += line_total

            rows.append([
                str(line_num),
                ss_id,
                ss['name'],
                part['Digikey_PN'],
                part['MFR'],
                part['MFR_PN'],
                part['Description'],
                str(qty),
                f"{unit_price:.2f}",
                f"{line_total:.2f}",
                part['Leadtime_Weeks'],
                part['ROHS'],
                part.get('Notes', '')
            ])
            line_num += 1

    # Subtotal, misc, total
    misc_15pct = subtotal * 0.15
    total = subtotal + misc_15pct

    rows.append(['---', '---', '---', '---', '---', '---', 'SUBTOTAL', '---', '---', f"{subtotal:.2f}", '---', '---', '---'])
    rows.append(['---', '---', '---', '---', '---', '---', 'Misc 15%', '---', '---', f"{misc_15pct:.2f}", '---', '---', 'Passives, connectors'])
    rows.append(['---', '---', '---', '---', '---', '---', 'TOTAL', '---', '---', f"{total:.2f}", '---', '---', '---'])

    return rows

def generate_comparison_matrix(archs):
    """Generate architecture-comparison-matrix.md"""

    output = []
    output.append("# Architecture Comparison Matrix\n\n")
    output.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}\n")
    output.append(f"**Source:** source/architectures.yaml v{archs['metadata']['version']}\n\n")

    arch_ids = list(archs['architectures'].keys())

    # Iterate through comparison dimensions
    for dim in archs['comparison_dimensions']:
        output.append(f"## {dim['category']}\n\n")

        # Qualitative
        if dim['qualitative']:
            output.append("### Qualitative\n\n")
            header = "| Metric | " + " | ".join(arch_ids) + " |\n"
            sep = "|--------|" + "|".join(["---------" for _ in arch_ids]) + "|\n"
            output.append(header)
            output.append(sep)

            for metric in dim['qualitative']:
                row = [metric.replace('_', ' ').title()]
                for arch_id in arch_ids:
                    arch = archs['architectures'][arch_id]
                    # Navigate nested qualitative structure
                    category_key = dim['category'].lower().replace(' & ', '_').replace(' ', '_')
                    if category_key == 'user_experience':
                        category_key = 'ux'
                    value = arch['qualitative'].get(category_key, {}).get(metric, 'N/A')
                    row.append(format_qualitative(value))
                output.append(f"| {' | '.join(row)} |\n")
            output.append("\n")

        # Quantitative
        if dim['quantitative']:
            output.append("### Quantitative\n\n")
            header = "| Metric | " + " | ".join(arch_ids) + " |\n"
            sep = "|--------|" + "|".join(["---------" for _ in arch_ids]) + "|\n"
            output.append(header)
            output.append(sep)

            for metric in dim['quantitative']:
                row = [metric.replace('_', ' ').title()]
                for arch_id in arch_ids:
                    arch = archs['architectures'][arch_id]
                    # Navigate nested quantitative structure
                    category_key = dim['category'].lower().replace(' & ', '_').replace(' ', '_')
                    value = None

                    # Special handling for different categories
                    if category_key == 'cost':
                        value = arch['quantitative']['cost'].get(metric)
                    elif category_key == 'size_weight':
                        value = arch['quantitative']['size'].get(metric)
                    elif category_key == 'user_experience':
                        value = arch['quantitative']['performance'].get(metric)
                    elif category_key == 'complexity':
                        value = arch['quantitative']['manufacturing'].get(metric)
                    elif category_key == 'timeline':
                        value = arch['quantitative']['timeline'].get(metric)
                    elif category_key == 'manufacturing':
                        value = arch['quantitative']['manufacturing'].get(metric)

                    if value is not None:
                        if isinstance(value, (int, float)):
                            if 'cost' in metric or 'bom' in metric:
                                row.append(f"${value:,.2f}" if value < 1000 else f"${value/1000:.0f}K")
                            elif 'pct' in metric or 'estimate' in metric:
                                row.append(f"{value*100:.0f}%")
                            else:
                                row.append(f"{value}")
                        else:
                            row.append(str(value))
                    else:
                        row.append('N/A')
                output.append(f"| {' | '.join(row)} |\n")
            output.append("\n")

        output.append("---\n\n")

    return ''.join(output)

def main():
    print("Loading source files...")
    archs, subsys, parts = load_sources()

    print("Generating artifacts/architecture.md...")
    arch_md = generate_architecture_md(archs, subsys, parts)
    Path('artifacts').mkdir(exist_ok=True)
    with open('artifacts/architecture.md', 'w') as f:
        f.write(arch_md)
    print(f"✅ Generated artifacts/architecture.md ({len(arch_md)/1024:.1f} KB)")

    print("\nGenerating BOMs...")
    Path('artifacts/bom').mkdir(exist_ok=True)

    # Generate filename from architecture ID (e.g., ARCH_PIEZO_ECO → arch-piezo-eco-bom.csv)
    arch_list = []
    for arch_id in archs['architectures'].keys():
        filename = arch_id.lower().replace('_', '-') + '-bom.csv'
        arch_list.append((arch_id, filename))

    bom_summary = []
    for arch_id, filename in arch_list:
        arch = archs['architectures'][arch_id]
        rows = generate_bom_csv(arch_id, arch, subsys, parts)

        filepath = f'artifacts/bom/{filename}'
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        # Get totals for summary
        total = float(rows[-1][-4])
        bom_summary.append(f"  - {arch_id} ({arch['name']}): ${total:.2f}")
        print(f"✅ Generated {filepath} ({len(rows)} lines)")

    print("\nGenerating artifacts/architecture-comparison-matrix.md...")
    comp_md = generate_comparison_matrix(archs)
    with open('artifacts/architecture-comparison-matrix.md', 'w') as f:
        f.write(comp_md)
    print(f"✅ Generated artifacts/architecture-comparison-matrix.md ({len(comp_md)/1024:.1f} KB)")

    print("\n" + "="*70)
    print("📊 BOM Summary:")
    for line in bom_summary:
        print(line)
    print("\n⚠️  Cost Gap: All architectures over BOM target (primary driver: actuators)")
    print("="*70)

if __name__ == '__main__':
    main()
