---
description: Generate traceability matrix from requirements.yaml
---

# Requirements Traceability Matrix Generator

Analyze `source/requirements.yaml` and all project documents to generate comprehensive traceability report showing requirement → design → test relationships.

## Your Task

Create bidirectional traceability matrix showing forward trace (req → artifact) and backward trace (artifact → req).

---

## Step 1: Load Requirements (1 min)

Read `source/requirements.yaml` and extract:
- All requirement IDs (hierarchical PRD naming v2.0.0):
  - **PRD-XXXX-NNN** (ground truth from PDF): PRD-SCHED-001, PRD-SIZE-001, PRD-IFACE-001, PRD-COST-001, PRD-VOL-001, PRD-USER-001, PRD-FUNC-001/002/003
  - **PRD-XXXX-NNN-ASMP** (assumptions): PRD-SCHED-001-ASMP, PRD-SIZE-001-ASMP, PRD-IFACE-001-ASMP, PRD-COST-001-ASMP, PRD-VOL-001-ASMP, PRD-FUNC-002-ASMP
- All `traces_to.*` fields (design, analysis, tradeoffs, solution, tests, artifacts)
- Priority for each requirement (P0-Critical, P1-High)
- Parent relationships (PRD-XXXX-NNN-ASMP → parent: PRD-XXXX-NNN)

---

## Step 2: Scan Project Documents (3 min)

**Search these files for requirement references:**
- `docs/architecture.md`
- `docs/tradeoffs.md`
- `docs/solution.md`
- `artifacts/requirements.md`
- `artifacts/assumption-risk-report.md`
- Any files in `artifacts/`

**Look for patterns (NEW HIERARCHICAL NAMING):**
- Explicit mentions: `PRD-SCHED-001`, `PRD-COST-001-ASMP`, etc.
- Links: `[PRD-SCHED-001](#prd-sched-001)`
- Tables/lists referencing requirement IDs
- Pattern: `PRD-[A-Z]+-[0-9]{3}(-ASMP)?`

**Extract:**
- Which files mention each requirement
- Line numbers (if possible)
- Context (surrounding text)

---

## Step 3: Forward Traceability Analysis (2 min)

**For each requirement, check:**
- ✅ Has at least one `traces_to` link
- ⏳ No traces yet (acceptable early in project)
- ❌ Should have traces but doesn't (based on priority/phase)

**Categorize:**
- **Fully Traced:** Has traces to design, analysis, and solution
- **Partially Traced:** Has some traces but missing key ones
- **Orphaned:** No traces at all

**Priority-based expectations:**
- P0-Critical: MUST have design + solution traces by v1.5.0
- P1-High: SHOULD have design + solution traces by v1.5.0
- P2-Medium: May have partial traces
- P3-Low: Traces optional (future work)

---

## Step 4: Backward Traceability Analysis (3 min)

**For each design document, identify:**
- Design decisions mentioned
- Which requirements justify them
- Any design elements WITHOUT requirement justification (orphaned design)

**Example:**
- `docs/architecture.md` mentions "192 I/O pins needed"
- Should trace back to `SYS-FUNC-003` (192 control signals)
- If no requirement exists → orphaned design decision

**Generate list of orphaned designs:**
| Document | Design Element | Line | Missing Requirement? |
|----------|----------------|------|---------------------|
| architecture.md | WiFi module | 145 | No req justifies WiFi vs BLE decision |

---

## Step 5: Gap Analysis (2 min)

**Identify:**
1. **High-priority orphaned requirements** (P0/P1 with no traces)
2. **Orphaned design** (design decisions with no requirement justification)
3. **Broken links** (traces_to points to non-existent files/sections)
4. **Missing traces expected at current phase** (v1.2.0+ should have analysis, v1.3.0+ should have design)

---

## Output Format

Generate traceability report in Markdown:

