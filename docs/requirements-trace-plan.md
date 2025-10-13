# Enhanced Requirements Traceability Analysis - Implementation Plan

**Status:** Deferred to post-interview (Technical Debt)
**Priority:** P1-High (affects traceability rubric score)
**Effort:** 2-3 hours (Python script enhancement)
**Owner:** Post-interview refactoring
**Created:** 2025-10-12

---

## Problem Statement

**Current Gap:**
- `/req-trace` only checks if requirement IDs exist in `architectures.yaml`
- Does NOT verify subsystems actually provide the requirement
- Does NOT generate coverage matrix (% requirements each architecture satisfies)
- `artifacts/architecture.md` has minimal traceability (just lists a few requirements per arch)

**Impact:**
- No visibility into which requirements each architecture ACTUALLY satisfies
- Can't answer: "Does ARCH_SOL_ECO meet the AA battery requirement?"
- Dangling references possible (arch claims requirement, but no subsystem provides it)
- Orphaned requirements not detected (requirement exists but no arch satisfies it)

---

## Solution: Enhanced `/req-trace` Command

### Inputs (SSOT)
- `source/requirements.yaml` (all 27 requirements)
- `source/architectures.yaml` (3 architectures, `traces_to_requirements` field)
- `source/subsystems.yaml` (19 subsystems, `rationale` field mentions requirements)
- `source/parts.csv` (30 parts, optional for BOM verification)

### Output
- `artifacts/requirements-traceability-report.md` (comprehensive coverage matrix + validation issues)

---

## Algorithm

### Step 1: Parse YAML Sources (1 min)
```python
requirements = load_yaml("source/requirements.yaml")
architectures = load_yaml("source/architectures.yaml")
subsystems = load_yaml("source/subsystems.yaml")
parts = load_csv("source/parts.csv")
```

### Step 2: Extract Requirement References (2 min)

**From architectures.yaml:**
```python
# ARCH_SOL_ECO.traces_to_requirements = [PRD-COST-001, NFR-EMI-001, ...]
arch_claims = {}
for arch in architectures:
    arch_claims[arch.id] = arch.traces_to_requirements
```

**From subsystems.yaml (parse rationale text):**
```python
# Regex: "PRD-[A-Z]+-\d+(-ASMP)?(-[A-Z0-9-]+)?" or "NFR-[A-Z]+-\d+"
subsystem_provides = {}
for subsystem in subsystems:
    req_refs = extract_requirement_ids(subsystem.rationale)
    subsystem_provides[subsystem.id] = req_refs
```

**From architectures.yaml (which subsystems each arch uses):**
```python
arch_subsystems = {}
for arch in architectures:
    arch_subsystems[arch.id] = arch.core + arch.unique
```

### Step 3: Build Coverage Matrix (5 min)

For each requirement × architecture pair:

```python
coverage = {}  # {req_id: {arch_id: status}}

for req in requirements:
    for arch in architectures:
        # Check if architecture CLAIMS to satisfy requirement
        claims = req.id in arch_claims[arch.id]

        # Check if architecture's subsystems PROVIDE requirement
        provides = False
        for subsystem_id in arch_subsystems[arch.id]:
            if req.id in subsystem_provides.get(subsystem_id, []):
                provides = True
                break

        # Determine status
        if claims and provides:
            status = "✅ SATISFIED"
        elif claims and not provides:
            status = "⚠️ CLAIMED (no subsystem)"  # Dangling reference!
        elif not claims and provides:
            status = "⚠️ PROVIDED (not claimed)"  # Missing trace!
        else:
            status = "❌ NOT SATISFIED"

        coverage[req.id][arch.id] = status
```

### Step 4: Vertical Traceability (depth analysis)

For each requirement, show the full trace:

```
NFR-EMI-001 (requirement)
  ↓ listed in architectures.yaml
ARCH_SOL_ECO.traces_to_requirements
  ↓ architecture includes subsystems
  - SS-EMI-BULK-CAP (in arch.core)
  - SS-EMI-BYPASS-CAP (in arch.core)
  ↓ subsystems reference requirement
  - SS-EMI-BULK-CAP.rationale: "Derived from NFR-EMI-001..."
  - SS-EMI-BYPASS-CAP.rationale: "Derived from NFR-EMI-001..."
  ↓ subsystems use parts
  - Nichicon UVR1H102MHD (from parts.csv)
  - Kemet C0805C104K5RACTU (from parts.csv)
✅ TRACE COMPLETE
```

### Step 5: Identify Validation Issues

**Dangling References:**
- Architecture claims requirement, but no subsystem in that arch provides it
- Example: `ARCH_PIEZO_ECO.traces_to_requirements = [PRD-FUNC-006-ASMP]` but no subsystem mentions PRD-FUNC-006-ASMP

**Orphaned Requirements:**
- Requirement exists, but NO architecture traces to it
- Example: `PRD-USER-001` (Sight-Impaired User) is universal but not in any `traces_to_requirements`

**Missing Universal Requirements:**
- P0-Critical requirements that should be in ALL architectures but aren't
- Example: `NFR-STD-002` (ADA compliance) should be universal

---

## Output Format: `artifacts/requirements-traceability-report.md`

