# Interview Prep Checklist

**Interview Date:** LAM Research EE5 Position (October 21, 2025)
**Presentation:** 30 minutes, Braille Display Concept Evaluation
**Location:** LAM Research, Tualatin, OR

**CRITICAL:** This checklist consolidates all presentation prep guidance:
- Q&A anticipated questions with prepared answers
- Key messages to memorize (systems engineering philosophy)
- Timing strategy and rubric alignment
- Practice workflow and success criteria
- Technical guide: How to use speaker notes in PowerPoint

---

## Q&A Prep - Anticipated Questions

### 1. Why can't you find COTS actuators?
**Answer:** "2.5mm pitch is non-standard, most displays use 200V custom piezos. The industry has standardized on custom piezoelectric actuators with 8-12 week lead times. Our challenge is meeting the 2-month timeline requirement."

### 2. What if timeline extends to 4 months?
**Answer:** "Opens door to custom actuator standard lead time, better cost optimization. We could negotiate better volume pricing and explore additional mechanical designs that leverage longer development cycles."

### 3. Which architecture would YOU pick?
**Answer:** "ARCH_PIEZO_ECO is most robust across scenarios, but it depends on the wireless requirement. If wireless is mandatory, PIEZO_DLX is the only option. If cost is the primary driver, SOL_ECO wins. This is exactly why I built a portfolio approach - there's no universal 'best', only 'best for YOUR constraints'."

### 4. Can you hit $200 BOM?
**Answer:** "Not with pilot quantities and COTS components. We need volume negotiation (10K+ units) or custom actuator design to hit that target. Current BOMs are $505-$605 for pilot quantities. Path to $200: (1) Volume pricing at 10K units, (2) Reduce from 32 to 24 cells (25% savings), (3) Value engineering (2-layer PCB, lower-cost MCU)."

### 5. Power supply design for 200V piezo?
**Answer:** "DC-DC boost converter from 5V USB to 100-200V. Key challenges: EMI mitigation (30mm cantilever acts as λ/4 antenna @ 1.67 GHz), efficiency (target >85%), and isolation. See EMI slides for detailed mitigation strategy - firmware alone gives us 68 dB reduction at $0 cost."

### Deep Technical Backup
- **EMI Physics:** 30mm piezo cantilever = λ/4 monopole antenna @ 1.67 GHz → 192 radiating antennas
- **Cost Sensitivity:** Actuators are 55-65% of BOM ($326-$384 for 192 pins)
- **Timeline Reality:** ALL architectures violate 2-month timeline due to custom actuator lead time (12 weeks)
- **Risk Mitigation:** $50K NRE budget allocated for custom actuator quickturn (90% success rate, 2-4 weeks)

---

## Timing Targets (30-Minute Presentation)

| Section | Slides | Time | Avg/Slide | Notes |
|---------|--------|------|-----------|-------|
| Intro + Agenda | 2 | 2 min | 60s | Set expectations |
| Problem Statement | 1 | 2 min | 120s ⚠️ | CRITICAL - spend time here |
| Market Context | 2 | 2 min | 60s | Establish credibility |
| Requirements | 4 | 4 min | 60s | Show rigor |
| Architectures | 4 | 4 min | 60s | Clear comparisons |
| **Evaluation** | 7 | **8 min** | 69s | **← HIGHEST RUBRIC WEIGHT (30%)** |
| Production | 4 | 4 min | 60s | Path to volume |
| Summary + Q&A | 2 | 2 min | 60s | Recap + invite questions |
| **TOTAL** | **29** | **28 min** | **58s/slide** | **2-min buffer** |

**Key Timing Notes:**
- **Problem Statement (120s):** Spend double time here - sets up entire conversation
- **Evaluation Section (8 min):** Highest rubric weight (30 points) - don't rush trade-off analysis
- **Buffer (2 min):** For interruptions, questions, transitions
- **If running long:** Cut Market Gap Analysis slide (covered in other slides)
- **If running short:** Expand on EMI physics or actuator sourcing strategy

