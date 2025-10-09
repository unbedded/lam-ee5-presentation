---
description: Generate requirements.md from requirements.yaml (YAML→MD)
---

# Requirements YAML to Markdown Generator

Transform `source/requirements.yaml` into human-readable `artifacts/requirements.md` document.

## Your Task

Parse YAML requirements database and generate professionally formatted requirements analysis document.

---

## Step 1: Load Source (1 min)

Read:
- `source/requirements.yaml` - Requirements database (SSOT)
- `docs/requirements-policy.md` - Formatting standards

---

## Step 2: Extract Metadata (30 sec)

From `metadata` section:
- Project name
- Version
- Date
- Author
- Source document

---

## Step 3: Extract Scope & Assumptions (1 min)

From `metadata.scope`:
- In scope items
- Out of scope items
- Assumptions
- Rationale

This goes at the beginning of the document to set context.

---

## Step 4: Parse Requirements by Category (3 min)

**NEW HIERARCHICAL NAMING (v2.0.0):**
- **PRD-SCHED-NNN** → Schedule/Timeline requirements
- **PRD-SIZE-NNN** → Size/Portability requirements
- **PRD-IFACE-NNN** → Interface/Connectivity requirements
- **PRD-COST-NNN** → Cost requirements
- **PRD-VOL-NNN** → Volume/Manufacturing requirements
- **PRD-USER-NNN** → User/Accessibility requirements
- **PRD-FUNC-NNN** → Functional requirements
- **PRD-XXXX-NNN-ASMP** → Assumptions (linked to parent PRD-XXXX-NNN)

**For each requirement, extract:**
- ID (PRD-XXXX-NNN or PRD-XXXX-NNN-ASMP)
- Title
- pdf_verbatim (for ground truth PRD-XXXX-NNN)
- pdf_says + our_assumption (for PRD-XXXX-NNN-ASMP)
- Status (CLEAR or VAGUE)
- Parent (for ASMP, link to PRD-XXXX-NNN)
- Priority
- Category
- Rationale
- risk_level (for ASMP)
- customer_validation_needed (for ASMP)
- sensitivity_range (for ASMP)
- Acceptance criteria
- test_plan (for ASMP)
- impact_if_wrong (for ASMP)
- Any other fields present

---

## Step 5: Generate Document (5 min)

Create professional requirements document in this format:

