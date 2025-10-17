# Lam Research EE Concept Evaluation

**Current Version:** v1.3.0 (Solution Architecture Development - Complete)

## Braille Display Device - Interview Preparation

### Project Overview
This repository contains preparation materials for the Lam Research Electrical Engineering interview concept evaluation. The challenge is to design electronics for a portable, low-cost braille display device that interfaces with a cell phone.

### Design Challenge
**Objective:** Create a companion device for cell phones that displays a single line of braille text (32 characters, 6 dots each = 192 control signals)

**Key Constraints:**
- Portable & low-cost
- High volume manufacturing
- 2-month timeline to production
- Interface with cell phone

### Directory Structure
```
.
├── .claude/                   # Claude Code slash commands
│   └── commands/
│       ├── rubric-eval.md     # AI-powered rubric evaluation
│       ├── req-audit.md       # Requirements compliance audit (TBD)
│       ├── req-yaml-to-md.md  # Generate requirements.md from YAML (TBD)
│       └── req-trace.md       # Requirements traceability report (TBD)
├── docs/                      # RULE 1: YOUR markdown documentation
│   ├── problem-statement.md   # EE Concept Evaluation challenge (from PDF p.9-10)
│   ├── requirements-policy.md # Requirements naming conventions & traceability rules
│   ├── interview-rubric.md    # 100-point evaluation rubric (Lam's 4 criteria)
│   ├── quality-metrics.md     # v1.1.0 Quality metrics (TBD)
│   ├── architecture.md        # v1.3.0 Solution architectures (TBD)
│   ├── tradeoffs.md           # v1.4.0 Trade-off analysis (TBD)
│   └── solution.md            # v1.5.0 Recommended solution (TBD)
├── reference/                 # RULE 2: IMMUTABLE external materials
│   ├── interview/             # Interview assignment materials
│   │   ├── contact-info.md    # Recruiter, hiring manager, contacts
│   │   └── Interview Overview and Concept Evaluation - EE Presentation.pdf
│   ├── datasheets/            # Component datasheets (downloaded PDFs)
│   │   ├── actuators/         # Piezo, solenoid, SMA, motor datasheets
│   │   ├── mcus/              # STM32, ESP32, RP2040, FPGA datasheets
│   │   ├── communication/     # BLE, USB-C, WiFi module specs
│   │   └── power/             # Battery, regulator, charging IC specs
│   ├── app-notes/             # Application notes, design guides
│   └── standards/             # ADA, FCC, ISO standards (if needed)
├── resources/                 # RULE 3: MUTABLE working files YOU create
│   ├── diagrams/              # Block diagrams (editable - PNG, Draw.io, etc.)
│   ├── schematics/            # Circuit sketches (KiCad, PDF exports)
│   ├── calculations/          # Excel/spreadsheets
│   │   ├── power-budget.xlsx  # Power consumption calculations
│   │   ├── bom-cost-estimate.xlsx  # Bill of materials with costs
│   │   └── timeline-gantt.xlsx     # Production timeline
│   └── notes/                 # Research notes, brainstorming
├── artifacts/                 # RULE 4: GENERATED outputs
│   ├── requirements.md        # v1.2.0 Generated from source/requirements.yaml
│   ├── rubric-reports/        # AI-generated evaluation reports
│   │   ├── v1.X.0-*-eval.md   # Incremental evaluations (per phase)
│   │   ├── phase1-rubric-eval.md        # v1.6.0 Phase 1 comprehensive (0-100 pts)
│   │   └── req-traceability-report.md   # v1.6.0 Requirements coverage matrix
│   ├── presentation.pdf       # v3.2.0 Final PDF (generated from source/)
│   └── presentation.pptx      # v3.2.0 Final PowerPoint (copied from source/)
├── source/                    # Single source of truth (YAML, master docs)
│   ├── requirements.yaml      # Machine-readable requirements (YAML SSOT)
│   ├── technical-analysis.md  # v3.1.0 Phase 1 consolidation
│   └── presentation.pptx      # v2.x.0 Master PowerPoint slides
├── style/                     # LaTeX styling for PDF generation
│   └── table-style.tex
├── CLAUDE.md                  # Project instructions for Claude Code
├── TODO.md                    # Phase-based task checklist (gitflow workflow)
├── TIME-LOG.md                # Phase-based time tracking (used by /status)
├── VERSION                    # Semantic version tracking
├── Makefile                   # Build system for PDFs (TBD)
└── README.md                  # This file
```

**Directory Organization Rules:**
1. **`docs/`** = Markdown files YOU write (analysis, documentation)
2. **`reference/`** = Downloaded/external materials (IMMUTABLE - datasheets, standards)
3. **`resources/`** = Working files YOU create (MUTABLE - diagrams, calculations, BOM)
4. **`artifacts/`** = Generated outputs (AI reports, build artifacts, requirements.md)

