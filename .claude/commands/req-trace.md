---
description: Generate traceability matrix from requirements.yaml
---

# Requirements Traceability Matrix Generator

⚠️ **TODO: This command needs enhancement**

**Current Status:** Basic ID checking only (validates requirement IDs exist in architectures.yaml)

**Enhancement Plan:** See [docs/requirements-trace-plan.md](../../../docs/requirements-trace-plan.md) for comprehensive coverage matrix implementation

**What's Missing:**
- Coverage matrix (which requirements each architecture satisfies)
- Subsystem traceability (verify subsystems actually provide the requirement)
- Vertical traces (requirement → architecture → subsystem → part → BOM)
- Validation issues (dangling references, orphaned requirements)

**Current Basic Implementation:**

## Your Task

Parse `source/requirements.yaml` and `source/architectures.yaml` to verify:
1. All requirement IDs in `architectures.yaml` exist in `requirements.yaml`
2. Generate basic traceability report showing which architectures claim which requirements

---

## Step 1: Load Source Files (1 min)

```python
requirements = load_yaml("source/requirements.yaml")
architectures = load_yaml("source/architectures.yaml")
```

Extract:
- All requirement IDs from requirements.yaml (27 requirements)
- All `traces_to_requirements` lists from architectures.yaml

---

## Step 2: Validate References (2 min)

For each architecture, check if all `traces_to_requirements` IDs exist:

```python
req_ids = set(requirements['requirements'].keys())

for arch in architectures:
    for req_ref in arch.get('traces_to_requirements', []):
        if req_ref not in req_ids:
            print(f"❌ ERROR: {arch['id']} references non-existent {req_ref}")
```

---

## Step 3: Generate Basic Report (2 min)

Create `artifacts/rubric-reports/req-traceability-report.md`:

```markdown
# Requirements Traceability Report (Basic)

**Generated:** YYYY-MM-DD
**Source Files:** requirements.yaml (27 reqs), architectures.yaml (3 archs)

⚠️ **Note:** This is a basic report. See [docs/requirements-trace-plan.md](../../../docs/requirements-trace-plan.md) for planned enhancements.

---

## Architecture → Requirement Mapping

### ARCH_SOL_ECO
Traces to: [list requirement IDs]

### ARCH_PIEZO_ECO
Traces to: [list requirement IDs]

### ARCH_PIEZO_DLX
Traces to: [list requirement IDs]

---

## Validation Results

✅ All requirement references valid
❌ Found X dangling references

---

## Limitations

This basic report only checks ID validity. It does NOT:
- Verify subsystems actually provide the requirement
- Generate coverage matrix (% of requirements each arch satisfies)
- Check if parts exist in BOM
- Validate quantitative specs match requirements

**See [docs/requirements-trace-plan.md](../../../docs/requirements-trace-plan.md) for full implementation plan.**
```

---

## Save Output

**File:** `artifacts/rubric-reports/req-traceability-report.md`

---

## After Completion

Display summary:
```
✅ Basic Traceability Report Generated

Architectures: 3
Requirements referenced: X
Validation: [✅ PASS / ❌ ERRORS FOUND]

⚠️  This is a basic check. See docs/requirements-trace-plan.md for comprehensive coverage matrix.

Report: artifacts/rubric-reports/req-traceability-report.md
```
