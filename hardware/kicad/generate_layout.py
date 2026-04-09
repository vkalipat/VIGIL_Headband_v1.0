"""Generate an SVG layout of the VIGIL v1.0 PCB showing all component positions."""

BOARD_W = 185
BOARD_H = 35
SCALE = 4  # pixels per mm
PAD = 20   # padding around board

W = BOARD_W * SCALE + PAD * 2
H = BOARD_H * SCALE + PAD * 2

def tx(x): return PAD + x * SCALE
def ty(y): return PAD + y * SCALE

# Components: (ref, value, x_mm, y_mm, w_mm, h_mm, rotation, color, hand_solder)
# Positions are corrected Y (Y_new = 35 - Y_original)
components = [
    ("U1", "nRF52840", 42.77, 28.04, 7.0, 7.0, 90, "#2563eb", False),
    ("U2", "LIS3DH", 48.73, 23.18, 3.0, 3.0, 0, "#059669", False),
    ("U3", "TMP117", 45.33, 22.69, 2.0, 2.0, 270, "#059669", False),
    ("U4", "ICS-43434", 48.55, 27.70, 3.5, 2.65, 90, "#dc2626", True),
    ("U5", "AD8606", 42.05, 18.89, 3.0, 3.0, 0, "#7c3aed", False),
    ("U6", "TPS62840", 51.79, 23.42, 2.0, 2.0, 90, "#dc2626", True),
    ("U7", "BQ24072", 57.39, 26.75, 3.0, 3.0, 270, "#ea580c", False),
    ("Y1", "32.768kHz", 47.82, 31.24, 2.0, 1.2, 90, "#dc2626", True),
    ("D1", "LED_GRN", 24.86, 23.37, 1.0, 0.5, 0, "#16a34a", False),
    ("L1", "2.2uH", 52.16, 20.90, 2.0, 1.2, 180, "#78716c", False),
    ("J1", "USB-C", 57.15, 33.74, 9.0, 7.5, 0, "#dc2626", True),
    ("J2", "BAT JST", 56.52, 23.26, 4.0, 3.0, 0, "#dc2626", True),
    ("R1", "4.7k", 51.59, 19.08, 1.0, 0.5, 0, "#78716c", False),
    ("R2", "4.7k", 46.04, 20.29, 0.5, 1.0, 90, "#78716c", False),
    ("C1", "100nF", 46.04, 18.13, 0.5, 1.0, 270, "#78716c", False),
    ("C2", "100nF", 51.59, 25.51, 1.0, 0.5, 0, "#78716c", False),
    ("C3", "10uF", 54.37, 24.44, 1.2, 2.0, 90, "#78716c", False),
    ("C4", "10uF", 48.55, 20.21, 2.0, 1.2, 0, "#78716c", False),
    ("C5", "12pF", 28.69, 25.29, 0.5, 1.0, 90, "#78716c", False),
    ("C6", "12pF", 52.54, 27.44, 0.5, 1.0, 90, "#78716c", False),
]

# Vias from drill file (already in correct coords since drill file Y was board-relative)
# Converting: drill Y values are in original coords, need to keep as-is since
# they represent physical positions. The drill file uses Y from top.
vias_raw = [
    # Perimeter top (Y≈1.124)
    (1.124,1.124),(9.251,1.124),(17.378,1.124),(25.505,1.124),(33.633,1.124),
    (41.76,1.124),(49.887,1.124),(58.014,1.124),(66.141,1.124),(74.269,1.124),
    (82.396,1.124),(90.523,1.124),(98.65,1.124),(106.777,1.124),(114.905,1.124),
    (123.032,1.124),(131.159,1.124),(139.286,1.124),(147.414,1.124),(155.541,1.124),
    (163.668,1.124),(171.795,1.124),
    # Perimeter bottom (Y≈33.875)
    (1.124,33.875),(9.251,33.875),(17.378,33.875),(25.505,33.875),(33.633,33.875),
    (41.76,33.875),(49.887,33.875),(58.014,33.875),(66.141,33.875),(74.269,33.875),
    (82.396,33.875),(90.523,33.875),(98.65,33.875),(106.777,33.875),(114.905,33.875),
    (123.032,33.875),(131.159,33.875),(139.286,33.875),(147.414,33.875),(155.541,33.875),
    (163.668,33.875),(171.795,33.875),(179.922,33.875),
    # Right edge
    (183.875,5.319),(183.875,13.446),(183.875,21.574),
    # Left edge
    (1.124,9.23),(1.124,17.357),(1.124,25.484),
    # Interior
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

svg_parts = []
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H + 120}" font-family="monospace">')

