# ARCH_SOL_ECO - Solenoid Selection & Mechanical Interface

**Architecture:** ARCH_SOL_ECO (Solenoid Economy with Rotary Cam)
**Document:** Technical notes on COTS solenoid selection and cam interface design
**Date:** 2025-10-12
**Status:** Engineering analysis - informs BOM and mechanical design

---

## Executive Summary

Selected **Olimex PUSH-PULL-SOLENOID-5V** as COTS actuator for ARCH_SOL_ECO rotary cam mechanism. Key findings:

- ✅ **4mm shaft diameter** matches cam interface requirement
- ✅ **Flat plunger face** ideal for cam follower contact (vs conical)
- ✅ **5-6VDC operation** simplifies power supply (vs 12V alternatives)
- ⚠️ **5mm stroke** requires mechanical stop to limit to 1mm (cam over-rotation protection)
- ⚠️ **$2.73 unit cost** vs $0.50 assumption → **$431 BOM impact** (192 units × $2.23 delta)
- ⚠️ **0.63A @ 5V** per solenoid → **121A peak** if all actuated (requires multiplexing)

**Updated ARCH_SOL_ECO BOM:** $708 pilot (was $277) due to solenoid cost correction

---

## Part Specifications

### Olimex PUSH-PULL-SOLENOID-5V

**Manufacturer:** Olimex Ltd.
**Part Number:** PUSH-PULL-SOLENOID-5V
**Digikey PN:** (Available at Digikey - exact PN TBD)
**Price:** €2.50 (~$2.73 USD)
**Lead Time:** ~4 weeks (standard Digikey stock)

### Electrical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Voltage | 5-6 VDC | Matches system logic level |
| Current @ 5V | 0.63 A | 3.15W per solenoid |
| Current @ 6V | 0.75 A | 4.5W per solenoid |
| Coil Resistance | 6 Ω | Pure resistive load |
| Duty Cycle | Pulse only | Max 5 sec continuous (thermal limit) |

**Power Consumption Analysis:**
- Single solenoid: 3.15W @ 5V
- 192 solenoids (all actuated): 121A @ 5V = **605W peak**
- **Mitigation:** Multiplex actuation (max 32 characters × 1 dot = 32 solenoids active = 20A @ 5V = 100W)

### Mechanical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Shaft Diameter | **4mm** | ✓ Matches cam follower interface |
| Shaft Length | 15.1mm | Extends beyond body |
| Stroke Length | **5mm** | Mechanically limited to 1mm by housing stop |
| Body Dimensions | 8 × 10.3 × 16.3 mm (W × H × D) | Open-frame design |
| Wire Length | 150mm | With 2.54mm connector |
| Mounting | Chassis mount | Requires custom bracket |

### Plunger End Shape

**Type:** **Flat face** (vs conical alternative)

**Advantages for cam follower application:**
- ✅ Larger contact area with cam surface → lower contact stress
- ✅ Simpler geometry → easier cam profile design
- ✅ Better for short stroke (<1.5mm) per industry best practice
- ✅ Higher holding force (vs conical)
- ✅ Lower manufacturing cost (vs conical machining)

**Cam Interface Design:**
```
    Solenoid Shaft                 Cam Disc
    (Flat Face)                    (12mm dia)
         ↓                              ↓
    ┌────────┐                      ╔═════╗
    │  ████  │──────────→           ║  ○  ║
    │  ████  │  Horizontal          ║ ╱ ╲ ║ ← Rotates ±45°
    │  ████  │  1mm stroke          ║●   ●║    (cam profile)
    └────────┘                      ╚═════╝
         ↑                              ↑
    Flat plunger face            Cam follower surface
    (4mm dia contact)            (tangent contact point)
```

**Contact Point:** Solenoid flat face contacts cam at 4:00 position (horizontal tangent)

---

## Mechanical Interface Design

### Stroke Limiting Mechanism

**Challenge:** Solenoid has 5mm stroke, but cam only needs 1mm stroke to achieve ±45° rotation.

**Solution:** Mechanical stop integrated into cam housing

