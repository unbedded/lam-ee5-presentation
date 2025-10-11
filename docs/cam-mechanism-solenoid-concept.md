# ARCH-SOL: Rotary Cam Mechanism for COTS Solenoid Actuation

**Project:** Lam Research EE Concept Evaluation
**Author:** Spencer Barrett
**Date:** 2025-10-09
**Status:** Concept - Replaces ARCH-D (ARCH-D violated braille spacing standard)

---

## Executive Summary

**Problem:** ARCH-D required 3.5mm cell pitch (vs 2.5mm standard) to fit 4mm COTS solenoids → **280mm device length** → **Violates braille muscle memory** (users must retrain brain for non-standard spacing)

**Solution:** **ARCH-SOL** uses rotary cam mechanism (motorcycle engine concept) to decouple solenoid size from braille spacing → **198mm standard ADA spacing** ✅

**Key Insight:** Solenoids actuate **perpendicular** to dot motion, not inline. Cam converts horizontal solenoid stroke → vertical dot displacement via angular rotation.

---

## Why ARCH-D is a Non-Starter

**Critical Flaw:** Non-standard braille spacing (3.5mm vs 2.5mm standard)

**User Impact:**
- Braille readers develop **muscle memory** for standard 2.5mm dot spacing
- Similar to Morse code or Japanese character recognition - **pattern recognition is spatial**
- Non-standard spacing forces users to **retrain their brain** (unacceptable UX)
- **Market rejection risk:** Users won't adopt device that "feels wrong"

**Analogy:** Like a QWERTY keyboard with 1.2× key spacing - typists would constantly mistype

**Lesson Learned:** ARCH-D was valuable **design exploration** (proved solenoid cost savings $96 vs $288 piezo), but violated fundamental UX requirement

**Replacement:** ARCH-SOL preserves solenoid cost savings while maintaining **standard 2.5mm braille spacing**

---

## Mechanical Architecture: Motorcycle Engine Concept

### Core Innovation

**Analogy:** Motorcycle V-twin engine (opposing cylinders) but with **limited rotation (±45°)** instead of continuous rotation

**Key Transformation:** Horizontal solenoid motion → Rotary cam motion (±45°) → Vertical piston motion (0.7mm stroke)

### Single Character Module (6 Dots)

**3 layers of opposing solenoid pairs = 6 dots total per character**

```
VIEW: Side view of 3-layer stack (one braille character)

LAYER 1 (Top):
   Dot 1 (UP)                          Dot 4 (UP)
      ↑                                    ↑
   Piston                              Piston
   (8:00→12:00)                       (8:00→12:00)
      ↕                                    ↕
   [Cam Disc ⟲]───────────────────[Cam Disc ⟳]
    ↖ Solenoid L1                  Solenoid R1 ↗
      (4:00→8:00)                      (4:00→8:00)
   [PCB Left]                          [PCB Right]

LAYER 2 (Middle):
   Dot 2                                Dot 5
   [Same mechanism, horizontally offset by 2.5mm from Layer 1]

LAYER 3 (Bottom):
   Dot 3                                Dot 6
   [Same mechanism, horizontally offset by 5.0mm from Layer 1]
```

**Actuation Sequence (Raise Dot 1):**
1. **Solenoid L1 fires** (50ms pulse) → Pushes cam disc at 4:00 position
2. **Cam rotates clockwise** (±45° rotation) → 4:00 → 8:00
3. **Piston connected at 8:00** → Rotates to 12:00 position
4. **Piston moves vertically** (0.7mm stroke) → Dot 1 raised
5. **Mechanical brake engages** at 12:00 (gravity + detent)
6. **Solenoid L1 OFF** → Zero hold power (mechanical lock)

**Lower Dot:**
1. **Solenoid R1 fires** (counter-rotation) → Cam rotates counter-clockwise
2. Piston retracts from 12:00 → 8:00 → Dot lowered
3. Spring return assists retraction

