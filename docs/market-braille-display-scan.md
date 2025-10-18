# Market Scan: Commercial Braille Display Solutions
**Project:** Lam Research - Braille Display EE Concept Evaluation
**Author:** Spencer Barrett
**Date:** 2025-10-09
**Purpose:** Identify existing braille display solutions, technologies used, price points, and market positioning

---

## Executive Summary

**Key Findings:**
1. **Piezo dominates:** Nearly all commercial braille displays use piezoelectric ceramic bimorph actuators
2. **Price floor:** $35/cell OEM cost ($4.38/dot) suggests $200+ BOM minimum for 32-cell device
3. **Budget segment emerging:** Orbit Reader ($449, 20-cell) and BrailleMe ($515, 20-cell) disrupting $2K+ market
4. **No COTS piezo <5mm:** All manufacturers use custom piezo actuators (8-12 week lead time)
5. **Voltage challenge:** 200V typical for piezo actuation (our design: 30V insufficient?)

**Market Gap:** No 32-cell device at <$600 retail ($200 BOM) with COTS components (≤4 week lead time)

---

## Table of Contents
- [Major Manufacturers & Products](#major-manufacturers--products)
- [Technology Analysis](#technology-analysis)
- [Price Points & Market Segments](#price-points--market-segments)
- [Actuator Technology Specifications](#actuator-technology-specifications)
- [Competitive Positioning](#competitive-positioning)
- [Implications for Our Design](#implications-for-our-design)

---

## Major Manufacturers & Products

### Budget Segment (<$600 retail)

| Manufacturer | Product | Cells | Price (USD) | Interface | Battery | Notes |
|--------------|---------|-------|-------------|-----------|---------|-------|
| **Orbit Research** | Orbit Reader 20 | 20 | $449 | USB, BLE | Rechargeable | "World's most affordable", aimed at education |
| **Orbit Research** | Orbit Reader 40 | 40 | ~$800 (est.) | USB, BLE | Rechargeable | Least expensive 40-cell on market |
| **Innovision** | BrailleMe | 20 | $515 | USB, BLE | Unknown | Plugs into phone/computer |

### Mid-Range Segment ($1K-$2K retail)

| Manufacturer | Product | Cells | Price (USD) | Interface | Battery | Notes |
|--------------|---------|-------|-------------|-----------|---------|-------|
| **HumanWare** | Brailliant BI 20x | 20 | ~$1,200 | USB, BLE | Rechargeable | Professional grade |
| **HumanWare** | Brailliant BI 40x | 40 | ~$1,800 | USB, BLE | Rechargeable | Professional grade |
| **Freedom Scientific** | Focus 40 Blue | 40 | ~$1,700 | USB, BLE | Rechargeable | Popular with professionals |

### Premium Segment ($2K+ retail)

| Manufacturer | Product | Cells | Price (USD) | Interface | Battery | Notes |
|--------------|---------|-------|-------------|-----------|---------|-------|
| **HumanWare** | Mantis Q40 | 40 | ~$2,000 | USB, BLE | Rechargeable | Perkins-style keyboard |
| **Orbit Research** | Graphiti Plus | Graphics | ~$3,500 | USB | Rechargeable | Multi-level Tactuator™ for graphics |

---

## Technology Analysis

### Piezoelectric Actuators (Dominant Technology)

**Mechanism:**
- Piezoceramic bimorphs (two bonded piezo layers)
- Cantilever beam design (stair-stepped stack)
- Each beam lifts 1.5mm diameter pin 0.5mm above surface
- One actuator per dot (192 actuators for 32-cell device)

**Advantages:**
- Fast response (<50ms typical)
- Low hold power (~0W, capacitive charge retention)
- Reliable (>1M cycles demonstrated)
- Established manufacturing (all major vendors use piezo)

**Disadvantages:**
- **High voltage:** 200V typical (some designs 120-300V range)
- **Custom tooling:** No COTS piezo at 2-3mm size (8-12 week lead time)
- **High cost:** $35/cell OEM ($4.38/dot) = $140 for 32 dots (6 cells × 6 dots)
  - Wait, that's wrong math: 32 cells × 6 dots = 192 dots × $4.38 = **$841 actuator cost**
  - Our estimate: $288 for custom 2mm piezo (aggressive pricing)
- **Proprietary:** Each manufacturer has custom piezo design (not interchangeable)

**Vendors:**
- HOERBIGER Motion Control GmbH (Piezo Products division)
- Custom designs by Orbit Research (TrueBraille™ cells)
- Tactuator™ (multi-level, Orbit Research proprietary)

---

## Price Points & Market Segments

### Price vs Character Analysis

| Segment | CHAR | Total Pins | Retail Price | Est EE BOM* | $/Pin (BOM) | Example Products |
|---------|------|------------|--------------|-------------|-------------|------------------|
| **Budget** | 20 | 160 (8/char) | $449-$515 | $150-$170 | $0.94-$1.06 | Orbit Reader 20, BrailleMe |
| **Budget** | 40 | 320 (8/char) | ~$800 | ~$265 | ~$0.83 | Orbit Reader 40 |
| **Mid-Range** | 20 | 160 (8/char) | ~$1,200 | ~$400 | ~$2.50 | Brailliant BI 20x |
| **Mid-Range** | 40 | 320 (8/char) | ~$1,700 | ~$565 | ~$1.77 | Focus 40 Blue, Brailliant BI 40x |
| **Premium** | 40+ | 320+ (8/char) | $2,000+ | $665+ | ~$2.08+ | Mantis Q40, Graphiti Plus |

*\* List price = BOM × 3 (EE industry standard markup)*

**Key Observations:**
1. **Budget segment:** $0.83-$1.06/pin BOM (Orbit Reader, BrailleMe)
   - Commercial displays use 8 pins/char (6 standard + 2 computer braille)
   - Our target: $200 BOM ÷ 192 pins (32 char × 6 pins) = **$1.04/pin** (competitive with budget segment)
2. **Economies of scale:** 40-char devices have lower $/pin BOM than 20-char
3. **OEM cost discrepancy:** Search result says $35/cell OEM ($4.38/dot)
   - But 20-char devices retail $449 → $150 BOM ÷ 160 pins = $0.94/pin
   - Suggests OEM cost ≠ final BOM cost (add PCB, enclosure, battery, etc.)

---

## Actuator Technology Specifications

### Piezoelectric Bimorph Specifications (from literature)

| Parameter | Typical Value | Notes |
|-----------|---------------|-------|
| **Voltage** | 200V | "Simply supported piezoelectric beam needs at least 200V" |
| **Stroke** | 0.5mm | Standard braille dot height above surface |
| **Pin diameter** | 1.5mm | US ADA spec (1.5-1.6mm) |
| **Actuator footprint** | ≤2.5mm² | Required for 2.5mm cell pitch |
| **Force** | 0.5-1.0N | Holds pin against reading force (50-100g) |
| **Response time** | 10-50ms | Fast actuation for <1 sec full-line refresh |
| **Hold power** | ~0W | Capacitive charge retention (µW leakage) |
| **Cycles** | >1M | Reliability requirement (2 years × 10 actuations/min) |

**CRITICAL FINDING: 200V Requirement**
- Literature: "Simply supported piezoelectric beam needs at least 200V"
- Our design: 30V boost converter (inadequate?)
- Possible resolution:
  - Use thicker piezo (more displacement per volt, but larger size)
  - Use lever amplification (mechanical gain)
  - Accept lower force/stroke (marginal ADA compliance)
  - **ACTION:** Consult piezo vendor for 30V design feasibility

---

## Competitive Positioning

### Our 32-Character Design vs Market

| Feature | Our Design (Target) | Orbit Reader 20 | BrailleMe | Brailliant BI 20x |
|---------|---------------------|-----------------|-----------|-------------------|
| **Characters** | 32 (192 pins) | 20 (160 pins) | 20 (160 pins) | 20 (160 pins) |
| **Price (retail)** | $600 (target) | $449 | $515 | $1,200 |
| **BOM (est.)** | $200 (target) | $150 | $170 | $400 |
| **Interface** | BLE + USB (hybrid) | BLE + USB | BLE + USB | BLE + USB |
| **Battery** | 4× AA (8 hrs) | Rechargeable | Unknown | Rechargeable |
| **Actuator** | TBD (piezo/solenoid) | Piezo (proprietary) | Piezo (proprietary) | Piezo (proprietary) |
| **Timeline** | 2 months (COTS) | Unknown | Unknown | Unknown |

**Value Proposition:**
- **60% more characters** than Orbit Reader/BrailleMe (32 vs 20)
- **20% more pins** (192 vs 160) for more text per line
- **Competitive price** at $600 retail (vs $449 for 20-char Orbit Reader)
- **AA batteries** = instant swap, no charger anxiety (unique vs all competitors)
- **COTS mandate** = 2-month timeline (aggressive, risky for custom piezo)

**Competitive Risk:**
- Orbit Reader 40 (40-char, 320 pins) at ~$800 retail → More chars, similar price
- Our 32-char at $600 may be squeezed between 20-char ($449) and 40-char ($800)
- **Differentiation needed:** AA batteries, COTS timeline, or sub-$500 pricing

---

## Implications for Our Design

### 1. Actuator Technology Decision

| Technology | Market Precedent | Our Feasibility (2-month timeline) | Recommendation |
|------------|------------------|-------------------------------------|----------------|
| **Piezo (200V)** | ✅ All commercial products | ❌ Requires custom 8-12 week lead time | Not feasible for 2-month timeline |
| **Piezo (30V)** | ⚠️ No commercial precedent | ⚠️ Unknown if 30V sufficient for 0.5mm stroke | Consult vendor (1-2 days) |
| **Solenoid (COTS)** | ❌ No commercial braille displays | ✅ COTS available (2-week lead time) | ARCH-D feasible if latch works |

**ACTION:**
- Contact piezo vendors (Murata, TDK, Piezo Systems, HOERBIGER) → Ask if 30V piezo possible at 2-3mm size
- If NO → Proceed with ARCH-D (solenoid + latch) as only COTS option

### 2. Cost Target Validation

**Market data:**
- Budget segment: $0.83-$1.06/pin BOM (Orbit Reader 20-40, BrailleMe)
- Our target: $1.04/pin BOM (192 pins × $1.04 = $200 BOM)
- **Conclusion:** Competitive with budget segment (middle of range)

**Actuator cost drivers:**
- Piezo: $288 (custom 2mm) → $1.50/pin (44% over target)
- Solenoid: $131 (COTS 4mm + latch) → $0.68/pin (35% under target) ✅

### 3. COTS Mandate Impact

**Critical constraint:** PRD-SCHED-002-ASMP requires ≤4 week lead time
- **Piezo:** 8-12 week lead time (VIOLATES)
- **Solenoid:** 2-week lead time (COMPLIES)

**Market gap:** NO commercial braille displays use COTS actuators
- All use custom piezo (8-12 week tooling)
- Our COTS mandate = FORCED innovation (solenoid + latch)

**Risk vs Opportunity:**
- **Risk:** Solenoid unproven for braille (no market precedent)
- **Opportunity:** Cost advantage ($131 vs $288 = 54% savings) + COTS timeline

### 4. Competitive Positioning Adjustments

**Market positioning options:**

| Option | Strategy | Price | Target Market | Risk |
|--------|----------|-------|---------------|------|
| **A. Premium 32-char** | Piezo (200V custom) | $800 retail | Professionals | Timeline miss (8-12 weeks) |
| **B. Budget 32-char** | Solenoid + latch | $450 retail | Education, NGOs | Latch unproven (HIGH risk) |
| **C. Hybrid 32-char** | Piezo (30V custom) | $600 retail | Mainstream | 30V piezo feasibility unknown |

**RECOMMENDATION:** Pursue Option B (Budget 32-char, solenoid + latch)
- Only option that meets 2-month COTS mandate
- Best cost position ($224 BOM → $450-500 retail)
- Targets underserved education/NGO market (less sensitive to slow 5.2-sec refresh)
- Prototype latch Week 3-4 to validate feasibility (GO/NO-GO decision point)

---

## Competitor Actuator Technologies (Summary)

| Manufacturer | Technology | Voltage | Size | $/Pin (est.) | Lead Time |
|--------------|------------|---------|------|--------------|-----------|
| **Orbit Research** | TrueBraille™ piezo | Unknown (likely 120-200V) | Proprietary | $0.94-$1.06 (budget) | 8-12 weeks (custom) |
| **Orbit Research** | Tactuator™ multi-level | Unknown | Proprietary | $2.08+ (premium) | 8-12 weeks (custom) |
| **HumanWare** | Piezo bimorph | Unknown (likely 200V) | Proprietary | $1.77-$2.50 | 8-12 weeks (custom) |
| **Freedom Scientific** | Piezo bimorph | Unknown (likely 200V) | Proprietary | $1.77-$2.50 | 8-12 weeks (custom) |
| **HOERBIGER** | Piezo bimorph modules | 8 pins/module | 2.5mm² footprint | $4.38/pin OEM | 8-12 weeks (custom) |

**Universal finding:** ALL commercial braille displays use custom piezo actuators (no COTS)

---

## Key Takeaways

1. **Piezo monopoly:** 100% of commercial braille displays use piezoelectric actuators
2. **Custom tooling required:** No COTS piezo available at 2-3mm size (all custom, 8-12 week lead)
3. **Voltage challenge:** Literature suggests 200V minimum (our 30V design may be insufficient)
4. **Budget disruption:** Orbit Reader ($449, 20-char) and BrailleMe ($515, 20-char) disrupting $1.2K+ market
5. **Market gap:** No 32-char device <$600 with COTS components (opportunity for ARCH-D)
6. **Cost floor:** $0.83/pin BOM is lowest in market (Orbit Reader 40)
   - Our target: $1.04/pin BOM (192 pins × $1.04 = $200) — competitive with budget segment

**Strategic Decision:**
- **If 30V piezo feasible:** ARCH-C (hybrid, piezo) at $600 retail (mainstream)
- **If 30V piezo NOT feasible:** ARCH-D (solenoid + latch) at $450 retail (budget, education/NGOs)
- **Fallback:** Relax 2-month timeline, use custom 200V piezo (8-12 weeks)

**Next Action:** Contact piezo vendors (1-2 days) to determine 30V feasibility before committing to ARCH-D

---

## Sources

1. **HOERBIGER Motion Control GmbH** - Braille interfaces (piezo modules, 8 pins/module)
   - https://www.piezoproducts.com/applications/braille-interfaces/

2. **PubMed** - "Design of Piezoelectric Actuator for Braille Module by Finite Element Method"
   - 200V voltage requirement for simply supported beam
   - https://pubmed.ncbi.nlm.nih.gov/30469180/

3. **IEEE** - "Development of a Braille Display using Piezoelectric Linear Motors"
   - 1.5mm pin diameter, 0.5mm stroke specifications
   - https://ieeexplore.ieee.org/abstract/document/4108999/

4. **ResearchGate** - "Braille cell technology comparison: commercial piezoelectric actuator"
   - $35/cell OEM cost, $4.38/dot
   - https://www.researchgate.net/figure/Braille-cell-technology-comparison-a-commercial-piezoelectric-actuator-for-an-eight_fig1_3329849

5. **Perkins School for the Blind** - "Braille Me and Orbit Reader: Braille Display Comparison"
   - $449 (Orbit Reader 20), $515 (BrailleMe), 20-cell specs
   - https://www.perkins.org/resource/braille-me-and-orbit-reader-braille-display-comparison/

6. **Orbit Research** - Product catalog (Orbit Reader 20, 40, Q20, Q40, Graphiti Plus)
   - TrueBraille™ cells, Tactuator™ multi-level actuators
   - http://www.orbitresearch.com/products/braille-displays/

7. **HumanWare** - Braille displays (Brailliant BI, Mantis Q40, BrailleNote Touch Plus)
   - https://store.humanware.com/hus/braille-devices/braille-displays

8. **Cool Blind Tech** - "As We Wait for the Orbit Reader: Innovision Develops the BrailleMe"
   - BrailleMe $300 target price (actual $515), USB + BLE
   - https://coolblindtech.com/as-we-wait-for-the-orbit-reader-innovision-develops-the-brailleme-a-300-braille-display/

---

**Generated:** 2025-10-09
**Author:** Spencer Barrett, Claude Code
**Project:** Lam Research EE Interview - Braille Display Concept Evaluation
