---
description: Generate architecture docs and BOMs from YAML/CSV sources
---

# Architecture Generation Command

Auto-generate architecture documentation and BOMs from YAML+CSV databases.

**Scope:** Individual architecture details (subsystems, specs, BOMs)
**Future:** Comparison/tradeoff logic will move to `/arch-tradeoff` slash command (see TODO.md Technical-Debt)

## What You'll Generate

### Direct Source Files (Read by Generator)
1. `source/architectures.yaml` - Full architecture specs (ARCH-A, ARCH-B, ARCH-C, ARCH-D)
2. `source/subsystems.yaml` - Subsystem definitions and part references
3. `source/parts.csv` - Digikey parts database with pricing/lead times

### Supporting Analysis (Referenced in YAML, Not Read by Generator)
These documents informed the YAML data but are not directly parsed:
- `source/requirements.yaml` - 24 requirements driving architecture decisions
- `docs/market-braille-display-scan.md` - Competitive landscape analysis
- `docs/actuator-technology-tradeoff.md` - 5 actuator technologies compared
- `docs/actuator-mechanical-latch-concept.md` - Mechanical latch design (ARCH-D)
- `docs/power-budget-analysis.md` - Detailed power calculations
- `docs/cots-timeline-analysis.md` - Lead time constraints analysis
- `artifacts/rubric-reports/req-traceability-report.md` - Requirements coverage

**Note:** The generator creates technical reference docs. For strategic analysis with trade-offs and recommendations, see manually-maintained `docs/architecture.md`.

### Generated Artifacts

### 1. Architecture Documentation
**File:** `artifacts/architecture.md`

**Structure:**
```markdown
# Braille Display - Solution Architectures

[Executive Summary - 1 paragraph comparing 3 architectures]

## Architecture Overview
[Table: ARCH-B/C/A with nickname, market position, BOM target, timeline]

---

## ARCH-B: Wired (Budget) - "Value Desk"

### Market Position
[Entry-level, Education, Desktop]

### Requirements Traceability
[List driven_by_requirements from YAML with IDs]

### Subsystem Breakdown
**Core Subsystems (Shared):**
- SS-ACTUATOR: [description from subsystems.yaml] → [Digikey PN from parts.csv]
- SS-CONTROL: [description] → [Digikey PN]
[... all core subsystems]

**Unique Subsystems (ARCH-B only):**
- SS-COMM-USB: [description] → [Digikey PN]
- SS-POWER-USB-LDO: [description] → [Digikey PN]

### Qualitative Assessment
[Format qualitative ratings as tables with 💚 BEST / 🟡 GOOD / 🔴 FAIR ratings]

**Cost Profile:**
- BOM: 💚 LOW
- Certification: 💚 LOW ($20K FCC 15B only)
- NRE: 💚 LOW

**User Experience:**
- Setup: 💚 BEST (plug and play)
- Convenience: 🔴 FAIR (tethered)
- Mobility: 🔴 POOR (wired only)
[... all qualitative dimensions]

### Quantitative Metrics
**Cost:**
- BOM Total: $419.75 (Target: $125, Range: $100-150)
- Certification: $20,000
- NRE Total: $35,000

**Size & Weight:**
- Dimensions: 200×100×15 mm (8.0×4.0×0.6 in)
- Weight: 0.79 lbs (360g)

**Timeline:**
- Design: 2 weeks | Prototype: 2 weeks | Pilot: 2 weeks
- Total: 6 weeks | Certification: 4 weeks

[Repeat for ARCH-C and ARCH-A]

---

## Architecture Comparison Matrix

### Cost Comparison
| Metric | ARCH-B (Wired) | ARCH-C (Hybrid) | ARCH-A (Wireless) |
|--------|----------------|-----------------|-------------------|
| BOM Target | $125 | $220 | $225 |
| BOM Actual | $419.75 ⚠️ | $435.85 ⚠️ | $449.08 ⚠️ |
| Certification | $20K | $26.5K | $35K |
| NRE Total | $35K | $55K | $70K |

[... all comparison dimensions from architectures.yaml]

---

## Cost Gap Analysis

**All architectures currently OVER BOM target:**
- ARCH-B: $419.75 actual vs $125 target → **$295 gap (236% over)**
- ARCH-C: $435.85 actual vs $220 target → **$216 gap (98% over)**
- ARCH-A: $449.08 actual vs $225 target → **$224 gap (100% over)**

**Primary cost driver:** SS-ACTUATOR ($288 for 192× piezo actuators @ $1.50 ea)

**Cost reduction strategies (for v1.4.0 Trade-off Analysis):**
1. Negotiate actuator volume pricing (currently using 100-qty, need 1K+ quotes)
2. Reduce cell count (32→24 cells = 25% actuator savings)
3. Alternative actuator technologies (solenoid, SMA wire)
4. Value engineering (2-layer PCB, simpler enclosure)

---

## PCB Design Requirements by Architecture

| Architecture | Layers Required | Key Drivers | Min Trace | HV Clearance | Max Emissions |
|--------------|-----------------|-------------|-----------|--------------|---------------|
| ARCH-B (Wired) | 4-layer | STM32F4 (168 MHz), 30V drivers, USB, boost | 6 mil | 50 mil | 168 MHz |
| ARCH-C (Hybrid) | 4-layer | STM32F4, 30V drivers, USB, BLE (2.4 GHz), boost | 6 mil | 50 mil | 2440 MHz |
| ARCH-A (Wireless) | 4-layer | STM32F4, 30V drivers, BLE (2.4 GHz), boost | 6 mil | 50 mil | 2440 MHz |

**Layer Stack (all 3 architectures):**
- Layer 1 (Top): Signal routing (6 mil min trace/space for MCU fanout)
- Layer 2 (GND): Continuous ground plane (FCC Part 15B requirement)
- Layer 3 (Power): Isolated planes for 30V / 5V / 3.3V
- Layer 4 (Bottom): Signal routing

**Cost Impact:** 4-layer PCB ~$15 vs 2-layer ~$8 (but 2-layer would fail FCC emissions)

---

## Block Diagrams

[Reference to docs/diagrams/arch-{a,b,c}-block.png - to be created]

---

## Next Steps (v1.4.0 Trade-off Analysis)

1. **Cost optimization:** Address $200-300 BOM gap
2. **Vendor quotes:** Get real pricing for piezo actuators (TBD-PIEZO-01)
3. **Trade-off analysis:** Document decision rationale for final recommendation
4. **Risk mitigation:** Plan for supply chain, certification timeline risks
```

