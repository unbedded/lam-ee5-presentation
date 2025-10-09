# Production Plan Guide - v1.5.0

**Phase:** v1.5.0 Recommended Solution & Production Plan
**Rubric Weight:** 20/100 points (Step 4)
**PDF Source:** "Outline the process for transitioning the concept from initial design to volume production."

---

## Purpose: Show the Path from Concept → Pilot → Volume

**LAM wants to see:**
1. ✅ You understand **Design for Manufacturability (DFM)**
2. ✅ You have a **realistic 2-month timeline** to pilot production
3. ✅ You can **scale from pilot (10-100 units) → volume (10K+ units/year)**
4. ✅ You've **identified and mitigated risks** (timeline, cost, technical, supply chain)

**This is NOT:**
- ❌ A detailed manufacturing process spec (that comes post-pilot)
- ❌ A business plan (focus on engineering/production feasibility)
- ❌ A cost justification (that was v1.4.0 trade-off analysis)

**This IS:**
- ✅ A realistic **2-month Gantt chart** (design → pilot production)
- ✅ A **pilot validation strategy** (what you'll test with 10-100 units)
- ✅ A **scale plan** (how to go from pilot → 1K → 10K+ units)
- ✅ **Risk mitigation** (what could go wrong, what's your plan B?)

---

## Deliverable: `docs/solution.md`

### Required Sections:

#### 1. Selected Architecture
- **Final architecture selection** (from v1.4.0 trade-off analysis)
- **Justification** (data-driven: "Architecture C scored 8.2/10 vs 7.1 and 6.8")
- **Block diagram** (`resources/diagrams/final-architecture.png`)
- **Key components** (MCU, actuators, power, comm)

#### 2. Design Detail (Engineering Depth)
- **Preliminary schematics** (power, MCU core, I/O expansion, comm)
  - Show you understand the electrical design
  - Doesn't need to be production-ready, but shows feasibility
- **Power budget** (link to `resources/calculations/power-budget.xlsx`)
- **Thermal analysis** (worst-case power dissipation, cooling needed?)
- **PCB complexity** (2-layer? 4-layer? Stack-up considerations)

#### 3. 2-Month Timeline to Pilot Production ⭐ CRITICAL
**Gantt chart:** `resources/calculations/timeline-gantt.xlsx`

**Typical phases:**
| Week | Phase | Deliverables | Critical Path Items |
|------|-------|--------------|---------------------|
| 1 | Requirements finalization | requirements.yaml, component selection | Long-lead parts ordering |
| 2 | Architecture design | Block diagrams, preliminary schematics | MCU/actuator selection |
| 3 | Detailed schematic | Production schematics, BOM | Actuator samples ordered |
| 4 | PCB layout | Gerbers, assembly drawings | PCB fab (2-3 week lead) |
| 5 | Component procurement | Parts arrival, kitting | Critical: actuators, MCU |
| 6 | PCB fabrication | Bare boards arrive | 10-15 day fab cycle |
| 7 | Assembly & bring-up | First 5-10 prototypes assembled | Debug/rework |
| 8 | Pilot production | 10-100 units, validation testing | Production-ready design |

**Critical Path:**
- Actuator selection (Week 2) → Actuator samples (Week 3-4) → Pilot build (Week 7-8)
- PCB design (Week 4) → PCB fab (Week 5-6) → Assembly (Week 7)

#### 4. Pilot Production Strategy (10-100 Units)
**Purpose of pilot:**
- ✅ Validate design (does it work as expected?)
- ✅ Verify manufacturing tolerances (can it be assembled reliably?)
- ✅ Identify failure modes (what breaks? how often?)
- ✅ Test DFM (yield rate, assembly time, rework needed?)

**Pilot validation plan:**
- **Functional testing:** All 192 actuators working? BLE connectivity? Battery life?
- **Reliability testing:** 100-hour burn-in? Drop test? Button cycle test?
- **Manufacturing assessment:** Assembly time per unit? Yield rate? Defect types?
- **User testing:** 5-10 beta testers with target demographic?

**Success criteria:**
- >90% yield on pilot run (9/10 units pass functional test)
- <10% rework rate (assembly issues minimal)
- User feedback positive (readability, UX, battery life acceptable)

#### 5. Design for Manufacturability (DFM)
**Show you've thought about volume production:**

**PCB DFM:**
- ✅ SMT components preferred (automated assembly)
- ✅ Standard PCB processes (no exotic materials/vias)
- ✅ Component orientation consistent (reduces pick-and-place errors)
- ✅ Test points accessible (automated testing)
- ✅ Fiducials for automated optical alignment

**Mechanical DFM:**
- ✅ Enclosure design for injection molding (draft angles, uniform wall thickness)
- ✅ Snap-fit assembly (no screws = faster assembly)
- ✅ Minimal hand assembly (only battery insertion, final QC)

**Component selection DFM:**
- ✅ Multi-source components where possible (reduces supply risk)
- ✅ Standard packages (0402/0603/0805 resistors, SOIC/QFN ICs)
- ✅ Automotive/industrial grade for critical parts (actuators, MCU)

#### 6. Manufacturing Plan
**Assembly process:**
1. **SMT assembly** (automated pick-and-place → reflow)
   - Stencil → paste → place → reflow → AOI (automated optical inspection)
   - Typical yield: 95-99% for simple boards
2. **Through-hole (if any)** (wave solder or hand assembly)
3. **Battery insertion** (manual or semi-automated)
4. **Enclosure assembly** (snap-fit or ultrasonic welding)
5. **Final test** (functional test, battery charge test, BLE pairing test)
6. **Packaging** (box, cable, manual)

**Contract manufacturer (CM) requirements:**
- SMT capability (pick-and-place, reflow oven, AOI)
- Volume capacity >10K units/year
- Quality certifications (ISO 9001, IPC-A-610)
- Lead time: 4-6 weeks from PO to delivery (after NPI)

**Test strategy:**
- **In-circuit test (ICT):** Bed-of-nails fixture tests PCB functionality
- **Functional test:** Custom test jig exercises all features
- **Battery test:** Charge/discharge cycle, capacity verification
- **BLE test:** Pairing with reference phone, range test

#### 7. Supply Chain & Sourcing
**Component sourcing:**
- **Tier 1 (critical):** MCU, actuators, BLE module
  - Multi-source where possible
  - Secure 6-month supply commitment
  - Alternates identified (second-source approved)
- **Tier 2 (important):** Power management ICs, connectors, batteries
  - Multi-source preferred
  - Standard parts from major distributors (Digikey, Mouser, Arrow)
- **Tier 3 (commodity):** Passives (resistors, capacitors, inductors)
  - High availability, many sources

**Lead time analysis:**
| Component | Lead Time | Risk | Mitigation |
|-----------|-----------|------|------------|
| MCU (STM32) | 12-16 weeks | MEDIUM | Order in Week 1, use dev board for early proto |
| Actuators (piezo/solenoid) | 8-12 weeks | HIGH | Sample evaluation Week 2-3, PO Week 4 |
| BLE module | 4-6 weeks | LOW | Standard module, many suppliers |
| PCB fabrication | 10-15 days | LOW | Use quick-turn vendor for prototypes |
| Batteries (Li-ion) | 6-8 weeks | MEDIUM | Standard cells available, custom pack if needed |

**Supply chain risks:**
- ❌ **Actuator single-source** → Mitigation: Evaluate 2-3 suppliers in v1.3.0, qualify alternates
- ❌ **MCU shortages (2025 market)** → Mitigation: Order long-lead in Week 1, use dev boards for prototyping
- ❌ **Battery compliance delays** → Mitigation: Use pre-certified cells, plan for UL/IEC testing post-pilot

#### 8. Risk Mitigation ⭐ CRITICAL

**Approach:** Lightweight risk analysis (what can fail, impact, mitigation) - NOT formal FMEA/DFMEA with RPN scoring (that's post-pilot).

**Why lightweight, not formal FMEA?**
- Formal DFMEA takes weeks (cross-functional team, detailed RPN calculations, documentation)
- 2-month timeline doesn't allow for formal FMEA process
- Pilot validation IS the risk mitigation (build 10-100 units, find issues before volume)
- Post-pilot: Use pilot learnings to inform formal DFMEA before mass production

**What to include in v1.5.0 risk analysis:**
- Identify top 5-10 risks (timeline, cost, technical, supply chain)
- Qualitative assessment (HIGH/MEDIUM/LOW probability and impact)
- Mitigation plan for each risk (what's plan B?)
- Show you've thought about failure modes (actuators fail, PCB shorts, battery issues)

**Timeline risks:**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Actuator lead time >8 weeks | HIGH | CRITICAL | Order samples Week 2, PO Week 4, expedite if needed |
| PCB layout takes >2 weeks | MEDIUM | HIGH | Use reference designs, parallel layout work |
| First prototypes don't work | MEDIUM | CRITICAL | Plan 2-week debug buffer (Week 7-8), use dev boards early |
| Pilot assembly issues | MEDIUM | MEDIUM | DFM review before PCB fab, dry-run assembly process |

**Cost risks:**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Actuator cost 2x estimate | MEDIUM | HIGH | Sensitivity analysis in v1.4.0 tested this scenario |
| NRE exceeds budget | LOW | MEDIUM | Detailed cost tracking, weekly reviews |
| Volume pricing not achieved | LOW | LOW | Negotiate volume commitments with CM |

**Technical risks:**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Actuator performance insufficient | MEDIUM | CRITICAL | Sample evaluation in Week 2-3, test before committing |
| Battery life <8 hours | MEDIUM | HIGH | Power budget analysis, conservative estimate, oversized battery if needed |
| BLE range/reliability issues | LOW | MEDIUM | Use certified module, antenna design review |
| EMI/EMC compliance failure | LOW | HIGH | Follow best practices, pre-compliance testing |

**Supply chain risks:** (see Section 7 above)

#### 9. Scale Strategy: Pilot → 1K → 10K+ Units
**Pilot (10-100 units, Month 2):**
- **Purpose:** Validate design, manufacturing, user acceptance
- **Assembly:** Manual/semi-automated (acceptable for low volume)
- **Lead time:** 2 months from concept to pilot units
- **Cost:** High NRE amortization ($500-1000/unit effective cost)

**Low-volume production (100-1K units, Months 3-6):**
- **Purpose:** Early customer deployments, field trials
- **Assembly:** CM with SMT automation, some manual steps
- **Lead time:** 4-6 weeks PO to delivery
- **Cost:** Moderate NRE amortization ($150-300/unit effective cost)
- **Changes from pilot:** Refine DFM based on pilot learnings, reduce rework

**Medium-volume (1K-10K units/year, Year 1-2):**
- **Purpose:** Market launch, ramp to volume
- **Assembly:** Fully automated SMT + final assembly
- **Lead time:** 6-8 weeks PO to delivery
- **Cost:** Approaching target BOM (<$60-80/unit with NRE spread)
- **Changes from low-volume:** Tooling for enclosure (injection molds), automated test fixtures

**High-volume (10K+ units/year, Year 2+):**
- **Purpose:** Scale to market demand
- **Assembly:** High-volume CM, multiple lines, optimized for throughput
- **Lead time:** 8-12 weeks PO to delivery (volume buffered inventory)
- **Cost:** Target BOM achieved (<$50/unit at 10K+ volume)
- **Changes from medium-volume:** Second-source components, regional CMs, supply chain optimization

**Scale investments:**
- **Pilot → 1K:** Minimal ($10K for assembly fixtures, test jigs)
- **1K → 10K:** Moderate ($50K for injection mold tooling, automated test equipment)
- **10K+ → 100K:** High ($200K+ for multi-cavity molds, regional CMs, inventory)

#### 10. Post-Pilot Activities (Out of Scope but Acknowledge)

**⚠️ IMPORTANT:** The `out_of_scope` section in `source/requirements.yaml` lists activities that are **deferred to post-pilot phases**, NOT ignored. Every out-of-scope item should be addressed in future work.

**After pilot validation (Month 3+):**
- ✅ **Compliance testing** (FCC/CE EMI/EMC, UL/IEC battery safety) → v1.5.0 identifies standards, post-pilot does certification
- ✅ **Field trials** (beta testing with 50-100 users) → Post-pilot user validation at scale
- ✅ **Formal FMEA/DFMEA** (Design Failure Mode and Effects Analysis with RPN scoring) → v1.5.0 does lightweight risk analysis, post-pilot does formal DFMEA
- ✅ **Manufacturing process optimization** (reduce cycle time, improve yield, process capability studies) → Post-pilot continuous improvement
- ✅ **Supply chain contracts** (volume pricing, lead time guarantees, multi-year agreements) → Post-pilot when volume is proven
- ✅ **Service/support infrastructure** (warranty, repair, spare parts logistics, RMA process) → Post-pilot when product scales
- ✅ **Regulatory compliance** (full certification testing, not just design awareness) → Post-pilot before mass production
- ✅ **IP strategy** (patent search, freedom-to-operate analysis, filing) → Post-pilot when design is frozen
- ✅ **Quality management system** (ISO 9001, manufacturing process controls, SPC) → Post-pilot when scaling to volume

**What v1.5.0 DOES include (in-scope for 2-month pilot):**
- ✅ **Lightweight risk analysis** (what can fail, what's the impact, what's the mitigation) → Part of Section 8 risk mitigation
- ✅ **Standards awareness** (identify FCC/CE/UL requirements, design to anticipate them) → Part of requirements (NFR-STD-001)
- ✅ **DFM considerations** (design for manufacturability, pilot validates assembly process) → Part of Section 5
- ✅ **Component sourcing** (identify suppliers, get quotes, order long-lead items) → Part of Section 7
- ✅ **Pilot validation plan** (what to test with 10-100 units) → Part of Section 4

**Key Distinction:**
- **In-scope:** Design awareness, lightweight risk analysis, pilot validation
- **Out-of-scope:** Full formal processes (FMEA, certification, ISO 9001, IP filing)

**Why this matters for the presentation:**
- Shows you understand the **complete** path to production (not just 2 months)
- Demonstrates **realistic scope** (you know what's achievable in 2 months vs what comes after)
- Proves **engineering maturity** (you think ahead, not just "build it and ship it")

**Example slide talking point:**
> "The 2-month timeline focuses on pilot production to validate the design. Post-pilot activities include formal FMEA, full compliance certification, and ISO 9001 quality systems. These are out of scope for the initial timeline but critical before mass production. We've designed with these requirements in mind to avoid rework later."

---

## Quality Checklist (Before Creating `docs/solution.md`)

- [ ] **Architecture selection justified** (data from v1.4.0 decision matrix)
- [ ] **Block diagram created** (`resources/diagrams/final-architecture.png`)
- [ ] **Preliminary schematics drafted** (power, MCU, I/O, comm)
- [ ] **2-month Gantt chart complete** (`resources/calculations/timeline-gantt.xlsx`)
  - [ ] All critical path items identified
  - [ ] Long-lead parts ordered early (Week 1-2)
  - [ ] Buffer time for debug/rework (Week 7-8)
- [ ] **Pilot strategy defined** (10-100 units, validation plan, success criteria)
- [ ] **DFM considerations documented** (PCB, mechanical, component selection)
- [ ] **Manufacturing plan outlined** (assembly process, test strategy, CM requirements)
- [ ] **Supply chain analyzed** (lead times, multi-sourcing, risk mitigation)
- [ ] **Risk register complete** (timeline, cost, technical, supply chain risks + mitigations)
- [ ] **Scale strategy defined** (pilot → 1K → 10K+ with investments needed)

---

## Example: 2-Month Gantt Chart (Week-by-Week)

```
Week 1: Requirements & Component Selection
├── [Day 1-2] Finalize requirements.yaml
├── [Day 3-4] MCU selection (order dev boards + long-lead samples)
├── [Day 4-5] Actuator evaluation (order samples from 2-3 suppliers)
└── Critical: Place PO for long-lead components (MCU, actuators)

Week 2: Architecture & Preliminary Design
├── [Day 1-2] Block diagram finalization
├── [Day 3-5] Preliminary schematics (power, MCU core)
└── Critical: Actuator samples arrive, begin testing

Week 3: Actuator Evaluation & Schematic Detail
├── [Day 1-3] Actuator sample testing (force, power, reliability)
├── [Day 4-5] Finalize actuator selection, place production PO
└── Critical: Complete detailed schematics (power, MCU, I/O, comm)

Week 4: PCB Layout & BOM Finalization
├── [Day 1-3] PCB layout (4-layer board, SMT components)
├── [Day 4-5] BOM finalization, supplier quotes
└── Critical: Send Gerbers to PCB fab (10-15 day turnaround)

Week 5: Component Procurement & PCB Fabrication
├── [Day 1-5] Await PCB fab completion, component procurement
└── Critical: Monitor PCB fab progress, expedite if needed

Week 6: PCB Arrival & Assembly Prep
├── [Day 1-2] PCB boards arrive, inspection
├── [Day 3-5] First 5 boards assembled (hand assembly or CM quick-turn)
└── Critical: Bring-up testing, debug

Week 7: Prototype Debug & Pilot Prep
├── [Day 1-3] Debug first prototypes, fix critical issues (rework if needed)
├── [Day 4-5] Pilot assembly planning (CM coordination, test fixtures)
└── Critical: Prototype validation complete

Week 8: Pilot Production (10-100 Units)
├── [Day 1-3] Pilot assembly (10-100 units at CM)
├── [Day 4-5] Functional testing, yield analysis, user testing
└── Deliverable: Pilot units validated, design frozen
```

---

## Presentation Slides (from `docs/solution.md`)

**Slide 20: Selected Architecture**
- Block diagram
- Key components table
- Justification: "Architecture C scored 8.2/10 (vs 7.1 and 6.8) based on..."

**Slide 21: 2-Month Timeline**
- Gantt chart (simplified for slide)
- Critical path highlighted (actuators, PCB fab)
- Week 8: Pilot production complete

**Slide 22: Pilot Production Strategy**
- 10-100 units, validation plan
- Success criteria: >90% yield, user feedback positive
- Purpose: Validate design before volume commitment

**Slide 23: Risk Mitigation & Scale Plan**
- Top 3-5 risks + mitigations
- Scale path: Pilot → 1K → 10K+ units
- Investments needed at each stage

---

## Common Mistakes to Avoid

❌ **Don't:**
- Skip the Gantt chart (LAM explicitly asks for "process" = timeline)
- Assume everything works first time (plan for debug/rework buffer)
- Ignore long-lead components (actuators, MCU - order early!)
- Forget pilot validation (purpose of pilot = find issues BEFORE volume)
- Be vague on DFM (show you understand SMT, injection molding, test strategy)

✅ **Do:**
- Show week-by-week timeline with critical path
- Identify risks and show mitigation plans
- Explain pilot purpose (validate, verify, identify failures)
- Show scale path (pilot → volume with realistic transitions)
- Demonstrate DFM thinking (SMT, multi-source, test strategy)

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-08 | Spencer Barrett | Initial production plan guide for v1.5.0 |
