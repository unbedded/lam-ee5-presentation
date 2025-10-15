# Trade-off Analysis Guide - v1.4.0

**Phase:** v1.4.0 Trade-off Analysis
**Rubric Weight:** 30/100 points ← **HIGHEST WEIGHT**
**PDF Source:** Step 3 - "Evaluate the proposed solutions by discussing their **advantages and disadvantages**, as well as **any other considerations** that influenced your final selection."

---

## Purpose: Give Stakeholders the Facts They Need to Decide

**Your Role as EE:** Provide the **fundamental facts** and **trade-off analysis** so stakeholders (program director, customer, executives) can make informed decisions.

**NOT your job:** Pick the "right" answer (you don't know what they value!)
**IS your job:** Show how each option performs, and how the recommendation changes based on priorities

---

## The Reality of This Assignment

**What We Know:**
- ✅ 2-month timeline to pilot production (FIXED constraint)
- ✅ "Portable, low-cost, high-volume" (clues about market)
- ✅ 32 characters × 6 dots = 192 control signals (technical spec)
- ✅ Companion device to cell phone (interface requirement)

**What We DON'T Know (HUGE HOLES):**
- ❓ Who's the customer? (Internal? External? Government? Strategic partner?)
- ❓ What market? (US/EU premium? China/India budget? Emerging markets?)
- ❓ What's the budget? (Unit cost target? Development NRE?)
- ❓ What do stakeholders value most? (Speed? Cost? Risk? UX? Margins?)
- ❓ What's the business model? (Sell hardware? Subscription? Non-profit?)

**LAM's Expectation:** Show you can make engineering decisions **even with incomplete information**

---

## Part 1: Visual Comparison Framework - Show Trade-offs, Not Scores

**Key Philosophy:** Requirements are too vague to assign precise weights. Instead, show **relative strengths visually** and let stakeholders decide based on their priorities.

### Step 1: Define Evaluation Dimensions (What Matters?)

**For EE projects, typical dimensions:**

| Dimension | Why It Matters | Data Source |
|-----------|----------------|-------------|
| **Cost (BOM)** | Product pricing, margins | Quantitative (architectures.yaml) |
| **Timeline** | Meeting customer deadline | Quantitative (architectures.yaml) |
| **UX/Usability** | Customer satisfaction | Qualitative rating |
| **Manufacturability** | Yield, scalability to volume | Qualitative rating |
| **Robustness/Reliability** | Warranty costs, reputation | Qualitative rating |
| **Supply Chain Risk** | Component availability | Qualitative rating |
| **Power Efficiency** | Battery life, portability | Quantitative (architectures.yaml) |
| **Complexity** | Development risk, debugging | Qualitative rating |

**Result:** 8-dimension spider/radar chart showing trade-off profile

### Step 2: Generate Visualizations from YAML Data

**Automated Chart Generation:**

```bash
# Run Python script to generate charts from architectures.yaml
python3 scripts/generate_tradeoff_charts.py

# Output files (resources/diagrams/):
#   • architecture-radar-comparison.png   (Spider chart - 8 dimensions)
#   • architecture-cost-comparison.png    (Bar chart - BOM costs)
#   • architecture-timeline-comparison.png (Bar chart - timelines)
#   • architecture-decision-tree.png      (Decision framework)
```

**Chart Types:**

1. **Spider/Radar Chart** (8 dimensions, all 3 architectures overlaid)
   - Shows relative strengths at a glance
   - No single "best" - each has different profile
   - Visual reinforces "it depends on your priorities" message

2. **Bar Charts** (Quantitative comparisons)
   - Cost comparison (pilot BOM)
   - Timeline comparison (weeks to pilot production)
   - Easy to present, clear winners per dimension

3. **Decision Tree Diagram** ("When X Wins" visual)
   - Flowchart: "Wireless required?" → ARCH_PIEZO_DLX
   - "Cost < $300?" → ARCH_SOL_ECO
   - "Timeline < 8 wks?" → ARCH_PIEZO_ECO

### Step 3: Advantages & Disadvantages (Honest Assessment)

**For EACH architecture, document:**

- ✅ **Advantages** (strengths, what it does well - be specific with data)
- ❌ **Disadvantages** (weaknesses, limitations, risks - be honest)
- 🏆 **When it wins** (under what conditions does this architecture excel?)
- ⚠️ **When it fails** (under what conditions does this become unviable?)

**Example:**

```markdown
## ARCH_PIEZO_ECO: Piezo Economy (USB-C Wired)

### Advantages
- ✅ Fastest to market (8-10 weeks - simplest electrical design)
- ✅ Proven technology (piezo monopoly in commercial braille displays)
- ✅ Standard 2.5mm pitch (preserves muscle memory, ADA compliant)
- ✅ No battery complexity (USB-C powered, simpler BOM)

### Disadvantages
- ❌ Needs COTS piezo at 2.5mm pitch (not found yet - sourcing risk)
- ❌ Higher cost ($420 vs $277 for ARCH_SOL_ECO)
- ❌ Tethered to phone (USB-C cable reduces portability)

### When This Wins
- If timeline < 8 weeks (fastest electrical integration)
- If wireless NOT required (cable acceptable)
- If standard pitch REQUIRED (ADA 703.3 compliance critical)

### When This Fails
- If wireless required (no BLE - only USB-C)
- If cost < $300 target (exceeds budget)
- If actuator sourcing fails (no COTS piezo available)
```

---

## Part 2: Sensitivity Analysis - How Answers Change

### Type 1: Sensitivity to Stakeholder Values (What If They Care About Different Things?)

**Question:** "What if I'm wrong about what stakeholders value?"

```markdown
## Sensitivity to Decision Criteria

### Scenario 1: TIME is CRITICAL (Customer Deadline is Hard)
**Weights:** Time=40%, Cost=20%, DFM=20%, DevCost=10%, Risk=10%
**Winner:** Architecture B (9/10 on time, fastest to market)
**Conclusion:** B is robust to time-critical scenarios

### Scenario 2: UNIT COST is CRITICAL (China Market, Price-Sensitive)
**Weights:** Time=20%, Cost=40%, DFM=20%, DevCost=10%, Risk=10%
**Winner:** Architecture B (8/10 on cost, $30 BOM lowest)
**Conclusion:** B wins in cost-sensitive markets

### Scenario 3: RISK MINIMIZATION is CRITICAL (Internal Customer, Reputation)
**Weights:** Time=20%, Cost=15%, DFM=15%, DevCost=10%, Risk=40%
**Winner:** Architecture A (9/10 reliability, proven tech)
**Conclusion:** If risk is paramount, A becomes preferred

### Scenario 4: PREMIUM POSITIONING (US/EU Market, High Margins)
**Weights:** Time=15%, Cost=10%, DFM=20%, DevCost=10%, UX=30%, Risk=15%
**Winner:** Architecture C (best UX, justifies $200 price point)
**Conclusion:** For premium market, C enables better margins

**ROBUSTNESS SUMMARY:**
- Architecture A: Wins 1/4 scenarios (risk-critical)
- Architecture B: Wins 2/4 scenarios (time/cost-critical) ← Most robust
- Architecture C: Wins 1/4 scenarios (premium positioning)
```

### Type 2: Sensitivity to External Constraints (What If Reality Changes?)

**Question:** "What if market conditions or constraints shift?"

```markdown
## Sensitivity to External Changes

### Change 1: Component Cost Doubles (Tariffs, Shortage, Inflation)
**Test:** BOM costs increase 2x

| Architecture | Baseline BOM | 2x Cost | Still Viable? |
|--------------|--------------|---------|---------------|
| A (Piezo) | $45 | $90 | ⚠️ Marginal (exceeds target) |
| B (Solenoid) | $30 | $60 | ✅ Yes (still in range) |
| C (SMA) | $75 | $150 | ❌ No (way over budget) |

**Winner:** B (most robust to cost inflation)

### Change 2: Timeline Compresses to 1 Month (Customer Pressure)
**Test:** 2-month timeline cut in half

| Architecture | Design Time | Parts Lead | Total | Meets 1mo? |
|--------------|-------------|------------|-------|------------|
| A (Piezo) | 4 weeks | 8 weeks | 12 weeks | ❌ No |
| B (Solenoid) | 2 weeks | 4 weeks | 6 weeks | ⚠️ Tight |
| C (SMA) | 6 weeks | 8 weeks | 14 weeks | ❌ No |

**Winner:** B (only viable option at compressed timeline)

### Change 3: Key Component Goes EOL (Supply Chain Disruption)
**Test:** Primary component unavailable

| Architecture | Component Risk | Alternates Available? | Risk Level |
|--------------|----------------|----------------------|------------|
| A (Piezo) | Custom piezo array | 2 suppliers, 12-week lead | ⚠️ Medium |
| B (Solenoid) | Standard solenoid | 5+ suppliers, drop-in | ✅ Low |
| C (SMA) | SMA wire | 2 suppliers, proprietary | ⚠️ Medium |

**Winner:** B (best supply chain resilience)

### Change 4: Volume Target Changes (1K vs 100K Units)
**Test:** Production volume shifts

| Architecture | 1K Units (Cost) | 100K Units (Cost) | NRE Impact |
|--------------|-----------------|-------------------|------------|
| A (Piezo) | $50/unit ($50K total) | $35/unit ($3.5M) | $30K (high NRE) |
| B (Solenoid) | $35/unit ($35K total) | $30/unit ($3.0M) | $15K (low NRE) |
| C (SMA) | $80/unit ($80K total) | $60/unit ($6.0M) | $60K (very high) |

**Winner at low volume (1K):** B (lowest total cost)
**Winner at high volume (100K):** B (still lowest, NRE amortizes)
**Note:** A becomes competitive at >200K units (NRE amortization)

**ROBUSTNESS SUMMARY:**
- B wins 4/4 external constraint scenarios
- B is most robust to changing conditions
```

---

## Part 3: "Other Considerations" - Beyond Quantitative Analysis

**PDF asks for:** "any other considerations that influenced your final selection"

### Market Segmentation Strategy

**The USB-C vs Battery Question (Your Insight!):**

```markdown
## Power Strategy Trade-off

**Option 1: USB-C Powered (Parasitic from Phone)**
- ✅ No battery (lower cost, lighter weight)
- ✅ Always charged (no dead battery issues)
- ✅ Simpler design (no charging circuit, BMS)
- ❌ Tethered to phone (less portable)
- ❌ Phone battery drain (customer dissatisfaction risk)

**Option 2: Battery Powered (Cordless)**
- ✅ Truly portable (wireless freedom)
- ✅ No phone battery drain
- ❌ Battery adds cost (+$5-10 BOM)
- ❌ Battery adds weight (+50g)
- ❌ Charging hassle (USB port, cable management)
- ❌ Battery compliance (UN38.3, shipping restrictions)

**Decision:**
For 2-month timeline + low-cost target → USB-C powered (simpler, faster)
For premium market + better UX → Battery powered (better experience)

**This feeds back into Architecture Evaluation:**
- If USB-C: Reduces power budget requirement (can draw 2.5W from phone)
- If Battery: Tightens power budget (<200mW for 8hr runtime on 2000mAh)
```

### Supply Chain Realities

- **Lead times:** COTS parts (2-4 weeks) vs custom (8-12 weeks)
- **MOQ:** Standard parts (1 unit) vs custom (1000 units minimum)
- **Geographic sourcing:** China-only vs multi-source
- **Distributor stock:** Digi-Key/Mouser inventory levels

### Team Expertise

- **Familiar tech:** Team has done solenoid drivers before
- **New tech:** Piezo driver is new learning curve (training time)
- **Vendor support:** Solenoid vendors offer reference designs

### Tooling & Equipment

- **Existing tools:** Standard bench equipment sufficient for B
- **New equipment needed:** High-voltage driver tester for A ($15K capex)

### Risk Tolerance

- **Proven tech (A):** Lower performance, but predictable outcome
- **Cutting-edge (C):** Higher performance, but unproven at scale

---

## Part 4: Portfolio Strategy - "It Depends on YOUR Constraints"

**Key Message:** No universal "best" architecture - selection depends on customer priorities

### Decision Framework (Visual: Decision Tree)

```markdown
## Portfolio Strategy: Which Architecture Wins Under What Conditions?

### Decision Logic

IF wireless REQUIRED:
  → ARCH_PIEZO_DLX (only BLE option)

ELSE IF cost < $300:
  → ARCH_SOL_ECO (lowest BOM: $277)

ELSE IF timeline < 8 weeks:
  → ARCH_PIEZO_ECO (fastest to market: 8-10 wks)

ELSE IF volume > 10K units:
  → ARCH_SOL_ECO (best scaling via mechanical cost-down)

ELSE:
  → ARCH_PIEZO_ECO (most robust across scenarios)


### When Each Architecture Wins

**ARCH_PIEZO_ECO Wins:**
- Timeline < 8 weeks (fastest electrical integration)
- Wireless NOT required (cable acceptable)
- Standard pitch REQUIRED (ADA 703.3 compliance)
- Most scenarios (robust choice)

**ARCH_SOL_ECO Wins:**
- Cost < $300 budget (lowest BOM: $277)
- Volume > 10K units (mechanical scaling)
- Mechanical innovation acceptable (3.5mm pitch pilot-ok)
- Cost-sensitive markets (China, India)

**ARCH_PIEZO_DLX Wins:**
- Wireless REQUIRED (only BLE architecture)
- Premium positioning (US/EU market)
- UX differentiation critical (wireless freedom)
- Higher price point acceptable ($450+)


### Critical Assumptions to Validate

**MUST verify with stakeholders before architecture selection:**
1. **Wireless requirement?** (Hard constraint - only DLX has BLE)
2. **Cost threshold?** ($300? $400? $500? - drives SOL_ECO vs PIEZO)
3. **Timeline flexibility?** (8 weeks? 10 weeks? 12 weeks? - drives PIEZO_ECO)
4. **Volume target?** (1K pilot? 10K production? 100K volume? - affects scaling)
5. **Actuator pitch?** (2.5mm strict? 3.5mm pilot-acceptable? - enables SOL_ECO)

**Recommendation Process:**
1. Present spider chart showing 8-dimension trade-offs
2. Show bar charts (cost, timeline) - quantitative comparison
3. Walk through decision tree - "Tell me your constraints, I'll tell you the winner"
4. Validate critical assumptions with stakeholders
5. Make architecture selection based on THEIR priorities

**Philosophy:** Give stakeholders the facts they need to decide, not a single "answer"
```

---

## Deliverable: docs/tradeoffs.md Structure

When you create `docs/tradeoffs.md`, use this structure:

```markdown
# Trade-off Analysis - Braille Display Device

## 1. Evaluation Framework
- Decision criteria (7-10 factors)
- Stakeholder priority assumptions (weights)
- Budget/timeline assumptions

## 2. Architecture Comparison
- Fundamental facts (cost, time, power, risk for each)
- Advantages & disadvantages (honest assessment)
- Weighted scoring results

## 3. Sensitivity Analysis
- Sensitivity to stakeholder values (4 scenarios)
- Sensitivity to external constraints (4 scenarios)
- Robustness summary matrix

## 4. Other Considerations
- Market segmentation options
- Supply chain realities
- Team expertise/tooling
- Risk tolerance

## 5. Recommended Solution
- Final selection with data-driven justification
- Conditions under which recommendation changes
- Critical assumptions to verify with stakeholders
```

---

## Final Checklist for v1.4.0

Before marking v1.4.0 complete:

- [ ] Define 8 evaluation dimensions (cost, timeline, UX, mfg, robust, supply, power, complexity)
- [ ] Generate spider/radar chart (`python3 scripts/generate_tradeoff_charts.py`)
- [ ] Generate cost comparison bar chart (from YAML data)
- [ ] Generate timeline comparison bar chart (from YAML data)
- [ ] Generate decision tree diagram ("When X Wins" visual)
- [ ] Document advantages & disadvantages for EACH architecture (honest assessment)
- [ ] Document "When it wins" conditions for each architecture
- [ ] Document "When it fails" conditions for each architecture
- [ ] Run sensitivity analysis (4 "what if" scenarios showing how winner changes)
- [ ] Address "other considerations" (supply chain, expertise, tooling, risk)
- [ ] Create portfolio strategy section ("It depends on YOUR constraints")
- [ ] Create `docs/tradeoffs.md` with all analysis and visuals
- [ ] Run `/rubric-eval` to verify 30/30 points

**Deliverable:** Visual trade-off analysis that gives stakeholders the facts they need to make informed decisions, with decision framework showing when each architecture wins.

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-08 | Spencer Barrett | Consolidated guide - evaluation + sensitivity |

**Related Documents:**
- [design-plan.md](design-plan.md) - Step 3 requirements from PDF
- [interview-rubric.md](interview-rubric.md) - Category 3 scoring (30/100 pts)
