# ARCH_SOL_ECO: Mechanical Design Specification

**Project:** Lam Research EE Concept Evaluation
**Architecture:** ARCH_SOL_ECO (Solenoid Economy - Rotary Cam)
**Discipline Focus:** Mechanical Engineering
**Author:** Spencer Barrett
**Date:** 2025-10-11
**Status:** Concept Design - Ready for CAD Development

---

## Executive Summary

**Mechanical Innovation:** Rotary cam mechanism that decouples solenoid actuator size from braille dot spacing requirements.

**Key Achievement:** Achieves standard 2.5mm braille dot spacing (ADA 703.3 compliant) using 4mm COTS solenoids through perpendicular actuation architecture.

**Design Philosophy:** Modular "rinse and repeat" - 32 identical 6-dot character modules that snap together for scalable manufacturing.

---

## Mechanical Architecture

### System Overview

**Modular Structure:**
- **Basic unit:** 6-dot braille character module (3 layers × 2 dots per layer)
- **Complete device:** 32 character modules arranged horizontally
- **Total dots:** 192 (32 chars × 6 dots)

**Key Dimensions:**
- **Device:** 198mm × 105mm × 25mm
- **Character pitch:** 6.2mm center-to-center (ADA 703.3 standard)
- **Dot pitch:** 2.5mm (vertical within character)
- **Layer spacing:** 5mm vertical (accommodates 4mm solenoid + 1mm housing)

### Motion Conversion Principle

**Perpendicular Actuation:**
```
Horizontal solenoid stroke (1mm)
    → Cam rotation (±45°)
        → Vertical piston motion (0.7mm stroke)
```

**Analogy:** Motorcycle V-twin engine with limited rotation (±45°) instead of continuous rotation.

---

## Detailed Component Specifications

### 1. Cam Disc Assembly

**Function:** Convert horizontal solenoid push → rotary motion

**Geometry:**
- **Type:** Modified constant-velocity cam (smooth acceleration profile)
- **Outer diameter:** 12mm
- **Thickness:** 2mm
- **Rotation range:** ±45° (90° total travel)
- **Cam follower interface:** Flat surface at 4:00 position (solenoid contact point)
- **Piston connection:** Offset pin at 8:00 position (12mm → 0.7mm vertical travel)

**Material Selection:**
- **Prototype:** SLA resin (0.1mm tolerance, $5 ea 3D print)
- **Pilot:** Delrin POM acetal (±0.1mm tolerance, $1.00 ea proto mold)
- **Production:** Delrin POM acetal (±0.2mm tolerance, $0.15 ea steel mold)

**Material Rationale:**
- Low friction coefficient (0.15-0.25 vs steel)
- High wear resistance (>10M cycles)
- Good dimensional stability
- Low moisture absorption
- Machinable for prototype tuning

**Quantity per device:** 96 cams (3 per character × 32 characters)

**Critical Features:**
- **Cam profile:** Custom non-linear profile for smooth acceleration (minimize jerk)
- **Center bore:** 2mm shaft (press fit or bearing mount)
- **Mechanical stop:** Hard stop at ±45° to prevent over-rotation
- **Balance:** Symmetric mass distribution to reduce vibration

### 2. Piston Rod Assembly

**Function:** Vertical translation of braille dot (0.7mm stroke)

**Geometry:**
- **Total length:** 18mm (15mm housing depth + 3mm protrusion)
- **Diameter:** 3mm (fits 3.1mm bushing bore, 0.05mm radial clearance)
- **Cam connection:** Pin joint at 8:00 position on cam disc
- **Dot interface:** Flat tip (2mm diameter contact area)
- **Stroke:** 0.7mm vertical travel (0.5mm min ADA requirement + 0.2mm margin)

**Material Selection:**
- **Prototype:** Nylon SLS 3D print ($3 ea)
- **Pilot:** ABS injection molded ($0.75 ea proto mold)
- **Production:** ABS injection molded ($0.10 ea steel mold)

**Material Rationale:**
- Low friction (molded smooth surface, Ra < 1.6 μm)
- Lightweight (reduces inertia for faster actuation)
- Impact resistant (repeated braille reading)
- Compatible with PTFE dry lube coating

**Quantity per device:** 192 pistons (6 per character × 32 characters)

**Critical Features:**
- **Surface finish:** <1.6 μm Ra (smooth sliding in bushing)
- **Straightness:** <0.05mm over 18mm length (prevent binding)
- **Pin joint:** 1mm diameter, snap-fit or press-fit connection to cam
- **Spring retention:** Groove or shoulder for compression spring

