# Braille Display - Solution Architectures
**Generated:** 2025-10-15
**Source:** source/architectures.yaml v2.0.0

## Executive Summary

This document presents 3 alternative architectures for a 32-character braille display device:

- **Piezo Economy (Wired) (ARCH_PIEZO_ECO):** Entry-level / Education / Desktop / Low-cost Piezo - Target BOM $125
- **Solenoid Economy (Rotary Cam) (ARCH_SOL_ECO):** Economy / Budget-Conscious / Best Cost-Performance / Standard Braille Spacing - Target BOM $165
- **Piezo Deluxe (Wireless) (ARCH_PIEZO_DLX):** Premium / Mobile Professional / Sleek Design / Rechargeable - Target BOM $225

## Architecture Overview

| Architecture | Nickname | Market Position | BOM Target | BOM Actual | Timeline |
|--------------|----------|-----------------|------------|------------|----------|
| ARCH_PIEZO_ECO | Value Desk | Entry-level | $125 | $415.35 | 6 weeks |
| ARCH_SOL_ECO | Cam Innovation | Economy | $165 | $240.75 | 10 weeks |
| ARCH_PIEZO_DLX | Premium Pro | Premium | $225 | $436.51 | 8 weeks |

---

## ARCH_PIEZO_ECO: Piezo Economy (Wired) - "Value Desk"

### Market Position

Entry-level / Education / Desktop / Low-cost Piezo

### Requirements Traceability

- **PRD-IFACE-001-ASMP:** Scenario B (USB-C wired): Tethered, no battery, $100-150 BOM
- **PRD-COST-001-ASMP:** Low-end BOM target ($100-150)
- **PRD-SCHED-001-ASMP:** Fastest to pilot (simplest design)

### Subsystem Breakdown

**Core Subsystems (Shared):**

- **SS-ACTUATOR:** Braille Actuator Array → TBD-PIEZO-01 (TBD TBD-PIEZO-2MM)
  - 192 bimorph piezo dots (32 cells × 6 dots/cell), 100-200VDC drive, CAPACITIVE LOAD
  - Qty: 1 × 192 = 192
- **SS-CONTROL:** Main Control Unit (MCU) → 497-14367-ND (STMicro STM32F407VGT6)
  - Microcontroller for actuator control + text processing
  - Qty: 1 × 1 = 1
- **SS-IO-EXPAND:** I/O Expander Array → MCP23017-E/SP-ND (Microchip MCP23017-E/SP)
  - GPIO expansion (STM32 140 GPIO → 192 total needed)
  - Qty: 1 × 4 = 4
- **SS-ACTUATOR-DRIVER:** Actuator High-Voltage Driver Array → TBD-HV-DRIVER (TBD TBD-HV-DRV-200V)
  - 200V drivers for piezo actuators (CAPACITIVE LOAD)
  - Qty: 1 × 24 = 24
- **SS-USER-IO:** User Interface Buttons → CKN12221-ND (C&K KMR221NGLFS)
  - 2× tactile buttons (UP/DOWN navigation)
  - Qty: 1 × 2 = 2
- **SS-PCB:** Main PCB (4-layer) → CUSTOM-PCB-01 (PCBWay PCB-4L-200x100)
  - 200mm × 100mm board for all electronics
  - Qty: 1 × 1 = 1
- **SS-ENCLOSURE:** Mechanical Enclosure → CUSTOM-ENCL-01 (Shapeways 3DP-SLS-NYLON)
  - Housing + braille dot surface
  - Qty: 1 × 1 = 1
- **SS-EMI-BULK-CAP:** EMI Bulk Capacitor Array → 493-2203-ND (Nichicon UVR1H102MHD)
  - 1000µF electrolytic capacitors for driver IC power rail filtering
  - Qty: 1 × 24 = 24
- **SS-EMI-BYPASS-CAP:** EMI Bypass Capacitor Array → 399-4151-1-ND (Kemet C0805C104K5RACTU)
  - 100nF ceramic capacitors for high-frequency EMI suppression
  - Qty: 1 × 24 = 24

**Unique Subsystems (Architecture-Specific):**

