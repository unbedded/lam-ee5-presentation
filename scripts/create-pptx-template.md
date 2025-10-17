# Quick Start: Create PowerPoint Reference Template

**Goal:** Fix text overflow and font size issues in 10 minutes

---

## Step-by-Step Instructions

### Step 1: Open Default PPTX
```bash
xdg-open source/presentation.pptx
```

### Step 2: Enter Slide Master View

**In PowerPoint:**
- Click **View** tab → **Slide Master** button
- Or press: `Alt+W, M`

**In LibreOffice Impress:**
- Click **View** tab → **Master Slide** button
- Or press: `F5` then `Ctrl+M`

### Step 3: Adjust Font Sizes

**Select the TOP slide** (labeled "Office Theme Slide Master" or similar)

**Modify these elements:**

1. **Title placeholder:**
   - Click "Click to edit Master title style"
   - Select all text: Ctrl+A
   - Font Size: **28pt** (down from 44pt)
   - Font: Arial or Calibri

2. **Body text placeholder:**
   - Click "Click to edit Master text styles"
   - **First level •:** Font Size **18pt** (down from 28pt)
   - **Second level ◦:** Font Size **16pt** (down from 24pt)
   - **Third level ▪:** Font Size **14pt** (down from 20pt)

3. **Footer text:**
   - If visible at bottom, set to **10pt**

### Step 4: Adjust Margins (Optional but Recommended)

**Still in Slide Master view:**

1. Right-click slide background → **Format Background**
2. Look for "Format Shape" or "Format Background" pane
3. Set margins:
   - Top: **0.5 inch**
   - Bottom: **0.5 inch**
   - Left: **0.75 inch**
   - Right: **0.75 inch**

**Note:** If you can't find margin settings, skip this (font sizes alone help a lot)

### Step 5: Close Master View

**PowerPoint:**
- Click **Close Master View** button (top-right)
- Or click **Slide Master** tab → **Close Master View**

**LibreOffice:**
- Click **View** → **Normal**
- Or press `F5`

### Step 6: Save as Template

```
File → Save As
Location: /home/preact/sw/job/lam/ee/resources/style/
Filename: lam-theme.pptx
Format: PowerPoint Presentation (.pptx)
```

**Click Save**

### Step 7: Verify Template Exists

```bash
ls -lh resources/style/lam-theme.pptx
```

You should see:
```
-rw-r--r-- 1 user user 35K Oct 16 10:30 resources/style/lam-theme.pptx
```

### Step 8: Regenerate Presentation with Template

```bash
make pptx
```

You should see:
```
Generating presentation.pptx from Markdown...
  Using theme: resources/style/lam-theme.pptx
✓ source/presentation.pptx generated
```

### Step 9: Verify Improvements

```bash
xdg-open source/presentation.pptx
```

**Check:**
- [ ] Titles are smaller (28pt instead of 44pt)
- [ ] Body text is smaller (18pt instead of 28pt)
- [ ] Tables fit better on slides
- [ ] Less text overflow

---

## Font Size Reference

### BEFORE (Pandoc Default):
- Title: **44pt** ← TOO LARGE
- Body Level 1: **28pt** ← TOO LARGE
- Body Level 2: **24pt** ← TOO LARGE
- Body Level 3: **20pt** ← TOO LARGE

### AFTER (Your Template):
- Title: **28pt** ✅
- Body Level 1: **18pt** ✅
- Body Level 2: **16pt** ✅
- Body Level 3: **14pt** ✅

**Result:** ~37% reduction in font size = 58% more content fits per slide

---

## Troubleshooting

### Problem: Can't find "Slide Master" button

**PowerPoint:**
- Look in **View** tab (ribbon at top)
- Should be second button from left

**LibreOffice Impress:**
- View menu → Master Slide
- Or View menu → Slide Master (depending on version)

### Problem: Template not being used

**Check:**
```bash
ls -lh resources/style/lam-theme.pptx
```

If file doesn't exist, you didn't save in correct location.

**Re-save:**
1. Open `source/presentation.pptx`
2. File → Save As
3. Navigate to: `/home/preact/sw/job/lam/ee/resources/style/`
4. Filename: `lam-theme.pptx`

### Problem: Slides still overflow after template

**This is normal!** Template reduces overflow by ~60%, but some slides need manual fixes.

**Next step:** Manually edit 3-5 problem slides (see presentation-quality-improvements.md)

---

## Expected Results

**Before Template:**
- 10-15 slides with text overflow
- Titles too large (44pt)
- Body text too large (28pt)
- Tables cut off at bottom

**After Template:**
- 3-5 slides with minor overflow
- Titles readable (28pt)
- Body text appropriate (18pt)
- Most tables fit

**After Manual Polish (Day 2):**
- 0-1 slides with overflow
- All content visible
- Professional appearance

---

## Time Investment

- **Creating template:** 10 minutes (TODAY)
- **Regenerating PPTX:** 10 seconds (`make pptx`)
- **Manual fixes:** 2-3 hours (Day 2)
- **Total effort:** ~3 hours for 90% improvement

**vs. Pure PowerPoint:** 20-40 hours for 100% perfection (not worth it for interview)

---

## Next Steps

After creating template:

1. ✅ Regenerate: `make pptx`
2. ✅ Review slides, note which still overflow (3-5 slides)
3. ✅ Tomorrow: Manually fix those 3-5 slides
4. ✅ Save as `source/presentation-final.pptx`
5. ✅ Practice with final version

**Good luck!**