```markdown
# Requirements Traceability Report

**Generated:** 2025-10-12
**Source Files:** requirements.yaml (27 reqs), architectures.yaml (3 archs), subsystems.yaml (19 subsystems)

---

## Executive Summary

**Coverage by Architecture:**
- ARCH_SOL_ECO: 23/27 requirements (85% coverage)
- ARCH_PIEZO_ECO: 21/27 requirements (78% coverage)
- ARCH_PIEZO_DLX: 22/27 requirements (81% coverage)

**Validation Issues:**
- Dangling references: 3 (arch claims, no subsystem provides)
- Orphaned requirements: 2 (no arch traces to it)
- Missing universal requirements: 4 (P0 reqs should be in all archs)

---

## Coverage Matrix (Horizontal Traceability)

| Requirement | Priority | ARCH_SOL_ECO | ARCH_PIEZO_ECO | ARCH_PIEZO_DLX | Notes |
|-------------|----------|--------------|----------------|----------------|-------|
| PRD-SCHED-001 | P0 | ✅ | ✅ | ✅ | All meet 2-month timeline |
| PRD-SCHED-002-ASMP | P0 | ✅ COTS | ⚠️ Custom piezo | ⚠️ Custom piezo | Only SOL_ECO fully COTS |
| PRD-COST-001-ASMP | P0 | ✅ $252 | ⚠️ $345 | ❌ $364 | DLX exceeds $300 ceiling |
| PRD-POWER-004-ASMP | P1 | ✅ 1.53W | ❌ 2.16W | ❌ 2.16W | Only SOL fits AA budget |
| NFR-EMI-001 | P0 | ✅ | ✅ | ✅ | All have EMI subsystems |
| PRD-USER-001 | P0 | ⚠️ NOT CLAIMED | ⚠️ NOT CLAIMED | ⚠️ NOT CLAIMED | Universal req, add to all |
| ... | ... | ... | ... | ... | ... |

**Legend:**
- ✅ = Fully satisfies (claimed + provided)
- ⚠️ = Issue (claimed but not provided, or provided but not claimed)
- ❌ = Does not satisfy requirement

---

## Vertical Traceability (Depth Analysis)

### NFR-EMI-001: FCC Part 15B >6dB Margin

[Show full trace from requirement → architecture → subsystems → parts → BOM]

---

## Validation Issues

### 1. Dangling References (architecture claims, but no subsystem provides)

[List with fix recommendations]

### 2. Orphaned Requirements (no architecture traces to it)

[List with fix recommendations]

### 3. Missing Universal Requirements (P0 reqs should be in ALL archs)

[List with fix recommendations]

---

## Subsystem → Requirement Mapping

| Subsystem | Referenced Requirements | Used By Architectures |
|-----------|-------------------------|------------------------|
| SS-EMI-BULK-CAP | NFR-EMI-001, NFR-STD-001-DRV-LOWRISK | ALL (3 archs) |
| SS-EMI-BYPASS-CAP | NFR-EMI-001, NFR-STD-001-DRV-LOWRISK | ALL (3 archs) |
| ... | ... | ... |

---

## Recommendations

1. Fix dangling references (3 issues)
2. Add universal requirements to all architectures (4 P0 reqs)
3. Enhance subsystem rationale (5 subsystems don't cite any requirements)

---

**END OF TRACEABILITY REPORT**
```

---

## Implementation Steps

### 1. Update `/req-trace` Slash Command (1 hour)
- Modify `.claude/commands/req-trace.md` to use enhanced algorithm
- Add regex parsing for requirement IDs in subsystem rationale
- Add coverage matrix generation logic

### 2. Create Python Script `scripts/generate_traceability_report.py` (1 hour)
- Implement algorithm from Step 1-5 above
- Output markdown report to `artifacts/requirements-traceability-report.md`
- Add to Makefile: `make req-trace` target

### 3. Test with Current Data (30 min)
- Run `/req-trace` on current source files
- Verify coverage matrix is accurate
- Fix any validation issues discovered

### 4. Update README.md Dependencies (15 min)
- Add `artifacts/requirements-traceability-report.md` to dependency map
- Update slash command documentation

---

## Success Criteria

**Functional:**
- ✅ Coverage matrix shows all 27 requirements × 3 architectures (81 cells)
- ✅ Vertical traces show full path: requirement → arch → subsystem → part → BOM
- ✅ Validation issues detected: dangling refs, orphaned reqs, missing universal reqs
- ✅ Report is readable and actionable (fix recommendations)

**Quality:**
- ✅ No false positives (claims subsystem provides requirement when it doesn't)
- ✅ No false negatives (misses subsystem that does provide requirement)
- ✅ Regex correctly extracts requirement IDs from rationale (test edge cases)

**Performance:**
- ✅ Runs in <10 seconds for 27 reqs × 3 archs × 19 subsystems
- ✅ Report size <50KB (readable in editor)

---

## Future Enhancements (Post-Interview)

### Phase 2: BOM Verification
- Cross-reference `artifacts/bom/*.csv` to verify parts actually appear
- Detect if BOM is missing a part that subsystem requires

### Phase 3: Quantitative Validation
- Parse quantitative specs from subsystems (e.g., "1.53W power budget")
- Validate against requirement thresholds (e.g., "PRD-POWER-004-ASMP: ≤1.5W")
- Generate PASS/FAIL verdicts (not just ✅/❌ symbols)

### Phase 4: Interactive HTML Report
- Generate `artifacts/requirements-traceability-report.html` with:
  - Sortable/filterable coverage matrix
  - Drill-down from requirement → architecture → subsystem → part
  - Color-coded by status (green/yellow/red)

---

## References

- **Source Files:** `source/requirements.yaml`, `source/architectures.yaml`, `source/subsystems.yaml`
- **Current `/req-trace`:** `.claude/commands/req-trace.md` (basic ID checking only)
- **Coverage Matrix Example:** This document, "Output Format" section
- **README Dependencies:** `README.md` lines 137-236 (Build Structure & Dependencies)

---

**Status:** Ready for implementation (post-interview, P1-High priority)
**Estimated Effort:** 2-3 hours (Python script + testing + documentation)
**Risk:** Low (purely analysis tool, doesn't modify source files)

---

**END OF IMPLEMENTATION PLAN**
