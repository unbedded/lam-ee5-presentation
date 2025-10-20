# Lam Research EE Interview - Project TODO

## 📊 REALISTIC PROJECT STATUS (Updated Oct 18, 2025)

**Interview:** Oct 21, 2025 (Tuesday) - **3 DAYS AWAY** ⚠️

**AI Workflow Focus (this TODO):** Track remaining presentation refinement tasks
**Human Prep Focus (separate doc):** See `docs/interview-prep-checklist.md` for Q&A, delivery coaching, practice workflow

---

**✅ PHASE 1 COMPLETE: Technical Analysis (v1.0.0)**
- Requirements Analysis: 17 requirements (9 ground truth + 6 assumptions + 2 standards) ✅
- Architecture Development: 3 viable architectures (SOL_ECO $506, PIEZO_ECO $592, PIEZO_DLX $606) ✅
- Trade-off Analysis: EMI analysis, cost comparison, decision framework ✅
- Production Plan: 8-week pilot timeline, success criteria defined ✅

**✅ PHASE 2 COMPLETE: Presentation Development (v2.0.0 - v2.3.0)**
- 34 slides with speaker notes, CSS styling, takeaway messages ✅
- Content condensed (Summary + Q&A combined, 3 slides moved to backup) ✅
- Committed to git (5c4162f) ✅

**🔵 PHASE 3 IN PROGRESS: Practice & Final Delivery (v2.4.0 - v3.0.0)**

**Remaining Work (4-6h over 3 days):**
1. ⏳ Practice runs (Oct 18-20) - 3+ full runs, timing checkpoints, Q&A prep
2. ⏳ Generate final PDF (Oct 20) - export from HTML, verify renders correctly
3. ⏳ Email to Nathan Briggs (Oct 20 EOD) - CRITICAL DEADLINE

