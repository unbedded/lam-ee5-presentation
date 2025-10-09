# Requirements Policy & Naming Conventions

**Project:** Lam Research EE Concept Evaluation - Braille Display Device
**Version:** 1.0.0
**Date:** 2025-10-05
**Purpose:** Define standards for requirements definition, naming, and traceability

---

## Single Source of Truth

**Location:** `source/requirements.yaml`

**Rule:** All requirements MUST be defined in the YAML file. Generated documents (markdown, reports) are READ-ONLY outputs.

---

## Requirement ID Naming Convention

### Format
```
[CATEGORY]-[SUBCATEGORY]-[NUMBER]
```

### Category Codes

| Code | Category | Description |
|------|----------|-------------|
| **SYS** | System Requirements | High-level functional requirements |
| **EE** | Electrical Engineering | Electrical design requirements |
| **MFG** | Manufacturing | Production & cost requirements |
| **USR** | User Experience | Usability & accessibility requirements |
| **NFR** | Non-Functional | Performance, reliability, compliance |
| **PRD** | Production | Timeline, supply chain, delivery |

### Subcategory Codes

#### EE (Electrical Engineering)
- **EE-PWR** = Power supply & distribution
- **EE-CTRL** = Control system (MCU/FPGA)
- **EE-IO** = I/O expansion & signal routing
- **EE-COMM** = Communication interfaces
- **EE-SNS** = Sensors & feedback
- **EE-ACT** = Actuator drive circuits

#### SYS (System)
- **SYS-FUNC** = Core functional requirements
- **SYS-PERF** = System-level performance
- **SYS-IF** = System interfaces

#### MFG (Manufacturing)
- **MFG-COST** = Cost constraints
- **MFG-VOL** = Volume production
- **MFG-TIME** = Timeline requirements
- **MFG-DFM** = Design for manufacturability

#### USR (User Experience)
- **USR-PORT** = Portability requirements
- **USR-UX** = Usability requirements
- **USR-ACC** = Accessibility requirements

#### NFR (Non-Functional)
- **NFR-PERF** = Performance metrics
- **NFR-REL** = Reliability & MTBF
- **NFR-STD** = Standards & compliance
- **NFR-SEC** = Security requirements

### Numbering
- Use 3-digit zero-padded numbers: `001`, `002`, `003`
- Sequential within subcategory
- DO NOT reuse numbers (even if requirement deleted)

### Examples
- `SYS-FUNC-001` = System > Functional > Single Line Braille Display
- `EE-PWR-001` = Electrical Engineering > Power > Portable Power Source
- `MFG-COST-001` = Manufacturing > Cost > Low-Cost BOM
- `NFR-STD-001` = Non-Functional > Standards > Compliance Requirements

---

## Priority Levels

| Priority | Label | Definition | Project Impact | Example |
|----------|-------|------------|----------------|---------|
| **P0** | Critical | Must have - product fails without this | Project failure if not met | 192 control signals |
| **P1** | High | Should have - significant value/risk | Major degradation if not met | Portable power source |
| **P2** | Medium | Nice to have - enhances product | Minor impact if deferred | Fast refresh rate |
| **P3** | Low | Future enhancement | No immediate impact | Color-coded indicators |

---

## Requirement Attributes

Each requirement MUST include:

### Mandatory Fields
- **ID** - Unique identifier (see naming convention above)
- **title** - Short descriptive name (< 10 words)
- **description** - Clear, testable statement of requirement
- **source** - Where requirement originated (PDF page, stakeholder, derived)
- **priority** - P0-Critical, P1-High, P2-Medium, P3-Low
- **category** - Functional, Electrical, Manufacturing, etc.

### Recommended Fields
- **rationale** - Why this requirement exists (business/technical justification)
- **verification_method** - How to verify (test, analysis, inspection, demonstration)
- **acceptance_criteria** - Measurable criteria for "done" (bullet list)
- **subcategory** - More specific categorization (Power, I/O, Cost, etc.)

### Optional Fields
- **calculation** - Derived requirements show math
- **assumptions** - Any assumptions made
- **constraints** - Known limitations
- **references** - Related standards, documents, research
- **notes** - Additional context

