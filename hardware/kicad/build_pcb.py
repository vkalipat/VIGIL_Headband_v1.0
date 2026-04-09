"""Generate a syntactically correct KiCad 8 .kicad_pcb file for VIGIL v1.0."""
import uuid

def uid():
    return str(uuid.uuid4())

# Components with corrected Y positions (Y_new = 35 - Y_original)
components = [
    {"ref": "U1",  "val": "nRF52840-QIAA",  "fp": "QFN-73-1EP_7x7mm",     "x": 42.7735, "y": 28.0358, "rot": 90,  "pads": [("EP", "smd", "rect", 0, 0, 5.3, 5.3)], "body": (7.0, 7.0), "hand": False},
    {"ref": "U2",  "val": "LIS3DHTR",        "fp": "LGA-16_3x3mm",          "x": 48.7267, "y": 23.1786, "rot": 0,   "pads": [], "body": (3.0, 3.0), "hand": False},
    {"ref": "U3",  "val": "TMP117AIDRVR",    "fp": "WSON-6_2x2mm",          "x": 45.3339, "y": 22.6866, "rot": 270, "pads": [("EP", "smd", "rect", 0, 0, 0.65, 1.4)], "body": (2.0, 2.0), "hand": False},
    {"ref": "U4",  "val": "ICS-43434",       "fp": "LGA-6_3.5x2.65mm",      "x": 48.5477, "y": 27.7049, "rot": 90,  "pads": [], "body": (3.5, 2.65), "hand": True},
    {"ref": "U5",  "val": "AD8606ARMZ",      "fp": "MSOP-8_3x3mm",          "x": 42.0479, "y": 18.8929, "rot": 0,   "pads": [], "body": (3.0, 3.0), "hand": False},
    {"ref": "U6",  "val": "TPS62840DLCR",    "fp": "WSON-8_2x2mm",          "x": 51.793,  "y": 23.4245, "rot": 90,  "pads": [("EP", "smd", "rect", 0, 0, 0.9, 1.6)], "body": (2.0, 2.0), "hand": True},
    {"ref": "U7",  "val": "BQ24072RGTR",     "fp": "QFN-16_3x3mm",          "x": 57.3946, "y": 26.754,  "rot": 270, "pads": [("EP", "smd", "rect", 0, 0, 1.68, 1.68)], "body": (3.0, 3.0), "hand": False},
    {"ref": "Y1",  "val": "32.768kHz",       "fp": "Crystal_SMD_2012",       "x": 47.8207, "y": 31.2425, "rot": 90,  "pads": [("1","smd","rect",-0.75,0,0.6,0.9),("2","smd","rect",0.75,0,0.6,0.9)], "body": (2.0, 1.2), "hand": True},
    {"ref": "D1",  "val": "LED_GRN",         "fp": "LED_0402",               "x": 24.8559, "y": 23.369,  "rot": 0,   "pads": [("1","smd","rect",-0.48,0,0.56,0.62),("2","smd","rect",0.48,0,0.56,0.62)], "body": (1.0, 0.5), "hand": False},
    {"ref": "L1",  "val": "2.2uH",           "fp": "L_0805",                 "x": 52.1559, "y": 20.8963, "rot": 180, "pads": [("1","smd","rect",-0.95,0,0.7,1.0),("2","smd","rect",0.95,0,0.7,1.0)], "body": (2.0, 1.25), "hand": False},
    {"ref": "J1",  "val": "USB_C",           "fp": "USB_C_GCT_USB4105",      "x": 57.1544, "y": 33.7386, "rot": 0,   "pads": [], "body": (8.94, 7.32), "hand": True},
    {"ref": "J2",  "val": "BAT_JST_PH",      "fp": "JST_PH_B2B-PH-K",       "x": 56.5234, "y": 23.2587, "rot": 0,   "pads": [("1","thru_hole","circle",-1,0,1.2,1.2,0.75),("2","thru_hole","circle",1,0,1.2,1.2,0.75)], "body": (5.0, 4.2), "hand": True},
    {"ref": "R1",  "val": "4.7k",            "fp": "R_0402",                  "x": 51.5942, "y": 19.0832, "rot": 0,   "pads": [("1","smd","rect",-0.48,0,0.56,0.62),("2","smd","rect",0.48,0,0.56,0.62)], "body": (1.0, 0.5), "hand": False},
    {"ref": "R2",  "val": "4.7k",            "fp": "R_0402",                  "x": 46.0382, "y": 20.2939, "rot": 90,  "pads": [("1","smd","rect",-0.48,0,0.56,0.62),("2","smd","rect",0.48,0,0.56,0.62)], "body": (1.0, 0.5), "hand": False},
    {"ref": "C1",  "val": "100nF",           "fp": "C_0402",                  "x": 46.0392, "y": 18.1347, "rot": 270, "pads": [("1","smd","rect",-0.48,0,0.56,0.62),("2","smd","rect",0.48,0,0.56,0.62)], "body": (1.0, 0.5), "hand": False},
    {"ref": "C2",  "val": "100nF",           "fp": "C_0402",                  "x": 51.5942, "y": 25.5118, "rot": 0,   "pads": [("1","smd","rect",-0.48,0,0.56,0.62),("2","smd","rect",0.48,0,0.56,0.62)], "body": (1.0, 0.5), "hand": False},
    {"ref": "C3",  "val": "10uF",            "fp": "C_0805",                  "x": 54.3729, "y": 24.4361, "rot": 90,  "pads": [("1","smd","rect",-0.95,0,0.7,1.0),("2","smd","rect",0.95,0,0.7,1.0)], "body": (2.0, 1.25), "hand": False},
    {"ref": "C4",  "val": "10uF",            "fp": "C_0805",                  "x": 48.5516, "y": 20.2131, "rot": 0,   "pads": [("1","smd","rect",-0.95,0,0.7,1.0),("2","smd","rect",0.95,0,0.7,1.0)], "body": (2.0, 1.25), "hand": False},
    {"ref": "C5",  "val": "12pF",            "fp": "C_0402",                  "x": 28.6945, "y": 25.2939, "rot": 90,  "pads": [("1","smd","rect",-0.48,0,0.56,0.62),("2","smd","rect",0.48,0,0.56,0.62)], "body": (1.0, 0.5), "hand": False},
    {"ref": "C6",  "val": "12pF",            "fp": "C_0402",                  "x": 52.5421, "y": 27.4368, "rot": 90,  "pads": [("1","smd","rect",-0.48,0,0.56,0.62),("2","smd","rect",0.48,0,0.56,0.62)], "body": (1.0, 0.5), "hand": False},
]