---

## Key Features

### 1. Standard Braille Spacing ✅
- **Cell pitch:** 2.5mm (standard ADA 703.3)
- **Device length:** 32 chars × 6.2mm = **198mm** (standard, not 280mm ARCH-D)
- **User experience:** No retraining required (muscle memory preserved)

### 2. COTS Solenoid Compatibility ✅
- **Solenoid diameter:** 4mm (Takaha BS-0420N-01, Digikey stock)
- **Lead time:** 2 weeks (meets PRD-SCHED-002-ASMP)
- **Cost:** $0.50 ea (192× = $96 total vs $288 piezo)

### 3. Perpendicular Actuation
- **Solenoids mount horizontally** (left/right PCBs)
- **Dots actuate vertically** (cam converts horizontal → vertical)
- **Decouples** solenoid size from braille spacing constraint

### 4. Modular "Rinse and Repeat" Design ✅
- **6-dot character = standardized subassembly**
- 32 identical character modules stack horizontally
- **Assembly:** Snap-together injection molded parts
- **Repair:** Swap individual character modules (not entire device)

### 5. Zero Hold Power ✅
- **Mechanical brake** at 12:00 position (gravity + detent)
- **No electrical latch** needed (vs ARCH-D global latch complexity)
- **Battery life:** Same as ARCH-D (solenoid only active during actuation)

---

## Manufacturing Strategy: 3D Print → Proto Molds → Production Molds

### Phase 1: Prototype Testing (Weeks 1-4)
**Goal:** Risk reduction, validate cam profiles, piston alignment, friction

**Method:** 3D printed parts (SLA resin for precision)
- **Cam discs:** 3D print (0.1mm tolerance, SLA resin)
- **Piston rods:** 3D print (Nylon or ABS)
- **Housing:** 3D print (FDM or SLA)
- **Linear bushings:** 3D print or COTS brass bushings

**Testing:**
- Cam profile optimization (acceleration curves, backlash)
- Piston alignment (binding issues, friction)
- Solenoid actuation timing (push-pull vs push-spring)
- Layer offset validation (mechanical interference check)
- Durability testing (1000-cycle life test)

**Cost:** $500-1000 (3D printing service)
**Timeline:** 2 weeks design + 2 weeks prototype + 2 weeks testing = **6 weeks**

---

### Phase 2: Pilot Production (Weeks 5-8) - Proto Molds
**Goal:** 10-100 units for validation, use "proto molds" (soft tooling)

**Method:** Soft tooling (aluminum molds, 1K-10K shot life)
- **Cam discs:** Aluminum mold ($3K-5K per mold, 2-week lead time)
- **Piston rods:** Aluminum mold ($2K-3K per mold)
- **Housing:** Aluminum mold ($5K-8K per mold)
- **Linear bushings:** COTS or aluminum mold ($2K per mold)

**Material:** Engineering plastics (Delrin POM, ABS, PC)
- **Tolerance:** ±0.1mm (tighter than production molds)
- **Cost per part:** $0.50-2.00 (labor-intensive, manual ejection)

**Pilot volume:** 100 units
- Validates injection molding feasibility
- Identifies tolerance stack-up issues
- Tests assembly automation concepts

**Cost:** $20K-30K (tooling + 100 units)
**Timeline:** 2 weeks tooling + 1 week molding + 1 week assembly = **4 weeks**

---

### Phase 3: Production (Post-Pilot) - Hard Tooling
**Goal:** 1K-100K+ units, use hardened steel molds (long-life precision)

**Method:** Hardened steel molds (100K-1M shot life)
- **Cam discs:** Steel mold ($15K-25K per mold, 4-6 week lead time)
- **Piston rods:** Steel mold ($10K-15K per mold)
- **Housing:** Steel mold ($25K-40K per mold)
- **Linear bushings:** Steel mold ($10K per mold)

