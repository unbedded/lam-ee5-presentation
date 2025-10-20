# Presentation Practice Guide
**Lam Research EE5 Interview - Oct 21, 2025**

**Target Time:** 27-30 minutes (leave 10-15 min for Q&A)
**Total Slides:** 34 slides
**Average Pace:** ~53 seconds/slide (but variable by section)

---

## 🎯 Practice Session Checklist

### Before Each Run:
- [ ] Open `artifacts/presentation-marp.html` in browser
- [ ] Enable presenter mode (if available)
- [ ] Have timer/stopwatch ready
- [ ] Water nearby
- [ ] Practice standing (if presenting in-person)

### After Each Run:
- [ ] Note actual time per section
- [ ] Identify slides where you stumbled
- [ ] Mark transitions that felt awkward
- [ ] Rate confidence 1-10 for each section

---

## ⏱️ Timing Targets by Section

### SECTION 1: Introduction (Slides 1-5)
**Target:** 1-2 minutes | **Pace:** Fast intro, establish credibility

| Slide | Content | Time | Key Point |
|-------|---------|------|-----------|
| 1 | Title | 10s | Project, name, date |
| 2 | Agenda | 15s | "Five sections, 30 min" |
| 3 | Who Am I | 30s | Embedded systems, medical, military |
| 4 | What You'll See | 30s | "Honest engineering, not marketing" |
| 5 | Approach | 30s | "Deep research, assumptions transparent" |

**CHECKPOINT 1:** Should be at ~2:00 by Slide 6

---

### SECTION 2: Requirements (Slides 6-11)
**Target:** 6-8 minutes | **Pace:** Moderate - this establishes your credibility

| Slide | Content | Time | Key Point |
|-------|---------|------|-----------|
| 6 | Requirements Overview | 45s | 17 requirements, 3 sources |
| 7 | Requirements Process | 60s | YAML SSOT, policy compliance |
| 8 | Ground Truth | 75s | Braille spacing constraint (critical!) |
| 9 | Derived Requirements | 75s | Size ≤2.3mm, UL/FCC, ADA |
| 10 | Assumptions Made | 90s | 6 assumptions, risk-ranked |
| 11 | Requirements Takeaways | 45s | "Defensible, auditable, traceable" |

**CHECKPOINT 2:** Should be at ~8:00 by Slide 12

**Critical Talking Points:**
- "2.3mm diameter constraint came from 2.5mm braille pitch minus 1.5mm dot diameter"
- "6 assumptions explicitly risk-ranked - high risk items flagged for validation"
- "93% SMART compliance per audit"

---

### SECTION 3: Alternative Architectures (Slides 12-20)
**Target:** 10-12 minutes | **Pace:** Moderate, technical depth here

| Slide | Content | Time | Key Point |
|-------|---------|------|-----------|
| 12 | Architecture Overview | 45s | 3 architectures, decision tree |
| 13 | ARCH_SOL_ECO | 75s | "$506, 12 weeks, excellent mfg" |
| 14 | SOL_ECO Subsystems | 75s | Olimex driver, cost breakdown |
| 15 | ARCH_PIEZO_ECO | 75s | "$592, 12 weeks, most robust" |
| 16 | PIEZO_ECO Subsystems | 75s | DRV2667, cost breakdown |
| 17 | ARCH_PIEZO_DLX | 75s | "$606, BLE, wireless premium" |
| 18 | PIEZO_DLX Subsystems | 75s | nRF52840, cost breakdown |
| 19 | Decision Tree | 60s | "No single best - depends on constraints" |
| 20 | Architecture Takeaways | 45s | "SOL cheapest, PIEZO most robust" |

**CHECKPOINT 3:** Should be at ~18:00 by Slide 21

**Critical Talking Points:**
- "SOL wins on cost and manufacturability - $86 cheaper than PIEZO"
- "PIEZO wins on robustness and EMI margin - 20dB vs 15dB"
- "All three architectures meet <8 week pilot timeline"
- Point to spider chart: "Visual shows no clear winner"

---

### SECTION 4: Trade-off Analysis (Slides 21-27)
**Target:** 4-5 minutes | **Pace:** Faster - data speaks for itself

