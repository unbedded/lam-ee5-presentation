---
description: Generate requirements.yaml to cheat sheet (lean ASCII tree + quick reference)
---

# Requirements Cheat Sheet Generator

Generate a **token-efficient** quick reference from requirements.yaml (<5KB vs 32KB full requirements.md).

## What to Generate

**Output File:** `artifacts/requirements-cheat-sheet.md`

## Content Sections

### 1. Header
```markdown
# Requirements Cheat Sheet (Auto-Generated)

**Source:** source/requirements.yaml v{version}
**Generated:** {date}
**Total Requirements:** {count} ({ground_truth} ground truth + {assumptions} assumptions + {standards} standards)
```

### 2. Category Codes Reference
Extract from `source/requirements-policy.md` lines 25-34:

```markdown
## Category Codes

| Code | Category | Description |
|------|----------|-------------|
| **SYS** | System Requirements | High-level functional requirements |
| **EE** | Electrical Engineering | Electrical design requirements |
| **MFG** | Manufacturing | Production & cost requirements |
| **USR** | User Experience | Usability & accessibility requirements |
| **NFR** | Non-Functional | Performance, reliability, compliance |
| **PRD** | Production | Timeline, supply chain, delivery |
```

### 3. Requirements Hierarchy (ASCII Tree)
```markdown
## Requirements Hierarchy

PRD (24 total: 9 ground truth + 13 assumptions + 2 standards)
├── SCHEDULE (3 requirements)
│   ├── PRD-SCHED-001 [P0][VAGUE] Production Timeline
│   ├── PRD-SCHED-001-ASMP [P0][MEDIUM] Pilot Production (100-500 units)
│   └── PRD-SCHED-002-ASMP [P0][CRITICAL] COTS Mandate (≤4 week lead)
├── SIZE (2 requirements)
│   ├── PRD-SIZE-001 [P1][VAGUE] Portable Device
│   └── PRD-SIZE-001-ASMP [P1][MEDIUM] ≤1.3 lbs, 200-280mm
├── INTERFACE (2 requirements)
│   ├── PRD-IFACE-001 [P0][VAGUE] Cell Phone Connectivity
│   └── PRD-IFACE-001-ASMP [P0][HIGH] BLE/USB-C Portfolio
├── COST (2 requirements)
│   ├── PRD-COST-001 [P0][VAGUE] Low Cost
│   └── PRD-COST-001-ASMP [P0][CRITICAL] $200 ±$100 BOM @ 10k/mo
├── VOLUME (2 requirements)
│   ├── PRD-VOL-001 [P1][VAGUE] High Volume
│   └── PRD-VOL-001-ASMP [P1][HIGH] 10k/month capability
├── USER (1 requirement)
│   └── PRD-USER-001 [P0][CLEAR] Sight-Impaired User
├── FUNCTIONAL (7 requirements)
│   ├── PRD-FUNC-001 [P0][CLEAR] 32 chars × 6 dots = 192 actuators
│   ├── PRD-FUNC-002 [P1][VAGUE] Braille Line Update
│   ├── PRD-FUNC-002-ASMP [P1][MEDIUM] <2 sec refresh, tactile buttons
│   ├── PRD-FUNC-003 [P0][CLEAR] Raised/Lowered Dots
│   ├── PRD-FUNC-003-ARCH-C-EXCEPT [P1][MEDIUM] 4mm solenoid exception (ARCH-C only)
│   ├── PRD-FUNC-005-ASMP [P2][LOW] 125 words/min reading speed
│   └── PRD-FUNC-006-ASMP [P2][LOW] 50%/25%/25% duty cycle
├── POWER (3 requirements)
│   ├── PRD-POWER-003-ASMP [P0][MEDIUM] USB: ≤2.0W
│   ├── PRD-POWER-004-ASMP [P1][HIGH] AA: ≤1.5W (8h life)
│   └── PRD-POWER-005-ASMP [P1][LOW] Li-ion: ≤3.7W (2h life)
└── STANDARDS (2 requirements)
    ├── NFR-STD-001 [P1] UL + FCC Compliance
    └── NFR-STD-002 [P0] US ADA 703.3 Braille Dimensions
```

**Format Rules:**
- Ground truth: `[Priority][Status]` where Status = VAGUE | CLEAR
- Assumptions: `[Priority][Risk]` where Risk = CRITICAL | HIGH | MEDIUM | LOW
- Standards: `[Priority]` only
- Title: Short 1-liner summary (not full description)

