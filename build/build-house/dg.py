import math
import diagrams
diagrams.TSCALE = 1.15
from diagrams import svg, t, lead, arrow, box, INK, BLUE, LBLUE, RED, GRN, GROUND, GSTROKE, STEEL, AMBER
WOOD = "#d9b382"; WOOD2 = "#b8895a"; WDK = "#8a5a2b"; STONE = "#b0aca3"; INS = "#f3d36b"; CONC = "#c9c6bf"; SOIL = "#c8b48a"

def R(x, y, w, h, fill="#fff", stroke=INK, sw=1.2, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def L(x1, y1, x2, y2, col=INK, w=1.2, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{d}/>'
def P(pts, fill="none", stroke=INK, sw=1.2, extra=""):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def PL(pts, stroke=INK, sw=1.2, dash="", fill="none"):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def C(x, y, r, fill="#fff", stroke=INK, sw=1.2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def dim(x1, y1, x2, y2, label, off=0, size=10, col="#44525e"):
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="0.9" marker-start="url(#ar)" marker-end="url(#ar)"/>'
    mx, my = (x1+x2)/2, (y1+y2)/2
    if y1 == y2: s += t(mx, my-4+off, label, size, "middle", "600", col)
    else: s += t(mx+5+off, my+4, label, size, "start", "600", col)
    return s

# ---------------------------------------------------------------- emergency shelters
def shelters():
    b = R(0, 0, 760, 300, "#f7f9fa", "none")
    g = 250
    b += R(0, g, 760, 50, GROUND, "none")
    # lean-to
    b += L(20, g, 20, 120, WDK, 5) + L(200, g, 200, 120, WDK, 5) + L(10, 120, 210, 120, WDK, 6)
    for i in range(9):
        x = 25 + i*21
        b += L(x, 120, x-55, g, WOOD2, 4)
    b += P([(10,120),(210,120),(150,g),(-40,g)], "#6b8e4e", "none", extra='opacity="0.55"')
    b += f'<path d="M 120 {g} q 10 -30 20 0 z" fill="{AMBER}"/>' + t(150, g-6, "fire", 10, "start", "600", RED)
    b += t(110, 30, "Lean-to", 14, "middle", "700") + t(110, 48, "with fire reflector in front", 10, "middle", fill="#44525e")
    b += lead(60, 180, 30, 80) + t(32, 76, "ridge pole 2 m, lashed", 9.5)
    b += lead(110, 200, 150, 280) + t(120, 293, "boughs/bark shingled bottom-up", 9.5)
    # debris hut
    x0 = 290
    b += L(x0, g, x0+190, g-70, WDK, 5) + L(x0+175, g, x0+190, g-70, WDK, 4) + L(x0+205, g, x0+190, g-70, WDK, 4)
    b += P([(x0-10,g),(x0+190,g-82),(x0+215,g)], "#8d6e4a", "none", extra='opacity="0.6"')
    b += P([(x0+20,g),(x0+185,g-52),(x0+190,g)], "#f7f9fa", "none")
    b += t(x0+110, 30, "Debris hut", 14, "middle", "700") + t(x0+110, 48, "one person; no fire needed", 10, "middle", fill="#44525e")
    b += lead(x0+90, g-42, x0+70, 90) + t(x0+20, 86, "leaves/needles ≥ 60–90 cm thick", 9.5)
    b += lead(x0+120, g-10, x0+120, 120) + t(x0+70, 114, "dry leaf bed 15–30 cm", 9.5)
    b += t(x0+5, g+30, "entrance downwind; plug with debris pile", 9.5)
    # tarp A-frame
    x0 = 560
    b += L(x0, g-110, x0+180, g-110, INK, 1.5) + L(x0-10, g, x0+10, g-125, WDK, 3) + L(x0+190, g, x0+170, g-125, WDK, 3)
    b += P([(x0+20, g-110), (x0-30, g), (x0+70, g)], LBLUE, BLUE, 1.2) + P([(x0+20,g-110),(x0+160,g-110),(x0+210,g),(x0+70,g)], "#9cc9ea", BLUE, 1.2)
    b += t(x0+90, 30, "Tarp A-frame", 14, "middle", "700") + t(x0+90, 48, "fast; ridge line between trees", 10, "middle", fill="#44525e")
    b += lead(x0+130, g-80, x0+150, 80) + t(x0+70, 76, "taut-line hitch ridge", 9.5)
    b += t(x0+10, g+30, "stake corners; ground pad essential", 9.5)
    return svg(760, 300, b, "Emergency shelters")

# ---------------------------------------------------------------- site plan
def site_plan():
    W, H = 760, 520
    b = R(0, 0, W, H, "#eef3e6", "none")
    # contours
    for i, yy in enumerate([60, 120, 190]):
        b += f'<path d="M0,{yy} C200,{yy-30} 500,{yy+30} {W},{yy-10}" fill="none" stroke="#a7b58e" stroke-width="1"/>'
        b += t(8, yy-4, ["elev. 112 m", "elev. 110 m", "elev. 108 m"][i], 8.5, fill="#6d7c55")
    # creek + floodplain
    b += f'<path d="M0,470 C200,430 450,500 {W},450 L{W},{H} L0,{H} Z" fill="#cfe0ef" opacity="0.8"/>'
    b += f'<path d="M0,492 C220,455 470,520 {W},475" fill="none" stroke="{BLUE}" stroke-width="7"/>'
    b += f'<path d="M0,410 C200,380 450,450 {W},400" fill="none" stroke="{BLUE}" stroke-width="1.3" stroke-dasharray="6 4"/>'
    b += t(470, 418, "100-year flood line — build ABOVE this, plus margin", 9.5, fill=BLUE, weight="600")
    b += t(560, 505, "creek", 10, fill=BLUE, italic=True)
    # defensible space rings around house
    hx, hy, hw, hh = 330, 210, 120, 70
    cx, cy = hx+hw/2, hy+hh/2
    for r_, col, lab in [(160, "#f9e0c0", "30 m (100 ft): thin trees, prune limbs"), (95, "#f6cfa0", "9 m (30 ft): lean, green, mowed"), (55, "#f2b880", "1.5 m (5 ft): bare / gravel")]:
        b += f'<ellipse cx="{cx}" cy="{cy}" rx="{r_+hw/2-20}" ry="{r_*0.75+hh/2-10}" fill="{col}" opacity="0.55" stroke="#d08a3a" stroke-dasharray="4 3"/>'
    b += t(70, 330, "Fire-defensible zones", 9.5, "start", "700", "#a0521b")
    b += t(70, 343, "around house: 1.5 m · 9 m · 30 m", 9, fill="#a0521b")
    # house
    b += R(hx, hy, hw, hh, "#fff", INK, 2) + t(cx, cy+4, "HOUSE", 11, "middle", "700")
    b += L(hx, hy+hh, hx+hw, hy+hh, AMBER, 5) + t(cx, hy+hh+14, "long side + most glass faces south", 9, "middle", "600", "#8a5a00")
    # garden south
    b += R(hx-20, 330, 170, 55, "#c5e1a5", GRN, 1) + t(hx+65, 362, "garden / orchard (sunny side)", 9.5, "middle", fill=GRN)
    # windbreak NW
    for i in range(9):
        x, y = 60+i*28, 112 + (i%2)*8 - i*2
        b += C(x, y, 13, "#5d8a4a", "#3e6b30", 1)
    for i in range(5):
        b += C(40, 140+i*26, 12, "#5d8a4a", "#3e6b30", 1)
    b += t(100, 86, "windbreak (evergreens) on winter-wind side, 2–5× tree height from house", 9.5, "start", "600", "#2e5a22")
    b += arrow(20, 34, 62, 58, BLUE, 2.2, "arb") + t(22, 22, "prevailing winter wind (NW in much of N. America)", 9, fill=BLUE)
    # well uphill
    b += C(560, 120, 10, LBLUE, BLUE, 1.5) + t(546, 112, "well / spring box", 9.5, "end", "600", BLUE) + t(546, 124, "uphill of outhouse", 9, "end", fill=BLUE)
    # outhouse downhill
    b += R(640, 330, 26, 26, "#e7d1b0", WDK, 1.5) + t(653, 371, "outhouse", 9.5, "middle", "600", WDK)
    b += L(560, 130, 650, 330, RED, 1.2, "5 3") + t(612, 240, "≥ 30 m", 10, "start", "700", RED) + t(612, 252, "(100 ft)", 9, fill=RED)
    # woodshed & shop
    b += R(200, 235, 60, 30, WOOD, WDK, 1) + t(230, 254, "woodshed", 9, "middle")
    b += L(260, 250, hx, 250, "#8a7d5a", 1, "3 3") + t(270, 244, "short covered path", 8.5, fill="#6b5e3e")
    # cistern
    b += C(hx+hw+30, hy+20, 14, LBLUE, BLUE, 1.5) + t(hx+hw+30, hy+24, "C", 10, "middle", "700", BLUE) + t(hx+hw+48, hy+10, "rain cistern", 9, fill=BLUE)
    # swale
    b += f'<path d="M260,190 C330,180 450,180 520,195" fill="none" stroke="#7a9e5e" stroke-width="4" stroke-dasharray="10 4"/>'
    b += t(250, 168, "diversion swale (uphill) sheds runoff around house", 9, "start", "600", "#4f6e3a")
    # compass
    b += f'<g transform="translate(715,60)"><polygon points="0,-28 7,0 0,-6 -7,0" fill="{INK}"/><polygon points="0,28 7,0 0,6 -7,0" fill="#fff" stroke="{INK}"/>' + t(0, -32, "N", 11, "middle", "700") + t(0, 42, "S", 10, "middle") + '</g>'
    b += t(10, H-8, "Not to scale. Northern-hemisphere layout; slope falls toward the creek (south).", 9, italic=True)
    return svg(W, H, b, "Homestead site plan")

# ---------------------------------------------------------------- passive solar section
def passive_solar(lat=40):
    W, H = 760, 380
    b = R(0, 0, W, H, "#f7fbff", "none")
    g = 300
    b += R(0, g, W, 80, GROUND, "none")
    # house section
    x0, x1 = 240, 600
    b += R(x0, 150, x1-x0, g-150, "#fff", INK, 2)
    b += P([(x0-90, 150), (x0+180, 60), (x1+20, 150)], "#cfd8dc", INK, 1.5)  # roof w/ south overhang to the left
    b += t(x0+180, 52, "insulated roof", 9.5, "middle")
    # south window (left wall)
    b += R(x0-4, 175, 8, 95, LBLUE, BLUE, 1.5)
    b += t(x0-80, 205, "south glass", 9.5, "start", "600", BLUE) + t(x0-80, 217, "≈7–12% of", 9, fill=BLUE) + t(x0-80, 228, "floor area", 9, fill=BLUE)
    # thermal mass floor and wall
    b += R(x0, g-22, x1-x0, 22, CONC, INK, 1, 'fill-opacity="0.9"')
    b += t(x0+170, g-7, "dark thermal-mass floor (stone, brick, earth, slab)", 9.5, "middle", "600")
    b += R(x0, g, x1-x0, 10, "url(#ins)", "#8a7d5a", 0.8) + t(x1+8, g+9, "insulation under / around mass", 9)
    b += R(x0+240, 170, 30, g-192, "#c49a6c", INK, 1) + t(x0+255, 165, "mass wall", 9, "middle")
    # sun rays
    ws = 90 - lat - 23.45; ss = 90 - lat + 23.45
    def ray(ang, col, lab, y_hit, xs=x0, labx=20, laby=40):
        a = math.radians(ang)
        L0 = 300
        xa, ya = xs - L0*math.cos(a), y_hit - L0*math.sin(a)
        s = f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xs}" y2="{y_hit}" stroke="{col}" stroke-width="2.4" marker-end="url(#ar)"/>'
        return s
    # winter: enters window and hits floor deep
    a = math.radians(ws)
    for dy in (180, 230, 268):
        xa, ya = x0-260*math.cos(a), dy-260*math.sin(a)
        b += L(xa, ya, x0, dy, AMBER, 2.2)
        # continue inside to floor
        xf = x0 + (g-22-dy)/math.tan(a)
        b += L(x0, dy, xf, g-22, AMBER, 1.6, "5 3")
    b += t(10, 170, f"Winter noon sun ≈ {ws:.0f}° (at {lat}°N)", 10.5, "start", "700", "#b97800")
    b += t(10, 184, "low, enters deep, heats mass", 9.5, fill="#b97800")
    # summer: blocked by overhang
    a = math.radians(ss)
    xo, yo = x0-90+2, 150+1
    xa, ya = xo-120*math.cos(a), yo-120*math.sin(a)
    b += L(xa, ya, xo, yo, RED, 2.2) + L(xo, yo, xo + (g-yo)/math.tan(a)*0.35, yo + (g-yo)*0.35, RED, 1.4, "4 3")
    b += t(70, 36, f"Summer noon sun ≈ {ss:.0f}°", 10.5, "start", "700", RED) + t(70, 50, "high — overhang shades glass", 9.5, fill=RED)
    b += lead(x0-60, 156, x0-120, 120) + t(x0-205, 115, "overhang sized for latitude", 9.5, "start", "600")
    # north side
    b += R(x1-4, 190, 8, 30, LBLUE, BLUE, 1) + t(x1+12, 200, "few, small north windows", 9.5) + t(x1+12, 214, "earth berm / storage on north", 9.5)
    b += P([(x1, g), (x1, 230), (x1+150, g)], SOIL, GSTROKE, 1)
    b += t(x0+180, 125, "SOUTH ◄", 10, "middle", "700") 
    b += t(10, H-10, "Noon solar altitude = 90° − latitude ± 23.45° (+ in June, − in December).", 9.5, italic=True)
    return svg(W, H, b, "Passive solar section")

# ---------------------------------------------------------------- floor plan 16x24
def floor_plan():
    s = 22  # px per ft
    ox, oy = 70, 60
    Wf, Hf = 24, 16
    W, H = ox + Wf*s + 200, oy + Hf*s + 80
    b = R(0, 0, W, H, "#fff", "none")
    wall = 0.5*s
    b += R(ox, oy, Wf*s, Hf*s, "#f4efe6", INK, 3)
    # interior partitions: bedroom NE 10x8, bath/pantry NW
    b += L(ox+14*s, oy, ox+14*s, oy+8*s, INK, 2.5) + L(ox+14*s, oy+8*s, ox+Wf*s, oy+8*s, INK, 2.5)
    b += L(ox+5*s, oy, ox+5*s, oy+6*s, INK, 2.5) + L(ox, oy+6*s, ox+5*s, oy+6*s, INK, 2.5)
    # door openings (gaps)
    b += R(ox+14*s-3, oy+5*s, 6, 2.6*s, "#f4efe6", "none") + f'<path d="M{ox+14*s},{oy+5*s} a {2.6*s},{2.6*s} 0 0 0 {-2.6*s},{2.6*s}" fill="none" stroke="#888" stroke-dasharray="3 2"/>'
    b += R(ox+2*s, oy+6*s-3, 2.4*s, 6, "#f4efe6", "none")
    # labels
    b += t(ox+19*s, oy+4*s, "BEDROOM", 11, "middle", "700") + t(ox+19*s, oy+4*s+14, "10 × 8 ft (loft above)", 9, "middle")
    b += t(ox+2.5*s, oy+2.6*s, "PANTRY /", 10, "middle", "700") + t(ox+2.5*s, oy+2.6*s+13, "COMPOST", 10, "middle", "700") + t(ox+2.5*s, oy+2.6*s+26, "TOILET", 10, "middle", "700")
    b += t(ox+9.5*s, oy+3*s, "KITCHEN", 11, "middle", "700") + t(ox+9.5*s, oy+3*s+14, "counter on north wall", 9, "middle")
    b += R(ox+5.5*s, oy+0.3*s, 8*s, 2*s, "#e0d6c2", "#8a7d5a", 1) 
    b += t(ox+9*s, oy+11.5*s, "LIVING / DINING", 11, "middle", "700") + t(ox+9*s, oy+11.5*s+14, "sun-warmed mass floor", 9, "middle")
    # stove central
    b += R(ox+12*s, oy+9.5*s, 2*s, 1.6*s, "#555", INK, 1) + t(ox+13*s, oy+9.5*s-6, "wood stove", 9, "middle", "700", RED)
    b += f'<rect x="{ox+11.3*s}" y="{oy+8.9*s}" width="{3.4*s}" height="{3*s}" fill="none" stroke="{RED}" stroke-dasharray="4 3"/>'
    b += t(ox+11.3*s, oy+12.4*s, "hearth pad", 8.5, "start", fill=RED)
    # entry vestibule east
    b += R(ox+Wf*s, oy+10*s, 4*s, 5*s, "#efe7d8", INK, 2) + t(ox+Wf*s+2*s, oy+12.3*s, "AIRLOCK", 9.5, "middle", "700") + t(ox+Wf*s+2*s, oy+12.3*s+12, "mudroom", 8.5, "middle")
    b += R(ox+Wf*s-3, oy+11*s, 6, 3*s, "#f4efe6", "none")
    b += R(ox+Wf*s+4*s-3, oy+11.5*s, 6, 2.6*s, "#fff", "none") + t(ox+Wf*s+4*s+8, oy+13*s, "door", 9)
    # windows south (bottom) big; north small
    for xft in (1.5, 6.5, 11.5, 17):
        b += R(ox+xft*s, oy+Hf*s-4, 4*s if xft < 17 else 3*s, 8, LBLUE, BLUE, 1.3)
    for xft in (7, 19):
        b += R(ox+xft*s, oy-4, 2*s, 8, LBLUE, BLUE, 1.3)
    b += R(ox-4, oy+9*s, 8, 3*s, LBLUE, BLUE, 1.3)
    # dims
    b += dim(ox, oy+Hf*s+30, ox+Wf*s, oy+Hf*s+30, "24 ft (7.3 m)")
    b += dim(ox-30, oy, ox-30, oy+Hf*s, "", 0) + t(ox-48, oy+Hf*s/2, "16 ft", 10, "middle", "600", "#44525e") + t(ox-48, oy+Hf*s/2+12, "(4.9 m)", 9, "middle", fill="#44525e")
    b += t(ox+Wf*s/2, oy+Hf*s+52, "SOUTH — main glazing", 10, "middle", "700", "#8a5a00")
    b += t(ox+Wf*s/2, oy-14, "NORTH — pantry, storage, few windows", 10, "middle", "700", "#44525e")
    # ladder to loft
    for i in range(5):
        b += L(ox+15*s, oy+8.6*s+i*9, ox+16.4*s, oy+8.6*s+i*9, WDK, 1.5)
    b += t(ox+16.6*s, oy+9.3*s, "ladder", 8.5)
    b += t(ox+Wf*s+8, oy+20, "384 ft² (36 m²)", 10, "start", "700") + t(ox+Wf*s+8, oy+34, "+ 10×16 sleeping loft", 9) + t(ox+Wf*s+8, oy+48, "2–4 people", 9)
    return svg(W, H, b, "Small cabin floor plan")

# ---------------------------------------------------------------- foundations
def foundations():
    W, H = 780, 330
    b = R(0, 0, W, H, "#fff", "none")
    g = 120; frost = 230
    b += R(0, g, W, H-g-30, SOIL, "none", extra='opacity="0.55"')
    b += L(0, frost, W, frost, BLUE, 1.6, "8 5") + t(160, frost-18, "frost line", 9.5, "start", "700", BLUE) + t(160, frost-6, "(local depth)", 9, "start", "600", BLUE)
    def title(x, s1, s2): return t(x, 22, s1, 12.5, "middle", "700") + t(x, 38, s2, 9.5, "middle", fill="#44525e")
    # 1 pier
    x = 95
    b += title(x, "Pier / post", "fast, cheap, good on slopes")
    b += R(x-60, 85, 120, 14, WOOD, WDK, 1) + t(x, 80, "beam", 9, "middle")
    b += R(x-12, 99, 24, 70, CONC, INK, 1) + R(x-30, frost+5, 60, 20, CONC, INK, 1)
    b += R(x-12, 169, 24, frost+5-169, CONC, INK, 1)
    b += lead(x+12, 140, x+48, 140) + t(x+50, 136, "stone/", 8.5) + t(x+50, 147, "concrete", 8.5) + t(x+50, 158, "pier", 8.5)
    b += lead(x+30, frost+15, x+48, frost+40) + t(x+20, frost+52, "footing below frost", 8.5, "middle")
    # 2 rubble trench
    x = 290
    b += title(x, "Rubble trench", "drains water; no concrete needed")
    b += R(x-40, frost-10+15, 80, 0, INK)
    b += P([(x-35, g), (x+35, g), (x+35, frost+15), (x-35, frost+15)], "#d8d4cb", INK, 1)
    for i in range(40):
        cx_ = x-28 + (i*13) % 56; cy_ = g+8 + (i*17) % (frost+5-g)
        b += C(cx_, cy_, 5, "#bdb7aa", "#8b857a", 0.6)
    b += C(x, frost+8, 6, "#fff", BLUE, 1.5) + t(x+40, frost+12, "perforated drain to daylight", 8.5, "start", fill=BLUE)
    b += R(x-35, g-30, 70, 30, "#a39e94", INK, 1) + t(x, g-12, "grade beam / stone", 8.5, "middle")
    b += R(x-25, g-55, 50, 25, "#fff", INK, 1) + t(x, g-38, "wall", 8.5, "middle")
    b += lead(x+30, 170, x+60, 170) + t(x+62, 166, "washed", 8.5) + t(x+62, 177, "stone 2–5 cm", 8.5)
    # 3 dry stone / mortared
    x = 490
    b += title(x, "Stone foundation wall", "mortared or dry-laid; durable")
    rows = int((frost+15-(g-40))/18)
    for r_ in range(rows):
        y = g-40 + r_*18; off = (r_ % 2)*14
        for k in range(3):
            b += R(x-42+off+k*28 - (14 if off else 0), y, 28, 18, STONE, "#6e6a62", 0.8, 'rx="3"')
    b += R(x-50, frost+15, 100, 14, "#a39e94", INK, 1) + t(x, frost+40, "wide footing course", 8.5, "middle")
    b += lead(x-42, g-20, x-75, g-55) + t(x-115, g-60, "sill on gasket/flashing", 8.5)
    b += t(x+52, g-25, "≥ 20 cm (8 in)", 8.5) + t(x+52, g-14, "above grade", 8.5)
    # 4 concrete stem wall / FPSF
    x = 690
    b += title(x, "Concrete footing + stem", "strongest; needs cement")
    b += R(x-15, g-30, 30, frost-g+30, CONC, INK, 1) + R(x-40, frost, 80, 25, CONC, INK, 1)
    for k in range(2): b += L(x-30, frost+8+k*8, x+30, frost+8+k*8, RED, 1.2)
    b += L(x-5, g-25, x-5, frost+20, RED, 1) + L(x+5, g-25, x+5, frost+20, RED, 1)
    b += lead(x+15, 170, x+50, 160) + t(x+40, 152, "rebar", 8.5, "start", fill=RED)
    b += t(x, frost+40, "see Concrete & Masonry vol.", 8.5, "middle", "600", "#8a4b08")
    b += t(10, H-10, "Ground level at the top of the brown band. In permafrost, use posts/pads or piles and keep the ground frozen (see Region 1).", 9, italic=True)
    return svg(W, H, b, "Foundation types")

# ---------------------------------------------------------------- wall section
def wall_section():
    W, H = 700, 560
    b = R(0, 0, W, H, "#fff", "none")
    g = 460
    b += R(0, g, W, 100, SOIL, "none", extra='opacity="0.6"')
    wx = 300  # outside face of studs
    # foundation
    b += R(wx-20, g-50, 140, 150, CONC, INK, 1.2) + R(wx-50, g+80, 200, 20, CONC, INK, 1)
    b += P([(wx-120, g+100), (wx-20, g+100), (wx-20, g-10), (wx-120, g+10)], "#d8d4cb", "none")
    b += C(wx-40, g+88, 7, "#fff", BLUE, 1.5)
    # sill
    b += R(wx-5, g-60, 98, 10, WOOD2, WDK, 1) + L(wx-6, g-50, wx+94, g-50, "#000", 2)
    # studs (section shows one stud cavity)
    b += R(wx, 110, 88, g-170, "url(#ins)", "#8a7d5a", 0.8)
    b += R(wx+88, 110, 6, g-170, "#e8e2d6", INK, 1)  # interior finish
    b += L(wx+86, 110, wx+86, g-60, RED, 1.2, "6 3")  # vapor retarder
    b += R(wx-12, 110, 12, g-170, "#c9a46e", WDK, 1)  # sheathing
    b += R(wx-17, 110, 4, g-170, "#fff", "#8a7d5a", 0.5)  # WRB
    for yy in range(115, g-60, 30): b += R(wx-27, yy, 7, 18, WOOD, WDK, 0.5)  # furring/rainscreen
    b += R(wx-35, 105, 8, g-155, "#e0c08f", WDK, 1)  # siding
    # top plates
    b += R(wx-5, 96, 98, 7, WOOD2, WDK, 1) + R(wx-5, 103, 98, 7, WOOD2, WDK, 1)
    # rafter + roof
    b += P([(wx-140, 120), (wx+400, -40), (wx+400, -10), (wx-140, 150)], WOOD, WDK, 1)
    b += P([(wx-140, 113), (wx+400, -47), (wx+400, -40), (wx-140, 120)], "#7d8b96", INK, 1)
    b += P([(wx+10, 103), (wx+400, -10), (wx+400, 40), (wx+93, 96)], "url(#ins)", "#8a7d5a", 0.5)
    b += R(wx+93, 80, 300, 8, "#e8e2d6", INK, 1)  # ceiling
    b += P([(wx-60, 125), (wx-30, 116), (wx-30, 130), (wx-60, 139)], "#fff", "none")
    # gutter
    b += f'<path d="M{wx-150},140 q 0 16 14 16 q 14 0 14 -16" fill="#cfd8dc" stroke="{INK}"/>'
    # interior floor
    b += R(wx+94, g-60, 220, 12, WOOD, WDK, 1) + R(wx+94, g-48, 220, 30, "url(#ins)", "#8a7d5a", 0.5)
    # drip edge water
    b += arrow(wx-160, 175, wx-160, 260, BLUE, 1.4, "arb") 
    labs_l = [
        (wx-31, 300, "siding (boards, shakes, salvaged metal)"),
        (wx-23, 340, "19 mm (¾\") air gap / rainscreen on furring"),
        (wx-15, 380, "weather-resistive barrier (house wrap, tar paper)"),
        (wx-6, 410, "sheathing (boards laid diagonal or plywood)"),
        (wx-30, 150, "eave overhang 45–60 cm (18–24\") + gutter"),
        (wx-20, g+30, "foundation ≥ 20 cm (8\") above grade"),
        (wx-40, g+88, "gravel + perforated drain"),
    ]
    for x, y, s_ in labs_l:
        b += lead(x, y, 10+len(s_)*0, y) if False else ""
        b += f'<line x1="{x}" y1="{y}" x2="{x-50}" y2="{y}" stroke="{INK}" stroke-width="0.8"/><circle cx="{x}" cy="{y}" r="2" fill="{INK}"/>'
        b += t(x-54, y+3.5, s_, 9.5, "end")
    labs_r = [
        (wx+44, 250, "insulation fills the cavity (see Table)"),
        (wx+86, 290, "warm-side vapor retarder (cold climates only)", RED),
        (wx+91, 330, "interior finish (boards, plaster, drywall)"),
        (wx+44, g-55, "sill plate on gasket + capillary break", INK),
        (wx+44, 100, "doubled top plate", INK),
        (wx+250, 60, "R-38 to R-60 ceiling in cold climates", INK),
        (wx+200, g-35, "insulated floor", INK),
    ]
    for item in labs_r:
        x, y, s_ = item[:3]; col = item[3] if len(item) > 3 else INK
        b += f'<line x1="{x}" y1="{y}" x2="{wx+130}" y2="{y}" stroke="{col}" stroke-width="0.8"/><circle cx="{x}" cy="{y}" r="2" fill="{col}"/>'
        b += t(wx+134, y+3.5, s_, 9.5, fill=col)
    b += t(10, 20, "OUTSIDE", 11, "start", "700", "#44525e") + t(W-10, 20, "INSIDE", 11, "end", "700", "#44525e")
    b += t(10, H-8, "Stick-frame wall, cold-climate version. In hot-humid climates omit the interior vapor retarder (let walls dry inward).", 9, italic=True)
    return svg(W, H, b, "Wall section")

# ---------------------------------------------------------------- log notches
def log_notches():
    W, H = 780, 330
    b = R(0, 0, W, H, "#fff", "none")
    def logend(cx, cy, r, fill=WOOD):
        s = C(cx, cy, r, fill, WDK, 1.2)
        for k in (0.65, 0.35): s += f'<circle cx="{cx}" cy="{cy}" r="{r*k:.1f}" fill="none" stroke="{WDK}" stroke-width="0.5" opacity="0.6"/>'
        return s
    def logside(x, y, w, h): return R(x, y, w, h, WOOD, WDK, 1.2, 'rx="6"')
    # 1 saddle notch: lower log end with upper log sitting in a saddle cut on its underside
    x = 100
    b += t(x, 24, "Saddle notch", 12.5, "middle", "700") + t(x, 40, "easiest round-log notch", 9.5, "middle", fill="#44525e")
    b += logside(x-80, 150, 160, 44)  # lower log running across
    b += f'<path d="M{x-80},120 L{x-30},120 A 34 34 0 0 0 {x+30} 120 L{x+80},120 L{x+80},96 L{x-80},96 Z" fill="{WOOD}" stroke="{WDK}" stroke-width="1.2"/>'
    b += logend(x, 172, 34, "#e3c79c")
    b += lead(x+30, 112, x+70, 70) + t(x+20, 64, "cup cut in upper log", 9)
    b += t(x, 230, "scribe the curve, cut a cup", 9, "middle") + t(x, 243, "in the log's UNDERSIDE so", 9, "middle") + t(x, 256, "water can't collect in it", 9, "middle")
    # 2 dovetail (hewn)
    x = 290
    b += t(x, 24, "Dovetail", 12.5, "middle", "700") + t(x, 40, "hewn logs; locks both ways", 9.5, "middle", fill="#44525e")
    for k in range(3):
        y = 90 + k*48
        b += P([(x-50, y), (x+50, y+8), (x+50, y+44), (x-50, y+40)], WOOD if k % 2 == 0 else "#e3c79c", WDK, 1.2)
    b += t(x, 250, "sloped faces shed water out", 9, "middle") + t(x, 263, "and wedge corner tight", 9, "middle")
    # 3 square / butt-and-pass
    x = 480
    b += t(x, 24, "Square / half-lap", 12.5, "middle", "700") + t(x, 40, "simple; pin with pegs/spikes", 9.5, "middle", fill="#44525e")
    for k in range(4):
        y = 85 + k*36
        b += R(x-55, y, 110, 34, WOOD if k % 2 == 0 else "#e3c79c", WDK, 1.2)
    b += L(x, 75, x, 235, RED, 1.2, "4 3") + t(x+5, 252, "drift pin / trunnel", 9, "start", fill=RED)
    b += t(x, 270, "needs good flashing", 9, "middle") 
    # 4 Scandinavian full scribe (cross-section)
    x = 670
    b += t(x, 24, "Full-scribe (Scandinavian)", 12.5, "middle", "700") + t(x, 40, "no chinking; best seal", 9.5, "middle", fill="#44525e")
    b += logend(x, 200, 42)
    b += f'<path d="M{x-44},140 A 44 44 0 0 1 {x+44} 140 L {x+30} 158 A 42 42 0 0 0 {x-30} 158 Z" fill="#e3c79c" stroke="{WDK}" stroke-width="1.2"/>'
    b += C(x, 110, 44, "#e3c79c", WDK, 1.2)
    b += f'<path d="M{x-30},154 Q {x} 140 {x+30} 154" fill="none" stroke="{GRN}" stroke-width="4"/>'
    b += t(x, 58, "groove + wool/moss gasket", 9, "middle", "600", GRN)
    b += t(x, 270, "upper log scribed to lower", 9, "middle") 
    # chinking strip
    b += R(0, 285, W, 45, "#f6f1e7", "none")
    b += t(12, 303, "Chinking (for saddle/square/dovetail walls): 1) stuff gaps with wood wedges or split poles, 2) pack moss, oakum or wool,", 9.5)
    b += t(12, 318, "3) finish with lime-sand-sawdust daub or clay-straw both sides. Re-chink after 1–2 years of settling (logs shrink ~5% across the grain).", 9.5)
    return svg(W, H, b, "Log notch types")

# ---------------------------------------------------------------- timber frame joints
def timber_joints():
    W, H = 760, 260
    b = R(0, 0, W, H, "#fff", "none")
    # mortise & tenon w/ peg (elevation)
    x = 40
    b += t(130, 22, "Mortise & tenon, pegged", 12, "middle", "700")
    b += R(x, 50, 50, 190, WOOD, WDK, 1.2) + t(x+25, 252, "post", 9, "middle")
    b += R(x+50, 115, 170, 50, "#e3c79c", WDK, 1.2) + t(x+150, 145, "beam", 9, "middle")
    b += R(x+5, 125, 45, 30, "#e3c79c", WDK, 1, 'stroke-dasharray="4 2"')
    b += C(x+28, 140, 5, WDK, INK, 1) + lead(x+28, 140, x+90, 85) + t(x+60, 78, "oak peg (drawbored)", 9)
    b += t(x+100, 190, "tenon ≈ ⅓ beam thickness", 9)
    # half lap
    x = 300
    b += t(370, 22, "Half-lap", 12, "middle", "700")
    b += P([(x, 110), (x+90, 110), (x+90, 135), (x+140, 135), (x+140, 160), (x, 160)], WOOD, WDK, 1.2)
    b += P([(x+90, 110), (x+230, 110), (x+230, 160), (x+140, 160), (x+140, 135), (x+90, 135)], "#e3c79c", WDK, 1.2)
    b += C(x+115, 135, 4, WDK, INK, 1) + t(x+115, 185, "half the depth from each piece; peg or bolt", 9, "middle")
    # knee brace
    x = 560
    b += t(650, 22, "Knee brace (racking)", 12, "middle", "700")
    b += R(x, 50, 36, 190, WOOD, WDK, 1.2) + R(x+36, 50, 170, 36, "#e3c79c", WDK, 1.2)
    b += P([(x+36, 170), (x+36, 145), (x+141, 86), (x+166, 86)], WOOD2, WDK, 1.2)
    b += t(x+110, 150, "45°; 60–90 cm legs", 9) + t(x+110, 163, "both ends tenoned", 9)
    return svg(W, H, b, "Timber frame joints")

# ---------------------------------------------------------------- roof framing
def roof_framing():
    W, H = 780, 330
    b = R(0, 0, W, H, "#fff", "none")
    # left: rafters with ridge, collar tie, ceiling joist
    x0, x1, yb, yr = 30, 380, 230, 70
    xm = (x0+x1)/2
    b += R(x0-10, yb, 30, 70, WOOD2, WDK, 1) + R(x1-20, yb, 30, 70, WOOD2, WDK, 1)
    b += t(x0+5, yb+85, "wall", 9, "middle") 
    b += P([(x0-30, yb+10), (xm, yr), (xm+6, yr+8), (x0-18, yb+20)], WOOD, WDK, 1.2)
    b += P([(x1+30, yb+10), (xm, yr), (xm-6, yr+8), (x1+18, yb+20)], WOOD, WDK, 1.2)
    b += R(xm-6, yr-8, 12, 26, WOOD2, WDK, 1) + lead(xm, yr-4, xm+40, yr-30) + t(xm+43, yr-30, "ridge board", 9)
    b += R(x0, yb-8, x1-x0, 10, "#e3c79c", WDK, 1) + t(xm, yb+20, "ceiling joist = rafter tie (resists outward thrust)", 9, "middle", "600", RED)
    b += R(xm-70, 135, 140, 8, "#e3c79c", WDK, 1) + t(xm, 130, "collar tie (upper ⅓)", 9, "middle")
    b += lead(x0+8, yb-4, x0-5, 150) + t(x0-15, 145, "birdsmouth seat", 9, "start")
    b += t(x0+60, 300, "Common-rafter roof: rafters at 40–60 cm (16–24\") centers", 9.5) + t(x0+60, 314, "Hurricane/uplift zones: strap every rafter to the wall", 9.5, fill=RED)
    # dims: span, rise, run
    b += dim(x0, 285, x1, 285, "span")
    b += L(xm, yr+12, xm, yb-10, "#44525e", 0.8, "3 3") + t(xm+4, 190, "rise", 9, fill="#44525e")
    # right: king post truss + fink
    ox = 430
    pts = [(ox, 180), (ox+150, 80), (ox+300, 180)]
    b += P(pts, "none", WDK, 6) 
    b += L(ox, 180, ox+300, 180, WDK, 6) + L(ox+150, 80, ox+150, 180, WOOD2, 5) + L(ox+150, 180, ox+75, 130, WOOD2, 4) + L(ox+150, 180, ox+225, 130, WOOD2, 4)
    for (xx, yy) in [(ox+150, 80), (ox+150, 180), (ox+75, 130), (ox+225, 130), (ox, 180), (ox+300, 180)]:
        b += R(xx-7, yy-7, 14, 14, "#cfd8dc", INK, 0.8)
    b += t(ox+150, 40, "King-post truss", 12, "middle", "700") + t(ox+150, 56, "spans 6–9 m (20–30 ft) with no interior wall", 9, "middle", fill="#44525e")
    b += t(ox+150, 205, "gusset plates: 12 mm plywood both sides,", 9, "middle") + t(ox+150, 218, "glued + nailed, or bolted steel plates", 9, "middle")
    b += lead(ox+150, 175, ox+190, 245) + t(ox+150, 258, "top chord · bottom chord (tension) · web", 9)
    b += lead(ox+75, 130, ox+40, 100) + t(ox-10, 95, "gusset", 9)
    b += t(ox+150, 290, "Build all trusses on one floor jig so they match;", 9.5, "middle") + t(ox+150, 304, "set at 60 cm (24\") and brace diagonally.", 9.5, "middle")
    return svg(W, H, b, "Roof framing")

# ---------------------------------------------------------------- roof pitch
def roof_pitch():
    W, H = 760, 330
    b = R(0, 0, W, H, "#fff", "none")
    ox, oy, run = 60, 290, 300
    b += L(ox, oy, ox+run+10, oy, INK, 1.5) + t(ox+run/2, oy+18, "run = 12", 10, "middle", "600")
    data = [(1, "1:12 sod/membrane only", "#9e9e9e"), (3, "3:12 min. metal panels", STEEL), (4, "4:12 shingles, shakes (min)", "#6d4c41"),
            (6, "6:12 general rain", BLUE), (8, "8:12 heavy snow", "#1f4e5f"), (12, "12:12 (45°) thatch min.", "#8a5a00")]
    for rise, lab, col in data:
        ang = math.degrees(math.atan(rise/12))
        y2 = oy - run*rise/12
        b += L(ox, oy, ox+run, y2, col, 2.4)
        b += t(ox+run+8, y2+4, f"{lab}  ({ang:.0f}°)", 10, "start", "600", col)
    b += L(ox+run, oy, ox+run, oy-run, "#c5ccd2", 1, "3 3")
    b += t(ox+run-6, oy-run+14, "rise", 9.5, "end", fill="#44525e")
    b += t(10, 22, "Roof pitch = inches of rise per 12 inches of run.  Angle = arctan(rise ÷ 12).", 10.5, "start", "700")
    b += t(10, 38, "Steeper sheds rain and snow faster but uses more material and catches more wind.", 9.5, fill="#44525e")
    return svg(W, H, b, "Roof pitch guide")

# ---------------------------------------------------------------- chimney clearances
def chimney():
    W, H = 780, 450
    b = R(0, 0, W, H, "#fff", "none")
    # left: stove in room with clearances
    fl = 390
    b += R(0, fl, 420, 12, WOOD, WDK, 1)
    b += R(40, 60, 12, fl-60, "#e8e2d6", INK, 1) + t(46, 52, "combustible wall", 9, "middle")
    sx, sw_, sh = 200, 90, 80
    b += R(sx, fl-sh-25, sw_, sh, "#4a4a4a", INK, 1.5) + R(sx+8, fl-25, 8, 25, "#4a4a4a") + R(sx+sw_-16, fl-25, 8, 25, "#4a4a4a")
    b += t(sx+sw_/2, fl-sh/2-20, "STOVE", 10, "middle", "700", "#fff")
    b += R(sx+35, 70, 20, fl-sh-25-70, "#7d8b96", INK, 1) + t(sx+60, 110, "single-wall", 9) + t(sx+60, 121, "stovepipe", 9)
    b += R(80, fl-4, 300, 6, "#a39e94", INK, 1) 
    b += dim(52, fl-60, sx, fl-60, "36\" (914 mm) unshielded")
    b += dim(52, 160, sx+35, 160, "18\" (457 mm)")
    b += t(60, 150, "pipe to combustibles:", 9, "start", fill="#44525e")
    b += R(70, fl-150, 4, 120, "#cfd8dc", INK, 1) + t(75, fl-160, "sheet-metal shield, 1\" air gap:", 9, "start", "600", BLUE) + t(75, fl-148, "cuts 36\" to about 12\"", 9, "start", "600", BLUE)
    b += dim(sx+sw_, fl+0-15, 380, fl-15, "18\" hearth in front", -0)
    b += t(80, fl+28, "non-combustible hearth pad under stove, 18\" (457 mm) on the loading side, 8\" (203 mm) on other sides", 9)
    b += t(80, fl+42, "Unlisted stove values (NFPA 211). Listed stoves: follow the label. Never vent into a chimney flue used by another appliance.", 9, fill="#44525e")
    # right: 3-2-10 rule
    ox = 470; rb = 360
    b += P([(ox, rb), (ox+150, 210), (ox+300, rb)], "#cfd8dc", INK, 1.5)
    cx = ox+215
    b += R(cx, 120, 30, 200, "#b85c38", INK, 1.2)
    for yy in range(126, 320, 12): b += L(cx, yy, cx+30, yy, "#7a3b22", 0.6)
    roof_y_at = lambda x: 210 + (x-(ox+150))*(150/150)
    yc = roof_y_at(cx)
    b += dim(cx+42, yc, cx+42, 120, "") + t(cx+46, (yc+120)/2+4, "≥ 3 ft (0.9 m)", 9.5, "start", "700") + t(cx+46, (yc+120)/2+16, "above roof", 9, "start")
    b += L(cx-120, 120, cx, 120, RED, 1, "4 3") 
    b += L(cx-120, 144, cx-120, 120, RED, 1)
    b += dim(cx-120, 105, cx, 105, "10 ft (3 m) horizontal")
    b += t(cx-125, 150, "≥ 2 ft (0.6 m) higher than", 9.5, "end", "700", RED) + t(cx-125, 162, "any roof within 10 ft", 9.5, "end", fill=RED)
    b += t(ox+150, 30, "The 3-2-10 rule", 13, "middle", "700") + t(ox+150, 46, "chimney height for good draft & sparks", 9.5, "middle", fill="#44525e")
    b += t(ox, rb+30, "2\" (51 mm) air space between masonry chimney and framing;", 9) + t(ox, rb+43, "metal chimney: listed clearance (usually 2\"). Spark arrestor cap.", 9)
    b += t(ox, 70, "Through-wall/roof: use a listed thimble or", 9) + t(ox, 82, "Class A insulated chimney — never bare pipe.", 9, "start", "600", RED)
    return svg(W, H, b, "Stove and chimney clearances")

# ---------------------------------------------------------------- rocket mass heater
def rocket():
    W, H = 760, 330
    b = R(0, 0, W, H, "#fff", "none")
    fl = 280
    b += R(0, fl, W, 50, CONC, "none")
    # feed tube
    fx = 70
    b += R(fx, 120, 40, fl-120-20, "#fff", INK, 2) + t(fx+20, 112, "feed tube", 9.5, "middle", "700")
    for i in range(5): b += L(fx+8+i*6, 125, fx+8+i*6, 200, WDK, 3)
    # burn tunnel
    b += R(fx, fl-60, 160, 40, "#ffe0b2", INK, 2) + t(fx+60, fl-23, "burn tunnel", 9.5, "middle", "700")
    # heat riser
    rx = 190
    b += R(rx, 80, 40, fl-60-80+40, "#ffccbc", INK, 2) 
    b += R(rx-14, 80, 14, fl-100, "url(#ins)", "#8a7d5a", 0.8) + R(rx+40, 80, 14, fl-100, "url(#ins)", "#8a7d5a", 0.8)
    b += t(rx+20, 70, "insulated heat riser", 9.5, "middle", "700")
    # barrel
    b += R(rx-40, 50, 120, fl-60-50+40, "none", STEEL, 3, 'rx="8"') + t(rx+20, 42, "steel barrel radiates heat", 9, "middle", fill=STEEL)
    # flames arrows
    b += arrow(fx+20, 150, fx+20, fl-40, RED, 2, "arr") + arrow(fx+40, fl-40, rx+10, fl-40, RED, 2, "arr") + arrow(rx+20, fl-50, rx+20, 90, RED, 2, "arr")
    b += arrow(rx+60, 70, rx+70, fl-45, "#b97800", 1.6) 
    # mass bench
    bx = 300
    b += R(rx+80, fl-60, bx-rx-70, 20, '#fff', INK, 1) + arrow(rx+82, fl-50, bx+15, fl-50, '#8a8a8a', 1.4)
    b += R(bx, fl-90, 420, 90, "#d7c4a3", WDK, 1.5) + t(bx+210, fl-95, "cob / stone thermal-mass bench (stores heat 12–24 h)", 9.5, "middle", "700")
    b += R(bx+10, fl-60, 380, 20, "#fff", INK, 1) + arrow(bx+20, fl-50, bx+380, fl-50, "#8a8a8a", 1.4)
    b += R(bx+390, fl-200, 20, 160, "#7d8b96", INK, 1) + arrow(bx+400, fl-60, bx+400, fl-210, "#8a8a8a", 1.4) + t(bx+380, fl-205, "exhaust to chimney", 9, "end")
    b += lead(bx+200, fl-50, bx+200, fl-130) + t(bx+120, fl-134, "flue duct inside mass", 9)
    b += t(10, 22, "J-tube rocket mass heater (section)", 12, "start", "700")
    b += t(10, fl+20, "Same cross-section area through feed, tunnel, riser and duct (e.g., 6\" ≈ 28 in²). Riser ≈ 3–4× tunnel length tall. Exhaust must still be warm enough to draft.", 9)
    b += t(10, fl+34, "Not covered by most codes; smoke-back and CO risk — CO alarm required, clean-outs at every bend, test draft before closing up the mass.", 9, "start", "600", RED)
    return svg(W, H, b, "Rocket mass heater")

# ---------------------------------------------------------------- outhouse
def outhouse():
    W, H = 760, 380
    b = R(0, 0, W, H, "#fff", "none")
    g = 200
    b += R(0, g, W, H-g, SOIL, "none", extra='opacity="0.6"')
    wt = 340
    b += f'<path d="M0,{wt} C200,{wt-10} 500,{wt+10} {W},{wt-5}" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="7 4"/>'
    b += t(330, wt-8, "seasonal HIGH water table", 9.5, "start", "700", BLUE)
    # outhouse
    ox = 140
    b += R(ox, 60, 150, g-60, "#e7d1b0", WDK, 1.5) + P([(ox-15, 60), (ox+75, 25), (ox+165, 60)], "#7d8b96", INK, 1.5)
    b += R(ox+20, 140, 110, 30, WOOD, WDK, 1) + t(ox+75, 160, "seat box + lid", 9, "middle")
    b += R(ox-12, g-6, 174, 12, WOOD2, WDK, 1) + t(ox-16, g-12, "sill on pad", 8.5, "end")
    # pit
    b += R(ox+20, g+6, 110, 90, "#8d6e4a", INK, 1.2, 'fill-opacity="0.7"') + t(ox+75, g+50, "PIT", 11, "middle", "700", "#fff")
    b += t(ox+75, g+64, "1–1.5 m deep", 9, "middle", fill="#fff")
    b += R(ox+14, g+6, 6, 90, WOOD2, WDK, 0.8) + R(ox+130, g+6, 6, 90, WOOD2, WDK, 0.8) + lead(ox+136, g+40, ox+190, g+40) + t(ox+194, g+44, "cribbed walls (top 0.5 m at least)", 9)
    b += dim(ox+75, g+96, ox+75, wt, "") + t(ox+80, (g+96+wt)/2+4, "≥ 1.2 m (4 ft)", 9.5, "start", "700", RED)
    # vent
    b += R(ox+120, 15, 10, 130, "#9e9e9e", INK, 1) + t(ox+135, 22, "vent pipe, screened", 9) + t(ox+135, 34, "(black, sunny side)", 9)
    b += R(ox+20, 70, 18, 14, "#fff", INK, 1) + t(ox+14, 80, "fly screen", 8.5, "end")
    b += t(ox+200, g+80, "Mound soil around the base to shed rain.", 9) 
    # well
    wx = 640
    b += R(wx, 110, 40, g-110, "#cfd8dc", INK, 1.2) + R(wx+12, g, 16, wt+20-g, LBLUE, BLUE, 1) + t(wx+20, 100, "well", 10, "middle", "700", BLUE)
    b += dim(ox+150, 120, wx, 120, "≥ 30 m (100 ft), and DOWNHILL of the well")
    b += t(10, 22, "Pit privy (outhouse) — section", 12, "start", "700")
    b += t(10, H-8, "Add a scoop of ash, lime or sawdust after each use. When waste is 0.5 m (18 in) from the top: fill with soil, mound it, move the shelter.", 9, italic=True)
    return svg(W, H, b, "Outhouse section")

# ---------------------------------------------------------------- felling
def felling():
    W, H = 760, 260
    b = R(0, 0, W, H, "#fff", "none")
    # side view of trunk with notch & back cut
    x, w_ = 80, 80
    b += R(x, 30, w_, 210, WOOD, WDK, 1.2)
    b += P([(x+w_, 150), (x+w_-26, 150), (x+w_, 120)], "#fff", INK, 1)
    b += L(x, 158, x+w_-26+2, 158, RED, 2)
    b += t(x+w_+8, 128, "open-face notch", 9.5, "start", "700") + t(x+w_+8, 140, "¼–⅓ diameter deep", 9)
    b += t(x-6, 162, "back cut", 9.5, "end", "700", RED) + t(x-6, 174, "slightly above", 9, "end", fill=RED) + t(x-6, 186, "notch floor", 9, "end", fill=RED)
    b += R(x+w_-34, 150, 8, 8, AMBER, "none") + lead(x+w_-30, 158, x+w_+40, 200) + t(x+w_+42, 204, "hinge ≈ 10% of diameter", 9.5, "start", "700", "#8a5a00")
    b += t(x+w_+42, 216, "— never cut through it", 9, fill="#8a5a00")
    b += arrow(x+w_+20, 60, x+w_+90, 60, INK, 2) + t(x+w_+30, 52, "fall direction", 9.5)
    # top view escape routes
    cx, cy = 560, 140
    b += C(cx, cy, 16, WOOD, WDK, 1.2)
    b += arrow(cx, cy, cx, 30, INK, 2.4) + t(cx+6, 40, "planned fall", 9.5, "start", "700")
    for ang in (135, 225):
        a = math.radians(ang - 90)
        b += arrow(cx, cy, cx+120*math.cos(a), cy+120*math.sin(a), GRN, 2.4)
    b += t(cx-150, 250, "escape routes ~45° back from the line of fall", 9.5, "start", "700", GRN)
    b += f'<path d="M{cx-90},{cy-50} A 110 110 0 0 1 {cx+90} {cy-50}" fill="none" stroke="{RED}" stroke-dasharray="5 3"/>'
    b += t(cx-250, cy-75, "keep everyone 2 tree-", 9.5, "start", "700", RED) + t(cx-250, cy-62, "lengths away", 9.5, "start", "700", RED)
    b += t(cx, cy+55, "TOP VIEW", 9, "middle", "700", "#44525e") + t(x+40, 254, "SIDE VIEW", 9, "middle", "700", "#44525e")
    return svg(W, H, b, "Tree felling")

# ---------------------------------------------------------------- rain catchment
def catchment():
    W, H = 760, 290
    b = R(0, 0, W, H, "#f7fbff", "none")
    g = 250
    b += R(0, g, W, 40, GROUND, "none")
    b += R(60, 120, 260, g-120, "#fff", INK, 1.5) + P([(30, 125), (190, 40), (350, 125)], "#9aa7b0", INK, 1.5)
    b += t(190, 100, "metal roof (best for drinking water)", 9, "middle")
    b += f'<path d="M340,122 q 0 14 12 14 q 12 0 12 -14" fill="#cfd8dc" stroke="{INK}"/>' + t(372, 118, "gutter 1:200 slope (~1/16\" per ft)", 9)
    b += R(352, 134, 10, 40, "#cfd8dc", INK, 1)
    b += R(352, 170, 90, 10, "#cfd8dc", INK, 1) 
    b += R(372, 180, 12, 60, "#cfd8dc", INK, 1) + t(386, 230, "first-flush", 9, "start", "700") + t(386, 242, "diverter", 9)
    b += R(440, 140, 14, 40, "#cfd8dc", INK, 1) + t(458, 152, "leaf screen", 9)
    b += R(470, 160, 140, g-160, LBLUE, BLUE, 1.6, 'rx="10"') + t(540, 205, "CISTERN", 11, "middle", "700", BLUE) + t(540, 220, "covered, opaque,", 9, "middle", fill=BLUE) + t(540, 232, "screened vents", 9, "middle", fill=BLUE)
    b += R(610, 175, 50, 6, "#cfd8dc", INK, 1) + t(665, 172, "overflow", 9) + t(665, 194, "away from house", 9)
    b += R(480, g-14, 10, 10, "#7d8b96") + t(470, g+18, "tap ≥ 10 cm above floor", 9)
    b += t(10, 22, "Gutters to rainwater catchment", 12, "start", "700")
    b += t(10, 280, "Yield: 1 inch of rain on 1,000 ft² of roof ≈ 623 US gal (1 mm on 1 m² = 1 L), less ~15–25% losses. Treat before drinking (see Water volume).", 9, italic=True)
    return svg(W, H, b, "Rain catchment")

def tw(x, y, s, size=9.5, anchor="start", weight="normal", fill=INK):
    import diagrams; size = size * diagrams.TSCALE
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}" stroke="#fff" stroke-width="3" paint-order="stroke">{s}</text>'

def shelters():
    b = R(0, 0, 760, 300, "#f7f9fa", "none")
    g = 250
    b += R(0, g, 760, 50, GROUND, "none")
    # lean-to side view: ridge pole end-on at (160,130) on a post/tree; poles slope back to ground
    b += L(165, g, 165, 115, WDK, 7) + t(170, 108, "tree / post", 9)
    b += P([(160, 128), (172, 132), (40, g), (22, g)], "#6b8e4e", "#3e6b30", 1)
    for k in range(5): b += L(150-k*24, 140+k*22, 125-k*24, 150+k*22, "#3e6b30", 3)
    b += C(162, 130, 7, WOOD2, WDK, 1.5)
    b += f'<path d="M 200 {g} q 12 -34 24 0 z" fill="{AMBER}"/>' + t(212, g+14, "fire", 9.5, "middle", "600", RED)
    for k in range(4): b += R(250, g-14-k*14, 12, 14, WOOD2, WDK, 0.8)
    b += t(256, g-66, "reflector", 9, "middle") + t(256, g-55, "wall", 9, "middle")
    b += t(130, 30, "Lean-to", 14, "middle", "700") + t(130, 48, "fire + reflector in front", 10, "middle", fill="#44525e")
    b += lead(162, 130, 60, 85) + t(20, 78, "ridge pole (end view), lashed", 9.5)
    b += lead(95, 190, 60, 275) + t(20, 290, "boughs/bark laid bottom-up", 9.5)
    # debris hut
    x0 = 330
    b += P([(x0-10,g),(x0+190,g-82),(x0+215,g)], "#8d6e4a", "none", extra='opacity="0.6"')
    b += L(x0, g, x0+190, g-70, WDK, 5) + L(x0+175, g, x0+190, g-70, WDK, 4) + L(x0+205, g, x0+190, g-70, WDK, 4)
    b += t(x0+100, 30, "Debris hut", 14, "middle", "700") + t(x0+100, 48, "one person; no fire needed", 10, "middle", fill="#44525e")
    b += lead(x0+90, g-42, x0+70, 90) + t(x0+20, 86, "leaves/needles ≥ 60–90 cm thick", 9.5)
    b += lead(x0+120, g-8, x0+150, 120) + t(x0+110, 114, "dry leaf bed inside", 9.5)
    b += t(x0, g+30, "entrance downwind; plug with a debris pile", 9.5)
    # tarp A-frame
    x0 = 570
    b += L(x0-10, g, x0+10, g-125, WDK, 3) + L(x0+190, g, x0+170, g-125, WDK, 3) + L(x0, g-110, x0+180, g-110, INK, 1.5)
    b += P([(x0+20,g-110),(x0+160,g-110),(x0+210,g),(x0+70,g)], "#9cc9ea", BLUE, 1.2) + P([(x0+20, g-110), (x0-30, g), (x0+70, g)], LBLUE, BLUE, 1.2)
    b += t(x0+90, 30, "Tarp A-frame", 14, "middle", "700") + t(x0+90, 48, "fast; ridge line between trees", 10, "middle", fill="#44525e")
    b += lead(x0+130, g-110, x0+150, 80) + t(x0+80, 76, "taut-line hitch ridge", 9.5)
    b += t(x0-10, g+30, "stake corners; ground pad essential", 9.5)
    return svg(760, 300, b, "Emergency shelters")

def roof_pitch():
    W, H = 760, 360
    b = R(0, 0, W, H, "#fff", "none")
    ox, oy, run = 60, 330, 250
    b += L(ox, oy, ox+run+10, oy, INK, 1.5) + t(ox+run/2, oy+18-4, "", 10)
    data = [(1, "1:12 sod/membrane only", "#9e9e9e"), (3, "3:12 min. metal panels", STEEL), (4, "4:12 shingles, shakes (min)", "#6d4c41"),
            (6, "6:12 general rain", BLUE), (8, "8:12 heavy snow", "#1f4e5f"), (12, "12:12 (45°) thatch min.", "#8a5a00")]
    for rise, lab, col in data:
        ang = math.degrees(math.atan(rise/12))
        y2 = oy - run*rise/12
        b += L(ox, oy, ox+run, y2, col, 2.4)
        b += t(ox+run+8, y2+4, f"{lab}  ({ang:.0f}°)", 10, "start", "600", col)
    b += L(ox+run, oy, ox+run, oy-run, "#c5ccd2", 1, "3 3") + t(ox+run/2, oy-4, "run = 12", 9.5, "middle", "600")
    b += t(ox+run-6, oy-run+40, "rise", 9.5, "end", fill="#44525e")
    b += t(10, 22, "Roof pitch = inches of rise per 12 inches of run.  Angle = arctan(rise ÷ 12).", 10.5, "start", "700")
    b += t(10, 38, "Steeper sheds rain and snow faster but uses more material and catches more wind.", 9.5, fill="#44525e")
    b += t(560, 120, "Snow country: 8:12–12:12 so snow", 9.5, "start", "600") + t(560, 134, "slides; metal sheds best.", 9.5)
    b += t(560, 160, "Hurricane coasts: 4:12–6:12 hip", 9.5, "start", "600") + t(560, 174, "roofs resist uplift best.", 9.5)
    b += t(560, 200, "Sod roofs: 3:12–6:12 (heavy;", 9.5, "start", "600") + t(560, 214, "steeper slides off).", 9.5)
    return svg(W, H, b, "Roof pitch guide")

def passive_solar(lat=40):
    W, H = 760, 380
    b = R(0, 0, W, H, "#f7fbff", "none")
    g = 300
    b += R(0, g, W, 80, GROUND, "none")
    x0, x1 = 240, 600
    b += R(x0, 150, x1-x0, g-150, "#fff", INK, 2)
    b += P([(x0-90, 150), (x0+180, 60), (x1+20, 150)], "#cfd8dc", INK, 1.5)
    b += t(x0+180, 52, "insulated roof", 9.5, "middle")
    b += R(x0-4, 175, 8, 95, LBLUE, BLUE, 1.5)
    b += tw(x0+12, 186, "south glass ≈ 7–12%", 9.5, "start", "600", BLUE) + tw(x0+12, 198, "of floor area", 9, "start", "normal", BLUE)
    b += R(x0, g-22, x1-x0, 22, CONC, INK, 1)
    b += t(x0+170, g-7, "dark thermal-mass floor (stone, brick, earth, slab)", 9.5, "middle", "600")
    b += R(x0, g, x1-x0, 10, "url(#ins)", "#8a7d5a", 0.8) + t(x1+8, g+22, "insulation under", 9) + t(x1+8, g+34, "and around mass", 9)
    b += R(x0+240, 170, 30, g-192, "#c49a6c", INK, 1) + t(x0+255, 165, "mass wall", 9, "middle")
    ws = 90 - lat - 23.45; ss = 90 - lat + 23.45
    a = math.radians(ws)
    for dy in (180, 230, 268):
        xa, ya = x0-250*math.cos(a), dy-250*math.sin(a)
        b += L(xa, ya, x0, dy, AMBER, 2.2)
        xf = x0 + (g-22-dy)/math.tan(a)
        b += L(x0, dy, xf, g-22, AMBER, 1.6, "5 3")
    b += t(10, g+22, f"Winter noon sun ≈ {ws:.0f}° (at {lat}°N): low, enters deep, heats the mass", 10, "start", "700", "#b97800")
    a = math.radians(ss)
    xo, yo = x0-90+2, 150+1
    xa, ya = xo-125*math.cos(a), yo-125*math.sin(a)
    b += L(xa, ya, xo, yo, RED, 2.4)
    b += t(10, 22, f"Summer noon sun ≈ {ss:.0f}°: high — overhang shades the glass", 10, "start", "700", RED)
    b += lead(x0-70, 148, x0-10, 100) + t(x0-5, 98, "overhang sized for latitude", 9.5, "start", "600")
    b += R(x1-4, 190, 8, 30, LBLUE, BLUE, 1) + t(x1+12, 200, "few, small", 9.5) + t(x1+12, 212, "north windows", 9.5) + t(x1+60, 250, "earth berm /", 9) + t(x1+60, 262, "storage on north", 9)
    b += P([(x1, g), (x1, 230), (x1+150, g)], SOIL, GSTROKE, 1)
    b += t(10, g+50, "◄ SOUTH", 11, "start", "700") + t(W-10, g+50, "NORTH ►", 11, "end", "700")
    b += t(W/2, H-8, "Noon solar altitude = 90° − latitude ± 23.45° (+ late June, − late December).", 9.5, "middle", italic=True)
    return svg(W, H, b, "Passive solar section")

def chimney():
    W, H = 780, 460
    b = R(0, 0, W, H, "#fff", "none")
    fl = 390
    b += R(0, fl, 440, 12, WOOD, WDK, 1)
    b += R(40, 60, 12, fl-60, "#e8e2d6", INK, 1) + t(46, 52, "combustible wall", 9, "middle")
    sx, sw_, sh = 220, 90, 80
    b += R(sx, fl-sh-25, sw_, sh, "#4a4a4a", INK, 1.5) + R(sx+8, fl-25, 8, 25, "#4a4a4a") + R(sx+sw_-16, fl-25, 8, 25, "#4a4a4a")
    b += t(sx+sw_/2, fl-sh/2-20, "STOVE", 10, "middle", "700", "#fff")
    b += R(sx+35, 70, 20, fl-sh-25-70, "#7d8b96", INK, 1) + t(sx+62, 100, "single-wall", 9) + t(sx+62, 111, "stovepipe", 9)
    b += R(90, fl-4, 330, 6, "#a39e94", INK, 1)
    b += dim(52, fl-60, sx, fl-60, "36\" (914 mm) unshielded")
    b += dim(52, 170, sx+35, 170, "18\" (457 mm) pipe")
    b += R(72, fl-170, 4, 140, "#cfd8dc", BLUE, 1.5) + tw(80, fl-184, "sheet-metal shield on 1\" spacers:", 9, "start", "600", BLUE) + tw(80, fl-172, "36\" → about 12\"", 9, "start", "600", BLUE)
    b += dim(sx+sw_, fl-15, 420, fl-15, "18\" front")
    b += t(20, fl+26, "Non-combustible hearth pad: 18\" (457 mm) on the", 9) + t(20, fl+38, "loading side, 8\" (203 mm) on the other sides. Unlisted-", 9) + t(20, fl+50, "stove values (NFPA 211); listed stoves: follow the label.", 9, fill="#44525e")
    # right: 3-2-10 rule; roof slope rising to the right
    ox = 470
    eave = (ox, 380); ridge = (ox+300, 200)
    slope = (eave[1]-ridge[1])/(ridge[0]-eave[0])
    ry = lambda x: eave[1] - (x-eave[0])*slope
    b += P([eave, ridge, (ridge[0], 380)], "#cfd8dc", INK, 1.5)
    cx = ox+70
    top = ry(cx+120) - 40
    b += R(cx-14, top, 28, ry(cx)-top+6, "#b85c38", INK, 1.2)
    for yy in range(int(top)+6, int(ry(cx)), 12): b += L(cx-14, yy, cx+14, yy, "#7a3b22", 0.6)
    # 10 ft horizontal from chimney to roof
    xh = cx+120; yh = ry(xh)
    b += L(cx+14, yh, xh, yh, RED, 1.2, "4 3") + t((cx+xh)/2+6, yh+14, "10 ft (3 m)", 9.5, "middle", "700", RED)
    b += L(xh, yh, xh, top, RED, 1.2) + t(xh+6, (yh+top)/2+4, "≥ 2 ft (0.6 m)", 9.5, "start", "700", RED)
    b += L(cx+14, top, xh, top, RED, 0.8, "2 2")
    b += dim(cx-30, ry(cx), cx-30, top, "") + t(cx-36, (ry(cx)+top)/2, "≥ 3 ft", 9.5, "end", "700") + t(cx-36, (ry(cx)+top)/2+12, "(0.9 m)", 9, "end")
    b += t(ox-10, 30, "The 3-2-10 rule", 13, "start", "700") + t(ox-10, 46, "≥ 3 ft above where it exits the roof AND ≥ 2 ft higher than", 9.5, fill="#44525e") + t(ox-10, 58, "any roof, ridge or wall within 10 ft horizontally.", 9.5, fill="#44525e")
    b += t(ox-10, 84, "Through walls/roofs: listed thimble or Class A", 9, "start", "600", RED) + t(ox-10, 96, "insulated chimney — never bare stovepipe.", 9, "start", "600", RED)
    b += t(ox-10, fl+28, "Masonry chimney: 2\" (51 mm) air space to framing.", 9) + t(ox-10, fl+42, "Cap with a spark arrestor; clean when soot ≥ ⅛\" (3 mm).", 9)
    return svg(W, H, b, "Stove and chimney clearances")

def wall_section():
    W, H = 780, 640
    b = R(0, 0, W, H, "#fff", "none")
    g = 490; wx = 345
    b += R(0, g, W, H-g, SOIL, "none", extra='opacity="0.55"')
    # gravel + drain outside stem
    b += P([(wx-90, g+105), (wx-20, g+105), (wx-20, g+30), (wx-90, g+50)], "#d8d4cb", "#8b857a", 0.6)
    b += C(wx-45, g+90, 8, "#fff", BLUE, 1.6)
    # stem + footing
    b += R(wx-20, g-60, 120, 140, CONC, INK, 1.2) + R(wx-50, g+80, 180, 25, CONC, INK, 1.2)
    # sill & floor
    b += R(wx-5, g-70, 105, 10, WOOD2, WDK, 1) + L(wx-6, g-60, wx+100, g-60, "#000", 2.2)
    b += R(wx-5, g-100, 10, 30, WOOD2, WDK, 1)  # rim joist
    b += R(wx+5, g-100, W-wx-5, 30, "url(#ins)", "#8a7d5a", 0.6) + R(wx+5, g-106, W-wx-5, 6, WOOD, WDK, 1)
    # wall: bottom plate g-112..g-106; studs 150..g-112; top plates 136..150
    top = 150; bot = g-112
    b += R(wx-5, bot, 98, 6, WOOD2, WDK, 1)
    b += R(wx, top, 88, bot-top, "url(#ins)", "#8a7d5a", 0.8)
    b += R(wx+88, top, 6, bot-top+6, "#e8e2d6", INK, 1)
    b += L(wx+86, top, wx+86, bot, RED, 1.4, "6 3")
    b += R(wx-12, top, 12, g-100-top, "#c9a46e", WDK, 1)
    b += R(wx-16, top, 4, g-100-top, "#fff", "#8a7d5a", 0.6)
    for yy in range(top+20, g-110, 30): b += R(wx-26, yy, 10, 18, WOOD, WDK, 0.5)
    b += R(wx-34, 150, 8, g-65-150, "#e0c08f", WDK, 1)
    b += R(wx-5, top-14, 98, 7, WOOD2, WDK, 1) + R(wx-5, top-7, 98, 7, WOOD2, WDK, 1)
    # rafter (6:12) seated on outside corner of top plate
    pt = (wx-5, top-14)
    def yb(x): return pt[1] - 0.5*(x-pt[0])
    xe, xr = wx-130, W
    b += P([(xe, yb(xe)), (xr, yb(xr)), (xr, yb(xr)-34), (xe, yb(xe)-34)], WOOD, WDK, 1)
    b += P([(xe, yb(xe)-34), (xr, yb(xr)-34), (xr, yb(xr)-42), (xe, yb(xe)-42)], "#7d8b96", INK, 1)
    b += R(xe-6, yb(xe)-36, 6, 38, WOOD2, WDK, 1)  # fascia
    # ceiling + attic insulation
    b += R(wx+94, top-14, W-wx-94, 6, "#e8e2d6", INK, 1)
    b += P([(wx+10, top-14), (W, top-14), (W, yb(W)-2), (wx+10, yb(wx+10)-2)], "url(#ins)", "#8a7d5a", 0.5)
    # gutter
    b += f'<path d="M{xe-26},{yb(xe)-30} q 0 18 14 18 q 14 0 14 -18" fill="#cfd8dc" stroke="{INK}"/>'
    def ll(x, y, s_, col=INK):
        return f'<line x1="{x}" y1="{y}" x2="{wx-100}" y2="{y}" stroke="{col}" stroke-width="0.8"/><circle cx="{x}" cy="{y}" r="2.2" fill="{col}"/>' + tw(wx-104, y+3.5, s_, 9.5, "end", fill=col)
    def lr(x, y, s_, col=INK):
        return f'<line x1="{x}" y1="{y}" x2="{wx+140}" y2="{y}" stroke="{col}" stroke-width="0.8"/><circle cx="{x}" cy="{y}" r="2.2" fill="{col}"/>' + tw(wx+144, y+3.5, s_, 9.5, "start", fill=col)
    b += ll(xe+10, yb(xe+10)-40, "metal / shingle roofing on battens") if False else ""
    b += tw(xe-12, yb(xe)+24, "eave overhang 45–60 cm (18–24\")", 9.5, "end") + tw(xe-12, yb(xe)+36, "+ gutter & drip edge", 9.5, "end")
    b += ll(wx-30, 270, "siding (boards, shakes, salvaged metal)")
    b += ll(wx-21, 305, "19 mm (¾\") air gap on furring strips")
    b += ll(wx-14, 340, "weather barrier (house wrap / tar paper)")
    b += ll(wx-6, 375, "sheathing (diagonal boards or plywood)")
    b += ll(wx-20, g-20, "foundation top ≥ 20 cm (8\") above grade")
    b += ll(wx-45, g+90, "gravel + perforated drain to daylight", BLUE)
    b += lr(wx+44, 250, "cavity insulation (see insulation table)")
    b += lr(wx+86, 290, "warm-side vapor retarder (cold climates only)", RED)
    b += lr(wx+91, 330, "interior finish (boards, plaster, drywall)")
    b += f'<line x1="{wx+50}" y1="{top-4}" x2="{wx+140}" y2="{top+14}" stroke="{INK}" stroke-width="0.8"/><circle cx="{wx+50}" cy="{top-4}" r="2.2" fill="{INK}"/>' + tw(wx+144, top+17, "doubled top plate; strap rafter to it")
    b += lr(wx+50, g-65, "sill plate on gasket + capillary break")
    b += lr(wx+200, g-85, "insulated floor over vented crawl")
    b += tw(wx+200, 80, "ceiling insulation", 9.5, "start", "700") + tw(wx+200, 92, "R-38 to R-60 in cold climates", 9.5)
    b += t(10, 20, "OUTSIDE", 11, "start", "700", "#44525e") + t(W-10, 20, "INSIDE", 11, "end", "700", "#44525e")
    b += t(10, H-8, "Cold-climate stick-frame wall. In hot-humid climates omit the interior vapor retarder so the wall dries inward.", 9, italic=True)
    return svg(W, H, b, "Wall section")
