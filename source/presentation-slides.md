---
title: "Braille Display - Concept Evaluation"
subtitle: "Electrical Engineering Design for Portable Cell Phone Companion Device"
author: "Spencer Barrett"
date: "October 2025"
---

# Title Slide

**Braille Display - Concept Evaluation**

Electrical Engineering Design for Portable Cell Phone Companion Device

Spencer Barrett
Lam Research EE5 Interview
October 2025

::: notes
30 seconds introduction. State name, position applied for, and agenda overview.
4-part structure follows PDF design steps: Requirements → Solutions → Evaluation → Production
:::

---

# Agenda

**Four-Part Design Process:**

1. **Identify Key Technical Requirements** (25 pts)
   - System, electrical, and relevant specifications

2. **Develop Multiple Alternative Solutions** (25 pts)
   - 3 distinct architectures

3. **Evaluate the Proposed Solutions** (30 pts)
   - Advantages, disadvantages, and trade-off analysis

4. **Transition to Volume Production** (20 pts)
   - Process from initial design to pilot production

::: notes
Explicitly map to PDF rubric structure (Interview Overview p.10).
Emphasize: This is not "find the best solution" - it's "navigate trade-offs and provide decision framework."
:::

---

# Problem Statement

## Design Challenge

**Objective:** Create a companion device for cell phones that displays a single line of braille text

**Key Requirements:**
- 32 characters × 6 dots each = **192 control signals**
- Portable & low-cost
- High volume manufacturing
- **2-month timeline** to pilot production

::: notes
Emphasize the challenge: 192 independent actuators in a compact, cost-effective package.
This is the constraint tripod: cost, size, timeline - can't optimize all three simultaneously.
:::

---

# SECTION 1: Technical Requirements

---

# Design Step 1: Identify Key Technical Requirements

**Objective:** Define system, electrical, and relevant specifications

**Deliverables:**
- 17 requirements (9 ground truth + 6 assumptions + 2 standards)
- Requirements traceability matrix
- Standards compliance analysis

**Rubric Weight:** 25/100 points

::: notes
Section 1 of 4. This addresses PDF requirement: "Identify key technical requirements, including system, electrical, and other relevant specifications."
Key challenge: PDF spec was vague - had to make engineering assumptions.
:::

---

# Requirements Analysis

## Key Technical Requirements

**From PDF specification (vague → quantified):**
- PRD-FUNC-001: 32 characters × 6 dots = 192 actuators
- PRD-SIZE-001: Portable → <300mm length, <500g weight (derived from ADA 703.3)
- PRD-COST-001: Low cost → <$500 BOM target (China market assumption)
- PRD-SCHED-001: 2-month timeline → COTS components only (≤4 week lead time)

**Standards Compliance:**
- NFR-STD-001: UL/FCC (North America regulatory)
- NFR-STD-002: ADA 703.3 (2.5mm dot pitch, 6.2mm cell spacing)

**Total: 17 requirements** (9 ground truth + 6 assumptions + 2 standards)

::: notes
Critical point: PDF spec was vague. Had to make engineering assumptions.
All assumptions documented with derivation rationale and customer validation flags.
See requirements.yaml for complete traceability.
:::

---

# Systems Engineering Philosophy

## Trade-offs Over Perfection

**Key Principle:** Requirements exist in RANGES, not absolutes

**Example:** PRD-COST-001-ASMP: $200 ±$100 BOM (not "$200 exactly")

**Approach:**
- Portfolio of 3 architectures vs. single point design
- Each optimizes DIFFERENT trade-off:
  - Cost vs. UX
  - Timeline vs. Features
  - Simplicity vs. Innovation

**Philosophy:**
- "Not about 'best power supply with uber-clean output'"
- Balance cost/reliability/performance/timeline
- Simplification is innovation (wired = simpler than wireless)
- Know when SW replaces HW complexity

::: notes
This is the thesis of the presentation: There is NO "best" architecture.
Selection depends on customer priorities (cost? timeline? UX?).
Engineering is about navigating trade-offs, not finding perfection.
:::

---

# Assumptions & Sensitivity Ranges

## Managing Requirement Vagueness

**Hierarchical Structure:**
- PRD-XXXX-NNN: Ground truth (verbatim from PDF)
- PRD-XXXX-NNN-ASMP: Derived assumptions (documented reasoning)

