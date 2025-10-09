# TODO → Deliverables → Presentation - Complete Artifact Flow

**Purpose:** Show end-to-end progression from TODO tasks → technical deliverables → presentation slides

**Critical Insight:** Every TODO phase produces deliverables that become presentation content. This document shows the **complete artifact flow**.

**Source:** `docs/design-plan.md`

---

## ✅ Quick Check: Do We Have Artifacts for All 4 PDF Requirements?

| PDF Requirement | Primary Artifact | Guide Document | Presentation Slides | Status |
|----------------|------------------|----------------|---------------------|---------|
| **1. Identify requirements** | `requirements.yaml` → `requirements.md` | `requirements-policy.md` | Slides 5-8 | ✅ Ready |
| **2. Multiple solutions** | `architecture.md` + diagrams | (none yet) | Slides 9-12 | 🟡 Guide needed |
| **3. Evaluate solutions** | `tradeoffs.md` + calculations | `tradeoff-analysis-guide.md` | Slides 13-19 | ✅ Ready |
| **4. Path to production** | `solution.md` + Gantt chart | `production-plan-guide.md` | Slides 20-23 | ✅ **JUST CREATED** |

**Status:**
- ✅ **Step 1 (25 pts):** `requirements.yaml` (in progress), `assumptions-register.md` ✅, `requirements-policy.md` ✅
- 🟡 **Step 2 (25 pts):** `architecture.md` (not started, guide needed for v1.3.0)
- ✅ **Step 3 (30 pts):** `tradeoffs.md` (not started), `tradeoff-analysis-guide.md` ✅ (15KB comprehensive guide)
- ✅ **Step 4 (20 pts):** `solution.md` (not started), `production-plan-guide.md` ✅ **JUST CREATED** (12KB comprehensive guide)

**Verdict:** We have guides for 3/4 steps. Need an `architecture-guide.md` for Step 2 (v1.3.0).

---

## 🎯 Big Picture: Artifact Flow

### **Simple Answer: TODO → Deliverables → Slides → Email**

```
TODO Phase (work) → Technical Deliverables (docs/artifacts) → Presentation Slides (PPTX) → Email
     ↓                           ↓                                    ↓                    ↓
  v1.2.0            →    requirements.yaml/.md         →    Slides 5-8: Requirements
  v1.3.0            →    architecture.md + diagrams    →    Slides 9-12: Architectures
  v1.4.0 ⭐         →    tradeoffs.md + calculations   →    Slides 13-19: Trade-offs
  v1.5.0            →    solution.md + timeline        →    Slides 20-23: Production Plan
  v2.1.0-v2.5.0     →    Integrate all above           →    Final deck (20-25 slides)
  v3.1.0-v3.3.0     →    Generate PDF/PPTX             →    lam-ee-presentation.pdf/.pptx → Send 24h before

```

### **Key Principles:**

1. **v1.x phases = BUILD CONTENT** (markdown docs, Excel spreadsheets, diagrams)
2. **v2.x phases = ORGANIZE INTO SLIDES** (extract summaries from v1.x deliverables)
3. **v3.x phases = PRODUCE FINAL FILES** (PDF + PPTX exports)
4. **Every technical deliverable becomes slide content** (build once, use twice)

**Example Flow:**
- v1.4.0: Create detailed `bom-cost.xlsx` (50 line items, 3 volume scenarios)
- v2.3.0: Extract to **Slide 14** (3-bar chart: Arch A vs B vs C at 1K volume)
- v3.2.0: Export slide deck to `lam-ee-presentation.pptx`
- v3.3.0: Email PDF+PPTX 24 hours before interview

---

## 📊 Complete Artifact Traceability

### v1.2.0: Requirements Analysis
| TODO Tasks | Technical Deliverables | Presentation Slides | Rubric |
|------------|----------------------|---------------------|---------|
| Define 15-20 SMART requirements | `source/requirements.yaml` | **Slide 5:** Requirements Overview | 25 pts |
| Identify vague specs | `docs/assumptions-register.md` | **Slide 6:** Key Assumptions | (Step 1) |
| Competitive analysis | Competitive benchmark table | **Slide 7:** Competitive Analysis | |
| Standards compliance | Standards compliance list | **Slide 8:** Standards Awareness | |
| Run `/req-audit` | `artifacts/rubric-reports/req-audit.md` | (backup material) | |

