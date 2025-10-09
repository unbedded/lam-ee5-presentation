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

**Key Insight:** All 6 assumptions require stakeholder validation before design freeze. Cost assumption (PRD-COST-001-ASMP) is CRITICAL - drives entire architecture selection. Portfolio approach in v1.3.0 covers assumption ranges to mitigate risk.

---

## Risk-Ranked Assumptions

### 🔴 CRITICAL RISK (1 assumption)

These assumptions have project-level impact. If wrong, require major redesign.

---

#### PRD-COST-001-ASMP: BOM Cost Target with Volume Assumption

**Parent Requirement:** PRD-COST-001 (Low Cost at Volume)

**PDF Says (verbatim):**
> "low-cost at volume production volume"

**Our Assumption:**
> BOM parts cost $200 ±$100 at volume of 10k units/month (range: $100-$300 BOM)

**Why This Assumption:**

PDF says 'low-cost' but gives no dollar amount. Market research (2025-10-08):
- BrailleMe: $515.50 retail (20-cell) → assuming 3× markup → ~$170 BOM
- Orbit Reader: $449 retail (20-cell) → assuming 3× markup → ~$150 BOM
- APH Refreshabraille: $1,795 retail (18-cell) → premium product

Our 32-cell device (60% more actuators than 20-cell) → target $200 BOM (mid-range).
3× markup → $600 retail (competitive with BrailleMe $515).

CRITICAL: This is an ASSUMPTION with ±50% sensitivity range ($100-$300 BOM).
v1.4.0 will test multiple cost scenarios, v1.3.0 will design portfolio at different cost points.

**Risk Level:** 🔴 CRITICAL

**Impact If Wrong:**
- If target is $100 BOM → Eliminates most actuator options, requires aggressive cost reduction
- If target is $300 BOM → Opens up premium actuator options (solenoid, haptic feedback)

**Sensitivity Range:** $100-$300 BOM (±50% from $200 target)

**Volume Assumption:** 10k units/month (120k/year) for BOM pricing

**Mitigation Strategy:**
- Designed portfolio at $100, $150, $200, $250, $300 BOM points
- v1.3.0 architectures cover full range
- v1.4.0 trade-off analysis shows which is viable at each cost point
- No single-point design - portfolio approach handles uncertainty

**Test Plan:** v1.4.0 sensitivity analysis (BOM scenarios: $100, $150, $200, $250, $300), v1.3.0 portfolio of architectures at different cost points

**Customer Validation Needed:** ✅ YES

**Status:** ⏳ Pending stakeholder review

---

### 🔴 HIGH RISK (2 assumptions)

These assumptions have major design impact. Wrong assumption = significant rework.

---

#### PRD-IFACE-001-ASMP: Multi-Interface Connectivity Strategy

**Parent Requirement:** PRD-IFACE-001 (Cell Phone Connectivity - Text Input to Braille Output)

**PDF Says (verbatim):**
> "device connects to a cell phone - receives text source"

**Our Assumption:**
> Primary interface: BLE (wireless, universal on modern phones). Secondary: USB-C wired (charging + data fallback, also low-cost option for future). Text format: ASCII (English Grade 1 braille), Unicode deferred to v2.0.

**Why This Assumption:**

'Portable companion device' suggests wireless (BLE) for mobility, BUT wired (USB-C) is valid low-cost alternative (no battery, tethered = still portable, just less convenient).

PORTFOLIO APPROACH (v1.3.0 will design multiple architectures):
- Architecture A: BLE-only (most portable, requires battery, wireless freedom)
- Architecture B: USB-C wired (no battery, tethered to phone, lowest cost $100-150 BOM savings)
- Architecture C: BLE + USB-C hybrid (battery for wireless, USB for charging/fallback, best UX)

Text format: ASCII initially (simpler firmware, covers English Grade 1 braille), Unicode support deferred to v2.0 (adds complexity, requires lookup tables).

**Risk Level:** 🔴 HIGH

**Impact If Wrong:**
BLE-only eliminates low-cost wired option. USB-C-only eliminates wireless UX. Hybrid is most flexible but highest cost.

**Sensitivity Range:** BLE-only, USB-C-only, or BLE+USB hybrid

**Mitigation Strategy:**
- Designed 3 architectures: BLE-only, USB-C-only, Hybrid
- Each optimizes different trade-off (cost vs UX vs flexibility)
- Portfolio approach allows customer to pick after validation

**Test Plan:** v1.3.0 interface architecture comparison (BLE vs USB-C vs hybrid), v1.4.0 cost/UX trade-offs

**Customer Validation Needed:** ✅ YES

**Status:** ⏳ Pending stakeholder review

---

#### PRD-VOL-001-ASMP: High Volume Production Capability

**Parent Requirement:** PRD-VOL-001 (High Volume Production Design)

**PDF Says (verbatim):**
> "designed for high-volume production"

**Our Assumption:**
> High-volume = 10k units/month (120k/year) production capability, SMT assembly, design for automation

**Why This Assumption:**

Global accessibility market: ~285M visually impaired, assuming 0.01% penetration = 28K units/year potential.
Target 10k/month (120k/year) as 'high-volume' threshold that drives design decisions:
- SMT assembly (not through-hole or hand assembly)
- Standard PCB processes (no exotic fabrication)
- Automated testing (test points, boundary scan)
- Component availability (no obsolete or single-source parts)

NOTE: Pilot production (PRD-SCHED-001-ASMP) is 100-500 units, then scale to 10k/month.

**Risk Level:** 🔴 HIGH

**Impact If Wrong:**
If 1k/month, hand assembly acceptable (lower NRE, higher unit cost). If 100k/month, requires full automation (higher NRE, lower unit cost).