### 2. Bill of Materials (BOMs)
**Files:**
- `artifacts/bom/arch-b-wired-bom.csv`
- `artifacts/bom/arch-c-hybrid-bom.csv`
- `artifacts/bom/arch-a-wireless-bom.csv`

**CSV Format:**
```csv
Line,Subsystem_ID,Subsystem_Name,Digikey_PN,MFR,MFR_PN,Description,Qty,Unit_Price_100,Line_Total,Leadtime_Weeks,ROHS,Notes
1,SS-ACTUATOR,Braille Actuator Array,TBD-PIEZO-01,TBD,TBD-PIEZO-2MM,"Piezo 2mm dia, 0.5mm stroke",192,1.50,288.00,8,Y,"Need vendor quote, size ≤2.3mm"
2,SS-CONTROL,Main MCU,497-14367-ND,STMicro,STM32F407VGT6,"ARM M4 168MHz, 140 GPIO",1,8.00,8.00,12,Y,"Check stock, long leadtime"
[... all subsystems for this architecture]
---,---,---,---,---,---,SUBTOTAL,---,---,365.00,---,---,---
---,---,---,---,---,---,Misc 15%,---,---,54.75,---,---,"Passives, connectors"
---,---,---,---,---,---,TOTAL,---,---,419.75,---,---,---
```

**Logic:**
1. Read architectures.yaml → Get subsystems list (core + unique) for this architecture
2. For each subsystem ID:
   - Read subsystems.yaml → Get quantity
   - Read parts.csv (match Subsystem column) → Get Digikey_PN, pricing, leadtime
   - Calculate Line_Total = Qty × Unit_Price_100
3. Calculate SUBTOTAL, Misc 15%, TOTAL

### 3. Comparison Matrix
**File:** `artifacts/architecture-comparison-matrix.md`

Generate tables from architectures.yaml `comparison_dimensions`:
- Cost comparison (BOM, cert, NRE)
- Size & Weight
- User Experience (qualitative + battery life)
- Complexity
- Timeline
- Manufacturing
- Risk
- Market Fit

Use color coding: 💚 Best / 🟡 Medium / 🟠 Fair / 🔴 Poor