---

## Success Criteria

### Content Mastery
- ✅ Can explain 3 architectures WITHOUT looking at slides
- ✅ Can answer "Which architecture would YOU pick?" (answer: it depends!)
- ✅ Can explain GHz antenna physics (30mm = λ/4 @ 1.67 GHz)
- ✅ Can list 3 critical risks (actuator sourcing, EMI cert, timeline)
- ✅ Can state BOM costs from memory ($505.71, $591.99, $605.67)
- ✅ Can explain trade-off framework (wireless → PIEZO_DLX, cost → SOL_ECO, speed → PIEZO_ECO)

### Delivery
- ✅ Maintain 60s/slide pace (28-32 minutes total)
- ✅ Hit 5 key messages:
  - (1) **Problem Statement:** "7 of 10 requirements vague - need YOUR feedback"
  - (2) **Market Context:** "$0.83-$1.06/pin is market floor - our $1.04/pin is competitive"
  - (3) **EMI Physics:** "30mm cantilever = λ/4 antenna @ 1.67 GHz (senior EE differentiator)"
  - (4) **Decision Framework:** "No 'best' architecture - depends on YOUR priorities"
  - (5) **Risk Honesty:** "Actuator sourcing is MAKE-OR-BREAK, $50K NRE allocated"
- ✅ Use notes as PROMPTS, not script (glance for transitions)
- ✅ Navigate smoothly to backup content for technical deep-dives

### Backup Preparedness
- ✅ Printed speaker notes in binder (paper backup)
- ✅ Presentation files on USB drive (tech backup)
- ✅ Can deliver WITHOUT slides (elevator pitch version - see below)
- ✅ Can answer technical questions with backup calculations (BOM, power, EMI)

---

## Elevator Pitch Versions (If Slides Fail)

### 30-Second Problem Statement
"32-character braille display, 2-month timeline, COTS component mandate, $200 BOM target. Challenge: NO COTS actuators exist at 2.5mm pitch. Industry uses custom piezo with 8-12 week lead time. All architectures violate the 2-month timeline - this is about honest engineering and trade-off navigation."

### 15-Second Architecture Summary
"Three architectures: PIEZO_ECO (fastest to market, standard approach), SOL_ECO (cheapest via mechanical innovation), PIEZO_DLX (best UX with wireless). Each optimizes different constraints."

### 20-Second Decision Framework
"No universal 'best' architecture - depends on your priorities. Wireless requirement? PIEZO_DLX only option. Cost under $300? SOL_ECO wins. Timeline critical? PIEZO_ECO fastest. Give me your constraints, I'll tell you which architecture wins."

### 10-Second Critical Risk
"Actuator sourcing is the critical path. No COTS solution exists. $50K NRE budget allocated for custom quickturn. Decision point: end of Week 2."

### 30-Second "Why Hire Me" Answer
"I don't sell perfect solutions - I navigate trade-offs, manage risks, and provide decision frameworks. I understood GHz EMI physics, caught the actuator sourcing gap early, and built a portfolio approach because requirements were vague. That's senior EE systems thinking, not junior component design."

---

## Key Numbers to Memorize

**System Specs:**
- **32 characters × 6 dots = 192 pins** (not 8 dots - we use Grade 1 braille)
- **$200 ± $100 BOM target** = $100-$300 range ($1.04/pin competitive with budget segment)
- **2-month timeline = COTS mandate** (≤4 week component lead time)
- **10K units/month production** (SMT assembly at volume)

**Market Context:**
- **100% of commercial displays use custom piezo** (8-12 week lead time, proprietary)
- **Budget segment:** $0.83-$1.06/pin (Orbit Reader 20/40)
- **Mid-range:** $1.77-$2.50/pin (Brailliant, Focus)
- **Premium:** $2.08+/pin (Mantis, Graphiti)

**BOM Costs (Pilot Quantities):**
- **ARCH_SOL_ECO:** $505.71 (lowest cost, $1.70/actuator)
- **ARCH_PIEZO_ECO:** $591.99 (standard approach, $2.00/actuator)
- **ARCH_PIEZO_DLX:** $605.67 (wireless premium, $2.00/actuator)