**Key Assumptions:**
- Market: China accessibility market (price-sensitive)
- Timeline: 2-month pilot (not mass production)
- Volume: 100 pilot units → 10K production scaling path
- Power: USB/AA/Li-ion options (customer preference TBD)

**Sensitivity Analysis:** All architectures evaluated across assumption ranges

::: notes
customer_validation_needed flags show where spec clarification needed.
Alternative scenarios documented for each major assumption.
This drives the portfolio approach - different architectures win under different scenarios.
:::

---

# SECTION 2: Alternative Solutions

---

# Design Step 2: Develop Multiple Alternative Solutions

**Objective:** Create and describe distinct architecture options

**Deliverables:**
- 3 architectures with block diagrams
- Component selection rationale
- Pros/cons for each approach

**Rubric Weight:** 25/100 points

::: notes
Section 2 of 4. This addresses PDF requirement: "Develop and describe multiple alternative solutions."
Each architecture optimizes DIFFERENT trade-off (cost vs UX vs innovation).
:::

---

# Architecture A: ARCH_PIEZO_ECO

## Piezo Economy (Wired, Standard)

![Architecture diagram](../resources/diagrams/arch-piezo-eco-block.png)

**Key Features:**
- Piezoelectric actuators (200V, 2.5mm pitch)
- STM32 MCU + ULN2803A drivers
- USB-C wired (power + data)
- Simplest electrical design

**BOM:** $420 (pilot), Timeline: 8-10 weeks

**Optimizes:** Cost + Timeline (fastest to market)

::: notes
This is the "get to market fast" option.
Standard piezo technology, USB-C avoids BLE certification.
Constraint: Need COTS piezo at 2.5mm pitch (not found yet - see actuator sourcing slide).
:::

---

# Architecture B: ARCH_SOL_ECO

## Solenoid Economy (Rotary Cam, Innovative)

![Architecture diagram](../resources/diagrams/arch-sol-eco-block.png)

**Key Features:**
- 4mm COTS solenoids + rotary cam mechanism
- Mechanical innovation (motorcycle engine concept)
- Trades electrical complexity for mechanical simplicity
- 3.5mm pitch (relaxed spacing - pilot acceptable)

**BOM:** $277 (pilot), Timeline: 10-12 weeks (+2 weeks for cam tooling)

**Optimizes:** Volume scaling (mechanical cost-down potential)

::: notes
Creative solution: Can't find small actuators? Use bigger ones + mechanical reduction.
Trade-off: Violates 2.5mm pitch, but still functional for pilot validation.
Cam mechanism inspired by motorcycle valve trains - proven concept.
:::

---

# Architecture C: ARCH_PIEZO_DLX

## Piezo Deluxe (Wireless, Premium UX)

![Architecture diagram](../resources/diagrams/arch-piezo-dlx-block.png)

**Key Features:**
- Piezoelectric actuators (200V, 2.5mm pitch)
- nRF52840 BLE module (pre-certified FCC)
- Li-ion battery (8 hours usage)
- Best user experience (wireless freedom)

**BOM:** $442 (pilot), Timeline: 10-12 weeks (+1 week for BLE cert)

**Optimizes:** User experience (wireless convenience)

::: notes
Premium option for users who value wireless freedom.
BLE module is pre-certified (faster than custom radio).
Battery life: 8 hours at 10 char/min reading speed (see power-budget.xlsx).
:::

---

# SECTION 3: Solution Evaluation

---

# Design Step 3: Evaluate the Proposed Solutions

**Objective:** Discuss advantages, disadvantages, and other considerations

**Deliverables:**
- Evaluation framework with weighted criteria
- Quantitative comparison (cost, power, timeline)
- Sensitivity analysis ("what if" scenarios)
- Decision framework (context-dependent selection)

**Rubric Weight:** 30/100 points ← **HIGHEST**

::: notes
Section 3 of 4. This addresses PDF requirement: "Evaluate the proposed solutions by discussing their advantages and disadvantages, as well as any other considerations that influenced your final selection."
Critical: NO universal "best" - selection depends on customer priorities.
:::

---

# Trade-off Analysis

## Evaluation Framework

