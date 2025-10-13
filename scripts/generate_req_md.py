#!/usr/bin/env python3
"""
Generate requirements.md from source/requirements.yaml
Simplified version focusing on clean output
"""

import yaml
from datetime import datetime

# Load YAML
with open('source/requirements.yaml', 'r') as f:
    data = yaml.safe_load(f)

metadata = data['metadata']
requirements = data['requirements']

# Categorize requirements
ground_truth = []
assumptions = []
standards_reqs = []
mechanical_reqs = []

for req_id, req in requirements.items():
    if '-ASMP' in req_id or '-DRV-' in req_id or '-EXCEPT' in req_id:
        assumptions.append((req_id, req))
    elif req_id.startswith('NFR-'):
        standards_reqs.append((req_id, req))
    elif req_id.startswith('PRD-MECH-'):
        mechanical_reqs.append((req_id, req))
    elif req_id.startswith('PRD-'):
        ground_truth.append((req_id, req))

# Count by priority
p0_count = sum(1 for req in requirements.values() if 'P0-Critical' in req.get('priority', ''))
p1_count = sum(1 for req in requirements.values() if 'P1-High' in req.get('priority', ''))
p2_count = sum(1 for req in requirements.values() if 'P2-Medium' in req.get('priority', ''))

total = len(requirements)

# Generate Markdown
md = f"""# Requirements Analysis - Braille Display Device

**Project:** {metadata['project']}
**Version:** {metadata['version']}
**Date:** {metadata['date']}
**Author:** {metadata['author']}
**Source:** {metadata['source_doc']}

---

## Executive Summary

### Requirements Overview

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Requirements** | **{total}** | **100%** |
| Ground Truth (from PDF) | {len(ground_truth)} | {len(ground_truth)*100//total}% |
| Derived Assumptions | {len(assumptions)} | {len(assumptions)*100//total}% |
| Standards/Compliance | {len(standards_reqs)} | {len(standards_reqs)*100//total}% |
| Mechanical (ADA 703.3) | {len(mechanical_reqs)} | {len(mechanical_reqs)*100//total}% |

### Priority Breakdown

| Priority | Count | Percentage |
|----------|-------|------------|
| 🔴 P0-Critical | {p0_count} | {p0_count*100//total}% |
| 🟠 P1-High | {p1_count} | {p1_count*100//total}% |
| 🟡 P2-Medium | {p2_count} | {p2_count*100//total}% |

### Key Highlights

- **Critical assumption**: "Production" in 2 months = **pilot production** (100-500 units), not mass production
- **Cost target**: $200 ±$100 BOM ($100-$300 range) - **portfolio approach** in v1.3.0
- **Interface**: Portfolio of BLE (wireless) vs USB-C (wired) vs hybrid architectures
- **192 actuators**: 32 cells × 6 dots = most challenging electrical/mechanical design element
- **Actuator size constraint**: ≤2.3mm diameter (derived from 2.5mm pitch requirement from ADA 703.3)
- **Mechanical requirements**: 6 new requirements derived from US ADA Section 703.3 (dot diameter, height, spacing, shape, force)
- **Standards**: North America focus (UL + FCC), with low-risk design approach (4-layer PCB, EMI filtering, pre-certified modules)

---

## Scope & Rationale

### In Scope

"""

for item in metadata['scope']['in_scope']:
    md += f"- {item}\n"

md += "\n### Out of Scope\n\n"
for item in metadata['scope']['out_of_scope']:
    md += f"- {item}\n"

md += f"\n### Rationale\n\n{metadata['rationale']}\n\n---\n\n"

md += """## Ground Truth Requirements (from PDF)

These are requirements **verbatim from the PDF**. Status indicates whether they are directly testable (CLEAR) or require assumptions (VAGUE).

"""

for req_id, req in ground_truth:
    status_emoji = "✅ CLEAR" if req.get('testable') == 'YES' or req.get('status', '').startswith('CLEAR') else "🟠 VAGUE"
    priority_emoji = "🔴" if 'P0' in req.get('priority', '') else "🟠" if 'P1' in req.get('priority', '') else "🟡"

    md += f"### {req_id}: {req['title']}\n\n"
    md += f"**Priority:** {priority_emoji} {req.get('priority', 'N/A')} | **Status:** {status_emoji} | **Category:** {req.get('category', 'N/A')}\n\n"

    if 'pdf_verbatim' in req:
        md += f"**PDF Verbatim:** \"{req['pdf_verbatim']}\"\n\n"

    if 'why_vague' in req:
        md += f"**Why Vague:** {req['why_vague']}\n\n"

    if 'acceptance_criteria' in req:
        md += "**Acceptance Criteria:**\n"
        for criterion in req['acceptance_criteria']:
            md += f"- {criterion}\n"
        md += "\n"

    if 'standards_reference' in req:
        md += "**Standards Reference:**\n"
        for std in req['standards_reference']:
            md += f"- {std}\n"
        md += "\n"

    md += "---\n\n"

md += """## Derived Assumptions (Engineering Specs)

These are **engineering assumptions** to make vague requirements actionable. Each shows derivation process, sensitivity range, and risk level.

"""

