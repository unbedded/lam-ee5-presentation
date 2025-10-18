# Presentation Strategy - Begin With The End In Mind

**Project:** LAM Research EE Concept Evaluation
**Version:** 1.0.0
**Date:** 2025-10-08
**Purpose:** Strategic plan for 30-minute presentation aligned with interview rubric

---

## Executive Summary

**Core Constraint:** 2 months to pilot production (10-100 validation units)

**The Tripod Trade-off:**
- **Requirements** (what we must deliver)
- **Schedule** (2-month hard constraint)
- **Cost** (low-cost, high-volume design)

**Presentation Philosophy:** "Begin with the end in mind" - show the DELIVERABLE first, then justify the path.

---

## The 4 Pillars (Interview Rubric Alignment)

### Rubric Structure (100 points)
| Pillar | Points | Time Allocation | Focus |
|--------|--------|-----------------|-------|
| 1. Technical Requirements | 25 pts | 5-7 min | What we must deliver (scope, constraints) |
| 2. Alternative Solutions | 25 pts | 8-10 min | How we could solve it (3+ architectures) |
| 3. Trade-off Analysis | **30 pts** | 8-10 min | **WHY we chose solution** (data-driven) |
| 4. Path to Production | 20 pts | 5-7 min | HOW we get to pilot in 2 months |
| Documentation Quality | 10 pts | Throughout | Clear, professional, visual |

**Key Insight:** Pillar 3 (Trade-offs) is highest weighted → spend most time here!

---

## Presentation Flow: "End-First" Structure

### Option A: Traditional (Requirements → Solution)
```
Problem → Requirements → Alternatives → Trade-offs → Recommendation → Timeline
```
**Risk:** Audience loses thread, forgets context by the time we reach recommendation

### Option B: "End-First" (Recommendation → Justification) ✅ RECOMMENDED
```
1. The Deliverable (2 min)
   - Here's what we're building (show final architecture diagram)
   - 32-char braille display, BLE connectivity, 4-hour battery, $X BOM
   - Pilot production in 2 months, scales to high volume

2. The Constraint Tripod (3 min)
   - Requirements: 192 control signals, portable, low-cost
   - Schedule: 2-month hard deadline to pilot
   - Cost: Target BOM < $100, design for >10K/year volume
   - These three constraints drove ALL decisions

3. The Alternatives We Evaluated (8 min)
   - Architecture A: Piezo + MCU + BLE
   - Architecture B: Solenoid + FPGA + USB-C
   - Architecture C: SMA + Distributed MCU + WiFi
   - Each addresses requirements differently

4. Why We Chose Architecture [X] (10 min) ← MOST TIME HERE
   - Quantitative comparison (cost, power, timeline, risk)
   - BOM: $XX vs $YY vs $ZZ
   - Power: Xh battery vs Yh vs Zh
   - Timeline: Parts lead time, integration complexity
   - Risk: Technical maturity, supply chain
   - Decision matrix weighted for 2-month constraint

5. Path to Pilot Production (5 min)
   - Week-by-week Gantt chart
   - Critical path: Actuator sourcing, PCB fab, integration
   - Risk mitigation: Long-lead items identified, alternates sourced
   - Pilot validates design before mass production

6. Q&A (remaining time)
```

**Why this works:**
- Audience knows the answer upfront (reduces cognitive load)
- Trade-offs make sense because they know what we're comparing TO
- Justification is the star (aligns with highest rubric weight)
- Timeline feels achievable because we showed feasibility data

---

## The Constraint Tripod (Core Framing)

### Visual: Triangle Diagram
```
        REQUIREMENTS
        (192 signals)
             /\
            /  \
           /    \
          /      \
         /        \
        /          \
    SCHEDULE -------- COST
   (2 months)      ($100 BOM)
```

**Key Message:**
> "Every decision in this design is a trade-off between these three constraints.
> We can't optimize all three simultaneously - the 2-month schedule constraint
> forces us to prioritize COTS components and proven technology over custom
> optimization."

**Examples:**
- **Requirement vs Cost:** 192 signals needs I/O expansion → adds cost
- **Schedule vs Cost:** COTS actuators faster but more expensive than custom
- **Schedule vs Requirements:** Pilot run (10-100 units) validates before mass production

---

## What Must Be Delivered in 2 Months

### Deliverable 1: Production-Ready Design
- [ ] Complete schematics (power, MCU, I/O, communication)
- [ ] PCB layout (DFM validated, ready for fab)
- [ ] BOM with sourcing (all parts < 6 week lead time)
- [ ] Enclosure design (CAD model, ready for 3D print or molding)
- [ ] Firmware architecture (not fully coded, but architected)

### Deliverable 2: Pilot Production (10-100 units)
- [ ] PCBs fabricated and assembled
- [ ] Actuators sourced and integrated
- [ ] Basic firmware functional (braille display + BLE)
- [ ] Test plan executed (validates requirements)
- [ ] Failure modes identified (document for mass production)