| Criterion | Weight | ARCH_PIEZO_ECO | ARCH_SOL_ECO | ARCH_PIEZO_DLX |
|-----------|--------|----------------|--------------|----------------|
| Time to Market | 25% | 9/10 | 7/10 | 6/10 |
| Unit Cost | 20% | 8/10 | 9/10 | 6/10 |
| Manufacturability | 20% | 8/10 | 7/10 | 7/10 |
| UX/Usability | 10% | 7/10 | 6/10 | 9/10 |
| Robustness | 10% | 7/10 | 8/10 | 6/10 |

**Weighted Scores:** PIEZO_ECO (8.2), SOL_ECO (7.9), PIEZO_DLX (6.8)

::: notes
Weights reflect 2-month timeline constraint (time = 25%).
PIEZO_ECO scores highest IF timeline is critical.
SOL_ECO wins IF cost is paramount and timeline relaxes to 10-12 weeks.
PIEZO_DLX wins IF wireless required (only option).
:::

---

# Advantages & Disadvantages

## Honest Engineering Assessment

**ARCH_PIEZO_ECO:**
- ✅ Fastest to market (8-10 weeks)
- ✅ Simplest electrical design
- ❌ Needs COTS piezo at 2.5mm (not found yet)

**ARCH_SOL_ECO:**
- ✅ Lowest BOM cost ($277)
- ✅ COTS solenoids available (Olimex)
- ❌ Violates 2.5mm pitch (3.5mm actual)

**ARCH_PIEZO_DLX:**
- ✅ Best UX (wireless freedom)
- ❌ Highest cost ($442)
- ❌ Longest timeline (BLE cert)

::: notes
No perfect solution - each has trade-offs.
Critical honesty: PIEZO_ECO depends on actuator sourcing (see next slide).
SOL_ECO violates spacing but pilot-acceptable for proof-of-concept.
:::

---

# Sensitivity Analysis

## "What If" Scenarios

| Scenario | ARCH_PIEZO_ECO | ARCH_SOL_ECO | ARCH_PIEZO_DLX |
|----------|----------------|--------------|----------------|
| **Cost doubles** | $840 (still viable) | $554 (best) | $884 (fails) |
| **Timeline -50%** | Wins (8 wks → 4 wks) | Fails (cam tooling) | Fails (BLE cert) |
| **Wireless required** | Fails | Fails | **ONLY option** |
| **Volume > 10K** | Good | **Best scaling** | Poor (BLE $$$) |

**Robustness:** PIEZO_ECO most robust across scenarios

::: notes
Sensitivity analysis shows: No universal winner.
PIEZO_ECO wins most scenarios (robust choice).
SOL_ECO wins cost-constrained, high-volume.
PIEZO_DLX wins wireless-required scenario (no alternatives).
:::

---

# Decision Framework

## "It Depends on YOUR Priorities"

**Selection Criteria:**

```
IF wireless required:
  → ARCH_PIEZO_DLX (only option)

ELSE IF cost < $300:
  → ARCH_SOL_ECO (lowest BOM)

ELSE IF timeline < 8 weeks:
  → ARCH_PIEZO_ECO (fastest)

ELSE IF volume > 10K:
  → ARCH_SOL_ECO (best scaling)

ELSE:
  → ARCH_PIEZO_ECO (most robust)
```

::: notes
This is the key message: No "best" architecture, only "best FOR YOUR CONSTRAINTS".
Tell customer: "Give me your priorities, I'll tell you which architecture wins."
Portfolio approach acknowledges requirements uncertainty.
:::

---

# SECTION 4: Path to Production

---

# Design Step 4: Transition to Volume Production

**Objective:** Outline process from initial design to pilot production

**Deliverables:**
- 8-12 week production timeline (architecture-agnostic)
- Critical path analysis (actuator sourcing)
- Risk mitigation strategies
- DFM considerations

**Rubric Weight:** 20/100 points

::: notes
Section 4 of 4. This addresses PDF requirement: "Outline the process for transitioning the concept from initial design to volume production."
Key insight: Same production process for all architectures, just different timeline/risk profiles.
THE critical path risk: Actuator sourcing (all architectures blocked without resolution).
:::

---

# ⚠️ Actuator Sourcing - THE Critical Path Risk

## All Architectures Blocked Without Resolution

![Three-path strategy](../resources/diagrams/actuator-sourcing-decision.png)

**Problem:** NO COTS actuators found meeting 2.5mm pitch + force requirements

