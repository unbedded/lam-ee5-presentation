# Power Requirements - Actuation Strategy

<style scoped>
table {
  font-size: 17px;
}
</style>

## Holding Force vs Transient Switching

| Actuator Type | Hold Power | Transient Power (per dot) | Sequencing Strategy | Total Avg Power |
|---------------|------------|---------------------------|---------------------|-----------------|
| **Piezo** | **~0W** (capacitive) | 30V × 5mA × 10ms pulse | 24-way parallel (8 channels) | **2.16W** |
| **Solenoid** | **~0W** (bistable latch) | 12V × 500mA × 50ms pulse | 8-way parallel (2 channels) | **1.53W** |

**Key Insight:** Sequencing strategy reduces peak current AND EMI by spreading actuation over time

---

## Power Budget Breakdown by Architecture

| Subsystem | PIEZO_ECO | PIEZO_DLX | SOL_ECO |
|-----------|-----------|-----------|---------|
| **Actuators** (pulsed) | 0.60W (24 dots/sec avg) | 0.60W | 0.82W (8-way parallel) |
| **Drivers** | 0.15W (24× HV driver) | 0.15W | 0.18W (3× ULN2803A) |
| **Control + I/O** | 0.36W (STM32 + I2C) | 0.36W | 0.20W |
| **Boost Converter** | 1.00W (5V→100V, 85% η) | 1.00W (3.7V→100V) | 0.25W (5V→12V, 85% η) |
| **Communication** | 0.05W (USB-C) | 0.05W (BLE nRF52840) | 0.05W (USB-C) |
| **TOTAL** | **2.16W** | **2.16W** | **1.53W** |

---

## Power Source Capability

<style scoped>
table {
  font-size: 16px;
}
.pass { color: #27ae60; font-weight: bold; }
.fail { color: #e74c3c; font-weight: bold; }
</style>

| Power Source | Voltage | Capacity | Continuous Power | PIEZO (2.16W) | SOL (1.53W) |
|--------------|---------|----------|------------------|---------------|-------------|
| **USB-C** (bus-powered) | 5V | 500mA max | **2.5W** | <span class="pass">✓ 86% util</span> | <span class="pass">✓ 61% util</span> |
| **Li-ion 18650** | 3.7V nominal | 2500mAh (9.25Wh) | **3.7W** (2 hrs) | <span class="pass">✓ 58% util (4.3 hrs)</span> | <span class="pass">✓ 41% util (6 hrs)</span> |

**USB-C Android Phone Connection:**
- Phone battery: 3000mAh @ 3.7V = 11.1Wh
- **PIEZO drain:** 11.1Wh ÷ 2.16W = **5.1 hours** (drains phone battery)
- **SOL drain:** 11.1Wh ÷ 1.53W = **7.3 hours** (better for phone-powered use)

> **TAKEAWAY:** Sequencing reduces peak current from 192→24 dots (PIEZO) or 192→8 dots (SOL), enabling USB/battery power.

<!-- Speaker notes: "This is where systems engineering meets power electronics. Key insight: We can't actuate all 192 dots simultaneously - peak current would be 96A (192 × 500mA solenoids) or 10A (192 × 50mA piezos). Sequential actuation solves TWO problems: (1) Reduces peak current to fit USB/battery budget, (2) Reduces EMI by 28dB (fewer simultaneous radiating sources). PIEZO uses 24-way parallel (8 channels of 24 dots each) because it's faster (1.5s refresh) but needs 100V HV supply. SOL uses 8-way parallel (2 channels) to stay within power budget, slower refresh (2.4s) but only 12V supply. Both have zero hold power - piezo is capacitive (no DC current), solenoid has bistable latch (mechanical brake). Power breakdown: PIEZO 2.16W mostly from boost converter (5V→100V at 85% efficiency = 1W loss), SOL 1.53W mostly from actuator pulses. USB-C provides 2.5W (500mA @ 5V), Li-ion 18650 provides 3.7W average for 2 hours. Android phone connection: PIEZO drains phone in 5 hours, SOL in 7 hours - users must manage phone battery or use wall power. Trade-off: PIEZO is faster (1.5s refresh), SOL is lower power (1.53W vs 2.16W) and cheaper (12V vs 100V drivers)." -->