### Deliverable 3: Manufacturing Package
- [ ] Assembly instructions (for CM or internal)
- [ ] Test procedures (functional, electrical, mechanical)
- [ ] DFM report (what worked, what needs optimization)
- [ ] Risk register (supply chain, technical, timeline)
- [ ] Scale plan (path from pilot → 1K → 10K units)

**Timeline Realism Check:**
- Week 1-2: Component selection, schematic design
- Week 3-4: PCB layout, order long-lead parts
- Week 5-6: PCB fab, firmware architecture
- Week 7: Assembly, integration
- Week 8: Test, validate, iterate

**Critical Path:** Actuator lead time (longest, must order early)

---

## Alignment: TODO.md → Presentation Structure

### Current TODO Structure (by phase)
```
v1.2.0: Requirements Analysis
v1.3.0: Solution Architectures
v1.4.0: Trade-off Analysis
v1.5.0: Recommended Solution
v1.6.0: Self-Assessment
v2.0.0: Presentation Development
```

### Proposed TODO Enhancement: Add Cross-Links

**In each technical phase, add "Presentation Hook":**

```markdown
### v1.2.0: Requirements Analysis
- [ ] Populate requirements.yaml
  - **Presentation Hook:** Create "Constraint Tripod" slide (Req/Schedule/Cost)

### v1.3.0: Solution Architectures
- [ ] Design 3+ architectures
  - **Presentation Hook:** Create comparison table (one-pager per architecture)

### v1.4.0: Trade-off Analysis
- [ ] Build cost/power/timeline comparison
  - **Presentation Hook:** Create decision matrix slide (THIS IS THE MONEY SLIDE)

### v1.5.0: Recommended Solution
- [ ] Detailed architecture + timeline
  - **Presentation Hook:** Create "End State" slide (show THIS first in presentation)
```

**Why:** Ensures every technical phase feeds directly into presentation narrative.

---

## Presentation Slide Outline (25 slides, 30 min)

### Act 1: The Deliverable (Slides 1-5, 5 min)
1. Title slide
2. **The End State** - Final architecture diagram
3. **The Deliverable** - What we're building in 2 months
4. **The Constraint Tripod** - Req/Schedule/Cost
5. **The Challenge** - 192 signals, portable, low-cost, 2-month timeline

### Act 2: The Alternatives (Slides 6-13, 8 min)
6. Requirements summary (key specs)
7. Architecture A - Block diagram
8. Architecture A - Pros/cons
9. Architecture B - Block diagram
10. Architecture B - Pros/cons
11. Architecture C - Block diagram
12. Architecture C - Pros/cons
13. Comparison matrix (all three side-by-side)

### Act 3: The Decision (Slides 14-19, 10 min) ← CORE
14. **Trade-off criteria** (cost, power, timeline, risk weights)
15. **Cost comparison** - BOM breakdown chart
16. **Power comparison** - Battery life chart
17. **Timeline comparison** - Parts lead time, integration complexity
18. **Risk comparison** - Risk matrix (likelihood × impact)
19. **Decision matrix** - Weighted scoring → clear winner

### Act 4: The Path (Slides 20-24, 5 min)
20. **Pilot production timeline** - 8-week Gantt chart
21. **Critical path** - Actuator sourcing, PCB fab
22. **Risk mitigation** - Long-lead items, alternates, buffers
23. **Manufacturing plan** - DFM, test strategy, scale path
24. **What pilot validates** - Design, tolerances, failure modes

### Act 5: Wrap-up (Slide 25, 2 min)
25. Summary + Q&A

---

## Key Visuals (Must Create)

### High-Impact Diagrams
1. **Constraint Tripod Triangle** (Requirements/Schedule/Cost)
2. **Final Architecture Block Diagram** (the "end state")
3. **3-Architecture Comparison Table** (side-by-side, visual)
4. **Decision Matrix** (weighted scoring, color-coded winner)
5. **Cost Breakdown Chart** (BOM comparison, qty 1/100/1K)
6. **Battery Life Chart** (power budget → hours of operation)
7. **Timeline Gantt** (8 weeks, critical path highlighted)
8. **Risk Matrix** (2x2: likelihood × impact, mitigation noted)

**Visual Guidelines:**
- Readable from back of room (font ≥ 18pt)
- High contrast (dark text on light background)
- One key message per slide
- Use color strategically (green = good, red = risk, blue = neutral)

---

## Presentation Practice Strategy

### Dry Run 1: Content Complete (target 35 min)
- Goal: Get all content on slides
- Expected: Run over time, awkward transitions
- Action: Identify what to cut

### Dry Run 2: Refined (target 32 min)
- Goal: Smooth delivery, timed sections
- Expected: Still a bit long, some stumbles
- Action: Refine wording, practice transitions

### Dry Run 3: Polished (target 28 min)
- Goal: Confident delivery, 2-min buffer
- Expected: Smooth, professional
- Action: Memorize key stats, practice Q&A

### Q&A Preparation (10-15 questions)
**Technical deep-dives:**
1. "Why not use [other actuator technology]?"
2. "What if parts lead time exceeds 6 weeks?"
3. "How do you verify 192 outputs efficiently?"
4. "What's the biggest technical risk?"
5. "How does this scale from 100 to 10K units?"