### Traceability Fields
- **traces_to.design** - Links to design documents (architecture.md, tradeoffs.md, solution.md)
- **traces_to.analysis** - Links to analysis documents (requirements.md)
- **traces_to.tests** - Links to test cases (if applicable)
- **traces_to.rubric** - Links to rubric evaluation
- **traces_to.artifacts** - Links to deliverable artifacts

---

## Requirements Sources

Requirements come from multiple sources:

### 1. Explicit Requirements (PDF)
- Directly stated specifications
- Example: "32 characters × 6 dots = 192 control signals"
- **Source tag**: `"PDF p.9 'description...'"`

### 2. Derived Requirements
- Calculated/inferred from explicit requirements
- Example: 192 GPIO signals derived from 32 chars × 6 dots
- **Source tag**: `"Derived from [PARENT-REQ-ID]"`
- **Must include**: `calculation:` field showing math

### 3. Competitive Analysis Requirements
- Features/specs discovered from existing products
- Example: UP/DOWN navigation buttons (standard on BrailleMe, Orbit Reader)
- Example: Auto-sleep power management (BrailleMe feature)
- Example: Weight/size benchmarks (BrailleMe: 1.3 lbs, 20-cell)
- **Source tag**: `"Competitive analysis (BrailleMe, Orbit Reader)"`
- **Must include**: `competitor_reference:` field with product details

**Why competitive analysis matters:**
- Validates assumptions (what does "low-cost" mean? Look at market pricing: $449-$1795)
- Identifies industry-standard UX patterns (navigation, charging, interfaces)
- Establishes performance benchmarks (weight, battery life, features)
- Demonstrates market awareness to LAM interviewers

**Example competitive analysis requirement:**
```yaml
USR-UX-002:
  title: "Page Navigation Controls"
  description: "Device shall provide UP/DOWN buttons for forward/backward line navigation"
  source: "Competitive analysis (BrailleMe, Orbit Reader standard feature)"
  rationale: "Industry standard - all competitor products include navigation controls"
  priority: "P0-Critical"
  competitor_reference: "BrailleMe ($515.50, Perkins keyboard + nav), Orbit Reader (nav buttons)"
```

