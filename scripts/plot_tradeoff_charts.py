#!/usr/bin/env python3
"""
Plot trade-off analysis charts from extracted JSON data

This script reads pre-extracted data (from extract_tradeoff_data.py) and
generates presentation-ready visualizations.

Purpose: Pure plotting - no data extraction, easier debugging

Usage:
    python3 scripts/plot_tradeoff_charts.py

Inputs:
    data/tradeoff-data.json (from extract_tradeoff_data.py)

Outputs:
    source/images/architecture-radar-comparison.png
    source/images/architecture-cost-comparison.png
    source/images/architecture-timeline-comparison.png
    source/images/architecture-decision-tree.png
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Configuration
INPUT_JSON = Path("data/tradeoff-data.json")
OUTPUT_DIR = Path("source/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    """Load pre-extracted JSON data"""
    print(f"Loading: {INPUT_JSON}")
    with open(INPUT_JSON, 'r') as f:
        data = json.load(f)

    print(f"  Metadata version: {data['metadata']['version']}")
    print(f"  Architectures: {list(data['architectures'].keys())}")
    return data


def generate_spider_chart(data, output_path):
    """
    Generate spider/radar chart from pre-extracted data
    """
    spider_data = data['spider_chart']['data']
    dimensions = data['spider_chart']['dimensions']
    architectures = data['architectures']

    num_vars = len(dimensions)

    # Compute angles
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete circle

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

    # Plot each architecture
    for arch_id, scores in spider_data.items():
        arch_info = architectures[arch_id]
        scores_plot = scores + scores[:1]  # Complete circle
        color = arch_info['color']

        ax.plot(angles, scores_plot, 'o-', linewidth=2,
                label=arch_info['name'], color=color)
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


def generate_cost_chart(data, output_path):
    """
    Generate STACKED bar chart showing BOM cost breakdown by subsystem category
    """
    cost_data = data['cost_chart']
    architectures = data['architectures']
    actuator_assumptions = data.get('actuator_assumptions', {})

    # Extract data (already sorted by JSON: SOL_ECO, PIEZO_ECO, PIEZO_DLX)
    names = []
    arch_ids = []
    breakdowns = []

    for item in cost_data:
        arch_id = item['arch_id']
        arch_ids.append(arch_id)
        short_name = arch_id.replace('ARCH_', '').replace('_', ' ')
        names.append(short_name)
        breakdowns.append(item.get('breakdown', {}))

    # Define subsystem categories and colors
    categories = ['Actuators', 'Control', 'Power', 'Communication', 'Mechanical', 'EMI', 'Misc']
    category_colors = {
        'Actuators': '#E63946',      # Red (biggest cost)
        'Control': '#457B9D',         # Blue
        'Power': '#F1FAEE',           # Light blue
        'Communication': '#A8DADC',   # Cyan
        'Mechanical': '#1D3557',      # Dark blue
        'EMI': '#2A9D8F',             # Teal
        'Misc': '#FFB703'             # Orange (passives, connectors)
    }

    # Extract costs by category
    category_costs = {cat: [] for cat in categories}
    total_costs = []

    for breakdown in breakdowns:
        total = 0
        for cat in categories:
            cost = breakdown.get(cat, 0)
            category_costs[cat].append(cost)
            total += cost
        total_costs.append(total)

    # Create figure
    fig, ax = plt.subplots(figsize=(14, 8))

    # Create stacked bars
    x = np.arange(len(names))
    bar_width = 0.6
    bottom = np.zeros(len(names))

    bars_dict = {}
    for cat in categories:
        costs = category_costs[cat]
        bars = ax.bar(x, costs, bar_width, label=cat, bottom=bottom,
                     color=category_colors[cat], edgecolor='white', linewidth=1.5)
        bars_dict[cat] = bars
        bottom += np.array(costs)

    # Add total cost labels on top
    for i, (total, arch_id) in enumerate(zip(total_costs, arch_ids)):
        ax.text(i, total + 10, f'${total:.0f}',
                ha='center', va='bottom', fontsize=13, weight='bold')

        # Add actuator detail annotation below bar
        if arch_id in actuator_assumptions:
            act = actuator_assumptions[arch_id]
            annotation = f"Act: ${act['unit_price']:.2f}×{act['qty']}"
            ax.text(i, -25, annotation,
                    ha='center', va='top', fontsize=8, style='italic',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.4))

    # Add warning note at bottom
    fig.text(0.5, 0.02,
             '⚠️  Actuator costs are PRELIMINARY assumptions (no COTS found - vendor quotes needed)',
             ha='center', fontsize=10, style='italic', weight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='orange', alpha=0.3))

    # Styling
    ax.set_ylabel('Production BOM Cost (USD)', fontsize=13, weight='bold')
    ax.set_xlabel('Architecture', fontsize=13, weight='bold')
    ax.set_title('BOM Cost Breakdown by Subsystem Category',
                 fontsize=15, weight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=12)
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, p: f'${val:.0f}'))

    # Extend y-axis for annotations
    y_max = max(total_costs)
    ax.set_ylim(-50, y_max * 1.15)

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Generated stacked cost chart: {output_path}")


def generate_timeline_chart(data, output_path):
    """
    Generate STACKED bar chart showing timeline breakdown by phase
    """
    timeline_data = data['timeline_chart']
    architectures = data['architectures']

    # Extract data (already sorted by JSON: SOL_ECO, PIEZO_ECO, PIEZO_DLX)
    names = []
    arch_ids = []
    parts_leadtimes = []
    assembly_times = []
    cert_times = []

    for item in timeline_data:
        arch_id = item['arch_id']
        arch_ids.append(arch_id)
        short_name = arch_id.replace('ARCH_', '').replace('_', ' ')
        names.append(short_name)

        # Extract components
        max_leadtime = item.get('max_leadtime_weeks', 0)
        cert_weeks = item.get('certification_weeks', 0)
        assembly_weeks = item['timeline_low'] - max_leadtime  # timeline_low = leadtime + assembly

        parts_leadtimes.append(max_leadtime)
        assembly_times.append(assembly_weeks)
        cert_times.append(cert_weeks)

    # Define phase colors
    phase_colors = {
        'Parts Leadtime': '#E76F51',      # Orange-red
        'Assembly': '#2A9D8F',             # Teal
        'Certification': '#F4A261'         # Light orange
    }

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))

    # Create stacked bars
    x = np.arange(len(names))
    bar_width = 0.6

    # Stack: Parts -> Assembly -> Certification
    bars_parts = ax.bar(x, parts_leadtimes, bar_width, label='Parts Leadtime (Critical Path)',
                        color=phase_colors['Parts Leadtime'], edgecolor='white', linewidth=1.5)

    bars_assembly = ax.bar(x, assembly_times, bar_width, bottom=parts_leadtimes,
                           label='Assembly & Integration',
                           color=phase_colors['Assembly'], edgecolor='white', linewidth=1.5)

    bottom_with_cert = np.array(parts_leadtimes) + np.array(assembly_times)
    bars_cert = ax.bar(x, cert_times, bar_width, bottom=bottom_with_cert,
                      label='Certification (Parallel)',
                      color=phase_colors['Certification'], edgecolor='white', linewidth=1.5,
                      alpha=0.6, hatch='//')

    # Add timeline range labels on top
    for i, item in enumerate(timeline_data):
        timeline_low = item['timeline_low']
        timeline_high = item['timeline_high']
        total_height = bottom_with_cert[i] + cert_times[i]

        label = f'{timeline_low:.0f}-{timeline_high:.0f} wks'
        ax.text(i, total_height + 1, label,
                ha='center', va='bottom', fontsize=12, weight='bold')

    # Add certification details below each bar
    cert_details = {
        'ARCH_SOL_ECO': 'FCC 15B (wired only)',
        'ARCH_PIEZO_ECO': 'FCC 15B (wired only)',
        'ARCH_PIEZO_DLX': 'FCC 15C + UL 2054 (BLE + Li-ion)'
    }

    for i, arch_id in enumerate(arch_ids):
        cert_detail = cert_details.get(arch_id, '')
        ax.text(i, -2, cert_detail,
                ha='center', va='top', fontsize=8, style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.7))

    # Add subtitle explaining parallel certification
    fig.text(0.5, 0.94,
             'Pilot quantity ~200 units (distributor stock). Certification can run parallel to parts sourcing.',
             ha='center', fontsize=9, style='italic')

    # Styling
    ax.set_ylabel('Timeline to Pilot Production (Weeks)', fontsize=13, weight='bold')
    ax.set_xlabel('Architecture', fontsize=13, weight='bold')
    ax.set_title('Timeline Breakdown: Parts Leadtime + Assembly + Certification',
                 fontsize=14, weight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=11)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)

    # Extend y-axis for annotations
    y_max = max([item['timeline_high'] for item in timeline_data])
    ax.set_ylim(-4, y_max * 1.15)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Generated stacked timeline chart: {output_path}")


def generate_decision_tree(data, output_path):
    """
    Generate decision tree diagram from decision_tree rules
    """
    decision_tree = data.get('decision_tree', [])
    win_conditions = data.get('architecture_win_conditions', {})
    key_insight = data.get('key_insight', {})
    architectures = data['architectures']

    # Build decision tree text from rules
    tree_lines = []
    tree_lines.append("    WHICH ARCHITECTURE SHOULD YOU CHOOSE?")
    tree_lines.append("    ═════════════════════════════════════════")
    tree_lines.append("")
    tree_lines.append("    START: What are your constraints?")
    tree_lines.append("         │")

    # Generate tree from rules
    for i, node in enumerate(decision_tree):
        question = node.get('question', '')
        winner = node.get('winner', '')
        rationale = node.get('rationale', '')
        stop = node.get('stop', False)

        if node.get('condition', {}).get('type') == 'default':
            tree_lines.append(f"         └─── {question} ────────────────────────────────► {winner}")
            tree_lines.append(f"                                                         ({rationale})")
        else:
            tree_lines.append(f"         ├─── {question} ───► YES ───────────► {winner}")
            tree_lines.append(f"         │                               │                ({rationale})")
            tree_lines.append(f"         │                               │")
            tree_lines.append(f"         │                               └─► NO ───────► Continue...")
            tree_lines.append(f"         │")

    tree_lines.append("")
    tree_lines.append("")
    tree_lines.append(f"    {key_insight.get('title', 'KEY INSIGHT')}")
    tree_lines.append("    ═══════════════════════════════════════════════════")

    # Add key insight message
    insight_msg = key_insight.get('message', '').strip()
    for line in insight_msg.split('\n'):
        tree_lines.append(f"    {line}")

    tree_text = "\n".join(tree_lines)

    # Create figure
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.axis('off')

    # Display tree text
    ax.text(0.05, 0.95, tree_text,
            transform=ax.transAxes,
            fontsize=11,
            verticalalignment='top',
            fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    # Add color-coded architecture labels at bottom
    y_pos = 0.02
    for i, (arch_id, arch_info) in enumerate(architectures.items()):
        short_name = arch_id.replace('ARCH_', '')
        color = arch_info['color']
        patch = mpatches.Patch(color=color, label=short_name)
        ax.add_artist(plt.legend(handles=[patch], loc='lower left',
                                bbox_to_anchor=(0.05 + i * 0.3, y_pos),
                                fontsize=10, framealpha=0.9))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"✓ Generated decision tree: {output_path}")


def main():
    """Main execution"""
    print("\n" + "="*60)
    print("TRADE-OFF CHART PLOTTING")
    print("="*60 + "\n")

    # Load pre-extracted data
    data = load_data()

    # Generate charts
    print("\nGenerating charts...\n")

    generate_spider_chart(data, OUTPUT_DIR / "architecture-radar-comparison.png")
    generate_cost_chart(data, OUTPUT_DIR / "architecture-cost-comparison.png")
    generate_timeline_chart(data, OUTPUT_DIR / "architecture-timeline-comparison.png")
    generate_decision_tree(data, OUTPUT_DIR / "architecture-decision-tree.png")

    print("\n" + "="*60)
    print("✓ ALL CHARTS PLOTTED SUCCESSFULLY")
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
