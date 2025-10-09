---
description: Generate risk-ranked assumption requirements report
---

# Assumption Requirements Risk Report Generator

Generate `artifacts/assumption-risk-report.md` - risk-ranked analysis of all assumptions

---

## Your Task

Parse `source/requirements.yaml` and generate a professional risk assessment report focused on assumptions (PRD-XXXX-NNN-ASMP).

---

## Step 1: Load Source (30 sec)

Read:
- `source/requirements.yaml` - Requirements database (SSOT)

---

## Step 2: Extract All Assumptions (1 min)

Find all requirements with ID pattern `PRD-XXXX-NNN-ASMP`:
- PRD-SCHED-001-ASMP (Pilot production)
- PRD-SIZE-001-ASMP (Portable form factor)
- PRD-IFACE-001-ASMP (Interface strategy)
- PRD-COST-001-ASMP (BOM cost target)
- PRD-VOL-001-ASMP (Volume capability)
- PRD-FUNC-002-ASMP (Refresh speed)

For each assumption, extract:
- ID
- Title
- Parent requirement (PRD-XXXX-NNN)
- pdf_says (what PDF actually said)
- our_assumption (our interpretation)
- risk_level (CRITICAL/HIGH/MEDIUM/LOW)
- customer_validation_needed (YES/NO)
- impact_if_wrong
- sensitivity_range
- test_plan
- rationale

---

## Step 3: Generate Risk-Ranked Report (5 min)

Create `artifacts/assumption-risk-report.md` in this format:

```markdown
# Assumption Requirements Risk Report

**Project:** Lam Research - Braille Display EE Concept Evaluation
**Version:** 2.0.0
**Date:** 2025-10-09
**Source:** source/requirements.yaml

---

## Executive Summary

**Total Assumptions:** 6
**Risk Distribution:**
- 🔴 CRITICAL: 1 (17%)
- 🔴 HIGH: 2 (33%)
- 🟡 MEDIUM: 3 (50%)
- 🟢 LOW: 0 (0%)

**Customer Validation Required:** 6 (100%)

**Key Insight:** All 6 assumptions require stakeholder validation before design freeze. Cost assumption (PRD-COST-001-ASMP) is CRITICAL - drives entire architecture selection.

---

## Risk-Ranked Assumptions

### 🔴 CRITICAL RISK (1 assumption)

These assumptions have project-level impact. If wrong, require major redesign.

---

#### PRD-COST-001-ASMP: BOM Cost Target with Volume Assumption

**Parent Requirement:** [PRD-COST-001](#prd-cost-001-low-cost-at-volume)

**PDF Says (verbatim):**
> "low-cost at volume production volume"

**Our Assumption:**
> BOM parts cost $200 ±$100 at volume of 10k units/month (range: $100-$300 BOM)

**Why This Assumption:**
[rationale from YAML - show derivation process]

**Risk Level:** 🔴 CRITICAL

**Impact If Wrong:**
[impact_if_wrong from YAML]

**Sensitivity Range:**
[sensitivity_range from YAML]

**Mitigation Strategy:**
- Designed portfolio at $100, $150, $200, $250, $300 BOM
- v1.3.0 architectures cover full range
- v1.4.0 trade-off analysis shows which is viable at each cost point
- No single-point design - portfolio approach handles uncertainty

**Test Plan:**
[test_plan from YAML]

**Customer Validation Needed:** ✅ YES

**Status:** ⏳ Pending stakeholder review

---

### 🔴 HIGH RISK (2 assumptions)

These assumptions have major design impact. Wrong assumption = significant rework.

---

#### PRD-IFACE-001-ASMP: Multi-Interface Connectivity Strategy

[Same format as above - full details from YAML]

**Risk Level:** 🔴 HIGH

**Mitigation Strategy:**
- Designed 3 architectures: BLE-only, USB-C-only, Hybrid
- Each optimizes different trade-off (cost vs UX vs flexibility)
- Portfolio approach allows customer to pick after validation

---

#### PRD-VOL-001-ASMP: High Volume Production Capability

[Same format as above]

**Risk Level:** 🔴 HIGH

**Mitigation Strategy:**
- Sensitivity analysis: 1k vs 10k vs 100k units/month
- v1.5.0 DFM analysis shows scalability for each architecture
- SMT design supports volume scaling

---

### 🟡 MEDIUM RISK (3 assumptions)

These assumptions have moderate design impact. Wrong assumption = adjustments, not redesign.

---

#### PRD-SCHED-001-ASMP: Pilot Production Assumption

[Same format as above]

**Risk Level:** 🟡 MEDIUM

**Mitigation Strategy:**
- v1.5.0 production plan shows both pilot and mass production paths
- Timeline sensitivity analysis in v1.4.0

---

#### PRD-SIZE-001-ASMP: Portable Form Factor - Cell Phone Environment Compatible

[Same format as above]

**Risk Level:** 🟡 MEDIUM

**Mitigation Strategy:**
- v1.3.0 weight budget for each architecture
- Battery capacity can be adjusted without major redesign

---

#### PRD-FUNC-002-ASMP: Braille Refresh Speed and Navigation

[Same format as above]

**Risk Level:** 🟡 MEDIUM

**Mitigation Strategy:**
- Actuator selection in v1.3.0 considers refresh speed
- Piezo (fast) vs solenoid (slower) options evaluated

---

## Risk Mitigation Summary

### Portfolio Approach = Risk Management

**Strategy:** Design multiple architectures to cover assumption ranges

| Assumption | Range | Architectures |
|------------|-------|---------------|
| Cost | $100-$300 BOM | 3 architectures at $150/$200/$300 |
| Interface | BLE/USB-C/Hybrid | 3 architectures (each interface) |
| Volume | 1k-100k/month | DFM analysis for each scale |
| Timeline | Pilot vs Mass | Both paths documented in v1.5.0 |
| Size/Weight | 0.5-1.5 lbs | Weight budget for each architecture |
| Refresh | <1 sec to <5 sec | Actuator options cover range |

**Result:** No single assumption can derail project - portfolio covers alternatives

---

## Customer Validation Checklist

### Before Phase Gate (v1.2.0 → v1.3.0)

Recommended stakeholder review:

- [ ] **PRD-COST-001-ASMP** (CRITICAL)
  - Question: "Is $200 BOM target realistic? Or $150? Or $300?"
  - Impact: Drives actuator selection, interface choice, feature set
  - Action: Customer picks cost target → We recommend matching architecture

- [ ] **PRD-IFACE-001-ASMP** (HIGH)
  - Question: "Wireless (BLE) or wired (USB-C) or both?"
  - Impact: Battery requirement, $100 BOM difference
  - Action: Customer picks UX priority (portability vs cost)

- [ ] **PRD-VOL-001-ASMP** (HIGH)
  - Question: "Is 10k/month the right volume target? Or 1k? Or 100k?"
  - Impact: DFM approach, NRE investment, unit cost
  - Action: Customer confirms volume → We adjust DFM strategy

- [ ] **PRD-SCHED-001-ASMP** (MEDIUM)
  - Question: "2 months to pilot (100-500 units) or mass production?"
  - Impact: Timeline feasibility (mass production in 2 months = infeasible)
  - Action: Confirm pilot interpretation

- [ ] **PRD-SIZE-001-ASMP** (MEDIUM)
  - Question: "Is ≤1.3 lbs target acceptable? Or need <0.5 lbs?"
  - Impact: Battery capacity constraint
  - Action: Confirm weight target

- [ ] **PRD-FUNC-002-ASMP** (MEDIUM)
  - Question: "Is <2 sec refresh acceptable? Or need <0.5 sec?"
  - Impact: Actuator technology selection (piezo vs solenoid)
  - Action: Confirm UX requirement

---

## Sensitivity Analysis Plan (v1.4.0)

### Quantitative Testing of Assumptions

For each CRITICAL/HIGH risk assumption, test multiple scenarios:

**Cost Sensitivity:**
| BOM Target | Architecture | Actuator | Feasibility |
|------------|--------------|----------|-------------|
| $100 | USB-C only | Piezo | Aggressive |
| $150 | USB-C or BLE | Piezo | Achievable |
| $200 | BLE+USB | Solenoid | Comfortable |
| $300 | BLE+USB | Premium | Feature-rich |

**Volume Sensitivity:**
| Volume | DFM Approach | NRE | Unit Cost |
|--------|--------------|-----|-----------|
| 1k/mo | Hand assembly | Low | High |
| 10k/mo | SMT automated | Medium | Medium |
| 100k/mo | Full automation | High | Low |

**Interface Sensitivity:**
| Interface | BOM Cost | UX | Complexity |
|-----------|----------|----|-----------|
| USB-C only | $100-150 | Good | Low |
| BLE only | $200-250 | Best | Medium |
| Hybrid | $250-300 | Best+ | High |

---

## Recommendation: Portfolio Presentation

**Instead of:**
- "Here's my design based on these assumptions"
- Risk: If assumptions wrong, design fails

**Do this:**
- "Here are 3 designs covering the assumption range"
- "Customer validates assumptions → picks matching architecture"
- Risk mitigation: Portfolio approach handles uncertainty

**This IS systems engineering:** Design for ranges, not points

---

## Traceability

### Assumptions → Architectures (v1.3.0)

| Assumption | Drives | Architecture Impact |
|------------|--------|---------------------|
| PRD-COST-001-ASMP | Actuator selection, interface | A/B/C at $150/$200/$300 |
| PRD-IFACE-001-ASMP | Battery requirement, connectivity | A (BLE), B (USB-C), C (Hybrid) |
| PRD-VOL-001-ASMP | DFM approach, component sourcing | SMT design for all |
| PRD-SCHED-001-ASMP | Parts lead time, assembly method | COTS components only |
| PRD-SIZE-001-ASMP | Battery capacity, enclosure size | Weight budget per architecture |
| PRD-FUNC-002-ASMP | Actuator technology | Piezo (fast) vs solenoid (slower) |

### Assumptions → Trade-offs (v1.4.0)

Each assumption becomes a trade-off axis:
- Cost axis: $100 vs $200 vs $300
- UX axis: Wireless vs Wired vs Hybrid
- Volume axis: 1k vs 10k vs 100k
- Timeline axis: Pilot vs Mass production

Trade-off analysis = Quantitative sensitivity testing of assumptions

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.0.0 | 2025-10-09 | Spencer Barrett | Initial risk report from hierarchical PRD naming (v2.0.0) |

---

## References

- **Source (SSOT):** source/requirements.yaml
- **Requirements Report:** artifacts/requirements.md
- **Cheat Sheet:** artifacts/REQUIREMENTS-CHEAT-SHEET.md
- **Philosophy Alignment:** docs/requirements-philosophy-alignment.md
- **Presentation Key Messages:** docs/presentation-key-messages.md

---

**🔒 NOTE:** This is a **READ-ONLY generated file**. To modify assumptions, edit `source/requirements.yaml` and regenerate using `/req-risk-report`.

---

**END OF REPORT**
```

---

## Formatting Guidelines

**Risk Emojis:**
- 🔴 CRITICAL
- 🔴 HIGH
- 🟡 MEDIUM
- 🟢 LOW

**Status Indicators:**
- ✅ Validated
- ⏳ Pending validation
- ❌ Validation failed
- 🔄 Under review

**Priority Order:**
1. CRITICAL risks first (project-level impact)
2. HIGH risks second (major design impact)
3. MEDIUM risks third (moderate impact)
4. LOW risks last (minor impact)

---

## After Completion

Display summary to user:

```
✅ Assumption Risk Report Generated

Total Assumptions: 6
Risk Distribution:
- 🔴 CRITICAL: 1
- 🔴 HIGH: 2
- 🟡 MEDIUM: 3
- 🟢 LOW: 0

File: artifacts/assumption-risk-report.md
Size: ~XX KB

Customer Validation Needed: 6/6 (100%)

Next: Review report, share with stakeholders for validation
```