| Slide | Content | Time | Key Point |
|-------|---------|------|-----------|
| 21 | Trade-offs Overview | 30s | "7 dimensions evaluated" |
| 22 | Cost Analysis | 50s | SOL $506, PIEZO_ECO $592, PIEZO_DLX $606 |
| 23 | Timeline Analysis | 40s | All 8 weeks (actuator sourcing drives) |
| 24 | Risk Analysis | 50s | SOL supply risk, PIEZO robust, DLX wireless |
| 25 | UX/Performance | 40s | SOL/PIEZO fair, DLX good BLE UX |
| 26 | Power/EMI | 50s | SOL 0.63W/15dB, PIEZO 0.86W/20dB |
| 27 | Trade-off Takeaways | 30s | "Constraint-driven, not opinion-driven" |

**CHECKPOINT 4:** Should be at ~23:00 by Slide 28

**Critical Talking Points:**
- "Cost differs by only $100 - NOT the deciding factor"
- "Timeline identical - all 8 weeks due to actuator sourcing"
- "Real differentiator: robustness vs manufacturability"

---

### SECTION 5: Path to Pilot (Slides 28-33)
**Target:** 5-6 minutes | **Pace:** Moderate, forward-looking

| Slide | Content | Time | Key Point |
|-------|---------|------|-----------|
| 28 | Pilot Overview | 45s | 8 weeks, $20K NRE, 6 units |
| 29 | Phase 1: Design | 50s | Weeks 1-2, schematics/PCB |
| 30 | Phase 2: Procurement | 50s | Weeks 3-5, long-lead actuators |
| 31 | Phase 3: Assembly | 50s | Weeks 6-7, bring-up/validation |
| 32 | Phase 4: User Testing | 50s | Week 8, accessibility users |
| 33 | Success Criteria | 60s | Force, refresh, MTBF targets |

**CHECKPOINT 5:** Should be at ~28:00 by Slide 34

**Critical Talking Points:**
- "Actuator sourcing is critical path - 3-4 weeks"
- "Success criteria measurable: 30N force, 1Hz refresh, 10K cycles"
- "$20K NRE covers 6 pilot units + tooling"

---

### SECTION 6: Closing (Slide 34)
**Target:** 1-2 minutes

| Slide | Content | Time | Key Point |
|-------|---------|------|-----------|
| 34 | Summary + Q&A | 60-90s | Recap 3 architectures, decision tree, open Q&A |

**FINAL TIME:** Should be at 27-30 minutes

---

## 🎤 Delivery Best Practices

### Energy & Pacing
- **Start strong:** First 2 minutes set the tone - confident, clear
- **Vary pace:** Slow down for critical points (braille constraint, decision tree)
- **Pause for impact:** After takeaway slides, let it sink in (2-3 sec)
- **Don't rush:** If you hit 30 min, that's fine - better than racing through

### Transitions to Practice
1. **Section 1 → Section 2:** "Now that you know my approach, let's dive into requirements - the foundation of everything."
2. **Section 2 → Section 3:** "With 17 requirements defined, I explored 3 alternative architectures."
3. **Section 3 → Section 4:** "Three viable options - how do we choose? Trade-off analysis."
4. **Section 4 → Section 5:** "Recommendation: SOL_ECO for pilot. Here's the execution plan."
5. **Section 5 → Section 6:** "That's the path to pilot in 8 weeks. Questions?"

### Body Language (In-Person)
- Stand, don't sit (if possible)
- Face the panel, not the screen
- Use hand gestures for emphasis (spider chart, decision tree)
- Make eye contact with all interviewers

### Voice
- Project clearly (they need to hear you)
- Vary tone to avoid monotone
- Emphasize key numbers: "$506", "2.3mm", "8 weeks"
- Pause before/after TAKEAWAY slides

---

## 🚨 Common Pitfalls to Avoid

1. **Getting stuck on one slide:** If you blank, read the TAKEAWAY and move on
2. **Going too deep on backup slides:** Resist urge to explain everything - save for Q&A
3. **Apologizing:** Don't say "this slide is busy" or "sorry for the detail" - own it
4. **Rushing the requirements:** This is where you prove rigor - don't skip
5. **Missing time checkpoints:** Glance at timer at each checkpoint - adjust pace

---

## 📊 Self-Assessment Rubric

After each practice run, rate yourself 1-10:

| Criteria | Run 1 | Run 2 | Run 3 | Target |
|----------|-------|-------|-------|--------|
| Timing (27-30 min) | | | | 9+ |
| Confidence (no stumbling) | | | | 8+ |
| Energy (not monotone) | | | | 8+ |
| Transitions (smooth) | | | | 7+ |
| Key points hit | | | | 9+ |
| Stayed on slide (no wandering) | | | | 8+ |

