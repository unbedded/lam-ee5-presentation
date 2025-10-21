# Whiteboard Formulas - Study Guide for LAM Interview
**Purpose:** Key physics formulas you need to be able to derive on whiteboard during interview
**Study strategy:** Practice writing these formulas AND explaining the intuition behind each one

---

## 1. Piezo Actuator (Capacitive Load)

### Basic Capacitor Physics
```
Capacitance definition:  Q = C × V
Current definition:      i = dQ/dt
Substitute:              i = d(CV)/dt = C × (dV/dt)  [if C is constant]

KEY FORMULA: i = C × (dV/dt)
```

**Whiteboard script:**
> "Piezo is a capacitive load. Current equals capacitance times rate of voltage change. If we have 50 nanofarads and ramp 100V in 1 millisecond, that's..."
```
i = C × (dV/dt)
i = 50 nF × (100V / 1ms)
i = 50 nF × 100,000 V/s
i = 5 microamps
```

### Energy Storage in Capacitor
```
Energy = ½ C V²

For piezo @ 100V, 50nF:
E = ½ × 50 nF × (100V)²
E = ½ × 50 × 10⁻⁹ × 10,000
E = 250 microjoules per charge cycle
```

**Key insight to explain:**
> "Notice the energy is PROPORTIONAL to voltage squared. That's why high voltage is expensive energy-wise. But since it's capacitive, once charged, it holds voltage with ZERO DC current - that's the win."

---

## 2. Solenoid Actuator (Inductive Load)

### Inductor Voltage Equation (Faraday's Law)
```
V = L × (di/dt)

This is Faraday's law - changing current through inductor induces voltage
```

**Whiteboard script:**
> "Solenoid is inductive. Voltage across inductor equals inductance times rate of current change. When we turn OFF the coil..."
```
WITHOUT flyback diode (catastrophic):
  di/dt = -630mA / 1µs = -630,000 A/s
  V_spike = L × |di/dt| = 10mH × 630,000 = 6,300V  ← Destroys MOSFET!

WITH flyback diode (safe):
  Diode clamps voltage to V_supply + 0.7V
  V_spike = 5V + 0.7V = 5.7V (safe)
  di/dt = V/L = 5.7V / 10mH = 570 A/s
  Decay time = 630mA / 570 A/s ≈ 1.1ms
```

### Energy in Inductor
```
Inductive energy:  E_L = ½ L i²
Resistive energy:  E_R = i² R t  (Joule heating during pulse)

For solenoid @ 630mA, 10mH, 6Ω, 50ms pulse:
E_L = ½ × 10mH × (630mA)² = 2.0 millijoules
E_R = (630mA)² × 6Ω × 50ms = 119 millijoules
E_total ≈ 121 millijoules per pulse
```

**Key insight to explain:**
> "Most energy is wasted as heat in the coil resistance (119 mJ), not stored magnetically (2 mJ). That's why solenoids are power-hungry - they're resistive heaters that happen to make a magnetic field."

---

## 3. Power Budget Analysis

### Average Power with Duty Cycle
```
P_avg = P_peak × Duty_Cycle

Duty cycle = t_on / T_period
```

**CRITICAL: Bistable vs Continuous Operation**

**PIEZO (must refresh ALL dots every cycle):**
```
Refresh all 192 dots every cycle (capacitor discharges)
Power = constant 2.16W
```

