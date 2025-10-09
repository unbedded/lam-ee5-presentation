# Mechanical Latch Concept - Global Detent System

**Project:** Lam Research EE Concept Evaluation
**Date:** 2025-10-09
**Concept:** User insight - mechanical brake/detent to eliminate hold power

---

## Problem Statement (Current)

**Solenoid actuators** are 47-67% cheaper than piezo ($96-154 vs $288), but have **fatal flaw**:

- **Hold power: 50-100mW per solenoid × 192 dots = 9.6-19.2W continuous**
- Battery life: 6V × 3A = 18W → AA batteries last <1 hour
- **Makes battery operation impossible**

**Current "solution":** Latching solenoid ($1.00-1.50 each, negates cost advantage)

---

## User's Insight: Global Mechanical Latch

### Concept Description

**Mechanical System:**
1. **Actuators:** Standard cheap solenoids (4mm, $0.50 each) move dots up/down
2. **Global latch plate:** Sliding plate with 192 detents (holes/notches) that locks ALL dots in position
3. **Latch actuator:** Single solenoid/motor moves plate to engage/disengage detents
4. **Overdrive mode:** Drive solenoids at 2-3× rated current (short pulse, low duty cycle)

**Operation Sequence:**
1. **Disengage latch** (plate slides away, 50ms)
2. **Update dots** (solenoids fire in sequence/parallel, 20-100ms per dot)
3. **Engage latch** (plate slides back, detents capture dot positions, 50ms)
4. **Solenoids OFF** (zero hold power, latch holds everything)

**Total refresh time:** 50ms + (192 dots × sequential) + 50ms = 0.1-20 seconds (depends on parallel channels)

---

## Duty Cycle Analysis

**User's assumption:** 5-second refresh interval

### Scenario 1: Sequential Update (1 channel)

**Timing:**
- Latch disengage: 50ms
- Update 192 dots sequentially: 192 × 50ms = 9.6 seconds
- Latch engage: 50ms
- **Total active time: 9.7 seconds**
- **Repeat interval: Every 5 seconds** (text scrolling/page turn)

**Duty cycle:** 9.7s / 5s = **194%** ⚠️ (EXCEEDS 100%, not viable)

### Scenario 2: Parallel Update (8 channels)

**Timing:**
- Latch disengage: 50ms
- Update 24 dots per channel × 8 channels in parallel: 24 × 50ms = 1.2 seconds
- Latch engage: 50ms
- **Total active time: 1.3 seconds**
- **Repeat interval: Every 5 seconds**

**Duty cycle:** 1.3s / 5s = **26%** ✅ (viable, but still high)

### Scenario 3: Overdrive + Fast Update (8 channels)

**Overdrive parameters:**
- Normal solenoid: 5V, 200mA, 50ms response time
- Overdrive: 12V, 500mA, **10ms response time** (2.4× voltage, 2.5× current)
- Thermal limit: Safe for <100ms pulses (duty cycle limited)

**Timing:**
- Latch disengage: 50ms
- Update 24 dots per channel × 8 channels: 24 × 10ms = 240ms
- Latch engage: 50ms
- **Total active time: 340ms**
- **Repeat interval: Every 5 seconds**

**Duty cycle:** 340ms / 5s = **6.8%** ✅✅ (EXCELLENT)

### Scenario 4: Relaxed Refresh (30 seconds)

**User reading speed:** Average reader reads 1-2 lines per second, full page in 20-30 seconds

**Timing:**
- Total active time: 340ms (same as Scenario 3)
- **Repeat interval: Every 30 seconds** (page turn)

**Duty cycle:** 340ms / 30s = **1.1%** ✅✅✅ (NEGLIGIBLE)

---

## Mechanical Design Considerations

### Global Latch Plate

**Design:**
```
[Side View]
Solenoid pins (up/down): | | | | | | | |
Latch plate (sliding):   [==============] ← moves left/right
                          O O O O O O O O  ← detent holes

ENGAGED: Holes align with pins, capturing position
DISENGAGED: Plate shifts 2-3mm, holes clear pins
```

**Specifications:**
- Material: Delrin/acetal plastic (low friction, self-lubricating)
- Thickness: 2-3mm
- Detent holes: 1.5mm diameter (loose fit on 1mm pin)
- Latch stroke: 2-3mm (just enough to clear pins)
- Latch actuator: Small servo motor (180° rotation = 2-3mm linear via cam) OR linear solenoid

