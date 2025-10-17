# Presentation Speaker Notes Guide

**For:** LAM Research EE Interview Presentation
**Purpose:** How to generate and use speaker notes in PowerPoint
**Date:** October 2025

---

## Quick Start: Speaker Notes Are ALREADY Working

✅ **Good news:** Your presentation ALREADY has speaker notes built in!

All `:::notes` blocks in `source/presentation-slides.md` automatically convert to PowerPoint speaker notes when you run:

```bash
make pptx
```

**Result:** `source/presentation.pptx` with embedded speaker notes visible in Presenter View

---

## How to View Speaker Notes in PowerPoint

### Option 1: Presenter View (RECOMMENDED for practice/delivery)

**During presentation (F5 slideshow mode):**

1. Open `source/presentation.pptx` in PowerPoint/LibreOffice Impress
2. Press **F5** to start slideshow
3. Press **Alt+F5** (or right-click → "Presenter View")
4. You'll see:
   - **Left:** Current slide (audience view)
   - **Right:** Next slide preview
   - **Bottom:** Speaker notes panel with all your talking points

**Benefits:**
- Notes visible ONLY to you (not projected to audience)
- Timer and slide counter included
- Next slide preview helps transitions

### Option 2: Notes Page View (for printing/review)

**To review all slides with notes:**

1. Open `source/presentation.pptx`
2. Click **View** → **Notes Page** (or press **Alt+W, P**)
3. You'll see each slide with its speaker notes below
4. Use **Page Down** to navigate through all slides

**Benefits:**
- Print notes pages for paper backup
- Review all slides + notes in single view
- Share notes with others

### Option 3: Normal View Notes Panel

**For quick editing:**

1. Open `source/presentation.pptx`
2. Click **View** → **Normal** (default view)
3. Bottom panel shows notes for selected slide
4. Drag panel border up to expand notes area

**Benefits:**
- Quick reference while editing slides
- No need to switch views

---

## Current Speaker Notes Summary

Your presentation has comprehensive speaker notes on **ALL slides**:

### High-Value Speaker Notes (Memorize These)

**Slide 3: Problem Statement**
```
"Strategic framing: 'I read the spec CAREFULLY and extracted requirements.'
'6 of 9 are vague - I need YOUR feedback before building the wrong thing.'
'What you asked is NOT POSSIBLE in 2 months without trade-offs.'
This sets up the portfolio approach (3 architectures) and honest engineering discussion."
```

**Slide 5: Market Context**
```
"Market context shows: (1) $515-$2,199 USD range for 20-40 chars,
(2) 100% piezo monopoly, (3) all custom with 8-12 week lead time.
Our target: 32 chars @ $600 USD fills market gap between 20-cell budget
and 40-cell mid-range. COTS mandate (≤4 week lead) forces innovation
beyond piezo monopoly."
```

**Slide 13: EMI Challenge**
```
"This is the senior EE differentiator: GHz antenna physics.
30mm cantilever = λ/4 monopole @ 1.67 GHz → FCC Part 15B most restrictive band.
Piezo pays 2.5× EMI cost premium BUT gets 1.6× faster refresh + zero hold power.
See backup deck (docs/slides/emi-analysis-slides.md) for detailed EMI budget analysis."
```

**Slide 19: Decision Framework**
```
"This is the key message: No 'best' architecture, only 'best FOR YOUR CONSTRAINTS'.
Tell customer: 'Give me your priorities, I'll tell you which architecture wins.'
Portfolio approach acknowledges requirements uncertainty."
```

**Slide 21: Actuator Sourcing Risk**
```
"THE ELEPHANT IN THE ROOM - must address head-on.
Honest engineering: No COTS solution exists today.
Triple-path strategy shows risk management (parallel efforts).
Budget allocation: $50K contingency for custom actuator NRE.
Decision point: End of Week 2, commit to one path."
```

---

## Workflow: Generate PPTX with Notes

### Step 1: Edit Markdown Source

Edit `source/presentation-slides.md` and add/update notes using this syntax:

```markdown
# Your Slide Title

Slide content here...

::: notes
Your speaker notes here. These will appear in PowerPoint's speaker notes panel.
Can span multiple lines and include:
- Bullet points
- Key talking points
- Timing reminders ("spend 2 minutes here")
- Technical details for Q&A backup
:::
```

### Step 2: Generate PPTX

```bash
cd /home/preact/sw/job/lam/ee
make pptx
```

**Output:**
```
Generating presentation.pptx from Markdown...
  Note: resources/style/lam-theme.pptx not found, using default Pandoc theme
✓ source/presentation.pptx generated

⚠️  WARNING: This is automated generation (Phase 1)
   After manual editing in PowerPoint, DO NOT regenerate from Markdown!
   Manual edits will be lost.
```

### Step 3: Open and Practice

```bash
# Open in PowerPoint (or LibreOffice Impress)
xdg-open source/presentation.pptx

# Or for LibreOffice specifically:
libreoffice source/presentation.pptx
```

**Then:**
1. Press **F5** to start slideshow
2. Press **Alt+F5** for Presenter View
3. Practice delivery with notes visible

---

## Best Practices for Using Speaker Notes

### DO:
- ✅ **Use notes for timing reminders** ("2 minutes on this slide")
- ✅ **Include Q&A anticipation** ("If asked about X, mention Y")
- ✅ **Write key numbers** ("32 chars = 192 dots (6 dots/char + 2 extended)")
- ✅ **Add strategic framing** ("This is the senior EE differentiator")
- ✅ **Reference backup slides** ("See appendix slide 3 for derivation")
- ✅ **Practice with Presenter View** multiple times before interview

