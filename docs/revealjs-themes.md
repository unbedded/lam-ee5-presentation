# Reveal.js Themes Quick Reference

## Try Different Themes:

Edit Makefile line 158 to change theme:

```makefile
-V theme=black    # Current (dark background, white text)
```

### Available Themes:

**Professional:**
- `black` - Dark background, white text (current)
- `white` - White background, black text (corporate)
- `league` - Gray background, white text (elegant)
- `beige` - Beige background, brown text (warm)
- `serif` - Serif fonts, classic look

**Modern:**
- `sky` - Blue gradient background
- `night` - Dark with orange accents
- `simple` - Minimal, clean
- `solarized` - Solarized color scheme

**Technical:**
- `moon` - Dark blue, professional
- `blood` - Dark with red accents (dramatic)

## To Change Theme:

```bash
# Edit Makefile line 158, or run directly:
pandoc source/presentation-slides.md \
  -t revealjs -s \
  -o source/presentation.html \
  --slide-level=1 \
  -V theme=white \
  -V transition=slide

# Open
firefox source/presentation.html
```

## Recommended for LAM Interview:

**Option 1: `white` theme** (most corporate/professional)
**Option 2: `black` theme** (tech-forward, high contrast)
**Option 3: `league` theme** (elegant middle ground)

## Transitions:

Change line 159 for different slide transitions:

- `none` - Instant (fast-paced)
- `fade` - Crossfade (smooth)
- `slide` - Slide horizontally (default, good)
- `convex` - 3D rotate (fancy)
- `concave` - 3D rotate inward (fancy)
- `zoom` - Zoom effect (dramatic)

## Speaker Notes:

Your `:::notes` blocks work perfectly!

**During presentation:**
1. Press **'S'** key
2. Speaker view opens in new window
3. Shows:
   - Current slide
   - Next slide preview
   - Speaker notes
   - Timer

**Perfect for interview!**
