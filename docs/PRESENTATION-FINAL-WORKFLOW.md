# Final Presentation Workflow - LAM Research EE Interview

**Decision:** HTML Presentation (Marp) - Path A ✅

**Interview Date:** October 21, 2025 (4 days away)

---

## Quick Start

```bash
# Edit presentation
vim source/presentation-marp.md

# Regenerate (1 second!)
make marp

# Present
firefox artifacts/presentation-marp.html
# Press F11 for fullscreen
```

---

## File Structure

```
source/
  presentation-marp.md          ← EDIT THIS (source, in git)
  market-price-vs-chars.svg     ← Images (in git)

artifacts/
  presentation-marp.html        ← PRESENT FROM THIS (generated, NOT in git)
  presentation-marp.pdf         ← SHARE THIS (generated, NOT in git)
```

**Rule:** Only `source/` files go in git. `artifacts/` is regenerated with `make marp`

---

## Daily Workflow (Next 4 Days)

### Day 1 (Today - October 17):
- [x] Marp setup complete
- [ ] Review all slides in HTML
- [ ] Identify 3-5 slides needing content tweaks
- [ ] Update `source/presentation-marp.md`
- [ ] Regenerate: `make marp`

### Day 2 (October 18):
- [ ] Practice presentation (full run-through)
- [ ] Time each section (~60 sec/slide target)
- [ ] Fix any overflow/content issues
- [ ] Finalize content (no more major changes after today)

### Day 3 (October 19):
- [ ] Practice delivery (no content edits)
- [ ] Memorize 5 key talking points
- [ ] Export final PDF: `artifacts/presentation-marp.pdf`
- [ ] Print PDF as backup (2 pages/sheet)

### Day 4 (October 20):
- [ ] Final practice run
- [ ] Test on interview laptop (if possible)
- [ ] Load files on USB drive
- [ ] Email HTML + PDF to yourself (backup)

### Interview Day (October 21):
- [ ] Present from `artifacts/presentation-marp.html`
- [ ] Have printed PDF backup
- [ ] USB drive with HTML file
- [ ] Laptop with local copy

---

## Interview Presentation Setup

### Option 1: Present from Local File (RECOMMENDED)
```bash
firefox /home/preact/sw/job/lam/ee/artifacts/presentation-marp.html
# Press F11 for fullscreen
# Arrow keys to navigate
```

### Option 2: Present from USB Drive
1. Copy to USB: `cp artifacts/presentation-marp.html /media/usb/`
2. Also copy images: `cp source/*.svg /media/usb/`
3. On interview computer: Open HTML from USB in any browser

### Option 3: Present from Cloud (Backup)
1. Upload `artifacts/presentation-marp.html` to Google Drive
2. Share link (view-only)
3. Open in browser during interview

---

## Navigation Controls

| Key | Action |
|-----|--------|
| **Arrow Right** or **Space** | Next slide |
| **Arrow Left** or **Shift+Space** | Previous slide |
| **F11** | Fullscreen (IMPORTANT!) |
| **Esc** | Exit fullscreen |
| **Home** | First slide |
| **End** | Last slide |

---

## Making Content Changes

### Quick Text Edit:
```bash
# Edit Markdown
vim source/presentation-marp.md

# Find the slide (search for title)
/Problem Statement

# Make changes

# Regenerate
make marp

# View changes
firefox artifacts/presentation-marp.html
```

### Adjust Font Sizes:
Edit lines 7-51 in `source/presentation-marp.md`:

```yaml
style: |
  section {
    font-size: 24px;      # ← Body text (increase if too small)
  }
  h1 {
    font-size: 40px;      # ← Slide titles (decrease if too large)
  }
  table {
    font-size: 20px;      # ← Tables
  }
```

### Add/Remove Slides:
```markdown
---

# New Slide Title

Content here...

- Bullet 1
- Bullet 2

---
```

**Then:** `make marp` to regenerate

---

## Customization Options

### Change Theme Colors:

**Blue accent (current):**
```css
h1 {
  border-bottom: 3px solid #3498db;  /* Blue */
}
table thead th {
  background-color: #2980b9 !important;  /* Blue */
}
```

**LAM Research corporate colors (if you get them):**
```css
h1 {
  border-bottom: 3px solid #YOUR_COLOR;
}
```

### Adjust Slide Spacing:
```css
section {
  padding: 50px;  /* Increase for more whitespace */
}
```

