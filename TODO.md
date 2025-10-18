# Lam Research EE Interview - Project TODO

## 📊 REALISTIC PROJECT STATUS (Updated Oct 18, 2025)

**Interview:** Oct 21, 2025 (Tuesday) - **3 DAYS AWAY** ⚠️

**AI Workflow Focus (this TODO):** Track remaining presentation refinement tasks
**Human Prep Focus (separate doc):** See `docs/interview-prep-checklist.md` for Q&A, delivery coaching, practice workflow

---

**Remaining AI Work (~3-5h):**
1. ✅ Slide content refinement (DONE - added subsystem differentiators, BOM Details slide, Q&A prep)
2. ✅ Speaker notes (DONE - all slides have notes, Q&A prep integrated)
3. ⏳ Add images/diagrams (1-2h) - architecture comparison charts, decision tree
4. ⏳ Final slide polish (1h) - review all TAKEAWAYs ≤80 chars, check overflow
5. ⏳ Test presentation flow (1h) - open HTML, verify presenter mode works

**Key Files Ready:**
- ✅ source/presentation-marp.md (29 slides with speaker notes, CSS styled)
- ✅ artifacts/presentation-marp.html (regenerates in 1 second with `make marp`)
- ✅ artifacts/presentation-marp.pdf (backup distribution format)
- ✅ docs/interview-prep-checklist.md (16KB comprehensive prep guide)
- ✅ artifacts/interview-prep-checklist.pdf (printable backup)
- ✅ docs/actuator-emi-design-analysis.md (46 KB technical deep-dive)
- ✅ artifacts/bom/*.csv (3 architectures: $505.71, $591.99, $605.67)
- ✅ artifacts/architecture.md (auto-generated from YAML)

**Human Prep (not tracked here):**
- See `docs/interview-prep-checklist.md` for:
  - Q&A anticipated questions (5 prepared answers)
  - Timing strategy (30-min breakdown)
  - Key messages to memorize (systems engineering philosophy)
  - Practice workflow (days before interview)
  - Presenter mode technical guide

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

## <span style="color:red">v1.0.0: Technical Analysis (feature/tech-analysis)</span>

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

<details>
<summary><strong>Original v1.4.0 Plan (Collapsed - Already Complete via EMI Analysis)</strong></summary>

**Guide:** See [docs/tradeoff-analysis-guide.md](docs/tradeoff-analysis-guide.md) for complete methodology

**Quality Metrics:** See [docs/quality-metrics.md](docs/quality-metrics.md) v1.4.0 section for gate criteria

**Step 1: Define Evaluation Criteria (What Do We VALUE?)**
- [ ] Define evaluation framework based on design context:
  - [ ] **Context:** 2-month pilot production for China accessibility market
  - [ ] **Stakeholder priorities:** (ASSUME since not specified)
    - [ ] Time to market (CRITICAL - 2 month constraint)
    - [ ] Unit cost (HIGH - China market price sensitivity)
    - [ ] Development cost/NRE (MEDIUM - pilot budget limited)
    - [ ] Manufacturability/yield (HIGH - pilot → mass production)
    - [ ] Robustness/reliability (MEDIUM - accessibility device)
    - [ ] UX/usability (HIGH - sight-impaired users)
    - [ ] Safety (MEDIUM - low voltage, battery powered)
  - [ ] **Assumption documentation:** Explicitly state what was assumed and why
  - [ ] **Weighted scoring matrix:** Assign weights to each criterion (must sum to 100%)
- [ ] Example evaluation matrix structure:
  ```
  Criterion              | Weight | Arch A | Arch B | Arch C | Notes
  -----------------------|--------|--------|--------|--------|-------
  Time to Market         | 25%    | 7/10   | 9/10   | 5/10   | B fastest (COTS parts)
  Unit Cost (<$50 BOM)   | 20%    | 6/10   | 8/10   | 4/10   | B lowest cost
  Dev Cost (<$50K NRE)   | 10%    | 5/10   | 9/10   | 3/10   | A needs custom tooling
  Manufacturability      | 20%    | 8/10   | 7/10   | 6/10   | ARCH_PIEZO_ECO: simpler DFM
  Robustness/Reliability | 10%    | 7/10   | 6/10   | 8/10   | ARCH_PIEZO_DLX: more robust
  UX/Usability           | 10%    | 8/10   | 7/10   | 9/10   | ARCH_PIEZO_DLX: better tactile
  Safety                 | 5%     | 9/10   | 9/10   | 8/10   | All low voltage
  TOTAL SCORE            | 100%   | X.X    | X.X    | X.X    | Weighted average
  ```

**Step 2: Advantages & Disadvantages Analysis**
**⚠️ PDF REQUIREMENT:** "Discuss their advantages and disadvantages" (explicit in Step 3)

- [ ] For EACH architecture, document:
  - [ ] **Advantages** (strengths, what it does well - be specific with data)
  - [ ] **Disadvantages** (weaknesses, limitations, risks - be honest)
  - [ ] **When it wins** (under what conditions does this architecture excel?)
  - [ ] **When it fails** (under what conditions does this become unviable?)
- [ ] Create comparison table showing advantages/disadvantages side-by-side

**Step 3: Quantitative Comparison**
- [ ] **⚠️ ACTUATOR SOURCING RISK ANALYSIS (CRITICAL - affects ALL architectures)**
  - [ ] Document the crisis: NO COTS actuators found meeting 2.5mm pitch + force requirements
  - [ ] Create three-path analysis table (resources/calculations/actuator-sourcing-risk.xlsx)
    - Path A (COTS search): $5K cost, 2 weeks, 20% probability
    - Path B (Custom quickturn): $25K-50K NRE, 2-4 weeks, 90% probability
    - Path C (Spec relaxation): $0, 0 weeks, 100% probability (but violates ADA 703.3)
  - [ ] Timeline impact analysis: Best case (+0 wks), Likely case (+4 wks), Worst case (+8 wks)
  - [ ] Probability-weighted expected value: Timeline & NRE cost
  - [ ] **Key message:** "This is THE critical path risk - all architectures blocked without resolution"
- [ ] Create comparison matrix in resources/calculations/
  - [ ] Cost comparison (BOM estimates for each architecture)
  - [ ] Power budget calculations (actuators + MCU + communication)
  - [ ] Size/complexity metrics (component count, PCB area estimate)
  - [ ] Timeline feasibility (parts lead time, assembly complexity, actuator sourcing)
- [ ] Build resources/calculations/power-budget.xlsx
  - Calculate power for all 3 architectures
  - Battery life estimates
- [ ] Build resources/calculations/bom-cost-estimate.xlsx
  - Component costs (qty 1, qty 100, qty 1000)
  - Total BOM cost per architecture
- [ ] Build resources/calculations/timeline-gantt.xlsx
  - 2-month timeline with milestones
  - Critical path analysis
  - Risk buffers
- [ ] Assess manufacturability for high volume (DFM analysis)
- [ ] Risk analysis for each approach (technical, timeline, cost, supply chain)
- [ ] **⚠️ SENSITIVITY ANALYSIS (REQUIRED):**
  - [ ] "What if cost doubles?" - Which architecture is most robust?
  - [ ] "What if timeline compresses to 1 month?" - Which is fastest to implement?
  - [ ] "What if key component unavailable?" - Which has better supply chain alternates?
  - [ ] "What if volume targets change (1K vs 100K)?" - Which scales better?
  - [ ] Create sensitivity comparison matrix
- [ ] **"Other Considerations" Analysis:**
  - [ ] Supply chain availability (lead times, single-source risks)
  - [ ] Team expertise required (familiar vs new technology)
  - [ ] Tooling/equipment needs (what's available vs what to buy)
  - [ ] Risk tolerance (proven tech vs cutting edge)
  - [ ] Market timing considerations
- [ ] Create docs/tradeoffs.md with:
  - [ ] **Evaluation criteria framework** (what we value + weights)
  - [ ] **Assumptions documentation** (China market, pilot production, etc.)
  - [ ] **Advantages & disadvantages** for each architecture (honest assessment)
  - [ ] **Quantitative comparison** (cost, power, size, timeline - scored objectively)
  - [ ] **Weighted scoring results** (which architecture scores highest?)
  - [ ] **Sensitivity analysis** ("what if" scenarios - how evaluation changes)
  - [ ] **"Other considerations"** (supply chain, expertise, tooling)
  - [ ] **Portfolio strategy** showing when each architecture wins (decision framework based on constraints)
    - Example: "ARCH_PIEZO_ECO wins if cost < $450 AND timeline > 8 weeks"
    - Example: "ARCH_SOL_ECO wins if mechanical simplicity prioritized AND cost < $300"
    - Example: "ARCH_PIEZO_DLX wins if wireless required AND budget allows $450+"
- [ ] Run /rubric-eval for Category 3 assessment (Trade-off Analysis: 30 pts)
  - Generates artifacts/rubric-reports/v1.4.0-tradeoffs-eval.md

### <span style="color:red">v1.5.0: Production Transition Process (feature/tech-analysis-production)</span>
**Design Plan Alignment:** Complete Design Step 4 (PDF p.10) - 20/100 points

**Key Message:** "Same production process, but actuator sourcing is THE critical path risk"

**⚠️ CRITICAL PATH RISK (SHARED ACROSS ALL ARCHITECTURES):**
- **Week 0-2: Actuator Sourcing Crisis Resolution**
  - [ ] Document the problem: NO COTS actuators found that meet 2.5mm pitch + force requirements
  - [ ] Three-path strategy (parallel effort):
    - **Path A (Low Cost, High Risk):** Intensive COTS search (obscure suppliers, overseas, custom inquiries)
      - Budget: $5K inquiry costs, Timeline: 2 weeks, Probability: 20%
    - **Path B (High Cost, Low Risk):** Custom actuator 2-week quickturn (piezo OR solenoid)
      - Budget: $25K-50K NRE, Timeline: 2-4 weeks, Probability: 90%
    - **Path C (Spec Compromise):** Relax 2.5mm pitch → 3.5mm (violates ADA 703.3 but pilot-acceptable)
      - Budget: $0, Timeline: 0 weeks, Probability: 100% (but requirements violated)
  - [ ] Decision point: By end of Week 2, commit to one path
  - [ ] **THIS IS THE MAKE-OR-BREAK DECISION** - Without actuator, ALL architectures fail

- [ ] Define common production process (8-12 weeks, architecture-agnostic base)
  - Week 0-2: **Actuator sourcing resolution** (CRITICAL PATH)
  - Week 3-4: Detailed design (schematic capture, PCB layout, BOM lock)
  - Week 5-6: Prototype build (fab, assembly, debug)
  - Week 7-9: Pilot production (10-100 units, yield validation)
  - Week 10-12: Compliance & handoff (testing, documentation, manufacturing transfer)

- [ ] Create master Gantt chart with architecture-specific timeline impacts
  - **Base case (IF COTS actuator found Week 0-2):** 8 weeks total
  - **ARCH_PIEZO_ECO:** +0 weeks (simplest electrical integration)
  - **ARCH_SOL_ECO:** +2 weeks (mechanical cam tooling)
  - **ARCH_PIEZO_DLX:** +1 week (BLE certification testing)
  - **Custom actuator case:** +8 weeks (design, fab, validation) → 16-20 week timeline

- [ ] Create decision tree diagram (resources/diagrams/production-timeline-risk.png)
  - Show three timelines: COTS found (8-10 wks), Custom quickturn (12-14 wks), Custom standard (16-20 wks)
- [ ] Create shared preliminary schematic concepts applicable across architectures (resources/schematics/)
  - [ ] Power supply schematic concept (5V/3.3V rails - common to all)
  - [ ] MCU core schematic concept (STM32 - common to all)
  - [ ] Driver IC schematic concept (ULN2803A - common to all)
  - [ ] Communication interface options (USB-C vs BLE module - architecture-specific)
- [ ] Power supply design considerations (voltage rails, regulation, battery management - architecture-specific)
- [ ] Thermal analysis (worst-case power dissipation, cooling strategy - per architecture)
- [ ] Production timeline detail per architecture (update resources/calculations/timeline-gantt.xlsx)
  - ARCH_PIEZO_ECO: 8-10 weeks (COTS piezo if available)
  - ARCH_SOL_ECO: 10-12 weeks (mechanical tooling for cam)
  - ARCH_PIEZO_DLX: 10-12 weeks (BLE certification)
- [ ] Risk mitigation strategies (detailed breakdown)
  - [ ] **PRIMARY RISK (ALL ARCHITECTURES):** Actuator sourcing
    - Mitigation: Triple-path parallel effort (COTS search + Custom quote + Spec relaxation backup)
    - Contingency: $50K budget allocated for custom actuator NRE
    - Timeline impact: +8 weeks if custom required
  - [ ] **ARCH_PIEZO_ECO risks:** Piezo driver voltage (200V boost converter design)
  - [ ] **ARCH_SOL_ECO risks:** Mechanical cam tooling (CNC programming, tolerance stack-up)
  - [ ] **ARCH_PIEZO_DLX risks:** BLE certification (FCC testing, schedule slip)

- [ ] Create docs/production-process.md with:
  - Architecture-agnostic production flow
  - Actuator sourcing crisis analysis (THE ELEPHANT IN THE ROOM)
  - Decision framework: "Pick architecture AFTER actuator sourcing resolves"
  - Timeline scenarios: Best case (8 wks) vs Likely case (12 wks) vs Worst case (20 wks)
- [ ] Run /rubric-eval for Category 4 assessment (Path to Production: 20 pts)
  - Generates artifacts/rubric-reports/v1.5.0-solution-eval.md

### <span style="color:red">v1.6.0: Phase 1 Self-Assessment (feature/tech-analysis-assessment)</span>
- [ ] Run /rubric-eval for comprehensive Phase 1 evaluation
  - Generates artifacts/rubric-reports/phase1-rubric-eval.md (0-100 points)
  - Generates artifacts/rubric-reports/req-traceability-report.md (coverage matrix)
- [ ] Review evaluation report and address critical gaps
- [ ] Verify all Phase Gate criteria met before proceeding to v2.0.0

### Phase Gate: v1.0.0 → v2.0.0
- [ ] All technical analysis tasks complete
- [ ] Quality metrics met (3 architectures analyzed: ARCH_PIEZO_ECO, ARCH_SOL_ECO, ARCH_PIEZO_DLX)
- [ ] Trade-off analysis complete with quantitative data
- [ ] Portfolio strategy defined with decision framework (not "best" - context-dependent selection)

---

## <span style="color:red">v2.0.0: Presentation Development (feature/presentation)</span>

### <span style="color:red">v2.1.0: Quality Metrics Definition (feature/presentation-metrics)</span>
- [ ] Create docs/presentation-quality-metrics.md
  - Define time management targets (30 min presentation, 15 min Q&A)
  - Define visual clarity standards (readable at distance, clear diagrams)
  - Define decision justification depth (quantitative data shown, trade-offs clear)
  - Define Q&A readiness criteria (anticipate 10+ questions, prepare answers)

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

### <span style="color:blue">v2.3.0: Slide Refinement & Visuals (feature/presentation-refinement)</span>

**Focus:** Polish existing 20 slides, add takeaway messages, insert diagrams
**Estimate:** 3-4h (realistic, not original 3h estimate)

- [ ] Review all 20 slides in Firefox fullscreen - identify content gaps
- [ ] Add takeaway messages to remaining slides (currently 3 examples, need ~15 more)
- [ ] Refine slide content for clarity and impact
- [ ] Add market chart (market-price-vs-chars.svg already created)
- [ ] Add architecture block diagrams (if available from resources/diagrams/)
- [ ] Add EMI comparison visual (if helpful - may be overkill)
- [ ] Practice timing each slide (~60 sec target per slide)

### <span style="color:red">v2.4.0: Practice & Refinement (feature/presentation-practice)</span>
- [ ] Time the presentation (target: 30 minutes)
- [ ] Prepare Q&A responses for likely questions
- [ ] Whiteboard practice (circuit sketching)
- [ ] Create backup presentation formats (PDF + PPTX)

### <span style="color:red">v2.5.0: Phase 2 Self-Assessment (feature/presentation-assessment)</span>
- [ ] Run /rubric-eval for presentation readiness (Category 6: Presentation - 10 pts)
  - Generates artifacts/rubric-reports/v2.5.0-presentation-eval.md
- [ ] Grade against docs/presentation-quality-metrics.md
- [ ] Time check (does it fit 30 min? Run through with timer)
- [ ] Clarity check (can audience follow? Test with someone else)

### Phase Gate: v2.0.0 → v3.0.0
- [ ] Presentation complete and timed (30 min target)
- [ ] Visual materials clear and professional
- [ ] Q&A preparation complete
- [ ] Backup formats ready

---

## <span style="color:red">v3.0.0: Final Deliverables (feature/delivery)</span>

### <span style="color:red">v3.1.0: Documents to Build (feature/delivery-documents)</span>
- [ ] Consolidate Phase 1 docs into source/technical-analysis.md
  - Merge: docs/requirements.md, architecture.md, tradeoffs.md, solution.md
  - Add: Executive summary, table of contents, references
- [ ] Extract presentation notes to source/presentation-notes.md
  - Speaker notes for each slide
  - Q&A preparation material
- [ ] Download LinkedIn FISH controller presentation
  - [ ] Save Unbedded(1).pptx to resources/portfolio/
  - [ ] Extract key slides for appendix-E-portfolio.pdf
  - [ ] Verify file renders correctly (test on laptop)

### <span style="color:red">v3.2.0: Artifacts to Generate (feature/delivery-artifacts)</span>
- [ ] Generate artifacts/presentation.pdf (export from source/presentation.pptx)
- [ ] Copy artifacts/presentation.pptx (from source/presentation.pptx)
- [ ] Generate artifacts/appendix-A-technical-analysis.pdf (from source/technical-analysis.md)
- [ ] Generate artifacts/appendix-B-calculations.pdf (from resources/calculations/*.xlsx)
- [ ] Generate artifacts/appendix-C-datasheets.pdf (compile key datasheets from reference/)
- [ ] Generate artifacts/appendix-D-qa-prep.pdf (from source/presentation-notes.md)
- [ ] Generate artifacts/appendix-E-portfolio.pdf (FISH + ham radio docs + Unbedded(1).pptx slides)
- [ ] Verify all files under size limits for email (<25MB total)
- [ ] Test artifacts/presentation.pdf opens correctly on different devices (Windows + Mac)
- [ ] Test artifacts/presentation.pptx renders correctly (Windows + Mac)

### <span style="color:red">v3.3.0: Pre-Interview Checklist (feature/delivery-checklist)</span>
⚠️ **CRITICAL DEADLINE: OCT 20, 2025 (MONDAY)** - Presentation due 24hrs before interview!

**⚠️ 24-HOUR RULE:** Interview Oct 21 (Tue) → Presentation must be EMAILED by EOD Oct 20 (Mon)
- USB drives NOT supported per Lam security policy
- Late submission = No digital content = Failed interview

**Digital Checklist (Email Oct 20):**
- [ ] **OCT 20 (BY EOD MONDAY):** Email presentation & appendices to Nathan Briggs
  - Subject: "LAM EE5 Interview - Concept Evaluation Presentation & Appendices - Spencer Barrett"
  - Attach: presentation.pdf (primary - main slide deck)
  - Attach: presentation.pptx (backup - editable format)
  - Attach: appendix-A-technical-analysis.pdf (consolidated Phase 1 docs)
  - Attach: appendix-B-calculations.pdf (power budget, BOM, timeline)
  - Attach: appendix-C-datasheets.pdf (key component datasheets referenced)
  - Attach: appendix-D-qa-prep.pdf (anticipated questions & answers)
  - Attach: appendix-E-portfolio.pdf (FISH controller + ham radio documentation)
  - Verify: Total <25MB, email sent successfully
  - Confirm: Check for delivery confirmation/read receipt

**Laptop Preparation (Oct 19-20):**
- [ ] Test HDMI output from laptop (verify video works)
- [ ] Charge laptop fully (bring charger as backup)
- [ ] Load all files locally on laptop (don't rely on email/cloud)
  - presentation.pptx (main file to present from)
  - All appendix PDFs
  - FISH controller project files (code, schematics, photos)
  - Unbedded(1).pptx (LinkedIn FISH light controller presentation)
- [ ] Test presentation.pptx renders correctly on laptop
- [ ] Close all unnecessary apps (clean desktop for professionalism)
- [ ] Disable notifications (Slack, email, OS updates)
- [ ] Set display to "Extend" mode (not mirror) for presenter notes

**Physical Items Checklist (Pack Night Before - Oct 20):**

**Required:**
- [ ] Government-issued ID (driver's license or passport)
- [ ] Latest resume (5 printed copies - one per panel member + extras)
- [ ] Printed presentation slides (full deck backup if laptop fails)
- [ ] Printed appendices packet (all 5 appendices A-E, bound or stapled)
- [ ] Laptop with HDMI output support
- [ ] Laptop charger (just in case)
- [ ] HDMI cable (backup - they should have one, but bring yours)
- [ ] HDMI adapter if needed (USB-C to HDMI, etc.)

**Portfolio/Background Review:**
- [ ] FISH light controller hardware (PCB assembled, in protective case)
- [ ] FISH controller documentation packet:
  - [ ] 1-page project overview (what it does, why you built it)
  - [ ] Schematic printout (readable, annotated if helpful)
  - [ ] PCB layout printout (top/bottom layers)
  - [ ] Code snippet printout (key algorithm or driver)
  - [ ] Photos of installed system (in fish tank, working)
  - [ ] Lessons learned / design decisions (1-page)
  - [ ] LinkedIn presentation printout (Unbedded(1).pptx - key slides)
- [ ] Ham radio kit (assembled min-ham radio)
- [ ] Ham radio documentation packet:
  - [ ] 1-page project overview (kit model, build experience)
  - [ ] Schematic from kit (annotated with your notes)
  - [ ] Photos of build process (assembly stages)
  - [ ] Photos of completed radio (operational)
  - [ ] Operating demonstration plan (if applicable)
  - [ ] Lessons learned / technical challenges overcome (1-page)

**Backup Materials:**
- [ ] Printed copy of presentation slides (backup if laptop fails)
- [ ] Printed copy of resume (extras beyond the 5)
- [ ] Business cards (if you have them)
- [ ] Notebook + pen (for taking notes during interview)

**Comfort Items:**
- [ ] Water bottle (stay hydrated during 5h 45min interview)
- [ ] Breath mints (post-lunch freshness)
- [ ] Professional appearance (check night before):
  - [ ] Outfit planned (business casual or business professional)
  - [ ] Shoes polished
  - [ ] Minimal jewelry/accessories

**Verify Night Before (Oct 20):**
- [ ] All physical items packed in bag
- [ ] Laptop bag has: laptop, charger, HDMI cable, adapter
- [ ] Portfolio bag has: FISH controller, documentation packet
- [ ] Documents bag has: ID, resumes, printed slides
- [ ] Know exact address: Lam Research, Tualatin, OR campus
- [ ] Know parking instructions
- [ ] Know check-in procedure (security desk)
- [ ] Set 2 alarms for interview morning

### Phase Gate: v3.0.0 → v4.0.0
- [ ] All deliverable PDFs generated successfully
- [ ] Presentation emailed 24 hours before interview
- [ ] Physical materials prepared

---

## <span style="color:red">v4.0.0: Interview Preparation (feature/interview-prep)</span>

### <span style="color:red">v4.1.0: AI Skills Strategy (feature/interview-ai-strategy)</span>
- [ ] Review reference/interview/ai-strategy-context.md (Spencer's AI approach)
- [ ] Develop AI value proposition talking points
  - [ ] AI as force multiplier for EE work (design iteration, simulation, documentation)
  - [ ] Team/company benefits (knowledge capture, onboarding acceleration, design review efficiency)
  - [ ] Semiconductor-specific applications (test data analysis, yield optimization, failure analysis)
- [ ] Prepare responses to anticipated concerns
  - [ ] Data security and IP protection (what stays internal, what goes to cloud)
  - [ ] Accuracy and verification (AI-assisted != AI-autonomous, engineering judgment critical)
  - [ ] Tool governance (working within company policies, adaptable to their stack)
- [ ] Frame AI capabilities with concrete examples
  - [ ] RAG database for job experience (20% interview hit rate from 10 applications)
  - [ ] Custom document generation from requirements
  - [ ] ATS filter navigation strategy
- [ ] Connect AI to LAM-specific value
  - [ ] Equipment design documentation efficiency
  - [ ] Cross-functional communication (EE ↔ SW ↔ Mechanical)
  - [ ] Regulatory/standards compliance acceleration
- [ ] Wait for Tom's response on LAM AI tech stack and policy
- [ ] Tailor pitch based on Tom's feedback (update reference/interview/ai-strategy-context.md)

### <span style="color:red">v4.2.0: EE Skills Preparation (feature/interview-ee-skills)</span>
- [ ] Submit application through portal (if not already done)
- [ ] Wait for scheduling team contact
- [ ] Confirm interview date/time (week of Oct 20th - 4.5 hour onsite)
- [ ] Schedule calendar reminder (24hr before for materials email)
- [ ] Review core EE topics (power electronics, embedded systems, signal integrity)
- [ ] Whiteboard circuit design practice (op-amps, regulators, digital I/O)
- [ ] Semiconductor equipment domain research (plasma etch, deposition, metrology)
- [ ] Final practice run (30 min presentation + 15 min Q&A)
- [ ] Prepare questions to ask interviewers (about role, team, projects, AI policies)

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
