# ARCH_SOL_ECO - Rotary Cam Mechanism Diagram

**Architecture:** ARCH_SOL_ECO (Solenoid Economy with Rotary Cam)
**Document:** Mechanical assembly visualization
**Date:** 2025-10-11

---

## Single Character Assembly (Side View)

This shows ONE braille character (6 dots) using 3 cam layers (2 dots per layer).

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                   ARCH_SOL_ECO - CAM MECHANISM ASSEMBLY                       ║
║                   Single Character (3 Layers, 6 Dots)                         ║
╚═══════════════════════════════════════════════════════════════════════════════╝


┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 1 (DOTS 1 & 4) - Bottom Layer                                        │
└─────────────────────────────────────────────────────────────────────────────┘

                                    User Touch Surface
                                    ═══════════════════
                                    ┌─┐      ┌─┐
                                    │●│      │●│  ← Braille Dots 1 & 4
                                    └┬┘      └┬┘     (1.2mm dia, 0.5mm up)
                                     │        │
                    ┌────────────────┴────────┴────┐
                    │    Housing (ABS molded)      │
                    │    6.2 × 15 × 25mm            │
                    └─┬─────────────┬─────────────┬┘
                      │             │             │
                      │   ┌─────┐   │   ┌─────┐   │
          Springs ────┤   │~~~~│   │   │~~~~│   ├──── Return Springs
         (0.5N force) │   │~~~~│   │   │~~~~│   │     (SS 302, 8mm free)
                      │   └──┬─┘   │   └──┬─┘   │
                      │      │     │      │     │
                    ┌─┴──────┴─────┴──────┴─────┴──┐
                    │   ╔═════╗       ╔═════╗      │
    Pistons ────────┤   ║  │  ║       ║  │  ║      ├─── Piston Rods
   (3mm dia,        │   ║  │  ║       ║  │  ║      │    (ABS, 18mm long)
    0.7mm stroke)   │   ╚══╧══╝       ╚══╧══╝      │    Vertical motion
                    └──────┼─────────────┼──────────┘
                           │             │
                    ┌──────┴─────────────┴──────────┐
                    │   ┌─────┐       ┌─────┐       │
    Linear ─────────┤   │  O  │       │  O  │       ├─── Bushings
    Bushings        │   │  │  │       │  │  │       │    (PTFE-POM, 5mm OD)
   (Guide pistons)  │   └──┼──┘       └──┼──┘       │    Low friction
                    └──────┼─────────────┼──────────┘
                           │             │
                    ╔══════╧═════════════╧══════╗
                    ║      Cam Disc Assembly    ║
                    ║   ┌──────────────────┐    ║
                    ║   │    ╱ ╲          │    ║
    Cam Disc ───────║   │   ●   ●         │    ║──── Rotary Cam
   (12mm dia,       ║   │  ╱     ╲        │    ║     (Delrin POM)
    2mm thick)      ║   │ ●       ●       │    ║     ±45° rotation
                    ║   │  ╲     ╱        │    ║
                    ║   │   ●   ●         │    ║     ● = Piston contact
                    ║   └────┬─────────┬──┘    ║     ╱╲ = Cam profile
                    ╚════════╧═════════╧═══════╝
                             │         │
                           ┌─┴─┐     ┌─┴─┐
          Solenoid ────────│███│     │███│────────── COTS Solenoid
         (4mm dia)         │███│     │███│           (Takaha BS-0420N)
         5VDC, 1mm stroke  │███│     │███│           0.5N force
                           │███│     │███│           2-week lead time
                           └───┘     └───┘           $0.50 ea @ 100 qty
                             ↑         ↑
                      Horizontal actuation (LEFT/RIGHT)
                      Converts to vertical piston motion


┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 2 (DOTS 2 & 5) - Middle Layer (Same as Layer 1, stacked above)       │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 3 (DOTS 3 & 6) - Top Layer (Same as Layer 1, stacked above)          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Cam Mechanism Detail (Exploded View)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║              CAM MECHANISM - PERPENDICULAR ACTUATION PRINCIPLE                ║
╚═══════════════════════════════════════════════════════════════════════════════╝


