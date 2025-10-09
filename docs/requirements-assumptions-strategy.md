# Requirements Assumptions Strategy - KISS Version

**Problem:** Many requirements are vague ("low-cost", "portable", "high-volume")

**Solution:** Tag assumptions, make them explicit, test in sensitivity analysis

---

## Quick Rules:

### 1. Tag Unknown Requirements with `assumption_risk: HIGH/MEDIUM/LOW`

**Example:**
```yaml
MFG-COST-001:
  title: "Low-Cost BOM Target"
  description: "Unit cost shall be <$50 BOM at 1000-unit volume"
  source: "PDF p.9 'low-cost design'"
  assumption: "ASSUMED <$50 based on competitor products ($80-200 retail)"
  assumption_risk: HIGH  # ← This is KEY!
  rationale: "PDF says 'low-cost' but doesn't specify target"
```

### 2. Document Assumptions in Requirements YAML

Already doing this! (line 36-47 in your requirements.yaml)

### 3. Link High-Risk Assumptions → Sensitivity Analysis

**In docs/tradeoffs.md sensitivity section:**
```markdown
## Sensitivity to Requirements Assumptions

### Cost Assumption (HIGH RISK)
**Assumption:** "Low-cost" = <$50 BOM
**Test:** What if stakeholder actually wants <$30? Or <$100 is acceptable?
**Impact:**
- If <$30: Architecture C fails (too expensive)
- If <$100: Architecture A becomes viable (better reliability)
```

---

## The 5-Minute Fix for v1.2.0:

**Instead of getting stuck defining perfect requirements:**

1. ✅ Use PDF language directly ("low-cost", "portable")
2. ✅ Add your **ASSUMED** interpretation ("ASSUMED <$50 BOM")
3. ✅ Tag the risk level (`assumption_risk: HIGH`)
4. ✅ Test it in sensitivity analysis (v1.4.0)
5. ✅ Document in presentation: "Given vague spec, I assumed..."

---

## Example Requirements (copy-paste ready):

```yaml
MFG-COST-001:
  title: "Low-Cost BOM Target"
  description: "Unit cost shall be ≤$50 BOM at 1000-unit volume (ASSUMED)"
  source: "PDF p.9 'low-cost design for high-volume manufacturing'"
  assumption: "Interpreted 'low-cost' as <$50 BOM based on competitor braille displays ($80-200 retail, ~40% BOM ratio)"
  assumption_risk: HIGH
  verification: "BOM spreadsheet from selected suppliers (Digikey, Mouser)"
  priority: P0-Critical

MFG-VOL-001:
  title: "High-Volume Production Capability"
  description: "Design shall support >10,000 units/year production volume (ASSUMED)"
  source: "PDF p.9 'high-volume manufacturing'"
  assumption: "Interpreted 'high-volume' as >10K/year based on accessibility market size"
  assumption_risk: MEDIUM
  verification: "DFM analysis, supplier capacity confirmation"
  priority: P1-High

USR-PORT-001:
  title: "Portable Form Factor"
  description: "Device shall be ≤200g weight, ≤20cm × 10cm × 3cm dimensions (ASSUMED)"
  source: "PDF p.9 'portable companion device'"
  assumption: "Interpreted 'portable' as pocket/bag-portable, comparable to smartphone size"
  assumption_risk: MEDIUM
  verification: "CAD model, weight budget spreadsheet"
  priority: P1-High
```

---

## The Payoff:

**When LAM asks:** "Why did you choose $50 as the cost target?"

**You answer:** "The PDF said 'low-cost' but didn't specify a number. I researched competitor braille displays ($80-200 retail), assumed 40% BOM ratio, and set <$50 as the target. However, I tested sensitivity: if the actual target is $30, Architecture C fails; if $100 is acceptable, Architecture A becomes viable. Here's the analysis..."

**This shows:**
- ✅ Engineering judgment (made reasonable assumption)
- ✅ Transparency (documented the assumption)
- ✅ Risk management (tested what happens if wrong)
- ✅ Adaptability (know which design wins under different assumptions)

---

## STOP OVERTHINKING, START DESIGNING!

**Next action:**
1. Copy 3 example requirements above into `source/requirements.yaml`
2. Add 12 more requirements (use PDF language + ASSUMED values)
3. Mark v1.2.0 DONE
4. Move to v1.3.0 (design architectures!)
5. Come back to sensitivity analysis in v1.4.0

**Total time:** 2 hours, not 2 days!

---

**Remember:** LAM wants to see HOW you think, not a perfect requirements spec. They EXPECT you to make assumptions when info is missing!