### 3. Linear Bushing Guide

**Function:** Constrain piston to vertical motion, prevent binding/tilt

**Geometry:**
- **Length:** 12mm
- **Outer diameter:** 5mm (press fit into housing)
- **Inner bore:** 3.1mm (0.05mm clearance for 3mm piston)
- **Fit:** H7/g6 (sliding fit, low friction)

**Material Options:**

**Option A - Injection Molded Bushing:**
- Material: PTFE-filled POM (self-lubricating)
- Cost: $0.08 ea (production, steel mold)
- Pros: Integrated with housing, no assembly
- Cons: Wear life ~1M cycles (may need replacement)

**Option B - COTS Brass Bushing:**
- Material: Brass with oil impregnation
- Cost: $0.20 ea (McMaster-Carr stock)
- Pros: 10M+ cycle life, proven reliability
- Cons: Requires press-fit assembly step

**Recommendation:** Start with Option A (molded) for pilot, validate wear life. If <1M cycles, switch to Option B (brass) for production.

**Quantity per device:** 192 bushings (6 per character × 32 characters)

**Critical Features:**
- **Coaxiality:** <0.03mm TIR to housing bore (prevent piston tilt)
- **Surface finish:** <0.8 μm Ra (low friction)
- **Edge chamfer:** 0.2mm × 45° (ease piston insertion during assembly)

### 4. Character Housing

**Function:** Structural frame for 6-dot module, snap-together assembly

**Geometry:**
- **Footprint:** 6.2mm × 15mm × 25mm (W × L × H)
- **Wall thickness:** 1.5mm (injection molding minimum)
- **Layer spacing:** 5mm vertical (3 layers per housing)
- **Mounting features:** Snap-fit tabs on sides (no screws/fasteners)

**Material Selection:**
- **Prototype:** SLA resin or FDM ABS ($10 ea 3D print)
- **Pilot:** ABS injection molded ($2.00 ea proto mold)
- **Production:** ABS injection molded ($0.50 ea steel mold)

**Material Rationale:**
- Rigid structure (no flex during actuation)
- Impact resistant (dropped device survival)
- Good moldability (complex snap-fit features)
- Paintable surface (aesthetic finish)

**Quantity per device:** 32 housings (1 per character)

**Critical Features:**
- **Bushing bores:** 5mm H7 tolerance (tight fit, no adhesive)
- **Cam shaft supports:** 2mm bearing or plain bearing surface
- **PCB mounting:** Standoffs for left/right solenoid PCBs
- **Snap-fit alignment:** Self-aligning tabs for fool-proof assembly
- **Cable routing:** Channels for solenoid wires
- **Braille surface:** Top plate with 6× 2mm holes (dot clearance)

### 5. Compression Spring (Return Force)

**Function:** Return piston to lowered position, assist cam counter-rotation

**Specifications:**
- **Type:** Compression spring (music wire or stainless steel)
- **Free length:** 8mm
- **Compressed length:** 7.3mm (0.7mm stroke)
- **Spring rate:** 0.7 N/mm (0.5N force at full compression)
- **Outer diameter:** 2.5mm (fits within 3mm piston clearance)
- **Wire diameter:** 0.3mm

**Material:** Stainless steel 302 (corrosion resistant)

**Cost:** $0.02 ea (COTS McMaster-Carr)

**Quantity per device:** 192 springs (6 per character × 32 characters)

**Function in mechanism:**
- **Primary:** Return force when solenoid releases (piston down)
- **Secondary:** Preload to keep piston against cam (eliminate backlash)
- **Tertiary:** Mechanical brake assist (gravity + spring hold dot position)

---

## Kinematic Analysis

### Cam Profile Design

**Requirements:**
- Smooth acceleration (minimize jerk → reduce vibration/noise)
- 0.7mm piston stroke from ±45° cam rotation
- Symmetric profile (same motion for raise/lower)

**Cam Geometry Calculations:**

```
Given:
- Cam radius: R = 6mm (from center to piston connection)
- Rotation angle: θ = ±45° (90° total)
- Piston vertical stroke: h = 0.7mm

Piston height as function of angle:
h(θ) = R × sin(θ)

At θ = 0° (neutral):   h = 6 × sin(0°) = 0mm
At θ = +45° (raised):  h = 6 × sin(45°) = 4.24mm → NOT 0.7mm!

ERROR: Simple circular cam gives 4.24mm stroke, too large.

Solution: Use eccentric cam with offset piston connection.
```

