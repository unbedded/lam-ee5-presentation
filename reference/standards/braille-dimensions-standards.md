# Braille Dimensions Standards

**Purpose:** Reference document for braille tactile interface design requirements
**Sources:** Braille Authority of North America, US ADA Standards (703.3), Australian Braille Authority
**Date:** 2025-10-08

---

## Summary: Design Standards for Refreshable Braille Display

### Critical Dimensions (for actuator/mechanical design)

| Parameter | US ADA Standard | North American | Australian | Typical Target |
|-----------|----------------|----------------|------------|----------------|
| **Dot Diameter** | 1.5-1.6 mm (0.059″-0.063″) | ~1.5 mm | 1.4-1.6 mm | **1.5 mm** |
| **Dot Height** | 0.64-0.94 mm (0.025″-0.037″) | ~0.5 mm | 0.4-0.7 mm | **0.5-0.7 mm** |
| **Dot Spacing (within cell)** | 2.3-2.5 mm (0.090″-0.100″) | 2.54 mm (0.1″) | 2.3-2.5 mm | **2.5 mm** |
| **Cell Spacing (horizontal)** | 6.1-7.6 mm (0.241″-0.300″) | 5.08 mm (0.2″) | 6.0-7.0 mm | **6.0 mm** |
| **Line Spacing (vertical)** | 10.0-10.2 mm (0.395″-0.4″) | ~10 mm | 10.0-11.0 mm | **10.0 mm** |
| **Dot Shape** | Domed/rounded | Domed | Rounded | **Dome/hemisphere** |

---

## Detailed Specifications

### 1. Individual Dot (Actuator Requirements)

**Dot Diameter:**
- US ADA: 0.059″ – 0.063″ (1.5-1.6 mm)
- Australian: 1.4 mm – 1.6 mm
- **Design Target: 1.5 mm ±0.1 mm**

**Dot Height (raised position):**
- US ADA: 0.025″ – 0.037″ (0.64-0.94 mm)
- Australian: 0.4 mm – 0.7 mm
- North American: ~0.5 mm typical
- **Design Target: 0.5-0.7 mm** (higher = easier to read, but requires more actuator force)

**Dot Shape:**
- **Requirement:** Domed or rounded (NOT flat-topped)
- **Why:** Tactile sensitivity requires smooth dome for finger scanning
- **Actuator implication:** Pin must have hemispherical or rounded tip

**Dot Force (tactile feedback):**
- Not standardized, but literature suggests 50-100 grams force
- **Design consideration:** Actuator must maintain raised position under finger pressure

---

### 2. Braille Cell (6-dot pattern: 2 columns × 3 rows)

**Dot Spacing Within Cell (center-to-center):**
- US ADA: 0.090″ – 0.100″ (2.3-2.5 mm)
- North American: 0.1″ (2.54 mm) on centers
- Australian: 2.3 mm – 2.5 mm
- **Design Target: 2.5 mm pitch** (both horizontal and vertical within cell)

**Cell Dimensions:**
- Width: 2 dots × 2.5 mm spacing = **~2.5 mm wide** (dot 1 to dot 4 center-to-center)
- Height: 3 dots × 2.5 mm spacing = **~5.0 mm tall** (dot 1 to dot 3 center-to-center)

**Layout (standard numbering):**
```
Dot 1 •     • Dot 4
Dot 2 •     • Dot 5
Dot 3 •     • Dot 6
```
- Left column: dots 1, 2, 3 (top to bottom)
- Right column: dots 4, 5, 6 (top to bottom)

---

### 3. Character Spacing (Between Adjacent Cells)

**Horizontal Spacing (between adjacent characters):**
- US ADA: 0.241″ – 0.300″ (6.1-7.6 mm) spacing between corresponding dots in adjacent cells
- North American: 0.2″ (5.08 mm) space between cells
- Australian: 6.0 mm – 7.0 mm center-to-center of corresponding dots
- **Design Target: 6.0 mm pitch** (center of rightmost dot in cell N to leftmost dot in cell N+1)

**Vertical Spacing (between lines):**
- US ADA: 0.395″ – 0.4″ (10.0-10.2 mm) baseline spacing
- Australian: 10.0 mm – 11.0 mm center-to-center of nearest corresponding dots
- **Design Target: 10.0 mm pitch** (for multi-line displays; N/A for single-line)

---

### 4. Full 32-Character Display Dimensions

**Using design targets (2.5 mm dot pitch, 6.0 mm cell pitch):**

**Single braille cell:**
- Width: 2.5 mm (dot 1 to dot 4)
- Height: 5.0 mm (dot 1 to dot 3)