```
SIDE VIEW - Stroke Limiting:

┌─────────────────────────────────────────────────────────┐
│  Cam Housing with Integrated Stop                       │
└─────────────────────────────────────────────────────────┘

    RETRACTED (Default State):
    ═══════════════════════════════════════════════════════

    Housing Wall
         │
         │   ┌────────┐
         │   │Solenoid│
         │   │ Shaft  │───→ Ready to extend
         │   └────────┘
         │        ↓
         │   [Cam Disc] ← At rest (0°)
         │        ↓
         └───[STOP]───────── Housing stop (limits retraction)


    EXTENDED (Actuated, 1mm stroke):
    ═══════════════════════════════════════════════════════

    Housing Wall
         │
         │        ┌────────┐
         │        │Solenoid│
         │   ←────│ Shaft  │ Extended 1mm
         │        └────────┘
         │             ↓
         │        [Cam Disc] ← Rotated 45°
         │             ↓
         └────────[STOP]───── Housing stop prevents over-rotation


    FAIL-SAFE (If solenoid tries 5mm stroke):
    ═══════════════════════════════════════════════════════

    Housing Wall
         │
         │             ┌────────┐
         │             │Solenoid│
         │   ←─────────│ Shaft  │ Wants 5mm, blocked at 1mm
         │             └────────┘
         │                  ↓
         │   ┌─────┐   [Cam Disc] ← Rotation STOPPED by housing
         │   │STOP │───────↓
         └───┴─────┴───────────── Cam can't rotate past ±45°

         Mechanical stop prevents:
         - Cam over-rotation (would jam piston)
         - Excessive solenoid force (spring compression absorbs)
         - Damage to cam profile or bearings
```

**Implementation:**
- Cam housing has internal boss that contacts cam disc outer rim at ±45° rotation
- Solenoid spring absorbs excess force when stopped
- No electronic limiting needed (pure mechanical fail-safe)

### Contact Force Analysis

**Solenoid Output Force:** ~0.5N (manufacturer spec, not confirmed)

**Cam Contact Pressure:**
- Contact area: 4mm shaft × ~1mm contact width = 4mm²
- Contact pressure: 0.5N ÷ 4mm² = **0.125 MPa** (very low)
- Cam material: Delrin POM (compressive strength ~100 MPa)
- **Safety factor:** 800× (no wear concern)

**Cam Bearing Force:**
- Tangential force at cam surface: 0.5N
- Moment arm: 6mm (cam radius)
- Torque: 3 N·mm
- Shaft bearing: brass or PTFE bushing (adequate for low speed, low load)

---

## Alternative Solenoids Considered

### Option 1: Olimex PUSH-PULL-SOLENOID-5V ✓ SELECTED
- **Pros:** 4mm shaft, flat face, 5V operation, Digikey stock
- **Cons:** 5× cost assumption ($2.73 vs $0.50), 5mm stroke (needs limit)
- **Decision:** Best available COTS option, cost increase justified by low technical risk

### Option 2: 12V Miniature Solenoids (Amazon/eBay)
- **Pros:** Lower cost (~$1.00 ea), 4mm stroke available
- **Cons:** 12V requires additional boost converter (+cost, +complexity), unknown reliability, no Digikey stock (supply chain risk), no datasheet
- **Decision:** Rejected due to supply chain risk and certification concerns

### Option 3: Custom Solenoid (Chinese OEM)
- **Pros:** Can specify exact stroke (1mm), potentially lower cost at volume (>10K units)
- **Cons:** Long lead time (12+ weeks), requires MOQ (1000+ units), tooling cost ($5K+), no pilot availability
- **Decision:** Rejected for pilot phase, **revisit for production** if volume justifies

### Option 4: Voice Coil Actuator
- **Pros:** Linear force-displacement, precise positioning, no stroke limiting needed
- **Cons:** 10× cost ($20+ ea), requires closed-loop control (encoder feedback), higher complexity
- **Decision:** Rejected due to cost and complexity (violates ECO tier strategy)

---

## Cost Impact Analysis

### Original BOM Assumption (Placeholder)

| Item | Qty | Unit Cost | Line Total |
|------|-----|-----------|------------|
| Solenoid (assumed) | 192 | $0.50 | $96.00 |

### Updated BOM (Olimex Real Part)

| Item | Qty | Unit Cost | Line Total |
|------|-----|-----------|------------|
| Solenoid (Olimex) | 192 | $2.73 | **$524.16** |

### BOM Delta

| Parameter | Original | Updated | Delta |
|-----------|----------|---------|-------|
| Solenoid Line Total | $96.00 | $524.16 | **+$428.16** |
| ARCH_SOL_ECO Total (Pilot) | $276.58 | **$704.74** | **+$428.16 (155%)** |
| ARCH_SOL_ECO Total (Production) | $215.90 | **$644.06** | **+$428.16 (198%)** |

