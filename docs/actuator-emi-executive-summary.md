# Actuator EMI Analysis - Executive Summary

**Document:** actuator-emi-design-analysis.md (46KB, 1597 lines, 8 parts)
**Author:** Spencer Barrett
**Date:** 2025-10-15
**Purpose:** 1-page summary for quick review + foundation for presentation slides

---

## The Core Problem

**30mm piezo cantilever = Quarter-wavelength monopole antenna @ 1.67 GHz**

```
Physics: f_resonant = c / (4 × L × √ε_r) = 1.67 GHz (over PCB)
Reality: 192 actuators = 192 radiating antennas @ GHz frequencies
Impact: FCC Part 15B most restrictive band (54 dBµV/m @ 3m)
```

**Key Insight:** 30mm is NOT "just a wire" at GHz — it's a resonant antenna!

---

## The Cost Trade-off

| Metric | Solenoid (ARCH_SOL_ECO) | Piezo (ARCH_PIEZO_ECO/DLX) |
|--------|-------------------------|----------------------------|
| **EMI Frequency** | <10 MHz (LC ringing) | **500 MHz - 1 GHz** (antenna) |
| **Antenna Effect** | None (4mm << λ) | **30mm = λ/4 resonance** |
| **Mitigation Cost** | **$4.32** | **$10.84** (2.5× premium) |
| **Cert Risk** | LOW (10% fail) | HIGH (50% fail, +2 weeks) |
| **Rework Cost** | +$1.3K (expected) | **+$6.5K** (expected) |

**Bottom Line:** Piezo pays **2.5× EMI cost** for 1.6× faster refresh + zero hold power

---

## The Solution: 5-Layer Defense

**Cumulative EMI Reduction: +84 dB OVER → 21 dB compliance margin**

| Layer | Technique | dB Reduction | Cost/Unit |
|-------|-----------|--------------|-----------|
| **1. Firmware** | Sequential firing (8-way) | -28 dB | **$0** |
| | Slew-rate limiting (1ms) | -40 dB | **$0** |
| **2. PCB** | Twisted pairs + ferrite beads | -35 dB | $5.84 |
| **3. Enclosure** | Shielded aluminum + gaskets | -30 dB | $4.00 |
| **4. Testing** | Pre-compliance (Week 5-6) | N/A | $2.5K |

**Critical Insight:** Firmware alone (sequential + slew-rate) = **68 dB reduction at $0 hardware cost!**

This is the software-first EE approach: exploit the 2-second refresh requirement to slow down rise times and sequence actuators → massive EMI reduction before any hardware cost.

---

## The Risk Quantification

**Schedule Impact (if pre-compliance fails):**
- Root cause analysis: 3-5 days
- PCB re-spin: 2-3 weeks (layout + fab + assembly)
- Re-test: 1 week
- **Total delay per iteration: 4-6 weeks**

**Certification Risk by Architecture:**
- ARCH_SOL_ECO: 10% fail rate, +0.4 weeks expected delay, +$1.3K expected cost
- ARCH_PIEZO_ECO: 50% fail rate, +2 weeks expected delay, +$6.5K expected cost
- ARCH_PIEZO_DLX: 60% fail rate (+ BLE coexistence), +3 weeks expected, +$8K expected

**Risk Mitigation:**
- Pre-compliance testing Week 5-6 ($2.5K, semi-anechoic chamber)
- Go/No-Go: Pass with 6 dB margin → proceed to FCC certification
- Contingency budget: +$6.5K + 2 weeks for piezo architectures

---

## Key Numbers (Memorize for Q&A)

**Antenna Physics:**
- λ/4 @ 1.67 GHz = 30mm (over PCB with ε_r=2.2)
- 192 actuators → √192 = 13.9 → 20×log₁₀(13.9) = 22.8 dB radiation gain

**EMI Budget:**
- Baseline (no mitigation): +84 dB OVER FCC limit ❌
- Sequential firing: -28 dB (√24 reduction from 192→8 parallel)
- Slew-rate limiting: -40 dB (10µs → 1ms rise time, f_max: 35kHz → 350Hz)
- PCB mitigation: -35 dB (twisted pairs + ferrite beads)
- Shielded enclosure: -30 dB (SE=30dB @ 1 GHz, aluminum + gasket)
- **Final margin: 21 dB compliance margin** ✅