**Pros:**
- ✅ Single latch mechanism for ALL 192 dots (cost amortized)
- ✅ Simple injection-molded part ($5-10 in production)
- ✅ Self-centering detents (mechanical alignment)
- ✅ Audible/tactile "click" when latched (user feedback)

**Cons:**
- ❌ Additional moving part (wear, friction)
- ❌ Adds ~3mm to device height (latch plate clearance)
- ❌ Alignment critical (192 holes must align with pins)
- ❌ Contamination risk (dust/debris in detents)

### Latch Actuator Options

**Option 1: Servo Motor**
- Cost: $3-5
- Stroke: 180° rotation → 2-3mm linear (via cam or rack-and-pinion)
- Speed: 50ms (fast servo)
- Power: 0.5W peak, 0.1W hold (PWM to maintain position)
- Pros: Precise position control, gentle engagement
- Cons: Hold power required (0.1W), more complex mechanical linkage

**Option 2: Linear Solenoid**
- Cost: $2-4
- Stroke: 3mm push/pull
- Speed: 20ms (fast)
- Power: 2W peak (100ms), 0W hold (spring return)
- Pros: Simple, fast, zero hold power
- Cons: Harsh engagement (impact), limited positioning accuracy

**Recommendation:** **Linear solenoid** (simplicity + zero hold power)

---

## Cost Analysis

### Bill of Materials (192 dots + latch)

| Component | Qty | Unit Cost | Total | Notes |
|-----------|-----|-----------|-------|-------|
| Solenoid actuators (4mm) | 192 | $0.50 | $96 | Standard, not latching |
| Latch plate (custom) | 1 | $10 | $10 | Injection mold, pilot qty 100 |
| Latch solenoid | 1 | $3 | $3 | Linear, 3mm stroke |
| Latch spring | 1 | $0.50 | $0.50 | Return spring |
| Driver ICs (ULN2803A) | 24 | $0.80 | $19.20 | 8-channel, 192÷8=24 |
| Power supply (12V boost) | 1 | $2.25 | $2.25 | For overdrive |
| **TOTAL (actuator subsystem)** | | | **$131** | |

**Comparison:**
- **Piezo (current):** $288
- **Solenoid + latch:** $131
- **Savings: $157 (54% reduction)** ✅✅✅

### BOM Impact (ARCH-B Wired)

| Component | Current (Piezo) | New (Solenoid+Latch) | Savings |
|-----------|-----------------|----------------------|---------|
| Actuator system | $288 | $131 | $157 |
| MCU + I/O | $13 | $13 | $0 |
| Drivers (30V) | $19 | $19 | $0 |
| Power (USB boost) | $3 | $3 | $0 |
| USB interface | $2 | $2 | $0 |
| PCB (4-layer) | $15 | **$8** (2-layer) | **$7** |
| Enclosure | $25 | $25 | $0 |
| User I/O | $0.50 | $0.50 | $0 |
| **SUBTOTAL** | $365 | **$201** | **$164** |
| Misc 15% | $55 | $30 | $25 |
| **TOTAL BOM** | **$420** | **$231** | **$189 (45%)** ✅✅✅ |

**CRITICAL:** **BOM now $231 vs $125 target** → Still $106 over, but **85% closer to target**

---

## 2-Layer PCB Viability

### Current 4-Layer Drivers (Revisited)

With solenoid + latch system:

| Subsystem | 4-Layer Reason | Can We Eliminate? |
|-----------|----------------|-------------------|
| **SS-CONTROL (MCU)** | 168 MHz clock + USB | **NO** - still need GND plane for FCC |
| **SS-ACTUATOR-DRIVER** | 30V HV isolation | **YES** - Solenoids use 12V (not 30V) |
| **SS-POWER-USB-BOOST** | 5V→30V switching | **YES** - Only need 5V→12V boost |
| **SS-COMM-USB** | 90Ω differential pairs | **NO** - USB still needs controlled impedance |

**Verdict:** **Still need 4-layer** due to STM32F4 168 MHz + USB

### Alternative: Downgrade MCU to Eliminate 4-Layer

**Option: STM32F0** (48 MHz, no USB PHY) instead of **STM32F4** (168 MHz, USB PHY)