**SOLENOID BISTABLE (only actuate CHANGED dots):**
```
Typical text reading: 20% dots change per refresh
Dots actuated: 192 × 20% = 38 dots
Groups: 38 ÷ 8 parallel = 5 groups
Time: 5 × 50ms = 250ms

Energy per pulse: 121 mJ
Power: (38 dots × 121 mJ) / period

If refresh every 1 second:
P_avg = (38 × 121 mJ) / 1s = 4.6 W... WAIT, TOO HIGH!

CORRECT CALCULATION (sequential groups):
  Only 8 dots active at once (8-way parallel)
  Number of pulses: 38 dots total
  Time: 5 groups × 50ms = 250ms every 1 second
  Duty cycle: 250ms / 1000ms = 25%

  Peak power (during pulse): 8 dots × 5V × 630mA = 25.2W
  Average power: 25.2W × 25% × (38/192) = 1.24W... STILL WRONG!

LET ME FIX THIS PROPERLY:
  Average current: (8 dots × 630mA) × (50ms / 1000ms) × (38/192)
                 = 5.04A × 0.05 × 0.198
                 = 50 mA average
  Average power: 5V × 50mA = 0.25W ✓

Add control overhead (0.1W) → Total ≈ 0.33W
```

**Whiteboard script (simplified):**
> "For bistable operation, we only pulse the dots that CHANGE. Typical text has 20% change rate, that's 38 dots. Sequential firing means 5 groups at 50ms each, that's 250ms active out of every second. Average current is about 50 milliamps, so 5 volts times 50 milliamps is 0.25 watts for the actuators, add control overhead gets us to 0.33 watts total."

---

## 4. EMI Source Analysis

### Fourier Analysis (Rise Time → Frequency Content)
```
Bandwidth of trapezoidal pulse:
f_max ≈ 0.35 / τ_rise

Fast switching (10µs rise time):
  f_max = 0.35 / 10µs = 35 kHz
  BUT harmonics extend to ~10× → 350 kHz and beyond
  At 1 GHz: Attenuation = -20 × log₁₀(f/f_max)
           = -20 × log₁₀(1 GHz / 35 kHz)
           = -20 × log₁₀(28,571)
           = -20 × 4.46 = -89 dB

Slow switching (1ms slew-rate):
  f_max = 0.35 / 1ms = 350 Hz
  At 1 GHz: Attenuation = -20 × log₁₀(1 GHz / 350 Hz)
           = -20 × log₁₀(2,857,143)
           = -20 × 6.46 = -129 dB

EMI reduction: -129 dB - (-89 dB) = -40 dB improvement
```

**Whiteboard script:**
> "EMI comes from fast edges. If I slow the rise time from 10 microseconds to 1 millisecond - that's 100× slower - the high-frequency content drops by 40 dB. That's the fundamental reason slew-rate limiting works."

### Sequential Firing EMI Reduction
```
Incoherent radiators: E_total ∝ √N

Reduction in field strength:
  E_after / E_before = √(N_after / N_before)

In dB:
  Reduction = 20 × log₁₀(N_before / N_after)

Example: 192 dots → 8 dots (24× reduction)
  Reduction = 20 × log₁₀(192 / 8)
            = 20 × log₁₀(24)
            = 20 × 1.38
            = 27.6 dB ≈ 28 dB
```

**Whiteboard script:**
> "If I have 192 dots radiating simultaneously, the field strength goes as square root of N. By sequencing to only 8 dots at once, I get 28 dB reduction. Combined with 40 dB from slew-rate limiting, that's 68 dB total - and it costs ZERO in hardware."

### Square Law Physics (CRITICAL INSIGHT!)

**Why doubling voltage/speed → QUADRUPLES power dissipation**

```
FUNDAMENTAL: Any time you have quadratic losses (I²R, drag ∝ v², radiated power ∝ i²),
             doubling the driving parameter QUADRUPLES the power!
```

**EMI Radiated Power Example:**
```
Antenna radiated power ∝ i²

Piezo @ 100V:
  i = C × (dV/dt) = 50nF × (100V/1ms) = 5µA
  Radiated power ∝ (5µA)²

Piezo @ 200V (same rise time):
  i = 50nF × (200V/1ms) = 10µA  (current DOUBLES)
  Radiated power ∝ (10µA)² = (2 × 5µA)² = 4 × (5µA)²  (power QUADRUPLES!)

EMI increase: 10 × log₁₀(4) = +6 dB

This is why piezo displays are stuck at 100V - going to 200V quadruples EMI!
```

