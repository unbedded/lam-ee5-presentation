# Lam Research EE Interview - Project TODO

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

### <span style="color:red">v1.1.0: Quality Metrics Definition (feature/tech-analysis-metrics)</span>
- [ ] Review and refine requirements management procedure
  - Review docs/requirements-policy.md
  - Validate YAML structure in source/requirements.yaml
  - Test slash commands workflow (/req-audit, /req-yaml-to-md, /req-trace)
  - Refine as needed before proceeding to v1.2.0
- [ ] Create docs/quality-metrics.md
  - Define requirements completeness criteria
  - Define solution diversity targets (3+ architectures)
  - Define quantitative analysis standards
  - Define risk identification thoroughness
- [ ] Optional: Run /rubric-eval for early quality check
  - Generates artifacts/rubric-reports/v1.1.0-quality-metrics-eval.md

### <span style="color:red">v1.2.0: Requirements Analysis (feature/tech-analysis-requirements)</span>
- [ ] Create .claude/commands/req-audit.md (requirements compliance checker)
- [ ] Create .claude/commands/req-yaml-to-md.md (YAML→MD generator, outputs to artifacts/)
- [ ] Create .claude/commands/req-trace.md (traceability matrix generator)
- [ ] Populate source/requirements.yaml with all requirements
  - Define system-level requirements (SYS-FUNC-*)
  - Define electrical specifications (EE-PWR-*, EE-CTRL-*, EE-IO-*, EE-COMM-*)
  - Define user/UX requirements (USR-PORT-*, USR-UX-*, USR-ACC-*)
  - Define manufacturing/cost constraints (MFG-COST-*, MFG-VOL-*, MFG-TIME-*)
  - Research relevant standards (NFR-STD-*)
- [ ] Run /req-audit to validate compliance
- [ ] Run /req-yaml-to-md to generate artifacts/requirements.md
- [ ] Review generated requirements.md for completeness
- [ ] Run /rubric-eval for Category 1 assessment (Technical Requirements: 25 pts)
  - Generates artifacts/rubric-reports/v1.2.0-requirements-eval.md

### <span style="color:red">v1.3.0: Solution Architecture Development (feature/tech-analysis-architecture)</span>
- [ ] Download datasheets to reference/datasheets/
  - [ ] Actuators: piezo, solenoid, SMA, micro-motor
  - [ ] MCUs: STM32, ESP32, RP2040, or FPGA options
  - [ ] Communication: BLE modules, USB-C controllers, WiFi modules
  - [ ] Power: battery specs, voltage regulators, charging ICs
- [ ] Research braille actuator technologies
  - [ ] Piezoelectric actuators (datasheets, pros/cons, power, cost)
  - [ ] Solenoid-based systems (datasheets, pros/cons, power, cost)
  - [ ] Shape memory alloy (SMA) (datasheets, pros/cons, power, cost)
  - [ ] Micro-motor solutions (datasheets, pros/cons, power, cost)
- [ ] Design control architecture options (create block diagrams in resources/diagrams/)
  - [ ] Centralized MCU approach (block diagram, component selection)
  - [ ] Distributed control (block diagram, component selection)
  - [ ] FPGA-based solution (block diagram, component selection)
- [ ] Evaluate communication interfaces (comparison table)
  - [ ] Bluetooth LE (power, complexity, cross-platform support)
  - [ ] USB-C (power, complexity, cross-platform support)
  - [ ] WiFi (power, complexity, cross-platform support)
- [ ] Create docs/architecture.md with 3+ distinct solutions (reference diagrams in resources/)
- [ ] Run /rubric-eval for Category 2 assessment (Alternative Solutions: 25 pts)
  - Generates artifacts/rubric-reports/v1.3.0-architecture-eval.md

### <span style="color:red">v1.4.0: Trade-off Analysis (feature/tech-analysis-tradeoffs)</span>
- [ ] Create comparison matrix in resources/calculations/
  - [ ] Cost comparison (BOM estimates for each architecture)
  - [ ] Power budget calculations (actuators + MCU + communication)
  - [ ] Size/complexity metrics (component count, PCB area estimate)
  - [ ] Timeline feasibility (parts lead time, assembly complexity)
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
- [ ] Create docs/tradeoffs.md with quantitative analysis (reference spreadsheets)
- [ ] Run /rubric-eval for Category 3 assessment (Trade-off Analysis: 30 pts)
  - Generates artifacts/rubric-reports/v1.4.0-tradeoffs-eval.md

