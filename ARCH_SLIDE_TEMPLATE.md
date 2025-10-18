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

> **TAKEAWAY:** PIEZO_ECO wins on simplicity - standard piezo approach, fastest to pilot.

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

> **TAKEAWAY:** SOL_ECO wins cost via mechanical innovation - 15% actuator savings ($1.70 vs $2.00).

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