```markdown
# Requirements Traceability Matrix

**Project:** Lam Research - Braille Display EE Concept Evaluation
**Date:** YYYY-MM-DD
**Source:** source/requirements.yaml
**Phase:** [Current phase from TODO.md]

---

## Executive Summary

**Total Requirements:** XX
**Traceability Status:**
- Fully Traced: XX (XX%)
- Partially Traced: XX (XX%)
- Orphaned: XX (XX%)

**Critical Issues:**
- High-priority orphaned requirements: X
- Orphaned design elements: X
- Broken traceability links: X

**Status:** [✅ PASS / ⚠️ NEEDS ATTENTION / ❌ CRITICAL GAPS]

---

## Forward Traceability Matrix

### Full Traceability Table

**Ground Truth Requirements (PRD-XXXX-NNN):**

| Req ID | Type | Priority | Analysis | Design | Trade-offs | Solution | Tests | Status |
|--------|------|----------|----------|--------|------------|----------|-------|--------|
| PRD-SCHED-001 | Ground Truth | 🔴 P0 | ✅ | ✅ | ✅ | ✅ | ⏳ | Fully Traced |
| PRD-SIZE-001 | Ground Truth | 🔴 P0 | ✅ | ✅ | ⏳ | ⏳ | ⏳ | Partially Traced |
| PRD-COST-001 | Ground Truth | 🔴 P0 | ✅ | ❌ | ❌ | ❌ | ⏳ | ORPHANED |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Assumptions (PRD-XXXX-NNN-ASMP):**

| Req ID | Type | Parent | Priority | Analysis | Design | Trade-offs | Solution | Status |
|--------|------|--------|----------|----------|--------|------------|----------|--------|
| PRD-SCHED-001-ASMP | Assumption | PRD-SCHED-001 | 🔴 P0 | ✅ | ✅ | ✅ | ✅ | Fully Traced |
| PRD-COST-001-ASMP | Assumption | PRD-COST-001 | 🔴 P0 | ✅ | ❌ | ❌ | ❌ | ORPHANED |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Legend:**
- ✅ = Traced (link exists and valid)
- ⏳ = TODO (not applicable yet at current phase)
- ❌ = Missing (should exist but doesn't)

---

### Traceability by Category

**Schedule Requirements (PRD-SCHED):**
- Ground Truth: 1
- Assumptions: 1
- Fully Traced: X (XX%)
- Partially Traced: X (XX%)
- Orphaned: X (XX%)

**Cost Requirements (PRD-COST):**
- Ground Truth: 1
- Assumptions: 1
- Fully Traced: X (XX%)
- Partially Traced: X (XX%)
- Orphaned: X (XX%)

[Repeat for PRD-SIZE, PRD-IFACE, PRD-VOL, PRD-USER, PRD-FUNC]

---

### Traceability by Priority

**P0-Critical Requirements:**
| Req ID | Type | Status | Missing Traces |
|--------|------|--------|----------------|
| PRD-SCHED-001 | Ground Truth | ✅ Fully Traced | - |
| PRD-COST-001-ASMP | Assumption | ❌ ORPHANED | design, tradeoffs, solution |

**Summary:**
- P0 Fully Traced: X/X (XX%)
- P0 Orphaned: X/X (XX%) ← **CRITICAL IF > 0**

**P1-High Requirements:**
[Same format]

---

## Backward Traceability Matrix

### Design Documents Analysis

**docs/architecture.md:**
- Total design decisions: X
- With requirement justification: X (XX%)
- Orphaned (no req): X (XX%)

**Orphaned Design Elements:**
| Line | Design Element | Recommendation |
|------|----------------|----------------|
| 145 | WiFi module selection | Add EE-COMM-002 to justify WiFi vs BLE |
| 230 | 5V power rail | Traced to EE-PWR-001 ✅ |

**docs/tradeoffs.md:**
[Same analysis]

**docs/solution.md:**
[Same analysis]

---

### Reverse Trace Validation

**Check if all `traces_to` links are valid:**

| Req ID | Trace Type | Target | Valid? | Issue |
|--------|------------|--------|--------|-------|
| PRD-FUNC-001 | design | docs/architecture.md#braille-actuator-array | ✅ | - |
| PRD-COST-001-ASMP | design | docs/architecture.md#cost-analysis-wrong | ❌ | Section doesn't exist |

**Broken Links Found:** X

---

## Gap Analysis

### 1. High-Priority Orphaned Requirements

**Critical (P0) with no traces:**
| Req ID | Title | Recommendation |
|--------|-------|----------------|
| [List] | [Title] | [Action needed] |

**High (P1) with no traces:**
| Req ID | Title | Recommendation |
|--------|-------|----------------|
| [List] | [Title] | [Action needed] |

---

### 2. Orphaned Design Decisions

**Design elements without requirement justification:**
| Document | Line | Element | Recommendation |
|----------|------|---------|----------------|
| architecture.md | 145 | WiFi module | Create EE-COMM-002 or justify under EE-COMM-001 |

---

### 3. Broken Traceability Links

**Invalid `traces_to` references:**
| Req ID | Trace Type | Target | Issue | Fix |
|--------|------------|--------|-------|-----|
| PRD-COST-001-ASMP | design | docs/arch.md#wrong | Section missing | Update to correct anchor |

---

### 4. Phase-Appropriate Trace Expectations

**Current Phase:** [v1.X.0 from TODO.md]

**Expected traces at this phase:**
- v1.2.0: All requirements should have `analysis` trace
- v1.3.0: P0/P1 requirements should have `design` trace
- v1.4.0: P0/P1 requirements should have `tradeoffs` trace
- v1.5.0: P0/P1 requirements should have `solution` trace

**Missing expected traces:**
| Req ID | Priority | Expected Trace | Status |
|--------|----------|----------------|--------|
| [List] | [Pri] | [analysis/design/etc] | MISSING |

---

## Compliance Summary

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| P0 Fully Traced | XX% | 100% by v1.5.0 | [✅/⚠️/❌] |
| P1 Fully Traced | XX% | 80% by v1.5.0 | [✅/⚠️/❌] |
| Orphaned Design | X | 0 | [✅/⚠️/❌] |
| Broken Links | X | 0 | [✅/⚠️/❌] |

**Overall Traceability Health:** [✅ EXCELLENT / ⚠️ NEEDS WORK / ❌ CRITICAL GAPS]

---

## Recommendations

### Critical Actions (Must Fix)
1. [Fix broken links]
2. [Trace high-priority orphaned requirements]
3. [Add requirements for orphaned design decisions]

### Recommended Actions (Should Fix)
1. [Improve partial traces]
2. [Add missing analysis links]

### Future Work (Nice to Have)
1. [Trace P2/P3 requirements]
2. [Add test traceability when tests exist]

---

## Traceability Maintenance

**To maintain traceability:**
1. When adding a requirement → immediately add to relevant design docs
2. When making design decisions → reference justifying requirement
3. Run `/req-trace` after each phase completion
4. Update `traces_to` fields in requirements.yaml as artifacts evolve

**Automated checks:**
- `/req-audit` validates requirement structure
- `/req-trace` validates traceability (this command)
- `/rubric-eval` includes traceability assessment (v1.6.0)

---

## Next Steps

1. Fix critical gaps (P0 orphaned requirements)
2. Update requirements.yaml with missing `traces_to` links
3. Add missing requirements for orphaned design
4. Re-run `/req-trace` to verify fixes
5. Proceed to next phase once traceability health is ✅

---

**END OF REPORT**
```