**Key Files:**
- **SSOT:** `source/requirements.yaml` - All requirements defined here
- **Generated:** `artifacts/requirements.md` - Auto-generated from YAML via `/req-yaml-to-md`
- **Rubric:** `docs/interview-rubric.md` - Evaluation criteria (100 points)
- **Policy:** `docs/requirements-policy.md` - How to write requirements
- **Workflow:** `TODO.md` - Phase-by-phase tasks with version numbers
```

### Daily Workflow
1. **Start:** Check TODO.md for current phase tasks
2. **Work:** Focus on current phase task
3. **End:** Log time to TIME-LOG.md (use /status command)

### Workflow

**Phase 1: Technical Analysis** (v1.0.0)
Each minor release produces a markdown artifact in `docs/`:

- **v1.1.0:** Quality Metrics Definition → `docs/quality-metrics.md`
- **v1.2.0:** Requirements Analysis → `docs/requirements.md`
- **v1.3.0:** Solution Architecture Development → `docs/architecture.md`
- **v1.4.0:** Trade-off Analysis → `docs/tradeoffs.md`
- **v1.5.0:** Recommended Solution → `docs/solution.md`
- **v1.6.0:** Phase 1 Self-Assessment → `artifacts/rubric-reports/phase1-rubric-eval.md` & `artifacts/rubric-reports/req-traceability-report.md`

**Phase 2: Presentation Development** (v2.0.0)
Each minor release works on PowerPoint slides in `source/presentation.pptx`:

- **v2.1.0:** Quality Metrics Definition → Define presentation success criteria
- **v2.2.0:** Presentation Structure → Create slide outline (30 min flow)
- **v2.3.0:** Visual Materials → Build diagrams, charts, tables
- **v2.4.0:** Practice & Refinement → Time presentation, prepare Q&A
- **v2.5.0:** Phase 2 Self-Assessment → Verify quality metrics

**Phase 3: Final Deliverables** (v3.0.0)
- **v3.1.0:** Documents to Build → Consolidate technical analysis
- **v3.2.0:** Artifacts to Generate → Create final PDF/PPTX outputs
- **v3.3.0:** Pre-Interview Checklist → Email materials 24 hours before interview

### Building PDFs
```bash
make all              # Convert all markdown to PDF
make clean            # Remove generated PDFs
make rebuild          # Clean and rebuild
make list             # Show all files
make help             # Show all available commands
```

### Building Presentation

**Primary Workflow: Marp HTML Presentation (RECOMMENDED)**

Fast, editable Markdown source with 1-second regeneration:

```bash
# Install Marp CLI (one-time setup)
npm install -g @marp-team/marp-cli

# Edit → Regenerate → Present workflow
vim source/presentation-marp.md   # Edit Markdown with CSS styling
make marp                          # Regenerate (1 second!)
firefox artifacts/presentation-marp.html  # Present (F11 for fullscreen)
```

**Presentation structure (Marp):**
- `source/presentation-marp.md` - Editable Markdown source (in git)
- `source/market-price-vs-chars.svg` - Images (same directory as .md)
- `artifacts/presentation-marp.html` - HTML presentation (generated, not in git)
- `artifacts/presentation-marp.pdf` - PDF export (generated, not in git)
- `docs/PRESENTATION-FINAL-WORKFLOW.md` - Complete workflow guide

**Key features:**
- CSS styling in YAML frontmatter (blue theme, table headers, takeaway boxes)
- 1-second regeneration (`make marp`)
- Works in any browser (Firefox, Chrome, Edge)
- Keyboard navigation (Arrow keys, Space, F11 for fullscreen)
- Version controlled source (only .md in git)

**Alternative: Pandoc PPTX (legacy)**

For PPTX output (not recommended - quality issues, not editable):

```bash
make pptx           # Generate PPTX from Markdown (Pandoc)
make pptx-pdf       # Export PPTX to PDF (requires LibreOffice)
```

### Interview Format
- **Duration:** 90 minutes total
- **Presentation:** 30 minutes
- **Q&A:** 15 minutes
- **Format:** HDMI projection (PDF/PPT sent 24hrs prior)

### Build Structure & Dependencies

**Slash Command Reference:**
```
[/req-yaml-to-md]  # Generate human-readable requirements report (32KB, comprehensive)
    ├─ source
    │   └── source/requirements.yaml
    └─ target
        └── artifacts/requirements.md

[/req-yaml-to-cheatsheet]  # Generate lean requirements cheat sheet (<5KB, quick reference)
    ├─ source
    │   ├── source/requirements.yaml
    │   └── source/requirements-policy.md (category codes table)
    └─ target
        └── artifacts/requirements-cheat-sheet.md

[/req-audit]  # Validate SMART compliance
    ├─ source
    │   ├── source/requirements.yaml
    │   └── docs/requirements-policy.md
    └─ target
        └── artifacts/rubric-reports/req-audit-report.md

