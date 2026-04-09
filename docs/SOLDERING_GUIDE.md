# VIGIL v1.0 — Hand Soldering Guide

## Parts NOT assembled by JLCPCB (you must solder these)

| # | Ref | Part | Package | Method | Difficulty |
|---|-----|------|---------|--------|------------|
| 1 | U6 | TPS62840 buck converter | WSON-8 (2x2mm) | Hot air + solder paste | Hard |
| 2 | Y1 | 32.768kHz crystal | 2012 (2x1.2mm) | Iron | Easy |
| 3 | J2 | JST PH battery header | Through-hole 2-pin | Iron | Easy |
| 4 | J1 | USB-C connector | GCT USB4105-GF-A | Iron (drag solder) | Medium |
| 5 | U4 | ICS-43434 MEMS mic | LGA-6 (3.5x2.65mm) | Hot air + solder paste | Hard |
| 6 | PVDF | 2x LDT0-028K piezo strips | Solder tabs | Iron | Easy |

## Soldering Order (do in this sequence)

### Step 1: U6 — TPS62840 (Hot Air)
**Without this, nothing gets power.**

- Location: Center-right of component island, between L1 and C2
- Position: X=51.79mm, Y=23.42mm, rotated 90deg
- Pin 1: Look for dot on chip, match to board marking

**Procedure:**
1. Apply flux to all 8 pads + center ground pad
2. Apply solder paste (thin dots on each pad, larger blob on center pad)
3. Place chip with tweezers, align pin 1 under microscope
4. Hot air 300C, 30-40% airflow, 2cm distance, slow circles
5. Watch for paste going shiny (~30 sec) — that's reflow
6. Remove heat, let cool 30 sec
7. Inspect under microscope for bridges

### Step 2: Y1 — Crystal (Iron)
**Without this, nRF52840 won't boot.**

- Location: Upper-right area, near board edge, X=47.82mm, Y=31.24mm
- No polarity — either orientation works
- Package: 2.0 x 1.2mm, two pads

**Procedure:**
1. Flux both pads
2. Tin one pad (small dome of solder)
3. Hold crystal with tweezers, reflow tinned pad, slide crystal in
4. Solder second pad
5. Total time: ~30 seconds

### Step 3: J2 — JST Battery Header (Iron)
**Same as keyboard switch soldering.**

- Location: Right side of component island, X=56.52mm, Y=23.26mm
- Through-hole, 2 pins, 2mm pitch
- Check polarity marking on board (+/-)

**Procedure:**
1. Push pins through holes from top
2. Solder from back side
3. Done

### Step 4: J1 — USB-C Connector (Iron)
**Drag solder technique.**

- Location: Top-right edge of board, X=57.15mm, Y=33.74mm
- Port opening faces OFF the board edge
- 4 large mounting tabs + rows of signal pins

**Procedure:**
1. Align connector — mounting tabs sit on 4 large rectangular pads
2. Tack ONE mounting tab to hold it in place
3. Check alignment under microscope — every signal pin on its own pad
4. Solder remaining 3 mounting tabs
5. FLOOD signal pins with flux
6. Small blob of solder on iron tip
7. Drag slowly across pin row in one smooth motion
8. Inspect for bridges — fix with solder wick if needed

### Step 5: U4 — ICS-43434 Microphone (Hot Air)
**Trickiest part. Do last when you have confidence.**

First, desolder from Adafruit breakout:
1. Flux around chip on breakout board
2. Heat from BACK of breakout at 280C, low airflow (25%)
3. After 30-40 sec, chip slides off with tweezers
4. Clean chip pads with solder wick

Then solder onto VIGIL board:
- Location: Near nRF52840, X=48.55mm, Y=27.70mm
- Pin 1: Look for dot marking

**CRITICAL: Do NOT let solder paste enter the sound port hole on the bottom of the chip. If blocked, mic is dead.**

1. Flux U4 pads on VIGIL board
2. Apply minimal solder paste — keep paste AWAY from sound port area
3. Place chip, align under microscope
4. Hot air 300C, slow circles
5. Let cool, inspect

### Step 6: PVDF Sensors (Iron)
**Two strips, one at each temple end.**

- Temple 1 (component island side): Pads near U5
- Temple 2 (flex tail end): Pads at far right end of board

**Procedure:**
1. Tin pads on PCB
2. Tin solder tabs on LDT0-028K
3. Hold tab to pad with tweezers, touch iron to join
4. Repeat for second tab
5. Add flexible glue over joints for strain relief

## Critical Warnings

- **DO NOT touch any JLCPCB-assembled parts** — they're already soldered correctly
- **U6 pin 1 orientation** — wrong rotation = shorted regulator = dead board
- **U4 sound port** — solder in the port = dead microphone
- **Flex PCB handling** — don't bend sharply in the component area
- **Check polarity** on J2 before plugging in battery — reversed = damaged BQ24072
- **You have 5 boards** — use board #1 as practice, board #2 as your real build