- **SS-COMM-USB:** USB-C Communication Interface → 2073-USB4105-GF-A-ND (GCT USB4105-GF-A)
  - USB-C connector for wired connection
  - Qty: 1 × 1
- **SS-POWER-USB-LDO:** USB Power - LDO (5V→3.3V) → 296-38833-1-ND (TI TPS73633)
  - Logic power from USB
  - Qty: 1 × 1
- **SS-POWER-USB-BOOST:** USB Power - Boost (5V→200V) → TBD-HV-BOOST (TBD TBD-BOOST-200V)
  - Actuator HV power from USB (200V for bimorph piezo)
  - Qty: 1 × 1

### Qualitative Assessment

**Cost Profile:**

- Bom: 💚 LOW
- Certification: 💚 LOW
- Nre: 💚 LOW

**User Experience:**

- Setup: 💚 BEST
- Convenience: 🟠 FAIR
- Reliability: 💚 BEST
- Battery Anxiety: 💚 NONE
- Mobility: 🔴 POOR

**Complexity:**

- Hardware: 🔴 COMPLEX
- Firmware: 💚 SIMPLE
- Power: 🔴 COMPLEX
- Mechanical: 💚 SIMPLE

**Timeline:**

- Pilot: 💚 FASTEST
- Parts Leadtime: 💚 SHORT
- Certification: 💚 FAST

**Manufacturing:**

- Assembly: 💚 SIMPLE
- Component Count: 💚 LOW
- Dfm: 💚 EXCELLENT
- Yield Risk: 💚 LOW

**Risk:**

- Technical: 🔴 HIGH
- Supply Chain: 💚 LOW
- Safety: 🟡 MEDIUM
- Timeline: 🟡 MEDIUM
- Cost Overrun: 🟡 MEDIUM

**Market Fit:**

- Education: 💚 EXCELLENT
- Consumer: 🟠 FAIR
- Professional: 🔴 POOR
- Accessibility Ngos: 💚 EXCELLENT
- Global: 💚 EXCELLENT

### Quantitative Metrics

**Cost:**

- BOM Subtotal: $361.17
- Misc 15%: $54.18
- **BOM Total: $415.35** (Target: $125, Range: $100-$150)
- **Cost Gap: $290.35 (232% over target)** ⚠️
- Certification: $20,000
- NRE Total: $35,000

**Size & Weight:**

- Dimensions: 200×100×15 mm (7.9×3.9×0.6 in)
- Weight: 0.79 lbs (360g)

**Performance:**

- Refresh Speed: 1.5 seconds
- Battery Life: N/A (bus-powered)
- Power Consumption: 2.5 watts

**Timeline:**

- Design: 2 weeks | Prototype: 2 weeks | Pilot: 2 weeks
- **Total: 6 weeks** | Certification: 4 weeks

**Manufacturing:**

- Component Count: 250
- Assembly Time: 15 min/unit
- Yield Estimate: 98%

---

## ARCH_SOL_ECO: Solenoid Economy (Rotary Cam) - "Cam Innovation"

### Market Position

Economy / Budget-Conscious / Best Cost-Performance / Standard Braille Spacing

### Requirements Traceability

- **PRD-SCHED-002-ASMP:** COTS mandate (≤4 week lead time) → Use COTS solenoid (Takaha BS-0420N-01)
- **PRD-POWER-004-ASMP:** AA battery life (8 hours) → Solenoid+cam = 1.53W (marginal fit)
- **PRD-COST-001-ASMP:** Lowest BOM target ($165-216) via actuator cost savings (solenoid $96 vs piezo $288)
- **PRD-FUNC-001:** Standard 2.5mm braille spacing (ADA 703.3) - preserves muscle memory

### Subsystem Breakdown

**Core Subsystems (Shared):**

- **SS-ACTUATOR-SOLENOID:** Solenoid Actuator Array (COTS) → CUSTOM-SOL-01 (Custom OEM SOL-4MM-1MM-5V-FLAT)
  - 192× COTS solenoids for rotary cam actuation, 4mm diameter
  - Qty: 1 × 192 = 192