### 4. Assumption-Based Requirements
- Requirements created when PDF is vague
- Example: "Low-cost" → <$50 BOM (assumed)
- See [Handling Assumptions](#handling-assumptions-in-requirements) section below

---

## Writing Good Requirements

### SMART Criteria
Requirements should be:
- **S**pecific - Clearly defined scope
- **M**easurable - Quantifiable acceptance criteria
- **A**chievable - Technically feasible within constraints
- **R**elevant - Traceable to project goals
- **T**estable - Can be verified/validated

### Example - Good vs Bad

❌ **Bad:** "Device should be fast"
- Not specific (fast at what?)
- Not measurable (how fast?)
- Not testable

✅ **Good:** "Braille display shall refresh within 2 seconds of receiving new text"
- Specific (refresh action)
- Measurable (2 seconds)
- Testable (timing measurement)

### Use "Shall" Language
- **Shall** = Mandatory requirement
- **Should** = Recommended (use sparingly, prefer P2/P3 priority)
- **May** = Optional capability
- **Will** = Statement of fact (not a requirement)

### Examples
- ✅ "System **shall** provide 192 control signals"
- ✅ "Device **should** include battery level indicator" (P2)
- ❌ "Device **might** support WiFi" (unclear - make it P3 or remove)
- ❌ "User **will** press button to advance" (statement of fact, not requirement)

---

## Verification Methods

| Method | Description | When to Use | Example |
|--------|-------------|-------------|---------|
| **Test** | Physical testing of prototype/product | Hardware/software functions | Power-on self-test |
| **Analysis** | Calculation, simulation, review | Derived requirements, performance | Power budget calculation |
| **Inspection** | Visual check, measurement | Physical attributes | PCB dimensions |
| **Demonstration** | Show it works in use case | User-facing features | Braille display demo |

---

## Traceability Rules

### Forward Traceability (Requirement → Artifact)
Every requirement MUST trace forward to at least one:
- Design document (architecture.md, tradeoffs.md, solution.md)
- Test case (if testable requirement)
- Acceptance criteria

### Backward Traceability (Artifact → Requirement)
Every design decision, test case, or deliverable SHOULD trace back to:
- At least one requirement ID
- Source document (PDF, stakeholder input)

### Traceability Matrix
Generated from `source/requirements.yaml` via `/req-trace` command:
- Shows requirement → design → test → artifact relationships
- Identifies orphaned requirements (no design/test)
- Identifies orphaned design (no requirement justification)

---

## Change Control

### Modifying Requirements
1. Edit `source/requirements.yaml` (single source of truth)
2. Run `/req-yaml-to-md` to regenerate docs
3. Commit changes with clear description
4. Update traceability matrix if needed

### Adding New Requirements
1. Assign next sequential ID in appropriate category
2. Follow YAML template structure
3. Ensure mandatory fields populated
4. Add traceability links
5. Regenerate docs

### Deprecating Requirements
- DO NOT delete from YAML
- Add `status: "deprecated"` field
- Add `deprecated_reason` field
- Add `deprecated_date` field
- Requirement ID remains reserved (do not reuse)

---

## Derived Requirements

**Definition:** Requirements inferred from other requirements or constraints

**Example:**
- **Parent:** SYS-FUNC-001 (32 characters) + SYS-FUNC-002 (6 dots/char)
- **Derived:** SYS-FUNC-003 (192 control signals = 32 × 6)

**Mandatory Fields for Derived Requirements:**
- `source: "Derived from [PARENT-REQ-IDs]"`
- `calculation:` Show the math/logic

---

## Interview-Specific Rules

### Scope Alignment
Requirements MUST align with PDF p.10 scope:
1. Identify key technical requirements
2. Develop multiple alternative solutions
3. Evaluate advantages/disadvantages
4. Outline path to production

### Priority Guidance for 2-Month Timeline
- **P0-Critical:** Must be in initial production release
- **P1-High:** Should be in initial release if feasible
- **P2-Medium:** Defer if timeline at risk
- **P3-Low:** Post-production enhancement

---

## Generated Artifacts

### From `source/requirements.yaml`

1. **docs/requirements.md** (v1.2.0)
   - Human-readable requirements analysis
   - Generated via `/req-yaml-to-md`
   - Includes all requirement details, organized by category

2. **artifacts/rubric-reports/req-traceability-report.md** (v1.6.0)
   - Full traceability matrix
   - Orphan detection (requirements without design, design without requirements)
   - Coverage analysis

---

## Handling Assumptions in Requirements

### When Requirements Are Vague

**Problem:** PDF requirements often lack specificity:
- "low-cost" (no target given)
- "portable" (no dimensions given)
- "high-volume" (no quantity given)

**Solution:** Document assumptions as requirements with unique IDs and risk levels.

### Assumptions Register

**Location:** `docs/assumptions-register.md` (human-readable) + `source/requirements.yaml` metadata.assumptions (machine-readable)

**Convention:** `ASMP-[CATEGORY]-[NUMBER]`

**Example:**
```yaml
metadata:
  assumptions:
    ASMP-COST-001:
      description: "Low-cost means <$50 BOM at 1000-unit volume"
      rationale: "Competitor braille displays retail $80-200. Assuming 40% BOM ratio → $32-80 BOM."
      risk_level: CRITICAL
      impact_if_wrong: "If target is $30, eliminates premium architectures. If $100, enables more options."
      tested_in: "v1.4.0 sensitivity analysis"
```

### Creating Assumption-Based Requirements

When PDF requirement is vague, create TWO artifacts:

1. **Assumption** (in metadata.assumptions section):
   - Unique ID (ASMP-XXX-NNN)
   - Description of what you're assuming
   - Rationale (why this assumption is reasonable)
   - Risk level (CRITICAL, HIGH, MEDIUM, LOW)
   - Impact if wrong
   - Where tested (usually v1.4.0 sensitivity analysis)

2. **Requirement** (in requirements section):
   - Same ID as assumption (ASMP-COST-001)
   - Concrete testable requirement using assumed value
   - Add `assumption_risk: [LEVEL]` field
   - Add `impact_if_wrong:` field
   - Add `tested_in: "v1.4.0 sensitivity analysis"` field

### Assumption Risk Levels

| Risk Level | Definition | Impact If Wrong | Testing Required |
|------------|------------|-----------------|------------------|
| **CRITICAL** | Wrong assumption eliminates/enables entire architectures | Complete redesign needed | MUST test in v1.4.0 sensitivity |
| **HIGH** | Wrong assumption significantly changes design priorities | Major design changes | MUST test in v1.4.0 sensitivity |
| **MEDIUM** | Wrong assumption requires design adjustments | Moderate changes possible | SHOULD test in v1.4.0 |
| **LOW** | Wrong assumption has minimal impact | Minor tweaks only | Optional testing |

### Examples

**CRITICAL Risk:**
- ASMP-COST-001: "Low-cost = <$50 BOM" (vs $30 or $100 changes everything)
- ASMP-COMP-001: "COTS actuators only" (vs custom fabrication fundamentally different)

**HIGH Risk:**
- ASMP-MKT-001: "China/India emerging market" (vs US/EU changes priorities)
- ASMP-VOL-001: "High-volume = >10K/year" (vs 1K or 100K changes DFM)

**MEDIUM Risk:**
- ASMP-SIZE-001: "Portable = ≤200g, ≤20×10×3cm" (reasonable variation OK)
- ASMP-PWR-001: "Battery powered" (vs USB-C tethered is trade-off)

**LOW Risk:**
- ASMP-STD-001: "Grade 1 braille (6-dot)" (industry standard)
- ASMP-ENV-001: "Indoor, 0-40°C" (typical consumer environment)

### Integration with v1.4.0 Evaluation

**Sensitivity Analysis Tests Assumptions:**

1. **Stakeholder Value Sensitivity** (tests priority assumptions):
   - "What if they value cost > time-to-market?" (tests ASMP-MKT-001)
   - "What if they prioritize risk minimization?" (tests design approach)

2. **External Constraint Sensitivity** (tests quantitative assumptions):
   - "What if cost target is $30? $100?" (tests ASMP-COST-001)
   - "What if volume is 1K/year? 100K/year?" (tests ASMP-VOL-001)

**Output:** Robustness matrix showing which architecture wins under different assumption scenarios.

### Workflow

1. **v1.2.0: Define Requirements**
   - Encounter vague PDF requirement
   - Create assumption in metadata.assumptions
   - Create corresponding requirement with assumption_risk tag
   - Document in docs/assumptions-register.md

2. **v1.3.0: Design Architectures**
   - Use assumed values as constraints
   - Note which assumptions drive design choices

3. **v1.4.0: Sensitivity Analysis**
   - Test CRITICAL and HIGH risk assumptions
   - Show how recommendation changes if assumptions are wrong
   - Demonstrate engineering judgment and risk awareness

4. **v2.0.0: Presentation**
   - Slide: "Key Assumptions" (3-5 critical ones)
   - Talking point: "PDF was intentionally vague. Here's what I assumed and why."
   - Q&A ready: If challenged, show sensitivity analysis

### Red Flags

❌ **Don't do this:**
- Invent requirements without documenting assumptions
- Ignore vague specifications
- Assume one value without testing sensitivity
- Hide assumptions in notes/comments

✅ **Do this:**
- Explicitly document all assumptions with unique IDs
- Tag risk levels honestly
- Test CRITICAL/HIGH assumptions in v1.4.0
- Present assumptions transparently in interview

### Verification

Use `/req-audit` to verify:
- All ASMP-XXX-NNN IDs are unique
- All assumption-based requirements have risk level
- CRITICAL/HIGH assumptions are tested in v1.4.0
- Assumptions register is up to date

---

## References

- **Source Document:** `docs/reference/Interview Overview and Concept Evaluation - EE Presentation.pdf`
- **Problem Statement:** `docs/problem-statement.md`
- **YAML Source:** `source/requirements.yaml`
- **Assumptions Register:** `docs/assumptions-register.md`
- **Naming Inspiration:** `/home/preact/sw/job/rapyuta/movie_db_qa/docs/requirements.md`

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-05 | Spencer Barrett | Initial requirements policy |