**Impact on Architecture Ranking:**
- **Original ranking:** ARCH_SOL_ECO ($216) < ARCH_PIEZO_ECO ($420) < ARCH_PIEZO_DLX ($442)
- **Updated ranking:** ARCH_SOL_ECO ($644) > ARCH_PIEZO_ECO ($420) < ARCH_PIEZO_DLX ($442)
- **⚠️ CRITICAL:** ARCH_SOL_ECO is **NO LONGER the lowest cost option** due to solenoid price correction

**Recommendation:**
1. **Re-run trade-off analysis** with corrected BOM costs
2. **Investigate custom solenoid** for production (potential $1.00 ea → $192 line total → $316 production BOM)
3. **Consider ARCH_PIEZO_ECO as new cost leader** ($420 pilot, $436 production)

---

## Power Supply Considerations

### Peak Power Calculation

**Worst-case scenario:** All 192 solenoids actuated simultaneously (unlikely in practice)

| Parameter | Value | Calculation |
|-----------|-------|-------------|
| Solenoid Current | 0.63 A @ 5V | Per datasheet |
| Total Solenoids | 192 | 32 characters × 6 dots |
| **Peak Current** | **121 A @ 5V** | 192 × 0.63A |
| **Peak Power** | **605 W** | 121A × 5V |

**Reality check:** This is **not feasible** for portable device or USB power.

### Multiplexing Strategy (Required)

**Approach:** Actuate one character at a time (6 dots simultaneously)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Dots per character | 6 | Standard braille cell |
| Characters actuated | 1-4 simultaneous | Reasonable for refresh rate |
| Solenoids active (max) | 24 | 4 characters × 6 dots |
| **Multiplexed Current** | **15.1 A @ 5V** | 24 × 0.63A |
| **Multiplexed Power** | **75.5 W** | 15.1A × 5V |

**Refresh strategy:**
1. Divide 32 characters into 8 groups of 4 characters
2. Actuate one group at a time (6ms pulse each)
3. Total refresh cycle: 48ms (20 Hz refresh rate)
4. User perceives as simultaneous (persistence of touch ~100ms)

**Power supply implications:**
- **AA battery option:** 4×AA = 6V, boost to 5V regulated, **76W peak** → Need high-discharge AA cells (>10A capable) or supercapacitor buffer
- **USB-C option:** USB-C PD can deliver 15W (3A @ 5V) standard, 100W (5A @ 20V) with PD negotiation → **Insufficient for 76W at 5V** unless using 20V input + buck converter

**Recommendation:**
- Use **supercapacitor buffer** (1F @ 5V) to handle 6ms pulses (C = I·t/V = 15A × 6ms / 0.5V droop = 180mF minimum)
- Average power: 76W × (6ms / 48ms duty cycle) = **9.5W average** → feasible for USB-C PD or AA batteries

---

## Mechanical Design Checklist

### Cam Housing Design Requirements

- [ ] Integrated mechanical stop to limit cam rotation to ±45°
- [ ] Solenoid mounting bracket (8×10.3×16.3mm clearance)
- [ ] Cam shaft bushing (brass or PTFE, 2mm shaft dia)
- [ ] Piston linear bushing (5mm OD, 3.1mm ID)
- [ ] Spring retention pocket (8mm free length compression spring)
- [ ] Wire routing channel (150mm lead length × 192 solenoids)
- [ ] Assembly alignment features (snap-fit or screw bosses)
- [ ] User touch surface (braille dot holes, 1.2mm dia, 2.5mm pitch)

### Cam Disc Design Requirements

- [ ] Cam profile for ±45° rotation → 0.7mm vertical piston displacement
- [ ] Flat tangent surface at 4:00 position (solenoid contact)
- [ ] Eccentric pin at 8:00 position (piston connection)
- [ ] Shaft hole (2mm dia, press-fit or adhesive bond)
- [ ] Material: Delrin POM (low friction, high wear resistance)
- [ ] Tolerance: ±0.2mm (injection molded production)

### Solenoid Interface Requirements

- [ ] Flat face contact (4mm dia shaft)
- [ ] 1mm stroke limit (housing stop)
- [ ] Horizontal orientation (perpendicular to braille surface)
- [ ] Spring return to rest position (NdFeB magnet holds unpowered state)
- [ ] Electrical connection: 2.54mm connector or solder pads
- [ ] Wire strain relief (150mm leads, flexible routing)

---

## Testing & Validation Plan

### Prototype Phase

1. **Single solenoid bench test:**
   - Verify 5V actuation (0.63A current draw)
   - Measure actual stroke (confirm 5mm datasheet spec)
   - Test flat face contact with cam disc (3D printed SLA)
   - Measure force output (should be ~0.5N, verify with scale)
   - Thermal test (5 sec continuous, check coil temperature rise)