SIDE VIEW (Actuation Sequence):

┌─────────────────────────────────────────────────────────────────────────────┐
│  STATE 1: REST (Dot Down)                                                    │
└─────────────────────────────────────────────────────────────────────────────┘

                        User Surface
                        ─────────────
                            (flat)

                            Piston
                              │
                        ╔═════╧═════╗
                        ║           ║
                        ║   ┌───┐   ║
                        ║   │ ○ │   ║  ← Cam Disc (0° position)
                        ║   └─┬─┘   ║     Eccentric offset at 6:00
                        ╚═════╧═════╝

                        ┌───────────┐
           Solenoid ────│           │──── Retracted (no voltage)
          (no power)    └───────────┘
                              ↑
                        Spring force pulls cam to rest


┌─────────────────────────────────────────────────────────────────────────────┐
│  STATE 2: ACTUATING (Dot Rising)                                             │
└─────────────────────────────────────────────────────────────────────────────┘

                        User Surface
                        ─────────────
                            ┌─┐
                            │●│ ← Dot rising (0.25mm)
                            └┬┘
                             │
                        ╔════╧════╗
                        ║    │    ║
                        ║  ┌─┴─┐  ║
                        ║  │ ○ │  ║  ← Cam Disc (22° rotation)
                        ║  └───┘  ║     Eccentric offset at 4:00
                        ╚═════════╝
                              ↑
                              │
                        ┌─────┴─────┐
           Solenoid ───│█████████→  │──── Extending (5VDC applied)
          (energized)  └───────────┘

                        Solenoid pushes cam clockwise


┌─────────────────────────────────────────────────────────────────────────────┐
│  STATE 3: FULLY ACTUATED (Dot Up)                                            │
└─────────────────────────────────────────────────────────────────────────────┘

                        User Surface
                        ─────────────
                            ┌─┐
                            │●│ ← Dot fully raised (0.5mm)
                            └┬┘
                             │
                        ╔════╧════╗
                        ║    │    ║
                        ║    │    ║
                        ║  ┌─┴─┐  ║  ← Cam Disc (45° rotation)
                        ║  │ ○ │  ║     Eccentric offset at 3:00
                        ║  └───┘  ║     Maximum piston displacement
                        ╚═════════╝
                              ↑
                              │
                        ┌─────┴─────┐
           Solenoid ───│█████████→  │──── Fully extended (1mm stroke)
          (holding)    └───────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│  STATE 4: RETRACTING (Dot Lowering)                                          │
└─────────────────────────────────────────────────────────────────────────────┘

                        User Surface
                        ─────────────
                            (falling)

                            ↓ Piston retracting
                        ╔═══╧═══╗
                        ║   │   ║
                        ║   │   ║
                        ║ ┌─┴─┐ ║  ← Cam Disc (rotating back)
                        ║ │ ○ │ ║     Spring force returns cam
                        ║ └───┘ ║     to rest position
                        ╚═══════╝
                            ↑
                            │
                        ┌───┴───┐
           Solenoid ───│←──────│──── Retracting (voltage removed)
          (released)   └───────┘

                        Spring pulls solenoid + cam back