# Vias from drill file
vias = [
    (1.124,1.124),(9.251,1.124),(17.378,1.124),(25.505,1.124),(33.633,1.124),
    (41.76,1.124),(49.887,1.124),(58.014,1.124),(66.141,1.124),(74.269,1.124),
    (82.396,1.124),(90.523,1.124),(98.65,1.124),(106.777,1.124),(114.905,1.124),
    (123.032,1.124),(131.159,1.124),(139.286,1.124),(147.414,1.124),(155.541,1.124),
    (163.668,1.124),(171.795,1.124),
    (1.124,33.875),(9.251,33.875),(17.378,33.875),(25.505,33.875),(33.633,33.875),
    (41.76,33.875),(49.887,33.875),(58.014,33.875),(66.141,33.875),(74.269,33.875),
    (82.396,33.875),(90.523,33.875),(98.65,33.875),(106.777,33.875),(114.905,33.875),
    (123.032,33.875),(131.159,33.875),(139.286,33.875),(147.414,33.875),(155.541,33.875),
    (163.668,33.875),(171.795,33.875),(179.922,33.875),
    (183.875,5.319),(183.875,13.446),(183.875,21.574),
    (1.124,9.23),(1.124,17.357),(1.124,25.484),
    (47.073,22.051),(49.578,24.516),(51.604,18.425),(45.724,24.169),
    (46.624,21.342),(29.419,24.879),(46.906,30.576),
    (13.444,16.231),(21.569,16.205),(29.696,16.205),(37.823,16.205),
    (43.687,10.74),(71.784,10.104),(66.037,15.85),(60.29,21.597),
    (18.206,23.717),(10.079,23.717),(50.458,17.618),(27.596,23.955),(39.356,25.722),
    (98.197,9.251),(91.901,13.962),(83.807,13.916),(76.794,16.587),(71.047,22.334),
    (80.134,25.748),(88.261,25.748),(96.388,25.748),(104.516,25.748),
    (112.643,25.748),(120.77,25.748),(128.897,25.748),(137.024,25.748),
    (145.152,25.748),(153.279,25.748),(161.406,25.748),(169.533,25.748),
    (175.748,15.708),
    (165.951,9.251),(157.824,9.251),(149.696,9.251),(141.569,9.251),
    (133.442,9.251),(125.315,9.251),(117.188,9.251),(109.06,9.251),
    (101.878,17.621),(110.005,17.621),(118.132,17.621),(126.26,17.621),
    (134.387,17.621),(142.514,17.621),(150.641,17.621),(158.768,17.621),(166.896,17.621),
]