### <span style="color:red">v1.5.0: Recommended Solution (feature/tech-analysis-solution)</span>
- [ ] Select and justify final architecture (data-driven from v1.4.0 analysis)
- [ ] Create detailed block diagram (resources/diagrams/final-architecture.png)
- [ ] Draft preliminary schematic concepts (resources/schematics/)
  - [ ] Power supply schematic concept
  - [ ] MCU/FPGA core schematic concept
  - [ ] I/O expansion schematic concept
  - [ ] Communication interface schematic concept
- [ ] Power supply design considerations (voltage rails, regulation, battery management)
- [ ] Thermal analysis (worst-case power dissipation, cooling strategy)
- [ ] Production timeline detail (update resources/calculations/timeline-gantt.xlsx)
- [ ] Risk mitigation strategies (timeline, cost, technical, supply chain)
- [ ] Create docs/solution.md with production plan (reference diagrams/schematics/calculations)
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
- [ ] Quality metrics met (3+ architectures analyzed)
- [ ] Trade-off analysis complete with quantitative data
- [ ] Recommended solution selected and justified

---

## <span style="color:red">v2.0.0: Presentation Development (feature/presentation)</span>

### <span style="color:red">v2.1.0: Quality Metrics Definition (feature/presentation-metrics)</span>
- [ ] Create docs/presentation-quality-metrics.md
  - Define time management targets (30 min presentation, 15 min Q&A)
  - Define visual clarity standards (readable at distance, clear diagrams)
  - Define decision justification depth (quantitative data shown, trade-offs clear)
  - Define Q&A readiness criteria (anticipate 10+ questions, prepare answers)

### <span style="color:red">v2.2.0: Presentation Structure (feature/presentation-structure)</span>
- [ ] Create source/presentation.pptx (master slides)
- [ ] Slide 1: Title slide (30 sec)
- [ ] Slides 2-3: Problem statement & challenge (2-3 min)
  - 32 chars, 6 dots, 192 control signals
  - Portable, low-cost, high-volume, 2-month timeline
- [ ] Slides 4-6: Requirements summary (3-5 min)
  - Key technical requirements (SYS, EE, MFG, USR)
  - Prioritization and rationale
- [ ] Slides 7-12: Solution alternatives presentation (8-10 min)
  - 3+ architectures with block diagrams
  - Component selection rationale
  - Pros/cons for each
- [ ] Slides 13-16: Trade-off comparison (5-7 min)
  - Comparison matrix (cost, power, size, complexity, timeline)
  - Quantitative data (power budgets, BOM costs)
  - Risk assessment
- [ ] Slides 17-20: Recommended solution with justification (5-7 min)
  - Final architecture selected
  - Data-driven justification
  - Detailed block diagram
  - Preliminary schematics
- [ ] Slides 21-23: Path to production timeline (3-5 min)
  - 2-month Gantt chart
  - Critical path
  - Manufacturing plan (DFM, sourcing, testing)
- [ ] Slides 24-25: Risk mitigation strategies (2-3 min)
- [ ] Slide 26: Summary & Q&A (30 sec)

### <span style="color:red">v2.3.0: Visual Materials (feature/presentation-visuals)</span>
- [ ] Finalize block diagrams for each architecture (export from resources/diagrams/)
- [ ] Create comparison tables (clear & readable - import from spreadsheets)
- [ ] Timeline/Gantt chart for production path (export from resources/calculations/)
- [ ] Cost breakdown charts (export from resources/calculations/)
- [ ] Risk matrix visualization
- [ ] Ensure all visuals are presentation-quality (readable from distance)

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

### <span style="color:red">v3.2.0: Artifacts to Generate (feature/delivery-artifacts)</span>
- [ ] Generate artifacts/presentation.pdf (export from source/presentation.pptx)
- [ ] Copy artifacts/presentation.pptx (from source/presentation.pptx)
- [ ] Verify both files are under size limits for email
- [ ] Test artifacts/presentation.pdf opens correctly on different devices

### <span style="color:red">v3.3.0: Pre-Interview Checklist (feature/delivery-checklist)</span>
- [ ] Email presentation to Nathan Briggs 24 hours prior
- [ ] Test HDMI output from laptop
- [ ] Print backup copy of presentation
- [ ] Bring government-issued ID
- [ ] Bring latest resume
- [ ] Optional: Bring engineering portfolio examples

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
- Interview Format: Onsite at Fremont, CA (4.5 hours total)
- Presentation: 30 minutes
- Q&A: 15 minutes
- Interview Date: Week of Oct 20th (TBD - awaiting confirmation)
- Materials delivery: Email PDF/PPT 24 hours before (USB not supported)
