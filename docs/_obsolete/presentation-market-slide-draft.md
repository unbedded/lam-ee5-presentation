# Market Comparison Slide Draft
**For:** LAM Research EE Interview Presentation
**Purpose:** Show market context and competitive positioning (insert after problem statement, before requirements)

---

## SLIDE: Commercial Braille Display Market

### Market Landscape

**Budget Segment (<$1K USD)**
- **Orbit Reader 20** – 20 cells (20 characters), $799 USD, USB+BLE, rechargeable
  - "World's most affordable" (education market)
- **BrailleMe** – 20 cells (20 characters), $515 USD, USB+BLE, plugs into phone

**Mid-Range Segment ($1K-$2K USD)**
- **HumanWare Brailliant BI 20X** – 20 cells (20 characters), $2,199 USD, professional grade
- **Freedom Scientific Focus 40** – 40 cells (40 characters), ~$1,700 USD, popular with professionals

**Premium Segment ($2K+ USD)**
- **Orbit Graphiti Plus** – Graphics display, ~$3,500 USD, multi-level Tactuator™

---

### Market Analysis: Price vs Characters

```
Price (USD)
  2500│                    ● Brailliant BI 20X ($2,199 USD, 20 char)
      │
  2000│              ● Focus 40 ($1,700 USD, 40 char)
      │
  1500│
      │
  1000│  ● Orbit Reader 20 ($799 USD, 20 char)
      │
   500│  ● BrailleMe ($515 USD, 20 char)
      │
      │         ★ OUR TARGET ($600 USD, 32 char) ← Market Gap!
     0└─────────────────────────────────────────
       0        10       20       30       40   50
                    Character Count →
```

**Key Insight:** No commercial product in the 25-35 character range at <$1,000 USD price point

**Note:** 1 braille cell = 1 character (8 dots: 6 standard + 2 extended)

---

### Technology Landscape: Piezo Monopoly

**Universal Finding:** 100% of commercial braille displays use **piezoelectric actuators**

| Technology | Voltage | Size | Cost/Cell (BOM) | Lead Time | Market Share |
|------------|---------|------|-----------------|-----------|--------------|
| **Piezo (custom)** | 100-200V | 2-3mm | **$7-20 USD** | 8-12 weeks | **100%** |
| **Solenoid (COTS)** | 5-12V | 4mm+ | **$2-5 USD** | 2-4 weeks | **0%** |

**Market Gap:**
- All vendors use **custom piezo** with 8-12 week lead times
- No COTS-based designs (≤4 week lead time)
- No solenoid-based braille displays exist commercially

---

### Our Competitive Position

**Design Target:**
- **32 cells = 32 characters** (60% more than Orbit Reader 20's 20 chars)
- **$600 USD retail** (between budget and mid-range)
- **$200 USD BOM** ($6.25/cell vs $7.50-20 market)
- **COTS components** (≤4 week lead time) ← **UNIQUE**

**Three Architecture Candidates:**

| Architecture | Actuator | BOM (USD) | Refresh | Market Position |
|--------------|----------|-----------|---------|-----------------|
| **ARCH_SOL_ECO** | 4mm solenoid | **$245** | 2.4s | **Budget leader** |
| **ARCH_PIEZO_ECO** | 2mm piezo | $426 | 1.5s | Mid-range value |
| **ARCH_PIEZO_DLX** | 2mm piezo + BLE | $449 | 1.5s | Premium wireless |

**Key Differentiators:**
1. **COTS mandate** → 2-month timeline (vs 8-12 weeks custom piezo)
2. **Solenoid innovation** → 54% cost savings (ARCH_SOL_ECO only)
3. **32-cell sweet spot** → Fills market gap between 20-cell and 40-cell
4. **AA batteries** → No charger anxiety (vs all rechargeable competitors)

---

## Product Images Available

**Orbit Reader 20:**
- Image URL: https://www.orbitresearch.com/wp-content/uploads/2017/03/Orbit-Reader-20-left-angle-shot-scaled.jpg
- Caption: "World's most affordable at $799 USD (20 characters)"

**HumanWare Brailliant BI 20X:**
- Image URL: https://store.humanware.com/media/catalog/product/cache/af31f082d815f0cbf68dfc31e7356880/b/r/brailliant_bi_20x_-_dsc00285-lr_2.jpg
- Caption: "Professional grade at $2,199 USD (20 characters)"

**Usage:** If slide layout permits, show 2 product photos with captions. Otherwise, use text-only bullet points.

---

## Recommended Slide Flow (30-minute timing)

1. **Intro** (1 min) – Name, background, agenda
2. **Problem Statement** (1 min) – 7.7M blind adults, braille displays too expensive
3. **→ MARKET COMPARISON** (2 min) ← **INSERT HERE**
   - Show price vs cells chart
   - Highlight piezo monopoly
   - Identify market gap (32-cell, <$1K, COTS)
4. **Requirements** (2 min) – PRD-FUNC-001/002/003, NFR constraints
5. **Architecture Options** (3 min) – 3 designs, table comparison
6. ... (continue with trade-offs, EMI, path to production, Q&A)

---

## Key Talking Points (memorize these)

- **"100% of commercial displays use custom piezo"** → establishes technology monopoly
- **"$7.50 to $20 USD per cell BOM"** → shows our $6.25/cell target is aggressive but achievable
- **"No products in 25-35 character range at <$1,000 USD"** → market gap we're targeting
- **"32 characters = 32 cells = 192 dots total"** → 6 dots/char standard + 2 extended
- **"8-12 week lead time for custom piezo"** → why COTS mandate forces innovation
- **"ARCH_SOL_ECO at $245 USD BOM breaks piezo monopoly"** → solenoid innovation saves 54% cost

---

**END OF DRAFT**