lines = []
lines.append('(kicad_pcb')
lines.append('  (version 20240108)')
lines.append('  (generator "pcbnew")')
lines.append('  (generator_version "8.0")')
lines.append(f'  (general (thickness 0.11) (legacy_teardrops no))')
lines.append('  (paper "A3")')

# Layers
lines.append('  (layers')
lines.append('    (0 "F.Cu" signal)')
lines.append('    (31 "B.Cu" signal)')
lines.append('    (32 "B.Adhes" user "B.Adhesive")')
lines.append('    (33 "F.Adhes" user "F.Adhesive")')
lines.append('    (34 "B.Paste" user)')
lines.append('    (35 "F.Paste" user)')
lines.append('    (36 "B.SilkS" user "B.Silkscreen")')
lines.append('    (37 "F.SilkS" user "F.Silkscreen")')
lines.append('    (38 "B.Mask" user "B.Mask")')
lines.append('    (39 "F.Mask" user "F.Mask")')
lines.append('    (44 "Edge.Cuts" user)')
lines.append('    (46 "B.CrtYd" user "B.Courtyard")')
lines.append('    (47 "F.CrtYd" user "F.Courtyard")')
lines.append('    (48 "B.Fab" user "B.Fabrication")')
lines.append('    (49 "F.Fab" user "F.Fabrication")')
lines.append('  )')

# Setup
lines.append('  (setup')
lines.append('    (pad_to_mask_clearance 0.05)')
lines.append('    (allow_soldermask_bridges_in_footprints no)')
lines.append('    (pcbplotparams')
lines.append('      (layerselection 0x00010fc_ffffffff)')
lines.append('      (plot_on_all_layers_selection 0x0000000_00000000)')
lines.append('      (disableapertmacros no)')
lines.append('      (usegerberextensions no)')
lines.append('      (usegerberattributes yes)')
lines.append('      (usegerberadvancedattributes yes)')
lines.append('      (creategerberjobfile yes)')
lines.append('      (dashed_line_dash_ratio 12.000000)')
lines.append('      (dashed_line_gap_ratio 3.000000)')
lines.append('      (svgprecision 4)')
lines.append('      (plotframeref no)')
lines.append('      (viasonmask no)')
lines.append('      (mode 1)')
lines.append('      (useauxorigin no)')
lines.append('      (hpglpennumber 1)')
lines.append('      (hpglpenspeed 20)')
lines.append('      (hpglpendiameter 15.000000)')
lines.append('      (pdf_front_fp_property_popups yes)')
lines.append('      (pdf_back_fp_property_popups yes)')
lines.append('      (dxfpolygonmode yes)')
lines.append('      (dxfimperialunits yes)')
lines.append('      (dxfusepcbnewfont yes)')
lines.append('      (psnegative no)')
lines.append('      (psa4output no)')
lines.append('      (plotreference yes)')
lines.append('      (plotvalue yes)')
lines.append('      (plotfptext yes)')
lines.append('      (plotinvisibletext no)')
lines.append('      (sketchpadsonfab no)')
lines.append('      (subtractmaskfromsilk no)')
lines.append('      (outputformat 1)')
lines.append('      (mirror no)')
lines.append('      (drillshape 1)')
lines.append('      (scaleselection 1)')
lines.append('      (outputdirectory "")')
lines.append('    )')
lines.append('  )')

