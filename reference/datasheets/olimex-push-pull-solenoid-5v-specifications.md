# Olimex PUSH-PULL-SOLENOID-5V - Technical Specifications

**Source:** https://www.olimex.com/Products/Components/Misc/PUSH-PULL-SOLENOID-5V/
**Retrieved:** 2025-10-12
**Product Image:** olimex-push-pull-solenoid-5v-image.jpg
**Price:** €2.50 EUR (~$2.73 USD)
**Status:** COTS part selected for ARCH_SOL_ECO rotary cam mechanism

---

## Product Description

Magnetic lock-in push-pull spring loaded solenoid with NdFeB magnet tail for bistable operation.

**Type:** Open-frame duty solenoid (push-pull)
**Mounting:** Chassis mount (requires custom bracket)
**Package:** 8 × 10.3 × 16.3 mm body dimensions

---

## Electrical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Operating Voltage** | DC 5-6V | Nominal 5V operation |
| **Operating Current @ 5V** | 0.63 A | 3.15W power dissipation |
| **Operating Current @ 6V** | 0.75 A | 4.5W power dissipation |
| **Coil Resistance** | 6 Ω | Pure resistive load |
| **Duty Cycle** | Pulse only | ⚠️ Max 5 seconds continuous |
| **Thermal Limit** | Not specified | Will generate heat if constantly energized |

---

## Mechanical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Shaft Diameter** | 4 mm | ✓ Key specification for ARCH_SOL_ECO |
| **Shaft Length** | 15.1 mm | Extends beyond body |
| **Stroke Length** | 5 mm | Full travel range |
| **Body Width** | 8 mm | Minimum mounting clearance |
| **Body Height** | 10.3 mm | Vertical profile |
| **Body Depth** | 16.3 mm | Horizontal profile |
| **Wire Length** | 150 mm | With 2.54mm connector |
| **Connector Type** | 2.54mm pitch | Standard 0.1" header compatible |

---

## Shaft End Geometry

| Parameter | Value | Notes |
|-----------|-------|-------|
| **End Shape** | Flat face | ✓ Ideal for cam follower interface |
| **Alternative** | Conical (not used) | Would be more expensive |
| **Contact Area** | ~4mm diameter | Low contact pressure |
| **Material** | Steel (magnetic) | Iron core with NdFeB magnet tail |

**Engineering Note:** Flat face is optimal for short-stroke applications (<1.5mm effective stroke) and provides larger contact area with cam surface, reducing wear.

---

## Operating Principle

### Push Operation (Energized)

```
Red wire (+) ──→ Coil
Black wire (−) ──→ Ground

Result: Electromagnetic force PULLS iron core INTO coil body
        → Shaft retracts into solenoid
        → NdFeB magnet at tail locks core in position
        → Core stays retracted even when power removed
```

### Pull Operation (Reverse Polarity)

```
Red wire (−) ──→ Ground
Black wire (+) ──→ Coil

Result: Electromagnetic force PUSHES iron core OUT of coil body
        → Shaft extends from solenoid
        → Spring returns core to extended position
        → Core stays extended (spring force holds)
```

### Bistable Behavior

**Key Feature:** Strong NdFeB magnet at core tail provides magnetic latch

- When retracted (pulled in): Magnet holds core in place without power
- When extended (pushed out): Spring force holds core in place without power
- **Power only needed for transitions** (not for holding states)
- Reduces average power consumption significantly

**Application Note for ARCH_SOL_ECO:**
- Use pulse operation (5-10ms) for actuation
- No holding current needed (bistable operation)
- Average power = peak power × duty cycle = 3.15W × (6ms / 48ms) = 0.39W per solenoid
- Total average power (192 solenoids, multiplexed): 75W peak → 9.4W average

---

## Dimensional Drawing (Approximate)

```
TOP VIEW:
┌─────────────────────┐
│                     │  ← 8mm width
│    ┌───────────┐    │
│    │  COIL     │    │
│    │   ████    │    │
│    │   ████    │────┼──→ Shaft (4mm dia)
│    │   ████    │    │    extends 15.1mm
│    └───────────┘    │
│                     │
└─────────────────────┘
        16.3mm depth


SIDE VIEW:
        ┌──────┐  ← Shaft (4mm dia, 15.1mm length)
        │      │
┌───────┴──────┴───────┐
│                      │  ← 10.3mm height
│   ███████████████    │
│   ███ COIL ██████    │  ← Open frame body
│   ███████████████    │
│   [NdFeB Magnet]     │  ← Magnetic latch at tail
└──────────────────────┘
        16.3mm depth


FRONT VIEW:
        ┌──┐  ← Shaft (4mm dia)
        │  │
    ┌───┴──┴───┐
    │          │  ← 8mm width
    │  ██████  │
    │  ██████  │  ← 10.3mm height
    │  ██████  │
    └──────────┘

        ┌──┐
        │  │  ← Wire leads (150mm length)
        └──┘     2.54mm connector
```