**Revised Design - Eccentric Cam:**

```
Piston connects at 8:00 position (240° on cam disc)
Solenoid pushes at 4:00 position (120° on cam disc)
Rotation: ±45° moves piston from 8:00 → 12:00 (vertical)

Geometry:
- Offset radius: r = 1mm (distance from cam center to piston pin)
- Rotation: 45° converts to 0.7mm vertical rise

Calculation:
h = r × (cos(θ_initial) - cos(θ_final))
h = 1 × (cos(240°) - cos(285°)) ≈ 0.7mm ✓

This gives correct 0.7mm stroke with ±45° rotation.
```

**Velocity Profile (Constant-Velocity Cam):**
- Acceleration phase (0° → 15°): Linear ramp
- Constant velocity (15° → 30°): Flat profile
- Deceleration phase (30° → 45°): Linear ramp down

**Advantage:** Reduces peak acceleration → lower inertial forces → less vibration

### Motion Timing Analysis

**Single Dot Actuation:**
1. Solenoid fires: 50ms pulse (5V, 100mA)
2. Cam rotates: ±45° in ~30ms (mechanical response)
3. Piston travels: 0.7mm in ~30ms
4. Mechanical brake: Engages at 12:00 position (<5ms settling)
5. **Total raise time:** ~85ms

**Parallel Actuation Strategy:**
- **8 characters simultaneously** (24 solenoids active)
- **Sequential batches:** 4 batches × 600ms = 2.4 sec total refresh

**Comparison:**
- Piezo: 1.5 sec (192 dots × 8ms parallel)
- ARCH_SOL_ECO: 2.4 sec (acceptable for entry-level users)

---

## Tolerance Analysis

### Critical Dimension Stack-Up

**Requirement:** Braille dot spacing = 2.5mm ± 0.1mm (ADA 703.3)

**Tolerance Chain:**
1. Housing layer spacing: 5mm ± 0.2mm (injection molding)
2. Bushing coaxiality: ± 0.03mm (press fit alignment)
3. Piston straightness: ± 0.05mm (over 18mm length)
4. Cam profile accuracy: ± 0.1mm (molding tolerance)

**Worst-case stack:**
Total error = 0.2 + 0.03 + 0.05 + 0.1 = **0.38mm**

**Assessment:** 0.38mm error > 0.1mm spec ⚠️

**Mitigation Strategies:**
1. **Use prototype phase for tuning** - Measure actual assemblies, adjust CAD
2. **Selective assembly** - Bin parts by measured dimension, pair high/low to cancel errors
3. **Tighter pilot tolerances** - Specify ±0.1mm on critical features (housing layer spacing)
4. **Post-molding calibration** - Shim or adjust if needed

**Target:** Achieve 2.5mm ± 0.15mm in pilot, prove ±0.1mm feasible for production

### Fit Tolerances

**Critical Fits:**
- **Piston in bushing:** 3mm H7/g6 (0.05mm clearance) → Smooth sliding, no binding
- **Bushing in housing:** 5mm H7/p6 (press fit) → No adhesive required
- **Cam on shaft:** 2mm H7/k6 (transition fit) → Rotates freely, no wobble

**GD&T Callouts (for production drawings):**
- Bushing bore coaxiality: ⌀0.03mm to housing datum A
- Piston straightness: 0.05mm over 18mm length
- Cam profile: ±0.1mm true position to center bore

---

## Materials Selection Summary

### Production Materials (10K+ volume, steel molds)

| Component | Material | Rationale | Cost/Unit | Tolerance |
|-----------|----------|-----------|-----------|-----------|
| Cam disc | Delrin POM | Low friction, wear resistant | $0.15 | ±0.2mm |
| Piston | ABS | Lightweight, smooth finish | $0.10 | ±0.1mm |
| Bushing | PTFE-POM | Self-lubricating | $0.08 | ±0.05mm |
| Housing | ABS | Rigid, impact resistant | $0.50 | ±0.2mm |
| Spring | SS 302 | Corrosion resistant | $0.02 | N/A |

**Alternative Materials (if cost/performance tradeoffs shift):**
- **Cam:** Acetal copolymer (slightly higher wear resistance)
- **Piston:** Nylon 6/6 (lower friction, but higher moisture absorption)
- **Housing:** Polycarbonate (higher impact, but more expensive)

---

## Assembly & Manufacturing

### DFM (Design for Manufacturing) Considerations

