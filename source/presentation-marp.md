---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-size: 24px;
    padding: 50px;
  }
  h1 {
    font-size: 40px;
    color: #2c3e50;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 3px solid #3498db;
  }
  h2 {
    font-size: 32px;
    color: #34495e;
    margin-top: 10px;
    margin-bottom: 15px;
  }
  table {
    font-size: 20px;
    margin: 20px auto;
    border-collapse: collapse;
  }
  table thead th {
    background-color: #2980b9 !important;
    color: #ffffff !important;
    font-weight: bold;
    padding: 10px 12px;
    border: 2px solid #2c3e50;
  }
  table tbody tr:nth-child(even) {
    background-color: #ecf0f1;
  }
  table tbody tr:nth-child(odd) {
    background-color: #ffffff;
  }
  table td, table th {
    padding: 8px 12px;
    border: 1px solid #95a5a6;
  }
  table tbody td {
    color: #2c3e50;
  }
  code {
    font-size: 18px;
  }
  img {
    max-width: 90%;
    max-height: 500px;
    display: block;
    margin: 20px auto;
  }
  /* Normal text wrapping */
  p, li, td, th {
    white-space: normal;
  }
  strong {
    white-space: nowrap;
  }
  /* Takeaway message box (use > blockquote at bottom of slide) */
  blockquote {
    background-color: #eaf4fb;
    border-left: 5px solid #2980b9;
    padding: 12px 20px;
    margin: 30px 20px 10px 20px;
    font-size: 20px;
    font-weight: bold;
    color: #2c3e50;
    border-radius: 5px;
  }
  blockquote strong {
    color: #3498db;
  }
---

# Braille Display - Concept Evaluation

**Electrical Engineering Design for Portable Cell Phone Companion Device**

<img src="images/orbit-reader-20_20percent.jpg" alt="Orbit Reader 20">

Spencer Barrett
LAM Research EE5 Interview
October 2025

<!-- Speaker notes: 30 seconds introduction. State name, position applied for, and agenda overview. -->

---

# Agenda

**Four-Part Design Process:**

1. **Identify Key Technical Requirements** 
   - System, electrical, and relevant specifications
2. **Develop Multiple Alternative Solutions** 
   - 3 distinct architectures
3. **Evaluate the Proposed Solutions** 
   - Advantages, disadvantages, and trade-off analysis
4. **Transition to Volume Production**
   - Process from initial design to pilot production

<!-- Speaker notes: Explicitly map to PDF rubric structure. Emphasize: This is not "find the best solution" - it's "navigate trade-offs and provide decision framework." -->

---

# Problem Statement - Ground Truth Requirements