**Material:** Same engineering plastics (Delrin POM, ABS, PC)
- **Tolerance:** ±0.2mm (standard injection molding)
- **Cost per part:** $0.05-0.50 (fully automated, high throughput)

**Production volume:** 10K+ units
- Amortizes tooling cost ($70K-90K ÷ 10K = $7-9 per unit)
- Per-unit cost drops to $0.15-0.30 (parts only)

**Timeline:** 6 weeks tooling + ongoing production

---

## BOM Cost Estimate (Pilot vs Production)

### Pilot Volume (100 units, Proto Molds)

| Component | Qty/Char | Cost/Unit | Cost/Char | Total (32 chars) |
|-----------|----------|-----------|-----------|------------------|
| Solenoid (4mm COTS) | 6 | $0.50 | $3.00 | **$96.00** |
| Cam disc (proto mold) | 3 | $1.00 | $3.00 | $96.00 |
| Piston rod (proto mold) | 6 | $0.75 | $4.50 | $144.00 |
| Linear bushing (COTS) | 6 | $0.20 | $1.20 | $38.40 |
| Housing (proto mold) | 1 | $2.00 | $2.00 | $64.00 |
| Spring (compression) | 6 | $0.02 | $0.12 | $3.84 |
| **Actuation Subtotal** | | | **$13.82** | **$442.24** |
| Control MCU + drivers + PCBs | | | | $42.40 |
| USB-C + BLE module | | | | $13.50 |
| Enclosure | | | | $25.00 |
| **Pilot BOM Total** | | | | **$523.14** |

**Note:** High pilot BOM due to proto mold labor costs. Production BOM much lower.

---

### Production Volume (10K units, Hard Tooling)

| Component | Qty/Char | Cost/Unit | Cost/Char | Total (32 chars) |
|-----------|----------|-----------|-----------|------------------|
| Solenoid (4mm COTS) | 6 | $0.50 | $3.00 | **$96.00** |
| Cam disc (steel mold) | 3 | $0.15 | $0.45 | $14.40 |
| Piston rod (steel mold) | 6 | $0.10 | $0.60 | $19.20 |
| Linear bushing (steel mold) | 6 | $0.08 | $0.48 | $15.36 |
| Housing (steel mold) | 1 | $0.50 | $0.50 | $16.00 |
| Spring (compression) | 6 | $0.02 | $0.12 | $3.84 |
| **Actuation Subtotal** | | | **$4.75** | **$152.00** |
| Control MCU + drivers + PCBs | | | | $42.40 |
| USB-C + BLE module | | | | $13.50 |
| Enclosure (injection molded) | | | | $8.00 |
| **Production BOM Total** | | | | **$215.90** |

**vs ARCH-C (piezo):** $215.90 vs $435.85 = **50% cost savings** ✅

---

## Specifications

| Metric | Value | Notes |
|--------|-------|-------|
| **Device Size** | 198mm × 105mm × 25mm | Standard ADA spacing ✅ |
| **BOM Cost (Pilot)** | $523 | Proto molds (high labor cost) |
| **BOM Cost (Production)** | $216 | Steel molds (50% savings vs piezo) |
| **Refresh Speed** | 2.4 sec | 8-way parallel actuation |
| **Hold Power** | 0W | Mechanical brake (gravity + detent) |
| **Battery Life** | 8 hours | 4× AA, 1.53W avg (same as ARCH-D) |
| **Timeline (Pilot)** | 10 weeks | 6 weeks proto + 4 weeks pilot |
| **Manufacturing** | Injection molding | ±0.2mm tolerance, automation-friendly |
| **Assembly** | Modular 6-dot subassemblies | Snap-together, automation-ready |

---

## Advantages

### vs ARCH-D (Global Latch)
✅ **Standard braille spacing** (2.5mm, not 3.5mm) - No user retraining
✅ **Smaller device** (198mm, not 280mm) - 29% shorter
✅ **Faster refresh** (2.4 sec, not 5.2 sec) - 2× faster
✅ **Lower technical risk** - Cam mechanisms proven (automotive, robotics)
✅ **Better DFM** - Injection molding beats precision latch alignment