# Background
svg_parts.append(f'<rect width="{W}" height="{H + 120}" fill="#1a1a2e"/>')

# Title
svg_parts.append(f'<text x="{W/2}" y="16" text-anchor="middle" fill="white" font-size="14" font-weight="bold">VIGIL Headband v1.0 — PCB Component Layout (185mm x 35mm Flex)</text>')

# Board outline (polyimide color)
svg_parts.append(f'<rect x="{tx(0)}" y="{ty(0)}" width="{BOARD_W*SCALE}" height="{BOARD_H*SCALE}" fill="#c4841d" stroke="#e6a230" stroke-width="2" rx="2"/>')

# Component island zone
svg_parts.append(f'<rect x="{tx(20)}" y="{ty(0)}" width="{42*SCALE}" height="{BOARD_H*SCALE}" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="8,4"/>')
svg_parts.append(f'<text x="{tx(41)}" y="{ty(-1.5)}" text-anchor="middle" fill="#fbbf24" font-size="9">COMPONENT ISLAND</text>')

# Flex tail label
svg_parts.append(f'<text x="{tx(120)}" y="{ty(17.5)}" text-anchor="middle" fill="#e6a230" font-size="10" opacity="0.7">— FLEX TAIL —</text>')

# PVDF pad zones
svg_parts.append(f'<rect x="{tx(170)}" y="{ty(5)}" width="{12*SCALE}" height="{10*SCALE}" fill="none" stroke="#f97316" stroke-width="1" stroke-dasharray="4,3"/>')
svg_parts.append(f'<text x="{tx(176)}" y="{ty(3.5)}" text-anchor="middle" fill="#f97316" font-size="7">PVDF PADS</text>')
svg_parts.append(f'<text x="{tx(176)}" y="{ty(16)}" text-anchor="middle" fill="#f97316" font-size="6">(Temple 2)</text>')

# Antenna zone
svg_parts.append(f'<rect x="{tx(2)}" y="{ty(5)}" width="{14*SCALE}" height="{25*SCALE}" fill="none" stroke="#60a5fa" stroke-width="1" stroke-dasharray="4,3"/>')
svg_parts.append(f'<text x="{tx(9)}" y="{ty(3.5)}" text-anchor="middle" fill="#60a5fa" font-size="7">BLE ANTENNA</text>')

# Ground plane (back copper - shown as subtle overlay)
svg_parts.append(f'<rect x="{tx(0)}" y="{ty(0)}" width="{BOARD_W*SCALE}" height="{BOARD_H*SCALE}" fill="#854d0e" opacity="0.15"/>')

# Vias
for vx, vy in vias_raw:
    svg_parts.append(f'<circle cx="{tx(vx)}" cy="{ty(vy)}" r="1.2" fill="#a3a3a3" stroke="#737373" stroke-width="0.5" opacity="0.6"/>')

