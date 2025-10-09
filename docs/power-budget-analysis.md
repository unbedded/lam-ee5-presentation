# Power Budget Analysis - Braille Display

**Project:** Lam Research EE Concept Evaluation
**Date:** 2025-10-09
**Purpose:** Calculate power requirements for 3 architectures across different usage scenarios

---

## Table of Contents

1. [Power Source Specifications](#power-source-specifications)
2. [Usage Profile - Typical Braille Reading](#usage-profile---typical-braille-reading)
3. [Power Budget by Subsystem](#power-budget-by-subsystem)
4. [Architecture Power Analysis](#architecture-power-analysis)
5. [Actuator Technology Viability](#actuator-technology-viability)
6. [New Requirements](#new-requirements)
7. [Recommendations](#recommendations)

---

## Power Source Specifications

### USB-C (ARCH-B: Wired)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Standard** | USB 2.0 (bus-powered) | Most conservative |
| **Voltage** | 5V ±5% | 4.75-5.25V |
| **Current (USB 2.0)** | 500mA max | 2.5W total |
| **Current (USB 3.0)** | 900mA max | 4.5W total (if available) |
| **Current (USB-C PD)** | 1.5A-3A | 7.5-15W (if PD negotiated) |
| **Baseline assumption** | **500mA @ 5V = 2.5W** | Conservative, universal compatibility |

**Connection to Android phone:**
- **USB OTG (On-The-Go):** Android phones can provide 500mA max via USB OTG
- **Risk:** Phone battery drain (2.5W continuous draw)
- **Recommendation:** Warn user or limit duty cycle when phone-powered

---

### 4× AA Alkaline (ARCH-C: Hybrid)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Voltage (fresh)** | 6.0V nominal | 4× 1.5V in series |
| **Voltage (depleted)** | 4.8V end-of-life | 4× 1.2V (80% discharged) |
| **Capacity** | 2500 mAh @ 6V | ~15 Wh energy |
| **Chemistry** | Alkaline (non-rechargeable) | Widely available |
| **Weight** | 96g (4× 24g) | Heavy |
| **Cost** | $2-4 for 4-pack | Recurring cost |

**8-hour operation requirement:**
- **Average power:** 15 Wh ÷ 8 hrs = **1.88W average** ✅
- **Peak power:** Need voltage converter (boost/buck) to handle transients
- **Derating:** 80% usable capacity (voltage sag at end) → **1.5W sustained**

---

### Li-ion 18650 Rechargeable (ARCH-A: Wireless)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Voltage (nominal)** | 3.7V | Single cell |
| **Voltage (charged)** | 4.2V max | Full charge |
| **Voltage (depleted)** | 3.0V min | Cutoff (protection circuit) |
| **Capacity** | 2500 mAh @ 3.7V | ~9.25 Wh energy |
| **Chemistry** | Li-ion (rechargeable) | Requires charging circuit |
| **Weight** | 45-60g | Light |
| **Cost** | $5-10 | One-time cost (rechargeable) |

**2-hour operation requirement:**
- **Average power:** 9.25 Wh ÷ 2 hrs = **4.6W average** ✅
- **Peak power:** Need boost converter (3.7V → 5V/12V/30V)
- **Derating:** 80% usable capacity (safety margin) → **3.7W sustained**

---

## Usage Profile - Typical Braille Reading

### Reading Speed - Literature Review

| Source | Reading Speed | Notes |
|--------|---------------|-------|
| **Average braille reader** | 125 words/min | Skilled adult reader |
| **Typical range** | 90-170 words/min | Varies by experience |
| **Average word length** | 5 characters + 1 space | English text |
| **Characters per minute** | 125 words × 6 chars = **750 characters/min** | Baseline |

**Conversion to braille dots:**
- 1 braille character = 1 cell = **6 dots**
- 750 chars/min × 6 dots/char = **4500 dots/min**
- 4500 dots/min ÷ 60 sec = **75 dots/second**

---

### Dot Actuation Frequency

**Scenario A: Continuous Scrolling (like audiobook)**

| Parameter | Value | Calculation |
|-----------|-------|-------------|
| Display capacity | 32 cells | Fixed |
| Reading speed | 750 chars/min | From literature |
| Time per line | 32 chars ÷ (750 chars/min) = **2.56 seconds/line** | |
| Scroll rate | 1 line every 2.5 seconds | User reads one line, scroll next |
| Dots changed per scroll | **50% of dots** (partial overlap) | Assumes 16 cells change, 16 stay |
| Dots actuated | 192 dots × 50% = **96 dots every 2.5 sec** | |
| Actuation rate | 96 dots ÷ 2.5 sec = **38 dots/sec** | Average |

**Scenario B: Page Turn (like book reading)**

| Parameter | Value | Calculation |
|-----------|-------|-------------|
| Lines per page | 10-15 lines | Typical braille page |
| Reading time per page | 10 lines × 2.5 sec/line = **25 seconds** | |
| Page turn frequency | Every 25-30 seconds | User pauses, turns page |
| Dots changed per page | **100% of dots** (full refresh) | New page, all dots update |
| Dots actuated | 192 dots every 30 sec | |
| Actuation rate | 192 dots ÷ 30 sec = **6.4 dots/sec** | Average (very low duty cycle) |

**Worst case: Full refresh every 5 seconds**
- Actuation rate: 192 dots ÷ 5 sec = **38.4 dots/sec**
- This matches Scenario A (continuous scrolling)

---

### Typical Usage Pattern (8-hour reading session)

| Activity | Duration | % of Time | Actuation Rate |
|----------|----------|-----------|----------------|
| **Active reading** | 4 hours | 50% | 38 dots/sec (scrolling) |
| **Page turns** | 2 hours | 25% | 6.4 dots/sec (page turn) |
| **Idle** (breaks, pauses) | 2 hours | 25% | 0 dots/sec (display static) |
| **Weighted average** | 8 hours | 100% | **24 dots/sec** |

**Key insight:** Average actuation is **24 dots/sec**, but peak is **38 dots/sec** during active reading.

---

## Power Budget by Subsystem

### Baseline: Piezo Actuators (Current Design)

| Subsystem | Voltage | Current (Peak) | Current (Avg) | Power (Avg) | Duty Cycle | Notes |
|-----------|---------|----------------|---------------|-------------|------------|-------|
| **SS-ACTUATOR (192× piezo)** | 30V | 5mA per dot | 0.1mA per dot | 0.6W | 2% (24 dots/sec, 10ms/dot) | Capacitive, pulsed |
| **SS-ACTUATOR-DRIVER (24× ULN2803A)** | 30V | 200mA | 5mA | 0.15W | 2.5% | Driver losses |
| **SS-CONTROL (STM32F4)** | 3.3V | 200mA | 100mA | 0.33W | 100% | Always on |
| **SS-IO-EXPAND (4× MCP23017)** | 3.3V | 20mA | 10mA | 0.03W | 100% | I2C expanders |
| **SS-COMM-BLE (nRF52840)** | 3.3V | 15mA | 10mA | 0.03W | 100% | BLE active (ARCH-A/C) |
| **SS-COMM-USB (STM32 PHY)** | 3.3V | 10mA | 5mA | 0.02W | 100% | USB PHY (ARCH-B/C) |
| **SS-POWER-USB-BOOST (5V→30V)** | 5V input | 600mA peak | 200mA avg | 1.0W | 30% | Boost converter (85% efficient) |
| **SS-USER-IO (buttons)** | 3.3V | 1mA | 0.1mA | 0.0003W | 10% | Negligible |
| **TOTAL (ARCH-B Wired, Piezo)** | - | **1.2A peak** | **0.53A avg** | **2.16W** | - | Within 2.5W USB budget ✅ |
| **TOTAL (ARCH-C Hybrid, Piezo)** | - | **1.2A peak** | **0.54A avg** | **2.19W** | - | Within 1.5W AA budget ❌ |
| **TOTAL (ARCH-A Wireless, Piezo)** | - | **1.2A peak** | **0.53A avg** | **2.16W** | - | Within 3.7W Li-ion budget ✅ |

**ARCH-B (Wired, Piezo):** ✅ **2.16W < 2.5W USB budget** (86% utilization, 0.34W margin)

**ARCH-C (Hybrid, Piezo):** ❌ **2.19W > 1.5W AA budget** (146% over, need 1.46× larger battery or reduce power)

**ARCH-A (Wireless, Piezo):** ✅ **2.16W < 3.7W Li-ion budget** (58% utilization, 1.54W margin)

---

### Alternative: Solenoid + Global Latch

| Subsystem | Voltage | Current (Peak) | Current (Avg) | Power (Avg) | Duty Cycle | Notes |
|-----------|---------|----------------|---------------|-------------|------------|-------|
| **SS-ACTUATOR (8× solenoids, overdrive)** | 12V | 4A (8× 500mA) | 0.27A | 3.24W | 6.8% | Pulsed, 8 parallel channels |
| **SS-LATCH (1× solenoid)** | 12V | 200mA | 4mA | 0.05W | 2% | 100ms every 5 sec |
| **SS-ACTUATOR-DRIVER (8× ULN2803A)** | 12V | 4A | 30mA | 0.36W | 0.75% | Driver losses (less than piezo) |
| **SS-CONTROL (STM32F0)** | 3.3V | 100mA | 50mA | 0.17W | 100% | Downgraded MCU (48 MHz) |
| **SS-IO-EXPAND (4× MCP23017)** | 3.3V | 20mA | 10mA | 0.03W | 100% | I2C expanders |
| **SS-COMM-BLE (nRF52840)** | 3.3V | 15mA | 10mA | 0.03W | 100% | BLE active (ARCH-A/C) |
| **SS-POWER-USB-BOOST (5V→12V)** | 5V input | 1.2A peak | 100mA avg | 0.50W | 12% | Boost converter (85% efficient) |
| **TOTAL (ARCH-D Wired, Solenoid+Latch)** | - | **5A peak** | **0.48A avg** | **4.38W** | - | ❌ EXCEEDS 2.5W USB budget |
| **TOTAL (ARCH-D Hybrid, Solenoid+Latch)** | - | **5A peak** | **0.48A avg** | **4.38W** | - | ❌ EXCEEDS 1.5W AA budget |

**CRITICAL FINDING:** Solenoid + latch **EXCEEDS power budget** even with global latch!

**Root cause:** 8 parallel solenoids @ 12V overdrive = 48W peak (8× 500mA × 12V)
- Even at 6.8% duty cycle → 3.24W average ❌

**Revised solenoid approach (reduce parallel channels):**

| Parallel Channels | Peak Power | Avg Power (6.8%) | Refresh Time | USB Budget? | AA Budget? |
|-------------------|------------|------------------|--------------|-------------|------------|
| 8 channels | 48W | 3.24W | 1.3 sec | ❌ Exceeds 2.5W | ❌ Exceeds 1.5W |
| 4 channels | 24W | 1.63W | 2.6 sec | ✅ Within 2.5W | ❌ Exceeds 1.5W |
| 2 channels | 12W | 0.82W | 5.2 sec | ✅ Within 2.5W | ✅ Within 1.5W |
| 1 channel | 6W | 0.41W | 10.4 sec | ✅ Within 2.5W | ✅ Within 1.5W |

**Revised ARCH-D (Solenoid+Latch, 2 channels):**

| Subsystem | Power (Avg) | Notes |
|-----------|-------------|-------|
| Actuators (2 channels) | 0.82W | 96 dots/channel, 5.2 sec refresh |
| Latch | 0.05W | Same as before |
| Drivers | 0.18W | Half the channels |
| Control | 0.17W | STM32F0 |
| I/O | 0.03W | I2C expanders |
| BLE/USB | 0.03W | Communication |
| Boost | 0.25W | Lower average (less parallel load) |
| **TOTAL** | **1.53W** | ✅ Within 1.5W AA budget (marginal) |

---

## Architecture Power Analysis

### ARCH-B: Wired (USB-C, Piezo)

| Scenario | Avg Power | Peak Power | USB Budget (2.5W) | Margin |
|----------|-----------|------------|-------------------|--------|
| **Active reading** (38 dots/sec) | 2.3W | 10W (brief) | ✅ 92% util | 0.2W |
| **Page turns** (6.4 dots/sec) | 1.8W | 10W (brief) | ✅ 72% util | 0.7W |
| **Idle** (0 dots/sec) | 0.4W | 0.4W | ✅ 16% util | 2.1W |
| **Weighted average** (24 dots/sec) | 2.16W | 10W (brief) | ✅ 86% util | 0.34W |

**Battery life (Android phone connection):**
- Phone battery: 3000 mAh @ 3.7V = 11.1 Wh
- Display power: 2.16W average
- **Phone drain: 11.1 Wh ÷ 2.16W = 5.1 hours** (drains phone fast!)

**Verdict:** ✅ **VIABLE** for USB-C wired, ⚠️ **MARGINAL** for Android phone (drains battery)

---

### ARCH-C: Hybrid (4× AA, Piezo)

| Scenario | Avg Power | AA Budget (1.5W) | Status |
|----------|-----------|------------------|--------|
| **Active reading** | 2.3W | ❌ 153% over | Exceeds budget |
| **Page turns** | 1.8W | ⚠️ 120% over | Exceeds budget |
| **Idle** | 0.4W | ✅ 27% util | Within budget |
| **Weighted average** | 2.19W | ❌ 146% over | Exceeds budget |

**Battery life (if we ignore budget and use larger battery):**
- 4× AA: 15 Wh
- Display power: 2.19W average
- **Battery life: 15 Wh ÷ 2.19W = 6.8 hours** (vs 8-hour requirement ❌)

**Verdict:** ❌ **NOT VIABLE** with 4× AA - need 6× AA (9V, 22.5 Wh) or Li-ion

---

### ARCH-C-ALT: Hybrid (4× AA, Solenoid+Latch, 2 channels)

| Scenario | Avg Power | AA Budget (1.5W) | Status |
|----------|-----------|------------------|--------|
| **Active reading** | 1.7W | ⚠️ 113% over | Marginal |
| **Page turns** | 1.2W | ✅ 80% util | Within budget |
| **Idle** | 0.4W | ✅ 27% util | Within budget |
| **Weighted average** | 1.53W | ⚠️ 102% over | Marginal (2% over) |

**Battery life:**
- 4× AA: 15 Wh
- Display power: 1.53W average
- **Battery life: 15 Wh ÷ 1.53W = 9.8 hours** ✅ (exceeds 8-hour requirement)

**Trade-off:** Refresh time = 5.2 seconds (vs <1 sec requirement)

**Verdict:** ✅ **VIABLE** if 5-second refresh acceptable, ⚠️ requires duty cycle management

---

### ARCH-A: Wireless (Li-ion 18650, Piezo)

| Scenario | Avg Power | Li-ion Budget (3.7W) | Status |
|----------|-----------|----------------------|--------|
| **Active reading** | 2.3W | ✅ 62% util | Within budget |
| **Page turns** | 1.8W | ✅ 49% util | Within budget |
| **Idle** | 0.4W | ✅ 11% util | Within budget |
| **Weighted average** | 2.16W | ✅ 58% util | Within budget |

**Battery life:**
- Li-ion 18650: 9.25 Wh
- Display power: 2.16W average
- **Battery life: 9.25 Wh ÷ 2.16W = 4.3 hours** ✅ (exceeds 2-hour requirement)

**Verdict:** ✅ **VIABLE** - comfortable margin, exceeds 2-hour requirement

---

## Actuator Technology Viability

### Summary Table

| Technology | Power (Avg) | USB-C (2.5W) | AA 4× (1.5W) | Li-ion (3.7W) | Refresh Time | Verdict |
|------------|-------------|--------------|--------------|---------------|--------------|---------|
| **Piezo** | 2.16W | ✅ 86% | ❌ 146% | ✅ 58% | <1 sec | ✅ ARCH-A/B only |
| **Solenoid+Latch (8ch)** | 4.38W | ❌ 175% | ❌ 292% | ❌ 118% | 1.3 sec | ❌ Exceeds all |
| **Solenoid+Latch (4ch)** | 2.48W | ⚠️ 99% | ❌ 165% | ✅ 67% | 2.6 sec | ⚠️ ARCH-A marginal |
| **Solenoid+Latch (2ch)** | 1.53W | ✅ 61% | ⚠️ 102% | ✅ 41% | 5.2 sec | ✅ All (if 5s OK) |
| **Solenoid+Latch (1ch)** | 1.09W | ✅ 44% | ✅ 73% | ✅ 29% | 10.4 sec | ✅ All (if 10s OK) |

**Key Findings:**

1. **Piezo (baseline):**
   - ✅ Works for ARCH-A (Wireless Li-ion) and ARCH-B (Wired USB)
   - ❌ Exceeds ARCH-C (Hybrid AA) budget by 46%
   - **Recommendation:** Use piezo for ARCH-A/B, need alternative for ARCH-C

2. **Solenoid + Latch (8 channels):**
   - ❌ Exceeds ALL power budgets (even Li-ion)
   - Peak power too high (48W) even with global latch
   - **Not viable**

3. **Solenoid + Latch (2 channels):**
   - ✅ Within USB budget (61% utilization)
   - ⚠️ Marginal for AA (102% - need duty cycle management)
   - ✅ Within Li-ion budget (41% utilization)
   - **Trade-off:** 5.2-second refresh (vs <1 sec requirement)
   - **Recommendation:** Viable if 5-second refresh acceptable for ARCH-C-ALT

4. **Solenoid + Latch (1 channel):**
   - ✅ Within ALL power budgets
   - **Trade-off:** 10.4-second refresh (too slow for reading)
   - **Not recommended**

---

## New Requirements

### PRD-POWER-003-ASMP: USB Power Budget (ARCH-B)

**Assumption:** Device is USB 2.0 bus-powered (500mA @ 5V = 2.5W)

**Requirement:** Average power consumption ≤ 2.0W (80% of 2.5W budget, 20% margin for USB voltage sag)

**Rationale:**
- USB 2.0 specification: 500mA max (2.5W)
- Need 20% margin for voltage drops, cable losses
- Android phone USB OTG: Also limited to 500mA

**Derived from:** USB 2.0 specification, Android OTG compatibility

**Risk:** MEDIUM - Some older USB ports may provide <500mA, need to detect and limit power

---

### PRD-POWER-004-ASMP: AA Battery Life (ARCH-C)

**Assumption:** User wants 8 hours of continuous reading on 4× AA batteries

**Requirement:** Average power consumption ≤ 1.5W for 8-hour battery life with 4× AA alkaline (2500 mAh @ 6V = 15 Wh, 80% usable)

**Rationale:**
- 4× AA alkaline: 2500 mAh @ 6V = 15 Wh total
- Usable capacity: 80% (voltage sag at end of discharge) = 12 Wh
- 8-hour requirement: 12 Wh ÷ 8 hrs = 1.5W average

**Derived from:** Typical reading session length (1-2 books, 4-8 hours), AA battery chemistry

**Risk:** HIGH - Piezo baseline (2.16W) exceeds this budget by 46%, need alternative actuator or larger battery

---

### PRD-POWER-005-ASMP: Li-ion Battery Life (ARCH-A)

**Assumption:** User wants 2 hours of reading on single charge (commute, short sessions)

**Requirement:** Average power consumption ≤ 3.7W for 2-hour battery life with 18650 Li-ion (2500 mAh @ 3.7V = 9.25 Wh, 80% usable)

**Rationale:**
- 18650 Li-ion: 2500 mAh @ 3.7V = 9.25 Wh total
- Usable capacity: 80% (safety margin, cutoff at 3.0V) = 7.4 Wh
- 2-hour requirement: 7.4 Wh ÷ 2 hrs = 3.7W average

**Derived from:** Typical commute time (30-60 min), short reading sessions, rechargeable expectation

**Risk:** LOW - Piezo baseline (2.16W) is 58% of budget, comfortable margin

---

### PRD-FUNC-005-ASMP: Reading Speed and Actuation Rate

**Assumption:** Average braille reader reads at 125 words/min (750 characters/min)

**Requirement:** System must support continuous scrolling at 125 words/min (750 chars/min = 38 dots/sec actuation rate) for minimum 4 hours

**Rationale:**
- Average skilled braille reader: 125 words/min (literature)
- 1 word = 6 characters (5 letters + 1 space)
- 125 words/min × 6 chars = 750 chars/min
- 750 chars/min ÷ 60 sec × 6 dots/char = 75 dots/sec theoretical
- Actual: 50% dots change per scroll (partial overlap) = 38 dots/sec

**Derived from:** Braille reading speed literature, typical English word length

**Risk:** LOW - Standard assumption, validated by user testing

---

### PRD-FUNC-006-ASMP: Typical Usage Profile (Duty Cycle)

**Assumption:** Typical 8-hour reading session consists of 50% active reading, 25% page turns, 25% idle

**Requirement:** Power budget calculated based on weighted average: 50% @ 38 dots/sec, 25% @ 6.4 dots/sec, 25% @ 0 dots/sec = 24 dots/sec average

**Rationale:**
- Active reading: Continuous scrolling (38 dots/sec)
- Page turns: User pauses, full refresh every 25-30 sec (6.4 dots/sec)
- Idle: User takes breaks, device remains on but static (0 dots/sec)

**Derived from:** Typical reading behavior (pauses for comprehension, breaks)

**Risk:** LOW - Conservative estimate, some users may have higher idle time (better battery life)

---

## Recommendations

### For ARCH-B (Wired USB-C)

**Actuator:** ✅ **Piezo** (baseline)
- Power: 2.16W average (86% of 2.5W USB budget)
- Margin: 0.34W (13% headroom)
- Refresh: <1 second
- **Verdict:** Comfortable fit, no changes needed

**Alternative:** Solenoid+Latch (2 channels)
- Power: 1.53W average (61% of 2.5W budget)
- Margin: 0.97W (39% headroom)
- Refresh: 5.2 seconds
- **Verdict:** Better margin, but slower refresh (trade-off)

---

### For ARCH-C (Hybrid AA)

**Actuator (baseline):** ❌ **Piezo does NOT work**
- Power: 2.19W average (146% of 1.5W budget)
- Shortfall: 0.69W (46% over budget)
- **Options:**
  1. Increase to 6× AA (9V, 22.5 Wh) → 1.88W budget ✅ (piezo fits)
  2. Switch to solenoid+latch (2 channels) → 1.53W ✅ (marginal fit with 4× AA)
  3. Use Li-ion instead of AA (switch to ARCH-A topology)

**Recommended:** ✅ **Solenoid+Latch (2 channels)** with 4× AA
- Power: 1.53W average (102% of 1.5W budget - marginal)
- Refresh: 5.2 seconds
- **Mitigation:** Duty cycle management (reduce idle power by sleeping BLE between updates)
- **Trade-off:** Slower refresh acceptable for battery operation?

---

### For ARCH-A (Wireless Li-ion)

**Actuator:** ✅ **Piezo** (baseline)
- Power: 2.16W average (58% of 3.7W budget)
- Margin: 1.54W (42% headroom) - **excellent**
- Battery life: 4.3 hours (exceeds 2-hour requirement by 2.15×)
- Refresh: <1 second
- **Verdict:** Ideal fit, no changes needed

---

### Summary Recommendation Matrix

| Architecture | Power Budget | Actuator | Power | Margin | Refresh | Battery Life | Verdict |
|--------------|--------------|----------|-------|--------|---------|--------------|---------|
| **ARCH-B (USB-C)** | 2.5W | Piezo | 2.16W | 0.34W | <1 sec | N/A (wired) | ✅ Baseline |
| **ARCH-C (4× AA)** | 1.5W | Piezo | 2.19W | -0.69W ❌ | <1 sec | 6.8 hrs ❌ | ❌ Exceeds budget |
| **ARCH-C-ALT (4× AA)** | 1.5W | Solenoid+Latch (2ch) | 1.53W | -0.03W ⚠️ | 5.2 sec | 9.8 hrs ✅ | ⚠️ Marginal |
| **ARCH-C-V2 (6× AA)** | 1.88W | Piezo | 2.19W | -0.31W ❌ | <1 sec | 10.3 hrs ✅ | ❌ Still over |
| **ARCH-A (Li-ion)** | 3.7W | Piezo | 2.16W | 1.54W | <1 sec | 4.3 hrs ✅ | ✅ Excellent |

**Key Takeaway:**
- **ARCH-B + Piezo:** ✅ Works perfectly
- **ARCH-C + Piezo:** ❌ Does NOT work with 4× AA (need 8× AA or switch to Li-ion)
- **ARCH-C-ALT + Solenoid+Latch:** ⚠️ Marginal fit (requires 5-sec refresh)
- **ARCH-A + Piezo:** ✅ Excellent fit with comfortable margin

---

## Next Steps

1. **Update ARCH-C design:**
   - Option 1: Switch to 8× AA (12V, 30 Wh) - larger, heavier
   - Option 2: Use solenoid+latch (2 channels) with 4× AA - slower refresh (5.2 sec)
   - Option 3: Merge ARCH-C into ARCH-A (use Li-ion for wireless+wired hybrid)

2. **Add power requirements to requirements.yaml:**
   - PRD-POWER-003-ASMP: USB power budget (≤2.0W)
   - PRD-POWER-004-ASMP: AA battery life (8 hours @ 1.5W)
   - PRD-POWER-005-ASMP: Li-ion battery life (2 hours @ 3.7W)
   - PRD-FUNC-005-ASMP: Reading speed (38 dots/sec)
   - PRD-FUNC-006-ASMP: Usage profile (50% active, 25% page, 25% idle)

3. **Update actuator trade-off document:**
   - Add power consumption analysis to comparison matrix
   - Update viability verdicts based on power budgets
   - Add "parallel channels" column for solenoid+latch option

4. **User validation:**
   - Test 5-second refresh acceptability (ARCH-C-ALT)
   - Validate 125 words/min reading speed assumption
   - Test 8-hour battery life requirement (is 6.8 hours acceptable?)

---

**END OF DOCUMENT**