```

---

## Top View (Single Character Layout)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     BRAILLE CHARACTER TOP VIEW                                ║
║                     (Standard ADA 703.3 Spacing)                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝


                    ┌─────────────────────────────┐
                    │                             │
                    │   ●       ●                 │  ← Layer 3 (Dots 3 & 6)
                    │  Dot 3   Dot 6              │     Cam discs below surface
                    │   │       │                 │
                    │  2.5mm spacing              │
                    │   ↓       ↓                 │
                    │   ●       ●                 │  ← Layer 2 (Dots 2 & 5)
                    │  Dot 2   Dot 5              │     Cam discs below surface
                    │   │       │                 │
                    │  2.5mm spacing              │
                    │   ↓       ↓                 │
                    │   ●       ●                 │  ← Layer 1 (Dots 1 & 4)
                    │  Dot 1   Dot 4              │     Cam discs below surface
                    │                             │
                    │  └───2.5mm──┘               │  ← Horizontal spacing
                    │   (ADA 703.3)               │
                    └─────────────────────────────┘
                           ↑
                     User touch area
                     (6.2 × 15mm)


     Subsurface (Cam Mechanism Layout):

     ┌───────────────────────────────────────────────────────────────┐
     │                                                                │
     │   [Cam 3] ─── Solenoid 3       [Cam 6] ─── Solenoid 6        │
     │      │                             │                           │
     │   Piston 3                      Piston 6                      │
     │      ↓                             ↓                           │
     │   ┌───┐                         ┌───┐                         │
     │   │ ● │ Dot 3                   │ ● │ Dot 6                   │
     │   └───┘                         └───┘                         │
     │                                                                │
     │   [Cam 2] ─── Solenoid 2       [Cam 5] ─── Solenoid 5        │
     │      │                             │                           │
     │   Piston 2                      Piston 5                      │
     │      ↓                             ↓                           │
     │   ┌───┐                         ┌───┐                         │
     │   │ ● │ Dot 2                   │ ● │ Dot 5                   │
     │   └───┘                         └───┘                         │
     │                                                                │
     │   [Cam 1] ─── Solenoid 1       [Cam 4] ─── Solenoid 4        │
     │      │                             │                           │
     │   Piston 1                      Piston 4                      │
     │      ↓                             ↓                           │
     │   ┌───┐                         ┌───┐                         │
     │   │ ● │ Dot 1                   │ ● │ Dot 4                   │
     │   └───┘                         └───┘                         │
     │                                                                │
     └────────────────────────────────────────────────────────────────┘

     6 Solenoids (horizontal, 4mm dia)
     6 Cam discs (rotary, 12mm dia)
     6 Pistons (vertical, 3mm dia)
     6 Braille dots (1.2mm dia, 0.5mm travel)
```

---

## Motion Conversion Diagram

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║         PERPENDICULAR ACTUATION: HORIZONTAL → ROTARY → VERTICAL               ║
╚═══════════════════════════════════════════════════════════════════════════════╝


    SOLENOID             CAM DISC            PISTON            BRAILLE DOT
   (HORIZONTAL)          (ROTARY)           (VERTICAL)          (VERTICAL)
   ════════════          ════════            ════════          ════════════


      ┌──────┐              ┌─┐                 │                  ●
      │      │              │ │                 │                Raised
      │  ○→  │  ───────→   │ ○│    ───────→    ↑      ───────→  (0.5mm)
      │      │            ╱ └─┘ ╲               │                  │
      └──────┘           ───────────            │                  │
         ↑                    ↑                 ↑                  ↑
      1mm stroke          ±45° rotation     0.7mm stroke      0.5mm travel
      Horizontal          Rotary motion     Vertical lift     User feels dot


    KEY INNOVATION: Rotary cam decouples solenoid size from dot spacing!

    Without cam (direct actuation):
      4mm solenoid → 4mm pitch → 3.5mm spacing → VIOLATES ADA 703.3 ❌

    With cam (perpendicular actuation):
      4mm solenoid → cam rotation → 2.5mm spacing → MEETS ADA 703.3 ✓