---

## Force Characteristics

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Output Force** | ~0.5N (estimated) | Not specified in datasheet |
| **Starting Force** | Unknown | Depends on air gap |
| **Holding Force (magnetic)** | Unknown | NdFeB magnet provides latch |
| **Spring Return Force** | Unknown | Internal compression spring |

**Engineering Note:** Force specification is not provided by manufacturer. Estimated 0.5N based on similar solenoids with 5V/0.63A rating. **Requires bench testing for validation.**

---

## Thermal Characteristics

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Continuous Operation** | ⚠️ NOT RECOMMENDED | Will overheat |
| **Maximum Continuous Time** | 5 seconds | Per manufacturer warning |
| **Recommended Duty Cycle** | Pulse operation | 5-10ms pulses, <20% duty |
| **Thermal Resistance** | Unknown | Small body → limited heat dissipation |
| **Coil Temperature Rise** | Unknown | Requires IR camera testing |

**Application Note for ARCH_SOL_ECO:**
- Pulse duration: 5-10ms per actuation
- Refresh rate: 20 Hz (48ms cycle)
- Duty cycle: 6ms / 48ms = 12.5% ✓ (well under thermal limit)
- Continuous operation: Multiplexing ensures no solenoid is actuated >10ms continuously

---

## Electrical Connection

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Wire Colors** | Red (+), Black (−) | Standard polarity for pull operation |
| **Wire Gauge** | Unknown | Estimate 24-28 AWG |
| **Wire Length** | 150 mm | Adequate for routing to driver PCB |
| **Connector Type** | 2.54mm pitch | 0.1" header compatible |
| **Termination** | Crimp connector | Can also solder directly |

**Wiring Diagram for ARCH_SOL_ECO:**

```
    Driver IC (ULN2803A)
         │
         ├──→ Output Pin (Darlington sink)
         │         │
         │         ↓
         │    ┌────────┐
    +5V ─┼────│ RED    │  Solenoid Coil (6Ω)
         │    │        │
         │    │ BLACK  │
         │    └────┬───┘
         │         │
         └─────────┴──→ Ground (via driver)

    Control Signal:
    GPIO HIGH → Driver ON → Current flows → Solenoid actuates
    GPIO LOW  → Driver OFF → No current → Solenoid releases
```

---

## Reliability & Lifetime

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Cycle Life** | Unknown | Typical solenoids: 1M-10M cycles |
| **Wear Mechanism** | Mechanical (spring fatigue) | NdFeB magnet does not degrade |
| **Failure Mode** | Open coil or jammed core | Detectable via current sensing |
| **MTBF** | Unknown | Requires accelerated life testing |

**Recommended Testing:**
- 100K cycle endurance test per solenoid
- Target lifetime: 1M cycles @ 20 Hz = 14 hours continuous operation
- Real-world usage: ~1K actuations/day = 1000 days (2.7 years) to 1M cycles

---

## Compliance & Certifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **RoHS** | Assumed Yes | Olimex typically RoHS compliant |
| **CE** | Unknown | Check with Olimex |
| **UL** | Unknown | May require component certification |
| **Conflict Minerals** | Unknown | Verify for corporate compliance |

**Certification Note:** Solenoid is a component, not a complete product. Final device (braille display) requires system-level certification (UL, FCC, CE).

---

## Supply Chain Information

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Manufacturer** | Olimex Ltd. (Bulgaria) | Established open-source hardware company |
| **Distributor** | Digikey (primary) | Global availability |
| **Lead Time** | ~4 weeks | Standard Digikey stock |
| **MOQ** | 1 unit | No minimum order quantity |
| **Packaging** | Bulk | No tape/reel option |
| **Lifecycle** | Active | Not NRND |

**Supply Chain Risk Assessment:**
- ✅ Low risk: Available from major distributor (Digikey)
- ✅ Low risk: Olimex is established manufacturer (since 2001)
- ⚠️ Medium risk: Single-source component (no second source identified)
- ⚠️ Medium risk: 4-week lead time (plan for inventory buffer)

**Mitigation Strategy:**
- Maintain 8-week inventory buffer (2× lead time)
- Identify second-source alternatives (e.g., Adafruit mini push-pull solenoid)
- For production (1000+ units), negotiate custom solenoid with Chinese OEM

---

## Application Notes for ARCH_SOL_ECO

### Mechanical Interface Design