[/req-trace]  # Generate requirement → architecture traceability matrix
    ├─ source
    │   ├── source/requirements.yaml
    │   └── source/architectures.yaml
    └─ target
        └── artifacts/rubric-reports/req-traceability-report.md

[/req-risk-report]  # Risk-rank assumptions
    ├─ source
    │   └── source/requirements.yaml
    └─ target
        └── artifacts/rubric-reports/assumption-risk-report.md

[/arch-gen]  # Generate architecture documentation, BOMs, and trade-off charts
    ├─ source (SSOT - Single Source of Truth)
    │   ├── source/parts.csv (29 parts: Digikey PNs, costs, leadtimes, ROHS)
    │   ├── source/subsystems.yaml (19 core + 15 unique subsystems with specs)
    │   ├── source/architectures.yaml (3 architectures: PIEZO_ECO, SOL_ECO, PIEZO_DLX)
    │   └── source/decision-logic.yaml (decision tree rules for architecture selection)
    ├─ pipeline
    │   ├── scripts/generate_arch_artifacts.py (YAML → MD + CSV)
    │   ├── scripts/extract_tradeoff_data.py (YAML + CSV → JSON)
    │   ├── scripts/plot_tradeoff_charts.py (JSON → PNG charts)
    │   └── scripts/generate_subsystem_comparison_table.py (YAML → PNG table)
    ├─ intermediate
    │   └── data/tradeoff-data.json (extracted metrics for plotting)
    └─ target
        ├── artifacts/architecture.md (technical reference: subsystems, specs, BOMs)
        ├── artifacts/bom/arch-piezo-eco-bom.csv ($345.26 - wired, USB-powered)
        ├── artifacts/bom/arch-sol-eco-bom.csv ($240.75 - wired, AA batteries)
        ├── artifacts/bom/arch-piezo-dlx-bom.csv ($364.17 - BLE wireless, Li-ion)
        ├── artifacts/architecture-comparison-matrix.md (quantitative tables)
        ├── resources/diagrams/architecture-cost-comparison.png (stacked cost bars)
        ├── resources/diagrams/architecture-timeline-comparison.png (stacked timeline)
        ├── resources/diagrams/architecture-radar-comparison.png (8-dimension spider)
        ├── resources/diagrams/architecture-decision-tree.png (selection logic)
        └── resources/diagrams/subsystem-comparison-table.png (BLE/Power/Actuator)
    Data flow: parts.csv (SSOT) → BOM CSV → extract → JSON → plot → charts
    Note: All cost actuals derive from parts.csv (Unit_Price_1000 column)

[/rubric-eval]  # Evaluate phase against interview rubric (0-100 pts)
    ├─ source
    │   ├── docs/architecture.md
    │   ├── docs/quality-metrics.md
    │   ├── docs/interview-rubric.md
    │   ├── docs/tradeoff-analysis-guide.md
    │   ├── docs/market-braille-display-scan.md
    │   ├── docs/actuator-technology-tradeoff.md
    │   ├── docs/power-budget-analysis.md
    │   ├── docs/cots-timeline-analysis.md
    │   ├── artifacts/requirements.md
    │   ├── artifacts/rubric-reports/req-audit-report.md
    │   ├── artifacts/rubric-reports/req-traceability-report.md
    │   └── artifacts/rubric-reports/assumption-risk-report.md
    └─ target
        └── artifacts/rubric-reports/v1.X.0-*-eval.md (v0.1.0, v1.2.0, v1.3.0 exist)

[/status]  # Display time tracking & project progress
    ├─ source
    │   ├── TIME-LOG.md
    │   └── TODO.md
    └─ target
        └── console output (time summary, on-track status, focus recommendations)

[/phase-complete]  # Finish phase: validate, log time, update docs, commit & push
    ├─ source
    │   ├── TODO.md
    │   └── TIME-LOG.md
    └─ target
        ├── TODO.md (colors: blue→green, next red→blue)
        ├── TIME-LOG.md (append entry + update summary stats)
        ├── README.md (version, directory tree, dependencies)
        └── git commit + push to main

[make all]  # Convert all .md → .pdf (pandoc + xelatex)
    ├─ source
    │   ├── docs/*.md (22 files)
    │   ├── artifacts/*.md (5 files)
    │   └── artifacts/rubric-reports/*.md (6 files)
    └─ target
        └── artifacts/*.pdf (same basenames as .md files)
```

### Self-Evaluation

**Rubric:** `docs/interview-rubric.md` (100-point scale based on Lam's 4 criteria)

**Run evaluation after each phase:**
```bash
/rubric-eval  # Generates artifacts/rubric-reports/vX.X.0-*-eval.md
```

**Evaluation Criteria:**
1. Technical Requirements Identification (25 pts)
2. Alternative Solution Development (25 pts)
3. Solution Evaluation & Trade-off Analysis (30 pts)
4. Path to Production (20 pts)