**Presentation Milestone:** Draft slides 5-8 (Requirements section)

---

### v1.3.0: Solution Architecture Development
| TODO Tasks | Technical Deliverables | Presentation Slides | Rubric |
|------------|----------------------|---------------------|---------|
| Research actuators | `reference/datasheets/` | (research - not in slides) | 25 pts |
| Design 3+ architectures | `docs/architecture.md` | **Slides 9-11:** Architecture A, B, C | (Step 2) |
| Create block diagrams | `resources/diagrams/arch-*.png` | Embedded in slides 9-11 | |
| Component selection | Component tables | **Slide 12:** Key Components | |
| Pros/cons analysis | Pros/cons tables | Preview for slide 16 | |

**Presentation Milestone:** Draft slides 9-12 (Architecture section)

---

### v1.4.0: Trade-off Analysis ⭐ HIGHEST RUBRIC WEIGHT
| TODO Tasks | Technical Deliverables | Presentation Slides | Rubric |
|------------|----------------------|---------------------|---------|
| Define evaluation criteria | Evaluation framework | **Slide 13:** Evaluation Framework | 30 pts |
| BOM cost comparison | `resources/calculations/bom-cost.xlsx` | **Slide 14:** Cost Comparison | (Step 3) |
| Power budget analysis | `resources/calculations/power-budget.xlsx` | **Slide 15:** Power Budget | |
| Timeline feasibility | `resources/calculations/timeline.xlsx` | Integrated into slide 14 | |
| Advantages/disadvantages | `docs/tradeoffs.md` sections | **Slide 16:** Pros/Cons Matrix | |
| Weighted scoring matrix | Decision matrix | **Slide 17:** Decision Matrix 💰 | |
| Sensitivity analysis | Sensitivity scenarios | **Slide 18:** Sensitivity/Robustness | |
| Final recommendation | Recommendation + justification | **Slide 19:** Recommendation | |

**Presentation Milestone:** Draft slides 13-19 (THE MONEY SLIDES - 30% of rubric!)

---

### v1.5.0: Recommended Solution & Production Plan
| TODO Tasks | Technical Deliverables | Presentation Slides | Rubric |
|------------|----------------------|---------------------|---------|
| Final architecture diagram | `resources/diagrams/final-arch.png` | **Slide 20:** Selected Architecture | 20 pts |
| 2-month Gantt chart | `resources/calculations/timeline-gantt.xlsx` | **Slide 21:** 2-Month Timeline | (Step 4) |
| Pilot production strategy | `docs/solution.md` section | **Slide 22:** Pilot Strategy | |
| DFM considerations | DFM checklist | **Slide 22:** (bullets) | |
| Risk mitigation | Risk register | **Slide 23:** Risk Mitigation | |
| Scale path (pilot→mass) | Production roadmap | **Slide 23:** (timeline) | |

**Presentation Milestone:** Draft slides 20-23 (Production section)

---

### v2.1.0-v2.5.0: Presentation Development
| TODO Tasks | Technical Deliverables | Presentation Slides | Rubric |
|------------|----------------------|---------------------|---------|
| Synthesize all v1.x content | Master slide deck | **Slides 1-4:** Title, Agenda, Context | 10 pts |
| Create executive summary | One-page summary | **Slide 24:** Summary | (Quality) |
| Design visual materials | Charts, diagrams, tables | Throughout slides 5-23 | |
| Practice & refine | Timing notes, speaker notes | (presentation delivery) | |
| Prepare Q&A | Q&A backup slides | **Slides 25-30:** Appendix | |

**Presentation Milestone:** Complete 30-min slide deck (20-25 core slides + 5-10 backup)

---

### v3.1.0-v3.3.0: Final Deliverables
| TODO Tasks | Technical Deliverables | Presentation Slides | Rubric |
|------------|----------------------|---------------------|---------|
| Generate PDF | `deliverables/lam-ee-presentation.pdf` | Export from PPTX | Quality |
| Generate PPTX | `deliverables/lam-ee-presentation.pptx` | Master file | |
| Size check (<25MB) | File compression | Both files | |
| Platform compatibility test | Render on Windows/Mac/Linux | Both files | |
| Email 24h before | Email confirmation | Both files attached | |

