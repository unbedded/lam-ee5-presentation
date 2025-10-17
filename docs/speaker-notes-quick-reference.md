# Speaker Notes Quick Reference Card

**Interview Date:** October 21, 2025 (5 days away)
**Presentation:** 30 minutes, 29 main slides

---

## Status: ✅ Speaker Notes Fully Implemented

Your presentation has **comprehensive speaker notes on ALL 37 slides** (29 main + 8 appendix).

### How to View Notes RIGHT NOW:

```bash
# 1. Generate PPTX with embedded speaker notes
make pptx

# 2. Open in PowerPoint/Impress
xdg-open source/presentation.pptx

# 3. Start slideshow (F5) then press Alt+F5 for Presenter View
```

**Presenter View shows:**
- Your slide (audience view) - LEFT
- Next slide preview - RIGHT
- Speaker notes panel - BOTTOM
- Timer + slide counter

---

## Key Speaker Notes to Memorize

### Slide 3: Problem Statement ⭐ CRITICAL
```
"I read the spec CAREFULLY and extracted requirements."
"6 of 9 are vague - I need YOUR feedback before building the wrong thing."
"What you asked is NOT POSSIBLE in 2 months without trade-offs."
```

**Purpose:** Sets up honest engineering conversation, justifies portfolio approach

### Slide 5: Market Context
```
"$515-$2,199 USD range for 20-40 chars"
"100% piezo monopoly, 8-12 week lead time"
"Our 32 chars @ $600 USD fills market gap"
```

**Purpose:** Establishes commercial reality and competitive positioning

### Slide 13: EMI Challenge ⭐ SENIOR EE DIFFERENTIATOR
```
"30mm cantilever = λ/4 monopole @ 1.67 GHz"
"Piezo pays 2.5× EMI cost premium BUT gets 1.6× faster refresh"
```

**Purpose:** Shows GHz antenna physics understanding (senior-level knowledge)

### Slide 19: Decision Framework ⭐ KEY MESSAGE
```
"No 'best' architecture, only 'best FOR YOUR CONSTRAINTS'"
"Give me your priorities, I'll tell you which architecture wins"
```

**Purpose:** Demonstrates systems thinking and customer-centric design

### Slide 21: Actuator Sourcing ⭐ ELEPHANT IN ROOM
```
"THE ELEPHANT IN THE ROOM - must address head-on"
"No COTS solution exists today"
"$50K contingency for custom actuator NRE"
"Decision point: End of Week 2"
```

**Purpose:** Shows honest risk assessment and mitigation planning

---

## Practice Workflow (5 Days to Interview)

### Days 5-4 (Today-Tomorrow): Content Mastery
- ✅ Generate PPTX: `make pptx`
- ✅ Print Notes Pages: File → Print → "Notes Pages" (1 slide/page)
- ✅ Practice in Presenter View: Time each section (aim for ~60 sec/slide)
- ✅ Identify 5 key messages above - MEMORIZE those talking points

### Days 3-2: Delivery Practice
- ✅ Full run-through WITHOUT looking at notes (test internalization)
- ✅ Record yourself (audio/video) - identify weak spots
- ✅ Practice Q&A with appendix slides (be ready to jump to backup)
- ✅ Time transitions between sections

### Day 1: Final Prep
- ✅ Final run-through with notes (smooth delivery)
- ✅ Print backup: Notes Pages (2 pages/sheet, landscape, grayscale)
- ✅ Triple backup: USB drive + laptop + email PPTX to yourself