- **SS-ACTUATOR-CAM:** Rotary Cam Disc Array → CUSTOM-CAM-01 (Custom CAM-DISC-STEEL)
  - Cam discs for converting horizontal solenoid motion → vertical piston motion
  - Qty: 1 × 96 = 96
- **SS-ACTUATOR-PISTON:** Piston Rod Array → CUSTOM-PISTON-01 (Custom PISTON-ROD-STEEL)
  - Vertical piston rods for braille dot actuation
  - Qty: 1 × 192 = 192
- **SS-ACTUATOR-BUSHING:** Linear Bushing Array → CUSTOM-BUSHING-01 (Custom BUSHING-STEEL)
  - Linear bushings for piston alignment
  - Qty: 1 × 192 = 192
- **SS-ACTUATOR-CAM-HOUSING:** Cam Housing Array → CUSTOM-HOUSING-01 (Custom HOUSING-STEEL)
  - Housing for cam mechanism assembly
  - Qty: 1 × 32 = 32
- **SS-ACTUATOR-SPRING:** Compression Spring Array → CUSTOM-SPRING-01 (Custom SPRING-COMP-01)
  - Return springs for piston retraction
  - Qty: 1 × 192 = 192
- **SS-CONTROL:** Main Control Unit (MCU) → 497-14367-ND (STMicro STM32F407VGT6)
  - Microcontroller for actuator control + text processing
  - Qty: 1 × 1 = 1
- **SS-IO-EXPAND:** I/O Expander Array → MCP23017-E/SP-ND (Microchip MCP23017-E/SP)
  - GPIO expansion (STM32 140 GPIO → 192 total needed)
  - Qty: 1 × 4 = 4
- **SS-ACTUATOR-DRIVER-2CH:** Actuator Driver Array (2-channel) → 296-1781-5-ND (TI ULN2803A)
  - 12V drivers for solenoid actuators (2 channels vs 8 channels)
  - Qty: 1 × 3 = 3
- **SS-USER-IO:** User Interface Buttons → CKN12221-ND (C&K KMR221NGLFS)
  - 2× tactile buttons (UP/DOWN navigation)
  - Qty: 1 × 2 = 2
- **SS-PCB:** Main PCB (4-layer) → CUSTOM-PCB-01 (PCBWay PCB-4L-200x100)
  - 200mm × 100mm board for all electronics
  - Qty: 1 × 1 = 1
- **SS-ENCLOSURE:** Mechanical Enclosure → CUSTOM-ENCL-01 (Shapeways 3DP-SLS-NYLON)
  - Housing + braille dot surface
  - Qty: 1 × 1 = 1
- **SS-EMI-BULK-CAP:** EMI Bulk Capacitor Array → 493-2203-ND (Nichicon UVR1H102MHD)
  - 1000µF electrolytic capacitors for driver IC power rail filtering
  - Qty: 1 × 24 = 24
- **SS-EMI-BYPASS-CAP:** EMI Bypass Capacitor Array → 399-4151-1-ND (Kemet C0805C104K5RACTU)
  - 100nF ceramic capacitors for high-frequency EMI suppression
  - Qty: 1 × 24 = 24

**Unique Subsystems (Architecture-Specific):**

- **SS-COMM-USB:** USB-C Communication Interface → 2073-USB4105-GF-A-ND (GCT USB4105-GF-A)
  - USB-C connector for wired connection
  - Qty: 1 × 1
- **SS-POWER-AA-HOLDER:** AA Battery Holder (4×AA) → 36-2466K-ND (Keystone 2466)
  - Battery holder for 4× AA alkaline
  - Qty: 1 × 1
- **SS-POWER-AA-BOOST-3V3:** AA Power - Boost (6V→3.3V) → 296-50464-1-ND (TI TPS61088)
  - Logic power from AA batteries
  - Qty: 1 × 1
- **SS-POWER-AA-BOOST-12V:** AA Power - Boost (6V→12V) → 296-50464-1-ND (TI TPS61088)
  - Actuator power from AA (12V for solenoid overdrive)
  - Qty: 1 × 1

### Qualitative Assessment

**Cost Profile:**

- Bom: 💚 LOW
- Certification: 🟡 MEDIUM
- Nre: 🟠 MEDIUM-HIGH