---

## Common Issues & Fixes

### Issue: Title takes too much space
**Fix:** Reduce `h1` font-size (line 11):
```css
h1 {
  font-size: 36px;  /* Was 40px */
}
```

### Issue: Table too wide
**Fix:** Reduce columns or make font smaller:
```css
table {
  font-size: 18px;  /* Was 20px */
}
```

### Issue: Image doesn't show
**Fix:** Ensure image is in `source/` directory:
```bash
cp path/to/image.svg source/
```

Then use in Markdown:
```markdown
![Description](image.svg)
```

### Issue: Slide has too much content
**Fix:** Split into 2 slides:
```markdown
---

# Original Title (Part 1)

First half of content...

---

# Original Title (Part 2)

Second half of content...

---
```

---

## Backup Strategy (3-2-1 Rule)

**3 Copies:**
1. Laptop: `/home/preact/sw/job/lam/ee/artifacts/presentation-marp.html`
2. USB Drive: `presentation-marp.html` + images
3. Cloud: Google Drive backup

**2 Formats:**
1. HTML (primary - for presenting)
2. PDF (backup - for sharing)

**1 Offsite:**
- Email HTML + PDF to yourself
- Or upload to Google Drive/Dropbox

---

## Interview Day Checklist

### Before Leaving Home:
- [ ] Laptop charged (100%)
- [ ] USB drive with HTML + images
- [ ] Printed PDF backup (2 copies)
- [ ] Test presentation one final time

### At Interview:
- [ ] Offer to present from HTML ("I have an HTML presentation - works in any browser")
- [ ] If they prefer PDF: Share `artifacts/presentation-marp.pdf`
- [ ] If browser unavailable: Use printed backup

### During Presentation:
- [ ] F11 for fullscreen immediately
- [ ] Use arrow keys (smooth navigation)
- [ ] Refer to printed notes for key talking points
- [ ] Glance at screen to stay on track

---

## Key Talking Points (Memorize)

**Slide 3 (Problem Statement):**
"6 of 9 requirements are vague - I need YOUR feedback before building the wrong thing"

**Slide 5 (Market):**
"100% piezo monopoly, 8-12 week lead time. Our COTS mandate forces innovation"

**Slide 13 (EMI):**
"30mm cantilever = λ/4 monopole @ 1.67 GHz - this is GHz antenna physics"

**Slide 15 (Decision):**
"No 'best' architecture, only 'best FOR YOUR CONSTRAINTS'"

**Slide 17 (Actuator):**
"THE ELEPHANT IN THE ROOM - $50K NRE budget allocated"

---

## Advantages of HTML Presentation

✅ **Editable until last minute** - Fix typos up to interview day
✅ **Works everywhere** - Any browser, any OS
✅ **Professional** - Shows technical competency
✅ **Fast iteration** - Edit → regenerate → present (3 seconds)
✅ **No surprises** - What you see is what they see
✅ **Portable** - Single HTML file + images folder
✅ **Version controlled** - Markdown source in git

---

## If They Ask for PPTX

**Option 1: Share PDF instead**
"I have a PDF version available - would that work?"

**Option 2: Generate PPTX (but warn it's not editable)**
```bash
marp source/presentation-marp.md -o artifacts/presentation-marp.pptx --allow-local-files
```

Note: Slides will be images, not editable text

**Option 3: Import to Google Slides**
1. Upload HTML to Google Drive
2. Right-click → Open with Google Slides
3. May need manual cleanup
4. Download as PPTX

---

## Post-Interview

After interview, commit final version to git:

```bash
git add source/presentation-marp.md
git add source/*.svg
git commit -m "Final presentation for LAM Research EE interview (Oct 21, 2025)"
git push
```

Keep `artifacts/` files local (not in git - regenerate with `make marp`)

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `make marp` | Regenerate HTML + PDF |
| `firefox artifacts/presentation-marp.html` | Present |
| `vim source/presentation-marp.md` | Edit content |
| `cp source/*.svg /media/usb/` | Copy to USB |

---

## Summary

**Source:** `source/presentation-marp.md` (edit this)
**Present:** `artifacts/presentation-marp.html` (F11 for fullscreen)
**Share:** `artifacts/presentation-marp.pdf` (if requested)

**Workflow:** Edit → `make marp` → Present → Impress! 🎯

Good luck with your interview! 🚀