# Components
for ref, val, cx, cy, w, h, rot, color, hand in components:
    x1 = tx(cx) - w * SCALE / 2
    y1 = ty(cy) - h * SCALE / 2
    rw = w * SCALE
    rh = h * SCALE

    opacity = "1" if hand else "0.85"
    stroke = "#ef4444" if hand else "#374151"
    sw = "2" if hand else "1"

    svg_parts.append(f'<rect x="{x1}" y="{y1}" width="{rw}" height="{rh}" fill="{color}" stroke="{stroke}" stroke-width="{sw}" rx="1" opacity="{opacity}"/>')

    # Reference label
    fs = 8 if rw > 20 else 6 if rw > 10 else 5
    svg_parts.append(f'<text x="{tx(cx)}" y="{ty(cy) - 2}" text-anchor="middle" fill="white" font-size="{fs}" font-weight="bold">{ref}</text>')
    svg_parts.append(f'<text x="{tx(cx)}" y="{ty(cy) + 5}" text-anchor="middle" fill="white" font-size="{fs - 1}">{val}</text>')

    if hand:
        svg_parts.append(f'<text x="{tx(cx)}" y="{ty(cy) + rh/2 + 8}" text-anchor="middle" fill="#fca5a5" font-size="5" font-weight="bold">HAND SOLDER</text>')

# Pin 1 indicators for ICs
pin1_markers = [
    (42.77 - 3.0, 28.04 - 3.0, "U1"),  # nRF52840
    (51.79 - 0.8, 23.42 - 0.8, "U6"),   # TPS62840
    (48.55 - 1.5, 27.70 - 1.1, "U4"),   # ICS-43434
]
for px, py, _ in pin1_markers:
    svg_parts.append(f'<circle cx="{tx(px)}" cy="{ty(py)}" r="2" fill="#ef4444" opacity="0.9"/>')
    svg_parts.append(f'<text x="{tx(px)}" y="{ty(py) + 1.5}" text-anchor="middle" fill="white" font-size="3">1</text>')

# Legend
ly = H + 10
svg_parts.append(f'<text x="20" y="{ly}" fill="white" font-size="11" font-weight="bold">LEGEND</text>')
ly += 18

legend_items = [
    ("#2563eb", "MCU (nRF52840)"),
    ("#059669", "Sensors (LIS3DH, TMP117)"),
    ("#7c3aed", "Analog (AD8606 Op-Amp)"),
    ("#ea580c", "Power (BQ24072 Charger)"),
    ("#78716c", "Passives (R, C, L)"),
    ("#16a34a", "LED"),
    ("#dc2626", "HAND SOLDER (U4, U6, Y1, J1, J2)"),
]
for i, (color, label) in enumerate(legend_items):
    x = 20 + (i % 3) * 260
    y = ly + (i // 3) * 18
    svg_parts.append(f'<rect x="{x}" y="{y - 8}" width="12" height="12" fill="{color}" rx="1"/>')
    svg_parts.append(f'<text x="{x + 16}" y="{y + 2}" fill="#d1d5db" font-size="9">{label}</text>')

# Signal flow arrows (simplified)
ly2 = ly + 50
svg_parts.append(f'<text x="20" y="{ly2}" fill="#fbbf24" font-size="10" font-weight="bold">SIGNAL FLOW</text>')
svg_parts.append(f'<text x="20" y="{ly2+15}" fill="#9ca3af" font-size="8">PVDF (temples) → AD8606 (U5) → nRF52840 ADC → BLE → Phone</text>')
svg_parts.append(f'<text x="20" y="{ly2+28}" fill="#9ca3af" font-size="8">LIS3DH (U2) + TMP117 (U3) → I²C → nRF52840 → BLE → Phone</text>')
svg_parts.append(f'<text x="20" y="{ly2+41}" fill="#9ca3af" font-size="8">ICS-43434 (U4) → I²S → nRF52840 → BLE → Phone</text>')
svg_parts.append(f'<text x="20" y="{ly2+54}" fill="#9ca3af" font-size="8">USB-C (J1) → BQ24072 (U7) → Battery → TPS62840 (U6) + L1 → 3.3V</text>')

svg_parts.append('</svg>')

svg = '\n'.join(svg_parts)

with open('/Users/vedantk/Documents/pcb-design/hardware/kicad/VIGIL_v1.0_layout.svg', 'w') as f:
    f.write(svg)

print("SVG generated!")