### DON'T:
- ❌ **Read notes verbatim** - use as prompts, not script
- ❌ **Put slide content in notes** - notes should ADD context, not repeat
- ❌ **Make notes too long** - 3-5 sentences max per slide
- ❌ **Rely on notes during presentation** - internalize key messages
- ❌ **Print notes in tiny font** - use 12pt minimum for paper backup

---

## Recommended Practice Workflow

### Week Before Interview:
1. **Monday:** Generate PPTX, review all notes in Notes Page view
2. **Tuesday:** Practice full presentation in Presenter View, time each section
3. **Wednesday:** Identify weak spots, update notes in Markdown, regenerate
4. **Thursday:** Practice again without looking at notes (test internalization)
5. **Friday:** Final review with notes, print Notes Pages as paper backup

### Day Before Interview:
- Print Notes Pages (2 pages per sheet, landscape orientation)
- Bring printed notes as backup (in case screen sharing fails)
- Load PPTX on USB drive + laptop + email attachment (triple backup)

### Interview Day:
- Use Presenter View if possible (dual monitor/screen share setup)
- Have printed notes nearby (don't rely on tech)
- Glance at notes for transitions, not full reading

---

## Printing Speaker Notes

### Option A: Print from PowerPoint (Windows/Mac)

```
File → Print → Settings:
  - Layout: "Notes Pages"
  - Color: Grayscale
  - Handouts: 1 slide per page (for clarity)
```

### Option B: Print from LibreOffice Impress (Linux)

```
File → Print → Options:
  - Document: "Notes"
  - Color: Grayscale
  - Pages per sheet: 1 (or 2 for compact)
```

### Recommended Print Settings:
- **Font size:** Notes should be readable at arm's length (≥12pt)
- **Orientation:** Portrait (1 slide/page) or Landscape (2 slides/page)
- **Binding:** 3-hole punch + binder for easy flipping
- **Pages:** Print slides 1-29 (skip appendix for main deck)

---

## Technical Details: How It Works

### Pandoc Conversion Process

```
source/presentation-slides.md
    ↓ (Pandoc parser)
::: notes blocks → recognized as speaker notes div
    ↓ (PPTX writer)
PowerPoint XML: ppt/notesSlides/notesSlide*.xml
    ↓ (PowerPoint renders)
Visible in Presenter View / Notes Page
```

### File Locations:

**Source (Markdown):**
```
/home/preact/sw/job/lam/ee/source/presentation-slides.md
```

**Generated PPTX:**
```
/home/preact/sw/job/lam/ee/source/presentation.pptx
```

**Speaker notes XML (inside PPTX ZIP):**
```
ppt/notesSlides/notesSlide1.xml
ppt/notesSlides/notesSlide2.xml
...
ppt/notesSlides/notesSlide29.xml
```

### Verification:

To verify speaker notes are embedded:

```bash
# List all notes files in PPTX
unzip -l source/presentation.pptx | grep -i note

# Extract and view specific note (e.g., slide 3)
unzip -p source/presentation.pptx ppt/notesSlides/notesSlide3.xml
```

---

## Troubleshooting

### Problem: Notes not visible in PowerPoint

**Solution:**
1. Ensure you're in Presenter View (Alt+F5) or Notes Page view
2. Check if notes panel is collapsed (drag bottom edge up)
3. Verify PPTX was regenerated after adding `:::notes` blocks

### Problem: Notes are cut off or truncated

**Solution:**
- PowerPoint has no hard limit on note length
- If truncated in Presenter View, expand notes panel
- Print Notes Pages to see full text

### Problem: Notes formatting lost (bullets, emphasis)

**Expected behavior:**
- Pandoc converts notes to plain text
- Formatting (bold, italic) may not transfer
- Bullet points work but may render as plain text

**Workaround:**
- Use ALL CAPS for emphasis (works in plain text)
- Use numbered lists (1., 2., 3.) instead of bullets
- Keep formatting simple (speaker notes are for YOU, not audience)

### Problem: Make pptx fails

**Check:**
```bash
# Verify Pandoc is installed
pandoc --version

# Verify input file exists
ls -lh source/presentation-slides.md

# Check for syntax errors in Markdown
pandoc source/presentation-slides.md -t html -o /dev/null
```

---

## Advanced: Custom Theme with Speaker Notes

### If you create a custom PowerPoint theme:

1. Create reference PPTX in PowerPoint with desired styles
2. Save as `resources/style/lam-theme.pptx`
3. Regenerate presentation:

```bash
make pptx
```

Pandoc will automatically use `--reference-doc=resources/style/lam-theme.pptx`

**Benefits:**
- Custom fonts, colors, layouts
- LAM Research branding (if available)
- Consistent corporate style

**Note:** Speaker notes styling (font, size) is controlled by PowerPoint theme's "Notes Master" view.

---

## Summary: You're Already Set Up!

✅ **Speaker notes are working** - all 29 slides have detailed notes
✅ **Generation is automated** - `make pptx` regenerates with notes
✅ **Viewing is easy** - F5 → Alt+F5 for Presenter View
✅ **Printing works** - File → Print → Notes Pages

**Next steps:**
1. Open `source/presentation.pptx` in PowerPoint/Impress
2. Press F5 → Alt+F5 to enter Presenter View
3. Practice delivery with notes visible
4. Print Notes Pages as paper backup

**Key insight:** Your notes are EXCELLENT - they provide strategic framing, key numbers, and Q&A preparation. Practice with Presenter View multiple times to internalize the flow, then use notes as reminders rather than a script.

Good luck with your interview on **October 21, 2025**! 🎯