**Motor Kinetic Energy Analogy (same physics!):**
```
Move motor from point A to B in HALF the time:

Distance d = constant
Time: t → t/2
Velocity: v → 2v  (to cover same distance in half time)

For viscous drag (F_drag ∝ v):
  Drag force: F → 2F  (doubles with velocity)
  Power = F × v → (2F) × (2v) = 4 × (F×v)  (QUADRUPLES!)

This is P ∝ v² - same square law as EMI!
```

**Resistive Heating Example (I²R losses):**
```
Copper trace resistance: R = constant

Current doubles: I → 2I
Power dissipation: P = I²R → (2I)² × R = 4I²R  (QUADRUPLES!)

That's why high-current systems (solenoid @ 630mA) need thick traces -
power loss scales with SQUARE of current, not linearly!
```

**Whiteboard script:**
> "This is fundamental physics that shows up everywhere. EMI radiated power goes as current squared. If I double voltage - keeping same rise time - current doubles, so EMI power quadruples. That's a 6 dB increase. Same thing happens with motors - if you want to move twice as fast against viscous drag, force doubles AND velocity doubles, so power quadruples. Or resistive heating - double the current, you get four times the I-squared-R losses. This square law is why you can't just scale voltage arbitrarily - the losses grow much faster than the benefits."

**This is a senior-level insight** - recognizing that similar physics (square laws) govern seemingly different domains (EMI, motors, resistive losses)!

---

## 5. Force Requirements (Braille ADA Standards)

### ADA 703.3 Tactile Requirements
```
Braille dot specifications:
  Spacing: 2.5mm center-to-center (within cell)
  Height:  0.6-0.9mm above surface
  Force:   "Detectable by touch" (not quantified in ADA)

From tactile perception research:
  Minimum detectable: 0.05N (5 gf)
  Comfortable reading: 0.2-0.5N (20-50 gf)
  Maximum before pain: 1.0N (100 gf)

Design target: 0.5N (mid-range comfortable)
```

**Whiteboard script:**
> "ADA says braille dots must be detectable, but doesn't specify force. From HCI research, comfortable tactile reading is 0.2 to 0.5 newtons. I targeted 0.5 newtons - that's about 50 grams-force, similar to a light button press."

### Solenoid Force Equation (Simplified)
```
Electromagnetic force (simplified, DC):
F ∝ (N × I)² × A / g²

where:
  N = number of coil turns
  I = current
  A = plunger cross-sectional area
  g = air gap

Key insights:
  - Force ∝ (ampere-turns)²  (double current = 4× force)
  - Force ∝ area            (double diameter = 4× area = 4× force)
  - Force ∝ 1/gap²          (double gap = ¼ force - very sensitive!)
```

**Whiteboard script:**
> "Solenoid force scales with ampere-turns squared and inversely with gap squared. That gap-squared term is why we need a mechanical stop - if the plunger extends too far, force drops rapidly."

---

## 6. Thermal Analysis (Pulse vs Continuous)

### Thermal Time Constant
```
Heating equation:
  Temperature rise: ΔT = P × R_thermal

  R_thermal ≈ 50°C/W for small air-cooled solenoid

Continuous operation @ 2.1W:
  ΔT = 2.1W × 50°C/W = 105°C rise ← EXCEEDS 125°C LIMIT!

Pulsed operation (2.1% duty cycle):
  P_avg = 2.1W × 0.021 = 44 mW
  ΔT = 44 mW × 50°C/W = 2.2°C rise ✓ SAFE
```

**Whiteboard script:**
> "If we ran the solenoid continuously at 2 watts, it would overheat - 105 degree rise. But with 2% duty cycle from sequential firing, average power is only 44 milliwatts, that's 2 degrees rise. The thermal mass averages out the pulses."