```

---

## Key Dimensions & Specifications

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        COMPONENT SPECIFICATIONS                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│  COMPONENT              │  DIMENSION        │  MATERIAL      │  COST         │
├─────────────────────────┼───────────────────┼────────────────┼───────────────┤
│  Solenoid (COTS)        │  4mm dia × 10mm   │  Steel + Cu    │  $0.50 ea     │
│  Cam Disc               │  12mm dia × 2mm   │  Delrin POM    │  $0.15 ea     │
│  Piston Rod             │  3mm dia × 18mm   │  ABS           │  $0.10 ea     │
│  Linear Bushing         │  5mm OD × 3.1mm ID│  PTFE-POM      │  $0.08 ea     │
│  Compression Spring     │  8mm free length  │  SS 302        │  $0.02 ea     │
│  Cam Housing            │  6.2×15×25mm      │  ABS           │  $0.50 ea     │
│  Braille Dot            │  1.2mm dia        │  ABS (surface) │  (integrated) │
└─────────────────────────┴───────────────────┴────────────────┴───────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  MOTION SPECIFICATIONS                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  Solenoid Stroke        │  1.0mm (horizontal)                               │
│  Cam Rotation           │  ±45° (90° total range)                           │
│  Piston Travel          │  0.7mm (vertical)                                 │
│  Dot Height             │  0.5mm above surface (ADA spec: 0.36-0.9mm)       │
│  Actuation Force        │  0.5N (solenoid output)                           │
│  Tactile Force          │  ~0.3N (at fingertip)                             │
│  Response Time          │  <10ms (full actuation cycle)                     │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  SPACING COMPLIANCE (ADA 703.3)                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  Horizontal Spacing     │  2.5mm (dot center to dot center)     ✓ COMPLIANT │
│  Vertical Spacing       │  2.5mm (dot center to dot center)     ✓ COMPLIANT │
│  Character Spacing      │  6.1mm (min per ADA 703.3)            ✓ COMPLIANT │
│  Dot Diameter           │  1.2mm (spec: 1.2-1.5mm)              ✓ COMPLIANT │
│  Dot Height             │  0.5mm (spec: 0.36-0.9mm)             ✓ COMPLIANT │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Assembly BOM (Single Character)

**Quantity:** Per character (32 characters × 6 components = 192 total units)

| Line | Component | Qty/Char | Qty/Device | Unit Price | Line Total |
|------|-----------|----------|------------|------------|------------|
| 1 | Solenoid (BS-0420N) | 6 | 192 | $0.50 | $96.00 |
| 2 | Cam Disc | 6 | 192 | $0.15 | $28.80 |
| 3 | Piston Rod | 6 | 192 | $0.10 | $19.20 |
| 4 | Linear Bushing | 6 | 192 | $0.08 | $15.36 |
| 5 | Compression Spring | 6 | 192 | $0.02 | $3.84 |
| 6 | Cam Housing (shared) | 1 | 32 | $0.50 | $16.00 |
| **TOTAL (Actuator Subsystem)** | | | | | **$179.20** |

**Notes:**
- Cam housing holds 6 cam assemblies (one per dot)
- Production costs assume 10K+ volume with hard tooling
- Pilot costs ~2× higher (proto molds, lower volume)

---

## Advantages of Cam Mechanism

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ADVANTAGE                           │  BENEFIT                              │
├──────────────────────────────────────┼───────────────────────────────────────┤
│  Perpendicular actuation             │  Decouples solenoid size from spacing │
│  COTS solenoids (4mm)                │  2-week lead time, global availability│
│  Low voltage (5VDC)                  │  Simpler power supply, safer          │
│  Proven technology (automotive cams) │  Low technical risk                   │
│  50% cost savings vs piezo           │  $216 vs $436 production BOM          │
│  Injection moldable                  │  High-volume manufacturing ready      │
│  Standard braille spacing            │  Muscle memory preservation (ADA)     │
└──────────────────────────────────────┴───────────────────────────────────────┘
```

---

## Manufacturing Notes

**Prototype Phase:**
- 3D print cam discs (SLA resin, ±0.1mm tolerance)
- 3D print housing (SLS nylon)
- Validate cam profile with hand testing

**Pilot Phase (100 units):**
- Proto molds (aluminum) for cam/piston/bushing
- Injection molding (±0.2mm tolerance)
- Assembly jigs for alignment

**Production Phase (10K+ units):**
- Hard tooling (steel molds)
- Automated assembly line
- In-line quality control (vision inspection)

---

**End of Diagram**