### 4. Quick Stats
```markdown
## Quick Stats

**By Type:**
- Ground Truth: 9 requirements (6 VAGUE, 3 CLEAR)
- Assumptions: 13 requirements (2 CRITICAL, 3 HIGH, 5 MEDIUM, 3 LOW)
- Standards: 2 requirements

**By Priority:**
- P0-Critical: X requirements
- P1-High: X requirements
- P2-Medium: X requirements
- P3-Low: X requirements

**Risk Assessment:**
- Customer validation needed: 13 assumptions
- CRITICAL risk assumptions: 2
- HIGH risk assumptions: 3
```

### 5. Critical Assumptions List
```markdown
## Critical Assumptions (Customer Validation Required!)

### 🔴 CRITICAL Risk (2)
1. **PRD-SCHED-002-ASMP:** COTS mandate (≤4 week lead) → Solenoid only, no custom piezo
   - Impact: Custom piezo requires 8-12 weeks → Misses 2-month deadline by 6-10 weeks

2. **PRD-COST-001-ASMP:** $200 ±$100 BOM @ 10k/mo → Drives architecture selection
   - Impact: If $100 target → Eliminates most actuator options. If $300 → Opens premium options.

### 🟠 HIGH Risk (3)
3. **PRD-IFACE-001-ASMP:** BLE vs USB portfolio → 3 architectures
   - Impact: BLE-only eliminates low-cost. USB-only eliminates wireless UX.

4. **PRD-VOL-001-ASMP:** 10k/month capability → DFM decisions
   - Impact: If 1k/month → Hand assembly OK. If 100k/month → Full automation required.

5. **PRD-POWER-004-ASMP:** AA 8h life @ 1.5W → Piezo exceeds by 46%
   - Impact: Piezo (2.16W) doesn't fit AA budget. Need solenoid+latch or larger battery.
```

### 6. Slash Commands Reference
```markdown
## Slash Commands

```bash
/req-yaml-to-md         # Generate full requirements.md (32KB, comprehensive)
/req-yaml-to-cheatsheet # Generate this cheat sheet (<5KB, quick reference)
/req-audit              # Validate SMART compliance
/req-trace              # Generate traceability matrix
/req-risk-report        # Risk-rank all assumptions
```
```

## Implementation Notes

1. **Parse requirements.yaml:**
   - Extract metadata.version, metadata.date
   - Group requirements by category (SCHED, SIZE, IFACE, COST, VOL, USER, FUNC, POWER)
   - Count ground truth (no "-ASMP" suffix), assumptions ("-ASMP" suffix), standards ("NFR-STD")

2. **Build ASCII tree:**
   - Use `├──` and `└──` for branches
   - Use `│` for continuation lines
   - Format: `ID [Priority][Status/Risk] Short Title`

3. **Calculate stats:**
   - Count by type (ground truth, assumptions, standards)
   - Count by priority (P0, P1, P2, P3)
   - Count by risk (CRITICAL, HIGH, MEDIUM, LOW for assumptions)
   - Count customer_validation_needed: YES

4. **Extract critical assumptions:**
   - Filter assumptions with risk_level: CRITICAL or HIGH
   - Show impact_if_wrong field
   - Limit to top 5-8 most critical

5. **Output format:**
   - Compact markdown (no extra whitespace)
   - Use tables where appropriate
   - Keep total file size < 5KB

## Success Criteria

- ✅ File size: < 5KB (vs 32KB for requirements.md)
- ✅ ASCII tree: All 24 requirements visible in hierarchy
- ✅ Quick stats: Accurate counts by type/priority/risk
- ✅ Critical assumptions: Top 5-8 with impact statements
- ✅ Self-documenting: Includes category codes and slash commands
- ✅ Token efficient: Minimal text, maximum information density

## Output Message

```
✅ Generated artifacts/requirements-cheat-sheet.md ({size} KB)

📊 Requirements Summary:
- Total: {total} ({ground_truth} ground truth + {assumptions} assumptions + {standards} standards)
- VAGUE ground truth: {vague_count} (need assumptions)
- CRITICAL assumptions: {critical_count} (customer validation required!)
- HIGH assumptions: {high_count}

⚠️  Use /req-yaml-to-md for full 32KB report with complete details.
    This cheat sheet is optimized for quick reference and token efficiency.
```
