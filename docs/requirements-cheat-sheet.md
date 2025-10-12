# Requirements Cheat Sheet - Quick Reference

**Last Updated:** 2025-10-08 (v2.0.0 hierarchical refactor)

---

## Hierarchical Naming Convention

```
PRD-XXXX-NNN         = Ground Truth (verbatim from PDF)
PRD-XXXX-NNN-ASMP    = Assumption (our interpretation)
```

**Categories:**
- **PRD-SCHED** = Schedule/Timeline
- **PRD-SIZE** = Size/Portability
- **PRD-IFACE** = Interface/Connectivity
- **PRD-COST** = Cost
- **PRD-VOL** = Volume/Manufacturing
- **PRD-USER** = User/Accessibility
- **PRD-FUNC** = Functional

---

## All Requirements (Quick List)

### Ground Truth (9 requirements)

| ID | Title | Status | Priority |
|----|-------|--------|----------|
| PRD-SCHED-001 | Production Timeline (2 months) | VAGUE | P0 |
| PRD-SIZE-001 | Portable Device | VAGUE | P1 |
| PRD-IFACE-001 | Cell Phone Connectivity | VAGUE | P0 |
| PRD-COST-001 | Low Cost at Volume | VAGUE | P0 |
| PRD-VOL-001 | High Volume Production | VAGUE | P1 |
| PRD-USER-001 | Sight-Impaired User | CLEAR | P0 |
| PRD-FUNC-001 | 32 Braille Characters, 6 Dots Each | CLEAR | P0 |
| PRD-FUNC-002 | Braille Line Update | VAGUE | P1 |
| PRD-FUNC-003 | Raised or Lowered Dots | CLEAR | P0 |

### Assumptions (6 requirements)

| ID | Title | Risk | Validation |
|----|-------|------|------------|
| PRD-SCHED-001-ASMP | Pilot Production (100-500 units) | MEDIUM | YES |
| PRD-SIZE-001-ASMP | ≤1.3 lbs, 8"×4"×1" | MEDIUM | YES |
| PRD-IFACE-001-ASMP | BLE/USB-C options | HIGH | YES |
| PRD-COST-001-ASMP | $200 ±$100 BOM @ 10k/mo | CRITICAL | YES |
| PRD-VOL-001-ASMP | 10k units/month | HIGH | YES |
| PRD-FUNC-002-ASMP | <2 sec refresh, tactile buttons | MEDIUM | YES |

---

## Critical Assumptions (Need Customer Validation!)

### 🔴 CRITICAL: PRD-COST-001-ASMP

**Assumption:** $200 BOM ±$100 (range: $100-$300)

**Why Critical:** Drives entire architecture selection
- $100 BOM → Eliminates most actuator options
- $200 BOM → Mid-range baseline
- $300 BOM → Opens premium options (solenoid, haptic)

**Sensitivity Test (v1.4.0):** Design architectures at $100, $150, $200, $250, $300

---

### 🔴 HIGH: PRD-IFACE-001-ASMP

**Assumption:** BLE primary, USB-C secondary/fallback

**Portfolio Approach (v1.3.0):**
- Architecture A: BLE-only ($200-250 BOM)
- Architecture B: USB-C wired ($100-150 BOM) ← lowest cost!
- Architecture C: Hybrid BLE+USB ($250-300 BOM)

**Key Insight:** USB-C wired (tethered to phone) is valid low-cost option ($100-150 BOM savings!)

---

### 🔴 HIGH: PRD-VOL-001-ASMP

**Assumption:** 10k units/month (120k/year)

**Impact:**
- Drives DFM decisions (SMT vs hand assembly)
- Component selection (multi-source, no obsolete parts)
- NRE vs unit cost trade-off

**Sensitivity Test (v1.4.0):** 1k/month vs 10k/month vs 100k/month

---

## Slash Commands for Requirements

```bash
/req-yaml-to-md       # Generate artifacts/requirements.md from YAML
/req-trace            # Generate traceability matrix (TODO: update for PRD naming)
/req-audit            # Validate requirements structure (TODO: run)
/status               # Check time tracking progress
```

---

## Workflow: Modifying Requirements

1. **Edit:** `source/requirements.yaml` (SSOT)
2. **Regenerate:** `/req-yaml-to-md` → `artifacts/requirements.md`
3. **Validate:** `/req-audit`
4. **Commit:** Git commit with BREAKING CHANGE note (if naming changes)

**⚠️ NEVER edit `artifacts/requirements.md` directly - it's auto-generated!**

