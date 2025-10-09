---
description: Validate requirements.yaml compliance with requirements-policy.md
---

# Requirements Audit - Compliance Checker

Validate `source/requirements.yaml` against the standards defined in `docs/requirements-policy.md`.

## Your Task

Perform systematic compliance check of all requirements and generate audit report.

---

## Step 1: Load Standards (1 min)

Read these files:
- `docs/requirements-policy.md` - Standards reference
- `source/requirements.yaml` - Requirements to audit

---

## Step 2: Naming Convention Compliance (2 min)

**Check each requirement ID follows pattern:** `[CATEGORY]-[SUBCATEGORY]-[NUMBER]`

**Valid Categories:**
- SYS, EE, MFG, USR, NFR, PRD

**Valid Subcategories (examples):**
- EE-PWR, EE-CTRL, EE-IO, EE-COMM, EE-SNS, EE-ACT
- SYS-FUNC, SYS-PERF, SYS-IF
- MFG-COST, MFG-VOL, MFG-TIME, MFG-DFM
- USR-PORT, USR-UX, USR-ACC
- NFR-PERF, NFR-REL, NFR-STD, NFR-SEC

**Check:**
- [ ] All IDs follow format
- [ ] No duplicate IDs
- [ ] Numbers are 3-digit zero-padded (001, 002, 003)
- [ ] Sequential within subcategory

**Generate:**
| Req ID | Format Valid? | Issue (if any) |
|--------|---------------|----------------|
| SYS-FUNC-001 | ✅ | - |
| EE-PWR-001 | ✅ | - |
| BAD-ID | ❌ | Missing subcategory |

---

## Step 3: Mandatory Fields Check (3 min)

**Each requirement MUST have:**
- `title` - Short descriptive name (< 10 words)
- `description` - Clear, testable statement
- `source` - Origin (PDF page, derived from, etc.)
- `priority` - P0-Critical, P1-High, P2-Medium, P3-Low
- `category` - Must match ID prefix (SYS→System, EE→Electrical, etc.)

**Category Validation:**
The `category` field must be consistent with the requirement ID prefix:
- `SYS-*` → category must indicate "System" or "Functional"
- `EE-*` → category must indicate "Electrical"
- `MFG-*` → category must indicate "Manufacturing"
- `USR-*` → category must indicate "User Experience" or "Usability"
- `NFR-*` → category must indicate "Non-Functional", "Performance", "Reliability", "Compliance", etc.

**Generate:**
| Req ID | Title | Desc | Source | Priority | Category Match? | Status |
|--------|-------|------|--------|----------|-----------------|--------|
| SYS-FUNC-001 | ✅ | ✅ | ✅ | ✅ | ✅ Functional | PASS |
| EE-PWR-002 | ✅ | ✅ | ❌ | ✅ | ❌ Says "System" | FAIL - source missing, category mismatch |

**Common Issues:**
- Category says "Functional" but ID is `MFG-*`
- Category missing entirely
- Category says "Other" (too vague)

---

## Step 4: SMART Criteria Check (5 min)

**For each requirement, evaluate:**

**S - Specific:** No vague language ("fast", "good", "user-friendly")
- ❌ "Device should be fast"
- ✅ "Display shall refresh within 2 seconds"

**M - Measurable:** Quantifiable acceptance criteria present
- ❌ "Shall be portable"
- ✅ "Shall weigh < 500g"

**A - Achievable:** Technically feasible (use engineering judgment)
- ❌ "Shall cost $1 in high volume" (unrealistic)
- ✅ "Shall cost < $100 in volumes > 10K/year"

**R - Relevant:** Traceable to project goals (check source field)
- ❌ No source listed
- ✅ "source: PDF p.9 'portable companion device'"

**T - Testable:** Verification method specified
- ❌ No verification_method field
- ✅ "verification_method: Power budget analysis + battery life test"

**Generate SMART compliance table:**
| Req ID | S | M | A | R | T | Issues |
|--------|---|---|---|---|---|--------|
| SYS-FUNC-001 | ✅ | ✅ | ✅ | ✅ | ✅ | None |
| USR-UX-001 | ⚠️ | ❌ | ✅ | ✅ | ✅ | Not measurable: "intuitive" undefined |

---

## Step 5: Priority Distribution Analysis (2 min)

**Count requirements by priority:**
| Priority | Count | Percentage | Guideline |
|----------|-------|------------|-----------|
| P0-Critical | X | XX% | 20-30% (must have) |
| P1-High | X | XX% | 30-40% (should have) |
| P2-Medium | X | XX% | 20-30% (nice to have) |
| P3-Low | X | XX% | 10-20% (future) |