**Goal:** All 8+ by final practice run

---

## 🎯 Priority Practice Areas

Based on complexity and rubric weight:

### HIGH PRIORITY (Practice 3+ times)
1. **Slide 8-9:** Requirements ground truth + derived (establishes credibility)
2. **Slide 19:** Decision tree explanation (critical to trade-off story)
3. **Slide 22-24:** Cost/timeline/risk (30% of rubric - must be crisp)
4. **Slide 34:** Summary + Q&A transition (last impression)

### MEDIUM PRIORITY (Practice 2 times)
1. **Slide 13-18:** Architecture subsystems (technical depth)
2. **Slide 28-33:** Pilot execution (20% of rubric)

### LOW PRIORITY (Practice 1 time)
1. **Slide 1-5:** Intro (straightforward)
2. **Slide 6-7:** Requirements overview (setup, not critical)
3. **Slide 20, 27:** Takeaways (just read them)

---

## 📝 Practice Schedule Recommendation

**Oct 18 (Today):**
- [ ] Run 1: Full timed run, note rough spots
- [ ] Run 2: Focus on HIGH PRIORITY sections
- [ ] Review: What slides caused stumbles?

**Oct 19 (Sunday):**
- [ ] Run 3: Full timed run, aim for 27-30 min
- [ ] Run 4: Practice Q&A scenarios (see below)
- [ ] Review: Are you hitting checkpoints?

**Oct 20 (Monday):**
- [ ] Run 5: Final dress rehearsal, full presentation
- [ ] Generate PDF and email to Nathan Briggs (EOD)
- [ ] Light review (don't over-practice)

**Oct 21 (Interview Day):**
- [ ] Light review of TAKEAWAY slides only
- [ ] Don't practice full run (you'll be tired)
- [ ] Trust your preparation

---

## ❓ Anticipated Q&A Topics

Have 30-second answers ready:

### Technical Deep-Dives
- **"Why did you choose SOL_ECO over PIEZO_ECO?"**
  - "Cost-constrained pilot, excellent manufacturability, acceptable robustness. PIEZO is plan B if vibration becomes issue."

- **"What's your biggest technical risk?"**
  - "Actuator sourcing - 3-4 week lead time. Mitigation: order immediately upon approval, have backup supplier."

- **"How did you validate the 2.3mm size constraint?"**
  - "Derived from Braille Authority standards: 2.5mm pitch - 1.5mm dot diameter. Cited in requirements.yaml."

### Process Questions
- **"How would you handle requirement changes mid-pilot?"**
  - "Requirements.yaml is SSOT - change there, regenerate docs, assess impact on timeline/cost."

- **"What if user testing fails?"**
  - "Success criteria defined (30N force, 1Hz refresh). If fail, debug root cause - likely actuator performance or control timing."

### Scope Questions
- **"Why only 6 pilot units?"**
  - "Minimum for validation: 2 for durability testing, 2 for user testing, 2 for backup. Scales to 100+ in production phase."

- **"What about wireless charging?"**
  - "Out of scope for 8-week pilot. PIEZO_DLX architecture includes BLE for future wireless features."

### Meta Questions
- **"What would you do differently?"**
  - "More supplier outreach earlier - actuator sourcing is critical path. Also, earlier stakeholder review of assumptions."

- **"How does this compare to your past projects?"**
  - "Similar to [medical device project] - constrained timeline, regulatory considerations, user-centered validation."

---

## ✅ Final Checks Before Interview

**Day Before (Oct 20):**
- [ ] Presentation HTML loads in browser
- [ ] All images display correctly
- [ ] Presenter notes visible (if using presenter mode)
- [ ] PDF generated and emailed to Nathan Briggs
- [ ] Backup copy on USB drive (if presenting in-person)
- [ ] Know how to advance slides (keyboard/clicker)

**Interview Day (Oct 21):**
- [ ] Arrive 10 min early
- [ ] Test A/V setup (HDMI, screen mirroring)
- [ ] Confirm you can see timer/clock
- [ ] Deep breath, you've got this

---

## 🏆 You're Ready When...

- You can hit 27-30 min consistently (±2 min)
- You can explain the 2.3mm constraint without notes
- You can draw the decision tree from memory
- You can answer "why SOL_ECO?" in 30 seconds
- You feel confident, not nervous

**Remember:** This presentation shows depth, rigor, and honest engineering. You've done the work. Now just deliver it clearly.

---

Good luck! 🚀