**EMI Physics (Senior EE Differentiator):**
- **30mm piezo cantilever = λ/4 monopole antenna @ 1.67 GHz**
- **192 radiating antennas** (one per pin)
- **68 dB EMI reduction from firmware alone** ($0 hardware cost)
- **Total mitigation: 133 dB** → 21 dB compliance margin

**Risk Mitigation:**
- **$50K NRE budget** for custom actuator quickturn (90% success, 2-4 weeks)
- **Decision point:** End of Week 2 (actuator sourcing resolution)
- **Timeline impact:** +0 to +8 weeks depending on actuator path

**ADA 703.3 Mechanical Requirements:**
- **Dot diameter:** 1.5-1.6 mm
- **Dot height:** 0.64-0.94 mm (raised position)
- **Dot spacing:** 2.3-2.5 mm (drives actuator size constraint)
- **Cell spacing:** 6.1-7.6 mm (horizontal between characters)
- **Holding force:** 50-100 grams (tactile feedback)

---

## 🎯 KEY MESSAGES TO MEMORIZE (Systems Engineering Philosophy)

### Primary Thesis: Trade-offs Over Perfection

**Core Message (60-Second Version):**

> "One key insight from this project: As a systems engineer, I don't optimize individual components—I optimize the **system** for **value**.
>
> For example, the PDF says 'low cost portable device.' A junior engineer designs one solution at $200 BOM. I designed **three architectures** at $505, $591, and $605 BOM, because the requirement exists in a **range**, not a point.
>
> The SOL_ECO option ($505.71) came from asking: 'Can mechanical innovation enable cheaper actuators?' Challenging that assumption saved 15% on actuator costs through lever mechanisms.
>
> This is systems engineering: **Trade-offs over perfection. Innovation through simplification. Value over specs.**"

### Supporting Examples

**Example 1: Cost Range, Not Point Design**
- Wrong approach (junior engineer): "The requirement is $200 BOM. I designed to $200."
- Right approach (systems engineer): "The requirement is 'low cost' (vague). I assumed $200 ±$100 BOM range. I designed 3 architectures showing cost/UX/simplicity trade-offs. Customer picks based on their priorities."

**Example 2: Innovation = Mechanical Simplification (SOL_ECO)**
- Wrong approach: "Piezo actuators are industry standard. Use them."
- Right approach: "Piezo costs $2.00/actuator. Can we use cheaper solenoids ($1.70) with mechanical levers to achieve same 2.5mm pitch? Yes - SOL_ECO saves 15% on actuators through mechanical innovation."

**Example 3: Reliability Through Simplification**
- Quote: "The most reliable component is the one you don't include."
- Example: USB-C wired option eliminates battery subsystem (15+ components, 5+ failure modes) → 1 component, 1 failure mode
- Result: 15× fewer components = 15× lower failure risk

**Example 4: Senior EE Differentiator - GHz Antenna Physics**
- Junior engineer: "200V piezo needs EMI filtering"
- Senior engineer: "30mm cantilever = λ/4 monopole antenna @ 1.67 GHz → 192 radiating antennas at FCC Part 15B worst band. Firmware sequential firing gives 68 dB reduction at $0 cost. This is antenna physics, not just 'add ferrite beads'."

### Where This Fits in Rubric

**This philosophy directly addresses:**
- **Alternative Solutions (25 pts):** Multiple distinct solutions considered, design methodology explained
- **Trade-offs Analysis (30 pts):** Clear analysis of pros/cons, quantitative comparison
- **Path to Production (20 pts):** Cost/complexity considerations, risk mitigation
- **Presentation Quality (10 pts):** Systems thinking demonstration

**This message is worth ~20-25% of your rubric score!**

### Competitive Differentiation

What other candidates might say:
- "I designed a braille display with BLE and a battery."
- "Here's my power supply schematic with low-noise LDO."

