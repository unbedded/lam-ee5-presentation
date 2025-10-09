# Lam Research EE Interview - Evaluation Rubric

**Project:** Braille Display Device - EE Concept Evaluation
**Source:** `docs/problem-statement.md` (derived from PDF p.10)
**Version:** 1.0.0
**Date:** 2025-10-05

---

## Overview

This rubric defines the evaluation criteria for the Lam Research EE Concept Evaluation interview. It maps directly to the 4 requirements specified in the assignment (PDF p.10).

**Maximum Score:** 100 points
**Target Score:** 85+ points (Excellence threshold)

---

## Evaluation Categories

### 1. Technical Requirements Identification (25 points)

**Source:** PDF p.10 Scope Item 1 - "Identify key technical requirements, including system, electrical, and other relevant specifications."

#### Performance Levels

| Level | Score | Criteria |
|-------|-------|----------|
| **Excellent** | 23-25 | • All requirement categories identified (system, electrical, manufacturing, user)<br>• Requirements are specific, measurable, and testable<br>• Proper prioritization (P0/P1/P2/P3)<br>• Clear traceability to source documents<br>• Standards/compliance requirements researched |
| **Good** | 18-22 | • Most requirement categories covered<br>• Requirements mostly measurable<br>• Basic prioritization present<br>• Some traceability shown |
| **Adequate** | 13-17 | • Basic requirements identified<br>• Some categories missing<br>• Vague or incomplete specs<br>• Limited prioritization |
| **Poor** | 0-12 | • Minimal requirements identified<br>• Major gaps in coverage<br>• Not measurable or testable |

#### Detailed Scoring

**Requirement Coverage (10 points)**
- [ ] System requirements (I/O count, functionality) (3 pts)
- [ ] Electrical requirements (power, control, communication) (3 pts)
- [ ] Manufacturing requirements (cost, volume, timeline) (2 pts)
- [ ] User/accessibility requirements (2 pts)

**Requirement Quality (10 points)**
- [ ] Requirements are specific and measurable (3 pts)
- [ ] Proper prioritization (P0-Critical to P3-Low) (2 pts)
- [ ] Acceptance criteria defined (3 pts)
- [ ] Verification methods specified (2 pts)

**Standards & Compliance (5 points)**
- [ ] Relevant standards researched (EMI, safety, accessibility) (3 pts)
- [ ] Compliance requirements documented (2 pts)

---

### 2. Alternative Solution Development (25 points)

**Source:** PDF p.10 Scope Item 2 - "Develop and describe multiple alternative solutions."

#### Performance Levels

| Level | Score | Criteria |
|-------|-------|----------|
| **Excellent** | 23-25 | • 3+ distinct architectures developed<br>• Each architecture fully described (block diagrams, schematics)<br>• Wide solution diversity (different actuator types, control strategies, interfaces)<br>• Creative, non-obvious approaches considered<br>• Technical depth appropriate for concept phase |
| **Good** | 18-22 | • 3 architectures developed<br>• Adequately described<br>• Some diversity shown<br>• Reasonable technical depth |
| **Adequate** | 13-17 | • 2 architectures developed<br>• Basic descriptions<br>• Limited diversity<br>• Superficial analysis |
| **Poor** | 0-12 | • ≤1 architecture developed<br>• Incomplete descriptions<br>• No diversity shown |

#### Detailed Scoring

**Solution Diversity (10 points)**
- [ ] 3+ actuator technologies explored (piezo, solenoid, SMA, motor) (4 pts)
- [ ] 2+ control architectures (MCU, FPGA, distributed) (3 pts)
- [ ] 2+ communication interfaces (BLE, USB-C, WiFi) (3 pts)

**Solution Description Quality (10 points)**
- [ ] Block diagrams for each architecture (4 pts)
- [ ] Component selection justified (3 pts)
- [ ] Power/signal flow described (3 pts)

**Technical Depth (5 points)**
- [ ] Appropriate detail for concept phase (3 pts)
- [ ] Feasibility considerations addressed (2 pts)

---

### 3. Solution Evaluation & Trade-off Analysis (30 points)

**Source:** PDF p.10 Scope Item 3 - "Evaluate the proposed solutions by discussing their advantages and disadvantages, as well as **any other considerations** that influenced your final selection."