**User Experience:**

- Setup: 💚 BEST
- Convenience: 🟡 GOOD
- Reliability: 💚 BEST
- Battery Anxiety: 💚 NONE
- Mobility: 🟠 FAIR
- Refresh Speed: ACCEPTABLE

**Complexity:**

- Hardware: 🟡 MODERATE
- Firmware: 💚 SIMPLE
- Power: 🟡 MODERATE
- Mechanical: 🔴 COMPLEX

**Timeline:**

- Pilot: 💚 FAST
- Parts Leadtime: SHORTEST
- Certification: 💚 FAST

**Manufacturing:**

- Assembly: 🟡 MODERATE
- Component Count: 🟡 MEDIUM
- Dfm: 💚 EXCELLENT
- Yield Risk: 🟡 MEDIUM

**Risk:**

- Technical: 💚 LOW
- Supply Chain: LOWEST
- Safety: 💚 LOW
- Timeline: 💚 LOW
- Cost Overrun: LOWEST

**Market Fit:**

- Education: 💚 EXCELLENT
- Consumer: 💚 EXCELLENT
- Professional: 🟡 GOOD
- Accessibility Ngos: 💚 EXCELLENT
- Global: 💚 EXCELLENT

### Quantitative Metrics

**Cost:**

- BOM Subtotal: $209.35
- Misc 15%: $31.40
- **BOM Total: $240.75** (Target: $165, Range: $150-$180)
- **Cost Gap: $75.75 (46% over target)** ⚠️
- Certification: $20,000
- NRE Total: $70,000

**Size & Weight:**

- Dimensions: 198×105×25 mm (7.8×4.1×1.0 in)
- Weight: 1.21 lbs (550g)

**Performance:**

- Refresh Speed: 2.4 seconds
- Battery Life: 8 hours
- Power Consumption: 1.53 watts

**Timeline:**

- Design: 3 weeks | Prototype: 3 weeks | Pilot: 4 weeks
- **Total: 10 weeks** | Certification: 4 weeks

**Manufacturing:**

- Component Count: 320
- Assembly Time: 20 min/unit
- Yield Estimate: 94%

---

## ARCH_PIEZO_DLX: Piezo Deluxe (Wireless) - "Premium Pro"

### Market Position

Premium / Mobile Professional / Sleek Design / Rechargeable

### Requirements Traceability

- **PRD-IFACE-001-ASMP:** Scenario A (BLE-only): Wireless, requires battery, $200-250 BOM
- **PRD-COST-001-ASMP:** Premium BOM target ($200-250)
- **PRD-SIZE-001-ASMP:** Most portable (sleek, integrated rechargeable)

### Subsystem Breakdown

**Core Subsystems (Shared):**

- **SS-ACTUATOR:** Braille Actuator Array → TBD-PIEZO-01 (TBD TBD-PIEZO-2MM)
  - 192 bimorph piezo dots (32 cells × 6 dots/cell), 100-200VDC drive, CAPACITIVE LOAD
  - Qty: 1 × 192 = 192
- **SS-CONTROL:** Main Control Unit (MCU) → 497-14367-ND (STMicro STM32F407VGT6)
  - Microcontroller for actuator control + text processing
  - Qty: 1 × 1 = 1
- **SS-IO-EXPAND:** I/O Expander Array → MCP23017-E/SP-ND (Microchip MCP23017-E/SP)
  - GPIO expansion (STM32 140 GPIO → 192 total needed)
  - Qty: 1 × 4 = 4
- **SS-ACTUATOR-DRIVER:** Actuator High-Voltage Driver Array → TBD-HV-DRIVER (TBD TBD-HV-DRV-200V)
  - 200V drivers for piezo actuators (CAPACITIVE LOAD)
  - Qty: 1 × 24 = 24
- **SS-USER-IO:** User Interface Buttons → CKN12221-ND (C&K KMR221NGLFS)
  - 2× tactile buttons (UP/DOWN navigation)
  - Qty: 1 × 2 = 2
- **SS-PCB:** Main PCB (4-layer) → CUSTOM-PCB-01 (PCBWay PCB-4L-200x100)
  - 200mm × 100mm board for all electronics
  - Qty: 1 × 1 = 1