**Deliverable Milestone:** Email-ready PDF + PPTX

---

## Design Plan → TODO Mapping

### Design Step 1: Identify Key Technical Requirements (25 pts)
**PDF Requirement:** "Identify key technical requirements, including system, electrical, and other relevant specifications."

**Maps to TODO phases:**
- ✅ **v1.1.0:** Quality Metrics Definition (defines success criteria)
- ✅ **v1.2.0:** Requirements Analysis (core deliverable)

**Deliverables:**
- `source/requirements.yaml` (SSOT)
- `artifacts/requirements.md` (generated human-readable)
- `artifacts/rubric-reports/req-audit-report.md` (compliance check)
- `artifacts/rubric-reports/req-traceability-report.md` (coverage matrix)

**Phase Complete When:**
- [ ] 15-20 SMART requirements defined
- [ ] 100% requirements have verification methods
- [ ] Standards compliance addressed (FCC/CE, UL, ADA)
- [ ] Traceability matrix complete
- [ ] `/rubric-eval` Category 1 score ≥ 20/25 (80%)

---

### Design Step 2: Develop Multiple Alternative Solutions (25 pts)
**PDF Requirement:** "Develop and describe multiple alternative solutions."

**Maps to TODO phases:**
- ✅ **v1.3.0:** Solution Architecture Development (core deliverable)

**Deliverables:**
- `docs/architecture.md` (3+ architectures with block diagrams)
- `resources/diagrams/architecture-*.png` (visual block diagrams)
- `reference/datasheets/` (component research)

**Phase Complete When:**
- [ ] 3+ distinct architectures defined
- [ ] Block diagrams for each architecture
- [ ] Component families identified (STM32, TI expanders, etc.)
- [ ] Pros/cons for each approach documented
- [ ] At least 1 creative/non-obvious solution
- [ ] `/rubric-eval` Category 2 score ≥ 20/25 (80%)

---

### Design Step 3: Evaluate Solutions - Trade-off Analysis (30 pts) ← HIGHEST
**PDF Requirement:** "Evaluate the proposed solutions by discussing their **advantages and disadvantages**, as well as **any other considerations** that influenced your final selection."

**Guide:** See `docs/tradeoff-analysis-guide.md` for complete methodology

**Maps to TODO phases:**
- ✅ **v1.4.0:** Trade-off Analysis (core deliverable)

**Deliverables:**
- `docs/tradeoffs.md` (evaluation framework + quantitative comparison + sensitivity)
- `resources/calculations/bom-cost-estimate.xlsx` (cost comparison)
- `resources/calculations/power-budget.xlsx` (battery life analysis)
- `resources/calculations/timeline-gantt.xlsx` (schedule feasibility)

**Phase Complete When:**
- [ ] **Evaluation Framework Defined:**
  - [ ] 7-10 evaluation criteria (time, cost, DFM, risk, UX, etc.)
  - [ ] Weights assigned (sum to 100%, justified)
  - [ ] Assumptions documented (market, customer, budget, priorities)
- [ ] **Quantitative Comparison:**
  - [ ] Cost comparison (BOM: qty 1, 100, 1000)
  - [ ] Power budget (battery life for each architecture)
  - [ ] Timeline feasibility (parts lead time, integration complexity)
  - [ ] Weighted scoring matrix (which architecture scores highest?)
- [ ] **Advantages & Disadvantages:**
  - [ ] For EACH architecture: strengths, weaknesses, when it wins, when it fails
- [ ] **Sensitivity Analysis (5/30 pts - CRITICAL):**
  - [ ] Stakeholder value sensitivity (≥3 scenarios: what if they value cost>time? risk>speed?)
  - [ ] External constraint sensitivity (≥3 scenarios: cost 2x? timeline -50%? part unavailable?)
  - [ ] Robustness matrix (which wins across scenarios?)
- [ ] **Other Considerations:**
  - [ ] Supply chain (lead times, multi-source, geography)
  - [ ] Team expertise (familiar vs new tech)
  - [ ] Tooling/equipment (existing vs new capex)
  - [ ] Risk tolerance (proven vs cutting edge)
