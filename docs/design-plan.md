# EE Concept Evaluation - Design Plan

## Overview
This document captures the complete design plan for the Lam Research Electrical Engineering Concept Evaluation interview challenge.

**Source:** `reference/interview/Interview Overview and Concept Evaluation - EE Presentation.pdf`

**READ THIS DOCUMENT CAREFULLY** - It defines the 4-step evaluation scope that structures ALL work.

---

## Table of Contents

1. [Design Context](#design-context)
2. [Product Vision](#product-vision)
   - [Objective](#objective)
   - [Function](#function)
3. [Technical Specifications](#technical-specifications)
   - [System Requirements](#system-requirements)
   - [Design Constraints](#design-constraints)
4. [Design Scenario Scope](#design-scenario-scope-pdf-p10)
   - [Step 1: Identify Key Technical Requirements](#step-1-identify-key-technical-requirements)
   - [Step 2: Develop Multiple Alternative Solutions](#step-2-develop-multiple-alternative-solutions)
   - [Step 3: Evaluate Solutions - Trade-off Analysis](#step-3-evaluate-solutions---trade-off-analysis)
   - [Step 4: Path to Production (Volume Manufacturing)](#step-4-path-to-production-volume-manufacturing)
5. [Interview Deliverables](#interview-deliverables)
   - [Presentation Requirements](#presentation-requirements)
   - [Interview Evaluation Criteria](#interview-evaluation-criteria)
   - [Interview Structure](#interview-structure-90-minutes-total)
6. [Reference Information](#reference-information)
   - [Braille Alphabet](#braille-alphabet)
   - [Design Challenge Summary](#design-challenge-summary)
7. [Success Criteria](#success-criteria)

---

## Design Context

**Role:** Electrical Engineer at Company Z
**Timeline:** 2 months to **pilot production** (10-100 validation units)
**Objective:** Lead critical electrical engineering project to meet customer deadline
**Reality:** Pilot validates design before mass production commitment

---

## Product Vision

### Objective
Develop a **portable, low-cost, high-volume companion device** to a cell phone that enables sight-impaired individuals to read text from their mobile device.

### Function
- Display a single line of braille text (32 characters)
- Update the line of braille to read the next line of text after current line is read
- Interface with cell phone to receive text information

---

## Technical Specifications

### System Requirements
- **Input:** Text information from cell phone
- **Output:** Control signals to 32 braille characters
- **Character Definition:** Each character has 6 dots (raised or lowered based on control signals)
- **Total Control Signals:** 192 individual control points (32 characters × 6 dots)

### Design Constraints
- **Portability:** Must be portable companion device
- **Cost:** Low-cost design for high-volume manufacturing
- **Manufacturing:** High-volume production capability
- **Timeline:** Production-ready within 2 months
- **Interface:** Compatible with cell phone connectivity

---

## Design Scenario Scope (PDF p.10)

**CRITICAL:** These 4 steps define the interview evaluation rubric. ALL work must map to these.

**PDF Quote:** "In this scenario, you will be expected to:"

As the lead electrical engineer, you are responsible for designing the electronics system with the following deliverables:

### Step 1: Identify Key Technical Requirements
**Deliverable:** Comprehensive requirements analysis

**PDF Quote:** "Identify key technical requirements, including system, electrical, and other relevant specifications."

**Methodology:**
1. **Extract explicit requirements from PDF** (system, electrical, manufacturing)
2. **Derive requirements from constraints** (power budget from battery, I/O from 192 signals)
3. **Identify vague/missing requirements** (cost target, size/weight, interface type)
4. **Competitive analysis of existing products** (BrailleMe, Orbit Reader, APH Refreshabraille)
   - Benchmark pricing, features, form factor, weight, interfaces
   - Identify industry-standard UX patterns (navigation buttons, auto-sleep, charging)
   - Establish market context for "low-cost" and "portable" interpretation
5. **Document assumptions for vague specs** (see `docs/assumptions-register.md`)
   - Create unique assumption IDs (ASMP-XXX-NNN)
   - Tag risk levels (CRITICAL/HIGH/MEDIUM/LOW)
   - Plan sensitivity testing in v1.4.0

**Includes:**
- System-level specifications (I/O, functionality, interfaces)
- Electrical specifications (power, control, communication)
- Manufacturing requirements (cost, volume, timeline)
- User requirements (portability, usability, accessibility)
- Non-functional requirements (performance, reliability, standards compliance)
- **Assumptions register** (for vague PDF requirements like "low-cost", "portable", "high-volume")

**Output:**
- `source/requirements.yaml` (machine-readable SSOT)
- `artifacts/requirements.md` (human-readable report)
- `docs/assumptions-register.md` (assumption documentation + competitive benchmarks)

**Rubric Weight:** 25/100 points

**Key Insight:** PDF is intentionally vague - LAM tests how you handle ambiguity. Competitive analysis validates assumptions and demonstrates market awareness.

---

### Step 2: Develop Multiple Alternative Solutions
**Deliverable:** 3+ distinct architecture options

**PDF Quote:** "Develop and describe multiple alternative solutions."

**Includes:**
- Diverse actuator technologies (piezo, solenoid, SMA, motor)
- Different control strategies (MCU, FPGA, distributed)
- Communication interface options (BLE, USB-C, WiFi)
- Block diagrams for each architecture
- Component selection rationale

**Output:** `docs/architecture.md` with diagrams

**Rubric Weight:** 25/100 points

---

### Step 3: Evaluate Solutions - Trade-off Analysis
**Deliverable:** Quantitative comparison & justified selection

**PDF Quote:** "Evaluate the proposed solutions by discussing their **advantages and disadvantages**, as well as **any other considerations** that influenced your final selection."

**Guide:** See [docs/tradeoff-analysis-guide.md](../docs/tradeoff-analysis-guide.md) for complete methodology

**Critical Requirements:**
1. **Evaluation Framework** - Define what you value (criteria + weights + assumptions)
2. **Advantages & Disadvantages** - Honest, thorough analysis of each solution
3. **Quantitative Comparison** - Data-driven decision matrix
4. **Sensitivity Analysis** - Test robustness to changing priorities and constraints
5. **Other Considerations** - Supply chain, expertise, tooling, risk tolerance, market timing

**Includes:**
- **Evaluation Framework:**
  - Define 7-10 evaluation criteria (time, cost, DFM, risk, UX, etc.)
  - Assign weights (must sum to 100%, justified by context)
  - Document assumptions (market, customer, budget, priorities)
- **Quantitative Comparison:**
  - Cost comparison (BOM estimates: qty 1, 100, 1000)
  - Power budget (battery life calculations)
  - Size/complexity (component count, PCB area)
  - Timeline feasibility (parts lead time, integration complexity)
  - Weighted scoring matrix
- **Advantages & Disadvantages:**
  - For EACH architecture: strengths, weaknesses, when it wins, when it fails
- **⚠️ SENSITIVITY ANALYSIS (REQUIRED - 5/30 pts):**
  - **Type 1: Stakeholder Value Sensitivity**
    - "What if they value cost more than time?" (weight changes)
    - "What if they value risk minimization?" (priority shift)
    - "What if customer is internal vs external?" (different values)
  - **Type 2: External Constraint Sensitivity**
    - "What if cost doubles?" (market conditions)
    - "What if timeline compresses to 1 month?" (schedule pressure)
    - "What if key component unavailable?" (supply chain)
    - "What if volume targets change (1K vs 100K)?" (scale impact)
  - Robustness matrix: Which solution wins across scenarios?
- **Other Considerations:**
  - Supply chain (lead times, multi-source, geography)
  - Team expertise (familiar vs new tech, training)
  - Tooling/equipment (existing vs new capex)
  - Risk tolerance (proven vs cutting edge)
  - Market timing considerations

**Output:** `docs/tradeoffs.md` with evaluation framework + decision matrix + sensitivity analysis

**Rubric Weight:** 30/100 points ← **HIGHEST WEIGHT**

---

### Step 4: Path to Production (Volume Manufacturing)
**Deliverable:** Pilot production plan → scale to mass production

**PDF Quote:** "Outline the process for transitioning the concept from initial design to volume production."

**Includes:**
- **2-month timeline** (Gantt chart: design → pilot → validate)
- **Pilot production** (10-100 units to verify design, tolerances, failure modes)
- **Manufacturing plan** (DFM, sourcing, test strategy)
- **Risk mitigation** (long-lead items, alternates, buffers)
- **Scale strategy** (pilot → 1K → 10K+ units)

**Output:** `docs/solution.md` with timeline & manufacturing package

**Rubric Weight:** 20/100 points

---

**Documentation Quality:** 10/100 points (applies throughout)

**Total:** 100 points

---

## Interview Deliverables

### Presentation Requirements
- **Duration:** 30 minutes
- **Format:** "You may prepare **any form of content** that will best support your presentation"
  - Primary: Slide deck (PowerPoint/PDF)
  - Supporting: Appendices, calculations, datasheets, schematics
  - Physical: Printed backup materials, portfolio examples
- **⚠️ CRITICAL DEADLINE:** Digital content must be emailed to recruiter **24 HOURS PRIOR** to interview
  - Interview: October 23, 2025
  - **Presentation Due: October 22, 2025** ← HARD DEADLINE
  - Email to: Nathan Briggs (recruiting contact)
  - USB drives NOT supported - email only
- **Equipment:** HDMI projection available in interview room

### Interview Evaluation Criteria
Lam Research seeks to understand:
1. How you develop engineering concepts
2. How you make engineering decisions
3. Your ability to communicate technical solutions
4. Your approach to production-ready design

### Interview Structure (90 minutes total)
- Introductions: 15 minutes
- Background Discussion: 5 minutes
- **Concept Evaluation Presentation: 30 minutes**
- **Q&A on Evaluation: 15 minutes**
- Candidate Questions and Wrap-up: 15 minutes

---

## Reference Information

### Braille Alphabet
Each braille character consists of a 2×3 grid of dots:
- 6 dots total per character
- Each dot can be raised (1) or lowered (0)
- Different combinations represent different letters/characters

### Design Challenge Summary
**From:** Text on cell phone screen
**To:** 192 control signals (32 characters × 6 dots each)
**Through:** Electronics system you design
**Within:** Constraints of portability, low cost, high volume, 2-month timeline

---

## Success Criteria

A successful concept evaluation will demonstrate:
1. ✓ Thorough understanding of technical requirements
2. ✓ Multiple viable solution architectures explored
3. ✓ Rigorous trade-off analysis with clear justification
4. ✓ Realistic path to production within timeline constraints
5. ✓ Clear communication of engineering decisions and rationale