---

## 7. Battery Life Calculation

### Energy Capacity
```
Battery energy: E = V × A·h × 3600 (convert amp-hours to watt-hours)

Li-ion 18650: 2500 mAh @ 3.7V
  E = 3.7V × 2.5 A·h = 9.25 Wh

Battery life:
  Life = E / P_avg

PIEZO @ 2.16W:
  Life = 9.25 Wh / 2.16W = 4.3 hours

SOLENOID Bistable @ 0.33W:
  Life = 9.25 Wh / 0.33W = 28 hours
```

**Whiteboard script:**
> "Li-ion 18650 cell is 2500 milliamp-hours at 3.7 volts, that's 9.25 watt-hours. Divide by average power: 9.25 divided by 2.16 is 4.3 hours for piezo, 9.25 divided by 0.33 is 28 hours for bistable solenoid. That 7× power difference translates directly to battery life."

---

## 8. Cost-Down Opportunity (Custom Solenoid)

### Plunger Diameter Sizing
```
Minimum diameter to prevent buckling (Euler buckling):
  F_critical = (π² × E × I) / L²

  where:
    E = Young's modulus (steel = 200 GPa)
    I = (π × d⁴) / 64  (second moment of area)
    L = unsupported length

  Solve for d given F = 0.75N:
    d⁴ = (F × 64 × L²) / (π³ × E)
    d⁴ = (0.75 × 64 × (5mm)²) / (π³ × 200 GPa)
    d ≈ 0.37 mm

  Safety factor 5×: d_min = 1.85mm
  Design choice: d = 2mm ✓
```

**Whiteboard script:**
> "Buckling calculation shows I need at least 0.37 millimeters diameter. With 5× safety factor, 1.85 millimeters. I chose 2 millimeters for the custom design - that's half the area of the 4mm COTS part, saves size and cost."

### Ampere-Turns Calculation
```
Empirical solenoid force equation:
  F ≈ k × (N × I)² / g

  where k ≈ 10⁻⁶ N/(A·turn)² for air-core solenoids

Solve for N×I given F = 0.75N, g = 1mm:
  (N×I)² = F × g / k
  (N×I)² = 0.75 × 0.001 / 10⁻⁶
  (N×I)² = 750
  N×I ≈ 27.4 ampere-turns

Design choice: 60 turns × 0.46A = 27.6 A·turns ✓
```

**Whiteboard script:**
> "I need 27 ampere-turns to get 0.75 newtons force. I could do 100 turns at low current, or fewer turns at high current. I chose 60 turns at 460 milliamps because that gives me 10 ohms resistance, which matches the 5-volt system supply perfectly."

---

## 9. Quick Reference Card (FOR WHITEBOARD)

**PIEZO:**
```
i = C × (dV/dt) = 50nF × (100V/1ms) = 5µA
E = ½CV² = ½ × 50nF × (100V)² = 250µJ
P = 2.16W (must refresh all dots)
Battery: 4.3 hours
```

**SOLENOID:**
```
V = L × (di/dt) [back-EMF without flyback]
E = ½Li² + i²Rt = 2mJ + 119mJ = 121mJ per pulse
P = 0.33W (bistable, sparse updates)
Battery: 28 hours
Force: F ∝ (NI)² × A / g²
```

**EMI:**
```
f_max = 0.35 / τ_rise
Slew-rate: 1ms → -40 dB vs 10µs
Sequential: 192→8 dots → -28 dB
TOTAL: -68 dB (firmware only!)
```

**THERMAL:**
```
ΔT = P_avg × R_thermal
Continuous: 2.1W × 50°C/W = 105°C ❌
Pulsed (2%): 44mW × 50°C/W = 2.2°C ✓
```

---

## 10. Common Whiteboard Questions (Practice These!)

