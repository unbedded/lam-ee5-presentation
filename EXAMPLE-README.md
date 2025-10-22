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

---

## Post-Interview Lessons Learned

**Interview Stats:**
- **Duration:** 7 hours
- **Format:** Technical deep-dive + whiteboard + Q&A
- **Result:** 80% chance of offer, no other candidates under consideration
- **Overall Feedback:** Presentation was well-received, strong technical depth

### What Worked ✅

1. **Technical Depth & Accuracy**
   - Detailed power analysis (PIEZO vs SOLENOID calculations)
   - Realistic BOM sourcing (actual Digikey part numbers, not estimates)
   - EMI physics derivations (slew-rate limiting, sequential firing)
   - Trade-off framework (8 dimensions: cost, timeline, UX, manufacturability)

2. **Requirements Rigor**
   - 17 SMART requirements with acceptance criteria
   - Assumption risk ranking (6 assumptions documented)
   - Traceability matrix (requirements → architectures)
   - Standards compliance (ADA 703.3, FCC Part 15B, UL)

3. **AI Transparency**
   - Disclosed AI usage upfront: "I used Claude Code + 500 lines of Python to generate BOMs and manage requirements database"
   - Showed automation: requirements.yaml → Markdown → PDF pipeline
   - Demonstrated AI as force multiplier, not replacement for engineering judgment

4. **Verification Discipline**
   - Caught AI math errors (10% → 33% dot change rate, piezo power confusion)
   - Cross-checked all calculations in speaker notes
   - Validated BOMs against actual Digikey pricing

### What to Improve ❌

#### 1. **Timeline Messaging (Major Miss)**
**Problem:** Focused too much on "2-month timeline doesn't work" without providing the alternative.

**Better Approach:**
- "2 months is aspirational for pilot production. Here's the realistic 12-week plan:"
  - Week 0-2: Requirements clarification + actuator sourcing
  - Week 3-4: Detailed design (schematic, PCB, BOM lock)
  - Week 5-6: Prototype build (10 boards, bring-up, debug)
  - Week 7-9: Pilot production (50-100 units, yield analysis)
  - Week 10-12: Validation testing (functional, EMI, user)
- Don't just say "it doesn't work" - give the **realistic path forward**

**Action:** Move timeline slide from BACKUP to MAIN deck

#### 2. **Missing "Pick a Winner" Slide (Critical)**
**Problem:** Presented 3 architectures with trade-offs but didn't make a recommendation.

**What They Wanted:**
- "If we had to commit TODAY, I recommend **PIEZO_ECO** because:"
  - Proven technology (100% of commercial displays use piezo)
  - Lowest technical risk (no cam mechanism)
  - 5.8× better power efficiency than solenoid (0.22W vs 1.27W)
  - Trade-off: Higher cost ($868 vs $536), but faster to pilot
- Then: "However, if wireless is mandatory → PIEZO_DLX. If cost is critical → SOL_ECO."

**Action:** Add explicit "RECOMMENDATION" slide with reasoning

#### 3. **Forgot Backup Slides During Q&A**
**Problem:** FTE/NRE resource plan existed in backup slides, but I forgot to reference it when asked.

**Root Cause:** AI generated the slide, I didn't internalize the content.

**Fix:**
- If AI generates content, you MUST review and **own it**
- Practice Q&A: "What resources do you need?" → "See backup slide 28: 2.5 FTE, $75-110K NRE"
- Print backup slide index on note cards

**Action:** Move FTE/NRE to MAIN deck (not backup)

#### 4. **Didn't Explain AI Workflow Visually**
**Problem:** Said "I used AI and 500 lines of code" but interviewers had no context for what that means.

**Better Approach:** Half-slide visual showing:
```
Human Input              AI Assistant           Human Verification
────────────            ──────────────         ──────────────────
Define requirements  →  Generate BOMs      →   Validate pricing
  (YAML SSOT)           (3 architectures)      (Digikey actual)
                     →  Create charts      →   Check math
Write policies       →  Draft slides       →   Rewrite for accuracy
  (SMART criteria)      (speaker notes)        (catch 10%→33% error)
```

