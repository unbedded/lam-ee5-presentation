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

## Ground Truth Requirements from PDF

**"Let me validate I understood correctly BEFORE we proceed..."**

| ID | Requirement (PDF Verbatim) | Status | Impact |
|----|---------------------------|--------|--------|
| **PRD-SCHED-001** | "release into production within two months" | ⚠️ VAGUE | Pilot vs mass? |
| **PRD-SIZE-001** | "portable companion device" | ⚠️ VAGUE | How big? Weight? |
| **PRD-IFACE-001** | "connects to a cell phone" | ⚠️ VAGUE | BLE? USB? Both? |
| **PRD-COST-001** | "low-cost at volume" | ⚠️ VAGUE | $100? $200? $500? |
| **PRD-FUNC-001** | "32 characters × 6 dots = 192 dots" | ✅ CLEAR | Core spec |
| **PRD-FUNC-002** | "update to show next line" | ⚠️ VAGUE | <1s? <5s? |
| **PRD-FUNC-003** | "each dot raised or lowered" | ✅ CLEAR | Binary actuation |
| **PRD-VOL-001** | "high-volume production" | ⚠️ VAGUE | 1K? 10K? 100K/mo? |
| **PRD-USER-001** | "sight-impaired person" | ✅ CLEAR | ADA compliance |

**Key Observation:** Only **3 of 9** requirements are CLEAR. **6 are VAGUE.**

::: notes
Strategic framing: "I read the spec CAREFULLY and extracted requirements."
"6 of 9 are vague - I need YOUR feedback before building the wrong thing."
"What you asked is NOT POSSIBLE in 2 months without trade-offs."
This sets up the portfolio approach (3 architectures) and honest engineering discussion.
:::

---

# Market Context

---

# Commercial Braille Display Market

## Market Landscape & Technology Monopoly

![Price vs Characters](source/svg/market-price-vs-chars.svg)

**Key Finding:** 100% of commercial displays use **custom piezoelectric actuators**

| Segment | Example | Characters | Price (USD) | Technology |
|---------|---------|------------|-------------|------------|
| **Budget** | Orbit Reader 20 | 20 | $799 | Custom piezo (8-12 week lead) |
| **Budget** | BrailleMe | 20 | $515 | Custom piezo (8-12 week lead) |
| **Mid-Range** | Focus 40 | 40 | $1,700 | Custom piezo (8-12 week lead) |
| **Premium** | Brailliant BI 20X | 20 | $2,199 | Custom piezo (8-12 week lead) |

::: notes
Market context shows: (1) $515-$2,199 USD range for 20-40 chars, (2) 100% piezo monopoly, (3) all custom with 8-12 week lead time.
Our target: 32 chars @ $600 USD fills market gap between 20-cell budget and 40-cell mid-range.
COTS mandate (≤4 week lead) forces innovation beyond piezo monopoly.
:::

---

# Market Gap Analysis

## No Products in 25-35 Character Range at <$1,000 USD

**Technology Comparison:**

| Technology | Voltage | Size | Cost/Cell (BOM) | Lead Time | Market Share |
|------------|---------|------|-----------------|-----------|--------------|
| **Piezo (custom)** | 100-200V | 2-3mm | **$7-20 USD** | 8-12 weeks | **100%** |
| **Solenoid (COTS)** | 5-12V | 4mm+ | **$2-5 USD** | 2-4 weeks | **0%** |

**Our Opportunity:**
- **32 characters** (60% more than Orbit Reader 20)
- **$600 USD retail** ($200 USD BOM target)
- **COTS components** (≤4 week lead time) ← **UNIQUE**

::: notes
Market gap: No 25-35 char products <$1,000 USD.
Technology monopoly: 100% piezo, 0% solenoid (opportunity for innovation).
Our $6.25/cell BOM target is aggressive but achievable (vs $7.50-20 USD market).
COTS mandate differentiates from all competitors (custom piezo = 8-12 weeks).
Key numbers to remember: 32 chars = 192 dots (6 dots/char + 2 extended).
:::