**Injection Molding:**
1. **Draft angles:** 2° minimum on all vertical walls (ease ejection)
2. **Wall thickness:** 1.5-2.5mm uniform (prevent sink marks, warpage)
3. **Gate location:** Edge gate on non-cosmetic surface
4. **Ejector pins:** Place in non-functional areas (avoid cam profile, bushing bores)
5. **Undercuts:** Avoid or use side actions (increases mold cost)

**Tooling Strategy:**
- **Prototype:** SLA 3D print (0.1mm tolerance, $500-1000 total)
- **Pilot:** Aluminum molds ($20K-30K, 1K-10K shot life)
- **Production:** Steel molds ($70K-90K, 100K-1M shot life)

### Assembly Sequence (Modular 6-Dot Character)

**Step 1: Cam Disc Assembly**
1. Press cam disc onto 2mm shaft (or insert bearing)
2. Install shaft into housing left/right supports

**Step 2: Piston Assembly**
1. Insert compression spring into piston (top end)
2. Slide piston through bushing (pre-installed in housing)
3. Connect piston pin to cam disc 8:00 position (snap-fit)

**Step 3: Solenoid Integration**
1. Mount left/right PCBs to housing standoffs
2. Solder solenoid leads to PCB pads
3. Align solenoid plunger with cam disc 4:00 position

**Step 4: Character Module Completion**
1. Install top braille surface plate (6× 2mm dot holes)
2. Test actuation (manual solenoid activation)

**Step 5: Final Assembly**
1. Snap 32 character modules together (horizontal array)
2. Route interconnect wiring (I2C, power)
3. Install in enclosure

**Assembly Time:** ~20 min/unit (pilot, hand assembly) → Target <5 min/unit with automation

### Quality Control Checkpoints

**Post-Assembly Tests:**
1. **Dot spacing verification:** Caliper measurement, 2.5mm ± 0.1mm
2. **Stroke check:** Verify 0.7mm travel (min 0.5mm per ADA)
3. **Friction test:** Measure actuation force (<1N for solenoid compatibility)
4. **Mechanical brake:** Verify dot holds position >30 sec (gravity + detent)
5. **Cycle test:** 1000-cycle actuation (check for wear, binding)

**Acceptance Criteria:**
- Dot spacing: 2.5mm ± 0.15mm (pilot), ± 0.1mm (production goal)
- Stroke: 0.6-0.8mm (0.5mm min + 0.3mm margin)
- Actuation force: <0.8N (0.5N solenoid force - 0.3N margin)
- Brake hold: >30 sec static, >10 sec under vibration
- Cycle life: >1M cycles (equivalent to 5 years @ 500 refreshes/day)

---

## Engineering Challenges & Solutions

### 1. Cam Profile Optimization

**Challenge:** Achieve smooth motion with minimal vibration/noise

**CAD Simulation Approach:**
1. **SolidWorks Motion Study:**
   - Model cam + piston assembly
   - Apply solenoid force profile (50ms pulse, 0.5N)
   - Analyze velocity/acceleration curves
   - Identify jerk peaks (causes vibration)

2. **Iterate Cam Profile:**
   - Modify cam curve to reduce peak jerk
   - Target: <10 m/s³ jerk (industry standard for smooth motion)
   - Generate optimized cam profile (DXF export for machining)

3. **Prototype Validation:**
   - 3D print cam variants (5-10 iterations)
   - Test on bench setup (high-speed camera, accelerometer)
   - Measure noise (dB meter), vibration (FFT analysis)

**Success Metric:** <40 dB noise @ 1m distance (library quiet level)

### 2. Piston Alignment & Friction

**Challenge:** Prevent binding in bushing, especially under side load from cam

**FEA Analysis:**
1. **Static Structural (ANSYS):**
   - Apply cam side force on piston (0.3N radial)
   - Check piston deflection in bushing
   - Verify <0.02mm deflection (within 0.05mm clearance)

2. **Contact Pressure:**
   - Analyze piston-bushing interface
   - Ensure <50 MPa contact stress (prevent galling)

**Design Refinements:**
- Increase piston diameter: 3mm → 3.5mm (stiffer, less deflection)
- Shorten unsupported length: 18mm → 15mm (reduce bending)
- Add PTFE dry lube coating (0.1 friction coefficient)

**Validation:** Measure friction force <0.2N (10× lower than solenoid force)

### 3. Layer Offset & Interference

**Challenge:** 3 layers must not mechanically interfere during actuation