**Three-Path Strategy (parallel effort):**
- **Path A (COTS search):** $5K, 2 weeks, 20% success probability
- **Path B (Custom quickturn):** $25K-50K NRE, 2-4 weeks, 90% success
- **Path C (Spec relaxation):** $0, 0 weeks, 100% (but violates ADA 703.3)

**Timeline Impact:** +0 weeks (COTS found) to +8 weeks (custom standard lead time)

**Key Message:** This is MAKE-OR-BREAK. All 3 architectures depend on actuator resolution.

::: notes
THE ELEPHANT IN THE ROOM - must address head-on.
Honest engineering: No COTS solution exists today.
Triple-path strategy shows risk management (parallel efforts).
Budget allocation: $50K contingency for custom actuator NRE.
Decision point: End of Week 2, commit to one path.
:::

---

# Path to Production (Design Step 4)

## 8-12 Week Timeline (Architecture-Agnostic)

**Common Production Process:**
- **Week 0-2:** Actuator sourcing resolution ⚠️ CRITICAL PATH
- **Week 3-4:** Detailed design (schematic, PCB layout, BOM lock)
- **Week 5-6:** Prototype build (fab, assembly, debug)
- **Week 7-9:** Pilot production (10-100 units, yield validation)
- **Week 10-12:** Compliance testing & manufacturing transfer

**Architecture-Specific Timeline Deltas:**
- ARCH_PIEZO_ECO: +0 weeks (base case)
- ARCH_SOL_ECO: +2 weeks (mechanical cam tooling)
- ARCH_PIEZO_DLX: +1 week (BLE certification testing)

::: notes
Same production flow for all architectures - just different timeline/risk profiles.
Week 0-2 is critical: Without actuator, everything slips 8+ weeks.
Pilot = 10-100 units for validation, not mass production.
:::

---

# Risk Mitigation Strategies

## Primary Risk: Actuator Sourcing (ALL architectures)

**Mitigation:**
- Triple-path parallel effort (COTS / Custom / Spec relaxation)
- $50K NRE budget allocated for custom actuator quickturn
- Decision gate: End of Week 2

**Secondary Risks:**
- **ARCH_PIEZO_ECO:** 200V boost converter design (medium risk)
- **ARCH_SOL_ECO:** Mechanical cam tolerance stack-up (medium risk)
- **ARCH_PIEZO_DLX:** BLE certification schedule slip (low risk - pre-certified module)

**Supply Chain:**
- All architectures use COTS MCU/drivers (STM32, ULN2803A)
- Multi-source strategy for passives

::: notes
Actuator is THE risk. Everything else is manageable.
If actuator sourcing fails all paths: Project scope changes (spec relaxation or timeline extension).
Secondary risks are architecture-specific but lower impact.
:::

---

# Summary

**3 Viable Architectures:**
- ARCH_PIEZO_ECO: Optimizes cost + timeline
- ARCH_SOL_ECO: Optimizes volume scaling + mechanical innovation
- ARCH_PIEZO_DLX: Optimizes user experience (wireless)

**Selection Framework:**
- No universal "best" - depends on customer priorities
- Decision tree: wireless? cost threshold? timeline? volume?

**Critical Path Risk:**
- Actuator sourcing must resolve Week 0-2
- All architectures blocked without actuator solution

**Production Timeline:**
- 8-12 weeks depending on architecture choice
- Actuator sourcing adds +0 to +8 weeks

::: notes
Close with confidence: I have 3 solid options, here's how to choose.
Acknowledge reality: Actuator is the gating factor, but I have a mitigation plan.
Ready for Q&A on technical details, trade-off assumptions, or production strategy.
:::

---

# Q&A

Questions?

::: notes
Anticipated questions:
1. Why can't you find COTS actuators? (Answer: 2.5mm pitch is non-standard, most braille displays use 200V custom piezos)
2. What if timeline extends to 4 months? (Answer: Opens door to custom actuator standard lead time, better cost optimization)
3. Which architecture would YOU pick? (Answer: ARCH_PIEZO_ECO most robust, but depends on wireless requirement)
4. Can you hit $200 BOM? (Answer: Not with COTS, need volume negotiation or custom actuator design)
5. Power supply design for 200V piezo? (Answer: DC-DC boost converter, see preliminary schematic concepts)
:::
