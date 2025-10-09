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

## Part 1: Evaluation Framework - How to Score Options

### Step 1: Define Evaluation Criteria (What Matters?)

**For EE projects, typical criteria:**

| Criterion | Why It Matters | Typical Weight |
|-----------|----------------|----------------|
| **Time to Market** | Meeting customer deadline | 20-30% |
| **Unit Cost (BOM)** | Product pricing, margins | 15-25% |
| **Development Cost (NRE)** | Budget constraints, ROI | 10-20% |
| **Manufacturability (DFM)** | Yield, scalability to volume | 15-25% |
| **Power Consumption** | Battery life, portability | 5-15% |
| **Reliability/MTBF** | Warranty costs, reputation | 5-15% |
| **UX/Usability** | Customer satisfaction | 5-15% |
| **Risk (Technical/Timeline)** | Probability of success | 10-20% |
| **Supply Chain** | Component availability | 5-10% |

**Must sum to 100%**

### Step 2: Make Assumptions (Document What You Don't Know)

**Example Assumption Framework:**

```markdown
## Evaluation Assumptions

**⚠️ NOTE:** The assignment does not specify customer type, market, or budget.
The following assumptions were made based on context clues. If assumptions are
incorrect, the recommended solution may change (see Sensitivity Analysis).

### Market Assumption
- **Assumption:** Target market is China/India accessibility market
- **Rationale:** "Low-cost, high-volume" suggests emerging market price sensitivity
- **Impact if wrong:** If US/EU market, unit cost tolerance increases +$30-50

### Stakeholder Priority Assumption (Weights)
- **Time to Market: 30%** - 2-month constraint explicitly stated (FIXED)
- **Unit Cost: 25%** - "Low-cost" is primary requirement
- **Manufacturability: 20%** - "High-volume" requires good DFM
- **Development Cost: 15%** - Pilot budget assumed limited
- **Risk/Reliability: 10%** - Important but secondary to cost/time

### Budget Assumptions
- **Unit Cost Target: <$50 BOM** - Based on competitor braille display pricing
- **Development Budget: <$50K NRE** - Typical for 2-month pilot project
- **Timeline: 2 months (FIXED)** - Explicitly stated, non-negotiable

### Customer Type Assumption
- **Assumption:** External customer (B2C accessibility market)
- **Rationale:** "Companion device" suggests consumer product
- **Impact if wrong:** If internal customer, risk tolerance changes significantly
```

### Step 3: Score Each Architecture (The Fundamental Facts)

**Use 1-10 scale with rationale:**

```markdown
## Architecture Scoring

### Architecture A: Piezo Actuator + MCU + BLE

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Time to Market | 7/10 | 8 weeks (custom piezo sourcing adds 2 weeks) |
| Unit Cost | 6/10 | $45 BOM (piezo arrays expensive) |
| Dev Cost | 5/10 | $30K NRE (custom driver circuits) |
| Manufacturability | 8/10 | Good DFM (SMT assembly, no moving parts) |
| Power | 8/10 | 150mW avg (piezo efficient) |
| Reliability | 9/10 | Excellent (solid state, proven tech) |
| UX | 8/10 | Good tactile response |
| Risk | 7/10 | Low technical risk (proven), medium supply risk |
| Supply Chain | 6/10 | 2 suppliers for custom piezo (medium risk) |

**Advantages:**
- Best reliability (no moving parts)
- Low power consumption
- Good tactile feedback

**Disadvantages:**
- Higher unit cost ($45 vs target $30-40)
- Custom piezo sourcing (8-week lead time)
- Higher NRE ($30K for driver design)

**When This Wins:**
- If reliability is critical (medical/government)
- If power budget is tight (<200mW)
- If volume is high (>50K units, cost amortizes)
```

### Step 4: Calculate Weighted Scores

```markdown
## Weighted Scoring Results

| Criterion | Weight | Arch A | Arch B | Arch C |
|-----------|--------|--------|--------|--------|
| Time to Market | 30% | 7 → 2.1 | 9 → 2.7 | 5 → 1.5 |
| Unit Cost | 25% | 6 → 1.5 | 8 → 2.0 | 4 → 1.0 |
| Dev Cost | 15% | 5 → 0.75 | 9 → 1.35 | 3 → 0.45 |
| Manufacturability | 20% | 8 → 1.6 | 7 → 1.4 | 6 → 1.2 |
| Risk/Reliability | 10% | 7 → 0.7 | 6 → 0.6 | 8 → 0.8 |
|-----------|--------|--------|--------|--------|
| **TOTAL** | **100%** | **6.65** | **8.05** | **4.95** |

**Under stated assumptions: Architecture B wins (8.05/10)**
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

## Part 4: Final Recommendation - Data-Driven Decision

```markdown
## Recommended Solution: Architecture B (Solenoid + MCU + USB-C)

### Selection Rationale

**Based on stated assumptions:**
- Scores highest (8.05/10) under assumed stakeholder priorities
- Most robust to changing priorities (wins 2/4 value scenarios)
- Most robust to external changes (wins 4/4 constraint scenarios)
- Meets 2-month timeline (6 weeks total, 2-week buffer)
- Meets cost target ($30 BOM < $50 target)
- Low development risk ($15K NRE, proven technology)

### When This Recommendation Changes

**Recommend Architecture A instead if:**
- Reliability becomes paramount (>30% weight)
- Volume scales above 200K units (NRE amortizes)
- Customer is government/medical (proven tech critical)

**Recommend Architecture C instead if:**
- Premium market positioning (US/EU)
- UX differentiation is competitive advantage
- Higher price point acceptable ($150-200 retail)

### Assumptions That Drive This Decision

**CRITICAL ASSUMPTIONS (verify with stakeholders):**
1. **Market:** China/India emerging market (cost-sensitive)
2. **Customer:** External B2C (not internal project)
3. **Volume:** 10K-50K units/year (mid-range production)
4. **Timeline:** 2 months is hard deadline (non-negotiable)
5. **Power:** USB-C parasitic acceptable (no battery needed)

**If any assumption is incorrect, re-run analysis with adjusted weights.**
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

- [ ] Define 7-10 evaluation criteria
- [ ] Assign weights that sum to 100% (justify each)
- [ ] Document all assumptions (market, customer, budget, priorities)
- [ ] Score each architecture on each criterion (1-10 with rationale)
- [ ] Document advantages & disadvantages for each architecture
- [ ] Calculate weighted total scores
- [ ] Run 4 stakeholder value sensitivity scenarios
- [ ] Run 4 external constraint sensitivity scenarios
- [ ] Address "other considerations" (supply chain, expertise, tooling)
- [ ] Make final recommendation with data-driven justification
- [ ] Create `docs/tradeoffs.md` with all analysis
- [ ] Run `/rubric-eval` to verify 30/30 points

**Deliverable:** Trade-off analysis that gives stakeholders the facts they need to make informed decisions, even when priorities are unclear.

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-08 | Spencer Barrett | Consolidated guide - evaluation + sensitivity |

**Related Documents:**
- [design-plan.md](design-plan.md) - Step 3 requirements from PDF
- [interview-rubric.md](interview-rubric.md) - Category 3 scoring (30/100 pts)