### vs ARCH-C (Piezo)
✅ **50% cost savings** ($216 vs $436 production BOM)
✅ **COTS solenoids** (2-week lead time, meets PRD-SCHED-002-ASMP)
✅ **Modular repair** (swap character modules, not entire actuator array)
✅ **Tolerance-friendly** (±0.2mm molding OK, vs ±0.05mm piezo mounting)

### vs ARCH-B (Wired Piezo)
✅ **Wireless capable** (BLE + USB dual interface)
✅ **50% cost savings** ($216 vs $420)
✅ **Battery powered** (portable, not tethered)

---

## Disadvantages

⚠️ **Complex ME design** - Cam profiles, layer offsets, piston alignment require skilled mechanical engineer

⚠️ **Higher NRE** - $70K-90K steel tooling (vs $10K 3D print ARCH-D)

⚠️ **Longer timeline** - 10 weeks (6 proto + 4 pilot) vs 8.5 weeks ARCH-D

⚠️ **Assembly complexity** - 6-part assembly per character × 32 = 192 parts to assemble

⚠️ **Moderate refresh speed** - 2.4 sec (vs 1.5 sec piezo, but acceptable for beginners)

⚠️ **High pilot BOM** - $523 per unit (proto molds) vs $224 ARCH-D (3D print)

---

## Engineering Challenges (Solvable)

### 1. Cam Profile Design
**Challenge:** Non-linear cam profile to achieve constant velocity or smooth acceleration

**Solution:**
- CAD simulation (SolidWorks cam design tools)
- 3D print prototypes (SLA resin, 0.1mm tolerance)
- Iterate cam profile based on motion analysis
- **Reference:** Automotive cam design textbooks, robotics cam mechanisms

### 2. Layer Offset Calculation
**Challenge:** 3 layers must not mechanically interfere

**Solution:**
- **Vertical spacing:** 5mm per layer (4mm solenoid + 1mm housing) × 3 = 15mm stack height ✅
- **Horizontal offset:** Stagger by 2.5mm per layer (braille dot pitch)
- **Clearance check:** CAD assembly simulation (SolidWorks interference detection)

### 3. Piston Alignment and Friction
**Challenge:** Piston must slide vertically without binding (0.7mm stroke, ±0.1mm tolerance)

**Solution:**
- **Linear bushings:** Injection molded guides or COTS brass bushings
- **Lubrication:** Dry lube (PTFE coating, molybdenum disulfide)
- **Spring return:** Compression spring at top, piston retracts when cam rotates back
- **Prototype testing:** 1000-cycle life test to validate friction levels

### 4. Solenoid Actuation Strategy
**Challenge:** Sequential actuation too slow (19.2 sec for 32 chars)

**Solution:**
- **Parallel actuation:** 8 characters simultaneously (24 solenoids active)
- **Timeline:** 600ms per 6-dot char × 4 batches = **2.4 sec total** ✅
- **Power budget:** 24 solenoids × 50mW = 1.2W peak (fits AA budget)

### 5. Mechanical Brake Design
**Challenge:** Maintain dot position with zero hold power

**Solution:**
- **Gravity assist:** Piston at 12:00 vertical position, gravity pulls down
- **Detent:** Small indent or friction pad at 12:00 position locks cam
- **Spring preload:** Compression spring provides slight downward force
- **Prototype testing:** Validate brake holds position for 30+ seconds

---

## Architecture Comparison Summary