What YOU say (with this message):
- "I designed **three architectures** balancing cost, innovation, and UX."
- "The SOL_ECO option uses mechanical levers to enable 15% actuator cost savings."
- "I optimized **system value**, not individual components - that's senior EE systems thinking."

---

## Practice Workflow (Days Before Interview)

### Days 5-4: Content Mastery
- ✅ Review speaker notes for all slides (especially Q&A prep)
- ✅ Practice in presenter view (if using live slides)
- ✅ Time each section (aim for ~60 sec/slide, 120s for Problem Statement)
- ✅ Memorize 5 key messages (see Success Criteria above)
- ✅ Memorize key numbers (BOM costs, EMI physics, market $/pin)

### Days 3-2: Delivery Practice
- ✅ Full run-through WITHOUT looking at notes (test internalization)
- ✅ Record yourself (audio/video) - identify weak spots:
  - Are you spending enough time on Problem Statement? (should be 120s, not 60s)
  - Are you rushing through Evaluation section? (highest rubric weight - 8 min)
  - Are you hitting all 5 key messages?
- ✅ Practice Q&A with anticipated questions (see Q&A Prep above)
- ✅ Practice elevator pitches (30s problem, 15s architectures, 20s decision framework)

### Day 1: Final Prep
- ✅ Final run-through with notes (smooth delivery, timing check)
- ✅ Print backup: Speaker notes (2 pages/sheet, landscape, grayscale)
- ✅ Triple backup: USB drive + laptop + email files to yourself
- ✅ Review this checklist one more time