**⚠️ CRITICAL:** "Any other considerations" = sensitivity analysis, supply chain, expertise, tooling, market timing, risk tolerance

#### Performance Levels

| Level | Score | Criteria |
|-------|-------|----------|
| **Excellent** | 27-30 | • Quantitative comparison (cost, power, size, complexity, timeline)<br>• Rigorous trade-off analysis with clear decision criteria<br>• Advantages and disadvantages thoroughly analyzed<br>• **Sensitivity analysis** ("what if" scenarios)<br>• Risk assessment included<br>• Final selection well-justified with data<br>• Considerations beyond obvious (supply chain, expertise, tooling) |
| **Good** | 21-26 | • Quantitative data provided<br>• Good trade-off analysis<br>• Pros/cons covered<br>• Some sensitivity analysis<br>• Selection justified<br>• Some risk considerations |
| **Adequate** | 15-20 | • Basic comparison present<br>• Some trade-offs discussed<br>• Qualitative analysis mostly<br>• Weak justification<br>• No sensitivity analysis |
| **Poor** | 0-14 | • Minimal comparison<br>• No trade-off analysis<br>• Selection unjustified |

#### Detailed Scoring

**Quantitative Analysis (10 points)**
- [ ] Cost comparison (BOM estimates) (2 pts)
- [ ] Power budget calculations (2 pts)
- [ ] Size/complexity metrics (2 pts)
- [ ] Timeline feasibility analysis (2 pts)
- [ ] Comparison matrix/table (2 pts)

**Trade-off Analysis (8 points)**
- [ ] Clear decision criteria established (2 pts)
- [ ] Advantages thoroughly analyzed (3 pts)
- [ ] Disadvantages honestly assessed (3 pts)

**Sensitivity Analysis (5 points) ← NEW**
- [ ] "What if cost doubles?" scenario (1 pt)
- [ ] "What if timeline compresses?" scenario (1 pt)
- [ ] "What if key component unavailable?" scenario (1 pt)
- [ ] "What if volume targets change?" scenario (1 pt)
- [ ] Robustness comparison across solutions (1 pt)

**Risk Assessment (4 points)**
- [ ] Technical risks identified (1 pt)
- [ ] Timeline risks assessed (1 pt)
- [ ] Supply chain risks considered (1 pt)
- [ ] Mitigation strategies proposed (1 pt)

**Final Selection Justification (3 points)**
- [ ] Data-driven decision (2 pts)
- [ ] Clear rationale provided (1 pt)

---

### 4. Path to Production (20 points)

**Source:** PDF p.10 Scope Item 4 - "Outline the process for transitioning the concept from initial design to volume production."

#### Performance Levels

| Level | Score | Criteria |
|-------|-------|----------|
| **Excellent** | 18-20 | • Detailed production plan with timeline<br>• 2-month constraint explicitly addressed<br>• Critical path analysis included<br>• Supplier/component lead times considered<br>• Manufacturing process defined (DFM considerations)<br>• Testing/validation strategy outlined<br>• Risk mitigation for timeline |
| **Good** | 14-17 | • Production plan present<br>• Timeline constraint addressed<br>• Manufacturing process outlined<br>• Some risk mitigation |
| **Adequate** | 10-13 | • Basic production outline<br>• Timeline mentioned<br>• Minimal manufacturing detail |
| **Poor** | 0-9 | • Vague or missing production plan<br>• Timeline constraint ignored |

#### Detailed Scoring

**Production Timeline (8 points)**
- [ ] Detailed schedule with milestones (3 pts)
- [ ] 2-month constraint explicitly addressed (3 pts)
- [ ] Critical path identified (2 pts)

**Manufacturing Plan (7 points)**
- [ ] DFM considerations (PCB, assembly) (3 pts)
- [ ] Component sourcing strategy (2 pts)
- [ ] Testing/validation strategy (2 pts)

**Risk Mitigation (5 points)**
- [ ] Timeline risks identified (2 pts)
- [ ] Supply chain risks addressed (2 pts)
- [ ] Mitigation strategies defined (1 pt)

---

## Supporting Categories (Non-Interview Specific)

### 5. Documentation Quality (10 points)

