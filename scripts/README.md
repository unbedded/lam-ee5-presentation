# Scripts Directory

Python automation scripts for generating project artifacts from YAML/CSV source data.

## Scripts

### `generate_arch_artifacts.py`

**Purpose:** Auto-generate architecture documentation and BOMs from YAML/CSV databases

**Invoked by:** `/arch-gen` slash command

**Input Sources:**
- `source/architectures.yaml` - Architecture definitions (qualitative + quantitative specs)
- `source/subsystems.yaml` - Subsystem definitions and electrical specs
- `source/parts.csv` - Digikey parts database with pricing/lead times

**Generated Artifacts:**
- `artifacts/architecture.md` - Comprehensive architecture documentation (15 KB)
- `artifacts/bom/*.csv` - Bill of Materials for each architecture
- `artifacts/architecture-comparison-matrix.md` - Side-by-side comparison tables (3.8 KB)

**Key Features:**
- **Dynamic architecture support:** Automatically adapts to any architectures defined in YAML (no hardcoded IDs)
- **PCB layer calculation:** Analyzes subsystems to determine required PCB layers
- **Qualitative emoji formatting:** 💚 BEST / 🟡 GOOD / 🟠 FAIR / 🔴 POOR ratings
- **Cost gap analysis:** Highlights BOM vs target deltas
- **Dual subsystem lookup:** Checks both `subsystems_core` and `subsystems_unique`

**Usage:**
```bash
python3 scripts/generate_arch_artifacts.py
```

**Example Output:**
```
Loading source files...
✅ Generated artifacts/architecture.md (15.0 KB)
✅ Generated artifacts/bom/arch-piezo-eco-bom.csv (14 lines)
✅ Generated artifacts/bom/arch-sol-eco-bom.csv (21 lines)
✅ Generated artifacts/bom/arch-piezo-dlx-bom.csv (16 lines)
✅ Generated artifacts/architecture-comparison-matrix.md (3.8 KB)

📊 BOM Summary:
  - ARCH_PIEZO_ECO (Piezo Economy (Wired)): $419.75
  - ARCH_SOL_ECO (Solenoid Economy (Rotary Cam)): $276.58
  - ARCH_PIEZO_DLX (Piezo Deluxe (Wireless)): $442.18
```

---

## Future Scripts

Additional generators to be added:

- **`generate_req_artifacts.py`** - Requirements documentation from `source/requirements.yaml`
- **`generate_tradeoff_analysis.py`** - Trade-off analysis from architecture comparisons
- **`generate_presentation_slides.py`** - Marp/reveal.js slides from artifacts

---

**Note:** All scripts assume they're run from the project root directory (`/home/preact/sw/job/lam/ee/`)
