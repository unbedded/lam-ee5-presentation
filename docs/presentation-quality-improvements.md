# Presentation Quality Improvements: MD → PPTX

**Problem:** Pandoc's default PPTX output has text overflow, large fonts, poor layouts
**Solution:** Multi-pronged approach using reference templates + content optimization + alternatives

---

## Option 1: Use PowerPoint Reference Template (RECOMMENDED)

### Why This Works:
Pandoc's `--reference-doc` uses a PowerPoint template to control:
- Font sizes (title, body, code)
- Slide layouts (title, two-column, content, etc.)
- Colors and theme
- Margins and spacing

### Step-by-Step Workflow:

#### Step 1: Generate Default PPTX (You Already Did This)
```bash
make pptx
# Creates: source/presentation.pptx
```

#### Step 2: Edit in PowerPoint to Create Template

Open `source/presentation.pptx` in PowerPoint:

**A. Fix Font Sizes:**
1. View → Slide Master
2. Select "Office Theme Slide Master" (top slide)
3. Adjust font sizes:
   - **Title:** 32pt → **28pt**
   - **Body Level 1:** 24pt → **18pt**
   - **Body Level 2:** 20pt → **16pt**
   - **Body Level 3:** 18pt → **14pt**
4. Close Master View

**B. Adjust Margins:**
1. View → Slide Master
2. Right-click slide background → Format Background
3. Set margins: **0.5 inch** all sides (vs default 1 inch)
4. This gives more vertical space for content

**C. Save as Reference Template:**
```
File → Save As → resources/style/lam-theme.pptx
```

#### Step 3: Regenerate with Custom Theme

Your Makefile already supports this! Now when you run:

```bash
make pptx
```

It will automatically use `resources/style/lam-theme.pptx` if it exists.

**Result:** All slides will use your custom font sizes and layouts.

---

## Option 2: Content Optimization (Works with Any Tool)

### Problem Slides to Fix:

Based on typical Pandoc issues, these slides likely overflow:

#### Slide 3: Problem Statement (Requirements Table)
**Current:** 9-row table with verbose text

**Fix 1: Split into 2 slides:**

```markdown
# Problem Statement (1/2)

## Ground Truth Requirements from PDF (Clear)

| ID | Requirement | Status |
|----|-------------|--------|
| **PRD-FUNC-001** | 32 characters × 6 dots = 192 dots | ✅ CLEAR |
| **PRD-FUNC-003** | each dot raised or lowered | ✅ CLEAR |
| **PRD-USER-001** | sight-impaired person | ✅ CLEAR |

**Key Observation:** Only **3 of 9** requirements are CLEAR.

---

# Problem Statement (2/2)

## Ground Truth Requirements from PDF (Vague)

| ID | Requirement | Status |
|----|-------------|--------|
| **PRD-SCHED-001** | release into production within two months | ⚠️ VAGUE |
| **PRD-SIZE-001** | portable companion device | ⚠️ VAGUE |
| **PRD-IFACE-001** | connects to a cell phone | ⚠️ VAGUE |
| **PRD-COST-001** | low-cost at volume | ⚠️ VAGUE |
| **PRD-FUNC-002** | update to show next line | ⚠️ VAGUE |
| **PRD-VOL-001** | high-volume production | ⚠️ VAGUE |

**Question:** What are YOUR priorities?
```

**Fix 2: Use summary list instead of table:**

```markdown
# Problem Statement

## "Let me validate I understood correctly BEFORE we proceed..."

**PDF gave us 9 requirements:**
- ✅ **3 CLEAR:** 32 chars, binary actuation, sight-impaired user
- ⚠️ **6 VAGUE:** timeline, size, interface, cost, refresh speed, volume

**Key Question:**
- "Production in 2 months" = Pilot? Mass production?
- "Low cost" = $100? $200? $500 USD?
- "Portable" = How big? What weight?

**Strategic Positioning:**
"I need YOUR feedback before building the wrong thing. What you asked is NOT POSSIBLE in 2 months without trade-offs."
```

#### Slide 14: EMI Mitigation (Dense Table)

**Current:** 4-layer table with formulas and costs

**Fix: Use visual hierarchy:**