- [ ] **Final Recommendation:**
  - [ ] Data-driven selection with clear justification
  - [ ] Conditions under which recommendation changes
- [ ] `/rubric-eval` Category 3 score ≥ 24/30 (80%)

---

### Design Step 4: Path to Production (20 pts)
**PDF Requirement:** "Outline the process for transitioning the concept from initial design to volume production."

**Guide:** See `docs/production-plan-guide.md` for complete methodology

**Maps to TODO phases:**
- ✅ **v1.5.0:** Recommended Solution (core deliverable)

**Deliverables:**
- `docs/solution.md` ⭐ **PRIMARY ARTIFACT** (final architecture + complete production plan)
- `resources/diagrams/final-architecture.png` (selected architecture block diagram)
- `resources/schematics/` (preliminary schematic concepts - power, MCU, I/O, comm)
- `resources/calculations/timeline-gantt.xlsx` ⭐ **CRITICAL** (detailed 2-month week-by-week Gantt chart)

**Phase Complete When:**
- [ ] **Architecture selection justified** (data-driven from v1.4.0 decision matrix)
- [ ] **Block diagram** (`final-architecture.png`)
- [ ] **Preliminary schematics** (power, MCU, I/O, comm - show electrical depth)
- [ ] **2-month Gantt chart** ⭐ (`timeline-gantt.xlsx` - week-by-week with critical path)
- [ ] **Pilot production strategy** (10-100 units, validation plan, success criteria)
- [ ] **DFM considerations** (PCB SMT, mechanical, component multi-sourcing)
- [ ] **Manufacturing plan** (assembly process, test strategy, CM requirements)
- [ ] **Supply chain analysis** (lead times, long-lead items ordered Week 1-2)
- [ ] **Risk mitigation** (timeline, cost, technical, supply chain - with mitigation plans)
- [ ] **Scale strategy** (pilot → 1K → 10K+ with investments at each stage)
- [ ] **`docs/solution.md` complete** (10 sections per production-plan-guide.md)
- [ ] `/rubric-eval` Category 4 score ≥ 16/20 (80%)

---

## TODO Phase Alignment Check

### Current TODO Structure
```
v0.1.0: Project Setup ✅ COMPLETE
v1.1.0: Quality Metrics Definition ✅ COMPLETE
v1.2.0: Requirements Analysis → Design Step 1 (25 pts)
v1.3.0: Solution Architectures → Design Step 2 (25 pts)
v1.4.0: Trade-off Analysis → Design Step 3 (30 pts) ← HIGHEST WEIGHT
v1.5.0: Recommended Solution → Design Step 4 (20 pts)
v1.6.0: Phase 1 Self-Assessment → Overall quality check (85+ pts)
v2.0.0: Presentation Development → 30-min presentation
v3.0.0: Final Deliverables → PDF/PPTX generation
v4.0.0: Interview Prep → AI strategy, EE review
```

### Alignment Status: ✅ EXCELLENT

**The TODO structure perfectly maps to the 4-step design scope!**

**Refinements Needed:**
1. Add "Presentation Milestone" to each phase (v1.2.0 → v1.5.0)
2. Ensure rubric evaluation after each phase (gate decision)
3. Link each phase back to design-plan.md explicitly

---

## Recommended TODO Enhancements

### Add to Each Technical Phase:

**v1.2.0: Requirements Analysis**
```markdown
- [ ] **Design Plan Alignment:** Complete Design Step 1 (PDF p.10)
- [ ] **Presentation Milestone:** Draft "Constraint Tripod" slide
- [ ] **Gate Decision:** Run `/rubric-eval` → Category 1 ≥ 20/25
```

**v1.3.0: Solution Architectures**
```markdown
- [ ] **Design Plan Alignment:** Complete Design Step 2 (PDF p.10)
- [ ] **Presentation Milestone:** Draft architecture comparison slides (3+ block diagrams)
- [ ] **Gate Decision:** Run `/rubric-eval` → Category 2 ≥ 20/25
```