---

# SECTION 1: Technical Requirements

## Design Step 1: Identify Key Technical Requirements (25/100 pts)

**Objective:** Define system, electrical, and relevant specifications

**Deliverables:**
- 17 requirements (9 ground truth + 6 assumptions + 2 standards)
- Requirements traceability matrix
- Standards compliance analysis

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

## Design Step 2: Develop Multiple Alternative Solutions (25/100 pts)

**Objective:** Create and describe distinct architecture options

**Deliverables:**
- 3 architectures with block diagrams
- Component selection rationale
- Pros/cons for each approach

::: notes
Section 2 of 4. This addresses PDF requirement: "Develop and describe multiple alternative solutions."
Each architecture optimizes DIFFERENT trade-off (cost vs UX vs innovation).
:::

---

# Architecture A: ARCH_PIEZO_ECO

## Piezo Economy (Wired, Standard)

![Architecture diagram](resources/diagrams/arch-piezo-eco-block.png)

**Key Features:**
- Piezoelectric actuators (100V nominal, 2.5mm pitch)
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

![Architecture diagram](resources/diagrams/arch-sol-eco-block.png)

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

![Architecture diagram](resources/diagrams/arch-piezo-dlx-block.png)

**Key Features:**
- Piezoelectric actuators (100V nominal, 2.5mm pitch)
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

## Design Step 3: Evaluate the Proposed Solutions (30/100 pts ← HIGHEST)

**Objective:** Discuss advantages, disadvantages, and other considerations

**Deliverables:**
- Evaluation framework with weighted criteria
- Quantitative comparison (cost, power, timeline)
- Sensitivity analysis ("what if" scenarios)
- Decision framework (context-dependent selection)

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

# EMI Compliance Trade-offs

## The GHz Antenna Challenge: Why Piezo Costs 2.5× More

**The Physics Problem:**

```
30mm Piezo Cantilever = Quarter-Wavelength Monopole Antenna
λ/4 @ 1.67 GHz (over PCB, ε_r=2.2) → 192 radiating antennas @ GHz
```

**Comparison:**

| Parameter | Solenoid (ARCH_SOL_ECO) | Piezo (ARCH_PIEZO_ECO/DLX) |
|-----------|-------------------------|----------------------------|
| **EMI Frequency** | <10 MHz (LC ringing) | **500 MHz - 1 GHz** ⚠️ |
| **Antenna Effect** | None (4mm << λ) | **30mm = λ/4 resonance** |
| **Mitigation Cost** | **$4.32** | **$10.84** (2.5× premium) |
| **Cert Risk** | LOW (10% fail) | HIGH (50% fail, +2 weeks) |
| **Rework Cost** | +$1.3K (expected) | **+$6.5K** (expected) |

**Key Insight:** 30mm is NOT "just a wire" at GHz — it's a resonant antenna!

::: notes
This is the senior EE differentiator: GHz antenna physics.
30mm cantilever = λ/4 monopole @ 1.67 GHz → FCC Part 15B most restrictive band.
Piezo pays 2.5× EMI cost premium BUT gets 1.6× faster refresh + zero hold power.
See backup deck (docs/slides/emi-analysis-slides.md) for detailed EMI budget analysis.
:::

---

# EMI Mitigation Strategy (Piezo)

## 5-Layer Defense: Firmware → PCB → Mechanical → Shielding → Testing

**Layered Mitigation Approach:**

| Layer | Technique | dB Reduction | Cost/Unit | Physics |
|-------|-----------|--------------|-----------|---------|
| **1. Firmware** | Sequential firing (8-way) | -28 dB | **$0** | √N radiation reduction |
| | Slew-rate limiting (1ms) | -40 dB | **$0** | f_max: 35 kHz → 350 Hz |
| **2. PCB** | Twisted differential pairs | -20 dB | $2.00 | Magnetic cancellation |
| | Ferrite beads (192×) | -15 dB | $3.84 | Z=600Ω @ 1 GHz |
| **3. Enclosure** | Shielded aluminum + gaskets | -30 dB | $4.00 | SE=30dB @ 1 GHz |
| **4. Testing** | Pre-compliance (Week 5-6) | N/A | $2.5K | Go/No-Go @ 6dB margin |