### Interview Day: Checklist
- ✅ Printed notes nearby (don't rely on tech)
- ✅ Load PPTX on interview computer (test Presenter View works)
- ✅ Glance at notes for transitions, NOT full reading
- ✅ Use appendix slides for deep technical Q&A

---

## Files Generated (Your "SPEAKER Version")

**Source (Markdown with speaker notes):**
```
source/presentation-slides.md
```

**Generated PPTX (with embedded notes):**
```
source/presentation.pptx
```

**Documentation:**
```
docs/presentation-speaker-notes-guide.md    (Full guide - 400 lines)
docs/speaker-notes-quick-reference.md      (This card)
```

**How to regenerate:**
```bash
make pptx  # Converts Markdown → PPTX with notes
```

---

## Verification: Speaker Notes Are Working

✅ **Verified:** All 29 main slides have speaker notes
✅ **Verified:** All 8 appendix slides have speaker notes
✅ **Verified:** Notes are embedded in `ppt/notesSlides/notesSlide*.xml`
✅ **Verified:** Pandoc converts `:::notes` blocks to PowerPoint format

**Test yourself:**
```bash
# Count notes files in PPTX (should be 37)
unzip -l source/presentation.pptx | grep -c "notesSlide"
```

---

## Key Numbers to Remember (From Speaker Notes)

- **32 characters = 192 dots** (6 dots/char standard + 2 extended)
- **$600 USD retail, $200 USD BOM target** ($6.25/cell)
- **2-month timeline = COTS mandate** (≤4 week lead time)
- **100% of commercial displays use custom piezo** (8-12 week lead)
- **30mm piezo cantilever = λ/4 antenna @ 1.67 GHz** (EMI challenge)
- **68 dB EMI reduction from firmware alone** ($0 hardware cost)
- **$50K NRE budget for custom actuator quickturn** (risk mitigation)
- **3 architectures, no universal "best"** (depends on priorities)

---

## Q&A Prep (From Slide 29 Speaker Notes)

### Anticipated Questions:
1. **Why can't you find COTS actuators?**
   → "2.5mm pitch is non-standard, most displays use 200V custom piezos"

2. **What if timeline extends to 4 months?**
   → "Opens door to custom actuator standard lead time, better cost optimization"

3. **Which architecture would YOU pick?**
   → "ARCH_PIEZO_ECO most robust, but depends on wireless requirement"

4. **Can you hit $200 BOM?**
   → "Not with COTS, need volume negotiation or custom actuator design"

5. **Power supply design for 200V piezo?**
   → "DC-DC boost converter, see appendix slides for EMI deep-dive"

### Deep Technical Backup:
- **Appendix A-G:** EMI physics, budget analysis, mitigation layers
- **If asked about GHz antenna:** Jump to Appendix A (λ/4 resonance derivation)
- **If asked about EMI cost:** Jump to Appendix D (2.5× premium breakdown)

---

## Timing Targets (30-Minute Presentation)

| Section | Slides | Time | Avg/Slide |
|---------|--------|------|-----------|
| Intro + Agenda | 2 | 2 min | 60s |
| Problem Statement | 1 | 2 min | 120s ⚠️ |
| Market Context | 2 | 2 min | 60s |
| Requirements | 4 | 4 min | 60s |
| Architectures | 4 | 4 min | 60s |
| **Evaluation** | 7 | **8 min** | 69s ← HIGHEST RUBRIC WEIGHT |
| Production | 4 | 4 min | 60s |
| Summary + Q&A | 2 | 2 min | 60s |
| **TOTAL** | **29** | **28 min** | **58s/slide** |

**Buffer:** 2 minutes for questions/interruptions

---

## Success Criteria

### Content Mastery:
- ✅ Can explain 3 architectures WITHOUT looking at slides
- ✅ Can answer "Which architecture would YOU pick?" (answer: it depends!)
- ✅ Can explain GHz antenna physics (30mm = λ/4 @ 1.67 GHz)
- ✅ Can list 3 critical risks (actuator sourcing, EMI cert, timeline)

### Delivery:
- ✅ Maintain 60s/slide pace (28-32 minutes total)
- ✅ Hit 5 key messages (Problem Statement, Market, EMI, Decision, Risk)
- ✅ Use notes as PROMPTS, not script (glance for transitions)
- ✅ Navigate smoothly to appendix slides for technical Q&A

### Backup Preparedness:
- ✅ Printed notes in binder (paper backup)
- ✅ PPTX on USB drive (tech backup)
- ✅ Can deliver WITHOUT slides (elevator pitch version)

---

## Final Confidence Check

**Before interview, ask yourself:**

1. Can I explain the problem in 30 seconds? ✅
   → "32-char braille display, 2-month timeline, COTS mandate, $200 BOM target"

2. Can I name 3 architectures in 15 seconds? ✅
   → "PIEZO_ECO (fast), SOL_ECO (cheap), PIEZO_DLX (wireless)"

3. Can I explain decision framework in 20 seconds? ✅
   → "No universal 'best' - depends on your priorities: wireless? cost? timeline?"

4. Can I state THE critical risk in 10 seconds? ✅
   → "Actuator sourcing - no COTS solution exists, $50K NRE mitigation budget"

5. Can I answer "Why should we hire YOU?" in 30 seconds? ✅
   → "I don't sell perfect solutions - I navigate trade-offs, manage risks, and provide decision frameworks. I understood GHz EMI physics, caught the actuator sourcing gap, and built a portfolio approach because requirements were vague. That's senior EE thinking."

---

## YOU'RE READY! 🎯

✅ **Speaker notes are implemented** - all 37 slides
✅ **Documentation is complete** - full guide + this quick reference
✅ **Practice workflow is defined** - 5-day plan
✅ **Key messages are identified** - memorize 5 critical points
✅ **Q&A prep is done** - 5 anticipated questions + appendix backup

**Next action:** Run `make pptx` → Open in PowerPoint → Press F5 → Alt+F5 → Practice!

**Interview:** October 21, 2025 @ LAM Research
**Presentation:** 30 minutes, 29 slides, 5 key messages
**Your edge:** Senior EE thinking + honest engineering + systems approach

**Good luck!** 🚀