| Criteria | ARCH-B (Wired) | ARCH-C (Piezo Hybrid) | **ARCH-SOL (Cam)** | ARCH-A (Li-ion Wireless) |
|----------|----------------|------------------------|-------------------|--------------------------|
| **BOM Cost (Production)** | $420 | $436 | **$216** ⭐ | $449 |
| **Device Size** | 200mm | 220mm | **198mm** ⭐ | 210mm |
| **Braille Spacing** | 2.5mm ✅ | 2.5mm ✅ | **2.5mm** ✅ ⭐ | 2.5mm ✅ |
| **Refresh Speed** | 1.5 sec | 1.5 sec | 2.4 sec | 1.5 sec |
| **Hold Power** | 2.5W | 1.5W | **0W** ⭐ | 1.0W |
| **Battery Life** | ∞ (USB) | 18 hrs | **8 hrs** | 10 hrs |
| **Timeline (Pilot)** | 6 wks | 7.5 wks | 10 wks | 8 wks |
| **NRE (Pilot)** | $35K | $55K | $70K | $70K |
| **Technical Risk** | LOW | MEDIUM | **MEDIUM** | MEDIUM |
| **Manufacturing** | Good | Good | **Excellent** (injection mold) ⭐ | Good |
| **Modularity** | None | None | **Excellent** (character modules) ⭐ | None |

⭐ = Best in category or top-tier performance

---

## Recommendation

**ARCH-SOL should REPLACE ARCH-D** as the solenoid-based architecture option.

**Reasons:**
1. **Standard braille spacing** - ARCH-D's 3.5mm pitch violates muscle memory (non-starter)
2. **50% cost savings** - $216 vs $436 piezo (production volume)
3. **Lower technical risk** - Cam mechanisms proven vs unproven global latch
4. **Better manufacturability** - Injection molding scalable, modular assembly
5. **Standard device size** - 198mm (ADA compliant) vs 280mm ARCH-D

**Trade-offs:**
- **Higher NRE** - $70K steel tooling vs $60K ARCH-D (justified by lower technical risk)
- **Longer timeline** - 10 weeks vs 8.5 weeks ARCH-D (justified by standard spacing)
- **Moderate refresh** - 2.4 sec vs 1.5 sec piezo (acceptable for target market)

---

## Next Steps

1. **Update source/architectures.yaml** - Replace ARCH-D with ARCH-SOL
2. **Update docs/architecture.md** - Replace ARCH-D section with ARCH-SOL
3. **Update TODO.md** - Mark v1.3.0 complete with ARCH-SOL substitution
4. **Proceed to v1.4.0** - Trade-off Analysis with 4 architectures (A, B, C, SOL)

---

## Design Evolution Context

**ARCH-D (Global Latch) → ARCH-SOL (Rotary Cam)**

ARCH-D was a valuable **design exploration** that proved:
- ✅ Solenoid cost savings feasible ($96 vs $288 piezo)
- ✅ COTS parts meet timeline constraint (2-week lead time)
- ✅ Zero hold power achievable (mechanical lock vs electrical)

**Critical lesson learned:** Non-standard braille spacing (3.5mm) violates fundamental UX requirement (users must retrain muscle memory)

**ARCH-SOL preserves all ARCH-D benefits** while maintaining standard 2.5mm spacing via rotary cam mechanism.

**Analogy:** Like learning Morse code or Japanese characters - **spatial patterns are muscle memory**. Changing spacing = forcing brain retraining = market rejection.

---

## References

- **Braille Standards:** ADA 703.3 (2.5mm dot spacing, 6.2mm cell center-to-center)
- **Cam Design:** SolidWorks Cam Design Tutorial, Automotive Cam Profile Analysis
- **Injection Molding:** Protolabs Design Guide (tolerance ±0.2mm for engineering plastics)
- **Solenoid Specs:** Takaha BS-0420N-01 datasheet (4mm dia, 1mm stroke, 0.5N force)
- **User Research:** Braille muscle memory studies (spatial pattern recognition)

---

**Document Status:** ✅ Complete - Ready for architecture database update
**Next Milestone:** Update architectures.yaml, proceed to v1.4.0 Trade-off Analysis