2. **Single cam mechanism assembly:**
   - Solenoid → Cam → Piston → Braille dot full kinematic chain
   - Verify ±45° rotation → 0.7mm vertical travel
   - Test mechanical stop (attempt 5mm stroke, confirm 1mm limit)
   - Measure friction (should be <0.1N with PTFE bushings)
   - Validate braille dot height (0.5mm ± 0.05mm)

3. **Single character test (6 dots):**
   - Wire 6 solenoids to driver circuit (ULN2803A)
   - Multiplex test (actuate dots sequentially, measure timing)
   - Power consumption (6 × 0.63A = 3.78A @ 5V = 18.9W)
   - Thermal test (continuous refresh for 5 min, check for hot spots)

4. **Full device test (32 characters, 192 solenoids):**
   - Multiplexed refresh (4 characters simultaneous, 8 groups)
   - Power consumption (24 × 0.63A = 15.1A peak, 9.5W average)
   - Refresh rate validation (20 Hz, user perceives as simultaneous)
   - Thermal mapping (IR camera, identify hot spots)
   - Mechanical reliability (10,000 cycle test per dot)

### Pilot Phase

1. **Environmental testing:**
   - Temperature range: 0°C to 40°C (indoor use)
   - Humidity: 10% to 90% RH (non-condensing)
   - Shock/vibration: Drop test from 1m (simulate desk fall)

2. **User acceptance testing:**
   - Tactile feedback quality (compare to commercial braille displays)
   - Refresh rate perception (is 20 Hz fast enough?)
   - Acoustic noise (solenoid clicking, is it acceptable?)

3. **Certification testing:**
   - UL 60950-1 (IT equipment safety)
   - FCC Part 15 Class B (EMI/EMC)
   - ADA 703.3 compliance (braille spacing, dot height, force)

---

## Design Trade-offs Summary

| Parameter | Solenoid Choice | Impact | Mitigation |
|-----------|----------------|--------|------------|
| **Cost** | Olimex $2.73 vs $0.50 assumed | +$428 BOM (+155%) | Investigate custom solenoid for production |
| **Stroke** | 5mm vs 1mm needed | Requires mechanical stop | Integrated into cam housing design |
| **Plunger Shape** | Flat face (best for cam) | None (optimal) | N/A |
| **Power** | 0.63A per solenoid = 121A peak | Requires multiplexing | 4-char groups, 20 Hz refresh |
| **Supply Chain** | Digikey stock, 4-week lead | Low risk | COTS part, multiple distributors |
| **Technical Risk** | Proven technology | Low risk | Solenoids used in automotive, medical |

---

## Conclusion

Selected **Olimex PUSH-PULL-SOLENOID-5V** as COTS actuator for ARCH_SOL_ECO despite **$428 BOM cost increase** (+155%). Key factors:

**Advantages (Why ARCH_SOL_ECO still viable):**
- ✅ **Flat plunger face** ideal for cam interface (vs conical alternatives)
- ✅ **4mm shaft diameter** enables standard 2.5mm braille spacing (key innovation)
- ✅ **COTS availability** at Digikey → low supply chain risk (vs custom solenoid 12-week lead)
- ✅ **5V operation** simplifies power supply (vs 12V alternatives)
- ✅ **Proven technology** → low technical risk (automotive/medical heritage)

**Challenges (Engineering work required):**
- ⚠️ **Cost no longer competitive** ($644 vs $420 ARCH_PIEZO_ECO) → Need custom solenoid for production
- ⚠️ **High power consumption** (76W peak) → Multiplexing + supercap buffer required
- ⚠️ **5mm stroke over-design** → Mechanical stop required (adds housing complexity)

**Recommendation:**
1. Use Olimex part for **pilot phase** (100 units) to validate cam mechanism concept
2. Negotiate **custom solenoid** ($1.00 target) for **production phase** (1000+ units) to restore cost competitiveness
3. Re-run **trade-off analysis** with corrected BOM ($644 vs $420 vs $442) to confirm architecture selection

**Updated ARCH_SOL_ECO value proposition:**
- **Pilot:** $644 BOM (non-competitive) but **fastest to market** (2-week solenoid lead vs 8-week piezo)
- **Production:** $316 BOM potential (if custom solenoid @ $1.00) → **Restores cost leadership**
- **Key innovation:** Rotary cam enables standard 2.5mm braille spacing with COTS actuators

---

**End of Document**