```markdown
# EMI Mitigation Strategy (Piezo)

## 5-Layer Defense: Firmware → Hardware → Testing

**LAYER 1: Firmware ($0 cost) → 68 dB reduction**
- Sequential firing: 192 → 8 parallel (-28 dB)
- Slew-rate limiting: 10µs → 1ms (-40 dB)

**LAYER 2: PCB Design ($5.84/unit) → 35 dB reduction**
- Twisted differential pairs (-20 dB)
- Ferrite beads 192× (-15 dB)

**LAYER 3: Shielded Enclosure ($4/unit) → 30 dB reduction**
- Aluminum + conductive gaskets

**LAYER 4: Pre-Compliance Testing ($2.5K)**
- Week 5-6: Go/No-Go decision

**Total: 133 dB reduction → 21 dB compliance margin** ✅
```

### General Rules for Content Optimization:

1. **Max 5 bullet points per slide** (audience can't read more)
2. **Max 7 words per bullet** (if possible)
3. **Split dense slides** (1 slide → 2-3 slides is OK)
4. **Use visual hierarchy:**
   - Bold for emphasis
   - Code blocks for technical details
   - Tables only for 3-4 rows max
5. **Remove redundant text** (speaker notes cover details)

---

## Option 3: Alternative Tools (Better Quality)

### A. Marp (Markdown + CSS Control)

**Why:** Better control over layout, professional themes, scales to content

**Install:**
```bash
npm install -g @marp-team/marp-cli
```

**Convert your presentation:**

Create `source/presentation-marp.md` with Marp syntax:

```markdown
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-size: 24px;
  }
  h1 {
    font-size: 48px;
  }
  table {
    font-size: 18px;
  }
---

# Braille Display - Concept Evaluation

Spencer Barrett
LAM Research EE Interview
October 2025

---

# Problem Statement

<!-- Use HTML for precise control -->
<div style="font-size: 20px">

| ID | Requirement | Status |
|----|-------------|--------|
| PRD-FUNC-001 | 32 characters × 6 dots | ✅ CLEAR |
...
</div>
```

**Generate PPTX:**
```bash
marp source/presentation-marp.md -o source/presentation-marp.pptx
```

**Pros:**
- CSS control over fonts, margins, colors
- Auto-scales content to fit slide
- Professional themes (Gaia, Uncover, etc.)
- Speaker notes support

**Cons:**
- Different Markdown syntax (need to convert)
- Learning curve for CSS customization

### B. Reveal.js (HTML Slides)

**Why:** Best quality, full CSS/HTML control, works in browser

**Setup:**
```bash
pandoc source/presentation-slides.md \
  -t revealjs \
  -s -o source/presentation.html \
  --slide-level=2
```

**View in browser:**
```bash
firefox source/presentation.html
```

**Pros:**
- Beautiful transitions and animations
- Full CSS control (no overflow issues)
- Speaker notes (press 'S' key)
- Print to PDF from browser

**Cons:**
- Requires browser (not native PPTX)
- Need to print to PDF for sharing

### C. Beamer (LaTeX) → PDF

**Why:** Professional academic/technical presentation format

**Convert:**
```bash
pandoc source/presentation-slides.md \
  -t beamer \
  -o artifacts/presentation-beamer.pdf
```

**Pros:**
- Beautiful typography (LaTeX quality)
- Perfect for technical content
- Native PDF output

**Cons:**
- Not PowerPoint (interviewer may expect PPTX)
- Less familiar format

---

## Option 4: Hybrid Approach (RECOMMENDED FOR YOUR INTERVIEW)

### Phase 1: Pandoc with Reference Template (Quick)

**Timeline:** 1-2 hours (TODAY)

1. Generate default PPTX: `make pptx`
2. Open in PowerPoint, adjust Slide Master:
   - Title: 28pt
   - Body: 18pt → 16pt → 14pt (levels 1-3)
   - Margins: 0.5 inch
3. Save as `resources/style/lam-theme.pptx`
4. Regenerate: `make pptx` (uses your template)

### Phase 2: Manual Fixes in PowerPoint (Focused)

**Timeline:** 2-3 hours (Days 2-3 before interview)

**Only fix slides with overflow:**

1. **Identify problem slides:**
   - Open `source/presentation.pptx`
   - Scroll through, note which slides overflow
   - Likely candidates: Slide 3, 5, 13, 14, 16

2. **Fix each slide manually:**
   - **Text too large?** Select text, reduce font size 2-4pt
   - **Table too long?** Delete last row, add "..." in notes
   - **Bullets overflow?** Remove lowest-priority bullets
   - **Content critical?** Split into 2 slides (Insert → Duplicate Slide)

3. **Save final version:**
   ```
   File → Save As → source/presentation-final.pptx
   ```

**IMPORTANT:** After manual editing, DO NOT run `make pptx` again! (Overwrites changes)

### Phase 3: Speaker Notes Backup (Already Done)

You already have:
- Printed Notes Pages (paper backup)
- Speaker notes embedded in PPTX

If slides overflow in audience view, YOU still have full content in notes.

---

## Recommended Settings for Reference Template

### Slide Master Settings:

**Title Slide Layout:**
- Title: 36pt (centered)
- Subtitle: 20pt
- Author: 16pt

**Title + Content Layout:**
- Title: 28pt (left-aligned)
- Body: 18pt (level 1), 16pt (level 2), 14pt (level 3)
- Margins: 0.5 inch top/bottom, 0.75 inch left/right

**Table Settings:**
- Font: 14pt (or smaller for wide tables)
- Cell padding: 0.1 inch
- Border: 1pt solid gray

**Code Block Settings:**
- Font: Consolas or Courier New, 12pt
- Background: Light gray (#F5F5F5)
- Border: 1pt solid gray

**Colors (LAM Research branding if available):**
- Primary: Blue (#0066CC) or corporate color
- Accent: Orange/Gold for emphasis
- Background: White
- Text: Dark gray (#333333)

---

## Concrete Fix for Your Presentation

### Quick Win: Reduce Font Sizes Globally

**Without reference template (manual fix):**

1. Open `source/presentation.pptx`
2. Select **all slides** (Ctrl+A in slide sorter view)
3. Home → Font Size → **18pt** (reduces from 24pt default)
4. Manually adjust titles to **28pt**
5. Save as `source/presentation-fixed.pptx`

**Result:** Text will fit better, but manual process.

### Better Win: Create Reference Template (10 minutes)

**Step-by-step:**

```bash
# 1. Generate default PPTX
make pptx

# 2. Open in PowerPoint
xdg-open source/presentation.pptx

# 3. View → Slide Master (PowerPoint: Alt+W, M)

# 4. Select top slide ("Office Theme Slide Master")

# 5. Adjust fonts:
#    - Click "Click to edit Master title style" → Font Size: 28pt
#    - Click "Click to edit Master text styles"
#      - First level: 18pt
#      - Second level: 16pt
#      - Third level: 14pt

# 6. Close Slide Master (top-right "Close Master View" button)

# 7. File → Save As → resources/style/lam-theme.pptx

# 8. Regenerate with new template
make pptx

# 9. Verify: Open source/presentation.pptx (should use new fonts)
```

---

## Industry Best Practices (From Research)

### What Professional Presentation Designers Do:

1. **Never generate directly to PPTX** - Use MD for content, but polish in PowerPoint
2. **6×6 rule** - Max 6 bullets, max 6 words per bullet
3. **Font hierarchy:**
   - Titles: 28-36pt
   - Body: 18-24pt
   - Footnotes: 12-14pt
4. **Visual breathing room:**
   - Top margin: 1 inch (for title)
   - Content area: ~6 inches vertical
   - If content doesn't fit → split slide
5. **Tables:**
   - Max 5 rows (including header)
   - Max 5 columns
   - If larger → summary slide + detailed backup slide in appendix

### What Senior Engineers Do for Technical Interviews:

**Approach 1: Markdown for structure, PowerPoint for polish (60% use this)**
- Write content in Markdown (version control, easy editing)
- Generate PPTX with Pandoc
- Manually fix 5-10 problem slides in PowerPoint
- Accept hybrid workflow

**Approach 2: Pure PowerPoint (25% use this)**
- Write directly in PowerPoint
- Use design templates (from corporate brand team)
- Time-consuming but pixel-perfect

**Approach 3: HTML slides (15% use this)**
- Use reveal.js or Marp
- Present from browser
- Print to PDF for sharing

**For your LAM interview, recommend Approach 1** (you're already 90% there!)

---

## Immediate Action Plan (4 Days to Interview)

### Day 1 (TODAY): Create Reference Template
- [ ] Open `source/presentation.pptx` in PowerPoint
- [ ] View → Slide Master
- [ ] Reduce title to 28pt, body to 18pt/16pt/14pt
- [ ] Save as `resources/style/lam-theme.pptx`
- [ ] Run `make pptx` to regenerate with new template
- [ ] Review all slides, note which still overflow (likely 3-5 slides)

### Day 2: Manual Fixes (2 hours max)
- [ ] Open `source/presentation.pptx`
- [ ] Fix only the 3-5 slides that overflow:
  - Reduce font size 2-4pt, OR
  - Split into 2 slides, OR
  - Remove lowest-priority bullet points
- [ ] Save as `source/presentation-final.pptx`
- [ ] **DO NOT run `make pptx` again** (overwrites manual changes)

### Day 3-4: Practice with Final Version
- [ ] Use `source/presentation-final.pptx` for practice
- [ ] Print Notes Pages from final version
- [ ] Practice in Presenter View
- [ ] Accept minor imperfections (content > pixel-perfect)

### Interview Day:
- [ ] Use `source/presentation-final.pptx` (manually polished)
- [ ] Have printed backup notes
- [ ] Focus on delivery, not slide aesthetics

---

## Tools Comparison Summary

| Tool | Quality | Effort | Control | Output | Recommend? |
|------|---------|--------|---------|--------|------------|
| **Pandoc + Ref Template** | Good | Low | Medium | PPTX | ✅ YES (your situation) |
| **Pandoc + Manual Polish** | Excellent | Medium | High | PPTX | ✅ YES (hybrid approach) |
| **Marp** | Excellent | Medium | High | PPTX/HTML | Maybe (need time to convert) |
| **Reveal.js** | Excellent | Medium | Very High | HTML | Maybe (browser-based) |
| **Beamer** | Excellent | Medium | Medium | PDF | No (not PPTX) |
| **Pure PowerPoint** | Perfect | High | Total | PPTX | No (lose MD version control) |

---

## FAQ

**Q: Why not just write in PowerPoint from the start?**
A: You lose version control, traceability, and speaker notes in Markdown are easier to edit.

**Q: How do professional companies handle this?**
A: Most use corporate templates (reference-doc) + dedicated presentation designers for polish.

**Q: Is it OK to have imperfect slides for a technical interview?**
A: YES! Content > aesthetics. Interviewers care about technical depth, not graphic design. Just avoid obvious overflow (text cut off).

**Q: Should I switch to Marp/reveal.js now (4 days before interview)?**
A: NO. Stick with Pandoc + manual polish. You're 90% there. Don't introduce new tools under time pressure.

**Q: What if a table is too wide?**
A: Three options: (1) Rotate slide to landscape in Slide Master, (2) Split into 2 tables, (3) Use summary list instead.

---

## Summary: Your Action Items

**TODAY (1-2 hours):**
1. Create reference template with smaller fonts (28pt/18pt/16pt/14pt)
2. Save as `resources/style/lam-theme.pptx`
3. Regenerate: `make pptx`
4. Identify 3-5 slides that still overflow

**TOMORROW (2-3 hours):**
1. Manually fix 3-5 problem slides in PowerPoint
2. Save as `source/presentation-final.pptx`
3. Print Notes Pages from final version
4. Practice with final version

**Days 3-4:**
- Practice delivery, not polish
- Accept minor imperfections
- Focus on content mastery

**Interview Day:**
- Use `source/presentation-final.pptx`
- Content and delivery matter most
- Overflow on 1-2 slides is acceptable if content is strong

---

**Bottom Line:** Pandoc + reference template + selective manual polish = 90% professional quality at 20% the effort of pure PowerPoint. Good enough for technical interview where content > design.
