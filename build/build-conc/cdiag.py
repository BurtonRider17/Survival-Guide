import math
from basediag import svg, t, lead, arrow, box, INK, BLUE, LBLUE, RED, GRN, GROUND, GSTROKE, STEEL, AMBER, region_map, REGIONS

CEM = "#9aa3ab"; SAND = "#e8cf8f"; GRAV = "#a1887f"; WAT = "#8cc4ec"; LIME = "#f4f1e6"; CONC = "#c9cdd1"
CLAY = "#c27c5a"; BRICK = "#b5523b"; WOOD = "#c9a26b"; WOODD = "#8d6e45"; EARTH = "#d8c49a"

def shifted(b, dy): return f'<g transform="translate(0,{dy})">{b}</g>'

def rect(x, y, w, h, fill, stroke=INK, sw=1, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def line(x1, y1, x2, y2, col=INK, w=1.2, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{d}/>'
def poly(pts, fill, stroke=INK, sw=1):
    return f'<polygon points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def dim(x1, y1, x2, y2, label, off=0, size=9.5, vertical=False):
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="0.8" marker-start="url(#ar)" marker-end="url(#ar)"/>'
    if vertical:
        s += t(x1 + 5 + off, (y1 + y2) / 2 + 3, label, size)
    else:
        s += t((x1 + x2) / 2, y1 - 4 + off, label, size, "middle")
    return s
def pebbles(x, y, w, h, n=40, seed=1, col=GRAV, rmax=4):
    import random
    r = random.Random(seed); s = ""
    for _ in range(n):
        s += f'<circle cx="{x + r.random()*w:.1f}" cy="{y + r.random()*h:.1f}" r="{1.5 + r.random()*(rmax-1.5):.1f}" fill="{col}" stroke="#6d4c41" stroke-width="0.4"/>'
    return s
def dots(x, y, w, h, n=120, seed=2, col="#b59b5a", r_=0.9):
    import random
    r = random.Random(seed)
    return "".join(f'<circle cx="{x + r.random()*w:.1f}" cy="{y + r.random()*h:.1f}" r="{r_}" fill="{col}"/>' for _ in range(n))
def rebar(cx, cy, r=3.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#5d4037" stroke="#3e2723" stroke-width="0.8"/>'

# ---------------------------------------------------------- 1 mix ratios + w/c curve
def mix_ratios():
    b = ""
    rows = [("Structural concrete", "1 : 2 : 3", [1, 2, 3], ["cement", "sand", "gravel"], "≈7 bags / yd³ · ~3,000–4,000 psi"),
            ("General concrete", "1 : 2 : 4", [1, 2, 4], ["cement", "sand", "gravel"], "≈6 bags / yd³ · ~2,500–3,000 psi"),
            ("Mass / lean (fill, footing pads)", "1 : 3 : 6", [1, 3, 6], ["cement", "sand", "gravel"], "≈4 bags / yd³ · ~1,500–2,000 psi"),
            ("Cement-lime mortar (Type N)", "1 : 1 : 6", [1, 1, 6], ["cement", "lime", "sand"], "bricklaying, block, stone"),
            ("Lime mortar / plaster base", "1 : 3", [1, 3], ["putty", "sand"], "old buildings, earth & soft brick"),
            ("Lime–pozzolan concrete", "1 : 2 : 3", [1, 2, 3], ["lime", "pozzolan", "aggregate"], "slow set, weeks to harden")]
    cols = {"cement": CEM, "sand": SAND, "gravel": GRAV, "lime": LIME, "putty": LIME, "pozzolan": "#8d8d6a", "aggregate": GRAV}
    unit = 23; x0 = 240; y = 34; gap = 13
    b += t(10, 18, "Parts by loose volume (one part = one bucket)", 12, weight="700")
    for name, ratio, parts, labs, note in rows:
        b += t(10, y + 15, name, 10.5, weight="600") + t(10, y + 30, ratio, 10.5, fill="#8a4b08", weight="700")
        x = x0
        for p, lab in zip(parts, labs):
            for k in range(p):
                b += rect(x + k * unit, y + 2, unit - 3, 22, cols[lab], "#5c6a75", 0.8, 3)
            b += t(x + (p * unit - 3) / 2, y + 37, lab, 8.5, "middle", "600", fill="#44525e")
            x += p * unit + gap
        n1, _, n2 = note.partition(" · ")
        b += t(x + 2, y + 13, n1, 9, fill="#44525e") + (t(x + 2, y + 26, n2, 9, fill="#44525e") if n2 else "")
        y += 50
    # w/c chart
    gx, gy, gw, gh = 70, y + 40, 300, 150
    b += t(10, y + 20, "Water–cement ratio vs 28-day strength (portland cement, no air entrainment)", 12, weight="700")
    b += rect(gx, gy, gw, gh, "#f7f9fa", "#9aa7b0", 0.8)
    pts = [(0.41, 6000), (0.48, 5000), (0.57, 4000), (0.68, 3000), (0.82, 2000)]
    X = lambda w: gx + (w - 0.35) / (0.9 - 0.35) * gw
    Y = lambda p: gy + gh - (p - 1000) / (7000 - 1000) * gh
    for p in range(1000, 7001, 1000):
        b += line(gx, Y(p), gx + gw, Y(p), "#dde3e7", 0.6) + t(gx - 6, Y(p) + 3, f"{p:,}", 8.5, "end")
    for w in [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        b += line(X(w), gy + gh, X(w), gy + gh + 4, INK, 0.8) + t(X(w), gy + gh + 15, f"{w:.1f}", 8.5, "middle")
    b += '<polyline points="' + " ".join(f"{X(w):.1f},{Y(p):.1f}" for w, p in pts) + f'" fill="none" stroke="{RED}" stroke-width="2.2"/>'
    for w, p in pts: b += f'<circle cx="{X(w):.1f}" cy="{Y(p):.1f}" r="3" fill="{RED}"/>'
    b += t(gx + gw / 2, gy + gh + 30, "water ÷ cement (by weight)", 9.5, "middle") + t(14, gy + 10, "psi", 9.5)
    b += t(gx + gw + 18, gy + 14, "How to read it:", 10, weight="700")
    notes = ["5 US gal water per 94-lb bag = 0.44", "6 gal per bag = 0.53  (good target)", "7 gal per bag = 0.62", "8 gal per bag = 0.71  (weak, porous)",
             "Every extra gallon of water per bag", "costs roughly 10–15% of strength.", "Count water already in wet sand —", "damp sand holds ~½–1 gal per bag."]
    for i, n in enumerate(notes): b += t(gx + gw + 18, gy + 30 + i * 14, n, 9.3)
    b += t(10, gy + gh + 50, "Curve: ACI 211.1 typical values (1 psi ≈ 0.0069 MPa; 3,000 psi ≈ 21 MPa).", 8.8, italic=True)
    b += t(10, gy + gh + 64, "Field-mixed concrete is usually weaker — design with margin.", 8.8, italic=True)
    return svg(720, gy + gh + 72, b, "Mix ratios and water-cement ratio")

# ---------------------------------------------------------- 2 jar test
def jar_test():
    b = ""
    def jar(x, y, w, h, layers, labels):
        s = f'<path d="M{x},{y+12} q0,-12 12,-12 h{w-24} q12,0 12,12 v{h-20} q0,8 -8,8 h{-(w-16)} q-8,0 -8,-8z" fill="#eef6fb" stroke="{INK}" stroke-width="1.4"/>'
        s += rect(x + 6, y - 14, w - 12, 14, "#90a4ae", INK, 1, 2)
        yy = y + h - 8
        for (hh, col, kind), (lab) in zip(layers, labels):
            yy -= hh
            s += rect(x + 2, yy, w - 4, hh, col, "none", 0)
            if kind == "grav": s += pebbles(x + 4, yy + 2, w - 8, hh - 4, 18, 3, GRAV, 4.5)
            if kind == "sand": s += dots(x + 4, yy + 1, w - 8, hh - 2, 140, 5, "#a78b45", 1.1)
            if kind == "silt": s += dots(x + 4, yy + 1, w - 8, hh - 2, 120, 7, "#8d7f6a", 0.6)
            if lab: s += lead(x + w + 40, yy + hh / 2, x + w - 8, yy + hh / 2) + t(x + w + 44, yy + hh / 2 + 4, lab, 9.5)
        return s, yy
    s, top = jar(40, 50, 110, 250, [(40, GRAV, "grav"), (70, SAND, "sand"), (40, "#bcae96", "silt"), (22, "#a1887f", ""), (60, "#cfe3ee", "")],
                 ["gravel (settles at once)", "sand (settles in ~1 minute)", "silt (settles in 1–2 hours)", "clay (24–48 h; water clears)", "water"])
    b += s + t(95, 20, "A. Soil / gravel-pit jar test", 11.5, "middle", "700")
    b += t(40, 330, "Fill a straight-sided jar ⅓ with soil, add water", 9.3) + t(40, 343, "to ¾ and a pinch of dish soap. Shake 2–3 min.", 9.3)
    b += t(40, 356, "Mark the top of each layer as it settles; layer", 9.3) + t(40, 369, "height ÷ total height = % of each.", 9.3)
    # B: silt test
    x2 = 400
    b += t(x2 + 55, 20, "B. Concrete-sand silt test", 11.5, "middle", "700")
    s2, _ = jar(x2, 120, 110, 180, [(70, SAND, "sand"), (8, "#8d7f6a", "silt"), (70, "#d7e9f3", "")], ["", "", ""])
    b += s2
    b += dim(x2 + 128, 300 - 8, x2 + 128, 300 - 78, "50 mm (2 in) sand", vertical=True)
    b += lead(x2 + 160, 210, x2 + 104, 218) + t(x2 + 164, 206, "silt layer after 1 hour:", 9.5, weight="700")
    b += t(x2 + 164, 220, "≤ 3 mm (⅛ in) — OK to use", 9.5, fill=GRN) + t(x2 + 164, 234, "> 3 mm (over ~6%) — wash", 9.5, fill=RED) + t(x2 + 164, 248, "the sand before use", 9.5, fill=RED)
    b += t(x2, 330, "Same jar, but only 2 in of sand and clean water to ¾.", 9.3)
    b += t(x2, 343, "Floating dark specks or tea-colored water = organic", 9.3) + t(x2, 356, "matter (leaves, peat): weakens and slows concrete.", 9.3)
    return svg(720, 380, b, "Jar tests for soil and sand")

# ---------------------------------------------------------- 3 lime kiln
def lime_kiln():
    b = ""
    # hillside ground
    b += poly([(0, 60), (150, 60), (150, 330), (0, 330)], GROUND, GSTROKE)
    b += poly([(0, 330), (720, 330), (720, 360), (0, 360)], GROUND, GSTROKE)
    b += f'<rect x="0" y="60" width="150" height="270" fill="url(#hatch)" opacity="0.6"/>'
    # kiln walls (stone), section
    b += poly([(150, 60), (200, 60), (215, 330), (150, 330)], "#9e9e9e", INK)  # back wall against hill
    b += poly([(400, 60), (450, 60), (470, 330), (390, 330)], "#9e9e9e", INK)  # front wall
    for yy in range(75, 330, 22):
        b += line(152, yy, 205 + (yy - 60) * 0.05, yy, "#757575", 0.6) + line(398 - (yy - 60) * 0.03, yy, 452 + (yy - 60) * 0.07, yy, "#757575", 0.6)
    # inner lining
    b += poly([(200, 60), (212, 60), (225, 330), (215, 330)], "#d7a184", INK, 0.6)
    b += poly([(388, 60), (400, 60), (390, 330), (378, 330)], "#d7a184", INK, 0.6)
    # fire chamber arch of large stones
    cx, cy = 300, 300
    for i in range(9):
        a0 = math.pi * i / 9; a1 = math.pi * (i + 1) / 9
        r1, r2 = 60, 82
        pts = [(cx + r1 * math.cos(a0), cy - r1 * math.sin(a0)), (cx + r2 * math.cos(a0), cy - r2 * math.sin(a0)),
               (cx + r2 * math.cos(a1), cy - r2 * math.sin(a1)), (cx + r1 * math.cos(a1), cy - r1 * math.sin(a1))]
        b += poly(pts, "#eceff1", INK, 0.9)
    # flames
    b += f'<path d="M260,300 q10,-40 25,-15 q8,-35 20,-5 q12,-30 20,5 q10,-20 15,15z" fill="{AMBER}" opacity="0.85"/>'
    b += f'<path d="M275,300 q8,-25 15,-8 q8,-20 14,2 q8,-15 12,6z" fill="#ffca28"/>'
    b += rect(250, 300, 100, 30, "#4e342e", INK, 0.8)
    for xx in range(255, 345, 14): b += line(xx, 318, xx + 10, 310, "#8d6e63", 3)
    # charge of limestone: graded sizes
    import random
    r = random.Random(4)
    for row in range(14):
        yy = 210 - row * 11
        if yy < 70: break
        xl = 220 + (210 - yy) * 0.0; xr = 384 - (210 - yy) * 0.02
        size = 9 - row * 0.4
        xx = xl + size
        while xx < xr - size:
            if not (yy > 215):
                b += f'<ellipse cx="{xx:.1f}" cy="{yy + r.random()*3:.1f}" rx="{size:.1f}" ry="{size*0.75:.1f}" fill="#f5f5f0" stroke="#90a4ae" stroke-width="0.7"/>'
            xx += size * 2 + 1
    # stones beside arch
    for xx, yy in [(232, 270), (232, 248), (368, 270), (368, 248), (240, 226), (360, 226)]:
        b += f'<ellipse cx="{xx}" cy="{yy}" rx="9" ry="7" fill="#f5f5f0" stroke="#90a4ae" stroke-width="0.7"/>'
    # draw/stoke arch in front wall
    b += rect(392, 280, 74, 50, "#3e2723", INK, 1)
    b += f'<path d="M392,280 q37,-24 74,0" fill="#3e2723" stroke="{INK}"/>'
    # heat arrows & smoke
    for xx in (260, 300, 340):
        b += arrow(xx, 200, xx, 60, RED, 1.2, "arr", "4 3")
    b += f'<path d="M290,52 q-10,-15 5,-25 q15,-10 0,-25" fill="none" stroke="#9e9e9e" stroke-width="3" opacity="0.7"/>'
    b += f'<path d="M320,52 q10,-15 -5,-25 q-15,-10 5,-25" fill="none" stroke="#9e9e9e" stroke-width="3" opacity="0.6"/>'
    # labels
    L = 490
    b += t(L, 70, "Open top: smoke and CO₂ out;", 9.8) + t(L, 83, "cap loosely with sod/iron when done", 9.8) + lead(L - 4, 74, 385, 66)
    b += t(L, 112, "Charge: fist-size limestone or shell,", 9.8, weight="700") + t(L, 125, "larger pieces low, smaller on top", 9.8) + lead(L - 4, 118, 370, 140)
    b += t(L, 152, "Stone walls 1–2 ft (0.3–0.6 m) thick,", 9.8) + t(L, 165, "fire-brick or clay lining inside", 9.8) + lead(L - 4, 158, 450, 170)
    b += t(L, 192, "Burning zone ≈ 900–1,000 °C:", 9.8, weight="700", fill=RED) + t(L, 205, "stone glows bright orange", 9.8) + lead(L - 4, 198, 350, 230)
    b += t(L, 232, "Self-supporting arch of large", 9.8) + t(L, 245, "limestone blocks over fire chamber", 9.8) + lead(L - 4, 238, 365, 262)
    b += t(L, 285, "Stoke / draw arch: feed wood for", 9.8) + t(L, 298, "2–4 days; rake out lime when cool", 9.8) + lead(L - 4, 290, 466, 300)
    b += t(10, 16, "Built into a bank: earth", 9.8) + t(10, 30, "insulates and lets you", 9.8) + t(10, 44, "load from the top", 9.8)
    b += t(10, 352, "Typical: 3 m³ (≈100 ft³) charge ≈ 1.6 t stone + 1.4 t dry wood → ≈0.9 t quicklime (Practical Action Dedza kiln).", 8.6, italic=True, fill="#44525e")
    b += t(10, 367, "Never stand on the charge or lean over the top while burning.", 8.6, italic=True, fill="#44525e")
    return svg(720, 376, b, "Simple intermittent lime kiln cross-section")

# ---------------------------------------------------------- 4 lime cycle
def lime_cycle():
    b = ""
    cx, cy, R = 360, 190, 125
    nodes = [(-90, "1. LIMESTONE", "CaCO₃", "limestone, chalk, marble,\nshells, coral, caliche", "#eceff1"),
             (0, "2. QUICKLIME", "CaO", "white lumps, ~44% lighter;\nCAUSTIC — reacts with water", "#fff3e0"),
             (90, "3. SLAKED LIME", "Ca(OH)₂", "lime putty (wet) or\nhydrated lime (dry powder)", "#e3f2fd"),
             (180, "4. CARBONATED LIME", "CaCO₃", "hard mortar / plaster in\nthe wall: 'stone' again", "#e8f5e9")]
    pos = []
    for ang, title, f, sub, col in nodes:
        a = math.radians(ang); x = cx + R * 1.55 * math.cos(a); y = cy + R * math.sin(a)
        pos.append((x, y))
        b += f'<rect x="{x-95}" y="{y-36}" width="190" height="72" rx="10" fill="{col}" stroke="{INK}" stroke-width="1.4"/>'
        b += t(x, y - 18, title, 11, "middle", "700") + t(x, y - 2, f, 13, "middle", "700", "#8a4b08")
        for i, ln in enumerate(sub.split("\n")): b += t(x, y + 14 + i * 11, ln, 9, "middle", fill="#44525e")
    steps = [("BURN 900–1,000 °C", "drives off CO₂ (2–4 days)", RED), ("SLAKE: add to water", "violent heat — boils!", RED),
             ("MIX with sand, build;", "absorbs CO₂ over months", BLUE), ("CYCLE COMPLETE", "repeat with new stone", GRN)]
    arcs = [(-58, -24), (24, 58), (122, 156), (204, 238)]
    lab = [(cx + 205, 52), (cx + 205, 318), (cx - 205, 318), (cx - 205, 52)]
    for (a0, a1), (l1, l2, col), (lx, ly) in zip(arcs, steps, lab):
        r0, r1 = math.radians(a0), math.radians(a1)
        x0, y0 = cx + R * 1.55 * math.cos(r0), cy + R * math.sin(r0)
        x1, y1 = cx + R * 1.55 * math.cos(r1), cy + R * math.sin(r1)
        m = "arr" if col == RED else ("arb" if col == BLUE else "ar")
        b += f'<path d="M{x0:.1f},{y0:.1f} A{R*1.55},{R} 0 0 1 {x1:.1f},{y1:.1f}" fill="none" stroke="{col}" stroke-width="2.4" marker-end="url(#{m})"/>'
        b += t(lx, ly, l1, 10, "middle", "700", col) + t(lx, ly + 13, l2, 9.2, "middle")
    b += t(cx, cy - 4, "THE LIME CYCLE", 13, "middle", "700", "#1f4e5f") + t(cx, cy + 12, "CaCO₃ → CaO + CO₂ → Ca(OH)₂ → CaCO₃", 9, "middle")
    return svg(720, 345, b, "The lime cycle")

# ---------------------------------------------------------- 5 footing form
def footing_form():
    b = ""
    gl = 70
    b += poly([(0, gl), (150, gl), (150, 330), (0, 330)], GROUND, GSTROKE) + poly([(570, gl), (720, gl), (720, 330), (570, 330)], GROUND, GSTROKE)
    b += poly([(0, 330), (720, 330), (720, 360), (0, 360)], GROUND, GSTROKE)
    b += f'<rect x="0" y="{gl}" width="150" height="260" fill="url(#hatch)" opacity="0.5"/><rect x="570" y="{gl}" width="150" height="260" fill="url(#hatch)" opacity="0.5"/>'
    # trench air
    b += rect(150, gl, 420, 260, "#f7f9fa", "none", 0)
    # gravel base
    b += rect(150, 300, 420, 30, "#d7ccc8", INK, 0.8) + pebbles(152, 302, 416, 26, 70, 9, GRAV, 3.5)
    # concrete footing
    b += rect(200, 230, 320, 70, CONC, INK, 1.4) + dots(204, 234, 312, 62, 160, 11, "#8a9097", 1)
    # forms 2x10 boards
    b += rect(186, 226, 14, 74, WOOD, WOODD, 1) + rect(520, 226, 14, 74, WOOD, WOODD, 1)
    # stakes
    b += poly([(172, 200), (186, 200), (186, 318), (179, 330), (172, 318)], WOOD, WOODD) + poly([(534, 200), (548, 200), (548, 318), (541, 330), (534, 318)], WOOD, WOODD)
    # spreader
    b += rect(172, 192, 376, 10, WOOD, WOODD, 1)
    # rebar on chairs (3 bars)
    for xx in (260, 360, 460):
        b += rebar(xx, 276, 4.5) + rect(xx - 5, 280, 10, 20, "#bdbdbd", INK, 0.6)
    # key way
    b += rect(330, 230, 60, 14, "#ffe0b2", INK, 0.8)
    # stem wall dowels
    b += line(320, 276, 320, 140, "#5d4037", 3) + line(400, 276, 400, 140, "#5d4037", 3)
    b += line(320, 276, 345, 276, "#5d4037", 3) + line(400, 276, 375, 276, "#5d4037", 3)
    # frost line
    b += line(0, 215, 720, 215, BLUE, 1.5, "8 5") + t(712, 210, "frost line (local depth)", 9.5, "end", fill=BLUE)
    # dimensions
    b += dim(200, 352, 520, 352, "W ≈ 2 × wall thickness (min 12 in / 300 mm);  T ≥ wall thickness (min 6–8 in)", off=-2)
    b += dim(560, 230, 560, 300, "", vertical=True) + t(566, 300, "T", 10, weight="700")
    b += dim(110, 300, 110, 215, "", vertical=True) + t(10, 250, "bottom ≥ 6 in", 9.5) + t(10, 263, "(150 mm) below", 9.5) + t(10, 276, "frost line", 9.5)
    # labels
    b += t(160, 40, "Spreader cleat ties form tops together", 9.8) + lead(250, 44, 260, 193)
    b += t(400, 40, "Vertical dowels for stem wall / block cores", 9.8) + lead(420, 44, 400, 150)
    b += t(600, 100, "2×10 or plank", 9.8) + t(600, 113, "forms, oiled", 9.8) + lead(598, 108, 528, 240)
    b += t(600, 140, "Stakes every", 9.8) + t(600, 153, "2–3 ft (0.6–0.9 m)", 9.8) + lead(598, 150, 545, 210)
    b += t(585, 245, "2–3 #4 (½ in) bars,", 9.8) + t(585, 258, "≥ 3 in (75 mm) cover,", 9.8) + t(585, 271, "on stone/brick chairs", 9.8) + lead(583, 254, 466, 276)
    b += t(10, 120, "Firm, undisturbed", 9.8) + t(10, 133, "soil; remove topsoil", 9.8) + t(10, 146, "and roots", 9.8)
    b += t(395, 242, "keyway (optional)", 8.8) 
    b += t(10, 320, "Compacted gravel 4–6 in", 9.3)
    return svg(720, 362, b, "Footing form cross-section")

# ---------------------------------------------------------- 6 well ring mold
def well_ring_mold():
    b = ""
    # plan view
    cx, cy = 170, 190
    b += t(cx, 22, "A. PLAN (looking down)", 11, "middle", "700")
    b += f'<circle cx="{cx}" cy="{cy}" r="140" fill="none" stroke="{STEEL}" stroke-width="8"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="132" fill="{CONC}" stroke="{INK}" stroke-width="0.8"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="112" fill="#fff" stroke="{INK}" stroke-width="0.8"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="108" fill="none" stroke="{STEEL}" stroke-width="8"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="122" fill="none" stroke="#5d4037" stroke-width="1.6" stroke-dasharray="6 3"/>'
    for a in range(0, 360, 30):
        x = cx + 122 * math.cos(math.radians(a)); y = cy + 122 * math.sin(math.radians(a)); b += rebar(f"{x:.1f}", f"{y:.1f}", 2.6)
    # split joints with wedges
    for a in (0, 180):
        x = cx + 140 * math.cos(math.radians(a)); b += rect(x - 6, cy - 8, 12, 16, AMBER, INK, 0.8)
    b += rect(cx - 10, cy - 116, 20, 12, AMBER, INK, 0.8)
    b += dim(cx - 112, cy, cx + 112, cy, "inside Ø 1.0–1.2 m (40–48 in)")
    b += lead(250, 48, 231, 84) + t(240, 44, "concrete wall 75–100 mm", 9.5)
    b += t(10, 365, "Outer shell: 2 halves, bolted/wedged. Inner shell: 3 segments", 9) + t(10, 377, "with a key piece (top) that is pulled first to collapse it.", 9)
    # section
    X = 400; Y = 70
    b += t(560, 22, "B. SECTION through one wall", 11, "middle", "700")
    b += rect(X, Y, 10, 230, STEEL, INK, 0.8) + rect(X + 80, Y, 10, 230, STEEL, INK, 0.8)
    b += rect(X + 10, Y, 70, 230, CONC, INK, 0.8) + dots(X + 12, Y + 4, 66, 222, 120, 21, "#8a9097", 1)
    # cutting edge bevel for caisson ring
    b += poly([(X + 10, Y + 230), (X + 80, Y + 230), (X + 80, Y + 250), (X + 30, Y + 250)], CONC, INK, 0.8)
    for yy in range(Y + 25, Y + 230, 45): b += rebar(X + 45, yy, 3.2)
    b += line(X + 45, Y + 10, X + 45, Y + 240, "#5d4037", 1.6)
    b += rect(X - 20, Y + 250, 130, 10, WOOD, WOODD, 0.8)
    b += dim(X + 10, Y - 6, X + 80, Y - 6, "75–100 mm")
    b += dim(X + 108, Y, X + 108, Y + 230, "", vertical=True) + t(X + 114, Y + 110, "ring height", 9.5) + t(X + 114, Y + 123, "0.5–0.6 m", 9.5) + t(X + 114, Y + 136, "(20–24 in)", 9.5)
    b += t(X + 175, Y + 30, "hoops: 6 mm bar or", 9.3) + t(X + 175, Y + 43, "doubled fence wire", 9.3) + t(X + 175, Y + 56, "every 150 mm", 9.3) + lead(X + 172, Y + 38, X + 48, Y + 70)
    b += t(X + 175, Y + 170, "verticals: 6–8 bars", 9.3) + t(X + 175, Y + 183, "joined to hoops", 9.3) + lead(X + 172, Y + 178, X + 47, Y + 180)
    b += t(X + 175, Y + 225, "bevelled cutting edge", 9.3) + t(X + 175, Y + 238, "(bottom ring only)", 9.3) + lead(X + 172, Y + 232, X + 60, Y + 244)
    b += t(X - 20, Y + 280, "Casting pad, oiled or lined with plastic.", 9) + t(X - 20, Y + 292, "1:2:3 mix, ≤ 12 mm gravel. Strip next day,", 9) + t(X - 20, Y + 304, "cure wet 7+ days. One 1.0 m ring ≈ 300 kg!", 9, weight="700")
    return svg(720, 385, b, "Well ring mold")

# ---------------------------------------------------------- 7 block mold
def block_mold():
    b = ""
    b += t(200, 20, "A. PLAN — hollow block mold (opens at pins)", 11, "middle", "700")
    X, Y, W, H = 40, 50, 320, 160
    b += rect(X - 18, Y - 18, W + 36, H + 36, WOOD, WOODD, 1.2)
    b += rect(X, Y, W, H, "#f0f0f0", INK, 1)
    b += dots(X + 2, Y + 2, W - 4, H - 4, 260, 31, "#9e9e9e", 1)
    for cxx in (X + 85, X + 235):
        b += rect(cxx - 45, Y + 30, 90, 100, WOOD, WOODD, 1.2) + t(cxx, Y + 84, "core", 9.5, "middle", "600")
        b += rect(cxx - 8, Y + 75, 16, 10, "#6d4c41", INK, 0.6)
    for (px, py) in [(X - 9, Y - 9), (X + W + 9, Y - 9), (X - 9, Y + H + 9), (X + W + 9, Y + H + 9)]:
        b += f'<circle cx="{px}" cy="{py}" r="5" fill="{STEEL}" stroke="{INK}"/>'
    b += dim(X, Y + H + 42, X + W, Y + H + 42, "15⅝ in (397 mm) inside")
    b += dim(X + W + 30, Y, X + W + 30, Y + H, "", vertical=True) + t(X + W + 36, Y + 75, "7⅝ in", 9.5) + t(X + W + 36, Y + 88, "(194 mm)", 9.5)
    b += t(X, Y + H + 64, "Cores tapered ~3 mm per side so they lift out;", 9.2) + t(X, Y + H + 78, "steel pins at corners release the sides.", 9.2)
    # section
    X2 = 470; Y2 = 60
    b += t(590, 20, "B. SECTION — tamping", 11, "middle", "700")
    b += rect(X2, Y2 + 130, 220, 12, WOOD, WOODD, 1)  # pallet
    b += rect(X2, Y2 + 20, 14, 110, WOOD, WOODD) + rect(X2 + 206, Y2 + 20, 14, 110, WOOD, WOODD)
    b += rect(X2 + 14, Y2 + 20, 192, 110, "#f0f0f0", INK, 0.8) + dots(X2 + 16, Y2 + 22, 188, 106, 200, 33, "#9e9e9e", 1)
    b += poly([(X2 + 50, Y2 + 20), (X2 + 90, Y2 + 20), (X2 + 87, Y2 + 130), (X2 + 53, Y2 + 130)], WOOD, WOODD)
    b += poly([(X2 + 130, Y2 + 20), (X2 + 170, Y2 + 20), (X2 + 167, Y2 + 130), (X2 + 133, Y2 + 130)], WOOD, WOODD)
    b += rect(X2 + 20, Y2 - 30, 26, 46, "#78909c", INK, 1) + line(X2 + 33, Y2 - 30, X2 + 33, Y2 - 55, INK, 3)
    b += arrow(X2 + 60, Y2 - 40, X2 + 60, Y2 - 5, RED, 1.6, "arr") + t(X2 + 68, Y2 - 10, "tamp in 3 layers", 9.3)
    b += t(X2, Y2 + 165, "Mix: 1 cement : 6–8 damp sand/fine", 9.3) + t(X2, Y2 + 178, "gravel (≤ 10 mm). 'Squeeze-ball' wet:", 9.3)
    b += t(X2, Y2 + 191, "holds shape, no water drips out.", 9.3) + t(X2, Y2 + 204, "Lift mold off at once; block stays on", 9.3) + t(X2, Y2 + 217, "pallet. Cure in shade, wet, 7–14 days.", 9.3)
    return svg(720, 300, b, "Concrete block mold")

# ---------------------------------------------------------- 8 rammed earth form
def rammed_earth_form():
    b = ""
    gl = 300
    b += poly([(0, gl), (720, gl), (720, 360), (0, 360)], GROUND, GSTROKE)
    # footing & stem
    b += rect(220, 300, 200, 50, CONC, INK, 1) + rect(260, 230, 120, 70, CONC, INK, 1)
    b += rect(260, 226, 120, 4, "#37474f", INK, 0.5)
    # existing compacted lifts
    lift_cols = ["#c9a77c", "#bf9c70", "#c9a77c", "#bf9c70"]
    y = 226
    for i, c in enumerate(lift_cols):
        b += rect(260, y - 30, 120, 30, c, "#8d6e45", 0.6) + dots(262, y - 28, 116, 26, 60, 40 + i, "#8d6e45", 0.8); y -= 30
    # loose lift
    b += rect(260, y - 40, 120, 40, "#e3cfa6", "#8d6e45", 0.6, extra='stroke-dasharray="4 3"') + dots(262, y - 38, 116, 36, 50, 50, "#a1887f", 1.4)
    top = y - 40
    # forms
    b += rect(242, top - 20, 18, 250 - (top - 20) + 0, WOOD, WOODD, 1) + rect(380, top - 20, 18, 250 - (top - 20), WOOD, WOODD, 1)
    # walers / studs
    for yy in (top + 10, top + 120):
        b += rect(226, yy - 10, 16, 20, "#a1887f", WOODD) + rect(398, yy - 10, 16, 20, "#a1887f", WOODD)
        b += line(200, yy, 440, yy, STEEL, 3) + rect(196, yy - 7, 8, 14, "#455a64", INK) + rect(436, yy - 7, 8, 14, "#455a64", INK)
    # tamper
    b += rect(296, top - 70, 48, 22, "#78909c", INK) + line(320, top - 70, 320, top - 140, WOODD, 6)
    b += arrow(360, top - 120, 360, top - 50, RED, 1.6, "arr")
    # labels
    b += t(470, top - 115, "Hand tamper: 15–20 lb (7–9 kg) steel or", 9.6) + t(470, top - 102, "hardwood head, ~6×6 in face. Ram until", 9.6) + t(470, top - 89, "it rings and the tamper bounces.", 9.6) + lead(468, top - 108, 345, top - 60)
    b += t(470, top + 14, "Loose lift 6–8 in (150–200 mm) →", 9.6, weight="700") + t(470, top + 27, "compacts to ~60% of loose height", 9.6) + lead(468, top + 18, 375, top + 20)
    b += t(470, top + 70, "Rammed lifts (each 4–5 in / 100–125 mm)", 9.6) + lead(468, top + 66, 375, top + 90)
    b += t(470, top + 116, "Through-ties (threaded rod or pipe", 9.6) + t(470, top + 129, "clamps) with walers both sides", 9.6) + lead(468, top + 120, 440, top + 120)
    b += t(470, 220, "Capillary break (tar paper, slate,", 9.6) + t(470, 233, "plastic) on top of stem wall", 9.6) + lead(468, 226, 380, 228)
    b += t(470, 270, "Concrete or stone stem wall ≥ 12 in", 9.6) + t(470, 283, "(300 mm) above finished grade", 9.6) + lead(468, 275, 380, 260)
    b += t(10, top + 10, "Form boards: 1½ in planks", 9.6) + t(10, top + 23, "or ¾ in plywood + studs —", 9.6) + t(10, top + 36, "stiff enough not to bulge", 9.6) + lead(150, top + 26, 244, top + 40)
    b += t(10, 245, "Wall: 12–24 in thick", 9.6) + t(10, 258, "(18 in typical exterior)", 9.6) + dim(260, 214 - 0, 380, 214, "", 0)
    b += t(10, 330, "Footing below frost line", 9.6)
    return svg(720, 442, shifted(b, 80), "Rammed earth formwork")

# ---------------------------------------------------------- 9 clay tests
def clay_tests():
    b = ""
    b += t(110, 20, "A. Ribbon test", 11, "middle", "700")
    b += f'<path d="M40,120 q30,-40 70,-30 q20,5 30,20" fill="#f1c9a5" stroke="{INK}"/>'
    b += f'<path d="M60,135 q40,30 80,-15" fill="#f1c9a5" stroke="{INK}"/>'
    b += f'<path d="M110,112 q30,10 40,60 q2,10 -8,12 q-10,-30 -32,-58z" fill="{CLAY}" stroke="{INK}" stroke-width="0.8"/>'
    b += t(20, 210, "Squeeze moist soil out between", 9.2) + t(20, 222, "thumb and finger into a ribbon:", 9.2)
    b += t(20, 238, "< 1 in (25 mm): sandy, low clay", 9.2) + t(20, 250, "1–2 in: clay loam — adobe, rammed", 9.2) + t(20, 262, "earth, cob", 9.2) + t(20, 274, "> 2 in (50 mm): clay — bricks", 9.2) + t(20, 286, "(temper with sand)", 9.2)
    b += t(360, 20, "B. Coil test", 11, "middle", "700")
    b += f'<path d="M300,120 a40,40 0 1,1 60,30" fill="none" stroke="{CLAY}" stroke-width="9" stroke-linecap="round"/>'
    b += f'<circle cx="330" cy="105" r="22" fill="#f1c9a5" stroke="{INK}"/>' + t(330, 109, "finger", 8.5, "middle")
    for (x1, y1) in [(298, 92), (305, 140)]: b += line(x1, y1, x1 + 8, y1 + 4, "#fff", 2)
    b += t(270, 210, "Roll a pencil-thick (6 mm) coil and", 9.2) + t(270, 222, "wrap it round a finger:", 9.2)
    b += t(270, 238, "no cracks = plastic clay, good for", 9.2) + t(270, 250, "throwing bricks; cracks = lean,", 9.2) + t(270, 262, "breaks = too sandy for fired brick", 9.2)
    b += t(600, 20, "C. Shrinkage bar", 11, "middle", "700")
    b += rect(490, 60, 220, 30, WOOD, WOODD, 1) + rect(496, 66, 208, 18, CLAY, INK, 0.6)
    b += rect(490, 120, 220, 30, WOOD, WOODD, 1) + rect(496, 126, 190, 18, "#d7a184", INK, 0.6) + rect(686, 126, 18, 18, "#fff", "none", 0)
    b += t(480, 55, "wet, day 0 (inside 600×40×40 mm,", 8.8) + t(480, 113, "dry, 7 days in shade", 8.8)
    b += dim(496, 162, 686, 162, "") + dim(686, 162, 704, 162, "") + t(695, 177, "gap", 8.8, "middle")
    b += t(490, 210, "Pack the box (oiled) with moist soil;", 9.2) + t(490, 222, "measure the gap when dry.", 9.2)
    b += t(490, 238, "Shrinkage % = gap ÷ 600 × 100", 9.2, weight="700") + t(490, 254, "Fired brick: aim 4–8%", 9.2) + t(490, 266, "Adobe / rammed earth: < 3–4%", 9.2) + t(490, 278, "Bar cracked or > 10%: add sand", 9.2) + t(490, 290, "or grog (crushed fired brick)", 9.2)
    return svg(720, 300, b, "Field tests for clay")

# ---------------------------------------------------------- 10 brick mold
def brick_mold():
    b = ""
    b += t(200, 20, "A. Four-brick gang mold (plan)", 11, "middle", "700")
    X, Y = 55, 50
    iw, ih = 75, 40  # scale 1 in = ~8.5 px
    b += rect(X, Y, 4 * iw + 5 * 10, ih + 20, WOOD, WOODD, 1.2)
    for i in range(4):
        b += rect(X + 10 + i * (iw + 10), Y + 10, iw, ih, "#fff", INK, 0.8)
    b += rect(X - 40, Y + 22, 40, 16, WOOD, WOODD) + rect(X + 4 * iw + 50, Y + 22, 40, 16, WOOD, WOODD)
    b += t(X - 38, Y + 55, "handle", 8.5) + t(X + 4 * iw + 52, Y + 55, "handle", 8.5)
    b += dim(X + 10, Y + ih + 38, X + 10 + iw, Y + ih + 38, "9 in (230 mm)")
    b += t(X + 120, Y + ih + 34, "each cell 9 × 4½ × 3 in inside", 9.3) + t(X + 120, Y + ih + 46, "→ fired brick ≈ 8¼ × 4 × 2¾ in", 9.3)
    b += t(X, Y + 130, "No bottom: mold sits on a sanded board or ground. Make it", 9.2) + t(X, Y + 142, "~8–10% larger than the brick you want (drying + firing shrinkage).", 9.2)
    b += t(X, Y + 154, "Adobe mold: 10 × 14 × 4 in (25 × 35 × 10 cm), 1 or 2 cells.", 9.2)
    # section steps
    X2 = 470
    b += t(590, 20, "B. Throwing a brick", 11, "middle", "700")
    steps = [("1 Wet + sand the mold", 0), ("2 Throw clot hard", 1), ("3 Strike off top", 2), ("4 Lift mold straight up", 3)]
    for i, (lab, k) in enumerate(steps):
        yy = 45 + i * 52
        b += rect(X2, yy + 24, 110, 6, "#d7ccc8", INK, 0.5)
        if k < 3:
            b += rect(X2 + 20, yy + 4, 8, 20, WOOD, WOODD) + rect(X2 + 82, yy + 4, 8, 20, WOOD, WOODD)
        if k == 1:
            b += f'<ellipse cx="{X2+55}" cy="{yy+12}" rx="20" ry="10" fill="{CLAY}" stroke="{INK}"/>' + arrow(X2 + 55, yy - 14, X2 + 55, yy + 2, RED, 1.4, "arr")
        if k >= 2:
            b += rect(X2 + 28, yy + 4, 54, 20, CLAY, INK, 0.6)
        if k == 2:
            b += line(X2 + 10, yy + 2, X2 + 105, yy + 2, WOODD, 4) + arrow(X2 + 70, yy - 6, X2 + 100, yy - 6, INK)
        if k == 3:
            b += rect(X2 + 20, yy - 22, 8, 20, WOOD, WOODD) + rect(X2 + 82, yy - 22, 8, 20, WOOD, WOODD) + arrow(X2 + 55, yy - 4, X2 + 55, yy - 26, INK)
        b += t(X2 + 120, yy + 18, lab, 9.6)
    return svg(720, 255, b, "Brick mold")

# ---------------------------------------------------------- 11 kilns: clamp + updraft
def brick_kilns():
    b = ""
    b += t(170, 20, "A. Scove kiln / clamp (section)", 11, "middle", "700")
    gl = 280
    b += rect(0, gl, 720, 25, GROUND, GSTROKE)
    # clamp body
    b += poly([(20, gl), (40, 70), (300, 70), (320, gl)], "#e7b08f", INK, 1)
    # bricks texture
    for row, yy in enumerate(range(80, gl - 50, 14)):
        off = 0 if row % 2 == 0 else 9
        for xx in range(48 + off, 296, 18):
            b += rect(xx, yy, 6, 11, BRICK if row % 2 else "#d08a6a", "none", 0)
    # fire tunnels
    for xx in (80, 170, 260):
        b += f'<path d="M{xx-22},{gl} v-26 q22,-22 44,0 v26z" fill="#3e2723" stroke="{INK}"/>'
        b += f'<path d="M{xx-14},{gl} q6,-22 14,-8 q6,-16 14,8z" fill="{AMBER}"/>'
    # scove plaster
    b += f'<path d="M20,{gl} L40,70 L300,70 L320,{gl}" fill="none" stroke="#6d4c41" stroke-width="7" opacity="0.6"/>'
    b += t(40, 62, "top: 1–2 courses of fired brick + earth to damp the fire", 8.6)
    b += lead(330, 160, 314, 170) + t(334, 152, "scove: 2–4 in mud plaster", 8.8) + t(334, 164, "(re-daub cracks)", 8.8)
    b += lead(330, 205, 300, 220) + t(334, 210, "green bricks set on edge,", 8.8) + t(334, 222, "finger-width gaps for draft", 8.8)
    b += t(30, 322, "Fire tunnels (arches of green brick) every 3–4 ft, fed from both ends.", 9) + t(30, 334, "Fine fuel (sawdust, coal dust) can be mixed into the clay or spread between layers.", 9)
    # updraft kiln
    X = 470
    b += t(590, 20, "B. Updraft kiln (permanent)", 11, "middle", "700")
    b += rect(X, 60, 24, gl - 60, "#9e5a43", INK) + rect(X + 216, 60, 24, gl - 60, "#9e5a43", INK)
    for yy in range(64, gl, 12):
        b += line(X, yy, X + 24, yy, "#5d2f20", 0.5) + line(X + 216, yy, X + 240, yy, "#5d2f20", 0.5)
    b += rect(X + 24, 60, 192, gl - 60, "#fbe9e7", "none", 0)
    # firebox below perforated floor
    b += rect(X + 24, 220, 192, 60, "#4e342e", "none")
    b += f'<path d="M{X+50},{gl} q20,-45 40,-10 q20,-40 40,5 q20,-35 40,5 q15,-20 25,0z" fill="{AMBER}"/>'
    for xx in range(X + 24, X + 216, 32):
        b += rect(xx, 208, 22, 12, "#9e5a43", INK, 0.6)
    # setting of bricks
    for row, yy in enumerate(range(100, 206, 13)):
        off = 0 if row % 2 == 0 else 8
        for xx in range(X + 30 + off, X + 208, 16):
            b += rect(xx, yy, 6, 11, "#d08a6a", "none", 0)
    b += rect(X - 6, 86, 252, 10, "#6d4c41", INK) 
    b += t(X + 120, 50, "loose cover of old brick / iron sheet;", 8.6, "middle") + t(X + 120, 63, "gaps adjusted to control draft", 8.6, "middle")
    for xx in (X + 80, X + 160): b += arrow(xx, 200, xx, 100, RED, 1.2, "arr", "4 3")
    b += t(X + 120, 300, "fireboxes / arches with ash pit", 8.8, "middle") 
    b += t(X - 2, 322, "Walls 1–2 bricks thick, clay mortar; 4–6 ft high.", 9) + t(X - 2, 334, "Spy-holes (plugged) let you see the color.", 9)
    b += t(X + 120, 238, "firebox", 9, "middle", "700", "#fff")
    return svg(720, 345, b, "Clamp and updraft brick kilns")

def firing_curve():
    b = ""
    gx, gy, gw, gh = 60, 30, 560, 190
    b += rect(gx, gy, gw, gh, "#f7f9fa", "#9aa7b0", 0.8)
    X = lambda d: gx + d / 7 * gw; Y = lambda c: gy + gh - c / 1200 * gh
    for c in range(0, 1201, 200): b += line(gx, Y(c), gx + gw, Y(c), "#dde3e7", 0.6) + t(gx - 6, Y(c) + 3, f"{c}", 8.5, "end")
    for d in range(0, 8): b += t(X(d), gy + gh + 14, f"day {d}", 8.5, "middle")
    zones = [(0, 120, "#e3f2fd", "1 Water-smoking ≤120 °C: steam leaves — go SLOW"), (120, 600, "#fff8e1", "2 Clay water driven off; quartz change at 573 °C — slow"),
             (600, 900, "#ffe0b2", "3 Carbon & sulfur burn off — keep air flowing"), (900, 1100, "#ffccbc", "4 Vitrification 900–1,100 °C: bricks fuse (hold 'soak')")]
    for c0, c1, col, lab in zones:
        b += rect(gx + 1, Y(c1), gw - 2, Y(c0) - Y(c1), col, "none", 0) + t((X(3.3) if c0 == 0 else gx + 8), Y(c1) + 13, lab, 9)
    pts = [(0, 20), (1.5, 110), (2.2, 150), (3.2, 600), (3.8, 900), (4.4, 1000), (5.0, 1000), (5.3, 700), (7, 120)]
    b += '<polyline points="' + " ".join(f"{X(d):.1f},{Y(c):.1f}" for d, c in pts) + f'" fill="none" stroke="{RED}" stroke-width="2.4"/>'
    b += t(X(5.4), Y(820), "seal & cool slowly", 9, weight="700", fill=RED) + t(X(5.4), Y(740), "(do not open hot)", 9, fill=RED)
    b += t(gx + gw + 6, Y(1000) + 3, "bright orange", 8.5) + t(gx + gw + 6, Y(800) + 3, "cherry red", 8.5) + t(gx + gw + 6, Y(600) + 3, "dull red glow", 8.5) + t(gx + gw + 6, Y(150) + 3, "no glow", 8.5)
    b += t(10, gy + gh + 34, "Typical small clamp or updraft kiln. Large clamps take 1–2 weeks to fire and 1–2 weeks to cool. Glow colors seen in a dark spy-hole.", 8.8, italic=True)
    return svg(720, gy + gh + 42, b, "Brick firing curve")

# ---------------------------------------------------------- 12 bonds
def brick_bonds():
    b = ""
    L, Hh, j = 36, 11, 3
    def course(x, y, pattern, width=230):
        s = ""; xx = x
        for k in pattern:
            w = L if k == "S" else (L - j) / 2
            if xx + w > x + width: w = x + width - xx
            if w > 2: s += rect(xx, y, w, Hh, BRICK if k == "S" else "#8e3b2a", "#f3e5dc", 0.6)
            xx += w + j
            if xx >= x + width: break
        return s
    def wall(x, y, rows, title):
        s = t(x + 115, y - 10, title, 10.5, "middle", "700")
        s += rect(x - 2, y - 2, 234, len(rows) * (Hh + j) + 2, "#f3e5dc", "none", 0)
        for i, pat in enumerate(rows): s += course(x, y + i * (Hh + j), pat)
        return s
    S = "S" * 10; H = "H" * 16
    run = [S, "h" + S] * 4
    run = [["S"] * 10, ["h"] + ["S"] * 10] * 4
    common = [["H"] * 16] + [["S"] * 10, ["h"] + ["S"] * 10] * 3 + [["H"] * 16]
    flem = [["S", "H"] * 8, ["H", "S"] * 8] * 4
    eng = [["S"] * 10, ["h"] + ["H"] * 16] * 4
    def norm(rows):
        out = []
        for r in rows: out.append(["H" if k == "h" else k for k in r])
        return out
    b += wall(20, 40, norm(run), "Running bond (½ overlap)")
    b += wall(260, 40, norm(common), "Common / American bond")
    b += wall(500, 40, norm(flem), "Flemish bond")
    b += wall(20, 200, norm(eng), "English bond")
    b += t(260, 205, "Stretcher (S) = long face showing", 9.5) + rect(470, 196, L, Hh, BRICK, "#fff", 0.5)
    b += t(260, 222, "Header (H) = end showing; ties the two", 9.5) + rect(470, 213, (L - j) / 2, Hh, "#8e3b2a", "#fff", 0.5)
    b += t(260, 236, "wythes (layers) of a thick wall together", 9.5)
    b += t(260, 256, "Rules: never line up vertical joints in two", 9.5) + t(260, 270, "courses; header course every 5–7 courses in", 9.5)
    b += t(260, 284, "double-wythe walls (or metal ties every 16 in", 9.5) + t(260, 298, "vertically, 24–32 in horizontally).", 9.5)
    return svg(740, 320, b, "Brick bonds")

# ---------------------------------------------------------- 13 floor plan
def floor_plan():
    b = ""
    s = 20  # px per ft
    X, Y = 60, 50; W, H = 24 * s, 20 * s
    th = 0.67 * s  # 8 in wall
    b += rect(X - th, Y - th, W + 2 * th, H + 2 * th, "#b0bec5", INK, 1.2)
    b += rect(X, Y, W, H, "#fffdf7", INK, 1)
    # interior wall at 14 ft
    iw = 0.33 * s
    b += rect(X + 14 * s, Y, iw, 12 * s, "#cfd8dc", INK, 0.8)
    b += rect(X + 14 * s, Y + 15 * s, iw, 5 * s, "#cfd8dc", INK, 0.8)
    # door openings (exterior) on south (bottom) wall
    def gap(x0, y0, w, h): return rect(x0, y0, w, h, "#fffdf7", "none", 0)
    b += gap(X + 5 * s, Y + H - 1, 3 * s, th + 2)
    b += f'<path d="M{X+5*s},{Y+H} A{3*s},{3*s} 0 0 0 {X+8*s},{Y+H-3*s}" fill="none" stroke="{INK}" stroke-width="0.8" stroke-dasharray="3 2"/>' + line(X + 8 * s, Y + H, X + 8 * s, Y + H - 3 * s, INK, 1.2)
    # windows
    wins = [("S", 15, 4), ("S", 1.5, 3) , ("N", 4, 3), ("N", 17, 3), ("E", 7, 3), ("W", 8, 3)]
    for side, pos, wd in wins:
        if side in "NS":
            yy = Y - th if side == "N" else Y + H
            b += rect(X + pos * s, yy, wd * s, th, "#e3f2fd", INK, 0.8) + line(X + pos * s, yy + th / 2, X + (pos + wd) * s, yy + th / 2, BLUE, 1)
        else:
            xx = X + W if side == "E" else X - th
            b += rect(xx, Y + pos * s, th, wd * s, "#e3f2fd", INK, 0.8) + line(xx + th / 2, Y + pos * s, xx + th / 2, Y + (pos + wd) * s, BLUE, 1)
    # vertical reinforcement at corners and jambs
    corners = [(X - th / 2, Y - th / 2), (X + W + th / 2, Y - th / 2), (X - th / 2, Y + H + th / 2), (X + W + th / 2, Y + H + th / 2)]
    for cx_, cy_ in corners: b += f'<circle cx="{cx_}" cy="{cy_}" r="4" fill="{RED}"/>'
    for side, pos, wd in wins + [("S", 5, 3)]:
        for p in (pos, pos + wd):
            if side in "NS":
                yy = Y - th / 2 if side == "N" else Y + H + th / 2
                b += f'<circle cx="{X + p*s + (-5 if p==pos else 5)}" cy="{yy}" r="3" fill="{RED}"/>'
            else:
                xx = X + W + th / 2 if side == "E" else X - th / 2
                b += f'<circle cx="{xx}" cy="{Y + p*s + (-5 if p==pos else 5)}" r="3" fill="{RED}"/>'
    # stove and hearth
    b += rect(X + 12 * s, Y + 12.5 * s, 2 * s, 2 * s, "#d7ccc8", INK, 0.8) + rect(X + 12.4 * s, Y + 12.9 * s, 1.2 * s, 1.2 * s, "#455a64", INK, 0.8)
    b += t(X + 13.6 * s, Y + 15.2 * s, "masonry hearth", 9.5, "end") + t(X + 13.6 * s, Y + 15.9 * s, "+ wood stove", 9.5, "end")
    # labels rooms
    b += t(X + 7 * s, Y + 6 * s, "MAIN ROOM", 12, "middle", "700") + t(X + 7 * s, Y + 6.8 * s, "kitchen · living", 9.5, "middle") + t(X + 7 * s, Y + 7.6 * s, "≈ 14 × 20 ft inside", 9.5, "middle")
    b += t(X + 19 * s, Y + 5 * s, "BEDROOM", 12, "middle", "700") + t(X + 19 * s, Y + 5.8 * s, "≈ 9½ × 12 ft", 9.5, "middle")
    b += t(X + 19 * s, Y + 16.5 * s, "STORAGE /", 10, "middle", "700") + t(X + 19 * s, Y + 17.3 * s, "pantry", 9.5, "middle")
    b += rect(X + 16 * s, Y + 13 * s, 3 * s, 2 * s, "none", INK, 0.8, extra='stroke-dasharray="4 3"') + t(X + 17.5 * s, Y + 14.2 * s, "cellar hatch", 9.5, "middle")
    # cistern & porch
    b += f'<circle cx="{X + W + 3.5*s}" cy="{Y + 2.5*s}" r="{2*s}" fill="{LBLUE}" stroke="{INK}"/>' + t(X + W + 3.5 * s, Y + 2.5 * s + 4, "cistern", 9, "middle")
    b += rect(X + 2 * s, Y + H + th, 9 * s, 4 * s, "none", INK, 0.8, extra='stroke-dasharray="5 3"') + t(X + 6.5 * s, Y + H + th + 2.5 * s, "covered porch / slab", 9, "middle")
    # dims
    b += dim(X - th, Y - th - 18, X + W + th, Y - th - 18, "24 ft (7.3 m) outside")
    b += dim(X - th - 22, Y - th, X - th - 22, Y + H + th, "", vertical=True) + f'<text x="18" y="{Y + H / 2}" font-size="9.5" text-anchor="middle" transform="rotate(-90 18 {Y + H / 2})" fill="{INK}">20 ft (6.1 m) outside</text>'
    b += t(X + W + 40, Y + 6 * s, "N ↑", 12, weight="700")
    # legend notes
    Lx = X + W + 40
    notes = [("Walls: 8 in grouted block,", 0), ("12 in brick/stone, or", 0), ("18 in rammed earth", 0), ("", 0),
             ("● vertical rebar at corners,", 1), ("both sides of openings,", 1), ("and ≤ 4 ft apart", 1), ("", 0),
             ("Openings ≥ 2 ft from corners;", 0), ("total ≤ ⅓ of wall length", 0), ("", 0),
             ("Larger windows on the south", 0), ("for winter sun; small on", 0), ("north and west", 0)]
    for i, (n, red) in enumerate(notes): b += t(Lx, Y + 7 * s + i * 14, n, 9.4, fill=RED if red else INK)
    return svg(760, Y + H + th + 5 * s + 10, b, "Small masonry house floor plan")

# ---------------------------------------------------------- 14 wall section
def wall_section():
    b = ""
    gl = 330
    b += poly([(0, gl), (200, gl - 6), (200, 470), (0, 470)], GROUND, GSTROKE)
    b += f'<rect x="0" y="{gl}" width="200" height="140" fill="url(#hatch)" opacity="0.5"/>'
    b += poly([(320, gl - 14), (720, gl - 14), (720, 470), (320, 470)], GROUND, GSTROKE)
    # footing
    b += rect(190, 420, 180, 40, CONC, INK, 1.2) + rebar(220, 445) + rebar(280, 445) + rebar(340, 445)
    # stem wall / block wall
    WX, WW = 245, 70
    b += rect(WX, 120, WW, 300, "#cfd8dc", INK, 1.2)
    for yy in range(128, 420, 20): b += line(WX, yy, WX + WW, yy, "#90a4ae", 0.6)
    b += line(WX + WW / 2, 130, WX + WW / 2, 445, "#5d4037", 2.5)
    # bond beam
    b += rect(WX, 100, WW, 28, CONC, INK, 1.2) + rebar(WX + 22, 114) + rebar(WX + 48, 114)
    # anchor bolt & plate
    b += line(WX + 35, 120, WX + 35, 80, STEEL, 3) + rect(WX + 6, 80, WW - 12, 16, WOOD, WOODD)
    # rafter & roof
    b += poly([(120, 108), (560, -10 + 0), (560, 6), (120, 124)], WOOD, WOODD)
    b += poly([(110, 100), (560, -24), (560, -14), (110, 110)], "#607d8b", INK)
    b += f'<path d="M{WX+10},96 l0,-14 l40,-10 l0,14" fill="none" stroke="{STEEL}" stroke-width="2"/>'
    # exterior insulation + plaster
    b += rect(WX - 26, 132, 22, 270, "#ffe082", INK, 0.6) + f'<rect x="{WX-26}" y="132" width="22" height="270" fill="url(#ins)"/>'
    b += rect(WX - 31, 132, 5, 290, "#eeeeee", INK, 0.5)
    b += rect(WX - 4, 132, 4, 290, "#455a64", "none")
    # interior plaster
    b += rect(WX + WW, 130, 4, 186, "#fafafa", INK, 0.4)
    # slab
    b += rect(WX + WW, 300, 400, 18, CONC, INK, 1) + rect(WX + WW, 318, 400, 4, "#263238", "none") + rect(WX + WW, 322, 400, 16, "#ffe082", INK, 0.5)
    b += rect(WX + WW, 338, 400, 24, "#d7ccc8", INK, 0.5) + pebbles(WX + WW + 2, 340, 396, 20, 60, 14, GRAV, 3)
    # perimeter drain
    b += rect(150, 380, 95, 40, "#d7ccc8", INK, 0.5) + pebbles(152, 382, 90, 36, 30, 17, GRAV, 3) + f'<circle cx="195" cy="408" r="9" fill="#fff" stroke="{INK}"/>'
    # grade slope arrow
    b += arrow(200, gl - 14, 30, gl - 2, BLUE, 1.6, "arb")
    # labels
    R = 545; Lx = 10
    labs_r = [(40, "Metal roofing; overhang ≥ 18–24 in", "(more for earth walls)"), (98, "Rafter strapped to plate (hurricane", "ties) — see House Building vol."),
              (140, "Plate on ½ in anchor bolts every", "4–6 ft, ≤ 12 in from corners"), (180, "Concrete bond beam: 2 #4 bars,", "continuous around the house"),
              (230, "Vertical #4 bar in grouted cells:", "corners, jambs, ≤ 4 ft apart"), (285, "Slab 4 in on vapor barrier, rigid", "insulation, 4–6 in gravel")]
    for y, l1, l2 in labs_r: b += t(R - 0, y + 0, l1, 10) + t(R, y + 14, l2, 10)
    b += lead(R - 3, 44, 460, 22) + lead(R - 3, 102, 470, 40) + lead(R - 3, 144, WX + WW - 10, 88) + lead(R - 3, 184, WX + WW - 6, 112) + lead(R - 3, 234, WX + WW / 2 + 2, 230) + lead(R - 3, 289, 500, 309)
    labs_l = [(150, "Exterior: lime or cement", "plaster over mesh"), (200, "Rigid insulation outside the", "masonry (cold climates)"),
              (255, "Damp-proof coating below", "grade (bitumen / lime)"), (300, "Ground slopes away 6 in in", "first 10 ft (5%)"),
              (370, "Gravel + perforated drain", "pipe to daylight"), (452, "Footing below frost line", "(see table)")]
    for y, l1, l2 in labs_l: b += t(Lx, y, l1, 9.6) + t(Lx, y + 13.5, l2, 9.6)
    b += lead(150, 154, WX - 31, 165) + lead(150, 204, WX - 20, 215) + lead(150, 259, WX - 3, 360) + lead(140, 306, 110, 322) + lead(150, 374, 180, 395) + lead(150, 456, 192, 440)
    b += t(WX + WW + 20, 290, "finished floor ≥ 8 in above outside grade", 8.8, fill=BLUE)
    return svg(760, 515, shifted(b, 40), "Masonry wall cross-section")