# Nets
lines.append('  (net 0 "")')
lines.append('  (net 1 "GND")')
lines.append('  (net 2 "+3V3")')
lines.append('  (net 3 "VBAT")')
lines.append('  (net 4 "VBUS")')
lines.append('  (net 5 "SDA")')
lines.append('  (net 6 "SCL")')

# Board outline
lines.append(f'  (gr_line (start 0 0) (end 185 0) (stroke (width 0.15) (type default)) (layer "Edge.Cuts") (uuid "{uid()}"))')
lines.append(f'  (gr_line (start 185 0) (end 185 35) (stroke (width 0.15) (type default)) (layer "Edge.Cuts") (uuid "{uid()}"))')
lines.append(f'  (gr_line (start 185 35) (end 0 35) (stroke (width 0.15) (type default)) (layer "Edge.Cuts") (uuid "{uid()}"))')
lines.append(f'  (gr_line (start 0 35) (end 0 0) (stroke (width 0.15) (type default)) (layer "Edge.Cuts") (uuid "{uid()}"))')

# Annotation lines on F.Fab
lines.append(f'  (gr_rect (start 20 0) (end 62 35) (stroke (width 0.2) (type dash)) (fill none) (layer "F.Fab") (uuid "{uid()}"))')
lines.append(f'  (gr_text "COMPONENT ISLAND" (at 41 -2) (layer "F.Fab") (uuid "{uid()}")')
lines.append(f'    (effects (font (size 2 2) (thickness 0.3)))')
lines.append(f'  )')
lines.append(f'  (gr_text "FLEX TAIL" (at 120 17.5) (layer "F.Fab") (uuid "{uid()}")')
lines.append(f'    (effects (font (size 2 2) (thickness 0.3)))')
lines.append(f'  )')
lines.append(f'  (gr_text "PVDF SENSOR PADS" (at 178 17.5) (layer "F.Fab") (uuid "{uid()}")')
lines.append(f'    (effects (font (size 1.5 1.5) (thickness 0.2)))')
lines.append(f'  )')
lines.append(f'  (gr_text "BLE ANTENNA" (at 10 17.5) (layer "F.Fab") (uuid "{uid()}")')
lines.append(f'    (effects (font (size 1.5 1.5) (thickness 0.2)))')
lines.append(f'  )')