---

## Save Output

**File:** `artifacts/rubric-reports/req-traceability-report.md`

---

## Analysis Tips

**Finding requirement references in documents:**
- Search for patterns: `PRD-[A-Z]+-[0-9]{3}(-ASMP)?` (hierarchical naming v2.0.0)
- Old pattern (if upgrading old docs): `[A-Z]{2,3}-[A-Z]+-[0-9]{3}`
- Look in tables, lists, headers
- Check code comments if any test code exists

**Determining "orphaned" status:**
- P0 with no traces at v1.3.0+ → CRITICAL
- P1 with no traces at v1.4.0+ → WARNING
- P2/P3 with no traces → ACCEPTABLE

**Broken link detection:**
- Parse `traces_to` fields
- Check if file exists
- Check if anchor/section exists (if specified)

---

## After Completion

Display summary to user:
```
✅ Traceability Matrix Generated

Total Requirements: XX
Traceability Health: [✅/⚠️/❌]

Status:
- Fully Traced: XX (XX%)
- Partially Traced: XX (XX%)
- Orphaned: XX (XX%)

Critical Issues:
- P0 Orphaned: X
- P1 Orphaned: X
- Broken Links: X
- Orphaned Design: X

Report: artifacts/rubric-reports/req-traceability-report.md

Next: [Fix critical gaps / Proceed to next phase]
```