**Timeline challenges:**
6. "What if you can't meet 2-month deadline?"
7. "Where's the slack in your schedule?"
8. "What's on the critical path?"

**Cost questions:**
9. "What's your BOM cost target?"
10. "How does cost change at 1K vs 10K volume?"

**Design justification:**
11. "Why [your choice] vs [alternative]?"
12. "What assumptions did you make?"

**Wildcard:**
13. "How would you use AI in this project?" (Spencer's differentiator)

---

## Success Criteria (Rubric Alignment)

### Pillar 1: Technical Requirements (25 pts)
- ✅ Clear articulation of 192-signal challenge
- ✅ Constraint tripod explained (Req/Schedule/Cost)
- ✅ Requirements traceable to PDF source
- ✅ Standards awareness (FCC/CE, UL, ADA)

### Pillar 2: Alternative Solutions (25 pts)
- ✅ 3+ distinct architectures shown
- ✅ Block diagrams for each (clear, readable)
- ✅ Component families identified (STM32, TI expanders, etc.)
- ✅ At least one creative/non-obvious approach

### Pillar 3: Trade-off Analysis (30 pts) ← HIGHEST WEIGHT
- ✅ Quantitative data (cost, power, timeline with numbers)
- ✅ Decision criteria transparent (weights shown)
- ✅ Risk assessment (likelihood × impact matrix)
- ✅ Sensitivity analysis ("what if cost 2x?")
- ✅ Final selection justified by data (not gut feel)

### Pillar 4: Path to Production (20 pts)
- ✅ 2-month Gantt chart (week-by-week)
- ✅ Critical path identified (actuator sourcing)
- ✅ Pilot run strategy explained (10-100 units, validates design)
- ✅ Risk mitigation for timeline risks (long-lead items, alternates)
- ✅ Scale path shown (pilot → 1K → 10K)

### Documentation Quality (10 pts)
- ✅ Slides readable, professional
- ✅ Diagrams clear and useful
- ✅ Data visualizations effective (charts, tables)
- ✅ Proper terminology, no typos

**Target Score:** 85+/100 (Excellent level)

---

## TODO Workflow Impact

### Add to TODO.md Structure

**After each technical phase, add presentation milestone:**

```markdown
### v1.2.0: Requirements Analysis
- [ ] Populate requirements.yaml
- [ ] Run /req-audit
- [ ] Run /req-yaml-to-md
- [ ] **Presentation Milestone: Draft Constraint Tripod slide**

### v1.3.0: Solution Architectures
- [ ] Design 3+ architectures
- [ ] Create block diagrams
- [ ] **Presentation Milestone: Draft Architecture comparison slides**

### v1.4.0: Trade-off Analysis
- [ ] Cost/power/timeline comparison
- [ ] Risk analysis
- [ ] **Presentation Milestone: Draft Decision Matrix slide (THE MONEY SLIDE)**

### v1.5.0: Recommended Solution
- [ ] Final architecture selection
- [ ] Detailed timeline
- [ ] **Presentation Milestone: Draft "End State" slide + Gantt chart**

### v2.2.0: Presentation Structure
- [ ] Assemble slides in "End-First" order
- [ ] Dry run 1 (target 35 min)
- [ ] Refine based on timing
```

**Why:** Presentation becomes iterative deliverable, not "oh crap we need slides" at the end.

---

## Key Messages (Memorize These)

1. **On the 2-month constraint:**
   > "We're targeting pilot production in 2 months - 10 to 100 validation units. This verifies the design, manufacturing tolerances, and failure modes before committing to high-volume tooling."

2. **On the constraint tripod:**
   > "Every decision balances three constraints: requirements, schedule, and cost. The 2-month timeline forces us to prioritize COTS components and proven technologies."

3. **On architecture selection:**
   > "We evaluated three distinct architectures. Architecture X won based on quantitative analysis: lowest BOM cost, acceptable battery life, shortest integration time, and lowest technical risk."

4. **On risk mitigation:**
   > "The critical path is actuator sourcing - 6-week lead time. We've identified alternate suppliers and designed for flexibility. If primary supplier delays, we can pivot without redesigning the PCB."

5. **On scale path:**
   > "The design is architected for high volume, but we de-risk with pilot first. Post-pilot, we optimize DFM, negotiate volume pricing, and scale to 10K+ units."

---

## Next Steps

1. **Immediate (v1.2.0):**
   - Complete requirements.yaml population
   - Draft "Constraint Tripod" slide concept

2. **v1.3.0:**
   - Design 3 architectures with this tripod in mind
   - Keep presentation clarity in focus (block diagrams must be slide-ready)

3. **v1.4.0:**
   - Build decision matrix (this becomes THE MONEY SLIDE)
   - Quantitative data must be presentation-ready (charts, not just spreadsheets)

4. **v2.0.0:**
   - Assemble slides in "End-First" order
   - Dry run #1 with timer

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-08 | Spencer Barrett | Initial presentation strategy |

---

**Remember:** The presentation IS the interview. Technical excellence doesn't matter if we can't communicate it clearly in 30 minutes. Begin with the end in mind.
