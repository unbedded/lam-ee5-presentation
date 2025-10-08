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

## References

- **Source Document:** `docs/reference/Interview Overview and Concept Evaluation - EE Presentation.pdf`
- **Problem Statement:** `docs/problem-statement.md`
- **YAML Source:** `source/requirements.yaml`
- **Naming Inspiration:** `/home/preact/sw/job/rapyuta/movie_db_qa/docs/requirements.md`

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-05 | Spencer Barrett | Initial requirements policy |