**Clarity & Professionalism**
- [ ] Clear, well-organized documents (3 pts)
- [ ] Professional diagrams/visuals (3 pts)
- [ ] Proper technical writing (2 pts)
- [ ] References cited (2 pts)

### 6. Presentation Readiness (10 points)

**30-Minute Presentation Preparation** (evaluated in Phase 2)
- [ ] Slides organized for 30-min delivery (4 pts)
- [ ] Key decisions highlighted (3 pts)
- [ ] Visual clarity (diagrams, charts) (3 pts)

---

## Scoring Summary

| Category | Weight | Max Points |
|----------|--------|------------|
| 1. Technical Requirements Identification | 25% | 25 |
| 2. Alternative Solution Development | 25% | 25 |
| 3. Solution Evaluation & Trade-off Analysis | 30% | 30 |
| 4. Path to Production | 20% | 20 |
| 5. Documentation Quality | 10% | 10 |
| 6. Presentation Readiness | 10% | 10 |
| **TOTAL** | | **100** |

**Note:** Categories 5-6 overlap across Phase 1 and Phase 2 work.

---

## Interpretation Guide

| Score | Grade | Interpretation |
|-------|-------|----------------|
| 85-100 | Excellent | Outstanding - exceeds interview expectations |
| 70-84 | Good | Professional quality - meets expectations |
| 55-69 | Adequate | Acceptable but needs improvement |
| 0-54 | Poor | Significant gaps - requires revision |

---

## Incremental Evaluation Points

The rubric can be applied incrementally to each Phase 1 deliverable:

### v1.1.0: Quality Metrics (`docs/quality-metrics.md`)
- Evaluate: Completeness, measurability, clarity
- Partial scoring: Requirements definition quality

### v1.2.0: Requirements Analysis (`docs/requirements.md`)
- Evaluate: Category 1 (Technical Requirements) - full 25 points
- Check: Coverage, quality, prioritization, traceability

### v1.3.0: Solution Architectures (`docs/architecture.md`)
- Evaluate: Category 2 (Alternative Solutions) - full 25 points
- Check: Diversity, descriptions, technical depth

### v1.4.0: Trade-off Analysis (`docs/tradeoffs.md`)
- Evaluate: Category 3 (Trade-offs) - full 30 points
- Check: Quantitative data, justification, risk assessment

### v1.5.0: Recommended Solution (`docs/solution.md`)
- Evaluate: Category 4 (Production Path) - full 20 points
- Check: Timeline, manufacturing plan, risk mitigation

### v1.6.0: Phase 1 Complete
- Evaluate: All categories (100 points)
- Generate: Final Phase 1 rubric evaluation report
- Generate: Requirements traceability report

---

## Critical Success Factors

### Must-Haves (to reach 70+ points)
✅ All 4 scope items addressed (requirements, solutions, trade-offs, production)
✅ 3+ alternative architectures developed
✅ Quantitative trade-off analysis with data
✅ 2-month timeline explicitly addressed
✅ Clear final solution justification

### Excellence Markers (to reach 85+ points)
⭐ Deep technical analysis with calculations
⭐ Creative, non-obvious solution approaches
⭐ Rigorous risk assessment and mitigation
⭐ Professional-quality documentation and diagrams
⭐ Comprehensive production plan with critical path

---

## Alignment with Lam Research Criteria

**What Lam is Evaluating:**
1. **Technical Competence** - Can you identify requirements and design solutions?
2. **Engineering Judgment** - Can you evaluate trade-offs and make justified decisions?
3. **Production Mindset** - Do you understand manufacturing/timeline constraints?
4. **Communication** - Can you explain your thinking clearly?

**This Rubric Maps To:**
- Technical Competence → Categories 1 & 2 (50 points)
- Engineering Judgment → Category 3 (30 points)
- Production Mindset → Category 4 (20 points)
- Communication → Categories 5 & 6 (documentation/presentation)

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-05 | Spencer Barrett | Initial rubric from problem statement |

---

## References

- **Source:** `docs/problem-statement.md`
- **PDF Reference:** `docs/reference/Interview Overview and Concept Evaluation - EE Presentation.pdf` (p.10)
- **Evaluation Command:** `.claude/commands/rubric-eval.md`
- **Reports:** `artifacts/rubric-reports/`