**Total Mitigation:** 133 dB reduction → **21 dB compliance margin** ✅

**Critical Insight:** Firmware alone (sequential + slew-rate) = **68 dB reduction at $0 hardware cost!**

::: notes
The key win: Software reduces EMI by 68 dB before any hardware cost.
Sequential firing: 192 → 8 parallel = √24 reduction = 27.6 dB.
Slew-rate: 10µs → 1ms rise time = 40 dB (Fourier bandwidth reduction).
Hardware mitigation adds defense-in-depth to reach 21 dB margin.
Pre-compliance testing in Week 5-6 (semi-anechoic chamber) catches issues before FCC cert.
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

## Design Step 4: Transition to Volume Production (20/100 pts)

**Objective:** Outline process from initial design to pilot production

**Deliverables:**
- 8-12 week production timeline (architecture-agnostic)
- Critical path analysis (actuator sourcing)
- Risk mitigation strategies
- DFM considerations

::: notes
Section 4 of 4. This addresses PDF requirement: "Outline the process for transitioning the concept from initial design to volume production."
Key insight: Same production process for all architectures, just different timeline/risk profiles.
THE critical path risk: Actuator sourcing (all architectures blocked without resolution).
:::

---

# ⚠️ Actuator Sourcing - THE Critical Path Risk

## All Architectures Blocked Without Resolution

![Three-path strategy](resources/diagrams/actuator-sourcing-decision.png)

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
5. Power supply design for 200V piezo? (Answer: DC-DC boost converter, see appendix slides for EMI deep-dive)
:::

---

# APPENDIX: Technical Deep-Dive Backup Slides

---

# Appendix A: Piezo EMI Challenge - Antenna Physics

## 30mm Cantilever = Quarter-Wavelength Monopole Antenna

```
         ↑ 30mm Piezo Cantilever
         │  (Bimorph, 100V drive)
         │
         │  λ/4 @ 2.5 GHz (free space)
         │  λ/4 @ 1.67 GHz (over PCB, ε_r=2.2)
         │
 ════════╪═══════  PCB Ground Plane
         │
      [Driver IC]
```

**Antenna Resonance Physics:**
```
f_resonant = c / (4 × L × √ε_r)
           = 3×10⁸ m/s / (4 × 0.030m × √2.2)
           = 1.67 GHz ⚠️
```

**Key Insight:** 30mm is NOT "just a wire" at GHz frequencies!
- **192 actuators** = 192 radiating antennas
- **100V switching** = high-voltage transients
- **GHz resonance** = FCC Part 15B most restrictive band (54 dBµV/m @ 3m)

::: notes
Deep-dive for technical questions on EMI physics.
This explains WHY piezo is fundamentally harder than solenoid for EMI.
:::

---

# Appendix B: EMI Budget Analysis - Detailed Breakdown

## From +84 dB Over Limit → 21 dB Compliance Margin

| Mitigation Step | Physics | dB Reduction | Cost/Unit | Cumulative Margin |
|-----------------|---------|--------------|-----------|-------------------|
| **Baseline (no mitigation)** | 192 actuators, 100V, 10µs rise | 0 dB | $0 | **+84 dB OVER FCC** ❌ |
| ↓ Sequential firing (8-way) | √24 reduction in sources | **-28 dB** | $0 (firmware) | +56 dB OVER ❌ |
| ↓ Slew-rate limiting (1 ms) | f_max: 35 kHz → 350 Hz | **-40 dB** | $3.84 | +16 dB OVER ❌ |
| ↓ Twisted-pair wiring | Magnetic field cancellation | **-20 dB** | $2.00 | -4 dB UNDER ⚠️ |
| ↓ Ferrite beads (192×) | Z=600Ω @ 1 GHz | **-15 dB** | $1.00 | -19 dB UNDER ✅ |
| ↓ Shielded enclosure | Faraday cage (SE=30dB) | **-30 dB** | $4.00 | **-49 dB UNDER ✅** |