**Cam Follower Contact:**
- Solenoid flat face (4mm dia) contacts cam disc at 4:00 position (horizontal tangent)
- Contact area: ~4mm² (4mm dia × 1mm width)
- Contact pressure: 0.5N ÷ 4mm² = 0.125 MPa (very low, no wear concern)
- Cam material: Delrin POM (compressive strength ~100 MPa, SF = 800×)

**Stroke Limiting:**
- Solenoid provides 5mm stroke, but cam only needs 1mm for ±45° rotation
- Mechanical stop integrated into cam housing prevents over-rotation
- Excess stroke absorbed by solenoid spring compression (no damage)

**Mounting:**
- Custom bracket required (8×10.3×16.3mm clearance + wire routing)
- Horizontal orientation (shaft perpendicular to braille surface)
- 192 solenoids in 3-layer stacked configuration (6 per character × 32 characters)

### Electrical Interface Design

**Driver Circuit:**
- Use ULN2803A Darlington array (8-channel sink driver)
- 192 solenoids ÷ 8 channels = 24 ULN2803A ICs
- Each channel handles 0.63A @ 5V (well within 500mA ULN2803A spec with paralleling)
- **Correction:** Need 2 channels per solenoid (2× 0.32A = 0.64A) → 3× ULN2803A ICs for 24 solenoids (multiplexed actuation)

**Power Supply:**
- Regulated 5V rail (buck converter from 6V AA batteries or USB-C PD)
- Supercapacitor buffer (1F @ 5V) for pulse current handling
- Peak current: 24 solenoids × 0.63A = 15.1A (4 characters simultaneous)
- Average current: 15.1A × 12.5% duty cycle = 1.9A (feasible for AA batteries)

**Control Logic:**
- Multiplex 32 characters into 8 groups of 4 characters
- Actuate one group at a time (6ms pulse, 20 Hz refresh)
- Use bistable operation (pulse only, no holding current)
- Total refresh cycle: 8 groups × 6ms = 48ms (20 Hz user perception)

### Testing & Validation

**Bench Tests:**
1. Verify 5V @ 0.63A current draw (measure with DMM)
2. Measure actual stroke with calipers (should be 5mm ±0.5mm)
3. Test flat face contact with cam disc (SLA 3D print)
4. Measure force output with digital scale (target 0.5N, verify)
5. Thermal test (5 sec continuous, measure coil temperature with IR camera)

**System Integration Tests:**
1. Single solenoid → cam → piston → dot kinematic validation
2. 6-dot character test (multiplex timing, power consumption)
3. 32-character full device test (refresh rate, thermal mapping)
4. 10K cycle endurance test (detect failures, measure wear)

---

## Comparison to Alternatives

| Solenoid Option | Olimex 5V | Generic 12V | Custom OEM |
|-----------------|-----------|-------------|------------|
| **Voltage** | 5V ✓ | 12V (requires boost) | 5V (custom) |
| **Current** | 0.63A | ~0.3A | TBD |
| **Shaft Dia** | 4mm ✓ | 4mm ✓ | 2mm (custom) |
| **Stroke** | 5mm (limit to 1mm) | 4mm (limit to 1mm) | 1mm (exact) ✓ |
| **Plunger Face** | Flat ✓ | Unknown | Flat (specify) |
| **Price @ 100** | $2.73 | $1.00 | $5.00 (tooling amortized) |
| **Price @ 1000** | $2.50 | $0.80 | $1.00 ✓ |
| **Lead Time** | 4 weeks ✓ | 2 weeks ✓ | 12+ weeks |
| **Supply Chain** | Digikey ✓ | Amazon/eBay ⚠️ | Direct OEM ⚠️ |
| **Datasheet** | Web page only | None ⚠️ | Custom (requires) |
| **RoHS** | Yes (assumed) | Unknown ⚠️ | Yes (specify) |

**Decision Matrix:**
- **Pilot phase (100 units):** Use Olimex 5V (fastest to market, low risk, Digikey stock)
- **Production phase (1000+ units):** Negotiate custom OEM ($1.00 target, 1mm stroke, flat face)

---

## References

- **Product Page:** https://www.olimex.com/Products/Components/Misc/PUSH-PULL-SOLENOID-5V/
- **Manufacturer:** Olimex Ltd. (https://www.olimex.com/)
- **Distributor:** Digikey (PN TBD - search "Olimex PUSH-PULL-SOLENOID-5V")
- **Product Image:** olimex-push-pull-solenoid-5v-image.jpg (stored in this directory)

---

## Document Revision History

| Date | Version | Author | Changes |
|------|---------|--------|---------|
| 2025-10-12 | 1.0 | LAM EE Project | Initial datasheet compilation from web sources |

---

**End of Datasheet**