**Changes:**
- MCU: $8 → $3 (STM32F042, 48 MHz, 32 KB Flash)
- USB: Need external USB-to-UART bridge ($1.50, e.g., CH340)
- Speed: 168 MHz → 48 MHz (still plenty for braille display)
- PCB: 4-layer → **2-layer** (48 MHz ≈ 50 MHz, manageable on 2-layer with care)

**Cost impact:**
- MCU savings: $5
- USB chip added: -$1.50
- **PCB savings: $7 (4-layer $15 → 2-layer $8)**
- **Net savings: $10.50**

**Revised BOM:** $231 - $10.50 = **$220.50** → **76% closer to $125 target** ✅✅✅

**Trade-offs:**
- ✅ 2-layer PCB (simpler, cheaper)
- ✅ Lower EMI (48 MHz vs 168 MHz)
- ⚠️ Slower processing (but 48 MHz >> 1 Hz refresh rate, not a bottleneck)
- ⚠️ Less Flash/RAM (32 KB vs 1 MB, but sufficient for braille text processing)

---

## Power Consumption Analysis

### Scenario: 8-Channel Parallel Update, Overdrive

**Components:**

| Component | Power (Peak) | Power (Avg) | Duty Cycle | Notes |
|-----------|--------------|-------------|------------|-------|
| 8× solenoids (overdrive) | 12V × 0.5A × 8 = 48W | 48W × 6.8% = 3.3W | 6.8% (5s refresh) | Pulsed |
| Latch solenoid | 12V × 0.2A = 2.4W | 2.4W × 2% = 0.05W | 2% (100ms / 5s) | Pulsed |
| MCU + logic | 0.5W | 0.5W | 100% | Continuous |
| BLE (ARCH-A/C) | 0.05W | 0.05W | 100% | Continuous |
| **TOTAL (ARCH-B Wired)** | **50.4W** | **3.85W** | - | USB-powered (5V × 0.77A avg) |
| **TOTAL (ARCH-C Hybrid)** | **50.4W** | **3.90W** | - | AA battery (4× AA = 6V × 0.65A avg) |

### Battery Life (ARCH-C Hybrid, AA)

**Battery capacity:** 4× AA alkaline = 2500 mAh @ 6V nominal = 15 Wh

**Average power:** 3.90W (with 5-second refresh, reading continuously)

**Battery life:** 15 Wh ÷ 3.90W = **3.8 hours** ✅ (vs <1 hour with non-latching solenoids)

**Idle power** (no refresh, latch holds position):
- MCU + BLE: 0.55W
- Battery life: 15 Wh ÷ 0.55W = **27 hours** ✅✅ (overnight reading session)

**Comparison:**
- **Non-latching solenoid:** <1 hour (unusable)
- **Latching solenoid:** 20-30 hours (good, but expensive)
- **Global latch + overdrive:** 3.8 hours active / 27 hours idle ✅ (acceptable for mobile use)

---

## New Assumption Requirements

### PRD-FUNC-004-ASMP: Refresh Rate for Reading

**Assumption:** User reads at 1-2 lines per second, full 32-cell line consumed in 15-30 seconds

**Requirement:** Refresh rate ≤ 5 seconds for scrolling, ≤ 30 seconds for page turn

**Rationale:**
- Reading speed: Average braille reader = 125 words/min = 2 words/sec
- 32 cells ≈ 5-6 words → 2-3 seconds to read one line
- **5-second refresh allows smooth scrolling** (refresh faster than user reads)
- **30-second refresh allows full page turn** (user pauses at page boundary)

**Risk:** LOW - User testing required to validate acceptable latency

### PRD-POWER-002-ASMP: Duty Cycle for Actuator Overdrive

**Assumption:** Solenoids can be overdriven (2.4× voltage, 2.5× current) for short pulses

**Requirement:** Actuator duty cycle ≤ 10% to allow thermal dissipation

**Rationale:**
- Standard solenoid: Rated for 100% duty cycle at 5V, 200mA
- Overdrive: 12V, 500mA → 6× power dissipation
- Thermal time constant: ~30 seconds (wire mass)
- **10% duty cycle → 5-10°C temperature rise** (safe)

**Risk:** MEDIUM - Vendor datasheet validation required, thermal testing needed

### PRD-MECH-001-ASMP: Mechanical Latch Reliability

**Assumption:** Global latch plate can survive 1 million cycles (10 years @ 5-second refresh)