**v1.4.0: Trade-off Analysis**
```markdown
- [ ] **Design Plan Alignment:** Complete Design Step 3 (PDF p.10) ← HIGHEST WEIGHT (30 pts)
- [ ] **Presentation Milestone:**
  - Draft Evaluation Framework slide (criteria + weights)
  - Draft Decision Matrix slide (THE MONEY SLIDE - weighted scores)
  - Draft Sensitivity Analysis slide (robustness matrix)
  - Draft Advantages/Disadvantages comparison
- [ ] **Gate Decision:** Run `/rubric-eval` → Category 3 ≥ 24/30
  - ⚠️ RED FLAG: Missing sensitivity analysis = automatic -5 pts (fails gate!)
```

**v1.5.0: Recommended Solution**
```markdown
- [ ] **Design Plan Alignment:** Complete Design Step 4 (PDF p.10)
- [ ] **Presentation Milestone:** Draft "End State" slide + Gantt chart
- [ ] **Gate Decision:** Run `/rubric-eval` → Category 4 ≥ 16/20
```

---

## Success Metrics (from design-plan.md)

### Phase 1 (Technical Analysis)
- ✅ 15-20 SMART requirements defined
- ✅ 3+ architectures with block diagrams
- ✅ Quantitative trade-off analysis (cost, power, timeline)
- ✅ Detailed 2-month pilot production plan
- ✅ Overall rubric score ≥85/100

### Phase 2 (Presentation)
- ✅ 20-25 slides, 30-minute delivery
- ✅ Content balanced across 4 design steps
- ✅ 3+ practice runs, all ≤30 min
- ✅ 10-15 Q&A questions prepared

### Phase 3 (Deliverables)
- ✅ PDF + PPTX <25MB total
- ✅ No errors, renders on all platforms
- ✅ Emailed 24 hours before interview

### Phase 4 (Prep)
- ✅ AI strategy clear and rehearsed
- ✅ EE fundamentals reviewed
- ✅ Whiteboard practice complete

---

## Critical Path (Rubric-Weighted)

**Focus effort on highest-rubric-weight phases:**

1. **v1.4.0: Trade-off Analysis** (30 pts) ← **MOST IMPORTANT**
   - Quantitative data (cost, power, timeline)
   - Decision matrix with clear justification
   - Sensitivity analysis

2. **v1.2.0: Requirements** (25 pts)
   - SMART requirements
   - Standards compliance

3. **v1.3.0: Architectures** (25 pts)
   - 3+ distinct solutions
   - Block diagrams

4. **v1.5.0: Production** (20 pts)
   - 2-month pilot timeline
   - Risk mitigation

5. **Documentation** (10 pts)
   - Throughout all phases

---

## Next Actions

1. **Immediate:**
   - [ ] Update TODO.md with "Design Plan Alignment" sections
   - [ ] Add "Presentation Milestone" to v1.2.0 → v1.5.0
   - [ ] Link each phase back to design-plan.md

2. **Before proceeding to v1.3.0:**
   - [ ] Complete v1.2.0 requirements population
   - [ ] Run `/req-audit` (compliance check)
   - [ ] Run `/rubric-eval` (Category 1 assessment)
   - [ ] Gate decision: Proceed only if score ≥ 20/25

3. **Throughout project:**
   - [ ] Run `/rubric-eval` after each phase
   - [ ] Update traceability matrix
   - [ ] Build presentation slides iteratively

---

---

## 📋 Quick Reference: What Gets Created When

### Phase v1.2.0 (Requirements) - Week 1, Days 1-2
**Work:** Define requirements, competitive analysis, assumptions
**Creates:** `requirements.yaml`, `assumptions-register.md`
**Becomes:** Slides 5-8 (Requirements, Assumptions, Competitive Analysis)

### Phase v1.3.0 (Architectures) - Week 1, Days 3-5
**Work:** Research actuators, design 3+ architectures, block diagrams
**Creates:** `architecture.md`, `diagrams/arch-A.png`, `diagrams/arch-B.png`, `diagrams/arch-C.png`
**Becomes:** Slides 9-12 (Architecture comparison)

### Phase v1.4.0 (Trade-offs) - Week 2, Days 1-3 ⭐ CRITICAL
**Work:** BOM cost, power budget, timeline, decision matrix, sensitivity analysis
**Creates:** `tradeoffs.md`, `bom-cost.xlsx`, `power-budget.xlsx`, `decision-matrix.xlsx`
**Becomes:** Slides 13-19 (Evaluation, Cost, Pros/Cons, Decision, Sensitivity, Recommendation)