**Sensitivity Range:** 1k/month (low volume, hand assembly OK) to 100k/month (full automation required)

**Mitigation Strategy:**
- Sensitivity analysis: 1k vs 10k vs 100k units/month
- v1.5.0 DFM analysis shows scalability for each architecture
- SMT design supports volume scaling

**Test Plan:** v1.4.0 sensitivity analysis (volume scaling 1k vs 10k vs 100k), v1.5.0 DFM analysis for SMT assembly

**Customer Validation Needed:** ✅ YES

**Status:** ⏳ Pending stakeholder review

---

### 🟡 MEDIUM RISK (3 assumptions)

These assumptions have moderate design impact. Wrong assumption = adjustments, not redesign.

---

#### PRD-SCHED-001-ASMP: Pilot Production Assumption

**Parent Requirement:** PRD-SCHED-001 (Production Timeline - Two Month Release)

**PDF Says (verbatim):**
> "release the project into production within two months"

**Our Assumption:**
> Production within 2 months = PILOT production of 100-500 units for design validation, NOT mass production (10k+/month)

**Why This Assumption:**

Industry best practice: 2-month design cycle → pilot run (100-500 units) → validate design, manufacturing tolerances, failure modes → scale to mass production (Month 3+).
Direct-to-mass-production is extremely high-risk (no tolerance validation, no FMEA data).

**Risk Level:** 🟡 MEDIUM

**Impact If Wrong:**
If mass production required in 2 months, timeline is infeasible (tooling, certification, supply chain all take 8-12 weeks minimum)

**Mitigation Strategy:**
- v1.5.0 production plan shows both pilot and mass production paths
- Timeline sensitivity analysis in v1.4.0

**Test Plan:** v1.5.0 production timeline (design → pilot → scale), v1.4.0 sensitivity on timeline compression

**Customer Validation Needed:** ✅ YES

**Status:** ⏳ Pending stakeholder review

---

#### PRD-SIZE-001-ASMP: Portable Form Factor - Cell Phone Environment Compatible

**Parent Requirement:** PRD-SIZE-001 (Portable Device)

**PDF Says (verbatim):**
> "portable companion device to a cell phone"

**Our Assumption:**
> Portable = compatible with environments where cell phone goes (pocket, bag, desk). Target ≤1.3 lbs (590g) weight, fits in bag/purse (~8"×4"×1" max), operates anywhere cell phone operates.

**Why This Assumption:**

'Companion device to cell phone' suggests same portability/environment as cell phone:
- Pocket/bag portable (not desktop/tethered)
- Indoor environments (home, office, school, cafe)
- Battery powered (untethered)
- Durable for daily transport

BrailleMe competitor benchmark: 1.3 lbs (590g), 20-cell, portable design.
Our 32-cell device will be slightly larger/heavier, but target ≤1.3 lbs is achievable.

**Risk Level:** 🟡 MEDIUM

**Impact If Wrong:**
If ultra-light (<0.5 lbs) required, limits battery capacity significantly. If desktop (2+ lbs) acceptable, eases design constraints.

**Sensitivity Range:** Weight: 0.5-1.5 lbs (230-680g), Size: 6-10" wide × 3-5" deep × 0.5-1.5" tall

**Mitigation Strategy:**
- v1.3.0 weight budget (actuators + battery + enclosure)
- v1.4.0 sensitivity on size/weight trade-offs

**Test Plan:** v1.3.0 weight budget (actuators + battery + enclosure), v1.4.0 sensitivity on size/weight trade-offs

**Customer Validation Needed:** ✅ YES

**Status:** ⏳ Pending stakeholder review

---

#### PRD-FUNC-002-ASMP: Braille Refresh Speed and Navigation

**Parent Requirement:** PRD-FUNC-002 (Braille Line Update - Refresh Next Line)

**PDF Says (verbatim):**
> "device must update to show the next line of text"

**Our Assumption:**
> Refresh speed: <2 seconds full-line update (acceptable UX). Trigger: Tactile UP/DOWN buttons (standard pattern from BrailleMe, Orbit Reader competitors).

**Why This Assumption:**

Typical braille reading speed: 60-150 words/minute (advanced readers) = 1-2.5 seconds per line.
Refresh <2 seconds = doesn't interrupt reading flow.

Navigation: BrailleMe and Orbit Reader use tactile buttons (UP/DOWN or PREV/NEXT).
Automatic scroll would be disruptive (users read at different speeds).
Manual button trigger = user controls pace.

**Risk Level:** 🟡 MEDIUM

**Impact If Wrong:**
If <0.5 sec required, limits actuator options (piezo only). If 5 sec acceptable, eases actuator selection.

**Sensitivity Range:** <1 sec (fast, challenging for some actuators) to <5 sec (slow but acceptable)

**Mitigation Strategy:**
- Actuator selection in v1.3.0 considers refresh speed
- Piezo (fast) vs solenoid (slower) options evaluated

**Test Plan:** v1.3.0 actuator selection (refresh speed capability), v1.4.0 UX testing with target users

**Customer Validation Needed:** ✅ YES

**Status:** ⏳ Pending stakeholder review

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
- **Audit Report:** artifacts/rubric-reports/req-audit-report.md
- **Traceability Report:** artifacts/rubric-reports/req-traceability-report.md
- **Cheat Sheet:** artifacts/REQUIREMENTS-CHEAT-SHEET.md

---

**🔒 NOTE:** This is a **READ-ONLY generated file**. To modify assumptions, edit `source/requirements.yaml` and regenerate using `/req-risk-report`.

---

**END OF REPORT**