<style scoped>
table {
  font-size: 16px;
}
.vague { color: #f39c12; font-weight: bold; }
.clear { color: #27ae60; font-weight: bold; }
</style>

| ID | Requirement | Assumptions |
|----|-------------|-------------|
| [PRD-SCHED-001](appendix/requirements.pdf#prd-sched-001-production-timeline---two-month-release) | Production Timeline - Two Month Release | <span class="vague">VAGUE</span> Pilot Prod x300 *(COTS 4x week lead time)* |
| [PRD-SIZE-001](appendix/requirements.pdf#prd-size-001-portable-device) | Portable Device | <span class="vague">VAGUE</span> ≤1.3 lbs (590g), fits in bag |
| [PRD-IFACE-001](appendix/requirements.pdf#prd-iface-001-cell-phone-connectivity---pairing-and-connection) | Cell Phone Connectivity | <span class="vague">VAGUE</span> BLE or USB-C, GATT/HID|
| [PRD-IFACE-002](appendix/requirements.pdf#prd-iface-002-text-data-reception---braille-output) | Text Data Reception | <span class="vague">VAGUE</span> ASCII -> Grade 1 braille|
| [PRD-COST-001](appendix/requirements.pdf#prd-cost-001-low-cost-at-volume) | Low Cost at Volume | <span class="vague">VAGUE</span> $200 ±$100 BOM ($100-$300) |
| [PRD-VOL-001](appendix/requirements.pdf#prd-vol-001-high-volume-production-design) | High Volume Production Design | <span class="vague">VAGUE</span> 10k units/month SMT assembly |
| [PRD-USER-001](appendix/requirements.pdf#prd-user-001-sight-impaired-user) | Sight-Impaired User | <span class="clear">CLEAR</span> ADA 703.3 |
| [PRD-FUNC-001](appendix/requirements.pdf#prd-func-001-single-line-braille-display---32-characters-6-dots-each) | 32 chars × 6 dots = 192 actuators | <span class="clear">CLEAR</span> ADA 703.3 |
| [PRD-FUNC-002](appendix/requirements.pdf#prd-func-002-braille-line-update-refresh-next-line) | Braille Line Update | <span class="vague">VAGUE</span> <2 sec refresh, UP/DOWN buttons |

> **TAKEAWAY:** 7 of 10 requirements need clarification before commit.

<!-- Strategic framing: "I read the spec CAREFULLY and extracted requirements." "7 of 10 are vague - I need YOUR feedback before building the wrong thing."  The most challenging constraint - 2mo deadline -> 4x week leadtime -->

---

# Mechanical Requirements (from US ADA 703.3)

| REQ-ID | Requirement Title | Specification Range |
|--------|-------------------|---------------------|
| [PRD-MECH-001](appendix/requirements.pdf#prd-mech-001-dot-diameter---ada-7033-compliance) | Dot Diameter - ADA 703.3 Compliance | 1.5-1.6 mm |
| [PRD-MECH-002](appendix/requirements.pdf#prd-mech-002-dot-height-raised-position---ada-7033) | Dot Height (Raised Position) - ADA 703.3 | 0.64-0.94 mm |
| [PRD-MECH-003](appendix/requirements.pdf#prd-mech-003-dot-spacing-within-cell---ada-7033) | Dot Spacing Within Cell - ADA 703.3 | 2.3-2.5 mm |
| [PRD-MECH-004](appendix/requirements.pdf#prd-mech-004-cell-spacing-horizontal-between-characters---ada-7033) | Cell Spacing (Horizontal Between Characters) - ADA 703.3 | 6.1-7.6 mm |
| [PRD-MECH-006](appendix/requirements.pdf#prd-mech-006-dot-holding-force---tactile-feedback) | Dot Holding Force - Tactile Feedback | 50-100 grams |

**Hard requirement - Braille dimension standards ensure tactile readability**

> **TAKEAWAY:** ADA 703.3 defines 5 critical dimensions driving design.

<!-- ADA 703.3 standards define minimum requirements for braille readability. PRD-MECH-005 (dot shape) intentionally omitted - implicit in actuator design. Click requirement ID for detailed specification in appendix
-->

---

# Actuator Technology Brainstorming

<style scoped>
table {
  font-size: 16px;
}
table td {
  white-space: nowrap;
}
.pass { color: #27ae60; font-weight: bold; }
.fail { color: #e74c3c; font-weight: bold; }
.warn { color: #f39c12; font-weight: bold; }
</style>

| Technology | Size (mm) | Force (N) | Speed (ms) | Hold PWR (W) | $/PIN (USD) | Verdict |
|------------|-----------|-----------|------------|--------------|-------------|---------|
| **Piezo** | <span class="pass">2</span> | <span class="pass">0.5-1.5</span> | <span class="pass">10-50</span> | <span class="pass">~0</span> | <span class="fail">1.50</span> | <span class="fail">**BASELINE (EMI RISK)**</span> |
| **Solenoid** | <span class="fail">4</span> | <span class="pass">0.5-2.0</span> | <span class="pass">20-100</span> | <span class="fail">9.6-19</span> | <span class="pass">0.50-0.80</span> | <span class="fail">**If size relaxed**</span> |
| **Solenoid (Latch)** | <span class="fail">4</span> | <span class="pass">0.5-2.0</span> | <span class="pass">20-100</span> | <span class="pass">~0</span> | <span class="fail">1.00-1.50</span> | <span class="fail">**If size relaxed**</span> |
| **SMA Wire** | <span class="pass">0.15</span> | <span class="fail">0.1-0.5</span> | <span class="fail">700-1500</span> | <span class="fail">38-96</span> | <span class="pass">0.10-0.30</span> | <span class="fail">**Too slow/weak**</span> |
| **Voice Coil** | <span class="fail">6</span> | <span class="pass">0.5-3.0</span> | <span class="pass">5-20</span> | <span class="fail">9.6-29</span> | <span class="fail">2.00-3.00</span> | <span class="fail">**Too expensive**</span> |
| **MEMS** | <span class="pass">2-5</span> | <span class="fail">0.001-0.01</span> | <span class="pass">1-10</span> | <span class="pass">~0</span> | <span class="fail">5.00-20.00</span> | <span class="fail">**Insufficient force**</span> |

**Key Constraint:** Actuator size ≤2.3mm (derived from 2.5mm ADA braille pitch)

**Solution:** Mechanical lever mechanism enables 6-7mm custom solenoid → 2.5mm pitch compliance

> **TAKEAWAY:** NO COTS actuators exist - mechanical levers enable solution.

<!-- Speaker notes: "Evaluated 5 actuator technologies against hard constraints: size ≤2.3mm, force 50-100gf, speed <100ms, low hold power." "Piezo is ONLY technology meeting all requirements as-is." "BUT - relaxing size constraint 2.3mm→4mm enables COTS solenoids with 47-67% cost savings." "SMA wire too slow (22-48 sec refresh), Voice Coil too expensive ($384-576), MEMS insufficient force." "This is engineering trade-offs in action - there's no perfect solution." Reference: docs/actuator-technology-tradeoff.md for detailed analysis of all 5 technologies. -->

---

# Commercial Braille Display Market (Price vs Character)

| Segment | CHAR | Total Pins | Retail Price | Est EE BOM* | $/Pin (BOM) | Example Products |
|---------|------|------------|--------------|-------------|-------------|------------------|
| **Budget** | 20 | 160 (8/char) | $449-$515 | $150-$170 | $0.94-$1.06 | Orbit Reader 20, BrailleMe |
| **Budget** | 40 | 320 (8/char) | ~$800 | ~$265 | ~$0.83 | Orbit Reader 40 |
| **Mid-Range** | 20 | 160 (8/char) | ~$1,200 | ~$400 | ~$2.50 | Brailliant BI 20x |
| **Mid-Range** | 40 | 320 (8/char) | ~$1,700 | ~$565 | ~$1.77 | Focus 40, Brailliant BI 40x |
| **Premium** | 40+ | 320+ (8/char) | $2,000+ | $665+ | ~$2.08+ | Mantis Q40, Graphiti Plus |

- **Our Target:** 32 char × 6 pins = 192 pins @ $200 BOM = **$1.04/pin** (competitive with budget segment) 
- ***\* List price** = BOM × 3 (EE industry standard markup)*
- **Key Finding:** 100% of commercial displays use **custom piezoelectric actuators** (8 pins/char)

> **TAKEAWAY:** Budget segment is $0.83-$1.06/pin - our $1.04/pin target  with 6-pin design

<!-- Speaker notes: "Commercial displays use 8 pins/char (6 standard + 2 computer braille), we use 6 pins (Grade 1 only)." "$0.83/pin is market floor (Orbit Reader 40)." "Our $1.04/pin is competitive - middle of budget range." "3× markup validated against Orbit Reader: $449 retail ÷ 3 = $150 BOM ÷ 160 pins = $0.94/pin." Reference: docs/market-braille-display-scan.md for detailed market analysis. -->

---

# Market Gap Analysis (Piezo vs COTS Solenoid)

| Technology | Voltage | Size | Cost/Cell | Lead Time | Market Share |
|------------|---------|------|-----------|-----------|--------------|
| **Piezo (custom)** | 100-200V | 2-3mm | **$2** | 8-12 weeks | **100%** |
| **Solenoid (COTS)** | 5-12V | 4mm+ | **$1.7** | 2-4 weeks | **0%** |

**OUR OPPORTUNITY:**  - **32 characters** (25% fewer pins/char -> Cheaper)  - **$1000 USD retail** ($330 USD BOM @ $1.70/pin target) -

<div style="display: flex; justify-content: space-around; align-items: center;">
  <div style="width: 45%;">
    <img src="images/orbit-reader-20_15percent.jpg" alt="Orbit Reader 20">
    <p><strong>Orbit Reader 20</strong><br>20 chars | $799 USD<br>"World's most affordable"</p>
  </div>
  <div style="width: 45%;">
    <img src="images/brailliant-bi-20x_15percent.jpg" alt="Brailliant BI 20X">
    <p><strong>Brailliant BI 20X</strong><br>20 chars | $2,199 USD<br>Professional grade</p>
  </div>
</div>

**Our target:** 32 chars @ $600 USD (60% more characters, competitive pricing)

<!-- Speaker notes: "No COTS-based braille displays exist commercially" - we're breaking piezo monopoly. "ARCH_SOL_ECO at $277 BOM saves 54% cost" vs custom piezo. Emphasize 2-month timeline REQUIRES COTS (can't wait 8-12 weeks). Show physical products to establish credibility. Orbit Reader 20 is education market leader. Brailliant is professional standard. Both use custom piezo actuators. Our 32-cell design fills gap between budget 20-cell and premium 40-cell products. -->

---

# Tech Req Database (S.M.A.R.T goals)

**SMART Criteria:** Specific, Measurable, Achievable, Relevant, Testable

**Key Fields:** Title | Source | Priority (P0/P1/P2) | Status (Clear/Vague) | Acceptance Criteria | Verification | Risk Level

**17 Requirements Grouped by Category:**

- **Timeline:** [PRD-SCHED-001](appendix/requirements.pdf#prd-sched-001-production-timeline---two-month-release) (2mo pilot, COTS ≤4wk lead)
- **Size/Portability:** [PRD-SIZE-001](appendix/requirements.pdf#prd-size-001-portable-device) (≤1.3 lbs, bag-portable)
- **Interface:** [PRD-IFACE-001](appendix/requirements.pdf#prd-iface-001-cell-phone-connectivity---pairing-and-connection) (BLE/USB-C) | [PRD-IFACE-002](appendix/requirements.pdf#prd-iface-002-text-data-reception---braille-output) (ASCII→Grade 1 braille)
- **Cost:** [PRD-COST-001](appendix/requirements.pdf#prd-cost-001-low-cost-at-volume) ($200±$100 BOM, $1.04/pin)
- **Manufacturing:** [PRD-VOL-001](appendix/requirements.pdf#prd-vol-001-high-volume-production-design) (10k/mo, SMT)
- **User:** [PRD-USER-001](appendix/requirements.pdf#prd-user-001-sight-impaired-user) (Sight-impaired, ADA 703.3)
- **Functional:** [PRD-FUNC-001](appendix/requirements.pdf#prd-func-001-single-line-braille-display---32-characters-6-dots-each) (32×6=192 pins) | [PRD-FUNC-002](appendix/requirements.pdf#prd-func-002-braille-line-update-refresh-next-line) (<2s refresh) | [PRD-FUNC-003](appendix/requirements.pdf#prd-func-003-braille-dot-actuation---raised-or-lowered) (Binary actuation)
- **Mechanical (ADA):** [MECH-001](appendix/requirements.pdf#prd-mech-001-dot-diameter---ada-7033-compliance) (Ø1.5-1.6mm) | [MECH-002](appendix/requirements.pdf#prd-mech-002-dot-height-raised-position---ada-7033) (H0.64-0.94mm) | [MECH-003](appendix/requirements.pdf#prd-mech-003-dot-spacing-within-cell---ada-7033) (2.3-2.5mm) | [MECH-004](appendix/requirements.pdf#prd-mech-004-cell-spacing-horizontal-between-characters---ada-7033) (6.1-7.6mm) | [MECH-006](appendix/requirements.pdf#prd-mech-006-dot-holding-force---tactile-feedback) (50-100g force)
- **Standards:** [NFR-STD-001](appendix/requirements.pdf#nfr-std-001-north-america-regulatory-compliance-ul--fcc) (UL/FCC) | [NFR-STD-002](appendix/requirements.pdf#nfr-std-002-accessibility-standards-compliance-us-ada) (ADA 703.3)

> **TAKEAWAY:** 17 requirements total, all SMART-testable with acceptance criteria.

<!-- Speaker notes: "Every requirement has SMART structure - not just 'portable', but ≤1.3 lbs with bag-portability test. Not just 'low-cost', but $200±$100 BOM with sensitivity range. This is engineering rigor - assumptions documented, risks quantified, trade-offs tested in v1.4.0." "Click any REQ-ID for full specification in appendix." Reference full database: source/requirements.yaml (1090 lines, auto-generates requirements.md and traceability matrix). -->

---

# Develop Multiple Alternative Solutions

## Design Step 2 of 4

<img src="images/orbit-reader-20_20percent.jpg" alt="Orbit Reader 20">

<!-- Section title slide - clean delimiter between phases -->

---

# Systems Engineering Philosophy

## Trade-offs Over Perfection

**CRITICAL CONSTRAINT - Show Stopper:**
- **2-month production requirement** → REQUIRES COTS components (≤4 week lead time)
- **Problem:** NO COTS actuators exist - searched 6-7mm solenoids, 2mm piezos - all custom >4wk
- **Reality:** ALL architectures require custom actuators → >8 week timeline (violates 2mo requirement)

**Core Principles:**
1. **Requirements exist in RANGES, not absolutes** - $100-$300 BOM (not "$200")
2. **Value engineering over feature creep** - Same function, lower cost, higher reliability
3. **Simplification drives reliability** - Fewer components = higher MTBF

> **TAKEAWAY:** NO COTS actuators - ALL architectures violate 2mo timeline.

<!-- This is the thesis: When electrical components can't solve the problem, mechanical innovation can. ARCH_SOL_ECO uses levers to bridge the gap between 6mm COTS actuators and 2.5mm ADA requirement. This is senior-level engineering - recognize when the solution isn't in the electrical domain. Junior engineers design components. Senior engineers design systems with explicit trade-offs. -->

---

# Architecture Overview - 3 Architectures, 3 Trade-offs

<style scoped>
.pass { color: #27ae60; font-weight: bold; }
.fail { color: #e74c3c; font-weight: bold; }
table {
  font-size: 18px;
}
</style>

| Attribute | SOL_ECO | PIEZO_ECO | PIEZO_DLX |
|-----------|---------|-----------|-----------|
| **Market Position** | Economy / Budget | Entry / Education | Premium / Pro |
| **Communication** | USB-C (Wired) | USB-C (Wired) | BLE Wireless |
| **Power Source** | USB Bus-Powered | USB Bus-Powered | Li-ion Battery + Charger |
| **Actuator Type** | Solenoid-12V | 2mm Piezo-100V | 2mm Piezo-100V |
| **Mechanical** | Lever (6mm→2.5mm) | Direct drive | Direct drive |
| **Timeline** | <span class="fail">>8wk (custom >4wk)</span> | <span class="fail">>8wk (custom >4wk)</span> | <span class="fail">>8wk (custom >4wk)</span> |
| **BOM Actual** | **$505.71** | **$591.99** | **$605.67** |
| **$/Actuator** | **$1.70** | **$2.00** | **$2.00** |
| **Key Trade-off** | **ME complexity (lever)** | **EMI risk (λ/4 antenna)** | **EMI + BLE cert risk** |

> **TAKEAWAY:** SOL_ECO wins on cost: $505.71 BOM via 15% actuator savings.

<!-- Speaker notes: "These are ACTUAL BOM costs from detailed parts sourcing, not back-of-envelope. All 3 architectures currently over target - this is honest engineering. Primary driver: actuators ($288 for piezo, $96 for solenoid). ARCH_SOL_ECO wins on cost-performance - only 46% over target. We have clear cost-down strategies: volume pricing, cell count reduction, value engineering. This is the reality of pilot vs volume economics." -->

---

# Power Requirements - Actuation Strategy

<style scoped>
table {
  font-size: 17px;
}
</style>

## Comparison: Power per Actuation

| Parameter | **PIEZO (Capacitive)** | **SOLENOID (Inductive + Bistable)** |
|-----------|------------------------|-------------------------------------|
| **Voltage** | 100V (unipolar drive) | 5V |
| **Current (peak)** | 5 µA (slew-limited) | 630 mA |
| **Actuation time** | 1 ms rise + 81 ms dwell | 50 ms pulse (magnet holds after) |
| **Capacitance/Inductance** | 50 nF | 10 mH (6Ω coil) |
| **Energy per pulse** | 250 µJ (E = ½CV²) | **121,000 µJ** (E = ½Li² + i²Rt) |
| **Hold power** | 0W (capacitive) | **0W (NdFeB magnet latch)** |
| **Avg power (worst-case)** | 2.16W (constant refresh) | **0.63W (3.4× lower!)** |

**Key Insight:** i = C(dV/dt) vs V = L(di/dt) — Bistable operation = **3.4× lower power** despite 480× higher energy/pulse

***Note:** Piezo drive assumes unipolar (0-100V) unimorph config. Bipolar drive (±100V, 2 drivers/actuator) available if more displacement needed*

<!-- Speaker notes: "This table shows the electrical parameters - look at that energy contrast: 250 microjoules versus 121,000 microjoules. Solenoid uses nearly FIVE HUNDRED TIMES more energy per pulse. Yet somehow it wins on average power - we'll see why on the next slide when we talk about sparse updates.

PIEZO - Capacitive Load (i = C × dV/dt):
- 50 nanofarad capacitor charged to 100 volts in 1 millisecond (slew-rate limited for EMI)
- Current: i = C × dV/dt = 50nF × 100,000 V/s = 5 microamps
- The 81ms 'dwell time' is just timing budget allocation - electrically it's charged in 1ms, but mechanically the piezo cantilever needs to settle (stop ringing) before we can trust the position is stable
- Energy: E = ½CV² = ½ × 50nF × 100V² = 250 microjoules per charge
- Raised dots experience leakage*(MechanicalCreep)* - domain walls drift, requiring ~60Hz refresh to maintain 0.7mm height

PIEZO MECHANICAL CONFIG (30mm cantilever):
- Bimorph cantilever: PZT top layer + metal shim (unimorph variant, not true bimorph with 2 active PZT layers)
- Unipolar drive: 0V → +100V on top layer (1 driver per actuator = 192 total drivers)
- Braille pin mounted PERPENDICULAR at cantilever TIP (not stacked parallel)
- Why? Cantilever deflection δ ∝ L³ → 30mm gives ~1mm tip displacement → pin pushes UP through display surface
- Drive options if more displacement needed: (1) Bipolar ±100V (2× displacement, 2× drivers, +$216 BOM), (2) Longer cantilever (35-40mm)

SOLENOID - Inductive Load (V = L × di/dt):
- 10 millihenry coil with 6 ohm resistance, 630 milliamps peak current
- Energy breakdown: ½Li² (stored magnetically, 2mJ) + i²Rt (wasted as heat in coil resistance, 119mJ) = 121 millijoules total
- That's 121,000 microjoules - look at the table, it's nearly 500× higher than piezo!
- BUT - bistable mechanical latch with NdFeB magnet holds the cam position with ZERO electrical power
- We'll see on the next slide how sparse updates flip this around - we only pulse the dots that CHANGE state

The paradox resolves when you realize: high energy per pulse doesn't matter if you have **zero hold power** (bistable latch). Piezo must continuously refresh all dots (capacitor leakage), Solenoid only pulses during line changes." -->

## Power & Timing Comparison (Worst Case: All 192 Dots Change)

| Actuator | Hold Power | Energy/Pulse | Sequential Timing (8-way parallel) | Peak Current | Avg Power |
|----------|------------|--------------|-------------------------------------|--------------|-----------|
| **Piezo** | 0W (capacitive) | 250 µJ | 24 groups × 83ms = **1.99s** ✓ | 40µA (slew-limited) | **2.16W** |
| **Solenoid** | **0W (magnet latch)** | 121 mJ | 24 groups × 50ms = **1.2s** ✓ | 5.04A @ 5V | **0.63W** |

**Sequential Firing Timing (192 dots ÷ 8 parallel = 24 groups):**
```
  0ms       500ms      1000ms     1500ms     2000ms
  |----------|----------|----------|----------|
PIEZO (83ms/group):
  [===][===][===][===][===][===]...[===][===]  ← 1.99s total
   ↑    ↑    ↑    ↑    ↑    ↑        ↑    ↑
  100V 100V 100V 100V 100V 100V    100V 100V   ← EMI source: dV/dt

SOLENOID (50ms/group):
  [==][==][==][==][==][==]...[==][==]          ← 1.2s total
   ↑   ↑   ↑   ↑   ↑   ↑       ↑   ↑
  630mA   630mA   630mA       630mA             ← EMI source: di/dt
```

**Key Insight:** Sequential firing reduces EMI by **28 dB** (1/24th simultaneous radiators) + spreads peak current

<!-- Speaker notes: "This table shows WORST CASE timing - all 192 dots changing at once. Both architectures meet the <2 second requirement.

THE ASCII CHART - Sequential Firing EMI Reduction:
- Why 24 groups gives 28 dB EMI reduction? Physics of coherent radiators.
- If we fired all 192 dots simultaneously, we'd have 192 antennas radiating at once
- Sequential firing: 192 ÷ 8 parallel = 24 groups, so only 8 dots active at any moment
- EMI field strength adds LINEARLY for coherent sources: E ∝ N
- But EMI power goes as the SQUARE: Power ∝ E² ∝ N²
- Ratio: (192)² / (8)² = 36,864 / 64 = 576
- In dB: 10 × log₁₀(576) = 27.6 dB ≈ 28 dB reduction!
- Plus we spread peak current from 96A (192 × 500mA) down to 4A (8 × 500mA) - fits USB budget!

SQUARE LAW PHYSICS - Why Voltage/Speed Doubles → Power Quadruples:

EMI Radiated Power Example:
- Piezo @ 100V: i = C(dV/dt) = 50nF × (100V/1ms) = 5µA → Radiated power ∝ i²
- Piezo @ 200V: i = 50nF × (200V/1ms) = 10µA → Radiated power ∝ (2i)² = 4i² → 4× EMI (+6 dB)
- This is why we're stuck at 100V - going to 200V quadruples EMI, not just doubles it!

Motor Kinetic Energy Analogy (same physics!):
- Move motor from A to B in HALF the time:
- Velocity must double: v → 2v (same distance, half time)
- Viscous drag force doubles: F_drag ∝ v → 2F
- Power against drag: P = F×v = (2F)×(2v) = 4×P (quadruples!)
- Same square law: P ∝ v²

This is fundamental physics - any time you have quadratic losses (I²R, drag ∝ v², radiated power ∝ i²),
doubling the driving parameter (voltage, velocity, current) QUADRUPLES the power dissipation!

Here's where bistable operation shines - WORST CASE ANALYSIS:
- Continuous braille text reading: 100% dots change (conservative assumption, simpler model)
- All 192 dots must be updated every line
- Reading speed: 10 lines/min = 1 line every 6 seconds (beginner pace)

SOLENOID Worst-Case Performance:
- 192 dots changed (100% worst case)
- 192 ÷ 8 parallel = 24 groups
- 24 groups × 50ms = 1.2s to actuate all dots
- Energy: 192 × 121mJ = 23.2J per full refresh
- Average power: 23.2J / 6s = 3.87W during actuation, averaged over 6s cycle = 0.63W

PIEZO can't do sparse updates - capacitors leak, must **continuously refresh** all 192 dots regardless of reading rate.

So the trade-off is: Solenoid uses 480× more energy PER PULSE, but **only pulses during line changes** (every 6 seconds). Piezo must **continuously power** all capacitors. Net result: 3.4× lower average power despite higher energy per pulse." -->

---

## EMI - PIEZO: P ∝ [C × (dV/dt)]²

| Parameter | **WITHOUT Slew-Rate Limiting** | **WITH Slew-Rate Limiting** |
|-----------|--------------------------------|------------------------------|
| **Mitigation** | Fast switching (hard-switched) | **RC gate driver (controlled rise)** |
| **Edge speed** | 10 µs rise time | **1 ms rise time (100× slower)** |
| **Rate (dV/dt)** | 100V / 10µs = 10,000,000 V/s | **100V / 1ms = 100,000 V/s** |
| **Peak current** | i = 50nF × 10M V/s = **500 mA** | **i = 50nF × 100k V/s = 5 mA** |
| **Harmonic bandwidth** | f_max = 0.35 / 10µs = **35 MHz** (extends to GHz) | **f_max = 0.35 / 1ms = 350 Hz** |
| **EMI Reduction** | Baseline | **-40 dB (100× current reduction)** |
| **FCC Part 15B Margin** | **FAIL (40 dB over limit @ 30-88 MHz)** | **PASS (+20 dB margin)** |

1. Fast voltage edges → displacement current → EMI radiation
2. **30mm piezo cantilever = λ/4 monopole @ 1.67 GHz** → 192 radiating antennas!
3. Combined with sequential firing (-28 dB): Total **-68 dB firmware EMI reduction at zero hardware cost**

**Note:** Analysis assumes **unshielded plastic enclosure** - aluminum shield adds optional -30 dB margin

<!-- Speaker notes: TAKEAWAY: Slew-rate limiting kills high-frequency harmonics at zero hardware cost -->

---

## EMI - SOLENOID: P ∝ [L × (di/dt)]²

| Parameter | **WITHOUT Flyback Diode** | **WITH Flyback Diode** |
|-----------|---------------------------|------------------------|
| **Mitigation** | MOSFET hard turn-off | **Diode energy recirculation** |
| **Edge speed** | 1 µs turn-off (fast MOSFET) | **10 ms ramp-down (diode path)** |
| **Rate (di/dt)** | 630mA / 1µs = 630,000 A/s | **630mA / 10ms = 63 A/s** |
| **Back-EMF spike** | V = 10mH × 630k A/s = **6,300V** | **V = 10mH × 63 A/s = 0.63V (clamped to 5.7V)** |
| **Component Risk** | **DESTRUCTIVE! (kills MOSFET)** | **SAFE (< 60V rating)** |
| **Voltage Reduction** | Baseline | **1,107× reduction (6,300V → 5.7V)** |
| **FCC Part 15B Margin** | **FAIL (broadband transient EMI)** | **PASS (+15 dB margin, low-voltage clamp)** |

1. Fast current turn-off → back-EMF voltage spike → Component destruction
2. **Flyback diode provides energy recirculation path** → Prevents inductive kickback
3. Combined with sequential firing (-28 dB): Reduces simultaneous radiators 192→8

**Note:** Analysis assumes **unshielded plastic enclosure** - aluminum shield adds optional -30 dB margin

<!-- Speaker notes: TAKEAWAY: Flyback diode is mandatory for inductive loads — protects components AND reduces EMI -->

---

## Power Budget Breakdown by Architecture

| Subsystem | PIEZO_ECO | PIEZO_DLX | SOL_ECO (Bistable) |
|-----------|-----------|-----------|---------------------|
| **Actuators** | 0.60W (refresh ALL dots) | 0.60W | **0.38W** (pulse ALL dots, 100% worst-case) |
| **Drivers** | 0.15W (24× HV driver) | 0.15W | 0.10W (3× ULN2803A, lower duty) |
| **Control + I/O** | 0.36W (STM32 + I2C) | 0.36W | 0.10W (lower scan rate) |
| **Boost Converter** | 1.00W (5V→100V, 85% η) | 1.00W (3.7V→100V) | 0 (no boost needed, 5V direct) |
| **Communication** | 0.05W (USB-C) | 0.05W (BLE nRF52840) | 0.05W (USB-C) |
| **TOTAL** | **2.16W** | **2.16W** | **0.63W** (3.4× lower!) |

***Note:** Final piezo power analysis must account for leakage*(MechanicalCreep)* refresh at ~60Hz to maintain raised dot position*

---

## Power Source Capability

<style scoped>
table {
  font-size: 16px;
}
.pass { color: #27ae60; font-weight: bold; }
.fail { color: #e74c3c; font-weight: bold; }
</style>

**Power Assumptions:** Reading rate = 10 lines/min (6s/line, beginner pace), **worst-case: 100% dots change** (continuous reading)

| Power Source | Voltage | Capacity | Continuous Power | PIEZO (2.16W) | SOL Bistable (0.63W) |
|--------------|---------|----------|------------------|---------------|----------------------|
| **USB-C** (bus-powered) | 5V | 500mA max | **2.5W** | <span class="pass">✓ 86% util</span> | <span class="pass">✓ 25% util</span> |
| **Li-ion 18650** | 3.7V nominal | 2500mAh (9.25Wh) | **3.7W** (2 hrs) | <span class="pass">✓ 58% util (4.3 hrs)</span> | <span class="pass">✓ 17% util (15 hrs)</span> |

**USB-C Android Phone Connection:**
- Phone battery: 3000mAh @ 3.7V = 11.1Wh
- **PIEZO drain:** 11.1Wh ÷ 2.16W = **5.1 hours** (drains phone battery)
- **SOL Bistable drain:** 11.1Wh ÷ 0.63W = **18 hours** (all-day use, minimal drain!)

> **TAKEAWAY:** Bistable operation = **3.4× lower power** (worst-case) → SOL_ECO achieves **15-hour battery life** vs 4.3 hours (piezo)

***Note:** Final piezo power analysis must account for leakage*(MechanicalCreep)* refresh at ~60Hz to maintain raised dot position*

<!-- Speaker notes: "This is where systems engineering meets power electronics. Key insight: We can't actuate all 192 dots simultaneously - peak current would be 96A (192 × 500mA solenoids) or 10A (192 × 50mA piezos). Sequential actuation solves TWO problems: (1) Reduces peak current to fit USB/battery budget, (2) Reduces EMI by 28dB (fewer simultaneous radiating sources). PIEZO uses 24-way parallel (8 channels of 24 dots each) because it's faster (1.5s refresh) but needs 100V HV supply. SOL uses 8-way parallel (2 channels) to stay within power budget, slower refresh (2.4s) but only 12V supply. Both have zero hold power - piezo is capacitive (no DC current), solenoid has bistable latch (mechanical brake). Power breakdown: PIEZO 2.16W mostly from boost converter (5V→100V at 85% efficiency = 1W loss), SOL 1.53W mostly from actuator pulses. USB-C provides 2.5W (500mA @ 5V), Li-ion 18650 provides 3.7W average for 2 hours. Android phone connection: PIEZO drains phone in 5 hours, SOL in 7 hours - users must manage phone battery or use wall power. Trade-off: PIEZO is faster (1.5s refresh), SOL is lower power (1.53W vs 2.16W) and cheaper (12V vs 100V drivers)." -->

---

# Common Subsystems - Shared Design Foundation

<style scoped>
table {
  font-size: 18px;
}
</style>

| Subsystem | Key Components | Function | Design Notes |
|-----------|----------------|----------|--------------|
| **SS-CONTROL** | STM32F407VGT6 (168MHz, 192KB RAM) | Main processor | 140 GPIO available, built-in USB PHY |
| **SS-IO-EXPAND** | 4× MCP23017 I2C expanders (16-bit each) | GPIO expansion | I2C bus for scalability, interrupt support |
| **SS-USER-IO** | 2× tactile switches (UP/DOWN) | User navigation | Debounce in firmware, interrupt-driven |
| **SS-PCB** | 4-layer, ENIG, 200×100mm | Main board | HV clearances, EMI routing, power planes |
| **SS-ENCLOSURE** | 3D print (pilot) → injection mold (prod) | Housing | Snap-fit assembly, optional Al shield |
| **SS-EMI-FILTER** | 24× 1000µF bulk + 24× 100nF ceramic | EMI compliance | Per-driver filtering (NFR-EMI-001) |

**Modular Design Strategy:**
- **60% of design is shared** - Control, I/O, PCB, enclosure, EMI filtering identical across all 3 architectures
- **40% varies** - Only actuators, power, and communication differ between architectures
- **Benefits:** Reduces NRE, accelerates variants, simplifies firmware reuse

> **TAKEAWAY:** Shared subsystems enable rapid architecture variants - only actuator/power/comm change.

<!-- Speaker notes: "This is modular systems engineering. 60% of the design - control, user IO, PCB, enclosure, EMI filtering - is 100% shared across all architectures. STM32F407 chosen for 140 GPIO (enough for direct-drive fallback), 168MHz performance, and built-in USB PHY. 4 MCP23017 I2C expanders give us 64 additional GPIO (total 140+64=204 available vs 192 needed). 4-layer PCB required for HV clearances even though SOL_ECO only needs 12V - we design for worst-case across all variants. EMI filtering per NFR-EMI-001: 1000µF bulk caps absorb inductive kickback, 100nF ceramic bypass for high-frequency suppression. This modularity means if we change from piezo to solenoid actuators, we only redesign 3 subsystems instead of starting from scratch - that's the value of architecture planning." -->

---

# Architecture A: ARCH_PIEZO_ECO

## Piezo Economy (Wired, Standard)

**Market Position:** Entry-level / Education / Desktop use case

**Unique Subsystems (vs common design):**

<style scoped>
table {
  font-size: 18px;
}
</style>

| Subsystem | Components | Design Choice | Cost Impact |
|-----------|------------|---------------|-------------|
| **SS-ACTUATOR** | 192× piezo bimorph (2mm, 100V) | Custom fab, 12-week lead | $384 (192 × $2.00) |
| **SS-ACTUATOR-DRIVER** | 24× HV driver ICs (100V) | Specialized HV MOSFETs | $72 (24 × $3.00) |
| **SS-COMM** | USB4105-GF-A (USB-C receptacle) | Wired only (no BLE radio) | $1.20 |
| **SS-POWER** | LDO 5V→3.3V + Boost 5V→100V | Bus-powered, no battery | $7.25 |

**Implementation Specs:**
- **BOM Cost:** $591.99 (pilot)
- **Timeline:** 6 weeks (design + prototype + pilot) + 12 weeks actuator sourcing
- **Power:** 2.5W avg (USB-C 5V @ 500mA)
- **Refresh Speed:** 1.5 sec (24-way parallel actuation)

**Design Challenges & Mitigation:**
1. **100V HV power supply** → Flyback topology, isolation, shielded magnetics
2. **EMI from piezo switching** → Sequential firing (-28dB), slew-rate limiting (-40dB), ferrite beads
3. **Custom actuator lead time** → 12-week sourcing blocks 2-month timeline requirement
4. **Dense 192-actuator packaging** → Requires ME support for multi-layer Z-axis stacking (see Path to Production)

> **TAKEAWAY:** PIEZO_ECO wins on simplicity - standard piezo approach, fastest to pilot.

***Note:** Mechanical design simplified for concept - dense packaging of 192×30mm cantilevers in 2.5mm spacing requires significant ME support*

<!-- Speaker notes: "This is the baseline architecture - standard piezo actuators like 100% of commercial displays use. Key differentiators: USB-C wired (no wireless complexity), bus-powered (no battery), piezo actuators (proven technology). BOM $592 - over target but closest to 'industry standard' approach. Major technical challenge: 100V HV power supply requires flyback topology with isolation and extreme EMI mitigation. Custom piezo actuators are 12-week lead time - violates 2-month requirement but unavoidable (NO COTS 2mm piezos exist). Design strategy: Sequential actuation (1/24th of array active at once) reduces peak current and EMI by 28dB. This is the 'safest' architecture from technical risk perspective - we're copying what commercial products already do." -->

---

# Architecture B: ARCH_SOL_ECO

## Solenoid Economy (Lever Mechanism, Innovative)

**Market Position:** Budget / Cost-conscious / Mechanical innovation

**Unique Subsystems (vs common design):**

| Subsystem | Components | Design Choice | Cost Impact |
|-----------|------------|---------------|-------------|
| **SS-ACTUATOR-SOLENOID** | 192× bistable solenoid (6-7mm, 12V) | Custom fab, 12-week lead | $326 (192 × $1.70) |
| **SS-ACTUATOR-CAM** | 96× cam discs (3 per character) | Lever mechanism (6mm→2.5mm) | $14.40 |
| **SS-ACTUATOR-PISTON** | 192× piston rods | Vertical actuation | $19.20 |
| **SS-ACTUATOR-DRIVER** | 3× ULN2803A (12V, 2-channel) | Standard low-voltage logic | $2.40 |
| **SS-COMM** | USB4105-GF-A (USB-C receptacle) | Wired only | $1.20 |
| **SS-POWER** | LDO + Boost 5V→12V (solenoid) | Bus-powered, lower voltage | $4.50 |

**Implementation Specs:**
- **BOM Cost:** $505.71 (pilot) - **LOWEST COST**
- **Timeline:** 10 weeks (cam mechanism prototyping + pilot)
- **Power:** 1.53W avg (solenoid + cam, 2-channel)
- **Refresh Speed:** 2.4 sec (8-way parallel, acceptable for beginners)

**Design Challenges & Mitigation:**
1. **Cam mechanism complexity** → Modular 6-dot subassemblies, SLA prototype validation
2. **Mechanical tolerances** → ±0.2mm acceptable with injection molding
3. **Custom solenoid lead time** → 12-week sourcing (same as piezo)
4. **Dense 192-actuator packaging** → Requires ME support for multi-layer cam/solenoid stacking (see Path to Production)

> **TAKEAWAY:** SOL_ECO wins cost via mechanical innovation - 15% actuator savings ($1.70 vs $2.00).

***Note:** Mechanical design simplified for concept - dense packaging of 192 actuators in 2.5mm spacing requires significant ME support*

<!-- Speaker notes: "This is the innovator's architecture - mechanical levers solve electrical constraints. Key insight: 6-7mm custom solenoids cost $1.70 (15% cheaper than $2.00 piezo), but don't fit 2.5mm braille spacing. Solution: Cam mechanism provides 2.4:1 leverage ratio (6mm solenoid stroke → 2.5mm effective pitch). BOM $506 - LOWEST COST of all 3 architectures. Trade-off: Mechanical complexity vs electrical simplicity. Uses standard 12V logic (ULN2803A drivers work fine), no 100V HV challenge. Design risk: Cam mechanism requires prototyping and tolerance validation - but automotive/robotics proven technology (not novel). Modular 6-dot subassemblies snap together - scalable to production. This architecture shows senior-level engineering: recognize when the solution isn't in the electrical domain." -->

---

# Architecture C: ARCH_PIEZO_DLX

## Piezo Deluxe (Wireless, Premium UX)

**Market Position:** Premium / Mobile professional / Best user experience

**Unique Subsystems (vs common design):**

| Subsystem | Components | Design Choice | Cost Impact |
|-----------|------------|---------------|-------------|
| **SS-ACTUATOR** | 192× piezo bimorph (2mm, 100V) | Same as PIEZO_ECO | $384 (192 × $2.00) |
| **SS-ACTUATOR-DRIVER** | 24× HV driver ICs (100V) | Same as PIEZO_ECO | $72 (24 × $3.00) |
| **SS-COMM-BLE** | nRF52840 BLE module (pre-certified) | Wireless freedom | $12.00 |
| **SS-POWER-LIION** | 18650 cell + charger + protection + gauge | Rechargeable, sleek design | $11.00 |
| **SS-POWER-BOOST** | Boost 3.7V→100V (battery-powered HV) | Complex flyback topology | $6.50 |

**Implementation Specs:**
- **BOM Cost:** $605.67 (pilot) - **HIGHEST COST**
- **Timeline:** 8 weeks (BLE cert faster than expected)
- **Power:** 1.0W avg (BLE efficient, Li-ion optimized)
- **Battery Life:** 10 hours (2500mAh @ 250mA avg)
- **Refresh Speed:** 1.5 sec (24-way parallel, fastest)

**Design Challenges & Mitigation:**
1. **Dual high-risk systems** → 100V HV + Li-ion battery (thermal runaway risk)
2. **FCC 15C + UL 2054 cert** → Pre-certified BLE module saves $20K + 4-6 weeks
3. **Battery anxiety (UX)** → Fuel gauge IC provides SOC %, USB-C charging

> **TAKEAWAY:** PIEZO_DLX wins UX - wireless freedom, only $13.68 premium over PIEZO_ECO.

<!-- Speaker notes: "This is the premium architecture - wireless convenience for mobile professionals. Wireless premium is only $13.68 ($606 vs $592 wired) - surprisingly affordable. BLE nRF52840 module is pre-certified FCC (saves $20K cert cost and 4-6 weeks timeline). Li-ion 18650 cell gives 10 hours runtime with fuel gauge for SOC display. Key risk: Dual high-risk systems - 100V HV power supply PLUS Li-ion battery. Requires UL 2054 cert (overcharge/discharge/thermal protection). Design strategy: Use pre-certified modules wherever possible to reduce cert burden. Battery-powered 100V generation is complex (flyback topology from 3.7V input) but justified by UX improvement. This architecture targets professionals who need mobility - educators, accessibility consultants, mobile workers." -->

---

# Design EE BOM Tracking

**Full Bill of Materials (CSV format):**

- [ARCH_PIEZO_ECO BOM](../artifacts/bom/arch-piezo-eco-bom.csv) - $591.99 total
- [ARCH_SOL_ECO BOM](../artifacts/bom/arch-sol-eco-bom.csv) - $505.71 total
- [ARCH_PIEZO_DLX BOM](../artifacts/bom/arch-piezo-dlx-bom.csv) - $605.67 total

**Important Notes:**

- **Prices shown:** Volume pricing (1K+ units)
- **$/Actuator estimates:** Based on similar components - **need supplier quotes**
- **Actuator lead time:** 12 weeks (custom fabrication, NO COTS available)
- **Cost sensitivity:** Actuators represent 55-65% of total BOM

**Next Steps:**
- Request formal quotes from 3 actuator suppliers (piezo + bistable solenoid)
- Verify volume pricing at 1K, 5K, 10K quantities
- Confirm lead time and MOQ requirements

> **TAKEAWAY:** Detailed BOMs available - actuator quotes needed for accuracy.

<!-- Speaker notes: "Click links for full line-item BOMs. All prices are volume estimates (1K+ units). Actuator costs are ESTIMATES based on similar components - we need formal supplier quotes to validate. This is honest engineering - showing our assumptions and where uncertainty exists. Actuators are 55-65% of BOM, so getting accurate quotes is critical path for cost model validation." -->

---

# Detailed Cost Breakdown

<img src="images/architecture-cost-comparison.png" alt="BOM Cost Comparison" style="max-height: 450px;">

> **TAKEAWAY:** SOL_ECO wins cost via mechanical innovation, not cheaper parts.

<!-- Speaker notes: "Stacked bar shows subsystem breakdown. SOL_ECO $506, PIEZO_ECO $592, PIEZO_DLX $606. All over $200 target - honest engineering. Key insights: Actuators dominate 55-65% of BOM ($326-$384 for 192 pins). SOL_ECO saves 15% on actuators ($1.70 vs $2.00 piezo). PIEZO_DLX wireless premium only $13.68 (BLE + battery + charger). Lever mechanism adds $0 BOM but ME complexity. Path to $200: volume pricing (10K units), reduce 32→24 cells (25% savings), value engineering (2-layer PCB)." -->

---

# EMI Compliance Trade-offs

## The GHz Antenna Challenge

**The Physics Problem:**
```
30mm Piezo Cantilever = Quarter-Wavelength Monopole Antenna
λ/4 @ 1.67 GHz → 192 radiating antennas @ GHz
```

| Parameter | Solenoid | Piezo |
|-----------|----------|-------|
| **EMI Frequency** | <10 MHz | **500 MHz - 1 GHz (HIGH)** |
| **Antenna Effect** | None | **λ/4 resonance** |
| **Mitigation Cost** | **$4.32** | **$10.84** (2.5×) |
| **Cert Risk** | LOW (10%) | HIGH (50%) |

**Key Insight:** 30mm is NOT "just a wire" at GHz — it's a resonant antenna!

<!-- This is the senior EE differentiator: GHz antenna physics -->

---

# EMI Mitigation Strategy (Piezo)

## 5-Layer Defense

| Layer | Technique | dB Reduction | Cost |
|-------|-----------|--------------|------|
| **Firmware** | Sequential firing | -28 dB | **$0** |
| | Slew-rate limiting | -40 dB | **$0** |
| **PCB** | Twisted pairs | -20 dB | $2.00 |
| | Ferrite beads (192×) | -15 dB | $3.84 |
| **Enclosure** | Shielded aluminum | -30 dB | $4.00 |

**Total:** 133 dB reduction → **21 dB compliance margin (PASS)**

**Key:** Firmware alone = **68 dB reduction at $0 cost!**

---

# Evaluate the Proposed Solutions

## Design Step 3 of 4

<img src="images/orbit-reader-20_20percent.jpg" alt="Orbit Reader 20">

<!-- Section title slide - clean delimiter between phases -->

---

# Trade-off Analysis

## Evaluation Framework

| Criterion | Weight | PIEZO_ECO | SOL_ECO | PIEZO_DLX |
|-----------|--------|-----------|---------|-----------|
| Time to Market | 25% | 9/10 | 7/10 | 6/10 |
| Unit Cost | 20% | 8/10 | 9/10 | 6/10 |
| Manufacturability | 20% | 8/10 | 7/10 | 7/10 |
| UX/Usability | 10% | 7/10 | 6/10 | 9/10 |
| Robustness | 10% | 7/10 | 8/10 | 6/10 |

**Weighted Scores:** PIEZO_ECO (8.2), SOL_ECO (7.9), PIEZO_DLX (6.8)

---

# Decision Framework

## "It Depends on YOUR Priorities"

```
IF wireless required:
  → ARCH_PIEZO_DLX (only option)

ELSE IF cost < $300:
  → ARCH_SOL_ECO (lowest BOM)

ELSE IF timeline < 8 weeks:
  → ARCH_PIEZO_ECO (fastest)

ELSE:
  → ARCH_PIEZO_ECO (most robust)
```

**Key Message:** No "best" architecture, only "best FOR YOUR CONSTRAINTS"

> **TAKEAWAY:** No "best" architecture - depends on YOUR priorities.

<!-- Tell customer: "Give me your priorities, I'll tell you which architecture wins." -->

---

# Actuator Sourcing - Critical Path Risk

## All Architectures Blocked Without Resolution

**Problem:** NO COTS actuators found meeting 2.5mm pitch + force requirements

**Three-Path Strategy:**
- **Path A (COTS search):** $5K, 2 weeks, 20% success
- **Path B (Custom quickturn):** $25K-50K NRE, 2-4 weeks, 90% success
- **Path C (Spec relaxation):** $0, 0 weeks, 100% (violates ADA 703.3)

**Timeline Impact:** +0 weeks to +8 weeks

**This is MAKE-OR-BREAK** - All 3 architectures depend on resolution

<!-- THE ELEPHANT IN THE ROOM - address head-on. $50K NRE budget allocated. -->

---

# NEXT STEPS - Initial Design to Pilot Production

## Design Step 4 of 4

<img src="images/orbit-reader-20_20percent.jpg" alt="Orbit Reader 20">

<!-- Section title slide - clean delimiter between phases -->

---

# Path to Production

## 8-12 Week Timeline

**Common Production Process:**
- **Week 0-2:** Actuator sourcing resolution **[CRITICAL PATH]**
- **Week 3-4:** Detailed design (schematic, PCB, BOM lock) + **ME support for dense actuator packaging**
- **Week 5-6:** Prototype build (fab, assembly, debug) + **Detailed EMI analysis when geometry solidifies**
- **Week 7-9:** Pilot production (10-100 units, yield validation)
- **Week 10-12:** Compliance testing & manufacturing transfer

**Architecture-Specific Deltas:**
- ARCH_PIEZO_ECO: +0 weeks (base case)
- ARCH_SOL_ECO: +2 weeks (cam tooling)
- ARCH_PIEZO_DLX: +1 week (BLE cert)

**Critical ME Support Required (All Architectures):**
- **Dense packaging challenge:** 192 actuators (30mm long) must fit in 2.5mm vertical dot spacing
- **Solution approach:** Radial/star actuator pattern within each cell + single-layer PCB assembly
- **Key insight:** 6.2mm character spacing (base) → 2.5mm dot spacing (tips) like wheel spokes
- **Layout:** Dots 1,4 vertical (top-justified), dots 3,6 vertical (bottom-justified), dots 2,5 at 45° (left/right)
- **Benefit:** All actuators on ONE PCB plane, different orientations → Eliminates Z-axis stacking complexity
- **Requirement:** ME resource with precision assembly/tolerance analysis experience

---

# Summary

**3 Viable Architectures:**
- ARCH_PIEZO_ECO: Optimizes cost + timeline
- ARCH_SOL_ECO: Optimizes volume scaling + innovation
- ARCH_PIEZO_DLX: Optimizes user experience (wireless)

**Selection Framework:**
- No universal "best" - depends on customer priorities
- Decision tree: wireless? cost threshold? timeline? volume?

**Critical Path Risk:**
- Actuator sourcing must resolve Week 0-2
- All architectures blocked without actuator solution

---

# Q&A

**Questions?**

Ready to discuss:
- Technical details (EMI physics, power budgets, BOM)
- Trade-off assumptions (cost ranges, timeline sensitivity)
- Production strategy (actuator sourcing, risk mitigation)
- Alternative approaches (other architectures considered)

<!-- Speaker notes: ANTICIPATED QUESTIONS: (1) "Why can't you find COTS actuators?" → "2.5mm pitch is non-standard, most displays use 200V custom piezos" | (2) "What if timeline extends to 4 months?" → "Opens door to custom actuator standard lead time, better cost optimization" | (3) "Which architecture would YOU pick?" → "ARCH_PIEZO_ECO most robust, but depends on wireless requirement" | (4) "Can you hit $200 BOM?" → "Not with COTS, need volume negotiation or custom actuator design" | (5) "Power supply design for 200V piezo?" → "DC-DC boost converter, see appendix slides for EMI deep-dive". Be ready to navigate to backup content if needed. Reference: docs/interview-prep-checklist.md for full Q&A prep. -->

---

# BACKUP SLIDES

## Reference Material for Q&A Deep-Dives

<img src="images/orbit-reader-20_20percent.jpg" alt="Orbit Reader 20">

<!-- Backup slides - detailed technical content for Q&A -->

---

## BACKUP-DEEP: EMI Field Strength - Fundamental Derivation to Rule of Thumb

**1. Fundamental Equation (Hertzian Dipole / Short Antenna Far-Field):**

```
E = (Z₀ × I × L × k × sin(θ)) / (4π × r)    [V/m]

Where:
Z₀ = √(μ₀/ε₀) = 377Ω    (impedance of free space)
μ₀ = 4π × 10⁻⁷ H/m      (permeability of free space)
ε₀ = 8.85 × 10⁻¹² F/m   (permittivity of free space)
k = 2πf/c = ω/c         (wave number, propagation constant)
c = 3 × 10⁸ m/s         (speed of light)
I = Peak current [A]
L = Antenna length [m]  (must be << λ for "short" antenna)
θ = Angle from antenna axis (sin(θ) = 1 for broadside, max radiation)
r = Distance [m]
4π = Total solid angle (steradians) for isotropic sphere
```

**2. Simplify for Isotropic Radiator (Conservative Worst-Case):**

Assume sin(θ) = 1 (maximum radiation, broadside direction):

```
E = (Z₀ × I × L × k) / (4π × r)
```

**3. Substitute Wave Number k = 2πf/c:**

```
E = (Z₀ × I × L × 2πf/c) / (4π × r)
E = (Z₀ × I × L × 2πf) / (4πc × r)
E = (Z₀ × I × L × f) / (2c × r)
```

**4. Plug in Constants (Z₀ = 377Ω, c = 3×10⁸ m/s):**

```
E = (377 × I × L × f) / (2 × 3×10⁸ × r)
E = (377 × I × L × f) / (6×10⁸ × r)
E ≈ (6.28×10⁻⁷ × I × L × f) / r    [V/m]
```

**5. Convert to µV/m (FCC units) and Simplify:**

Multiply by 10⁶ to get µV/m:

```
E ≈ (0.628 × I × L × f) / r    [µV/m]

For rough engineering estimates, 0.628 ≈ 0.6 or "60" when I is in mA:

E ≈ (I[mA] × L[m] × f[MHz] × 60) / r[m]    [µV/m]
```

**ASSUMPTIONS (All Conservative - Overestimate EMI):**
1. ✓ Isotropic radiator (sin(θ) = 1 everywhere) - Real antennas have nulls
2. ✓ 100% radiation efficiency - Real antennas: 1-10% efficient at these sizes
3. ✓ Far-field approximation valid (r >> λ) - True for FCC 3m test @ 30-88 MHz
4. ✓ Short antenna (L << λ) - True: 30mm << 3.4m (λ @ 88 MHz)
5. ✓ All displacement current radiates - Real: Most trapped in capacitance
6. ✓ No ground plane effects - Real: Horizontal wire over ground is LESS efficient

**RELATIONSHIP TO POWER:**
```
Power density:  S = E² / Z₀    [W/m²]
Therefore:      P ∝ E² ∝ I²

But FCC regulates E-field (µV/m), not power!
So use: E ∝ I (linear), not E ∝ I² (that's for power)
```

> **TAKEAWAY:** Rule of thumb E ≈ 60×I×L×f/r is conservative (overestimates EMI by 2-10×)

---

## BACKUP: Radiated Emissions - FCC Part 15B Compliance Challenge

<style scoped>
table {
  font-size: 15px;
}
</style>

**The Antenna Problem:** 30mm piezo cantilever = λ/4 monopole @ 1.67 GHz (192 radiating antennas!)

### Harmonic Spectrum Analysis

| Frequency Band | **FCC Part 15B Class B Limit** | **WITHOUT Slew-Rate (10µs rise)** | **WITH Slew-Rate (1ms rise)** | **Compliance** |
|----------------|--------------------------------|-----------------------------------|------------------------------|----------------|
| **30-88 MHz** | 100 µV/m @ 3m (40 dBµV/m) | **~80 dBµV/m** (40 dB OVER!) | **~20 dBµV/m** (-20 dB margin) | ✓ PASS |
| **88-216 MHz** | 150 µV/m @ 3m (43.5 dBµV/m) | **~75 dBµV/m** (31.5 dB OVER!) | **~15 dBµV/m** (-28.5 dB margin) | ✓ PASS |
| **216-960 MHz** | 200 µV/m @ 3m (46 dBµV/m) | **~70 dBµV/m** (24 dB OVER!) | **~10 dBµV/m** (-36 dB margin) | ✓ PASS |
| **Above 960 MHz** | 500 µV/m @ 3m (54 dBµV/m) | **~65 dBµV/m** (11 dB OVER!) | **~5 dBµV/m** (-49 dB margin) | ✓ PASS |

**Key Physics:**
- **Harmonic bandwidth:** f_max ≈ 0.35 / τ_rise
  - WITHOUT: 0.35 / 10µs = **35 MHz** (harmonics extend to 1 GHz+)
  - WITH: 0.35 / 1ms = **350 Hz** (virtually zero energy above 30 MHz)
- **λ/4 resonance @ 1.67 GHz:** 30mm cantilever acts as efficient radiating antenna at harmonics
- **192 coherent sources:** Without sequential firing, all antennas radiate simultaneously (+28 dB!)

**Mitigation Strategy:**
1. **Slew-rate limiting (1ms rise):** Kills harmonics above 350 Hz → **-40 dB reduction**
2. **Sequential firing (8-way parallel):** Reduces coherent radiators 192→8 → **-28 dB reduction**
3. **Total firmware EMI reduction:** -68 dB → **Passes FCC Part 15B with margin**

> **TAKEAWAY:** Piezo λ/4 antenna @ 1.67 GHz is EMI showstopper - firmware mitigation essential!

<!-- Speaker notes: EMI PHYSICS - Why 40 dB Reduction?

PIEZO Slew-Rate Limiting (Left column):
- WITHOUT: Fast 10µs rise → dV/dt = 10 million V/s → i = C × dV/dt = 500 mA peak → HIGH frequency harmonics!
- WITH: Slow 1ms rise → dV/dt = 100 thousand V/s → i = 5 mA peak → 100× current reduction

-40 dB Calculation (Radiated Power ∝ i²):
  Reduction = 10 × log₁₀(P_with / P_without)  [flipped to show reduction]
            = 10 × log₁₀((i_with)² / (i_without)²)
            = 10 × log₁₀((5mA)² / (500mA)²)
            = 10 × log₁₀((1/100)²)
            = 10 × log₁₀(1/10,000)
            = 10 × (-4)
            = -40 dB ✓

  Or equivalently (field strength):
  Reduction = 20 × log₁₀(i_with / i_without)
            = 20 × log₁₀(5mA / 500mA)
            = 20 × log₁₀(1/100)
            = 20 × (-2)
            = -40 dB ✓

SOLENOID Flyback Diode (Right column):
- WITHOUT: MOSFET turns off in 1µs → di/dt = 630,000 A/s → V = L × di/dt = 6,300V spike → DESTROYS MOSFET!
- WITH: Diode provides current path → slow 10ms ramp-down → V clamped to 5V + 0.7V diode drop = 5.7V (safe)
- This is L × di/dt in action - inductor resists current change by generating voltage

COMBINED FIRMWARE SAVINGS (Both):
- Slew-rate limiting: -40 dB (firmware-controlled gate drive)
- Sequential firing: -28 dB (1/24th simultaneous sources)
- TOTAL: -68 dB EMI reduction
- COST: $0 in hardware! (Just firmware intelligence)

This is senior-level physics - EMI isn't about peak current, it's about rate of change (dV/dt, di/dt). Slow the edges, kill the harmonics. -->