- **SS-ENCLOSURE:** Mechanical Enclosure → CUSTOM-ENCL-01 (Shapeways 3DP-SLS-NYLON)
  - Housing + braille dot surface
  - Qty: 1 × 1 = 1
- **SS-EMI-BULK-CAP:** EMI Bulk Capacitor Array → 493-2203-ND (Nichicon UVR1H102MHD)
  - 1000µF electrolytic capacitors for driver IC power rail filtering
  - Qty: 1 × 24 = 24
- **SS-EMI-BYPASS-CAP:** EMI Bypass Capacitor Array → 399-4151-1-ND (Kemet C0805C104K5RACTU)
  - 100nF ceramic capacitors for high-frequency EMI suppression
  - Qty: 1 × 24 = 24

**Unique Subsystems (Architecture-Specific):**

- **SS-COMM-BLE:** BLE 5.0 Communication Module → 1597-MDBT50Q-1MV2-ND (Raytac MDBT50Q-1MV2)
  - Bluetooth Low Energy radio for wireless connection
  - Qty: 1 × 1
- **SS-POWER-LIION-CELL:** Li-ion Cell (18650) → TBD-18650-01 (TBD TBD-18650-2500)
  - 18650 rechargeable cell 2500mAh
  - Qty: 1 × 1
- **SS-POWER-LIION-CHARGER:** Li-ion Charger IC → 296-38713-1-ND (TI BQ24075RGTT)
  - USB-C charging circuit
  - Qty: 1 × 1
- **SS-POWER-LIION-PROTECTION:** Li-ion Protection Circuit → TBD-PROTECTION-01 (TBD TBD-BMS-1S)
  - Battery safety (overcharge/discharge)
  - Qty: 1 × 1
- **SS-POWER-LIION-GAUGE:** Fuel Gauge IC → 296-41985-1-ND (TI BQ27441DRZT-G1A)
  - Battery SOC estimation
  - Qty: 1 × 1
- **SS-POWER-LIION-BOOST-200V:** Li-ion Power - Boost (3.7V→200V) → TBD-HV-BOOST (TBD TBD-BOOST-200V)
  - Actuator HV power from Li-ion battery (200V for bimorph piezo)
  - Qty: 1 × 1

### Qualitative Assessment

**Cost Profile:**

- Bom: 🟠 MEDIUM-HIGH
- Certification: 🔴 HIGH
- Nre: 🔴 HIGH

**User Experience:**

- Setup: 🟡 GOOD
- Convenience: 🟡 GOOD
- Reliability: 🟡 GOOD
- Battery Anxiety: 🔴 HIGH
- Mobility: 💚 EXCELLENT
- Refresh Speed: 💚 FAST

**Complexity:**

- Hardware: 🔴 COMPLEX
- Firmware: 🟡 MODERATE
- Power: 🔴 VERY COMPLEX
- Mechanical: 🟡 MODERATE

**Timeline:**

- Pilot: 🟡 MODERATE
- Parts Leadtime: 🟡 MEDIUM
- Certification: 🔴 SLOW

**Manufacturing:**

- Assembly: 🟡 MODERATE
- Component Count: 🟡 MEDIUM
- Dfm: 🟡 GOOD
- Yield Risk: 🟡 MEDIUM

**Risk:**

- Technical: 🔴 HIGH
- Supply Chain: 🟡 MEDIUM
- Safety: VERY HIGH
- Timeline: 🔴 HIGH
- Cost Overrun: 🔴 HIGH

**Market Fit:**

- Education: 🔴 POOR
- Consumer: 💚 EXCELLENT
- Professional: 💚 EXCELLENT
- Accessibility Ngos: 🟡 GOOD
- Global: 🟠 FAIR

### Quantitative Metrics

**Cost:**

- BOM Subtotal: $379.57
- Misc 15%: $56.94
- **BOM Total: $436.51** (Target: $225, Range: $200-$250)
- **Cost Gap: $211.51 (94% over target)** ⚠️
- Certification: $35,000
- NRE Total: $70,000

**Size & Weight:**