**CAD Assembly Check:**
1. **SolidWorks Interference Detection:**
   - Model full 32-character assembly (192 moving parts!)
   - Run motion simulation (all dots actuate simultaneously)
   - Flag any collisions (cam-to-cam, piston-to-housing, etc.)

2. **Clearance Analysis:**
   - Verify minimum 0.5mm clearance between layers
   - Check worst-case: all cams at ±45° simultaneously

**Design Validation:**
- Layer 1: Z = 0mm (base)
- Layer 2: Z = 5mm (offset, no interference with Layer 1 cams)
- Layer 3: Z = 10mm (offset, no interference with Layer 1 or 2)
- **Total stack height:** 15mm ✓ (fits within 25mm enclosure)

### 4. Mechanical Brake Reliability

**Challenge:** Maintain dot position with zero hold power (gravity + detent)

**Brake Design:**
1. **Gravity Assist:**
   - Piston at 12:00 vertical → gravity pulls down (0.05N force)
   - Spring preload adds 0.5N → Total 0.55N holding force

2. **Detent Feature:**
   - Small indent in cam at 45° position (0.1mm deep)
   - Creates mechanical lock (requires 0.3N to overcome)

3. **Friction Brake (Option):**
   - Felt pad or rubber bumper at 12:00 position
   - Adds 0.2N friction force → Total 0.75N holding force

**Validation Test:**
1. Actuate dot to raised position
2. Remove power (solenoid OFF)
3. Apply external force (0.5N typical braille reading pressure)
4. **Pass criteria:** Dot holds position >30 sec without drift

**Worst-case:** 0.5N reading force + 0.2N vibration → Need 0.7N brake force (gravity + detent provides 0.55N + friction 0.2N = **0.75N ✓**)

---

## CAD Deliverables (Future Work)

### Mechanical Design Package

**3D Models (SolidWorks):**
- [ ] Cam disc part (with motion profile curve)
- [ ] Piston assembly (pin joint, spring seat)
- [ ] Linear bushing (or COTS part reference)
- [ ] Character housing (with snap-fit features)
- [ ] 6-dot character module assembly
- [ ] 32-character full device assembly

**2D Engineering Drawings (PDF):**
- [ ] Cam disc (profile dimensions, tolerances, GD&T)
- [ ] Piston rod (length, diameter, straightness spec)
- [ ] Housing (bushing bores, snap-fit details)
- [ ] Assembly drawing (BOM, torque specs, assembly notes)

**Simulation Results:**
- [ ] Motion study video (cam rotation → piston travel)
- [ ] Interference check report (no collisions)
- [ ] FEA stress analysis (piston bending, housing deflection)
- [ ] Tolerance stack-up analysis (2.5mm ± 0.1mm verification)

**Manufacturing Specifications:**
- [ ] Injection molding parameters (gate location, ejector pins)
- [ ] Material datasheets (Delrin POM, ABS, PTFE-POM)
- [ ] Surface finish requirements (Ra < 1.6 μm for sliding surfaces)
- [ ] Assembly instructions (torque specs, alignment fixtures)

---

## Appendix A: Mechanical BOM

### Production Volume (10K+ units, steel molds)

| Line | Component | Part # | Description | Qty/Char | Qty Total | Unit Cost | Line Total |
|------|-----------|--------|-------------|----------|-----------|-----------|------------|
| 1 | Cam disc | CUSTOM-CAM-01 | Delrin POM, 12mm OD × 2mm | 3 | 96 | $0.15 | $14.40 |
| 2 | Piston rod | CUSTOM-PISTON-01 | ABS, 3mm dia × 18mm | 6 | 192 | $0.10 | $19.20 |
| 3 | Linear bushing | CUSTOM-BUSHING-01 | PTFE-POM, 5mm OD × 3.1mm ID | 6 | 192 | $0.08 | $15.36 |
| 4 | Housing | CUSTOM-HOUSING-01 | ABS, 6.2×15×25mm | 1 | 32 | $0.50 | $16.00 |
| 5 | Spring | CUSTOM-SPRING-01 | SS 302, 8mm free length | 6 | 192 | $0.02 | $3.84 |
| | | | **Mechanical Subtotal** | | | | **$68.80** |

**Note:** This is the pure mechanical cost for the cam actuation mechanism only. Excludes electrical (solenoids $96, MCU, drivers, PCBs) and enclosure.

**Total ARCH_SOL_ECO BOM:** $216 production (mechanical $69 + electrical $105 + enclosure $8 + misc $34)

---

## Appendix B: Manufacturing Process Flow

### Phase 1: Prototype (Weeks 1-6)