### 4. Presentation Slides
**File:** `artifacts/architecture-slides.md`

Generate markdown slides (for Marp or reveal.js):
```markdown
---
# Solution Architectures
## 3 Alternatives Evaluated

---
## Architecture Portfolio

| | ARCH-B | ARCH-C | ARCH-A |
|---|---|---|---|
| **Name** | Wired (Budget) | Hybrid (Mid) | Wireless (Premium) |
| **Market** | Education/Desktop | Mainstream Mobile | Professional |
| **BOM Target** | $125 | $220 | $225 |
| **Timeline** | 6 weeks | 7.5 weeks | 8 weeks |

---
## Qualitative Comparison
[Visual matrix from architectures.yaml]

---
## Cost Breakdown
[BOM comparison chart - suggest using artifacts to generate chart later]

---
## Recommendation
[Placeholder - to be filled in v1.5.0 after trade-off analysis]
```

## Execution

Run the generator script to create all architecture artifacts:

```bash
python3 scripts/generate_arch_artifacts.py
```

**Implementation:** `scripts/generate_arch_artifacts.py` (26KB, 609 lines)
**Dynamic architecture support:** Automatically adapts to any architectures defined in YAML (no hardcoded IDs)

### Key Functions:

1. **Load databases:**
   ```python
   import yaml, csv
   archs = yaml.safe_load(open('source/architectures.yaml'))
   subsys = yaml.safe_load(open('source/subsystems.yaml'))
   parts = list(csv.DictReader(open('source/parts.csv')))
   ```

2. **Calculate PCB layer requirements:**
   ```python
   def calculate_pcb_layers(arch_data, subsys_db):
       """Calculate required PCB layers based on subsystems used"""
       max_layers = 2  # Start with 2-layer minimum
       layer_drivers = []

       # Check all subsystems (core + unique)
       for ss_id in arch_data['subsystems']['core'] + arch_data['subsystems']['unique']:
           ss = subsys_db['subsystems_core'].get(ss_id) or subsys_db['subsystems_unique'].get(ss_id)
           if ss and 'pcb_specs' in ss:
               layers = ss['pcb_specs'].get('layers_required', 2)
               if layers >= 4:  # Track all 4-layer requirements
                   layer_drivers.append(ss_id)
               max_layers = max(max_layers, layers)

       return max_layers, layer_drivers
   ```

2. **Generate architecture.md:**
   - Iterate through archs['architectures'] (ARCH-B, ARCH-C, ARCH-A)
   - For each arch, format sections (requirements, subsystems, qualitative, quantitative)
   - Generate comparison tables using `comparison_dimensions`

3. **Generate BOMs:**
   - For each architecture:
     - Get subsystem list (core + unique)
     - Query subsystems.yaml for quantity
     - Query parts.csv for pricing/details
     - Calculate line totals
     - Write CSV

4. **Generate comparison matrix:**
   - Use `comparison_dimensions` from architectures.yaml
   - Extract qualitative and quantitative data for all 3 architectures
   - Format as tables

5. **Generate slides:**
   - Extract key tables/metrics from architecture.md
   - Format for presentation (concise, visual)

## Example Output

```
Loading source files...
Generating artifacts/architecture.md...
✅ Generated artifacts/architecture.md (15.0 KB)

Generating BOMs...
✅ Generated artifacts/bom/arch-piezo-eco-bom.csv (14 lines)
✅ Generated artifacts/bom/arch-sol-eco-bom.csv (21 lines)
✅ Generated artifacts/bom/arch-piezo-dlx-bom.csv (16 lines)

Generating artifacts/architecture-comparison-matrix.md...
✅ Generated artifacts/architecture-comparison-matrix.md (3.8 KB)

======================================================================
📊 BOM Summary:
  - ARCH_PIEZO_ECO (Piezo Economy (Wired)): $419.75
  - ARCH_SOL_ECO (Solenoid Economy (Rotary Cam)): $276.58
  - ARCH_PIEZO_DLX (Piezo Deluxe (Wireless)): $442.18

⚠️  Cost Gap: All architectures over BOM target (primary driver: actuators)
======================================================================
```

---

**Priority:** HIGH - Core deliverable for v1.3.0 Solution Architecture Development (25/100 rubric points)
**Location:** `scripts/generate_arch_artifacts.py`