---

## Phase Gate Checklist (v1.2.0 → v1.3.0)

Before proceeding to Architecture Design:

- [x] Extract 9 ground truth requirements from PDF
- [x] Create 6 assumptions for vague requirements
- [x] Single source of truth (requirements.yaml v2.0.0)
- [x] Generate requirements.md with summaries
- [ ] Run `/req-audit` to validate structure
- [ ] Customer review (if available) - 6 assumptions need validation
- [ ] **FREEZE requirements.yaml** (no changes without change request)

---

## Standards Quick Reference

### Braille Dimensions (US ADA 703.3)

| Parameter | Target | Tolerance | Standard Range |
|-----------|--------|-----------|----------------|
| Dot diameter | 1.5 mm | ±0.1 mm | 1.5-1.6 mm (ADA) |
| Dot height | 0.6 mm | ±0.1 mm | 0.64-0.94 mm (ADA) |
| Dot spacing (within cell) | 2.5 mm | ±4% | 2.3-2.5 mm (ADA) |
| Cell spacing (between chars) | 6.0 mm | ±8% | 6.1-7.6 mm (ADA) |
| Holding force | 75 g | ±33% | 50-100 g (literature) |

**Display width:** 32 cells × 6mm = 192mm (~7.6 inches)

---

## Cost Breakdown (Assumption: $200 BOM)

| Component | % of BOM | Cost Range |
|-----------|----------|------------|
| Actuators (192) | 40-50% | $80-$100 |
| PCB Assembly | 15% | $30 |
| Battery (if used) | 10% | $20 |
| Enclosure | 10% | $20 |
| Misc (connectors, buttons, etc.) | 15-25% | $30-$50 |

**Note:** USB-C wired option saves $100-150 (no battery, simpler power)

---

## Competitor Benchmarks

| Product | Retail | Cells | Weight | Features |
|---------|--------|-------|--------|----------|
| BrailleMe | $515.50 | 20 | 1.3 lbs | BLE, USB, SD, Perkins keyboard |
| Orbit Reader | $449 | 20 | - | Refreshable braille |
| APH Refreshabraille | $1,795 | 18 | - | Premium product |
| **Our Target** | **~$600** | **32** | **≤1.3 lbs** | **BLE/USB-C, tactile buttons** |

**Competitive Advantage:** 60% more characters (32 vs 20) at similar price

---

## Risk Summary (Assumptions)

| Risk Level | Count | Requirements |
|------------|-------|--------------|
| 🔴 CRITICAL | 1 | Cost ($200 ±$100) |
| 🔴 HIGH | 2 | Interface (BLE vs USB-C), Volume (10k/month) |
| 🟡 MEDIUM | 3 | Schedule (pilot), Size (≤1.3 lbs), Refresh (<2 sec) |

**All 6 assumptions require customer validation before finalizing design!**

---

## File Locations

```
source/requirements.yaml           # SSOT (edit this)
artifacts/requirements.md          # Generated report (read-only)
artifacts/REQUIREMENTS-CHEAT-SHEET.md  # This file
reference/standards/braille-dimensions-standards.md  # Braille specs
docs/requirements-policy.md        # Requirements standards
TIME-LOG.md                        # Time tracking
```

---

## Useful Grep Patterns

```bash
# Find all VAGUE requirements
grep "status: \"VAGUE" source/requirements.yaml

# Find all assumptions
grep "ASMP:" source/requirements.yaml

# Find CRITICAL risks
grep "risk_level: CRITICAL" source/requirements.yaml

# Find customer validation needs
grep "customer_validation_needed: YES" source/requirements.yaml
```

---

## Next Phase Preview: v1.3.0 Architecture Design

**Goal:** Design portfolio of 3-4 architectures at different cost points

**Architectures to Design:**
1. **Architecture A (BLE wireless):** $200-250 BOM, battery, most portable
2. **Architecture B (USB-C wired):** $100-150 BOM, tethered, lowest cost
3. **Architecture C (Hybrid BLE+USB):** $250-300 BOM, best UX
4. **(Optional) Architecture D:** Premium features (haptic, audio), $300+ BOM

**Key Decisions:**
- Actuator technology: Piezo vs solenoid vs SMA vs voice coil
- Microcontroller: STM32, ESP32, nRF52, RP2040
- I/O expansion: Shift registers, I2C GPIO expanders, mux
- Power architecture: Li-ion vs AA/AAA vs USB-C parasitic

---

**END OF CHEAT SHEET**