### Phase v1.5.0 (Production Plan) - Week 2, Day 4
**Work:** Final architecture, 2-month Gantt, pilot strategy, DFM, risk mitigation
**Creates:** `solution.md`, `final-architecture.png`, `timeline-gantt.xlsx`
**Becomes:** Slides 20-23 (Selected Architecture, Timeline, Production Strategy, Risks)

### Phase v2.1.0-v2.5.0 (Presentation) - Week 2, Day 5
**Work:** Synthesize all v1.x deliverables into slide deck, create visuals, practice
**Creates:** `presentation.pptx` (20-25 slides)
**Becomes:** Final presentation file

### Phase v3.1.0-v3.3.0 (Deliverables) - Before Interview
**Work:** Export PDF, compress, test compatibility
**Creates:** `lam-ee-presentation.pdf`, `lam-ee-presentation.pptx`
**Becomes:** Email attachments sent 24h before interview

---

## 🎬 Presentation Slide Breakdown (20-25 slides)

| Slide # | Content | Source Deliverable | Phase |
|---------|---------|-------------------|-------|
| 1 | Title Slide | Synthesized | v2.1.0 |
| 2 | Agenda | design-plan.md | v2.1.0 |
| 3 | Design Context | design-plan.md | v2.1.0 |
| 4 | Product Vision | design-plan.md | v2.1.0 |
| 5 | Requirements Overview | requirements.yaml | v1.2.0 |
| 6 | Key Assumptions | assumptions-register.md | v1.2.0 |
| 7 | Competitive Analysis | assumptions-register.md | v1.2.0 |
| 8 | Standards Awareness | requirements.yaml (NFR-STD-001) | v1.2.0 |
| 9 | Architecture A | architecture.md + diagrams | v1.3.0 |
| 10 | Architecture B | architecture.md + diagrams | v1.3.0 |
| 11 | Architecture C | architecture.md + diagrams | v1.3.0 |
| 12 | Key Components | architecture.md | v1.3.0 |
| 13 | Evaluation Framework | tradeoffs.md | v1.4.0 |
| 14 | Cost Comparison | bom-cost.xlsx | v1.4.0 |
| 15 | Power Budget | power-budget.xlsx | v1.4.0 |
| 16 | Pros/Cons Matrix | tradeoffs.md | v1.4.0 |
| 17 | **Decision Matrix** 💰 | decision-matrix.xlsx | v1.4.0 |
| 18 | Sensitivity Analysis | tradeoffs.md | v1.4.0 |
| 19 | Recommendation | tradeoffs.md | v1.4.0 |
| 20 | Selected Architecture | solution.md + final-arch.png | v1.5.0 |
| 21 | 2-Month Timeline | timeline-gantt.xlsx | v1.5.0 |
| 22 | Pilot Production Strategy | solution.md | v1.5.0 |
| 23 | Risk Mitigation | solution.md | v1.5.0 |
| 24 | Summary | Synthesized | v2.5.0 |
| 25-30 | Appendix/Q&A | All backup materials | v2.5.0 |

**Total:** 24 core slides + 5-6 backup = 30-min presentation

---

## 🔑 Key Insight: Build Once, Use Twice

**Every technical deliverable serves TWO purposes:**
1. ✅ **Engineering rigor** - Detailed analysis in markdown/Excel
2. ✅ **Presentation content** - Summarized in slides

**Example: BOM Cost Analysis**
- **v1.4.0 Work:** Create detailed `bom-cost.xlsx` with 50+ line items, 3 volume scenarios
- **v2.3.0 Slide:** Simplify to 3-bar chart comparing architectures at 1K volume
- **v2.5.0 Backup:** Keep full spreadsheet as appendix slide for Q&A

**Don't do work twice!** Write detailed docs in v1.x, extract slide summaries in v2.x.

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-08 | Spencer Barrett | Initial TODO/design-plan mapping |
| 2.0.0 | 2025-10-08 | Spencer Barrett | Added complete artifact flow: TODO → Deliverables → Slides |
| 3.0.0 | 2025-10-08 | Spencer Barrett | Added Step 4 artifact clarity (`solution.md` + `production-plan-guide.md`), quick check table for all 4 PDF requirements |