for req_id, req in assumptions:
    risk_emoji = {
        'CRITICAL': '🔴',
        'HIGH': '🟠',
        'MEDIUM': '🟡',
        'LOW': '🟢'
    }.get(req.get('risk_level', ''), '⚪')

    priority_emoji = "🔴" if 'P0' in req.get('priority', '') else "🟠" if 'P1' in req.get('priority', '') else "🟡"

    md += f"### {req_id}: {req['title']}\n\n"
    md += f"**Parent:** {req.get('parent', 'N/A')} | **Risk:** {risk_emoji} {req.get('risk_level', 'N/A')} | **Priority:** {priority_emoji} {req.get('priority', 'N/A')}\n\n"

    if 'pdf_says' in req:
        md += f"**PDF Says:** \"{req['pdf_says']}\"\n\n"

    if 'our_assumption' in req:
        md += f"**Our Derived Spec:** {req['our_assumption']}\n\n"

    if 'rationale' in req:
        md += f"**Derivation Process:**\n\n{req['rationale']}\n\n"

    if 'impact_if_wrong' in req:
        md += f"**Impact If Wrong:** {req['impact_if_wrong']}\n\n"

    if 'sensitivity_range' in req:
        md += f"**Sensitivity Range:** {req['sensitivity_range']}\n\n"

    if 'acceptance_criteria' in req:
        md += "**Acceptance Criteria:**\n"
        for criterion in req['acceptance_criteria']:
            md += f"- {criterion}\n"
        md += "\n"

    md += "---\n\n"

md += """## Mechanical Design Requirements (ADA 703.3 Derived)

These requirements are derived from US ADA Section 703.3 braille dimensions standards. They directly constrain actuator selection and mechanical design.

"""

for req_id, req in mechanical_reqs:
    priority_emoji = "🔴" if 'P0' in req.get('priority', '') else "🟠" if 'P1' in req.get('priority', '') else "🟡"

    md += f"### {req_id}: {req['title']}\n\n"
    md += f"**Priority:** {priority_emoji} {req.get('priority', 'N/A')} | **Category:** {req.get('category', 'N/A')} | **Derived From:** {req.get('derived_from', 'N/A')}\n\n"

    if 'requirement' in req:
        md += f"**Requirement:** {req['requirement']}\n\n"

    if 'rationale' in req:
        md += f"**Rationale:**\n\n{req['rationale']}\n\n"

    if 'design_impact' in req:
        md += f"**Design Impact:** {req['design_impact']}\n\n"

    if 'acceptance_criteria' in req:
        md += "**Acceptance Criteria:**\n"
        for criterion in req['acceptance_criteria']:
            md += f"- {criterion}\n"
        md += "\n"

    if 'standards_reference' in req:
        md += f"**Standards Reference:** {req['standards_reference']}\n\n"

    md += "---\n\n"

md += """## Standards & Compliance Requirements

These requirements address regulatory compliance and electromagnetic compatibility for North America market.

"""

for req_id, req in standards_reqs:
    priority_emoji = "🔴" if 'P0' in req.get('priority', '') else "🟠" if 'P1' in req.get('priority', '') else "🟡"

    md += f"### {req_id}: {req['title']}\n\n"
    md += f"**Priority:** {priority_emoji} {req.get('priority', 'N/A')} | **Category:** {req.get('category', 'N/A')}\n\n"

    if 'description' in req:
        md += f"**Description:** {req['description']}\n\n"

    if 'standards' in req:
        md += "**Applicable Standards:**\n"
        for std in req['standards']:
            md += f"- {std}\n"
        md += "\n"

    if 'rationale' in req:
        md += f"**Rationale:**\n\n{req['rationale']}\n\n"

    if 'acceptance_criteria' in req:
        md += "**Acceptance Criteria:**\n"
        for criterion in req['acceptance_criteria']:
            md += f"- {criterion}\n"
        md += "\n"

    if 'cost_impact' in req:
        md += f"**Cost Impact:** {req['cost_impact']}\n\n"

    md += "---\n\n"

md += """## Next Steps

1. **Review Requirements:** Validate completeness with stakeholders
2. **Run Audit:** Execute `/req-audit` to check SMART compliance
3. **Freeze requirements.yaml:** Phase gate review before v1.3.0 (architecture design)
4. **Develop Architecture:** Proceed to v1.3.0 solution architectures (actuator, control, interface options)
5. **Maintain Traceability:** Update `traces_to` fields as designs evolve

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| {metadata['version']} | {metadata['date']} | {metadata['author']} | Added 6 mechanical requirements from ADA 703.3, EMI/standards requirements, updated metadata |

---

## References

- **Source Document:** {metadata['source_doc']}
- **YAML Source (SSOT):** source/requirements.yaml
- **ADA Standards:** reference/standards/braille-dimensions-standards.md

---

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Note:** This is a READ-ONLY generated file. To modify requirements, edit `source/requirements.yaml` and regenerate with `/req-yaml-to-md`.

---

**END OF DOCUMENT**
"""

# Write to file
with open('artifacts/requirements.md', 'w') as f:
    f.write(md)

# Calculate file size
import os
file_size = os.path.getsize('artifacts/requirements.md')
file_size_kb = file_size / 1024

print(f"✅ Requirements Document Generated")
print(f"")
print(f"Total Requirements: {total}")
print(f"File: artifacts/requirements.md")
print(f"Size: {file_size_kb:.1f} KB")
print(f"")
print(f"Breakdown:")
print(f"- Ground Truth (PDF): {len(ground_truth)}")
print(f"- Derived Assumptions: {len(assumptions)}")
print(f"- Standards/Compliance: {len(standards_reqs)}")
print(f"- Mechanical (ADA 703.3): {len(mechanical_reqs)}")
print(f"")
print(f"Priority:")
print(f"- P0-Critical: {p0_count} ({p0_count*100//total}%)")
print(f"- P1-High: {p1_count} ({p1_count*100//total}%)")
print(f"- P2-Medium: {p2_count} ({p2_count*100//total}%)")
print(f"")
print(f"Next: Run /req-audit to validate SMART compliance")