### Q1: "Walk me through why slew-rate limiting helps EMI"
**Answer structure:**
1. Draw voltage step (10µs vs 1ms)
2. Write f_max = 0.35 / τ_rise
3. Calculate both: 35 kHz vs 350 Hz
4. Show harmonic rolloff: -20 dB/decade
5. Calculate at 1 GHz: -89 dB vs -129 dB
6. Difference = -40 dB reduction ✓

### Q2: "Why does bistable save power?"
**Answer structure:**
1. Draw braille display with text "THE CAT"
2. Next refresh: "THE BAT" (only 1 letter changes = 6 dots)
3. 6 dots / 192 total = 3% update rate
4. Piezo: Must refresh ALL → 192 × 250µJ = full power
5. Solenoid bistable: Only 6 dots × 121mJ = minimal power
6. Magnet holds mechanically → 0W between changes ✓

### Q3: "How did you size the actuator force?"
**Answer structure:**
1. ADA 703.3: "Detectable by touch" (vague!)
2. Research: 0.05N min, 0.5N comfortable, 1.0N max
3. Target 0.5N (mid-range)
4. Add margin for cam friction, losses → 0.75N solenoid
5. Cam leverage 2.4:1 → 0.75N / 2.4 = 0.31N at pin (below target, conservative) ✓

### Q4: "Show me the piezo charging current calculation"
**Answer structure:**
1. Write Q = CV
2. Take derivative: dQ/dt = C × (dV/dt)
3. But dQ/dt = i (definition of current)
4. So i = C × (dV/dt)
5. Plug in: i = 50nF × (100V / 1ms) = 50nF × 100,000 V/s = 5µA ✓
6. Compare without slew-rate: 50nF × (100V / 10µs) = 500mA (100,000× higher!)

### Q5: "Why do you need a flyback diode on the solenoid?"
**Answer structure:**
1. Write V = L × (di/dt)
2. Turn-off transient: i drops from 630mA to 0 in ~1µs (MOSFET switches fast)
3. di/dt = -630mA / 1µs = -630,000 A/s
4. V_spike = 10mH × 630,000 A/s = 6,300V
5. This DESTROYS the MOSFET (rated for maybe 60V)
6. Flyback diode clamps to V_supply + 0.7V = 5.7V (safe) ✓

---

## Study Tips

1. **Practice writing these on paper** (not typing!) - muscle memory matters
2. **Explain out loud** while writing - they want to see your thought process
3. **Draw diagrams** - voltage waveforms, current pulses, circuit snippets
4. **Know the UNITS** - nanofarads, microamps, millijoules, etc.
5. **Be ready to derive from first principles** - don't just memorize results
6. **Practice the "narrative"** - "The reason this matters is..." after each calculation

## Interview Red Flags to Avoid

❌ "I just used this formula" (without deriving it)
❌ "The datasheet says..." (without understanding why)
❌ "I assumed..." (without justifying the assumption)
❌ Unit errors (50nF → 50 microamps instead of 5 microamps)
❌ Off-by-1000 errors (milliamps vs amps)

✅ "Let me derive this from Faraday's law..."
✅ "The datasheet gives 630mA, let me validate that matches V/R..."
✅ "I assumed 20% update rate based on typical text, but it could be 5-50%..."
✅ Double-check units: "That's 5 MICRO-amps, not milliamps"
✅ Sanity check: "121 millijoules per pulse, 38 pulses, that's about 5 joules per refresh..."

---

**PRACTICE SCHEDULE:**

**Day 1 (Today):** Read through once, understand each section
**Day 2:** Practice writing Section 1-3 on whiteboard, explain out loud
**Day 3:** Practice Section 4-6 on whiteboard
**Day 4:** Practice Section 7-9 on whiteboard
**Day 5:** Do all 5 Q&A scenarios cold (no notes)
**Interview Day:** Quick review of Quick Reference Card (Section 9)

**CONFIDENCE CHECK:** If you can whiteboard all 5 Q&A scenarios without looking at notes, you're ready.