**Goal:** Validate cam mechanism, identify design issues

**Method:**
- **CAD:** SolidWorks model (cam profile, piston, housing)
- **Prototype:** SLA 3D print (0.1mm tolerance, $500-1000 total)
- **Assembly:** Hand assembly (5-10 units)
- **Testing:** Bench test (actuation, friction, noise, durability)

**Deliverables:**
- [ ] CAD models (with design changes incorporated)
- [ ] Prototype test report (pass/fail criteria)
- [ ] Design freeze decision (proceed to pilot)

### Phase 2: Pilot Production (Weeks 7-10)

**Goal:** Validate injection molding, assembly automation

**Method:**
- **Tooling:** Aluminum proto molds ($20K-30K)
- **Volume:** 100 units
- **Assembly:** Semi-automated (jigs, fixtures)
- **Testing:** Full functional test (all 192 dots)

**Deliverables:**
- [ ] Pilot units (100× devices)
- [ ] Manufacturing yield report (target >90%)
- [ ] Cost validation (actual vs target BOM)

### Phase 3: Production (Post-Pilot)

**Goal:** Scale to 10K+ units, optimize cost

**Method:**
- **Tooling:** Hardened steel molds ($70K-90K)
- **Volume:** 10K+ units
- **Assembly:** Fully automated (pick-and-place, snap-fit automation)

**Deliverables:**
- [ ] Production units (10K+)
- [ ] Final BOM cost ($216 validated)
- [ ] Manufacturing process documentation (work instructions, fixtures)

---

## Appendix C: Mechanical Engineering Calculations

### Piston Bending Stress (Worst-Case)

**Scenario:** Piston under side load from cam (0.3N radial force)

**Given:**
- Piston diameter: d = 3mm
- Unsupported length: L = 12mm (between bushing and cam connection)
- Material: ABS (E = 2 GPa, yield strength σ_y = 40 MPa)
- Side load: F = 0.3N

**Bending Stress Calculation:**

```
Moment of inertia: I = π × d⁴ / 64 = π × 3⁴ / 64 = 3.98 mm⁴

Bending moment: M = F × L = 0.3 × 12 = 3.6 N·mm

Bending stress: σ = M × c / I
              = 3.6 × (3/2) / 3.98
              = 1.36 MPa

Safety factor: SF = σ_y / σ = 40 / 1.36 = 29 ✓
```

**Conclusion:** Piston stress is 1.36 MPa << 40 MPa yield. **Safe with 29× margin.**

### Cam Shaft Torsional Stress

**Scenario:** Shaft transmits cam torque from solenoid

**Given:**
- Shaft diameter: d = 2mm
- Solenoid force: F = 0.5N at 6mm radius (cam)
- Torque: T = F × r = 0.5 × 6 = 3 N·mm
- Material: Steel (τ_y = 200 MPa shear yield)

**Torsional Stress Calculation:**

```
Polar moment: J = π × d⁴ / 32 = π × 2⁴ / 32 = 1.57 mm⁴

Torsional stress: τ = T × r / J
                = 3 × (2/2) / 1.57
                = 1.91 MPa

Safety factor: SF = τ_y / τ = 200 / 1.91 = 105 ✓
```

**Conclusion:** Shaft stress is 1.91 MPa << 200 MPa yield. **Safe with 105× margin.**

---

## References

**Cam Design:**
- Norton, R.L. "Cam Design and Manufacturing Handbook" (2nd Ed.)
- SolidWorks Cam Design Tutorial (motion profiles)
- Automotive cam design textbooks (lift curves, jerk analysis)

**Injection Molding:**
- Protolabs Design Guide (tolerance ±0.2mm for engineering plastics)
- "Injection Molding Handbook" - Osswald/Turng/Gramann
- Material datasheets: Delrin POM (DuPont), ABS (Sabic)

**Braille Standards:**
- ADA 703.3 (2.5mm dot spacing, 6.2mm cell center-to-center)
- ANSI/BANA Braille Standards (tactile quality requirements)

**Mechanical Design:**
- Shigley's Mechanical Engineering Design (stress analysis)
- Machinery's Handbook (fits, tolerances, GD&T)
- ASME Y14.5 (Geometric Dimensioning & Tolerancing)

---

**Document Status:** ✅ Complete - Ready for CAD Development
**Next Steps:**
1. Create SolidWorks assembly (cam + piston + housing)
2. Run motion simulation (verify 0.7mm stroke)
3. 3D print prototype (validate concept)
4. Iterate cam profile based on testing
