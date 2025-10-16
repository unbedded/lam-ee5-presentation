# Braille Actuator Technology Trade-off Analysis

**Project:** Lam Research EE Concept Evaluation
**Date:** 2025-10-09
**Purpose:** Compare 5 actuator technologies for refreshable braille display

---

## Executive Summary

**Problem:** Current BOM uses piezoelectric actuators ($288 for 192 dots), driving **69% of total cost** and causing all 3 architectures to exceed budget by 90-236%.

**Analysis:** Evaluated 5 actuator technologies against requirements (size ≤2.3mm, force 50-100gf, speed <100ms, low hold power).

**Key Finding:** Only **piezo** meets ALL requirements as-is. However, **relaxing size constraint** (2.3mm → 4mm diameter) enables **miniature solenoids** with **47-67% cost savings**.

**Recommendation:**
1. **Baseline:** Piezo + negotiate volume pricing ($288 → $230, 20% savings)
2. **Alternative:** Solenoid (if size relaxed) → $96-154, 47-67% savings, but requires AC power or large battery
3. **Best Value:** Solenoid + global mechanical latch → $131, 54% savings, zero hold power ✅✅✅

---

## Table of Contents

1. [Requirements Recap](#requirements-recap)
2. [Comparison Matrix](#comparison-matrix)
3. [Technology Details](#technology-details)
   - [1. Piezoelectric Bender](#1-piezoelectric-bender-baseline)
   - [2. Miniature Solenoid](#2-miniature-solenoid-linear-pullpush)
   - [3. Shape Memory Alloy (SMA) Wire](#3-shape-memory-alloy-sma-wire)
   - [4. Voice Coil Actuator](#4-voice-coil-actuator-vca)
   - [5. Electrostatic (MEMS)](#5-electrostatic-mems-actuator)
4. [Relaxed Requirements Scenarios](#relaxed-requirements-scenarios)
5. [Recommendations](#recommendations)
6. [Next Steps](#next-steps)

---

## Requirements Recap

From `source/requirements.yaml`:

**Hard Constraints:**
- **PRD-FUNC-001**: 32 cells × 6 dots/cell = **192 dots total**
- **PRD-FUNC-003**: Actuator size ≤ 2.3mm diameter (derived from 2.5mm braille pitch - 1.5mm dot ÷ 2)
- **PRD-FUNC-002-ASMP**: Refresh speed < 1 second (user experience assumption)

**Performance Targets:**
- **Force**: 0.5-1.0 N (50-100 gf) to be tactilely detectable
- **Stroke**: 0.5-0.7mm (standard braille dot height per ADA)
- **Response time**: <100ms (for <1 second full 32-cell refresh)
- **Hold power**: Low (battery-powered architectures need efficiency)

**Relaxed Scenarios (for cost reduction):**
- Slower refresh: 1-3 seconds acceptable?
- Lower force: 0.3 N (30 gf) sufficient?
- Larger size: 3-4mm diameter if pitch increases to 3.5mm?

---

## Comparison Matrix

| Technology | Size | Force | Speed | Hold Power | Cost (192×) | Voltage | Verdict |
|------------|------|-------|-------|------------|-------------|---------|---------|
| **[Piezo](#1-piezoelectric-bender-baseline)** | 2mm ✅ | 0.5-1.5N ✅ | 10-50ms ✅ | ~0W ✅ | $288 ⚠️ | 100-200V ❌ | ⚠️ **BASELINE (EMI RISK)** |
| **[Solenoid](#2-miniature-solenoid-linear-pullpush)** | 4mm ❌ | 0.5-2.0N ✅ | 20-100ms ✅ | 9.6-19W ❌ | $96-154 ✅ | 5V ✅ | ⚠️ **If size relaxed** |
| **[Solenoid (Latching)](#2-miniature-solenoid-linear-pullpush)** | 4mm ❌ | 0.5-2.0N ✅ | 20-100ms ✅ | ~0W ✅ | $192-288 ⚠️ | 5V ✅ | ⚠️ **If size relaxed** |
| **[SMA Wire](#3-shape-memory-alloy-sma-wire)** | 0.15mm ✅ | 0.1-0.5N ❌ | 700-1500ms ❌ | 38-96W ❌ | $19-58 ✅ | 3-5V ✅ | ❌ **Too slow/weak** |
| **[Voice Coil](#4-voice-coil-actuator-vca)** | 6mm ❌ | 0.5-3.0N ✅ | 5-20ms ✅ | 9.6-29W ❌ | $384-576 ❌ | 5V ✅ | ❌ **Too expensive** |
| **[MEMS](#5-electrostatic-mems-actuator)** | 2-5mm ✅ | 0.001-0.01N ❌ | 1-10ms ✅ | ~0W ✅ | $960-3840 ❌ | 50-200V ❌ | ❌ **Insufficient stroke** |

**Legend:**
- ✅ Meets requirement
- ⚠️ Marginal or requires trade-off
- ❌ Does not meet requirement

---

## Technology Details

### 1. Piezoelectric Bender (Baseline)

**VERDICT:** ⚠️ **BASELINE (WITH EMI RISK)** - Only technology meeting size/force/speed requirements, but expensive + EMI concerns

**Technology:** Piezo ceramic bimorph bender (two piezo layers bonded together)

#### Specifications

| Parameter | Value | Status |
|-----------|-------|--------|
| Size | 2mm dia × 8mm length | ✅ Meets ≤2.3mm constraint |
| Stroke | 0.5-0.7mm | ✅ Meets requirement |
| Force | 0.5-1.5 N (50-150 gf) | ✅ EXCELLENT |
| Response time | 10-50ms | ✅ FASTEST |
| Drive voltage | 100-200V | ❌ **VERY HIGH** (needs HV boost converter + isolation) |
| Drive current | 1-20mA peak | ✅ Low (capacitive load, higher during fast switching) |
| Hold power | ~0W | ✅ Near-zero (holds position) |
| **Unit cost** | **$1.50 @ 100 qty** | ⚠️ HIGH |
| **Cost (192 dots)** | **$288 @ 100 qty** | ⚠️ 69% of BOM |
| | **$230 @ 1K qty** | ⚠️ (20% savings with volume) |

#### Pros & Cons

| Pros ✅ | Cons ❌ |
|---------|---------|
| Fastest response time (10-50ms) | **HIGH COST** (biggest driver of BOM overrun) |
| Near-zero hold power (critical for battery) | **VERY HIGH VOLTAGE** (100-200V, complex HV boost converter) |
| Small size (2mm diameter achievable) | **EXTREME EMI RISK** (192 unshielded 200V antennas, see piezo-emi-design-analysis.md) |
| High force in small package | Brittle ceramic (vibration/shock sensitivity) |
| Proven technology in existing braille displays | Limited vendor availability for custom small sizes |
| Capacitive load = low power | Higher driver cost ($3 vs $0.65 for HV ICs) |

#### PCB Impact

- **4-layer PCB MANDATORY** (200V HV isolation + GND plane for FCC)
- **100mil HV clearance** (IPC-2221 Class 2 for 200V coated board)
- **Conformal coating required** (creepage/clearance protection)
- **NO flyback diodes** (capacitive load, not inductive)
- **Sequential firing required** (8-way parallel + 1ms slew rate, see piezo-emi-design-analysis.md)
- **High-frequency emissions:** 10-50 MHz (capacitive dV/dt switching transients)
- **Pre-compliance EMI testing MANDATORY** before pilot production

#### Cost Reduction Path

1. **Negotiate volume pricing:** $1.50 @ 100 → $1.00-1.20 @ 1K+ (20-33% savings)
2. **Request custom quotes:** Optimized size/force for braille application
3. **Reduce cell count:** 32 → 24 cells = $72 savings (25%)

---

### 2. Miniature Solenoid (Linear Pull/Push)

**VERDICT:** ⚠️ **VIABLE IF SIZE RELAXED** - 47-67% cost savings, but 4mm diameter exceeds constraint

**Technology:** Electromagnetic coil with spring return

#### Specifications

| Parameter | Value | Status |
|-----------|-------|--------|
| Size | 4mm dia × 10mm length | ❌ **EXCEEDS 2.3mm constraint** |
| Stroke | 1-2mm (adjustable with stop) | ✅ Exceeds requirement |
| Force | 0.5-2.0 N (50-200 gf) | ✅ EXCELLENT |
| Response time | 20-100ms | ✅ GOOD (depends on drive) |
| Drive voltage | 5V | ✅ Low voltage |
| Drive current | 50-200mA peak | ⚠️ High current |
| Hold power (standard) | 50-100mW per solenoid | ❌ **9.6-19W for 192 dots** |
| Hold power (latching) | ~0W | ✅ Zero (pulse to switch) |
| **Unit cost (standard)** | **$0.50-0.80 @ 100 qty** | ✅ 67% cheaper |
| **Unit cost (latching)** | **$1.00-1.50 @ 100 qty** | ⚠️ Similar to piezo |
| **Cost (192 dots, standard)** | **$96-154 @ 100 qty** | ✅ **$134-192 savings** |
| **Cost (192 dots, latching)** | **$192-288 @ 100 qty** | ⚠️ Similar to piezo |

#### Pros & Cons

| Pros ✅ | Cons ❌ |
|---------|---------|
| **MUCH LOWER COST** ($0.50 vs $1.50 = 67% savings) | **SIZE: 4mm diameter exceeds 2.3mm constraint** (need 3.5mm pitch) |
| Low voltage (5V, no boost converter needed) | Higher hold power: 50-100mW × 192 = 9.6-19.2W (battery killer) |
| Robust (mechanically simple, long life) | Slower response time (20-100ms) vs piezo (10-50ms) |
| High force available | Audible clicking noise (coil impact) |
| Readily available from many vendors | Higher EMI (magnetic field switching) |

#### PCB Impact

- **2-layer PCB possible** (low voltage)
- Higher current traces (30mil for 200mA)
- Flyback diodes on every coil
- Moderate EMI (magnetic coupling)

#### Latching Solenoid Option

**Latching solenoid:** Uses pulse to latch ON/OFF, zero hold power
- **Cost:** $1.00-1.50 (similar to piezo at low volume, negates cost advantage)
- **Still has size constraint issue** (4mm diameter)
- **Verdict:** Need to verify availability at ≤4mm diameter

#### Requirements Changes Required

To use standard solenoids:
- **PRD-FUNC-003:** Relax actuator size to ≤4mm diameter
- **PRD-SIZE-001-ASMP:** Device length 200mm → 280mm (40% longer)
- **Add PRD-POWER-001-ASMP:** AC-powered only (or large battery pack)

#### Trade-offs

- **Larger device:** 280mm vs 200mm (still portable, but bulkier)
- **Higher hold power:** 9.6-19W → need AC or large battery (AA lasts <1 hour)
- **Audible clicking:** May be disruptive in quiet environments

**Verdict for ARCH-B (Wired):** ✅ **Consider if cost is critical** (save $134-192)
**Verdict for ARCH-C/A (Battery):** ❌ **Not viable** without latching (hold power kills battery)

---

### 3. Shape Memory Alloy (SMA) Wire

**VERDICT:** ❌ **NOT VIABLE** - Too slow (0.7-1.5 sec per dot = 22-48 sec refresh), too weak (10-50 gf), massive hold power (38-96W)

**Technology:** Nitinol wire contracts when heated (Joule heating)

#### Specifications

| Parameter | Value | Status |
|-----------|-------|--------|
| Size | 0.15mm wire dia × 10mm length | ✅ **TINY** |
| Stroke | 3-5% contraction (0.3-0.5mm) | ⚠️ **MARGINAL** |
| Force | 0.1-0.5 N (10-50 gf) with 0.15mm wire | ❌ **LOW** |
| Heating time | 200-500ms | ❌ **SLOW** |
| Cooling time | 500-1000ms (passive) | ❌ **VERY SLOW** |
| Total response | 700-1500ms | ❌ **0.7-1.5 sec per dot** |
| Drive voltage | 3-5V | ✅ Low voltage |
| Drive current | 200-500mA peak | ⚠️ High power for heating |
| Hold power | 200-500mW per wire | ❌ **CONTINUOUS** (38-96W for 192) |
| **Unit cost** | **$0.10-0.30 @ 100 qty** | ✅ **EXTREMELY CHEAP** |
| **Cost (192 dots)** | **$19-58 @ 100 qty** | ✅ **$230-269 savings (93%)** |

#### Pros & Cons

| Pros ✅ | Cons ❌ |
|---------|---------|
| **EXTREMELY LOW COST** ($0.10 vs $1.50 = 93% savings) | **VERY SLOW** (700-1500ms per dot → 22-48 sec for 32 cells) |
| **SMALLEST SIZE** (0.15mm wire, no size constraint) | **LOW FORCE** (10-50 gf marginal for tactile feedback) |
| Silent operation (no clicking) | **HIGH HOLD POWER** (38-96W if all dots ON, unsustainable for battery) |
| Simple mechanical design (wire + bias spring) | Thermal management (wire gets hot, 80-120°C) |
| Low voltage (3-5V) | Limited cycle life (10K-100K cycles, fatigue failure) |
| | Non-linear response (temperature-dependent) |

#### PCB Impact

- **2-layer PCB possible**
- High current traces (30-40mil for 500mA)
- Individual PWM control per wire (thermal regulation)
- Low EMI (DC heating)

#### Full Refresh Time Calculation

**Sequential activation (worst case):**
- 192 dots × 700-1500ms per dot = **134-288 seconds (2.2-4.8 minutes)** ❌

**Parallel activation (8 channels):**
- 24 dots/channel × 700-1500ms = **16.8-36 seconds** ❌

**vs requirement:** <1 second ❌

**Verdict:** **Not viable for baseline design** due to speed/power, but could be ultra-low-cost option if:
- User accepts 20-40 second refresh time
- Plugged into AC power (not battery)
- Force requirements relaxed to 30 gf

---

### 4. Voice Coil Actuator (VCA)

**VERDICT:** ❌ **NOT COST-EFFECTIVE** - Highest cost ($384-576), too large (6mm), high hold power (9.6-29W)

**Technology:** Moving coil in permanent magnet (like speaker)

#### Specifications

| Parameter | Value | Status |
|-----------|-------|--------|
| Size | 6mm dia × 8mm length | ❌ **EXCEEDS 2.3mm constraint** |
| Stroke | 0.5-2mm (adjustable) | ✅ Meets requirement |
| Force | 0.5-3.0 N (50-300 gf) | ✅ **EXCELLENT, proportional** |
| Response time | 5-20ms | ✅ **FASTEST** |
| Drive voltage | 5V | ✅ Low voltage |
| Drive current | 100-300mA peak | ⚠️ High current |
| Hold power | 50-150mW per actuator | ❌ **CONTINUOUS** (9.6-28.8W for 192) |
| **Unit cost** | **$2.00-3.00 @ 100 qty** | ❌ **HIGHEST COST** |
| **Cost (192 dots)** | **$384-576 @ 100 qty** | ❌ **$96-288 MORE than piezo** |

#### Pros & Cons

| Pros ✅ | Cons ❌ |
|---------|---------|
| **FASTEST** response (5-20ms, better than piezo) | **HIGHEST COST** ($2-3 vs $1.50 piezo) |
| **PROPORTIONAL CONTROL** (analog force, variable dot height) | **SIZE: 6mm diameter exceeds 2.3mm constraint** (need 4mm pitch) |
| Smooth motion (no clicking) | **HIGH HOLD POWER** (9.6-28.8W, battery killer) |
| Long cycle life (>10M cycles) | Requires closed-loop position feedback (hall sensor or encoder) |
| Low voltage (5V) | Heavier moving mass (coil + shaft) |

#### PCB Impact

- **4-layer PCB** (analog feedback circuits, shielding)
- Position sensor per actuator (adds cost + complexity)
- High current traces (30mil)
- Moderate EMI (magnetic coupling)

**Verdict:** **Premium option** for high-performance applications (e.g., graphics braille display with grayscale), but **not cost-effective** for text-only display.

---

### 5. Electrostatic (MEMS) Actuator

**VERDICT:** ❌ **NOT VIABLE** - Stroke too small (10-100µm << 500µm needed), force too weak (0.1-1 gf << 50 gf needed)

**Technology:** Micro-electromechanical comb drive or parallel plate

#### Specifications

| Parameter | Value | Status |
|-----------|-------|--------|
| Size | 2-5mm die size | ✅ Small |
| Stroke | 10-100µm (0.01-0.1mm) | ❌ **INSUFFICIENT** (need 0.5mm) |
| Force | 0.001-0.01 N (0.1-1 gf) | ❌ **TOO WEAK** (need 50 gf) |
| Response time | 1-10ms | ✅ Very fast |
| Drive voltage | 50-200V | ❌ Very high voltage |
| Drive current | 1-10µA | ✅ Negligible (capacitive) |
| Hold power | ~0W | ✅ Near-zero |
| **Unit cost** | **$5-20 @ 100 qty** | ❌ **VERY HIGH** (custom MEMS) |
| **Cost (192 dots)** | **$960-3840** | ❌ **$672-3552 MORE than piezo** |

#### Pros & Cons

| Pros ✅ | Cons ❌ |
|---------|---------|
| Very fast response (1-10ms) | **INSUFFICIENT STROKE** (10-100µm << 500µm required) |
| Small size (MEMS die) | **TOO WEAK** (0.1-1 gf << 50 gf required) |
| Near-zero hold power | **VERY HIGH COST** (custom MEMS fabrication) |
| Long cycle life (no mechanical wear) | Requires 50-200V power supply (even higher than piezo) |
| Silent operation | Fragile (MEMS devices sensitive to shock) |

**Verdict:** **Not viable** - stroke and force are **order of magnitude too low** for braille. Better suited for micro-mirrors (DLP projectors) or RF switches.

---

## Relaxed Requirements Scenarios

### Scenario A: Relax Speed (1 sec → 3 sec)

**Enables:** SMA wire (with sequential activation to reduce peak power)

| Trade-off | Impact |
|-----------|--------|
| Cost savings | $230-270 (78-93% reduction) ✅✅✅ |
| Power | Still 38-96W peak (need AC power or large battery) ❌ |
| UX | 3-second refresh is sluggish, frustrating for reading ❌ |
| Refresh time | 22-48 seconds full refresh (vs <1 sec requirement) ❌ |

**Verdict:** ❌ **Not recommended** - speed matters for user experience, savings don't justify UX penalty

---

### Scenario B: Relax Size (2.3mm → 3.5-4mm)

**Enables:** Solenoid or latching solenoid

| Trade-off | Impact |
|-----------|--------|
| Cost savings (standard) | $134-192 (47-67% reduction) ✅✅ |
| Cost savings (latching) | $0-96 (0-33% reduction) ⚠️ |
| Size | Device grows 200mm → 280mm length ⚠️ |
| Pitch | 2.5mm → 3.5mm (within ADA acceptable range) ✅ |
| UX | Larger braille pitch still readable ✅ |
| Hold power (standard) | 9.6-19W (need AC or large battery) ❌ |
| Hold power (latching) | ~0W ✅ |

**Verdict:** ✅ **VIABLE** - moderate cost savings, acceptable UX penalty, **best with latching solenoids**

---

### Scenario C: Relax Force (50 gf → 30 gf)

**Enables:** Smaller/cheaper piezo actuators OR thicker SMA wire

| Trade-off | Impact |
|-----------|--------|
| Cost savings | $50-100 (17-35% reduction) with smaller piezo ⚠️ |
| UX | 30 gf is marginal but detectable (user testing required) ⚠️ |
| Tactile feedback | Reduced force may be difficult to feel ❌ |

**Verdict:** ⚠️ **MARGINAL** - need user testing to validate 30 gf threshold, modest savings

---

### Scenario D: Hybrid Approach (Fast + Slow)

**Concept:** Use piezo for "hot cells" (frequently updated) + SMA for "cold cells" (static text)

**Example:** 8× piezo (center reading window) + 144× SMA (context)

| Trade-off | Impact |
|-----------|--------|
| Cost | $288 (8× $1.50 piezo) + $58 (144× $0.40 SMA) = $346 ⚠️ |
| Complexity | Dual actuator system (mechanical integration, firmware) ❌ |
| Benefit | No cost savings vs all-piezo, added complexity ❌ |

**Verdict:** ❌ **Not worth complexity** - no savings, higher risk

---

## Recommendations

### Baseline Design (Current)

**Technology:** Piezoelectric bender

| Metric | Value |
|--------|-------|
| Cost (192 dots) | $288 @ 100 qty, $230 @ 1K qty |
| Meets all requirements? | ✅ YES |
| Hold power | ~0W (battery-friendly) |
| PCB | 4-layer ($15) |

**Rationale:**
- Only technology that meets ALL requirements (size, force, speed, hold power)
- Proven in commercial braille displays
- Path to cost reduction via volume pricing

**Cost Reduction Path:**
1. Negotiate 1K+ qty pricing ($1.50 → $1.00-1.20) → $58-96 savings
2. Request vendor quotes for custom size optimization
3. Reduce cell count (32 → 24 cells) → $72 savings

---

### Alternative #1: Solenoid (Budget Option)

**Technology:** Miniature solenoid (if size constraint relaxed to 3.5mm pitch)

| Metric | Value |
|--------|-------|
| Cost (192 dots) | $96-154 @ 100 qty |
| Savings vs piezo | $134-192 (47-67% reduction) ✅✅ |
| Hold power | 9.6-19W ❌ (battery killer) |
| PCB | 2-layer ($8) |
| Device size | 280mm vs 200mm (+40%) |

**Requirements Changes:**
- PRD-FUNC-003: Relax actuator size to ≤4mm diameter
- PRD-SIZE-001-ASMP: Device length 200mm → 280mm
- Add PRD-POWER-001-ASMP: AC-powered only (or large battery pack)

**Trade-offs:**
- ✅ Significant cost savings (47-67%)
- ✅ Low voltage (5V, simpler power supply)
- ⚠️ Larger device (280mm vs 200mm)
- ❌ High hold power (need AC or large battery)
- ⚠️ Audible clicking noise

**Verdict:** ✅ **Consider for ARCH-B (Wired "Value Desk")** if cost is critical and AC-powered acceptable

---

### Alternative #2: Latching Solenoid (Low-Power Budget)

**Technology:** Latching solenoid (pulse to switch, zero hold power)

| Metric | Value |
|--------|-------|
| Cost (192 dots) | $192-288 @ 100 qty |
| Savings vs piezo | $0-96 (0-33% reduction) ⚠️ |
| Hold power | ~0W ✅ (battery-friendly) |
| PCB | 2-layer ($8) |
| Device size | 280mm vs 200mm (+40%) |

**Requirements Changes:**
- Same as Alternative #1 (size relaxation)

**Trade-offs:**
- ✅ Zero hold power (battery-friendly)
- ✅ Low voltage (5V)
- ⚠️ Similar cost to piezo at low volume
- ⚠️ Larger device (280mm)
- ⚠️ Need to verify latching solenoid availability at ≤4mm diameter

**Verdict:** ⚠️ **Investigate vendor availability** - could be best of both worlds if cost competitive

---

### Alternative #3: Solenoid + Global Mechanical Latch (Best Value)

**See separate document:** `docs/actuator-mechanical-latch-concept.md`

**Technology:** Standard solenoid + global latch plate with detents (holds all dots with zero power)

| Metric | Value |
|--------|-------|
| Cost (192 dots + latch) | $131 @ 100 qty |
| Savings vs piezo | $157 (54% reduction) ✅✅✅ |
| Hold power | ~0W ✅ (latch holds position) |
| PCB | 2-layer ($8) possible with MCU downgrade |
| Device size | 220mm vs 200mm (+10%) |
| Refresh time | 1-5 seconds (vs <1 sec requirement) ⚠️ |

**Trade-offs:**
- ✅✅✅ **MASSIVE cost savings** (54% actuators + 45% total BOM)
- ✅ Zero hold power (battery-friendly)
- ✅ Overdrive possible (6.8% duty cycle @ 5-sec refresh)
- ⚠️ Slower refresh (1-5 sec vs <1 sec)
- ⚠️ New mechanical subsystem (risk: wear, alignment)
- ⚠️ Requires validation (duty cycle, latch life)

**Verdict:** ✅✅ **RECOMMENDED FOR DETAILED EVALUATION** - highest savings, acceptable trade-offs if 5-sec refresh acceptable

---

## Next Steps

### 1. Get Vendor Quotes

| Technology | Action | Priority |
|------------|--------|----------|
| **Piezo** | Custom 2mm benders at 1K, 5K, 10K qty | HIGH |
| **Solenoid** | Miniature 4mm latching solenoids at 1K qty | MEDIUM |
| **SMA** | Nitinol wire suppliers (backup option) | LOW |

### 2. User Testing

| Test | Purpose | Priority |
|------|---------|----------|
| 30 gf force threshold | Can we relax force requirement? | MEDIUM |
| 3.5mm braille pitch | Can we relax size requirement? | HIGH |
| 3-5 second refresh | Can we relax speed requirement? | HIGH |

### 3. Architecture Variants

| Variant | Technology | Target |
|---------|------------|--------|
| **ARCH-B-ALT** | Solenoid-based (if cost priority > size) | Wired, budget-constrained |
| **ARCH-A/B/C-V2** | Volume-priced piezo (if 1K+ orders) | All architectures |
| **ARCH-D** | Solenoid + global latch | New architecture, best value |

### 4. Add to v1.4.0 Trade-off Analysis

- Cost vs UX trade-offs (size, speed, force)
- Risk assessment (single-source piezo vendor? latch mechanism reliability?)
- Path to production (volume pricing, second source, prototyping)

---

**END OF DOCUMENT**