**Requirement:** Latch mechanism MTBF ≥ 1M cycles

**Rationale:**
- Reading session: 1 hour/day × 365 days = 365 hours/year
- Refresh rate: 5 seconds → 720 refreshes/hour
- **10-year life: 365 hrs/yr × 720/hr × 10 yr = 2.6M cycles**
- Wear parts: Delrin-on-delrin (low friction, 10M+ cycle life)

**Risk:** MEDIUM - Prototype testing required, wear mechanisms (dust, debris)

---

## Trade-offs Summary

### Pros (Why This Could Be Game-Changing)

1. ✅ **54% cost savings** ($288 → $131 actuators)
2. ✅ **45% total BOM savings** ($420 → $231)
3. ✅ **2-layer PCB possible** (with MCU downgrade, +$10.50 savings)
4. ✅ **Battery-friendly** (3.8 hrs active, 27 hrs idle vs <1 hr without latch)
5. ✅ **Simple mechanical design** (injection-moldable latch plate)
6. ✅ **Overdrive possible** (10× shorter pulse → faster response)
7. ✅ **Single-point-of-failure mitigation** (latch breaks → all dots stuck, but visible failure mode)

### Cons (Why This Adds Complexity)

1. ❌ **New mechanical subsystem** (latch plate, actuator, spring)
2. ❌ **Alignment critical** (192 detent holes must align perfectly)
3. ❌ **Wear mechanism** (1M-10M cycles, needs testing)
4. ❌ **Contamination risk** (dust/debris in detents → stuck latch)
5. ❌ **Duty cycle assumption** (needs validation: 5-sec refresh acceptable?)
6. ❌ **Height penalty** (+3mm for latch clearance)
7. ❌ **Latency** (50ms latch engage/disengage + sequential updates)

---

## Recommendation

### For v1.4.0 Trade-off Analysis

**Add 4th architecture variant:** **ARCH-D (Solenoid + Global Latch)**

| Metric | ARCH-B (Piezo) | ARCH-D (Solenoid+Latch) | Delta |
|--------|----------------|-------------------------|-------|
| **BOM Total** | $420 | $231 | **-$189 (-45%)** ✅✅✅ |
| **Target** | $125 | $125 | - |
| **Gap** | +$295 (236%) | +$106 (85%) | **-$189** ✅ |
| **PCB Layers** | 4-layer ($15) | 2-layer ($8) w/ MCU downgrade | -$7 ✅ |
| **Size** | 200×100×15 mm | 220×110×18 mm | +10% volume ⚠️ |
| **Refresh Time** | <1 sec | 1-5 sec | +1-4 sec ⚠️ |
| **Battery Life (N/A for wired)** | - | - | - |

**For ARCH-C (Hybrid):**

| Metric | ARCH-C (Piezo) | ARCH-C-ALT (Solenoid+Latch) | Delta |
|--------|----------------|------------------------------|-------|
| **BOM Total** | $438 | $248 | **-$190 (-43%)** ✅✅✅ |
| **Target** | $220 | $220 | - |
| **Gap** | +$218 (99%) | +$28 (13%) | **-$190** ✅✅ |
| **Battery Life (active)** | N/A (piezo ~50 hrs) | 3.8 hours | ⚠️ (but sufficient for 1-2 reading sessions) |
| **Battery Life (idle)** | N/A | 27 hours | ✅ |

### Next Steps

1. **User research:** Validate 5-second refresh acceptable
2. **Vendor quotes:** Get solenoid quotes (4mm, 5V/12V overdrive-capable)
3. **Mechanical CAD:** Sketch latch plate design (Fusion 360)
4. **Thermal analysis:** Validate 10% duty cycle thermal limit
5. **Risk assessment:** FMEA for latch failure modes
6. **Prototype plan:** 3D-print latch plate, test with 8-dot array

---

## Questions for User

1. **Is 5-second refresh acceptable?** (vs <1 second with piezo)
2. **Is 220×110×18mm size acceptable?** (vs 200×100×15mm)
3. **Should we pursue ARCH-D as primary recommendation?** (biggest cost savings)
4. **Willing to do mechanical prototyping?** (latch plate design needs validation)
5. **How much risk is acceptable?** (new mechanism vs proven piezo)

---

**This could be the breakthrough we need to hit cost targets while maintaining battery operation.**