```markdown
# Requirements Analysis - Braille Display Device

**Project:** [metadata.project]
**Version:** [metadata.version]
**Date:** [metadata.date]
**Author:** [metadata.author]
**Source:** [metadata.source_doc]

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Scope & Rationale](#scope--rationale)
3. [Ground Truth Requirements (PRD)](#ground-truth-requirements-prd)
4. [Assumptions (PRD-XXXX-ASMP)](#assumptions-prd-xxxx-asmp)
5. [Requirements Summary](#requirements-summary)
6. [Standards Compliance](#standards-compliance)
7. [Next Steps](#next-steps)

---

## Executive Summary

### Requirements Overview

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Requirements** | **[X]** | **100%** |
| Ground Truth (from PDF) | [X] | [XX]% |
| Derived Assumptions | [X] | [XX]% |

### Priority Breakdown

| Priority | Count | Percentage |
|----------|-------|------------|
| 🔴 P0-Critical | [X] | [XX]% |
| 🟠 P1-High | [X] | [XX]% |

### Key Highlights

- **Critical assumption**: "Production" in 2 months = **pilot production** (100-500 units), not mass production
- **Cost target**: $200 ±$100 BOM ($100-$300 range) - **portfolio approach** in v1.3.0
- **Interface**: Portfolio of BLE (wireless) vs USB-C (wired) vs hybrid architectures
- **192 actuators**: 32 cells × 6 dots = most challenging electrical/mechanical design element
- **Actuator size constraint**: ≤2.3mm diameter (derived from 2.5mm pitch requirement)
- **Standards**: North America focus (UL + FCC), EU (CE) as future expansion risk

### Quick Navigation

**Ground Truth (PDF Verbatim):**
[PRD-SCHED-001](#prd-sched-001) | [PRD-SIZE-001](#prd-size-001) | [PRD-IFACE-001](#prd-iface-001) | [PRD-COST-001](#prd-cost-001) | [PRD-VOL-001](#prd-vol-001) | [PRD-USER-001](#prd-user-001) | [PRD-FUNC-001](#prd-func-001) | [PRD-FUNC-002](#prd-func-002) | [PRD-FUNC-003](#prd-func-003)

**Derived Assumptions (Engineering Specs):**
[PRD-SCHED-001-ASMP](#prd-sched-001-asmp) | [PRD-SIZE-001-ASMP](#prd-size-001-asmp) | [PRD-IFACE-001-ASMP](#prd-iface-001-asmp) | [PRD-COST-001-ASMP](#prd-cost-001-asmp) | [PRD-VOL-001-ASMP](#prd-vol-001-asmp) | [PRD-FUNC-002-ASMP](#prd-func-002-asmp)

---

## Requirements Hierarchy

<pre style="font-family: 'Courier New', Consolas, Monaco, monospace; font-size: 13px; line-height: 1.4; background-color: #f6f8fa; padding: 16px; border-radius: 6px; border: 1px solid #d0d7de;">
📋 Braille Display Requirements (15 total)
│
├── 📅 PRD-SCHED: Schedule/Timeline (2)
│   ├── <a href="#prd-sched-001">PRD-SCHED-001</a> [Ground Truth] → Two Month Production Release
│   │   └── <a href="#prd-sched-001-asmp">PRD-SCHED-001-ASMP</a> [Derived] → Pilot Production (100-500 units)
│
├── 📏 PRD-SIZE: Size/Portability (2)
│   ├── <a href="#prd-size-001">PRD-SIZE-001</a> [Ground Truth] → Portable Companion Device
│   │   └── <a href="#prd-size-001-asmp">PRD-SIZE-001-ASMP</a> [Derived] → Cell Phone Environment Compatible (≤1.3 lbs)
│
├── 🔌 PRD-IFACE: Interface/Connectivity (2)
│   ├── <a href="#prd-iface-001">PRD-IFACE-001</a> [Ground Truth] → Companion Device to Cell Phone
│   │   └── <a href="#prd-iface-001-asmp">PRD-IFACE-001-ASMP</a> [Derived] → Multi-Interface Strategy (BLE / USB-C / Hybrid)
│
├── 💰 PRD-COST: Cost (2)
│   ├── <a href="#prd-cost-001">PRD-COST-001</a> [Ground Truth] → Low Cost at Volume
│   │   └── <a href="#prd-cost-001-asmp">PRD-COST-001-ASMP</a> [Derived] → BOM Cost Target ($200 ±$100)
│
├── 🏭 PRD-VOL: Volume/Manufacturing (2)
│   ├── <a href="#prd-vol-001">PRD-VOL-001</a> [Ground Truth] → High Volume Production
│   │   └── <a href="#prd-vol-001-asmp">PRD-VOL-001-ASMP</a> [Derived] → 10k units/month SMT Capability
│
├── 👤 PRD-USER: User/Accessibility (1)
│   └── <a href="#prd-user-001">PRD-USER-001</a> [Ground Truth] → Sight-Impaired/Blind User Population
│
└── ⚙️ PRD-FUNC: Functional (4)
    ├── <a href="#prd-func-001">PRD-FUNC-001</a> [Ground Truth] → 32-Cell × 6-Dot Display (192 actuators, ≤2.3mm dia)
    ├── <a href="#prd-func-002">PRD-FUNC-002</a> [Ground Truth] → Braille Line Refresh (Next Line)
    │   └── <a href="#prd-func-002-asmp">PRD-FUNC-002-ASMP</a> [Derived] → <2s Refresh, Tactile Buttons
    └── <a href="#prd-func-003">PRD-FUNC-003</a> [Ground Truth] → Binary Actuation (Raised/Lowered, ≤2.3mm dia)

📊 Statistics:
  • Ground Truth (from PDF): 9 requirements (60%)
  • Derived Assumptions: 6 requirements (40%)
  • Priority: 7 P0-Critical (47%), 8 P1-High (53%)
  • Risk: 1 CRITICAL, 2 HIGH, 3 MEDIUM
</pre>

---

## Scope & Rationale

### In Scope

[List from metadata.scope.in_scope]

### Out of Scope

[List from metadata.scope.out_of_scope]

### Rationale

[metadata.scope.rationale]

---

## Ground Truth Requirements (PRD)

These are requirements **verbatim from the PDF**. Status indicates whether they are directly testable (CLEAR) or require assumptions (VAGUE).

---

### Schedule / Timeline (PRD-SCHED)

#### PRD-SCHED-001: [Title]

|  |  |  |
|---|---|---|
| **Priority:** [🔴 P0 / 🟠 P1] | **Status:** [✅ CLEAR / 🟠 VAGUE - reason] | **Category:** [category] |
| **Testable:** [YES / NO → link to ASMP] | **Source:** [source] | |

**PDF Verbatim:** "[pdf_verbatim]"

**Why Vague:** [why_vague if VAGUE, otherwise omit]

**Acceptance Criteria:** [if CLEAR, list criteria as bullets]

---

### Size / Portability (PRD-SIZE)

[Same compact table format]

### Interface / Connectivity (PRD-IFACE)

[Same compact table format]

### Cost (PRD-COST)

[Same compact table format]

### Volume / Manufacturing (PRD-VOL)

[Same compact table format]

### User / Accessibility (PRD-USER)

[Same compact table format]

### Functional Requirements (PRD-FUNC)

#### PRD-FUNC-001: [Title]

|  |  |  |
|---|---|---|
| **Priority:** 🔴 P0-Critical | **Status:** ✅ CLEAR | **Category:** Function |
| **Testable:** YES | **Source:** [source] | **Actuator Size:** ≤2.3mm dia (derived) |

**PDF Verbatim:** "[pdf_verbatim]"

**Acceptance Criteria:**
- [List criteria including actuator size constraint: ≤2.3mm diameter (derived from 2.5mm pitch minus dot diameter 1.5mm ÷ 2)]

**Standards Reference:** [if applicable]

---

#### PRD-FUNC-003: [Title]

|  |  |  |
|---|---|---|
| **Priority:** 🔴 P0-Critical | **Status:** ✅ CLEAR | **Category:** Function |
| **Testable:** YES | **Source:** [source] | **Actuator Size:** ≤2.3mm dia |

**PDF Verbatim:** "[pdf_verbatim]"

**Acceptance Criteria:**
- [List criteria including actuator size constraint]

**Standards Reference:** [if applicable]

---

## Assumptions (PRD-XXXX-ASMP)

These are **engineering assumptions** to make vague requirements actionable. Each shows derivation process, sensitivity range, and risk level.

---

### PRD-SCHED-001-ASMP: [Title]

|  |  |  |
|---|---|---|
| **Parent:** [link to PRD-SCHED-001] | **Risk:** [🔴 CRITICAL / 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW] | **Priority:** [🔴 P0 / 🟠 P1] |
| **Category:** [category] | **Customer Validation:** [YES/NO] | |

**PDF Says:** "[pdf_says]"

**Our Derived Spec:** "[our_assumption]"

**Derivation Process:**

[rationale - show HOW we got from vague PDF to specific assumption]

**Risk Level:** [risk_level with emoji]

**Impact If Wrong:**

[impact_if_wrong]

**Sensitivity Range:** [sensitivity_range]

**Alternative Scenarios:** [if applicable, list as bullets]

**Test Plan:** [test_plan]

**Customer Validation Needed:** [YES/NO]

**Acceptance Criteria:**
[acceptance_criteria as bullets]

**Competitor Reference:** [if applicable]

---

[Repeat for all PRD-XXXX-NNN-ASMP assumptions]

---

## Requirements Summary

### By Category

| Category | Count | Percentage |
|----------|-------|------------|
| System (SYS) | X | XX% |
| Electrical (EE) | X | XX% |
| Manufacturing (MFG) | X | XX% |
| User (USR) | X | XX% |
| Non-Functional (NFR) | X | XX% |
| **Total** | **X** | **100%** |

### By Priority

| Priority | Count | Percentage | Examples |
|----------|-------|------------|----------|
| 🔴 P0-Critical | X | XX% | [List 2-3 key P0 req IDs] |
| 🟠 P1-High | X | XX% | [List 2-3 key P1 req IDs] |
| 🟡 P2-Medium | X | XX% | [List 2-3 key P2 req IDs] |
| ⚪ P3-Low | X | XX% | [List 2-3 key P3 req IDs] |

### By Verification Method

| Method | Count | Examples |
|--------|-------|----------|
| Test | X | [List examples] |
| Analysis | X | [List examples] |
| Inspection | X | [List examples] |
| Demonstration | X | [List examples] |

### Derived Requirements

| Req ID | Parent Requirements | Calculation |
|--------|-------------------|-------------|
| [List all derived] | [Parents] | [Calculation] |

---

## Traceability Matrix

### Forward Traceability (Requirement → Artifact)

| Req ID | Priority | Design | Trade-offs | Solution | Status |
|--------|----------|--------|------------|----------|--------|
| SYS-FUNC-001 | P0 | ✅ | ✅ | ✅ | Traced |
| SYS-FUNC-002 | P0 | ✅ | ⏳ | ⏳ | Partial |
| ... | ... | ... | ... | ... | ... |

**Legend:**
- ✅ = Traced
- ⏳ = TODO (expected later in project)
- ❌ = Missing (needs attention)

### Coverage Analysis

- **Fully Traced:** X/X (XX%)
- **Partially Traced:** X/X (XX%)
- **Orphaned (no trace):** X/X (XX%)

**Orphaned Requirements:** [List any with no traces]

---

## Standards Compliance

### Target Market Assumption: North America (Phase 1)

Our assumption: Phase 1 product targets **North America (UL + FCC)** for pilot and initial production. **EU (CE) expansion is future risk** assessed below but not blocking pilot.

**Rationale:** 2-month timeline to pilot production is aggressive. Simplify by targeting single market initially. North America (US + Canada) provides sufficient market size for pilot validation.

---

### North America (UL + FCC) - Phase 1 Compliance

| Standard | Applicability | Requirements | Status | Impact |
|----------|---------------|--------------|--------|--------|
| **UL 62368-1** | Audio/Video/ICT Equipment Safety | Electrical safety, fire/energy hazards, mechanical hazards | Post-pilot cert (Month 3-4) | Harmonized internationally (IECEE CB Scheme) |
| **UL 2054** | Battery Pack Safety (if BLE) | Overcharge/discharge protection, thermal management, short circuit | Post-pilot cert (Month 3-4) | **Critical:** Drives BMS design if BLE architecture |
| **UL 1642** | Lithium Battery Cells (if BLE) | Cell-level safety (less critical if using certified battery packs) | Post-pilot cert (Month 3-4) | Use pre-certified battery packs to mitigate |
| **FCC Part 15 Class B** | EMI/RFI Emissions | Conducted/radiated emissions limits (digital devices) | Post-pilot cert (Month 3-4) | Drives PCB layout, shielding, power supply filtering |
| **FCC Part 15C** | Intentional Radiators (if BLE) | Radio emissions, co-location, SAR (if applicable) | Post-pilot cert (Month 3-4) | Use pre-certified BLE modules (FCC ID) to simplify |
| **US ADA Section 703.3** | Braille Signage Standards | Dot spacing (2.5mm), dot diameter (1.5mm), dot height (0.64-0.94mm) | Design compliance (Phase 1) | **Critical:** Drives actuator mechanical design |

**Cost Impact (North America):**
- UL 62368-1: $8,000-15,000 (initial cert), 12-16 weeks
- UL 2054/1642 (if BLE): $10,000-20,000 (battery cert), 12-16 weeks
- FCC Part 15B/C: $5,000-10,000 (EMI/radio testing), 8-12 weeks
- **Total:** $23K-45K, 3-4 months (post-pilot, Month 3-6)

**Design Impact for North America:**
- **BLE Architecture:** UL 2054 battery certification is 12-16 weeks, $10-20K. **Mitigation:** Use pre-certified battery packs (LiPo pouches with integrated BMS from reputable suppliers like Varta, Panasonic, Murata).
- **USB-C Wired Architecture:** Eliminates UL 2054/1642 (no battery), simplifies FCC (no radio). Only UL 62368-1 + FCC Part 15B required. **Cost savings:** $10-20K, faster cert.
- **Component Selection:** RoHS-compliant parts for future EU expansion (no added cost, just limits BOM to RoHS-compliant suppliers).

---

### Europe (CE Marking) - Future Phase Risk Assessment

**⚠️ RISK:** If market expands to EU (Month 6+), additional certifications required:

| Standard | Applicability | Requirements | Cost | Timeline |
|----------|---------------|--------------|------|----------|
| **EN 62368-1** | IEC harmonized safety | Same as UL 62368-1 (harmonized via IECEE CB Scheme) | $0 if CB cert | Leverage UL cert |
| **EN 62133** | Battery Safety | Similar to UL 2054, but different test protocol | $8K-12K | 10-14 weeks |
| **RED 2014/53/EU** | Radio Equipment Directive (if BLE) | EMC, radio spectrum, health/safety | $12K-18K | 12-16 weeks |
| **RoHS 2011/65/EU** | Restriction of Hazardous Substances | Lead-free, no Hg/Cd/Cr(VI)/PBB/PBDE | **$0** if designed in | No timeline impact |
| **WEEE 2012/19/EU** | Waste Electrical Equipment | Recycling infrastructure, labeling | $2K-5K | 4-6 weeks (admin) |
| **REACH** | Chemical Registration | Compliance with EU chemical regulations | $5K-10K | 8-12 weeks |

**CE Certification Total (if expanding to EU):** $27K-45K, 3-4 months

**Mitigation Strategy:**
1. **Design for both markets from start:** RoHS-compliant BOM (no cost penalty), UL/EN harmonized design (minimize re-testing).
2. **USB-C wired architecture:** Simpler CE compliance (no radio, no battery). Only EN 62368-1 + RoHS/WEEE required.
3. **Defer certification, not design:** Phase 1 design is CE-ready (RoHS parts, harmonized safety), but defer testing until EU market validated.

**Risk Impact:**
- **Low risk if USB-C wired:** CE compliance is straightforward (EN 62368-1 + RoHS).
- **Medium risk if BLE:** RED + EN 62133 add $20K-30K and 3-4 months. Use pre-certified BLE modules (CE marked) and pre-certified battery packs to mitigate.

---

### Standards Summary Table

| Category | North America (Phase 1) | Europe (Future Risk) | Design Strategy |
|----------|-------------------------|----------------------|-----------------|
| **Electrical Safety** | UL 62368-1 ($8-15K) | EN 62368-1 (leverage CB cert) | Harmonized design, single test |
| **Battery Safety** | UL 2054 ($10-20K if BLE) | EN 62133 ($8-12K if BLE) | Pre-certified battery packs |
| **Radio (BLE)** | FCC Part 15C ($5-10K) | RED ($12-18K) | Pre-certified BLE modules |
| **EMI (all)** | FCC Part 15B ($5-10K) | Included in RED (BLE) or EN 62368-1 (wired) | PCB layout, shielding, filtering |
| **Environmental** | RoHS (voluntary, $0) | RoHS (mandatory, $0 if designed in) | RoHS BOM from start |
| **Accessibility** | US ADA 703.3 (design compliance) | No specific EU braille standard (ISO 9241 recommended) | ADA-compliant = international best practice |

---

### Key Takeaways for Design (v1.3.0)

1. **BLE vs USB-C trade-off:** USB-C wired architecture saves $15-30K in certification (no battery, no radio), simplifies compliance, but tethered UX.
2. **RoHS from day 1:** No cost penalty, keeps EU expansion option open.
3. **Pre-certified modules:** Use FCC/CE certified BLE modules (e.g., Nordic nRF52840 with FCC/CE ID) and UL/EN certified battery packs (e.g., Varta, Panasonic) to minimize re-testing.
4. **ADA 703.3 is critical:** Drives actuator size (≤2.3mm diameter), dot spacing (2.5mm), dot height (0.64-0.94mm). Non-negotiable.
5. **Post-pilot certification:** Design for compliance in Phase 1, but defer testing/certification to Month 3-6 (after pilot validation).

---

## Next Steps

1. **Review Requirements:** Validate completeness with stakeholders
2. **Run Audit:** Execute `/req-audit` to check compliance
3. **Freeze requirements.yaml:** Phase gate review before v1.3.0 (architecture design)
4. **Develop Architecture:** Proceed to v1.3.0 solution architectures (actuator, control, interface options)
5. **Maintain Traceability:** Update `traces_to` fields as designs evolve

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| [metadata.version] | [metadata.date] | [metadata.author] | Hierarchical PRD naming, assumptions refactored, standards compliance added |

---

## References

- **Source Document:** [metadata.source_doc]
- **Requirements Policy:** docs/requirements-policy.md
- **YAML Source (SSOT):** source/requirements.yaml

---

**END OF DOCUMENT**
```

---

## Formatting Guidelines

**Priority Emojis:**
- P0-Critical: 🔴
- P1-High: 🟠
- P2-Medium: 🟡
- P3-Low: ⚪

**Traceability Status:**
- ✅ = Link exists
- ⏳ = TODO (not yet applicable)
- ❌ = Missing (should exist but doesn't)

**Links:**
- Make all requirement IDs clickable anchors
- Link to external files when referenced
- Use relative paths (docs/architecture.md not /full/path)

**Tables:**
- Use Markdown tables for summaries
- Align columns for readability
- Include totals/percentages

---

## Save Output

**File:** `artifacts/requirements.md`

**Note:** This is a READ-ONLY generated file. To modify requirements, edit `source/requirements.yaml` and regenerate.

---

## After Completion

Display summary to user:
```
✅ Requirements Document Generated

Total Requirements: XX
File: artifacts/requirements.md
Size: XX KB

Breakdown:
- System (SYS): X
- Electrical (EE): X
- Manufacturing (MFG): X
- User (USR): X
- Non-Functional (NFR): X

Priority:
- P0-Critical: X (XX%)
- P1-High: X (XX%)
- P2-Medium: X (XX%)
- P3-Low: X (XX%)

Next: Run /req-audit to validate compliance
```
