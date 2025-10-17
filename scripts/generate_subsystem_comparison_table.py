#!/usr/bin/env python3
"""
Generate subsystem comparison table showing key differences between architectures

This creates a visual comparison showing which architectures use which subsystems,
especially highlighting communication (BLE vs USB) and power (Li-ion, AA, USB) differences.

Outputs:
    source/images/subsystem-comparison-table.png
"""

import yaml
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Configuration
OUTPUT_DIR = Path("source/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "subsystem-comparison-table.png"

# Load architectures
with open('source/architectures.yaml', 'r') as f:
    archs = yaml.safe_load(f)

# Define key subsystems to compare (unique differences)
key_subsystems = [
    ('Communication', [
        ('SS-COMM-USB', 'USB-C (Wired)'),
        ('SS-COMM-BLE', 'BLE Wireless'),
    ]),
    ('Power Source', [
        ('SS-POWER-USB-LDO', 'USB Bus-Powered'),
        ('SS-POWER-USB-BOOST', 'USB + Boost (30V)'),
        ('SS-POWER-AA-HOLDER', 'AA Batteries (4×)'),
        ('SS-POWER-AA-BOOST-3V3', 'AA Boost (3.3V)'),
        ('SS-POWER-AA-BOOST-12V', 'AA Boost (12V)'),
        ('SS-POWER-LIION-CELL', 'Li-ion Battery'),
        ('SS-POWER-LIION-CHARGER', 'Li-ion Charger'),
        ('SS-POWER-LIION-PROTECTION', 'Li-ion Protection'),
        ('SS-POWER-LIION-GAUGE', 'Li-ion Fuel Gauge'),
    ]),
    ('Actuator Type', [
        ('SS-ACTUATOR', 'Piezo (192×)'),
        ('SS-ACTUATOR-SOLENOID', 'Solenoid (192×)'),
        ('SS-ACTUATOR-CAM', 'Rotary Cam Mechanism'),
    ]),
]

# Architecture order
arch_ids = ['ARCH_PIEZO_ECO', 'ARCH_SOL_ECO', 'ARCH_PIEZO_DLX']
arch_names = [
    'Piezo Economy\n(Wired)',
    'Solenoid Economy\n(Rotary Cam)',
    'Piezo Deluxe\n(Wireless)'
]

# Build comparison matrix
comparison_data = []

for category, subsystems in key_subsystems:
    comparison_data.append((category, None, None, None, None))  # Category header

    for ss_id, ss_name in subsystems:
        row = [ss_name]
        for arch_id in arch_ids:
            arch = archs['architectures'][arch_id]
            all_subsystems = arch['subsystems']['core'] + arch['subsystems']['unique']
            has_subsystem = ss_id in all_subsystems
            row.append('✓' if has_subsystem else '')
        comparison_data.append((category, row[0], row[1], row[2], row[3]))

# Create figure
fig, ax = plt.subplots(figsize=(16, 10))
ax.axis('tight')
ax.axis('off')

# Create table data
table_data = []
table_data.append(['Subsystem', 'Piezo Economy\n(Wired)', 'Solenoid Economy\n(Rotary Cam)', 'Piezo Deluxe\n(Wireless)'])

for category, col1, col2, col3, col4 in comparison_data:
    if col1 is None:  # Category header
        table_data.append([f'\n{category}', '', '', ''])
    else:
        table_data.append([col1, col2, col3, col4])

# Create table
table = ax.table(cellText=table_data, cellLoc='left', loc='center',
                bbox=[0, 0, 1, 1])

table.auto_set_font_size(False)
table.set_fontsize(10)

# Style the table
for i, row in enumerate(table_data):
    for j in range(4):
        cell = table[(i, j)]

        # Header row
        if i == 0:
            cell.set_facecolor('#2E86AB')
            cell.set_text_props(weight='bold', color='white', fontsize=11)
            cell.set_height(0.08)

        # Category headers
        elif row[1] == '':
            cell.set_facecolor('#E8E8E8')
            cell.set_text_props(weight='bold', fontsize=11)
            cell.set_height(0.06)

        # Regular rows
        else:
            if j == 0:  # Subsystem name column
                cell.set_facecolor('#F8F8F8')
                cell.set_width(0.4)
            else:
                # Checkmark cells
                if row[j] == '✓':
                    cell.set_facecolor('#D4EDDA')  # Light green
                    cell.set_text_props(weight='bold', fontsize=14, color='#155724')
                else:
                    cell.set_facecolor('#F8D7DA')  # Light red
                    cell.set_text_props(color='#721C24', fontsize=10)

                cell.set_width(0.2)

            cell.set_height(0.05)

        # Add borders
        cell.set_edgecolor('#CCCCCC')
        cell.set_linewidth(1)

# Title
plt.title('Architecture Subsystem Comparison\n(Key Differences: Communication, Power, Actuator)',
         fontsize=14, weight='bold', pad=20)

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#D4EDDA', edgecolor='#CCCCCC', label='✓ = Subsystem Included'),
    mpatches.Patch(facecolor='#F8D7DA', edgecolor='#CCCCCC', label='(empty) = Not Included'),
]
ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.08),
         ncol=2, frameon=False, fontsize=10)

# Add note
fig.text(0.5, 0.02,
         'Note: Core subsystems (MCU, drivers, PCB, enclosure, etc.) are shared across all architectures - only unique differences shown above',
         ha='center', fontsize=8, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.04, 1, 0.98])
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
print(f"✓ Generated: {OUTPUT_FILE}")