**32-character line (horizontal layout):**
- Total width:
  - 32 cells × 6.0 mm pitch = **192 mm** (center of cell 1 to center of cell 32)
  - Plus margins: ~200-210 mm total device width
- Height:
  - Single line: 5 mm (cell height)
  - Plus margins: ~10-15 mm total device height (just braille area)

**Total dot count:**
- 32 characters × 6 dots/char = **192 individual actuators**

---

## Design Implications for Actuator Selection

### Mechanical Requirements:
1. **Stroke:** ≥0.5 mm (minimum dot height), prefer 0.7 mm for margin
2. **Force:** 50-100 grams to maintain raised position under finger pressure
3. **Dot tip:** Hemispherical or domed (1.5 mm diameter)
4. **Spacing:** 2.5 mm pitch within cell, 6.0 mm pitch between cells
5. **Reliability:** >1 million cycles (reading 8 hours/day × 2 years = ~5 million actuations)

### Electrical Requirements:
1. **Control:** Binary on/off (raised or lowered)
2. **Update rate:** <2 seconds for full line update (acceptable user experience)
3. **Power:** Will depend on actuator technology (piezo, solenoid, SMA)

---

## Flexibility in Standards (Engineering Trade-offs)

### Where there's flexibility:
- **Dot height:** 0.5-0.7 mm range (can optimize for actuator capability)
- **Cell spacing:** 6.0-7.0 mm range (can adjust for mechanical constraints)
- **Dot shape:** "Domed or rounded" (hemispherical, elliptical, rounded cone all acceptable)

### Where there's NO flexibility:
- **Dot diameter:** Must be ~1.5 mm (tactile sensitivity requirement)
- **Dot spacing within cell:** Must be 2.3-2.5 mm (reading comprehension)
- **6-dot pattern:** Standard Grade 1 braille (not negotiable per PDF spec)

### Design Recommendations:
1. **Start with:** 1.5 mm dot diameter, 0.5 mm height, 2.5 mm pitch
2. **Test:** User testing with target demographic (can adjust height ±0.2 mm)
3. **Optimize:** Trade height vs force vs cost (higher dots = better UX but harder actuation)

---

## Standards References

### Primary Sources:
1. **US ADA Standards (Section 703.3):** Legal requirement for US installations
   - https://www.access-board.gov/ada/guides/chapter-7-signs/

2. **Braille Authority of North America (BANA):**
   - https://brailleauthority.org/size-and-spacing-braille-characters

3. **Australian Braille Authority:**
   - https://brailleaustralia.org/about-braille/physical-specifications-for-braille/

### International Standards:
- **ISO 17049:2013** - Braille on packaging for medicinal products
- **ANSI/NISO Z39.86** - Specifications for the Digital Talking Book

---

## Assumptions for This Project

Based on standards research, we assume:

**ASMP-BRAILLE-001: Dot Dimensions**
- **Dot diameter:** 1.5 mm ±0.1 mm
- **Dot height:** 0.5-0.7 mm (target 0.6 mm for margin)
- **Dot shape:** Hemispherical dome
- **Risk level:** LOW (standards are clear and consistent)
- **Impact if wrong:** If <1.4 mm or >1.6 mm diameter, tactile readability degrades

**ASMP-BRAILLE-002: Spacing**
- **Dot pitch (within cell):** 2.5 mm center-to-center
- **Cell pitch (between chars):** 6.0 mm center-to-center
- **Risk level:** LOW (standards are clear)
- **Impact if wrong:** If spacing off by >10%, reading speed/accuracy degrades significantly

**ASMP-BRAILLE-003: Actuator Force**
- **Force:** 50-100 grams to maintain raised dot under finger pressure
- **Risk level:** MEDIUM (not formally standardized, based on literature)
- **Impact if wrong:** If <50g, dots collapse under finger. If >100g, harder to actuate (power/cost)

---

## Design Validation Plan

### v1.3.0 (Architecture Design):
- [ ] Select actuator technology capable of 0.5-0.7 mm stroke
- [ ] Verify actuator force capability (50-100g holding force)
- [ ] Check mechanical spacing compatibility (2.5 mm pitch achievable?)

### v1.5.0 (Production Plan):
- [ ] Prototype testing with braille readers (user validation)
- [ ] Measure actual dot height, diameter, spacing with calipers/profilometer
- [ ] Compare to ADA standards for compliance

### Presentation (v2.0.0):
- [ ] Reference ADA/BANA standards in requirements slide
- [ ] Show mechanical drawing with callouts to standard dimensions
- [ ] Demonstrate understanding of tactile interface engineering

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-08 | Spencer Barrett | Initial braille standards reference from web research (ADA, BANA, Australian standards) |