**FCC Part 15B Class B Limit @ 1 GHz:** 54 dBµV/m @ 3m
**Final Margin:** 54 - 33 = **21 dB compliance margin** ✅

**Total EMI Cost:** $10.84/unit (vs $4.32 for solenoid)

::: notes
Quantitative EMI budget showing each mitigation technique contribution.
Key insight: Firmware alone (68 dB) gets us partway, hardware adds margin.
:::

---

# Appendix C: EMI Mitigation - 4-Layer Defense

## Firmware → PCB → Mechanical → Shielding

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: FIRMWARE (0 hardware cost)                        │
├─────────────────────────────────────────────────────────────┤
│  • Sequential firing: 192 → 8 parallel (-28 dB)             │
│  • Slew-rate limiting: 10µs → 1ms rise time (-40 dB)        │
│  Total: 68 dB reduction, $0 cost                            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  LAYER 2: PCB DESIGN (+$5.84/unit)                          │
├─────────────────────────────────────────────────────────────┤
│  • Twisted differential pairs (10 mil trace/gap) → -20 dB   │
│  • Ferrite beads (192×, 0805 pkg, Z=600Ω @ 1GHz) → -15 dB   │
│  • 4-layer stack: Top + GND + 100V + Bottom                 │
│  • Via stitching: 10mm pitch around actuator array          │
│  • HV clearance: 100 mil (IPC-2221 Class 2 @ 100V)          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  LAYER 3: SHIELDED ENCLOSURE (+$4.00/unit)                  │
├─────────────────────────────────────────────────────────────┤
│  • 0.5mm aluminum sheet (skin depth << thickness @ 1 GHz)   │
│  • Conductive gasket (CHO-SEAL 1298, 2m perimeter)          │
│  • Feedthrough π-filters (USB/BLE connectors, 100pF+10nF)   │
│  • Shielding effectiveness: SE = 30 dB @ 1 GHz              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  LAYER 4: PRE-COMPLIANCE TESTING (Week 5-6, $2.5K)          │
├─────────────────────────────────────────────────────────────┤
│  • Semi-anechoic chamber, LPDA antenna, spectrum analyzer   │
│  • Critical bands: 500 MHz - 2 GHz (piezo resonance)        │
│  • Go/No-Go: Pass with 6 dB margin → Proceed to FCC cert    │
└─────────────────────────────────────────────────────────────┘
```

::: notes
Detailed implementation plan for each mitigation layer.
Shows practical engineering: component specs, PCB design rules, testing strategy.
:::

---

# Appendix D: EMI Cost & Schedule Impact

## Solenoid vs Piezo Comparison

| Metric | ARCH_SOL_ECO (Solenoid) | ARCH_PIEZO_ECO (Piezo) | ARCH_PIEZO_DLX (Piezo+BLE) |
|--------|-------------------------|------------------------|----------------------------|
| **Actuator Type** | 4mm solenoid (inductive) | 30mm piezo cantilever | 30mm piezo + BLE radio |
| **Primary EMI** | 500 kHz - 5 MHz (LC ringing) | **500 MHz - 1 GHz** (antenna) | **1 GHz + 2.4 GHz** (coexist) |
| **Mitigation** | Flyback diode + slew-rate | 5 techniques (full suite) | + BLE partition shield |
| **EMI Cost** | **$4.32** ✅ | $10.84 | $12.84 |
| **EMI Premium** | Baseline | **+$6.52 (+151%)** | **+$8.52 (+197%)** |
| **Cert Risk** | **LOW (10% fail)** | HIGH (50% fail) | VERY HIGH (60% fail + BLE) |
| **Rework Schedule** | +0.4 weeks (expected) | **+2 weeks** (expected) | +3 weeks (expected) |
| **Rework Cost** | +$1.3K (expected) | **+$6.5K** (expected) | +$8K (expected) |

**Schedule Impact if Pre-Compliance Fails:**
- Root cause analysis: 3-5 days
- PCB re-spin: 2-3 weeks (layout + fab + assembly)
- Re-test: 1 week
- **Total delay per iteration: 4-6 weeks** ⚠️

**EMI Mitigation Premium:** Piezo pays **2.5× cost** vs solenoid for GHz compliance

::: notes
Risk quantification for project planning.
Expected value calculation: 50% × 2 weeks = 1 week expected schedule slip for piezo.
:::

---

# Appendix E: Fourier Analysis & Rise Time

## Fundamental Relationship: f_max ≈ 0.35 / τ_rise

**Fundamental relationship:**
```
f_max ≈ 0.35 / τ_rise    (Bandwidth of trapezoidal pulse)

