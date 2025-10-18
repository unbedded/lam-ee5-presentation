# Common Subsystems - Shared Design Foundation

<style scoped>
table {
  font-size: 18px;
}
</style>

| Subsystem | Key Components | Function | Design Notes |
|-----------|----------------|----------|--------------|
| **SS-CONTROL** | STM32F407VGT6 (168MHz, 192KB RAM) | Main processor | 140 GPIO available, built-in USB PHY |
| **SS-IO-EXPAND** | 4× MCP23017 I2C expanders (16-bit each) | GPIO expansion | I2C bus for scalability, interrupt support |
| **SS-USER-IO** | 2× tactile switches (UP/DOWN) | User navigation | Debounce in firmware, interrupt-driven |
| **SS-PCB** | 4-layer, ENIG, 200×100mm | Main board | HV clearances, EMI routing, power planes |
| **SS-ENCLOSURE** | 3D print (pilot) → injection mold (prod) | Housing | Snap-fit assembly, optional Al shield |
| **SS-EMI-FILTER** | 24× 1000µF bulk + 24× 100nF ceramic | EMI compliance | Per-driver filtering (NFR-EMI-001) |

**Modular Design Strategy:**
- **60% of design is shared** - Control, I/O, PCB, enclosure, EMI filtering identical across all 3 architectures
- **40% varies** - Only actuators, power, and communication differ between architectures
- **Benefits:** Reduces NRE, accelerates variants, simplifies firmware reuse

> **TAKEAWAY:** Shared subsystems enable rapid architecture variants - only actuator/power/comm change.

<!-- Speaker notes: "This is modular systems engineering. 60% of the design - control, user IO, PCB, enclosure, EMI filtering - is 100% shared across all architectures. STM32F407 chosen for 140 GPIO (enough for direct-drive fallback), 168MHz performance, and built-in USB PHY. 4 MCP23017 I2C expanders give us 64 additional GPIO (total 140+64=204 available vs 192 needed). 4-layer PCB required for HV clearances even though SOL_ECO only needs 12V - we design for worst-case across all variants. EMI filtering per NFR-EMI-001: 1000µF bulk caps absorb inductive kickback, 100nF ceramic bypass for high-frequency suppression. This modularity means if we change from piezo to solenoid actuators, we only redesign 3 subsystems instead of starting from scratch - that's the value of architecture planning." -->

---