- Dimensions: 210×100×20 mm (8.3×3.9×0.8 in)
- Weight: 0.99 lbs (450g)

**Performance:**

- Refresh Speed: 1.5 seconds
- Battery Life: 10 hours
- Power Consumption: 1.0 watts

**Timeline:**

- Design: 3 weeks | Prototype: 2 weeks | Pilot: 3 weeks
- **Total: 8 weeks** | Certification: 8 weeks

**Manufacturing:**

- Component Count: 270
- Assembly Time: 18 min/unit
- Yield Estimate: 96%

---

## Architecture Comparison Matrix

### Cost Comparison

| Metric | ARCH_PIEZO_ECO | ARCH_SOL_ECO | ARCH_PIEZO_DLX |
|--------|---------|---------|---------|
| BOM Target | $125 | $165 | $225 |
| BOM Actual | $415.35 (232% over) ⚠️ | $240.75 (46% over) ⚠️ | $436.51 (94% over) ⚠️ |
| Certification | $20K | $20K | $35K |
| NRE Total | $35K | $70K | $70K |

## Cost Gap Analysis

**All architectures currently OVER BOM target:**

- **ARCH_PIEZO_ECO:** $415.35 actual vs $125 target → **$290.35 gap (232% over)**
- **ARCH_SOL_ECO:** $240.75 actual vs $165 target → **$75.75 gap (46% over)**
- **ARCH_PIEZO_DLX:** $436.51 actual vs $225 target → **$211.51 gap (94% over)**

**Primary cost driver:** SS-ACTUATOR ($288.00 for 192× actuators)

**Cost reduction strategies (for v1.4.0 Trade-off Analysis):**

1. Negotiate actuator volume pricing (currently using 100-qty, need 1K+ quotes)
2. Reduce cell count (32→24 cells = 25% actuator savings)
3. Alternative actuator technologies (solenoid + latch = $96 vs piezo $288, see ARCH-D)
4. Value engineering (2-layer PCB where possible, simpler enclosure)

---

## PCB Design Requirements by Architecture

| Architecture | Layers | Key Drivers | Min Trace | HV Clearance | Max Emissions |
|--------------|--------|-------------|-----------|--------------|---------------|
| ARCH_PIEZO_ECO (Piezo Economy (Wired)) | 4-layer | 200V drivers, USB, boost conv | 6 mil | 100 mil | 168 MHz |
| ARCH_SOL_ECO (Solenoid Economy (Rotary Cam)) | 4-layer | 12V drivers, USB, boost conv | 6 mil | 20 mil | 168 MHz |
| ARCH_PIEZO_DLX (Piezo Deluxe (Wireless)) | 4-layer | 200V drivers, BLE (2.4 GHz), boost conv | 6 mil | 100 mil | 2440 MHz |

**Layer Stack (all 4-layer architectures):**

- Layer 1 (Top): Signal routing (6 mil min trace/space for MCU fanout)
- Layer 2 (GND): Continuous ground plane (FCC Part 15B requirement)
- Layer 3 (Power): Isolated planes for 200V HV / 12V / 5V / 3.3V (voltage depends on architecture)
- Layer 4 (Bottom): Signal routing

**Cost Impact:** 4-layer PCB ~$15 vs 2-layer ~$8 (but 2-layer would fail FCC emissions)

---

## Block Diagrams

- **ARCH_PIEZO_ECO:** docs/diagrams/arch-piezo-eco-wired-block.png
- **ARCH_SOL_ECO:** docs/diagrams/arch-sol-eco-cam-block.png
- **ARCH_PIEZO_DLX:** docs/diagrams/arch-piezo-dlx-wireless-block.png

---

## Next Steps (v1.4.0 Trade-off Analysis)

1. **Cost optimization:** Address $200-300 BOM gap across all architectures
2. **Vendor quotes:** Get real pricing for piezo actuators (TBD-PIEZO-01) and solenoids (TBD-SOLENOID-01)
3. **Trade-off analysis:** Document decision rationale for final recommendation
4. **Risk mitigation:** Plan for supply chain, certification timeline risks
5. **Prototype validation:** Validate ARCH-D latch mechanism (Week 3-4)

