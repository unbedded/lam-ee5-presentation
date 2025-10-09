# Requirements Philosophy Alignment

**How Our Requirements Structure Supports Systems Engineering Trade-offs**

---

## The Connection: Requirements → Trade-offs → Value

Your presentation thesis:
> "Requirements exist in **ranges**, not absolutes. Systems engineering is about **trade-offs**, not perfection."

Our requirements structure (v2.0.0):
```
PRD-COST-001: "low cost" (PDF verbatim - VAGUE)
    ↓
PRD-COST-001-ASMP: "$200 ±$100 BOM" (RANGE, not point)
    ↓
sensitivity_range: "$100-$300 BOM"
    ↓
v1.3.0: Portfolio of architectures ($150, $200, $300)
    ↓
v1.4.0: Trade-off analysis (cost vs UX vs reliability)
    ↓
Presentation: "Here's the value/cost trade-off for customer to decide"
```

---

## How Each Requirement Field Supports This

### 1. `pdf_verbatim` - Shows What Customer Actually Said

**Purpose:** Prove you didn't invent requirements

**Example:**
```yaml
PRD-COST-001:
  pdf_verbatim: "The device must be low-cost at volume production volume"
  status: "VAGUE - no dollar amount specified"
```

**Presentation value:**
- "Here's what the PDF actually said: 'low cost'"
- "No dollar amount. No volume definition. This is typical."
- "Junior engineers freeze. Senior engineers **define the range**."

---

### 2. `our_assumption` - Shows Your Engineering Judgment

**Purpose:** Demonstrate how you make vague requirements actionable

**Example:**
```yaml
PRD-COST-001-ASMP:
  pdf_says: "low-cost at volume production volume"
  our_assumption: "BOM parts cost $200 ±$100 at volume of 10k units/month (range: $100-$300 BOM)"
```

**Presentation value:**
- "I interpreted 'low cost' as $200 BOM based on market analysis"
- "But I gave it **±50% sensitivity range** ($100-$300)"
- "Why? Because requirements exist in **ranges**, not points."

---

### 3. `sensitivity_range` - Enables Trade-off Analysis

**Purpose:** Shows you'll test multiple scenarios, not commit to one

**Example:**
```yaml
PRD-COST-001-ASMP:
  sensitivity_range: "$100-$300 BOM (±50% from $200 target)"
  test_plan: "v1.4.0 sensitivity analysis (BOM scenarios: $100, $150, $200, $250, $300)"
```

**Presentation value:**
- "I didn't design one solution at $200."
- "I designed **portfolio at $150, $200, $300** to test sensitivity."
- "This IS the trade-off analysis (rubric: 30 points)."

---

### 4. `alternative_scenarios` - Portfolio Approach

**Purpose:** Shows multiple valid solutions, each optimizing different trade-offs

**Example:**
```yaml
PRD-IFACE-001-ASMP:
  alternative_scenarios:
    - "Scenario A (BLE-only): Wireless, requires battery, $200-250 BOM"
    - "Scenario B (USB-C wired): Tethered, no battery, $100-150 BOM (great low-cost option!)"
    - "Scenario C (Hybrid BLE+USB): Best UX, highest cost $250-300 BOM"
```

**Presentation value:**
- "I didn't pick 'the best' interface. I designed **three valid options**."
- "Architecture A optimizes UX. Architecture B optimizes cost. Architecture C optimizes flexibility."
- "This is systems engineering: **Trade-offs, not perfection**."

---

### 5. `impact_if_wrong` - Risk Assessment

**Purpose:** Shows you understand consequences of assumptions

**Example:**
```yaml
PRD-COST-001-ASMP:
  impact_if_wrong: |
    - If target is $100 BOM → Eliminates most actuator options, requires aggressive cost reduction
    - If target is $300 BOM → Opens up premium actuator options (solenoid, haptic feedback)
```

**Presentation value:**
- "If customer says '$100 BOM, not $200,' I'm not starting over."
- "I already designed Architecture B at $150. We just adjust scope."
- "If they say '$300 OK,' great—Architecture C has premium features."
- "This is **risk mitigation through portfolio design**."

---

## The Presentation Flow (Using Requirements Structure)

### Slide 1: Requirements from PDF (Show Vagueness)

```
REQUIREMENT: "Low cost, high volume, portable companion device"

ANALYSIS:
- "Low cost" → No dollar amount specified
- "High volume" → No volume target specified
- "Portable" → No size/weight specified

CHALLENGE: How do you design to vague requirements?
```

---

### Slide 2: Systems Engineering Philosophy ⭐

```
APPROACH: Requirements Exist in Ranges, Not Absolutes

EXAMPLE: "Low cost"
- PDF says: "low cost" (vague)
- I assume: $200 BOM ±50% (range: $100-$300)
- I design: Portfolio at $150, $200, $300
- Customer picks: Value/cost trade-off

THIS IS SYSTEMS ENGINEERING:
✓ Trade-offs over perfection
✓ Portfolio over point design
✓ Value over specs
```

---

### Slide 3: Portfolio of Architectures (Show Options)

```
THREE ARCHITECTURES, THREE TRADE-OFFS:

Architecture A (BLE Wireless):
- Cost: $200-250 BOM
- UX: Best (untethered)
- Complexity: High (battery, BMS, certification)

Architecture B (USB-C Wired): ← VALUE ENGINEERING
- Cost: $100-150 BOM (LOWEST)
- UX: Good (tethered to phone)
- Complexity: Low (no battery, simpler)

Architecture C (Hybrid):
- Cost: $250-300 BOM
- UX: Best (wireless + wired fallback)
- Complexity: Highest

CUSTOMER DECIDES: Cost vs UX vs Reliability
```

