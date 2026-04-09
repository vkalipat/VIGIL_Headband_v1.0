# VIGIL

Low-cost continuous patient monitoring headband. ~$30 BOM.

## What It Does

Monitors 4 vital signs simultaneously from a single flex PCB worn on the forehead:

| Vital Sign | Sensor | Method |
|-----------|--------|--------|
| Heart Rate | LIS3DH (U2) | Ballistocardiography — skull micro-vibrations from heartbeat |
| Temperature | TMP117 (U3) | Direct skin contact, +/-0.1C accuracy |
| Respiratory Rate | ICS-43434 (U4) | Bone-conducted breathing sounds via MEMS mic |
| Pulse Waveform | PVDF + AD8606 (U5) | Bilateral piezoelectric strips on temporal arteries |

Data transmits over BLE 5.0 (nRF52840) to a phone/tablet.

## Specs

| Spec | Value |
|------|-------|
| Dimensions | 185mm x 35mm |
| PCB | 2-layer Flex (polyimide) |
| Thickness | 0.11mm |
| Finish | ENIG |
| Copper | 1/3 oz |
| Battery | 500mAh LiPo (USB-C rechargeable) |
| Battery Life | ~7-14 days (duty cycled) |
| Wireless | BLE 5.0 via nRF52840 |

## Repository Structure

```
hardware/
  gerbers/          # Production gerber files + drill file
  bom/              # BOM and CPL (original + corrected versions)
  kicad/            # KiCad project (schematic + board layout)
docs/
  SOLDERING_GUIDE.md  # Hand-soldering instructions for unpopulated parts
```

## BOM Corrections (v1.0)

The original BOM had several wrong LCSC part numbers. Use the corrected files:

| Ref | Issue | Original LCSC | Corrected LCSC |
|-----|-------|---------------|----------------|
| U2 | Wrong part (was inductor!) | C9900 | C15134 |
| U3 | Unmatched | C134053 | C699536 |
| U4 | Unmatched | C94935 | C5656610 |
| U5 | Unmatched | C40795 | C408833 |
| U6 | Wrong part (was resistor!) | C477640 | C2071859 |
| U7 | Unmatched | C15580 | C140288 |
| D1 | Out of stock | C72043 | C965794 |
| L1 | Wrong value (10uH not 2.2uH) | C1046 | C107322 |

## Parts Requiring Hand Soldering

JLCPCB could not assemble these due to footprint mismatches or pad size issues:

| Ref | Part | Reason | Method |
|-----|------|--------|--------|
| U6 | TPS62840 | Wrong LCSC mapping | Hot air reflow |
| U4 | ICS-43434 | Footprint mismatch | Hot air reflow |
| Y1 | 32.768kHz crystal | Package size mismatch (3215 vs 2012) | Soldering iron |
| J1 | USB-C connector | Footprint mismatch | Soldering iron |
| J2 | JST PH header | Pads not found | Soldering iron |

See `docs/SOLDERING_GUIDE.md` for detailed instructions.

## Ordering

1. Upload `hardware/gerbers/` to JLCPCB
2. Select: Flex PCB, 2 layers, 0.11mm, ENIG, polyimide
3. Use `hardware/bom/VIGIL_v1.0_BOM_corrected.csv` for BOM
4. Use `hardware/bom/VIGIL_v1.0_CPL_corrected.csv` for placement

## KiCad Project

Open `hardware/kicad/VIGIL_v1.0.kicad_pro` in KiCad 8.0+ to see:
- Component placement layout with all footprints positioned correctly
- 106 stitching vias visible
- Board outline (185x35mm)
- Hand-solder parts labeled with `[HAND SOLDER]`

## License

CERN-OHL-P-2.0