**Red flags:**
- ⚠️ > 50% P0 (too aggressive - timeline risk)
- ⚠️ < 10% P0 (insufficiently prioritized)
- ✅ Balanced distribution

---

## Step 6: Traceability Check (3 min)

**For each requirement, check `traces_to` fields:**

**Forward traceability (requirement → artifact):**
- [ ] `traces_to.design` - Links to architecture.md, tradeoffs.md, solution.md
- [ ] `traces_to.analysis` - Links to requirements.md
- [ ] `traces_to.tradeoffs` - Links to tradeoffs.md (if applicable)
- [ ] `traces_to.solution` - Links to solution.md (if applicable)

**Orphaned requirements (no forward trace):**
| Req ID | Priority | Issue |
|--------|----------|-------|
| EE-IO-002 | P1 | No design trace |

**Note:** Early in project, some traces may be empty - that's OK. Flag as "TODO" not "FAIL".

---

## Step 7: Derived Requirements Check (2 min)

**For requirements with `source: "Derived from ..."`:**
- [ ] `calculation` field present (shows the math)
- [ ] Parent requirement IDs referenced
- [ ] Logic is sound

**Example:**
```yaml
SYS-FUNC-003:
  source: "Derived from SYS-FUNC-001 + SYS-FUNC-002"
  calculation: "32 characters × 6 dots/character = 192 signals"
```

**Check:**
| Req ID | Parents | Calculation | Valid? |
|--------|---------|-------------|--------|
| SYS-FUNC-003 | SYS-FUNC-001, SYS-FUNC-002 | ✅ | ✅ |

---

## Step 8: Standards Compliance (2 min)

**Check for standards awareness requirements:**
- [ ] At least one NFR-STD-* requirement exists
- [ ] Relevant standards identified (FCC/CE, UL, ADA, ISO, etc.)
- [ ] Standards appropriate for product domain

**Red flags:**
- ❌ No standards requirements at all
- ❌ Vague: "Shall comply with all applicable standards"
- ✅ Specific: "Shall comply with FCC Part 15 Class B (EMI)"

---

## Output Format

Generate audit report in Markdown:

```markdown
# Requirements Audit Report

**Project:** Lam Research - Braille Display EE Concept Evaluation
**Date:** YYYY-MM-DD
**Source:** source/requirements.yaml
**Standards:** docs/requirements-policy.md
**Total Requirements:** XX

---

## Executive Summary

**Overall Compliance: [PASS / CONDITIONAL PASS / FAIL]**

- **Naming Compliance:** XX/XX (XX%)
- **Mandatory Fields:** XX/XX (XX%)
- **Category Consistency:** XX/XX (XX%)
- **SMART Criteria:** XX/XX (XX%)
- **Traceability:** XX/XX traced (XX% - expected at this stage)

**Critical Issues:** X
**Warnings:** X
**Recommendations:** X

---

## 1. Naming Convention Compliance

**Status:** [PASS / FAIL]

| Req ID | Valid? | Issue |
|--------|--------|-------|
| ... | ... | ... |

**Issues Found:**
- [List any ID format violations]

**Recommendation:**
- [Actions to fix, if any]

---

## 2. Mandatory Fields Compliance

**Status:** [PASS / FAIL]

**Missing Fields Summary:**
| Req ID | Missing Fields |
|--------|----------------|
| EE-PWR-002 | source, verification_method |

**Category Consistency Check:**
| Req ID | Category Field | Expected (from ID) | Match? |
|--------|----------------|-------------------|--------|
| SYS-FUNC-001 | Functional | System/Functional | ✅ |
| MFG-COST-001 | Electrical | Manufacturing | ❌ MISMATCH |

**Statistics:**
- title: XX/XX (XX%)
- description: XX/XX (XX%)
- source: XX/XX (XX%)
- priority: XX/XX (XX%)
- category: XX/XX (XX%)
- category consistency: XX/XX (XX%)

---

## 3. SMART Criteria Analysis

**Status:** [PASS / CONDITIONAL PASS / FAIL]

**Detailed Scoring:**
| Req ID | S | M | A | R | T | Score | Issues |
|--------|---|---|---|---|---|-------|--------|
| SYS-FUNC-001 | ✅ | ✅ | ✅ | ✅ | ✅ | 5/5 | None |
| USR-UX-001 | ⚠️ | ❌ | ✅ | ✅ | ✅ | 3/5 | Not measurable |

**Summary:**
- 5/5 (Excellent): XX requirements
- 4/5 (Good): XX requirements
- 3/5 (Adequate): XX requirements
- < 3/5 (Poor): XX requirements

**Common Issues:**
- [List patterns - e.g., "3 requirements use vague terms like 'user-friendly'"]

**Recommendations:**
1. [Specific improvements for flagged requirements]

---

## 4. Priority Distribution

| Priority | Count | Percentage | Guideline | Status |
|----------|-------|------------|-----------|--------|
| P0-Critical | X | XX% | 20-30% | [✅/⚠️/❌] |
| P1-High | X | XX% | 30-40% | [✅/⚠️/❌] |
| P2-Medium | X | XX% | 20-30% | [✅/⚠️/❌] |
| P3-Low | X | XX% | 10-20% | [✅/⚠️/❌] |

**Assessment:** [Balanced / Too aggressive / Under-prioritized]

**Recommendation:** [Adjust specific requirements if distribution off]

---

## 5. Traceability Status

**Forward Traceability (Req → Artifact):**
- With design trace: XX/XX (XX%)
- With analysis trace: XX/XX (XX%)
- Orphaned (no trace): XX/XX (XX%)

**Orphaned Requirements:**
| Req ID | Priority | Recommendation |
|--------|----------|----------------|
| [List] | [Pri] | [Add trace to...] |

**Note:** At v1.2.0 phase, some traces may be TODO - this is expected.

---

## 6. Derived Requirements

**Total Derived:** X
**With Calculation:** X/X (XX%)

**Issues:**
| Req ID | Issue |
|--------|-------|
| [List any missing calculations or invalid logic]

---

## 7. Standards Compliance

**Standards Requirements Found:** X
**Standards Identified:** [List standards - FCC/CE, UL, ADA, etc.]

**Status:** [PASS / FAIL]

**Coverage:**
- [ ] EMI/RF compliance
- [ ] Safety (electrical, battery)
- [ ] Accessibility
- [ ] Environmental (RoHS, REACH, etc.)

---

## Critical Issues (Must Fix Before v1.2.0 Complete)

1. **[Issue Title]** - [Req ID or pattern]
   - **Problem:** [Description]
   - **Impact:** [Why this matters]
   - **Fix:** [Specific action]

---

## Warnings (Should Fix Soon)

1. **[Warning Title]** - [Req ID or pattern]
   - **Problem:** [Description]
   - **Impact:** [Minor impact]
   - **Fix:** [Suggested action]

---

## Recommendations for Improvement

1. [General improvement suggestion]
2. [Process recommendation]
3. [Best practice to adopt]

---

## Compliance Summary

| Criterion | Status | Score |
|-----------|--------|-------|
| Naming Convention | [✅/⚠️/❌] | XX/XX |
| Mandatory Fields | [✅/⚠️/❌] | XX/XX |
| Category Consistency | [✅/⚠️/❌] | XX/XX |
| SMART Criteria | [✅/⚠️/❌] | XX/XX |
| Priority Distribution | [✅/⚠️/❌] | Balanced |
| Traceability | [✅/⚠️/❌] | XX% traced |
| Derived Requirements | [✅/⚠️/❌] | XX/XX |
| Standards | [✅/⚠️/❌] | Coverage OK |

**Overall: [PASS / CONDITIONAL PASS / FAIL]**

---

## Gate Decision

**Can proceed to requirements.md generation?** [✅ YES / ⚠️ WITH FIXES / ❌ NO]

**Required before proceeding:**
- [List blocking issues, if any]

**Recommended before proceeding:**
- [List warnings to address]

---

## Next Steps

1. [Fix critical issues, if any]
2. Run `/req-yaml-to-md` to generate artifacts/requirements.md
3. Run `/rubric-eval` for Category 1 assessment

---

**Audit Complete**
```

---

## Save Output

**File:** `artifacts/rubric-reports/req-audit-report.md`

---

## Audit Principles

**Be Objective:**
- Check against documented standards (requirements-policy.md)
- Cite specific examples
- Use consistent criteria

**Be Constructive:**
- Explain WHY issues matter
- Provide specific fix recommendations
- Acknowledge what's done well

**Be Practical:**
- Remember project phase (concept evaluation, not production)
- Distinguish critical issues from nice-to-haves
- Consider 2-month timeline constraint

**Be Thorough:**
- Check ALL requirements
- Don't skip categories
- Generate complete compliance matrix

---

## After Completion

Display summary to user:
```
✅ Requirements Audit Complete

Total Requirements: XX
Compliance Score: XX/XX (XX%)

Critical Issues: X
Warnings: X

Status: [PASS / CONDITIONAL PASS / FAIL]

Report: artifacts/rubric-reports/req-audit-report.md
```
