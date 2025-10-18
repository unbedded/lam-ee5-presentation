# Common Subsystems & Design

<style scoped>
table {
  font-size: 16px;
}
</style>

| Subsystem | Function | Key Components | Used In | Design Notes |
|-----------|----------|----------------|---------|--------------|
| **SS-CONTROL** | Main processor + I/O expansion | STM32F407VGT6 (168MHz, 192KB RAM)<br>4× MCP23017 I2C expanders | All 3 | I2C bus for scalability, 140 GPIO available |
| **SS-USER-IO** | Button interface | 2× tactile switches (UP/DOWN) | All 3 | Debounce in firmware, interrupt-driven |
| **SS-PCB** | Main board | 4-layer, ENIG, 200×100mm | All 3 | HV clearances for piezo (100V), EMI routing |
| **SS-ENCLOSURE** | Housing | 3D print (pilot), injection mold (production) | All 3 | Snap-fit assembly, aluminum shielding option |
| **SS-EMI-FILTER** | Bulk + bypass caps | 24× 1000µF bulk, 24× 100nF ceramic | All 3 | Per-driver filtering (NFR-EMI-001 compliance) |
| **SS-ACTUATOR** | Braille pin actuation | **PIEZO:** 192× 2mm piezo (100V)<br>**SOL:** 192× solenoid (12V) + cam | UNIQUE | Custom fabrication, 12-week lead, $2.00 vs $1.70 |
| **SS-ACTUATOR-DRIVER** | High-current switching | **PIEZO:** 24× HV driver (100V)<br>**SOL:** 3× ULN2803A (12V) | UNIQUE | PIEZO needs HV MOSFETs, SOL uses std logic |
| **SS-COMM** | Host connectivity | **USB:** USB4105-GF-A receptacle<br>**BLE:** nRF52840 module | UNIQUE | DLX only has BLE, ECO variants use USB-C |
| **SS-POWER** | Voltage regulation | **USB:** LDO 5V→3.3V + boost 5V→100V<br>**LIION:** Charger + gauge + boost | UNIQUE | DLX has Li-ion + charger, ECO variants USB-powered |

**Key Design Decisions:**
- **Modular subsystems** enable architecture variants without full redesign
- **Common control** (STM32 + I2C expanders) simplifies firmware reuse
- **Actuator + Power + Comm** are the 3 differentiators driving cost/performance trade-offs

> **TAKEAWAY:** Shared subsystems (60% of design) enable rapid variants - only actuator/power/comm change.

<!-- Speaker notes: "This is modular systems engineering. Control, user IO, PCB, enclosure, EMI filtering are 100% shared across all 3 architectures - that's 60% of the design. Only 3 subsystems vary: actuators (piezo vs solenoid), drivers (HV vs low-voltage), power (USB vs Li-ion), and comm (USB vs BLE). This modularity lets us generate 3 architectures from one base design - reducing NRE and accelerating time-to-market. STM32F407 chosen for 140 GPIO (enough for direct-drive if needed) and I2C master for expanders. 4-layer PCB required for HV clearances (100V piezo) even though SOL_ECO only needs 12V - we design for worst-case. EMI filtering per NFR-EMI-001: bulk caps for inductive kickback, ceramic bypass for high-freq. This table shows what I'd hand to a junior EE to implement - subsystem boundaries, key ICs, design constraints." -->
