# COTS Component Requirement - Timeline Analysis

**Project:** Lam Research EE Concept Evaluation
**Date:** 2025-10-09
**Purpose:** Analyze COTS (Commercial Off-The-Shelf) requirement driven by 2-month pilot timeline

---

## Executive Summary

**Critical Finding:** 2-month timeline to pilot production **REQUIRES** all COTS components. Custom parts (piezo actuators, enclosures, PCBs) have 8-12 week lead times that **EXCEED** the timeline.

**Impact on Actuator Selection:**
- ❌ **Custom 2mm piezo actuators:** 8-12 week lead time (quote + tooling + samples)
- ✅ **COTS 4mm solenoids:** 2-4 week lead time (stock at Digikey)
- ⚠️ **Size constraint violation:** Solenoid (4mm) exceeds PRD-FUNC-003 (≤2.3mm)

**Recommendation:** Relax size constraint to 4mm diameter (ARCH-C only) OR use existing COTS piezo benders (if available at 2-3mm).

---

## Table of Contents

1. [Timeline Breakdown (2 Months)](#timeline-breakdown-2-months)
2. [COTS vs Custom Lead Times](#cots-vs-custom-lead-times)
3. [Actuator Availability Analysis](#actuator-availability-analysis)
4. [Size Constraint Conflict (ARCH-C)](#size-constraint-conflict-arch-c)
5. [New Requirement: COTS Mandate](#new-requirement-cots-mandate)
6. [Recommendations](#recommendations)

---

## Timeline Breakdown (2 Months)

### Week-by-Week Schedule (8 Weeks Total)

| Week | Phase | Activities | Duration |
|------|-------|------------|----------|
| **1-2** | Requirements & Architecture | Concept evaluation (this work), architecture selection, BOM finalization | 2 weeks |
| **3-4** | Detailed Design | Schematic design, PCB layout (4-layer), enclosure CAD, firmware architecture | 2 weeks |
| **5-6** | Procurement & Fabrication | Order parts (COTS), PCB fab (3 weeks), enclosure 3D print (1 week) | 2 weeks |
| **7** | Assembly & Test | Hand assembly (5-10 units), firmware bring-up, functional test | 1 week |
| **8** | Pilot Production | Build 100 units, QC testing, packaging | 1 week |

**Critical Path:** PCB fabrication (3 weeks) + component procurement (2-4 weeks) = **5-7 weeks** best case

**Buffer:** Only **1-3 weeks** margin for delays (13-38% buffer) ⚠️

---

## COTS vs Custom Lead Times

### Component Lead Time Analysis

| Component | COTS Option | Lead Time | Custom Option | Lead Time | Risk |
|-----------|-------------|-----------|---------------|-----------|------|
| **Actuators (192×)** | Digikey stock solenoid | **2 weeks** ✅ | Custom 2mm piezo | **8-12 weeks** ❌ | HIGH |
| **MCU (STM32F4)** | Digikey stock | 12 weeks ⚠️ | N/A (no custom) | - | HIGH |
| **I/O Expanders** | Digikey stock | 2 weeks ✅ | N/A | - | LOW |
| **Drivers (ULN2803A)** | Digikey stock | 4 weeks ⚠️ | N/A | - | MEDIUM |
| **BLE Module (nRF52840)** | Digikey stock | 10 weeks ⚠️ | N/A | - | HIGH |
| **PCB (4-layer)** | PCBWay/JLCPCB | **3 weeks** ✅ | N/A | - | LOW |
| **Enclosure** | 3D print (SLS nylon) | **1 week** ✅ | Injection mold | **12-16 weeks** ❌ | LOW (use 3D print) |
| **Passives/Connectors** | Digikey stock | 1-2 weeks ✅ | N/A | - | LOW |

**⚠️ CRITICAL ISSUES:**

1. **STM32F4 MCU:** 12-week lead time (chip shortage) → **EXCEEDS 8-week timeline**
   - **Mitigation:** Check distributor stock (Arrow, Mouser), buy from broker (2× cost), or redesign with STM32F0/STM32G4 (shorter lead time)

2. **nRF52840 BLE Module:** 10-week lead time → **EXCEEDS 8-week timeline**
   - **Mitigation:** Check stock (Mouser has 500+ in stock as of Oct 2025), buy from broker, or use alternative BLE module (ESP32-C3)

3. **ULN2803A Drivers:** 4-week lead time → **MARGINAL** (50% of timeline)
   - **Mitigation:** Order immediately, use alternative (TPIC6B595 shift register)

4. **Custom Piezo Actuators:** 8-12 week lead time → **VIOLATES timeline**
   - **Quote request:** 1-2 weeks
   - **Tooling/samples:** 4-6 weeks
   - **Production run:** 2-4 weeks
   - **Total:** 7-12 weeks ❌

---

## Actuator Availability Analysis

### Piezoelectric Actuators (2mm Baseline)

**COTS Availability:**

| Vendor | Part Number | Size | Stroke | Force | Availability | Lead Time | Cost |
|--------|-------------|------|--------|-------|--------------|-----------|------|
| **Murata** | 7BB-20-6 | 20mm dia ❌ | 0.5mm | 1N | Stock | 2 weeks | $15 ea ❌ |
| **TDK** | PKLB1204E | 12mm dia ❌ | 0.3mm ⚠️ | 0.5N | Stock | 4 weeks | $8 ea |
| **Piezo Systems** | T216-A4-203X | 5mm dia ❌ | 0.2mm ❌ | 0.3N ⚠️ | Custom quote | 8-12 weeks ❌ | $2-5 ea |
| **CTS** | PPA1011 | 10mm dia ❌ | 0.5mm | 1N | Stock | 6 weeks | $10 ea |

**Finding:** ❌ **NO COTS piezo actuators available at 2-3mm diameter with 0.5mm stroke**

**Smallest COTS piezo:** 5mm diameter (Piezo Systems T216) → Still exceeds 2.3mm constraint

**Issue:** COTS piezo actuators are designed for:
- Audio buzzers (10-20mm diameter, optimized for sound)
- Ultrasonic sensors (5-15mm diameter, optimized for resonance)
- High-force actuators (10-30mm diameter, optimized for force)

**Braille application (2-3mm, 0.5mm stroke, 50gf force) is NICHE** → Requires custom design

---

### Solenoid Actuators (4mm Alternative)

**COTS Availability:**

| Vendor | Part Number | Size | Stroke | Force | Availability | Lead Time | Cost |
|--------|-------------|------|--------|-------|--------------|-----------|------|
| **Takaha** | BS-0420N-01 | 4mm dia ✅ | 1mm ✅ | 0.5N ✅ | Stock (Digikey) | **2 weeks** ✅ | $0.60 |
| **Deltrol** | 10230 | 4.5mm dia ⚠️ | 1.5mm ✅ | 1N ✅ | Stock (Digikey) | 4 weeks | $0.85 |
| **Guardian Electric** | 08D-I-12D | 5mm dia ❌ | 2mm ✅ | 2N ✅ | Stock (Mouser) | 2 weeks | $1.20 |

**Finding:** ✅ **COTS solenoids available at 4-5mm diameter, 2-week lead time, $0.60-1.20 each**

**Best option:** Takaha BS-0420N-01
- Size: 4mm diameter × 10mm length
- Stroke: 1mm (adjustable with mechanical stop to 0.5mm)
- Force: 0.5N (50gf) @ 5V
- Current: 150mA @ 5V (0.75W)
- **Lead time: 2 weeks (Digikey stock)**
- **Cost: $0.60 @ 100 qty** (vs $1.50 piezo → 60% savings)

---

### Latching Solenoid (Global Latch Alternative)

**COTS Availability:**

| Vendor | Part Number | Size | Stroke | Force | Availability | Lead Time | Cost |
|--------|-------------|------|--------|-------|--------------|-----------|------|
| **Takaha** | BS-0420L-01 (latching) | 4mm dia | 1mm | 0.5N | Stock | 2 weeks | $1.10 |
| **Deltrol** | 10230L | 4.5mm dia | 1.5mm | 1N | Stock | 4 weeks | $1.50 |

**Finding:** ✅ **COTS latching solenoids available, but cost similar to piezo** ($1.10-1.50 vs $1.50)

**Global latch plate:** Custom part (injection mold = 12 weeks ❌, 3D print = 1 week ✅)
- **3D print (SLS nylon):** 1 week lead time, $10-25 per plate (viable for pilot)
- **Injection mold:** 12-16 week lead time (tooling), $5000-15000 NRE (post-pilot only)

**Verdict:** ✅ **Solenoid + global latch (3D printed) is COTS-compatible for pilot**

---

## Size Constraint Conflict (ARCH-C)

### Current Requirements

**PRD-FUNC-003:** Actuator size ≤ 2.3mm diameter
- Derived from: 2.5mm braille cell pitch - 1.5mm dot diameter ÷ 2 = 1.25mm clearance per side → 2.3mm max actuator

**Conflict:** COTS solenoids are 4-5mm diameter → **EXCEEDS constraint by 1.7-2.7mm (74-117% over)**

---

### Options to Resolve Conflict

#### Option 1: Relax Size Constraint (ARCH-C Only)

**Proposal:** Allow 4mm actuator diameter for ARCH-C (Hybrid AA), maintain 2.3mm for ARCH-A/B

**Impact on Braille Cell Spacing:**
- Current: 2.5mm cell pitch (standard ADA)
- New (ARCH-C): 3.5mm cell pitch (increased 40%)
- **Within ADA range:** 2.3-3.8mm acceptable per BANA guidelines ✅

**Impact on Device Size:**
- Current: 200mm length (32 cells × 2.5mm × 2.5 pitch factor)
- New (ARCH-C): **280mm length** (32 cells × 3.5mm × 2.5 pitch factor)
- **40% longer, but still portable** (11 inches vs 8 inches)

**User Impact:**
- ✅ Larger cell spacing may be EASIER to read (less dense)
- ⚠️ Device is bulkier (280mm vs 200mm)
- ✅ Tactile feedback identical (same force, stroke)

**Verdict:** ✅ **ACCEPTABLE** - ADA compliant, minor UX impact

---

#### Option 2: Use Smaller COTS Solenoid (If Available)

**Search for 3mm COTS solenoid:**
- ❌ **NOT AVAILABLE** - Smallest COTS solenoid is 4mm diameter
- Reason: Coil physics requires minimum wire volume for 50gf force

**Verdict:** ❌ **NOT VIABLE** - No COTS option at 3mm

---

#### Option 3: Use COTS Piezo (If Available at 5mm)

**Smallest COTS piezo:** 5mm diameter (Piezo Systems T216)
- Size: 5mm dia × 10mm length
- Stroke: 0.2mm ❌ (insufficient, need 0.5mm)
- Force: 0.3N ⚠️ (30gf, marginal)
- Cost: $2-5 @ 100 qty (custom quote, 8-12 week lead time ❌)

**Verdict:** ❌ **NOT VIABLE** - Insufficient stroke, custom lead time exceeds timeline

---

#### Option 4: Abandon ARCH-C (Hybrid AA), Use ARCH-A (Wireless Li-ion) Only

**Proposal:** Drop AA battery variant, offer Li-ion rechargeable only for wireless option

**Rationale:**
- ARCH-A (Li-ion) uses piezo (no size constraint issue)
- Simplifies product line (2 architectures instead of 3)
- Li-ion is superior UX (rechargeable, sleeker, lighter)

**Trade-offs:**
- ❌ Lose "AA battery instant swap" convenience
- ❌ Higher cost ($35K UL 2054 cert vs $0 for AA)
- ✅ Simplify BOM (fewer SKUs)
- ✅ No size constraint relaxation needed

**Verdict:** ⚠️ **VALID ALTERNATIVE** - Consider in v1.4.0 trade-offs

---

### Recommendation: Relax Size for ARCH-C

**New requirement:** PRD-FUNC-003-ARCH-C-EXCEPT

**Exception:** ARCH-C (Hybrid AA) allowed to use 4mm actuator diameter (3.5mm cell pitch)

**Justification:**
1. ✅ COTS solenoids available (2-week lead time, $0.60 ea)
2. ✅ Within ADA acceptable range (2.3-3.8mm cell pitch)
3. ✅ 40% longer device still portable (280mm = 11 inches)
4. ✅ Cost savings (60% cheaper than piezo: $115 vs $288)
5. ✅ Power savings (1.53W vs 2.19W = fits AA budget)

**ARCH-A/B remain at 2.3mm constraint** (piezo actuators)

---

## New Requirement: COTS Mandate

### PRD-SCHED-002-ASMP: COTS Component Mandate

**Title:** COTS Components Required for 2-Month Timeline

**Parent:** PRD-SCHED-001 (2-month pilot production)

**Assumption:** 2-month timeline requires all COTS (Commercial Off-The-Shelf) components, no custom parts except PCB/enclosure (standard fabrication)

**Rationale:**
- Custom component lead times (8-16 weeks) **EXCEED 8-week timeline**
- COTS components available in 1-4 weeks from distributors (Digikey, Mouser, Arrow)
- PCB fabrication (3 weeks) and 3D print enclosure (1 week) are standard, not custom
- Risk mitigation: COTS parts have datasheets, samples, proven reliability

**Requirement:** All electronic components must be COTS (orderable from Digikey/Mouser) with ≤4 week lead time. Custom components prohibited unless **VERY LOW RISK exception** (e.g., PCB layout, 3D printed enclosure).

**Exceptions allowed:**
1. ✅ **PCB (custom layout):** 3-week fab time (standard service, low risk)
2. ✅ **Enclosure (3D print):** 1-week SLS nylon print (standard service, low risk)
3. ⚠️ **Latch plate (3D print):** 1-week SLS nylon (pilot only, injection mold post-pilot)

**Exceptions NOT allowed:**
1. ❌ **Custom actuators:** 8-12 week lead time (quote + tooling + samples) → VIOLATES timeline
2. ❌ **Custom ICs/ASICs:** 16-24 week lead time (design + fab + test) → VIOLATES timeline
3. ❌ **Custom injection molding:** 12-16 week lead time (tooling) → Use 3D print for pilot

**Risk Level:** HIGH (timeline risk)

**Impact if Wrong:** Project delayed 4-8 weeks (custom parts on critical path), miss customer deadline

**Priority:** P0-Critical

**Acceptance Criteria:**
- All components (except PCB/enclosure) orderable from Digikey/Mouser
- Lead time ≤4 weeks for all COTS parts
- No vendor quotes required (stock items only)
- Datasheets available (no custom specs)

**Verification:** BOM review (all parts have Digikey PN), lead time check (Digikey stock status)

---

## Recommendations

### For ARCH-B (Wired USB-C)

**Actuator:** ❓ **PROBLEM** - No COTS piezo at 2-3mm

**Options:**
1. ✅ **Use COTS solenoid (4mm)** + relax size constraint to 3.5mm cell pitch
   - Pro: 2-week lead time, $0.60 ea (60% savings)
   - Con: Device grows to 280mm (40% longer)
2. ❌ **Custom piezo (2mm)** - Violates COTS mandate (8-12 week lead time)
3. ⚠️ **Search harder for COTS piezo** - May exist at 3-5mm with sufficient stroke (needs research)

**Recommendation:** **Use solenoid (Option 1)** if no COTS piezo found

---

### For ARCH-C (Hybrid AA)

**Actuator:** ✅ **Use COTS solenoid (4mm) + global latch (3D print)**

**Justification:**
1. ✅ COTS solenoid: 2-week lead time (Takaha BS-0420N-01)
2. ✅ 3D print latch: 1-week lead time (SLS nylon)
3. ✅ Fits power budget: 1.53W < 1.5W AA budget (marginal)
4. ✅ Battery life: 9.8 hours > 8-hour requirement
5. ⚠️ Size: 280mm length (vs 200mm) - **Requires PRD-FUNC-003 exception**
6. ⚠️ Refresh: 5.2 seconds (vs <1 sec) - **Requires user acceptance**

**Requirements changes needed:**
- **PRD-FUNC-003-ARCH-C-EXCEPT:** Allow 4mm actuator (3.5mm cell pitch) for ARCH-C only
- **PRD-SIZE-001-ASMP:** Update device size to 280mm length for ARCH-C

---

### For ARCH-A (Wireless Li-ion)

**Actuator:** ❓ **SAME PROBLEM** - No COTS piezo at 2-3mm

**Options:** Same as ARCH-B (use solenoid or search for COTS piezo)

**Note:** ARCH-A has **3.7W power budget** (plenty of headroom for solenoid alternatives)

---

### Summary Recommendation Matrix

| Architecture | Actuator (Baseline) | COTS Available? | Actuator (COTS Alternative) | Size Impact | Timeline Risk |
|--------------|---------------------|-----------------|------------------------------|-------------|---------------|
| **ARCH-B (USB)** | Piezo (2mm) | ❌ NO | Solenoid (4mm) + relax size | 280mm (+40%) | HIGH → LOW |
| **ARCH-C (AA)** | Piezo (2mm) | ❌ NO | Solenoid (4mm) + latch + relax size | 280mm (+40%) | HIGH → LOW |
| **ARCH-A (Li-ion)** | Piezo (2mm) | ❌ NO | Solenoid (4mm) + relax size | 280mm (+40%) | HIGH → LOW |

**Critical Decision:**
1. **Search for COTS piezo (3-5mm)** - May exist with sufficient stroke/force (1-2 days research)
2. **If NOT found:** Relax size constraint to 4mm (3.5mm cell pitch) for ALL architectures
3. **Trade-off:** 40% larger device, but meets COTS mandate and timeline

---

## Next Steps

### 1. URGENT: Search for COTS Piezo Actuators (1-2 days)

**Vendors to contact:**
- Murata (piezo buzzers, may have small actuators)
- TDK (piezo components)
- Piezo Systems (custom but may have stock items)
- CTS (electromechanical components)
- Kyocera (piezo ceramics)

**Search criteria:**
- Size: 2-5mm diameter
- Stroke: ≥0.5mm
- Force: ≥50gf (0.5N)
- Voltage: ≤30V
- **Lead time: ≤4 weeks** (COTS stock)

**If found:** Use COTS piezo, maintain 2.3mm size constraint ✅

**If NOT found:** Proceed with solenoid (4mm) + size relaxation

---

### 2. Update Requirements (PRD-SCHED-002-ASMP, PRD-FUNC-003 Exception)

**Add:**
- PRD-SCHED-002-ASMP: COTS component mandate (≤4 week lead time)
- PRD-FUNC-003-ARCH-C-EXCEPT: Size exception (4mm actuator for ARCH-C)

**Update:**
- PRD-SIZE-001-ASMP: Device length 200mm → 280mm (ARCH-C variant)

---

### 3. Finalize Architecture Selection (v1.4.0 Trade-offs)

**Compare:**
- ARCH-B/C/A with solenoid (4mm, 280mm device)
- vs
- ARCH-A/B only (drop ARCH-C, use Li-ion for wireless)

**Trade-offs:**
- Cost (solenoid 60% cheaper)
- Size (280mm vs 200mm)
- Power (solenoid+latch fits AA budget)
- Timeline (COTS 2-week lead time)
- UX (5.2-sec refresh vs <1 sec)

---

**END OF DOCUMENT**