**Key Message:** "AI is my drafting tool, not my thinking replacement. I verify everything."

**Action:** Add "AI Workflow" slide to appendix

#### 5. **Role Confusion: EE vs EE+PM**
**Problem:** Presented as "Electrical Engineer" but they wanted "EE Lead who owns the entire project."

**What They Expected:**
- Not: "I design circuits, someone else manages schedule"
- But: "I own end-to-end: design + team + schedule + budget + risk"
- Program Director = VP-level strategy, NOT day-to-day PM
- You ARE the project manager for this pilot

**Action:** Frame future presentations as "EE Lead + PM" role

### Discoveries During Interview

#### COTS Piezo Pin Found
- **What:** There IS a COTS piezo pin with simple driver available
- **Impact:** Invalidates "no COTS actuators exist" assumption
- **Lesson:** Even exhaustive searches can miss parts (especially niche actuator market)
- **Fix:** Always caveat: "No COTS found in my search, but actuator market is fragmented"

#### Timeline Reality Check
- Unanimous agreement: 2-month pilot is unrealistic for custom actuators
- 8-12 weeks is honest engineering estimate
- Don't apologize for reality - own it and provide the path

### AI Usage Philosophy: "Not-Trust, Always Verify"

**What Worked:**
- AI as **drafting tool**: Generate initial BOMs, speaker notes, calculations
- Human as **verification**: Check math, validate assumptions, cross-reference sources
- Iterative refinement: Ask AI "Is 10% dots change realistic?" → Update to 33%

**Pitfalls Avoided:**
- AI gets simple math wrong (power calculations, percentage rates)
- AI hallucinates part numbers (always cross-check Digikey)
- AI over-optimizes (10% change rate was too optimistic)

**The Discipline:**
1. **AI generates** → 2. **Human questions** → 3. **AI refines** → 4. **Human validates**

**Quote:** "A bad carpenter blames his tools. AI is a superpower, but only if you stay curious and ask questions. Don't trust - verify."

### Interview Preparation Experiment

**Hypothesis:** What can a Senior EE accomplish with Claude Code in 14 days (84 hours)?

**Results:**
- ✅ 17 SMART requirements documented
- ✅ 3 complete architectures with real BOMs
- ✅ 500+ lines of automation (YAML → Markdown → PDF)
- ✅ Marp presentation with 40+ slides
- ✅ Power analysis, EMI calculations, timeline planning
- ✅ Resource plan (FTE, NRE, validation strategy)

**Time Saved:** Estimated 3-4 weeks of manual work compressed to 2 weeks with AI assistance

**Key Learning:** AI accelerates **breadth** (generate BOMs, requirements matrix, charts) so human can focus on **depth** (validate physics, catch errors, make decisions)

### Recommended Changes for Future Use

**Main Deck Additions:**
1. **Slide 5:** "RECOMMENDATION: Pick a Winner" (after trade-off analysis)
2. **Slide 6:** "Realistic Timeline: 12-Week Plan" (move from backup)
3. **Slide 7:** "Resource Plan: FTE & NRE" (move from backup)

**Backup Additions:**
4. **Backup Slide:** "AI-Assisted Workflow" (transparency visual)