**Key Files Ready:**
- ✅ source/presentation-marp.md (34 slides, final version committed)
- ✅ artifacts/presentation-marp.html (regenerates in 1 second with `make marp`)
- ✅ source/practice-guide.md (comprehensive practice guide with ChatGPT voice coaching)
- ✅ artifacts/practice-guide.pdf (run `make practice` to regenerate)
- ✅ docs/actuator-emi-design-analysis.md (46 KB technical deep-dive)
- ✅ artifacts/bom/*.csv (3 architectures with EMI components)
- ✅ artifacts/architecture.md (auto-generated from YAML)

**Practice Focus (see artifacts/PRACTICE-GUIDE.md):**
- Oct 18: Run 1-2 (baseline + high-priority sections)
- Oct 19: Run 3-4 (full timed + Q&A scenarios)
- Oct 20: Run 5 (final dress rehearsal) + PDF generation + email delivery

---

## <span style="color:green">v0.1.0: Project Setup (feature/project-init)</span>
- [x] Create directory structure
- [x] Create README.md
- [x] Create recruiter contact info reference
- [x] Create docs/problem-statement.md (EE Concept Evaluation challenge)
- [x] Create docs/requirements-policy.md (naming conventions, traceability rules)
- [x] Create docs/interview-rubric.md (maps to Lam's 4 criteria from PDF p.10)
- [x] Create .claude/commands/rubric-eval.md (AI-driven evaluation workflow)
- [x] Move source/requirements.yaml to proper location (single source of truth)
- [x] Setup GitHub repository for project
  - [x] Initialize git repo (git init)
  - [x] Create .gitignore (exclude artifacts/, .DS_Store, etc.)
  - [x] Create GitHub repo (public or private)
  - [x] Add remote origin
  - [x] Initial commit and push
  - [x] Setup branch protection rules (deferred - not needed for solo project)
- [x] Add other Lam contacts to reference/interview/contact-info.md (added all 10 panel members)
- [x] Create Makefile for PDF generation (auto-discovers artifacts/*.md and source/*.md)
- [x] Copy LaTeX style files (table-style.tex already in style/ directory, PDFs rendering correctly)

### Phase Gate: v0.1.0 → v1.0.0
- [x] All project setup tasks complete (core tasks done, LaTeX styles optional)
- [x] GitHub repo initialized and pushed
- [x] Build system functional (Makefile can generate PDFs)
- [x] Directory structure verified (4-rule system - documented in README.md)
- [x] Slash commands tested and working (/rubric-eval, /status)

---

## <span style="color:green">v1.0.0: Technical Analysis (feature/tech-analysis)</span>

### <span style="color:green">v1.1.0: Quality Metrics Definition (feature/tech-analysis-metrics)</span>
- [x] Review and refine requirements management procedure
  - Reviewed docs/requirements-policy.md (solid - SMART criteria, traceability, naming conventions)
  - Validated YAML structure in source/requirements.yaml (17 requirements, properly formatted)
  - Note: Slash commands (/req-audit, /req-yaml-to-md, /req-trace) moved to v1.2.0 creation
- [x] Create docs/quality-metrics.md
  - Defined requirements completeness criteria (15-20 SMART requirements)
  - Defined solution diversity targets (3+ architectures)
  - Defined quantitative analysis standards (BOM, power, timeline)
  - Defined risk identification thoroughness (likelihood × impact matrix)
  - Defined phase gate criteria (80% per category, 85+ overall)

### <span style="color:green">v1.2.0: Requirements Analysis (feature/tech-analysis-requirements)</span>
**Design Plan Alignment:** Complete Design Step 1 (PDF p.10) - 25/100 points
**Rubric Score:** 24/25 (Requirements) + 10/10 (Documentation) = 34/35 points (97%)

- [x] Renamed problem-statement.md → design-plan.md (per hiring manager: "READ THIS CAREFULLY")
- [x] Created docs/todo-design-plan-mapping.md (harmonize TODO with 4-step design scope)
- [x] Create .claude/commands/req-audit.md (req compliance checker)
- [x] Create .claude/commands/req-yaml-to-md.md (YAML→MD generator, outputs to artifacts/)
- [x] Create .claude/commands/req-trace.md (traceability matrix generator)
- [x] Create .claude/commands/req-risk-report.md (risk-ranked assumption report generator)
- [x] Create docs/presentation-plan.md (strategic presentation plan - "begin with end in mind")
- [x] Create docs/presentation-key-messages.md (systems engineering philosophy slide)
- [x] Create docs/requirements-philosophy-alignment.md (req structure → presentation thesis)
- [x] Updated scope/assumptions in requirements.yaml (pilot production strategy)
- [x] MAJOR REFACTOR: Hierarchical PRD naming (v2.0.0)
  - 9 ground truth requirements (PRD-XXXX-NNN) verbatim from PDF
  - 6 assumptions (PRD-XXXX-NNN-ASMP) with derivation process, risk levels
  - Generated artifacts/requirements.md (34KB professional report)
  - Generated artifacts/assumption-risk-report.md (risk-ranked analysis)
- [x] Add hierarchical ASCII tree to requirements.md with hyperlinks
- [x] Update /req-yaml-to-md to include tree + ground truth/assumptions sections
- [x] Create Makefile req transform targets (make req-md, req-trace, req-audit, req-risk, req-all, req-clean)
- [x] Update /req-trace for hierarchical PRD naming (PRD-XXXX-NNN → PRD-XXXX-NNN-ASMP)
- [x] Run /req-audit to validate compliance (93% SMART, CONDITIONAL PASS)
- [x] Add actuator size constraint (≤2.3mm) to PRD-FUNC-001 and PRD-FUNC-003
- [x] Add NFR-STD-001 (UL/FCC) and NFR-STD-002 (ADA) standards requirements
- [x] Regenerate requirements.md with 17 requirements (9 ground truth + 6 assumptions + 2 standards)
- [x] Review generated requirements.md for completeness (32KB, compact header tables)
- [x] Run /rubric-eval for Category 1 assessment (Technical Requirements: 24/25 pts - Excellent)
  - Generated artifacts/rubric-reports/v1.2.0-requirements-eval.md (24/25 + 10/10 doc = 34/35 total)
  - Generated artifacts/rubric-reports/req-audit-report.md (93% SMART compliance)
  - Generated artifacts/rubric-reports/req-traceability-report.md (100% analysis traced)
  - Generated artifacts/rubric-reports/assumption-risk-report.md (6 assumptions risk-ranked)
- [x] Phase gate: Freeze requirements.yaml before v1.3.0 (architecture design)
  - Committed to git: ba286f4 "feat(v1.2.0): Complete Requirements Analysis phase"
  - Gate Decision: ✅ READY for v1.3.0 (Architecture Development)

### <span style="color:green">v1.3.0: Solution Architecture Development (feature/tech-analysis-architecture)</span>
**Design Plan Alignment:** Complete Design Step 2 (PDF p.10) - 25/100 points
**Rubric Score:** 24/25 (Alternative Solutions) = 96% - Excellent
**Status:** COMPLETE - 5h logged (of 12h est)

**✅ CHECKPOINT COMPLETE (2025-10-15): EMI Requirements Validation**

**Final Status:**
- [x] Added EMI requirements to requirements.yaml (NFR-STD-001 family + NFR-EMI-001)
- [x] Added SS-EMI-BULK-CAP and SS-EMI-BYPASS-CAP to parts.csv
- [x] Added EMI subsystems to subsystems.yaml with PCB specs
- [x] Added EMI subsystems to all 3 architectures in architectures.yaml
- [x] Regenerated BOMs with EMI components ($2-3 per unit, <1% increase)
- [x] /req-yaml-to-md validated (requirements.md v2.3.0 up-to-date)
- [x] /req-audit completed (PASS - 92% SMART, 0 critical issues)
- [x] /req-trace completed (PASS - 100% reference integrity)
- [x] Validation reports generated (artifacts/rubric-reports/, gitignored)

**Validation Results:**
- Requirements database: v2.3.0, 37 requirements, production-ready ✅
- Audit status: PASS (34/37 fully SMART, v2.3.0 critical issue resolved)
- Traceability: PASS (7 strategic drivers traced, 30 cross-cutting implicit)
- Standards coverage: EXCELLENT (UL, FCC, ADA, ISO)

**Key Decisions:**
- User approved "ballpark pricing" (qty=24 for all archs, ~$2 overcost for ARCH_SOL_ECO acceptable)
- Low-risk EMI design: 1000µF bulk + 100nF bypass per driver IC (>6dB margin to FCC Part 15B)
- Cost-down optimization documented in Technical-Debt section (post-pilot)
- All source files updated, waiting for artifacts/requirements.md regeneration to complete

**Modified Files (need git commit):**
- source/requirements.yaml (+5 requirements)
- source/parts.csv (+2 EMI components)
- source/subsystems.yaml (+2 EMI subsystems)
- source/architectures.yaml (+EMI subsystems to 3 archs)
- artifacts/bom/*.csv (regenerated)
- TODO.md (this checkpoint)

**PDF Quote:** "Develop and describe **multiple alternative solutions**"

- [x] **Market scan: Identify what solutions currently exist**
  - [x] Search for existing braille displays (commercial products) - docs/market-braille-display-scan.md
  - [x] Identify technology types used (piezo monopoly - 100% of commercial products)
  - [x] Note price points (Orbit Reader $449, BrailleMe $515, Brailliant $1200+)
  - [x] Capture key specs (refresh rate, power, size, connectivity, actuator voltage)
  - [x] Document findings: docs/market-braille-display-scan.md (15KB)
  - **Key finding:** NO COTS piezo at 2-3mm, all use 200V custom (8-12 wk lead time)
- [x] Research braille actuator technologies (EXTENSIVE analysis)
  - [x] Piezoelectric actuators (pros/cons, power, cost) - docs/actuator-technology-tradeoff.md
  - [x] Solenoid-based systems (pros/cons, power, cost, mechanical latch concept)
  - [x] Shape memory alloy (SMA) (too slow 700-1500ms, ruled out)
  - [x] Voice coil actuators (high hold power, ruled out)
  - [x] MEMS electrostatic (insufficient stroke, ruled out)
  - [x] Piezo voltage options (200V standard, skipped 100V exploration per user decision)
  - [x] Mechanical latch concept - docs/actuator-mechanical-latch-concept.md (11KB)
  - [x] Power budget analysis - docs/power-budget-analysis.md (15KB)
  - [x] COTS timeline analysis - docs/cots-timeline-analysis.md
- [x] **Added critical requirements (derived from analysis):**
  - [x] PRD-SCHED-002-ASMP: COTS component mandate (≤4 week lead time)
  - [x] PRD-POWER-003/004/005-ASMP: Power budgets (USB/AA/Li-ion)
  - [x] PRD-FUNC-005/006-ASMP: Reading speed and usage profiles
  - [x] PRD-FUNC-003-ARCH-C-EXCEPT: Size exception for ARCH-D (4mm solenoid, 3.5mm pitch)
  - [x] Corrected ADA 703.3 spacing spec (6.2mm not 6.0mm center-to-center)
  - **Total requirements: 24** (9 ground truth + 13 assumptions + 2 standards)
- [x] **Created architecture database (4 architectures):**
  - [x] source/architectures.yaml: ARCH-A (Li-ion BLE), ARCH-B (USB wired), ARCH-C (AA hybrid piezo), ARCH-D (AA hybrid solenoid+latch)
  - [x] source/subsystems.yaml: 19 subsystems (7 core + 12 unique) with PCB specs
  - [x] source/parts.csv: 23 parts with Digikey PNs, costs, lead times
  - **Architectures:** ARCH-B ($420 BOM), ARCH-C ($436), ARCH-D ($224, 48% savings), ARCH-A ($449)
- [x] Evaluate communication interfaces (comparison table)
  - [x] Bluetooth LE (ARCH-A, ARCH-C, ARCH-D) - nRF52840 pre-certified FCC
  - [x] USB-C (ARCH-B, ARCH-C, ARCH-D) - STM32 built-in USB PHY
  - [x] WiFi (deferred - not needed for phone companion device)
- [x] **Skipped additional architecture variants per user decision:**
  - [x] ARCH-E (offset solenoid + pushrods) - explored, not formalized per user "skip it"
  - [x] 100V piezo variants - skipped per user "stick w/ 200 std is less risk"
- [x] Create docs/architecture.md with 4 distinct solutions (480 lines, comprehensive)
- [x] Run /rubric-eval for Category 2 assessment (Alternative Solutions: 24/25 pts = 96% Excellent)
  - Generated artifacts/rubric-reports/v1.3.0-architecture-eval.md

### Phase Gate: v1.3.0 → v1.4.0
- [x] All architecture tasks complete (4 architectures defined, documented, evaluated)
- [x] Quality metrics met (4 architectures > 3+ target, 24/25 rubric score)
- [x] Quantitative comparison complete (14 metrics per architecture)
- [x] Requirements traceability complete (100% architecture-requirement mapping)
- [x] Supporting analysis thorough (6 docs: market/actuator/voltage/latch/power/COTS)
- **Gate Decision:** ✅ READY for v1.4.0 Trade-off Analysis

### <span style="color:green">v1.4.0: Trade-off Analysis (feature/tech-analysis-tradeoffs)</span>
**Design Plan Alignment:** Complete Design Step 3 (PDF p.10) - 30/100 points ← **HIGHEST WEIGHT**
**Status:** COMPLETE - 5h logged (EMI analysis document IS the trade-off analysis!)

**✅ REALITY CHECK:** EMI analysis (docs/actuator-emi-design-analysis.md, 46KB) covers all trade-off requirements:
- ✅ Advantages & Disadvantages: Solenoid (LOW RISK, $4.32) vs Piezo (HIGH RISK, $10.84)
- ✅ Quantitative Comparison: Cost, schedule, certification risk, EMI mitigation layers
- ✅ Sensitivity Analysis: 3 architectures, decision framework based on priorities
- ✅ "Other Considerations": FCC compliance, antenna physics, firmware-first approach

**⚠️ PDF REQUIREMENT:** "Evaluate the proposed solutions by discussing their **advantages and disadvantages**, as well as **any other considerations** that influenced your final selection."

**Completed Work:**
- [x] EMI analysis document (46KB, 8 parts: fundamentals, solenoid, piezo, comparison, cost, testing, recommendations, implementation)
- [x] EMI executive summary (1-page, triple-duty: quick ref + slide foundation + leave-behind)
- [x] Integrated EMI trade-offs into main presentation (2 slides + 7 appendix slides)
- [x] Cost comparison: $4.32 (solenoid) vs $10.84 (piezo) - quantified 2.5× premium
- [x] Risk quantification: 10% vs 50% fail rate, +0.4 wks vs +2 wks expected rework
- [x] Decision framework: "Depends on YOUR priorities" (cost/timeline/UX trade-offs)

### Phase Gate: v1.4.0 → v1.5.0
- [x] All trade-off analysis tasks complete (EMI analysis covers all requirements)
- [x] Quantitative comparison complete (cost, EMI, risk analysis)
- [x] Decision framework defined (depends on priorities)
- [x] Quality metrics met
- **Gate Decision:** ✅ READY for v1.5.0 Production Process

### <span style="color:green">v1.5.0: Production Transition Process (feature/tech-analysis-production)</span>
**Design Plan Alignment:** Complete Design Step 4 (PDF p.10) - 20/100 points
**Status:** COMPLETE - Production plan integrated into presentation

**Completed Work:**
- [x] 8-week pilot timeline defined in presentation (Phases 1-4)
- [x] Success criteria documented (30N force, 1Hz refresh, 10K cycles MTBF)
- [x] Risk mitigation strategies identified (actuator sourcing critical path)
- [x] $20K NRE budget defined (covers 6 pilot units + tooling)
- [x] Production process outlined in slides 28-33

### Phase Gate: v1.0.0 → v2.0.0
- [x] All technical analysis tasks complete
- [x] Quality metrics met (3 architectures analyzed: ARCH_PIEZO_ECO, ARCH_SOL_ECO, ARCH_PIEZO_DLX)
- [x] Trade-off analysis complete with quantitative data
- [x] Portfolio strategy defined with decision framework
- **Gate Decision:** ✅ READY for v2.0.0 Presentation Development

---

## <span style="color:green">v2.0.0: Presentation Development (feature/presentation)</span>

### <span style="color:green">v2.2.0: Presentation Structure (feature/presentation-structure)</span>

**Status:** COMPLETE - 8h logged (of 6h est, +2h over budget)
**Workflow:** Marp HTML presentation system (source/presentation-marp.md → artifacts/presentation-marp.html)

- [x] Create slide content in source/presentation-marp.md (Markdown with CSS styling)
- [x] Set up Marp CLI workflow: `make marp` (1-second regeneration!)
- [x] Establish blue theme matching title/table headers
- [x] Create takeaway message boxes (blockquote styling)
- [x] Integrate market context and requirements slides
- [x] Fix icon/spacing issues (removed icons, fixed agenda spacing)
- [ ] Slide 1: Title slide (30 sec)
- [ ] Slides 2-3: Problem statement & challenge (2-3 min)
  - 32 chars, 6 dots, 192 control signals
  - Portable, low-cost, high-volume, 2-month timeline
- [ ] Slides 4-6: Requirements summary (3-5 min)
  - Slide 4: Show PDF requirements (verbatim - demonstrate vagueness)
    - Quote PRD-COST-001: "low cost" (no dollar amount)
    - Quote PRD-VOL-001: "high volume" (no quantity)
    - Quote PRD-SIZE-001: "portable" (no dimensions)
  - Slide 5: **⭐ SYSTEMS ENGINEERING PHILOSOPHY (KEY SLIDE)**
    - **Title:** "Systems Engineering: Trade-offs Over Perfection"
    - **Thesis:** Requirements exist in RANGES, not absolutes
    - **Example:** PRD-COST-001-ASMP ($200 ±$100 BOM, not "$200")
    - **Message:** Portfolio approach (3 architectures) vs point design (1 architecture)
    - **Visual:** Trade-off triangle OR Point vs Portfolio comparison
    - **Key phrases:**
      - "Not about 'best power supply with uber-clean output'"
      - "Balance cost/reliability/performance/timeline"
      - "Simplification is innovation (ARCH_PIEZO_ECO wired = simpler than wireless)"
      - "Know when SW replaces HW complexity"
    - **See:** docs/presentation-key-messages.md (complete talking points)
    - **See:** docs/requirements-philosophy-alignment.md (how requirements support this)
  - Slide 6: Assumptions & sensitivity ranges
    - Show PRD-XXXX-NNN-ASMP structure
    - Highlight customer_validation_needed flags
- [ ] Slides 7-12: Solution alternatives presentation (8-10 min)
  - Reference Slide 5 philosophy (portfolio driven by sensitivity ranges)
  - 3 architectures with block diagrams
  - Each architecture optimizes DIFFERENT trade-off:
    - ARCH_PIEZO_ECO: Optimizes simplicity & timeline (wired, standard piezo)
    - ARCH_SOL_ECO: Optimizes mechanical innovation (rotary cam, volume scaling)
    - ARCH_PIEZO_DLX: Optimizes user experience (BLE wireless, premium features)
  - Component selection rationale
  - Pros/cons for each (trace to alternative_scenarios in requirements.yaml)
- [ ] Slides 13-16: Trade-off comparison (5-7 min)
  - Comparison matrix (cost, power, size, complexity, timeline)
  - Quantitative data (power budgets, BOM costs)
  - Risk assessment
- [ ] Slides 17-20: Solution selection framework (5-7 min)
  - **Key message:** "Which architecture wins depends on YOUR constraints"
  - Decision tree: Cost threshold, timeline threshold, feature requirements
  - Example scenarios:
    - "If cost < $400 AND time < 8 weeks → ARCH_PIEZO_ECO"
    - "If wireless required → ARCH_PIEZO_DLX (only option)"
    - "If volume > 10K units → ARCH_SOL_ECO (best scaling)"
  - Detailed block diagrams for each architecture
  - Shared preliminary schematics (power, MCU, drivers)
- [ ] Slides 21-23: Path to production timeline (3-5 min)
  - Week-by-week Gantt chart (8-12 weeks base case)
  - **Critical path: Actuator sourcing (Week 0-2) gates everything**
  - Manufacturing plan (DFM, sourcing, testing)
- [ ] Slide 24: **Actuator Sourcing - THE Critical Path Risk** (2-3 min) ⚠️ NEW
  - **Problem:** No COTS actuators found (2.5mm pitch + force requirements)
  - **Three-path strategy diagram:**
    - Path A: COTS search ($5K, 2 wks, 20% success)
    - Path B: Custom quickturn ($25K-50K NRE, 2-4 wks, 90% success)
    - Path C: Spec relaxation ($0, 0 wks, 100% but violates ADA)
  - **Timeline impact:** +0 to +8 weeks depending on path
  - **Key message:** "All 3 architectures blocked without actuator - this is make-or-break"
- [ ] Slide 25: Other risk mitigation strategies (2-3 min)
- [ ] Slide 26: Summary (30 sec)
  - 3 viable architectures (cost/innovation/UX trade-offs)
  - Selection depends on customer priorities
  - **Critical path: Actuator sourcing must resolve Week 0-2**
- [ ] Slide 27: Q&A

### <span style="color:green">v2.3.0: Slide Refinement & Visuals (feature/presentation-refinement)</span>

**Status:** COMPLETE - 34 slides with speaker notes, CSS styling, condensed content

**Completed Work:**
- [x] All slides have speaker notes and takeaway messages
- [x] Combined Summary + Q&A slides (condensed to 34 slides total)
- [x] Moved 3 detailed slides to BACKUP section
- [x] Text condensed to fit on slides (no overflow)
- [x] Blue theme with styled takeaway boxes
- [x] Final presentation committed (5c4162f)

**DEFERRED to Backlog (per user decision Oct 18):**
- ~~Add images/diagrams to slides~~ - Moved to backlog, focus on practice instead

### Phase Gate: v2.3.0 → v2.4.0
- [x] All slide content complete (34 slides in 30 min = feasible)
- [x] Speaker notes on all slides
- [x] Presentation structure finalized
- **Gate Decision:** ✅ READY for v2.4.0 Practice & Refinement

### <span style="color:blue">v2.4.0: Practice & Refinement (feature/presentation-practice)</span>

**Focus:** Practice delivery, timing, Q&A preparation
**Estimate:** 4-6h over 3 days (Oct 18-20)
**Status:** IN PROGRESS

**Practice Guide Created:**
- [x] source/practice-guide.md (comprehensive practice guide with timing benchmarks)
- [x] ChatGPT voice mode coaching instructions (see Practice Guide for prompts)

**Practice Session Workflow (Human Work):**

**💡 TIP:** Use ChatGPT voice mode as your practice coach!
- Opens mobile app, start voice conversation
- Prompt: "Act as my presentation coach. Time me, note filler words, ask clarifying questions."
- Benefits: Real-time timing feedback, pacing guidance, Q&A simulation

**Manual Practice Sessions:**
- [ ] **Oct 18 (Today):**
  - [ ] Run 1: Full timed run (baseline - note rough spots)
  - [ ] Run 2: Focus on HIGH PRIORITY sections (Slides 8-9, 19, 22-24, 34)
  - [ ] Review: Identify slides that caused stumbles

- [ ] **Oct 19 (Sunday):**
  - [ ] Run 3: Full timed run (aim for 27-30 min)
  - [ ] Run 4: Practice Q&A scenarios (see Practice Guide Q&A section)
  - [ ] Review: Are you hitting timing checkpoints?

- [ ] **Oct 20 (Monday):**
  - [ ] Run 5: Final dress rehearsal (full presentation)
  - [ ] Generate final PDF (make marp, export PDF)
  - [ ] Email presentation to Nathan Briggs by EOD
  - [ ] Light review only (don't over-practice)

**Timing Targets (from Practice Guide):**
- Checkpoint 1 (after Slide 5): ~2:00
- Checkpoint 2 (after Slide 11): ~8:00
- Checkpoint 3 (after Slide 20): ~18:00
- Checkpoint 4 (after Slide 27): ~23:00
- Checkpoint 5 (after Slide 33): ~28:00
- Final (Slide 34): 27-30 minutes

**Q&A Preparation:**
- [ ] Review Q&A section in Practice Guide (anticipated questions + 30-sec answers)
- [ ] Key topics to prepare:
  - [ ] "Why SOL_ECO over PIEZO_ECO?" (cost-constrained, manufacturability)
  - [ ] "Biggest technical risk?" (actuator sourcing - 3-4 week lead time)
  - [ ] "How did you validate 2.3mm constraint?" (Braille Authority standards)
  - [ ] "What if user testing fails?" (success criteria defined, debug root cause)
  - [ ] "Why only 6 pilot units?" (2 durability, 2 user test, 2 backup)

**Backup Formats:**
- [ ] Generate artifacts/presentation-marp.pdf (export from HTML)
- [ ] Test PDF opens on different devices (Windows + Mac if available)

### Phase Gate: v2.4.0 → Final Delivery
- [ ] Presentation practiced (3+ runs, hitting timing targets)
- [ ] Q&A preparation complete (key questions answered confidently)
- [ ] Final PDF generated and tested
- [ ] Email sent to Nathan Briggs by EOD Oct 20

---

## <span style="color:red">v3.0.0: Final Delivery & Interview (Oct 20-21)</span>

### <span style="color:red">v3.1.0: Final Artifacts & Email (Oct 20 EOD - CRITICAL)</span>

**⚠️ CRITICAL DEADLINE: OCT 20, 2025 (MONDAY) EOD**

**Step 1: Generate PDF**
- [ ] Run: `make marp` (regenerate HTML)
- [ ] Export to PDF from browser (Chrome: Print → Save as PDF)
- [ ] Test PDF opens correctly (verify all 34 pages render)
- [ ] Verify file size <25MB for email attachment

**Step 2: Email Delivery**
- [ ] **To:** Nathan Briggs (nathan.briggs@lamresearch.com)
- [ ] **Subject:** "LAM EE5 Interview - Braille Display Concept Evaluation - [Your Name]"
- [ ] **Body:**
  ```
  Hi Nathan,

  Attached is my presentation for the Oct 21 interview. The main slide deck covers:
  - Requirements analysis (17 requirements from PDF + derived constraints)
  - 3 alternative architectures (SOL_ECO $506, PIEZO_ECO $592, PIEZO_DLX $606)
  - Trade-off analysis (cost, timeline, robustness)
  - 8-week pilot execution plan

  Looking forward to presenting on Tuesday.

  Best regards,
  [Your Name]
  ```
- [ ] **Attach:** artifacts/presentation-marp.pdf
- [ ] **Send & Verify:** Check sent folder, wait for delivery confirmation

### <span style="color:red">v3.2.0: Interview Day Prep (Oct 21)</span>

**Night Before (Oct 20):**
- [ ] Open presentation HTML locally (artifacts/presentation-marp.html)
- [ ] Test HDMI output from laptop
- [ ] Charge laptop fully (bring charger)
- [ ] Close unnecessary apps, disable notifications
- [ ] Pack bag: ID, resume (5 copies), laptop, charger, HDMI cable, water, notebook

**Morning Of (Oct 21):**
- [ ] Light review of TAKEAWAY slides only (10-15 min max)
- [ ] Arrive 10-15 min early
- [ ] Deep breath - trust your preparation

---

## Technical-Debt

### EMI Cost-Down Optimization (Post-Pilot)
- **Purpose:** Reduce EMI component costs from "pass with >6dB margin" to "pass with target margin (3dB)"
- **Rationale:** Current low-risk design uses conservative EMI suppression (1000µF bulk caps, 100nF bypass on every IC) to ensure pilot passes preliminary testing on first attempt. Post-pilot, optimize to "just good enough" based on actual measured emissions.
- **Cost reduction opportunities:**
  - **Bulk capacitors:** 1000µF → 470µF or 220µF (reduce by 50-75%) → Save $1.20-$1.80
  - **Ceramic bypass:** 100nF on all 24 ICs → Selectively place only on high-noise drivers → Save $0.12-$0.18
  - **Zener clamps:** Currently using ULN2803A internal flyback (free), could add zeners for faster decay if needed (cost neutral)
  - **Ferrite beads:** Currently not in BOM, add only if pre-scan shows >3dB margin violations → $0.50 adder if needed
- **Measurement-driven approach:**
  1. Week 7 pilot: EMI pre-scan with spectrum analyzer (baseline measurements)
  2. Identify worst-case emissions (conducted vs radiated, which frequencies)
  3. If >10dB margin: Reduce capacitance by 50% and re-test (cost-down iteration)
  4. If 3-6dB margin: Keep current design (optimal)
  5. If <3dB margin: Add targeted fixes (ferrite beads on specific rails, zener clamps on specific solenoids)
- **Target savings:** $1.50-$2.00 per unit (0.6-0.8% BOM reduction)
- **Risk:** LOW (only optimize after pilot validates baseline design works)
- **Status:** Deferred to Month 3-4 (post-pilot, pre-production volume ramp)
- **Philosophy:** **"Design for standards compliance with margin, then cost-down to target margin"** (not "design minimum and hope it passes")

### Future Slash Command: /arch-tradeoff
- **Purpose:** Generate trade-off analysis documentation from architectures.yaml
- **Rationale:** Separate concerns - /arch-gen focuses on individual architecture details, /arch-tradeoff focuses on comparison/evaluation
- **Reference template:** `docs/_obsolete/architecture-v1.3.0-4arch-manual.md` (22KB strategic analysis with advantages/disadvantages, "When X Wins/Fails", recommendations)
- **Target output:** `docs/tradeoffs.md` (manually edited strategic analysis)
- **Generated artifacts:**
  - `artifacts/architecture-comparison-matrix.md` (quantitative tables - MOVE from /arch-gen)
  - `artifacts/architecture-qualitative-comparison.md` (qualitative ratings across 8 dimensions)
  - `artifacts/architecture-advantages-disadvantages.md` (pros/cons extracted from qualitative YAML data)
  - `artifacts/architecture-decision-trees.md` ("When X Wins/Fails" logic based on quantitative thresholds)
  - `artifacts/architecture-recommendations.md` (portfolio strategy, cost reduction roadmap)
- **Implementation approach:**
  - Read source/architectures.yaml (comparison_dimensions + qualitative/quantitative sections)
  - Generate comparison tables (cost, size, UX, complexity, timeline, mfg, risk, market)
  - Extract advantages from qualitative ratings (💚 BEST/EXCELLENT → advantages, 🔴 POOR/FAIR → disadvantages)
  - Generate "When X Wins" decision trees from quantitative thresholds (e.g., "if timeline < 7 weeks → ARCH-B wins")
  - Generate "When X Fails" from constraints (e.g., "if budget < $300 → ARCH-A fails")
  - Keep strategic recommendations in docs/tradeoffs.md (manual)
- **Content mapping from obsolete template:**
  - Section "Advantages" → Extract from qualitative 💚 ratings
  - Section "Disadvantages" → Extract from qualitative 🔴 ratings
  - Section "When X Wins" → Generate from quantitative thresholds
  - Section "When X Fails" → Generate from constraint violations
  - Section "Trade-Off Analysis Summary" → Weighted scoring (manual in docs/tradeoffs.md)
  - Section "Recommendations" → Portfolio strategy (manual in docs/tradeoffs.md)
- **Benefit:** /arch-gen stays focused on subsystem details and specs, /arch-tradeoff handles evaluation logic
- **Status:** Deferred to post-interview (not blocking v1.4.0 Trade-off Analysis - can write manually)

### Documentation Structure Clarification
- **docs/_obsolete/architecture-v1.3.0-4arch-manual.md** - OBSOLETE v1.3.0 strategic analysis (moved before renaming + 5th arch)
- **docs/_obsolete/actuator-mechanical-latch-concept-v1.3.0.md** - OBSOLETE latch concept (specific to old ARCH-D design)
- **artifacts/architecture.md** - Technical reference with subsystem details (auto-generated via /arch-gen)
- **artifacts/architecture-comparison-matrix.md** - Quantitative comparison tables (auto-generated, currently by /arch-gen)
- **docs/tradeoffs.md** - Strategic trade-off analysis (v1.4.0, manually written)
- **docs/solution.md** - Recommended solution with justification (v1.5.0, manually written)
- Future: /arch-tradeoff command will auto-generate advantages/disadvantages, decision trees from YAML

### Enhanced Requirements Traceability Analysis
- **Purpose:** Create comprehensive coverage matrix showing which requirements each architecture satisfies
- **Plan:** See [docs/requirements-trace-plan.md](docs/requirements-trace-plan.md) for complete implementation details
- **Priority:** P1-High (affects traceability rubric score)
- **Effort:** 2-3 hours (Python script enhancement)
- **Status:** Deferred to post-interview

### Interview Logistics
- Interview Format: Onsite at Fremont, CA (4.5 hours total)
- Presentation: 30 minutes
- Q&A: 15 minutes
- Interview Date: Tuesday, Oct 21st, 2025 (CONFIRMED)
- Materials delivery: Email PDF/PPT by EOD Monday Oct 20th (USB not supported)