Example:
10 µs rise time → f_max = 35 kHz (uncontrolled MOSFET)
1 ms slew-rate  → f_max = 350 Hz (RC gate driver)

EMI reduction: 20 × log₁₀(1ms / 10µs) = 40 dB
```

**Harmonic content:**
- Fundamental: f_max (0 dB)
- Higher harmonics: -20 dB/decade rolloff (6 dB/octave)
- At 1 GHz (28,571× harmonic): -89 dB attenuation
- BUT: Antenna resonance amplifies by Q ≈ 20 → +20 dB gain

**Net effect:** Even deep harmonics radiate efficiently at antenna resonance!

::: notes
Explains the PHYSICS behind slew-rate limiting EMI reduction.
Shows senior-level understanding of signal processing and RF.
:::

---

# Appendix F: BLE Coexistence Risk (ARCH_PIEZO_DLX)

## Interference Mechanisms & Mitigation

**Interference mechanisms:**
1. **Harmonic overlap:** Piezo 2nd harmonic @ 3.4 GHz (close to 2.4 GHz BLE)
2. **Broadband noise floor:** Switching transients raise noise at 2.4 GHz
3. **Desensitization:** BLE RX front-end overload from in-band EMI

**Mitigation:**
- Time-division multiplexing (disable actuators during BLE TX/RX)
- BLE antenna isolation (opposite side of PCB)
- Internal shield partition (SE ≥ 20 dB between actuator/BLE zones)

**Testing:**
- BLE link quality during actuator operation
- Packet Error Rate (PER) < 1% @ 5m distance
- RSSI degradation < 3 dB during switching

**Cost:** +$2.00 (shield partition) + $2,000 (coexistence testing)

::: notes
ARCH_PIEZO_DLX specific challenge: BLE radio + GHz piezo EMI in same enclosure.
Shows understanding of RF coexistence issues.
:::

---

# Appendix G: FCC Part 15B Limits

## Regulatory Compliance Standards

| Frequency Range | Class B Limit (dBµV/m @ 3m) | Physical Band |
|-----------------|----------------------------|---------------|
| 30 - 88 MHz     | 40.0                       | VHF TV |
| 88 - 216 MHz    | 43.5                       | FM radio, TV Band III |
| 216 - 960 MHz   | 46.0                       | UHF TV, cellular |
| **> 960 MHz**   | **54.0** ⚠️                | **Cellular, WiFi, BLE** |

**Key insight:** Limits are **14 dB more relaxed** at GHz vs VHF
- BUT: 30mm antenna radiates **efficiently** at 1.67 GHz
- Net effect: GHz band is the **limiting constraint** for piezo compliance

**Pre-compliance testing must focus on 500 MHz - 2 GHz range!**

::: notes
Shows understanding of regulatory landscape and test strategy.
Explains why GHz is harder despite relaxed limits (antenna efficiency).
:::