### Interview Day: Execution Checklist
- ✅ Arrive 15 minutes early (tech setup buffer)
- ✅ Load presentation on interview computer (test before they arrive)
- ✅ Printed notes nearby (don't rely on tech alone)
- ✅ Glance at notes for transitions, NOT full reading
- ✅ Hit your timing targets (glance at watch at 10-min, 20-min marks)
- ✅ Be ready to navigate to backup slides for deep technical questions

---

## 3-2-1 Backup Strategy (Triple Redundancy)

**3 Copies of presentation:**
1. **Laptop:** `/home/preact/sw/job/lam/ee/artifacts/presentation-marp.html`
2. **USB Drive:** `presentation-marp.html` + images folder (copy entire artifacts/ dir)
3. **Cloud:** Email HTML to yourself OR upload to Google Drive

**2 Formats:**
1. **HTML** (primary - for presenting in browser)
2. **PDF** (backup - for sharing if browser unavailable)

**1 Offsite:**
- Email both HTML + PDF to yourself (access from anywhere)
- Or upload to cloud storage (Google Drive, Dropbox)

**Interview Day File Access:**

**Option 1: Present from Laptop (RECOMMENDED)**
```bash
firefox /home/preact/sw/job/lam/ee/artifacts/presentation-marp.html
# Press F11 for fullscreen
# Press P for Presenter Mode (notes + timer)
```

**Option 2: Present from USB Drive**
1. Before interview: Copy `artifacts/presentation-marp.html` to USB
2. Also copy `artifacts/images/` folder to USB (presentation needs images)
3. At interview: Open HTML from USB in any browser
4. Fallback: If images don't load, use PDF instead

**Option 3: Present from Cloud (Emergency Backup)**
1. Upload `artifacts/presentation-marp.html` to Google Drive (before interview)
2. Share link (view-only)
3. At interview: Open link in browser if laptop/USB fail

**Physical Backup (If Tech Fails):**
- Printed speaker notes (from this checklist - 16 pages)
- Printed PDF slides (2 pages/sheet, landscape)
- Can present from paper notes if all tech fails

---

## Rubric Alignment (100 Points Total)

| Criterion | Weight | Slides | Strategy |
|-----------|--------|--------|----------|
| **Trade-off Analysis** | 30 pts | Decision Framework, Actuator Sourcing | Spend 8 min here - highest value |
| **Requirements** | 25 pts | Problem Statement, Tech Req Database | Show SMART rigor, document assumptions |
| **Alternative Solutions** | 25 pts | 3 Architectures, Evaluation Framework | Clear differentiation, BOM details |
| **Path to Production** | 20 pts | 8-12 Week Timeline, Risk Mitigation | Honest about challenges, show planning |
| **Presentation Quality** | 10 pts | Slides, delivery, Q&A | Maintain pace, hit key messages |

**Optimization Strategy:**
- **If time is tight:** Prioritize Trade-off Analysis (30%) and Requirements (25%)
- **If running long:** Cut Market Gap Analysis (content covered elsewhere)
- **If running short:** Expand EMI physics deep-dive (shows senior EE thinking)

---

## Final Confidence Check

**Before presenting, ask yourself:**

1. **Can I explain the problem in 30 seconds?** ✅
   → "32-char braille display, 2-month timeline, COTS mandate, $200 BOM target - NO COTS actuators exist"

2. **Can I name 3 architectures in 15 seconds?** ✅
   → "PIEZO_ECO (fast), SOL_ECO (cheap via mechanical innovation), PIEZO_DLX (wireless)"

3. **Can I explain decision framework in 20 seconds?** ✅
   → "No universal 'best' - depends on YOUR priorities: wireless? cost? timeline? volume?"

4. **Can I state THE critical risk in 10 seconds?** ✅
   → "Actuator sourcing - no COTS solution exists, $50K NRE mitigation budget allocated"

5. **Can I answer "Why should we hire YOU?" in 30 seconds?** ✅
   → "I don't sell perfect solutions - I navigate trade-offs, manage risks, and provide decision frameworks. I understood GHz EMI physics, caught the actuator sourcing gap, and built a portfolio approach because requirements were vague. That's senior EE thinking."

---

## YOU'RE READY!

✅ **Presentation is polished** - clear slides, speaker notes on every slide
✅ **Q&A prep is done** - 5 anticipated questions with prepared answers
✅ **Timing is planned** - 28 min presentation + 2 min buffer
✅ **Key messages identified** - 5 critical talking points memorized
✅ **Backup plans in place** - printed notes, USB drive, elevator pitches
✅ **Rubric alignment verified** - prioritizing high-value sections

**Your Edge:**
- Senior EE thinking (GHz antenna physics understanding)
- Honest engineering (transparent about challenges and assumptions)
- Systems approach (portfolio of architectures, not "one perfect solution")
- Risk management (identified actuator sourcing gap, allocated $50K NRE)
- Decision frameworks (customer-centric, constraint-driven selection)

**Good luck!** 🚀

---

# APPENDIX: Technical Guide - Using Speaker Notes

## How to View Speaker Notes in Marp HTML Presentation

### Current Setup (Marp HTML)

Your presentation is built with Marp (Markdown to HTML), not PowerPoint. Speaker notes are embedded in HTML comments.

**File locations:**
- **Source:** `source/presentation-marp.md`
- **Generated:** `artifacts/presentation-marp.html` (1-second regeneration with `make marp`)
- **Backup PDF:** `artifacts/presentation-marp.pdf`

**Speaker notes format in Markdown:**
```markdown
# Slide Title

Slide content here...

<!-- Speaker notes: Your talking points here. Can include timing reminders,
key numbers, Q&A anticipation, strategic framing. -->
```

### How to Present with Speaker Notes (Marp HTML)

**Option 1: Browser Presenter Mode (RECOMMENDED)**

1. Open `artifacts/presentation-marp.html` in Firefox/Chrome
2. Press `P` key to enter **Presenter Mode**
3. You'll see:
   - **Main display:** Current slide (audience view)
   - **Presenter window:** Current slide + next slide preview + speaker notes + timer

**Option 2: Dual Monitor Setup**

1. Connect laptop to projector/second display
2. Set display mode to **Extend** (not Mirror)
3. Open `artifacts/presentation-marp.html` in browser
4. Press `P` for Presenter Mode
5. Drag presenter window to laptop screen
6. Fullscreen audience view on projector

**Option 3: Print Speaker Notes**

```bash
# Open presentation in browser
firefox artifacts/presentation-marp.html

# Print with speaker notes:
# 1. Right-click → "View Page Source" (Ctrl+U)
# 2. Search for "<!-- Speaker notes:"
# 3. Copy all notes to text file for printing
```

## Marp Keyboard Shortcuts

During presentation (`artifacts/presentation-marp.html` in browser):

- **Arrow keys / Space:** Next/previous slide
- **P:** Toggle Presenter Mode
- **F:** Toggle fullscreen
- **Home:** First slide
- **End:** Last slide
- **Number + Enter:** Jump to slide number
- **Esc:** Exit fullscreen

## Best Practices for Using Speaker Notes

### DO:
- ✅ **Use notes for timing reminders** ("2 minutes on this slide")
- ✅ **Include Q&A anticipation** ("If asked about X, mention Y")
- ✅ **Write key numbers** ("32 chars × 6 dots = 192 pins")
- ✅ **Add strategic framing** ("This is the senior EE differentiator")
- ✅ **Practice with Presenter Mode** multiple times before interview

### DON'T:
- ❌ **Read notes verbatim** - use as prompts, not script
- ❌ **Put slide content in notes** - notes should ADD context, not repeat
- ❌ **Make notes too long** - 3-5 sentences max per slide
- ❌ **Rely on notes during presentation** - internalize key messages

## Printing Speaker Notes Backup

**Option A: Screenshot Presenter Mode**
1. Open `artifacts/presentation-marp.html` in browser
2. Press `P` for Presenter Mode
3. Screenshot presenter window (shows notes)
4. Repeat for critical slides (Problem Statement, Decision Framework, Q&A)

**Option B: View HTML Source**
```bash
# View all speaker notes in terminal
grep -A 5 "<!-- Speaker notes:" source/presentation-marp.md
```

## Technical Details: How It Works

### Marp Markdown → HTML Pipeline
```
source/presentation-marp.md
    ↓ (Marp CLI parser)
HTML comments preserved as <!-- ... -->
    ↓ (Marp presenter mode JS)
Extracted and displayed in presenter window
    ↓ (Browser renders)
Visible in Presenter Mode (press P)
```

### Regenerating Presentation

```bash
cd /home/preact/sw/job/lam/ee
make marp

# Output:
# artifacts/presentation-marp.html (HTML with speaker notes)
# artifacts/presentation-marp.pdf (backup distribution format)
```

**Regeneration time:** ~1 second (much faster than PowerPoint conversion!)

## Troubleshooting

**Problem:** Presenter mode not working in browser

**Solution:**
1. Ensure you're opening the HTML file (not PDF)
2. Try different browser (Firefox, Chrome)
3. Press `P` key (case-sensitive)
4. Check JavaScript is enabled

**Problem:** Notes not visible in presenter mode

**Solution:**
1. Verify notes exist in source: `grep "Speaker notes:" source/presentation-marp.md`
2. Regenerate HTML: `make marp`
3. Refresh browser: `Ctrl+R` or `F5`

**Problem:** Need paper backup quickly

**Solution:**
```bash
# Extract all speaker notes to text file
grep -B 2 -A 10 "Speaker notes:" source/presentation-marp.md > /tmp/speaker-notes.txt
cat /tmp/speaker-notes.txt
```

## Summary: Marp Presentation Workflow

✅ **Speaker notes are working** - all slides have detailed HTML comments
✅ **Generation is fast** - `make marp` regenerates in 1 second
✅ **Viewing is easy** - Open HTML → Press P for Presenter Mode
✅ **Printing works** - Screenshot presenter mode or extract from source

**Next steps:**
1. Open `artifacts/presentation-marp.html` in browser
2. Press `P` to enter Presenter Mode
3. Practice delivery with notes visible on laptop, slides fullscreen on projector
4. Screenshot presenter mode for critical slides as paper backup

---

**END OF INTERVIEW PREP CHECKLIST**