---

### Slide 4: Trade-off Analysis (Quantitative)

```
SENSITIVITY ANALYSIS: How does cost assumption affect design?

| BOM Target | Architecture | Actuator | Interface | Feasibility |
|------------|--------------|----------|-----------|-------------|
| $100       | USB-C only   | Piezo    | Wired     | Aggressive  |
| $150       | USB-C or BLE | Piezo    | Either    | Achievable  |
| $200       | BLE+USB      | Solenoid | Hybrid    | Comfortable |
| $300       | BLE+USB      | Premium  | Hybrid    | Feature-rich|

INSIGHT: Requirements range → Portfolio → Customer picks value
```

---

## How This Wins the Interview

**Rubric Scoring:**

1. **Requirements (25 pts):**
   - ✅ "Identified key requirements" - 9 ground truth from PDF
   - ✅ "Clearly documented assumptions" - 6 assumptions with rationale
   - ✅ "Rationale for assumptions" - Sensitivity ranges + risk levels
   - **Differentiation:** Most candidates list requirements. You show **ranges and trade-offs**.

2. **Alternative Solutions (25 pts):**
   - ✅ "Multiple distinct solutions" - Portfolio of 3-4 architectures
   - ✅ "Design methodology explained" - Sensitivity-driven portfolio approach
   - **Differentiation:** Most show 2-3 options. You show **systematic sensitivity analysis**.

3. **Trade-offs (30 pts):**
   - ✅ "Clear pros/cons analysis" - Alternative_scenarios in YAML
   - ✅ "Quantitative where applicable" - Cost ranges, BOM breakdowns
   - ✅ "Design decision rationale" - Impact_if_wrong, value engineering
   - **Differentiation:** This is your **strongest section** (30% of rubric).

**Total Impact:** Your requirements structure directly supports 80% of rubric scoring (Requirements 25% + Solutions 25% + Trade-offs 30%).

---

## The "Wow" Moment

**What other candidates show:**
- "Here are my requirements (list of specs)"
- "Here is my design (one solution)"
- "Here's why my design is good (self-promotion)"

**What YOU show:**
- "Here's what the PDF said (verbatim, with analysis of vagueness)"
- "Here's the **range** I assumed (with sensitivity analysis)"
- "Here are **three architectures** optimizing different trade-offs"
- "Here's the **quantitative trade-off analysis** (cost vs UX vs reliability)"
- "**Customer picks** based on their priorities (value engineering)"

**Differentiation:** You're not selling a design. You're presenting **a systems engineering methodology for decision-making under uncertainty**.

---

## Key Phrases to Use in Presentation

1. "Requirements exist in **ranges**, not absolutes."
2. "I designed a **portfolio of architectures**, not a single solution."
3. "Each architecture **optimizes different trade-offs**: cost vs UX vs reliability."
4. "I didn't pick 'the best'—I let **quantitative analysis** rank them."
5. "The USB-C wired option? That's **value engineering**: same function, -$100 BOM."
6. "This is **systems engineering judgment**: Trade-offs over perfection."

---

## Why You Worked So Hard on Requirements

**You said:** "This is why I have been working so hard on these requirements."

**Exactly right.** The requirements aren't just documentation. They ARE your trade-off analysis framework:

1. **pdf_verbatim** → Shows vagueness (problem statement)
2. **our_assumption** → Shows judgment (your interpretation)
3. **sensitivity_range** → Enables portfolio (multiple solutions)
4. **alternative_scenarios** → Shows trade-offs (cost vs UX vs reliability)
5. **impact_if_wrong** → Shows risk mitigation (customer can adjust)

**The requirements structure IS your presentation story.**

Without this structure:
- You'd have to explain trade-offs verbally (weak)
- No traceability from PDF → assumptions → architectures (disconnected)
- Hard to show systematic methodology (looks ad-hoc)

With this structure:
- ✅ Every trade-off traces to a requirement
- ✅ Every assumption has sensitivity range
- ✅ Every architecture optimizes specific trade-offs
- ✅ Quantitative, systematic, professional

**This is why the refactor was worth 3.5 hours. It's your presentation foundation.**

---

## Next Steps: Capture in Presentation Plan

Add to TODO.md v2.2.0 (Presentation Structure):

```markdown
- [ ] Slide: Requirements Analysis (show PDF vagueness)
  - Quote PRD-COST-001 pdf_verbatim: "low cost"
  - Quote PRD-VOL-001 pdf_verbatim: "high volume"
  - Quote PRD-SIZE-001 pdf_verbatim: "portable"
  - Message: "Vague requirements are typical. How do you handle them?"

- [ ] Slide: Systems Engineering Philosophy ⭐ KEY SLIDE
  - Thesis: Requirements exist in ranges, not absolates
  - Example: PRD-COST-001-ASMP ($200 ±$100 range)
  - Visual: Point design vs Portfolio comparison
  - Message: Trade-offs over perfection, Value over specs

- [ ] Slide: Portfolio of Architectures
  - Show Architecture A/B/C from requirements.alternative_scenarios
  - Each optimizes different trade-off (cost vs UX vs reliability)
  - Trace to PRD-IFACE-001-ASMP, PRD-COST-001-ASMP

- [ ] Slide: Trade-off Analysis (Quantitative)
  - Table: BOM scenarios ($100/$150/$200/$250/$300)
  - Impact: Which architectures viable at each cost point?
  - Recommendation: Based on sensitivity analysis, not opinion
```

---

**Bottom line:** Your requirements work IS your presentation. The structure you built (PRD + ASMP + sensitivity_range + alternative_scenarios) directly supports your thesis: "Systems engineering is about trade-offs, not perfection."

**This is why you're going to crush this interview.** 🚀