# Footprints
for c in components:
    ref = c["ref"]
    val = c["val"]
    if c["hand"]:
        val += " [HAND SOLDER]"
    fp = c["fp"]
    x, y, rot = c["x"], c["y"], c["rot"]
    bw, bh = c["body"]

    lines.append(f'  (footprint "{fp}"')
    lines.append(f'    (layer "F.Cu")')
    lines.append(f'    (uuid "{uid()}")')
    lines.append(f'    (at {x} {y} {rot})')

    # Reference on silkscreen
    lines.append(f'    (property "Reference" "{ref}"')
    lines.append(f'      (at 0 {-(bh/2 + 1.5)} {0})')
    lines.append(f'      (layer "F.SilkS")')
    lines.append(f'      (uuid "{uid()}")')
    lines.append(f'      (effects (font (size 1 1) (thickness 0.15)))')
    lines.append(f'    )')

    # Value on fab
    lines.append(f'    (property "Value" "{val}"')
    lines.append(f'      (at 0 {bh/2 + 1.5} {0})')
    lines.append(f'      (layer "F.Fab")')
    lines.append(f'      (uuid "{uid()}")')
    lines.append(f'      (effects (font (size 0.8 0.8) (thickness 0.12)))')
    lines.append(f'    )')

    # Fab layer body outline
    lines.append(f'    (fp_rect (start {-bw/2} {-bh/2}) (end {bw/2} {bh/2})')
    lines.append(f'      (stroke (width 0.1) (type default))')
    lines.append(f'      (fill none)')
    lines.append(f'      (layer "F.Fab")')
    lines.append(f'      (uuid "{uid()}")')
    lines.append(f'    )')

    # Courtyard
    cw, ch = bw/2 + 0.25, bh/2 + 0.25
    lines.append(f'    (fp_rect (start {-cw} {-ch}) (end {cw} {ch})')
    lines.append(f'      (stroke (width 0.05) (type default))')
    lines.append(f'      (fill none)')
    lines.append(f'      (layer "F.CrtYd")')
    lines.append(f'      (uuid "{uid()}")')
    lines.append(f'    )')

    # Pin 1 marker for ICs
    if ref.startswith("U"):
        lines.append(f'    (fp_circle (center {-bw/2 + 0.3} {-bh/2 + 0.3}) (end {-bw/2 + 0.5} {-bh/2 + 0.3})')
        lines.append(f'      (stroke (width 0.2) (type default))')
        lines.append(f'      (fill solid)')
        lines.append(f'      (layer "F.SilkS")')
        lines.append(f'      (uuid "{uid()}")')
        lines.append(f'    )')

    # Pads
    for pad_def in c["pads"]:
        if len(pad_def) == 7:  # thru_hole: name, type, shape, dx, dy, sx, sy, drill
            pname, ptype, pshape, dx, dy, sx, sy = pad_def[:7]
            drill = pad_def[6] if len(pad_def) > 6 else 0.75
            # Actually for thru_hole we have 8 elements

        if len(pad_def) == 5:  # smd: name, type, shape, dx, dy, sx, sy -> wait no
            pass

        # Handle both smd and thru_hole
        pname = pad_def[0]
        ptype = pad_def[1]
        pshape = pad_def[2]
        dx = pad_def[3]
        dy = pad_def[4]

        if ptype == "smd":
            sx, sy = pad_def[5], pad_def[6]
            lines.append(f'    (pad "{pname}" smd {pshape}')
            lines.append(f'      (at {dx} {dy})')
            lines.append(f'      (size {sx} {sy})')
            lines.append(f'      (layers "F.Cu" "F.Paste" "F.Mask")')
            lines.append(f'      (uuid "{uid()}")')
            lines.append(f'    )')
        elif ptype == "thru_hole":
            sx, sy = pad_def[5], pad_def[6]
            drill = pad_def[7] if len(pad_def) > 7 else 0.75
            lines.append(f'    (pad "{pname}" thru_hole {pshape}')
            lines.append(f'      (at {dx} {dy})')
            lines.append(f'      (size {sx} {sy})')
            lines.append(f'      (drill {drill})')
            lines.append(f'      (layers "*.Cu" "*.Mask")')
            lines.append(f'      (uuid "{uid()}")')
            lines.append(f'    )')

    lines.append(f'  )')

# Vias
for vx, vy in vias:
    lines.append(f'  (via (at {vx} {vy}) (size 0.6) (drill 0.305) (layers "F.Cu" "B.Cu") (net 1) (uuid "{uid()}"))')

lines.append(')')

with open('/Users/vedantk/Documents/pcb-design/hardware/kicad/VIGIL_v1.0.kicad_pcb', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print("KiCad PCB file generated successfully!")
print(f"Components: {len(components)}")
print(f"Vias: {len(vias)}")