**Speaker Notes:**
- Add "See backup slide X" reminders for common Q&A topics
- Internalize ALL backup content (don't let AI-generated slides become black boxes)

---

## AI-Assisted Slide Workflow (Retrospective)

This section documents the actual workflow used to create the Marp presentation with Claude Code assistance.

### Workflow Overview

```
┌─────────────────┐
│ Human defines   │
│ requirements    │ → source/requirements.yaml (SSOT)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ AI generates    │
│ artifacts       │ → /req-yaml-to-md → artifacts/requirements.md
└────────┬────────┘   /arch-gen → artifacts/bom/*.csv
         │            scripts/generate_tradeoff_charts.py → charts
         ▼
┌─────────────────┐
│ Human validates │
│ & corrects      │ → Check BOMs against Digikey
└────────┬────────┘   Verify power calculations
         │            Catch AI math errors (10%→33%)
         ▼
┌─────────────────┐
│ AI drafts       │
│ slides          │ → source/presentation-marp.md (Markdown)
└────────┬────────┘   speaker notes, tables, technical content
         │
         ▼
┌─────────────────┐
│ Human rewrites  │
│ for accuracy    │ → Correct piezo power: 0.43W → 0.22W
└────────┬────────┘   Update solenoid: 0.38W → 1.27W
         │            Add "TOTAL POWER Per dot" clarity
         ▼
┌─────────────────┐
│ make marp       │
│ (1-sec rebuild) │ → artifacts/presentation-marp.html
└─────────────────┘   artifacts/presentation-marp.pdf
```

### Step-by-Step Process

#### Phase 1: Requirements Definition (Human-Led)
**Tools:** Text editor, YAML
**Time:** ~6 hours

1. Read interview PDF (pages 9-10: "EE Concept Evaluation")
2. Extract 9 ground-truth requirements (PRD-SCHED-001, PRD-SIZE-001, etc.)
3. Derive 6 assumption requirements (pilot production, BOM cost, power budget)
4. Write `source/requirements.yaml` with SMART structure:
   ```yaml
   - id: PRD-FUNC-001
     title: "Single Line Braille Display - 32 characters, 6 dots each"
     source: "PDF p.9 Scope Item 2"
     priority: "P0-Critical"
     acceptance_criteria:
       - "32 braille cells arranged horizontally"
       - "Each cell: 6 dots (2×3 matrix)"
       - "Total: 192 independently-controlled actuators"
   ```

**AI Role:** Minimal - just YAML syntax validation

#### Phase 2: Architecture & BOM Generation (AI-Assisted)
**Tools:** Claude Code, Python scripts, YAML
**Time:** ~12 hours (would be 3-4 weeks manual)

1. **Human defines architectures in YAML:**
   ```yaml
   architectures:
     - id: ARCH_PIEZO_ECO
       actuator_type: "Piezo Bimorph"
       communication: "USB-C Wired"
       subsystems: [SS-ACTUATOR-PIEZO, SS-COMM-USB, ...]
   ```

2. **AI generates BOMs via `/arch-gen`:**
   - Reads `source/parts.csv` (29 parts with Digikey PNs)
   - Reads `source/subsystems.yaml` (19 subsystems with specs)
   - Maps architectures → subsystems → parts → BOM CSV
   - Output: `artifacts/bom/arch-piezo-eco-bom.csv` ($868 total)

3. **Human validates pricing:**
   - Cross-check Digikey part numbers (STM32F407VGT6, nRF52840, etc.)
   - Verify volume pricing (1K+ units)
   - Catch AI errors: Initial BOM had wrong STM32 variant ($8 → $12)

4. **AI generates trade-off charts:**
   ```bash
   python3 scripts/extract_tradeoff_data.py  # YAML+CSV → JSON
   python3 scripts/plot_tradeoff_charts.py   # JSON → PNG charts
   ```
   - Output: spider chart, cost bars, timeline comparison

**AI Role:** High automation (BOM generation, chart plotting)
**Human Role:** Validation, error correction, design decisions

#### Phase 3: Slide Content Drafting (AI-Heavy)
**Tools:** Claude Code, Marp Markdown
**Time:** ~8 hours

1. **Human provides slide outline:**
   ```
   Slide 1: Title
   Slide 2: Agenda
   Slide 3: Requirements (ground truth)
   Slide 4: ADA 703.3 mechanical specs
   Slide 5: Actuator technology comparison
   ...
   ```

2. **AI drafts Markdown slides:**
   ```markdown
   # Power Per Actuator: Actuation and Hold

   | Phase | Parameter | PIEZO | SOLENOID |
   |-------|-----------|-------|----------|
   | ACTUATION | Energy/pulse | 250 µJ | 120 mJ |
   | HOLD | Refresh rate | 45 Hz | 0 Hz |
   ```

3. **AI generates speaker notes:**
   - Technical explanations (i=C×dV/dt derivation)
   - Calculation step-by-step math
   - Key talking points

**Critical Error Example:**
- AI initially calculated solenoid realistic power as 0.38W (10% dot change)
- Human questioned: "Is 10% dot change realistic for braille text?"
- AI refined: 33% is more realistic (typical English letter transitions)
- Human corrected: 0.38W → 1.27W
- **Lesson:** AI over-optimizes without domain knowledge

#### Phase 4: Math Verification (Human-Critical)
**Tools:** Calculator, whiteboard, speaker notes
**Time:** ~4 hours

**Example 1: Piezo Power Confusion**
- AI conflated "hold power per dot" with "total power per dot"
- Slide showed 2.25 mW in HOLD section, unclear if this was total
- Human added row: "TOTAL POWER | Per dot (avg) | 2.25 mW"
- **Fix:** Clarity that actuation = hold refresh for piezo

**Example 2: Solenoid Change Rate**
- AI assumed 10% dots change per line (too optimistic)
- Human calculated: 33% realistic (consecutive English lines)
- Recalculated power: 192 × 33% × 120mJ / 6s = 1.27W
- Updated slide: 0.38W → 1.27W

**Example 3: Power Budget Rollup**
- AI showed piezo "Avg power (realistic)" as 0.43W
- But this assumed 100% dots asserted, not 50%
- Human corrected: 192 × 50% × 2.25mW = 0.22W
- **Key insight:** Piezo = f(dots ASSERTED), Solenoid = f(dots CHANGED)

**Verification Process:**
1. Read AI-generated calculation in speaker notes
2. Work it out independently on whiteboard
3. If mismatch → question AI → iterate → validate
4. Add "SHOW YOUR WORK" math to speaker notes

#### Phase 5: Iterative Refinement (Human-Led)
**Tools:** Marp, `make marp` (1-second rebuild)
**Time:** ~6 hours

1. **Present to yourself (dry run):**
   - Read slides aloud, time each section
   - Notice confusing wording, awkward tables
   - Flag slides that need backup content

2. **Refine with AI:**
   - "This table is too dense - split into 2 slides"
   - "Move FTE/NRE to main deck, not backup"
   - "Add 'TOTAL POWER Per dot' row for clarity"

3. **Rebuild instantly:**
   ```bash
   vim source/presentation-marp.md
   make marp  # 1 second
   firefox artifacts/presentation-marp.html
   ```

4. **Iterate until flow is smooth:**
   - 30-minute target (achieved: 28 minutes)
   - Smooth transitions between sections
   - No jargon without definitions

### Tools & Technologies Used

**Single Source of Truth (SSOT):**
- `source/requirements.yaml` - All requirements (470 lines)
- `source/architectures.yaml` - 3 architectures (280 lines)
- `source/parts.csv` - 29 parts with Digikey PNs
- `source/subsystems.yaml` - 19 subsystems (350 lines)

**Automation Pipeline:**
- Python scripts: 500+ lines of code
- Slash commands: `/req-yaml-to-md`, `/arch-gen`, `/rubric-eval`
- Makefile: `make marp` (Marp CLI)

**AI Assistance:**
- Claude Code (Sonnet 4.5)
- Used for: BOM generation, chart plotting, slide drafting, speaker notes
- NOT used for: Design decisions, math validation, requirement prioritization

**Version Control:**
- Git + GitHub
- 47 commits over 14 days
- Semantic versioning (v0.1.0 → v1.3.0)

### Time Breakdown

| Phase | Task | Human Time | AI Time | Total |
|-------|------|------------|---------|-------|
| 1 | Requirements definition (YAML) | 6h | 0.5h | 6.5h |
| 2 | Architecture & BOM generation | 4h | 8h | 12h |
| 3 | Slide content drafting | 2h | 6h | 8h |
| 4 | Math verification & correction | 4h | 1h | 5h |
| 5 | Iterative refinement | 6h | 2h | 8h |
| **Total** | | **22h** | **17.5h** | **39.5h** |

**Traditional Approach (estimated):** 60-80 hours for equivalent output

**AI Productivity Gain:** 1.5-2× faster (39.5h vs 60-80h)

### Key Principles for AI-Assisted Technical Work

1. **Human Defines Strategy, AI Executes Tactics**
   - You pick architectures (PIEZO vs SOLENOID)
   - AI generates BOMs, charts, calculations
   - You validate and correct

2. **Never Trust, Always Verify**
   - AI math errors are common (10% → 33%, 0.38W → 1.27W)
   - Cross-check against primary sources (datasheets, standards)
   - Work calculations independently before accepting AI results

3. **Iterate Quickly, Validate Slowly**
   - Use AI for fast iteration (`make marp` = 1 second)
   - Spend time on validation (whiteboard math, dry runs)
   - Don't let speed compromise accuracy

4. **Document AI Usage Transparently**
   - Disclose: "I used Claude Code + 500 lines of Python"
   - Explain: "AI drafted, I validated"
   - Show: "Here's where I caught AI errors"

5. **Own the Content**
   - If AI generates backup slides (FTE/NRE), internalize them
   - Don't let AI-generated content become a black box
   - Practice Q&A for every slide (main + backup)

### What AI Did Well

✅ **BOM Generation:** Mapped 3 architectures × 19 subsystems × 29 parts = 3 BOMs in minutes
✅ **Chart Plotting:** Spider charts, cost bars, timeline stacks (would take hours in Excel)
✅ **Speaker Notes:** Technical derivations (i=C×dV/dt, EMI field strength)
✅ **Iteration Speed:** 1-second slide rebuild enabled rapid refinement
✅ **Requirements Matrix:** Generated traceability report (17 requirements → 3 architectures)

### What AI Struggled With

❌ **Domain Knowledge:** Assumed 10% dot change rate (too optimistic for braille)
❌ **Math Verification:** Power calculations had errors (0.38W → 1.27W)
❌ **Design Judgment:** Couldn't "pick a winner" - needed human prioritization
❌ **Cost Sourcing:** Hallucinated part numbers (always cross-check Digikey)
❌ **Presentation Strategy:** Generated backup slides but didn't flag importance (FTE/NRE should be main)

### The "Not-Trust, Always Verify" Workflow

```
┌──────────────────────────────────────────────────────────┐
│  AI GENERATES                                            │
│  ├─ Power calculation: "Solenoid realistic = 0.38W"     │
│  ├─ Assumption: 10% dots change per line                │
│  └─ Speaker notes: P = (192 × 0.10 × 120mJ) / 6s       │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  HUMAN QUESTIONS                                         │
│  ├─ "Is 10% dots change realistic for braille?"         │
│  ├─ "What's the actual letter frequency in English?"    │
│  └─ "How correlated are consecutive braille lines?"     │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  AI REFINES                                              │
│  ├─ "33% is more realistic (consecutive lines differ)"  │
│  ├─ Recalculates: (192 × 0.33 × 120mJ) / 6s = 1.27W    │
│  └─ Updates slide: 0.38W → 1.27W                        │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│  HUMAN VALIDATES                                         │
│  ├─ Whiteboard check: 192 × 0.33 × 0.120 / 6 = 1.267W ✓│
│  ├─ Cross-reference: Typical braille density = 50% dots │
│  └─ Update speaker notes with detailed derivation       │
└──────────────────────────────────────────────────────────┘
```

**Key Insight:** The questioning phase is what separates senior engineers from juniors. Stay curious, don't rush to solutions.

---

**Project Status:** ✅ Interview Complete (October 23, 2025)
**Outcome:** 80% chance of offer, no other candidates
**AI Experiment:** Success - 1.5-2× productivity gain with rigorous verification