**Fourier Relationship (explains 40dB slew-rate reduction):**
- f_max ≈ 0.35 / τ_rise
- 10µs → 35 kHz, 1ms → 350 Hz
- EMI reduction: 20 × log₁₀(1ms / 10µs) = 40 dB

**FCC Part 15B Class B Limit:**
- > 960 MHz: 54 dBµV/m @ 3m (most restrictive for GHz piezo)
- Pre-compliance testing must focus on 500 MHz - 2 GHz range

---

## Architecture Recommendation

**Portfolio Approach:** Proceed with all 3 architectures in concept evaluation

| Architecture | Best For | EMI Mitigation | Risk Level |
|--------------|----------|----------------|------------|
| **ARCH_SOL_ECO** | Budget + Low risk | $4.32 | **LOW** ✅ |
| **ARCH_PIEZO_ECO** | Performance + Desktop | $10.84 | HIGH ⚠️ |
| **ARCH_PIEZO_DLX** | Premium + Wireless | $12.84 | VERY HIGH ⚠️⚠️ |

**Trade-off:** Piezo pays 2.5× EMI premium for:
- ✅ 1.6× faster refresh (1.5s vs 2.4s)
- ✅ Zero hold power (50% longer battery life)
- ⚠️ HIGH certification risk (50% fail, +2 weeks rework)

**Honest Assessment:** No silver bullets. Present trade-offs, let stakeholders decide based on priorities.

---

## Demonstrates Senior EE Skills

✅ **Antenna theory:** λ/4 resonance, far-field radiation, Q-factor amplification
✅ **FCC Part 15B compliance:** Quantitative EMI budget, regulatory limits
✅ **Mitigation techniques:** Shielding SE, ferrite beads, PCB design rules
✅ **Signal processing:** Fourier analysis, f_max ≈ 0.35 / τ_rise relationship
✅ **Risk quantification:** Cost, schedule, failure probability (not hand-waving)
✅ **Trade-off analysis:** No "best" solution, context-dependent decisions

---

## How This Maps to Presentation Slides

**Main Presentation (source/presentation-slides.md):**
- **Slide 33:** "EMI Compliance Trade-offs" → Uses "Core Problem" + "Cost Trade-off" tables
- **Slide 34:** "EMI Mitigation Strategy" → Uses "5-Layer Defense" table + critical insight
- **Speaker notes:** Reference full document for technical backup

**Appendix Slides (A-G):**
- **Appendix A:** Antenna physics deep-dive (λ/4 calculation, 192 radiators)
- **Appendix B:** Detailed EMI budget table (+84 dB → +21 dB margin)
- **Appendix C:** 4-layer defense implementation details
- **Appendix D:** Cost & schedule impact comparison
- **Appendix E:** Fourier analysis math (f_max ≈ 0.35 / τ_rise)
- **Appendix F:** BLE coexistence risk (ARCH_PIEZO_DLX specific)
- **Appendix G:** FCC Part 15B regulatory limits

**Leave-Behind Document:** This executive summary (1 page) + full analysis (46KB) available on request

---

## For Interview Q&A

**If asked about EMI:**
1. Open with physics: "30mm piezo is a quarter-wavelength monopole at 1.67 GHz"
2. Quantify the problem: "+84 dB over FCC limit without mitigation"
3. Show the solution: "5-layer defense, firmware-first approach reduces 68 dB at zero cost"
4. Acknowledge the trade-off: "Piezo pays 2.5× cost premium for performance benefits"
5. Demonstrate risk management: "Pre-compliance testing Week 5-6, 6 dB margin go/no-go"

**If asked "Which architecture is best?"**
→ "Depends on your priorities. Solenoid wins on cost + risk, piezo wins on performance, wireless is only option for mobility. Here's the decision framework..." (flip to slide 36)

**If asked for technical depth:**
→ "Let me show you the detailed EMI budget analysis..." (flip to Appendix B)

---

**END OF EXECUTIVE SUMMARY**

For full analysis with 8-part deep-dive (fundamentals, solenoid analysis, piezo analysis, comparison, cost breakdown, testing strategy, recommendations, implementation details), see: `docs/actuator-emi-design-analysis.md`
