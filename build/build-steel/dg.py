"""Code-drawn SVG diagrams for the Steel guide (no AI images)."""
import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import svg, t, line, arrow, rect, label_box, INK

def cover_art():
    s = '<rect width="720" height="380" fill="#1b2730"/>'
    # anvil
    s += '<path d="M250 230 h240 q-10 22 -60 28 v40 h40 v22 h-200 v-22 h40 v-40 q-60 -6 -90 -28z" fill="#546e7a" stroke="#263238" stroke-width="3"/>'
    s += '<path d="M490 230 q60 0 90 -14 q-30 30 -90 34z" fill="#546e7a" stroke="#263238" stroke-width="3"/>'
    # glowing bar on anvil
    s += '<rect x="300" y="218" width="190" height="12" rx="3" fill="#ff9800"/><rect x="420" y="218" width="70" height="12" rx="3" fill="#ffeb3b"/>'
    # hammer
    s += '<rect x="372" y="120" width="70" height="34" rx="4" fill="#90a4ae" stroke="#263238" stroke-width="3" transform="rotate(-18 407 137)"/>'
    s += '<rect x="420" y="70" width="14" height="110" rx="5" fill="#8d6e63" transform="rotate(52 427 125)"/>'
    for i in range(9): s += f'<circle cx="{470+i*14}" cy="{200-(i%3)*14}" r="2.5" fill="#ffd54f"/>'
    # furnace (bloomery) at left
    s += '<path d="M70 320 L90 130 h70 L180 320z" fill="#a1887f" stroke="#4e342e" stroke-width="3"/>'
    s += '<path d="M110 130 q15 -40 5 -70 q25 30 15 70z" fill="#ff7043"/><path d="M118 130 q8 -22 3 -40 q14 20 7 40z" fill="#ffca28"/>'
    s += '<rect x="168" y="270" width="50" height="10" fill="#6d4c41" transform="rotate(-20 168 270)"/>'
    # tempering color strip
    cols = ["#f5e6a8", "#e8c66a", "#c8913c", "#8e5a2b", "#6b3a7a", "#2b3f8f", "#5d8fd0", "#7f97a8"]
    for i, ccol in enumerate(cols): s += f'<rect x="{560+i*18}" y="300" width="18" height="40" fill="{ccol}"/>'
    s += f'<text x="632" y="360" font-size="13" fill="#cfd8dc" text-anchor="middle" font-family="IBM Plex Sans">tempering colors</text>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

def d_carbon():
    s = t(360, 28, "Carbon content decides what iron becomes", 18, "middle", "700")
    x0, x1 = 60, 680
    def X(p): return x0 + (x1 - x0) * p / 4.5
    zones = [(0, 0.08, "#b0bec5", "wrought iron", "soft, welds easily"), (0.08, 0.3, "#90caf9", "mild (low-carbon) steel", "nails, wire, rebar"),
             (0.3, 0.6, "#64b5f6", "medium", "axes, hammers"), (0.6, 1.5, "#1e88e5", "high-carbon", "springs, files, blades"),
             (2.0, 4.5, "#6d4c41", "cast iron", "pours, brittle, won't forge")]
    for a, b, col, nm, use in zones:
        s += rect(X(a), 70, X(b) - X(a), 60, col, INK, 1.5, 0)
    s += rect(X(1.5), 70, X(2.0) - X(1.5), 60, "#eceff1", "#90a4ae", 1, 0) + t(X(1.75), 105, "rare", 12, "middle")
    labels = [(0.04, "wrought", "iron", 170), (0.19, "mild", "steel", 210), (0.45, "medium", "carbon", 250), (1.05, "high-carbon", "(tool) steel", 210), (3.2, "cast iron", "(pig iron)", 170)]
    for p, a, b, y in labels:
        s += line(X(p), 130, X(p), y - 22, "#607d8b", 1.5) + t(X(p), y, a, 14, "middle", "700") + t(X(p), y + 18, b, 13, "middle")
    for v in [0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0]:
        s += line(X(v), 130, X(v), 138) + t(X(v), 56, f"{v:g}%", 13, "middle")
    s += t(360, 300, "More carbon = harder and able to quench-harden, but less ductile.", 15, "middle", "600")
    s += t(360, 322, "Above about 2% carbon the metal melts at a lower temperature and cannot be forged.", 14, "middle")
    return svg(720, 335, s)

def d_tiers():
    rows = [("#2e7d32", "TIER A · hand-built", ["bog ore → roast → clay bloomery → bloom → wrought iron", "pack carburizing / case hardening · forging · heat treatment"]),
            ("#1565c0", "TIER B · workshop", ["cementation (blister/shear steel) · crucible steel · cupola casting", "hand-crank blower · power hammer · wire drawing · rolls"]),
            ("#6a1b9a", "TIER C · industrial", ["blast furnace → Bessemer / open hearth → basic oxygen", "electric arc furnace · rolling mills · alloy steels"])]
    s = t(360, 28, "Three tech levels of iron and steel", 18, "middle", "700")
    for i, (col, h, ls) in enumerate(rows):
        y = 50 + i * 110
        s += rect(30, y, 660, 92, "#fff", col, 4, 8) + rect(30, y, 660, 28, col, col, 0, 6)
        s += t(46, y + 20, h, 15, "start", "700", "#fff")
        for j, l in enumerate(ls): s += t(46, y + 52 + j * 22, l, 14)
        if i < 2: s += arrow(360, y + 92, 360, y + 108, col, 3)
    return svg(720, 385, s)

def d_mound():
    s = t(360, 26, "Earth-mound charcoal kiln (cross-section)", 18, "middle", "700")
    s += '<path d="M90 330 Q360 40 630 330 Z" fill="#8d6e63" stroke="#4e342e" stroke-width="3"/>'
    s += '<path d="M120 326 Q360 70 600 326 Z" fill="#a1887f"/>'
    s += '<path d="M135 324 Q360 95 585 324 Z" fill="#d7b98e" stroke="#8a6d3b" stroke-width="2"/>'
    for i in range(7):
        x = 190 + i * 55
        s += line(x, 320, 360 + (x - 360) * 0.25, 150, "#8a6d3b", 4)
    s += rect(345, 120, 30, 205, "#ffcc80", "#e65100", 2, 2) + t(360, 108, "central flue / ignition", 13, "middle", "600")
    for x in (180, 300, 420, 540): s += rect(x, 318, 14, 12, "#263238", "#263238", 0, 1)
    s += line(40, 330, 680, 330, INK, 3)
    s += t(650, 160, "earth 20 cm", 13, "end", "600") + arrow(570, 165, 520, 185)
    s += t(70, 160, "leaves / grass", 13, "start", "600") + arrow(140, 166, 205, 205)
    s += t(360, 352, "air vents at the base: open to burn, close progressively; seal everything to finish", 13, "middle")
    s += t(360, 372, "Steam is white and thick at first; thin bluish smoke means carbonization is nearly done.", 13, "middle")
    return svg(720, 385, s)

def d_furnace():
    s = t(360, 26, "Short-shaft clay bloomery (cross-section)", 18, "middle", "700")
    # walls
    s += '<path d="M250 70 L230 370 L285 370 L300 70 Z" fill="#bcaaa4" stroke="#4e342e" stroke-width="3"/>'
    s += '<path d="M420 70 L440 370 L385 370 L370 70 Z" fill="#bcaaa4" stroke="#4e342e" stroke-width="3"/>'
    s += '<rect x="300" y="70" width="70" height="300" fill="#fff8e1"/>'
    # charcoal column
    for r in range(13):
        for k in range(3):
            s += f'<circle cx="{312 + k*23 + (r%2)*8}" cy="{88 + r*17}" r="7" fill="#37474f"/>'
    # combustion zone
    s += '<ellipse cx="335" cy="290" rx="34" ry="26" fill="#ff7043" opacity="0.8"/>'
    # slag & bloom
    s += '<path d="M287 370 Q335 320 383 370 Z" fill="#5d4037"/>' + '<ellipse cx="335" cy="352" rx="30" ry="12" fill="#90a4ae" stroke="#263238" stroke-width="2"/>'
    # tuyere
    s += '<polygon points="440,262 500,240 504,252 444,276" fill="#b0bec5" stroke="#263238" stroke-width="2"/>'
    s += '<polygon points="383,282 440,262 444,276 386,296" fill="#b0bec5" stroke="#263238" stroke-width="2"/>'
    s += arrow(560, 232, 506, 248, "#1565c0", 3) + t(565, 228, "air from bellows", 14, "start", "600")
    s += t(565, 290, "tuyere 20–25° down,", 13, "start") + t(565, 307, "tip ~5 cm inside wall", 13, "start")
    # tap arch
    s += rect(232, 345, 30, 25, "#4e342e", "#4e342e", 0, 2) + t(200, 360, "slag tap", 13, "end", "600")
    # dims
    s += line(300, 60, 370, 60, "#c62828", 2) + t(335, 52, "25–30 cm inside", 13, "middle", "600", "#c62828")
    s += line(470, 70, 470, 270, "#c62828", 2) + t(478, 160, "≥ 40 cm above tuyere", 13, "start", "600", "#c62828")
    s += line(470, 270, 470, 370, "#c62828", 2, "5 4") + t(478, 335, "15–20 cm below", 13, "start", "600", "#c62828")
    s += t(120, 110, "charcoal +", 14, "middle", "600") + t(120, 128, "ore charges", 14, "middle", "600") + arrow(150, 120, 300, 90)
    s += t(120, 230, "walls: clay + sand", 13, "middle") + t(120, 248, "or clay + straw", 13, "middle") + t(120, 266, "5–10 cm thick", 13, "middle") + arrow(170, 250, 245, 250)
    s += t(150, 320, "slag bowl", 13, "middle") + t(150, 336, "and bloom", 13, "middle") + arrow(185, 330, 300, 350)
    s += line(200, 370, 520, 370, INK, 3)
    return svg(720, 390, s)

def d_bellows():
    s = t(360, 26, "Bellows you can build", 18, "middle", "700")
    # left: pair of bag/pot bellows
    s += t(180, 60, "Twin hand or foot bellows", 15, "middle", "700")
    for cx in (120, 230):
        s += f'<ellipse cx="{cx}" cy="150" rx="48" ry="50" fill="#d7b98e" stroke="#6d4c41" stroke-width="3"/>'
        s += rect(cx - 45, 92, 90, 12, "#8d6e63", "#4e342e", 2, 3) + rect(cx - 45, 196, 90, 12, "#8d6e63", "#4e342e", 2, 3)
        s += f'<circle cx="{cx}" cy="98" r="5" fill="#fff" stroke="#4e342e"/>'
        s += line(cx, 208, 175, 250, "#455a64", 6)
    s += line(175, 250, 175, 300, "#455a64", 8) + t(175, 320, "both feed one tuyere", 13, "middle")
    s += t(180, 345, "Work them alternately: one fills while", 13, "middle") + t(180, 362, "the other blows, giving a steady blast.", 13, "middle")
    s += t(60, 90, "flap", 12, "end") + t(60, 104, "valve", 12, "end") + arrow(62, 98, 112, 98)
    # right: box (double-acting) bellows
    s += t(530, 60, "Box bellows (double-acting)", 15, "middle", "700")
    s += rect(400, 110, 260, 110, "#efebe9", "#4e342e", 3, 4)
    s += rect(520, 115, 16, 100, "#8d6e63", "#4e342e", 2, 2) + line(536, 165, 690, 165, "#5d4037", 6) + t(700, 182, "handle", 12, "end")
    s += line(400, 228, 660, 228, "#4e342e", 2) + rect(400, 222, 260, 26, "#d7ccc8", "#4e342e", 2, 2) + t(530, 240, "air channel to outlet", 12, "middle")
    for x in (410, 640): s += rect(x, 120, 10, 30, "#90a4ae", "#455a64", 1, 1)
    s += t(530, 270, "A piston (packed with leather or feathers)", 13, "middle") + t(530, 287, "pushes air on BOTH strokes; flap valves", 13, "middle")
    s += t(530, 304, "at each end let air in behind it.", 13, "middle")
    s += arrow(660, 235, 700, 235, "#1565c0", 3)
    s += t(530, 345, "Target for a 30 cm bloomery: roughly", 13, "middle", "600") + t(530, 362, "800–1,100 L/min of steady air (see 4.2)", 13, "middle", "600")
    return svg(720, 380, s)

def d_forge():
    s = t(360, 26, "Two simple forges", 18, "middle", "700")
    # side blast
    s += t(180, 58, "Side-blast (charcoal)", 15, "middle", "700")
    s += rect(50, 200, 260, 120, "#bcaaa4", "#4e342e", 3, 4)
    s += '<path d="M90 200 Q180 140 270 200 Z" fill="#37474f"/>' + '<ellipse cx="180" cy="190" rx="40" ry="16" fill="#ff7043"/>'
    s += rect(270, 182, 70, 16, "#90a4ae", "#263238", 2, 2) + arrow(380, 190, 342, 190, "#1565c0", 3) + t(380, 182, "air", 13, "start")
    s += t(180, 345, "Brick, stone or clay hearth; tuyere enters", 13, "middle") + t(180, 362, "from the side about 10 cm above the floor", 13, "middle")
    s += rect(60, 100, 50, 100, "#cfd8dc", "#607d8b", 2, 2) + t(85, 92, "water", 12, "middle") + t(85, 150, "tank", 12, "middle")
    # bottom blast
    s += t(540, 58, "Bottom-blast (coal or charcoal)", 15, "middle", "700")
    s += rect(410, 160, 260, 40, "#78909c", "#263238", 3, 2)
    s += '<path d="M500 160 L515 210 L565 210 L580 160 Z" fill="#455a64" stroke="#263238" stroke-width="2"/>'
    s += '<ellipse cx="540" cy="150" rx="55" ry="18" fill="#37474f"/><ellipse cx="540" cy="146" rx="30" ry="10" fill="#ff7043"/>'
    s += rect(528, 210, 24, 70, "#90a4ae", "#263238", 2, 1) + t(560, 300, "air pipe with ash dump", 13, "start")
    s += line(552, 245, 640, 245, "#90a4ae", 14) + arrow(680, 245, 642, 245, "#1565c0", 3) + t(684, 238, "air", 13, "start")
    s += t(540, 120, "firepot (iron box, brake drum)", 13, "middle")
    s += rect(420, 200, 14, 120, "#607d8b") + rect(646, 200, 14, 120, "#607d8b")
    s += t(540, 345, "Keep the fire deep: work in the hot zone", 13, "middle") + t(540, 362, "above the oxygen-rich spot near the tuyere", 13, "middle")
    return svg(720, 380, s)

def d_anvil():
    s = t(360, 26, "Anvil parts — and substitutes", 18, "middle", "700")
    s += '<path d="M150 120 h300 v40 q-40 10 -60 30 v60 h50 v30 h-230 v-30 h50 v-60 q-20 -20 -110 -30z" fill="#78909c" stroke="#263238" stroke-width="3"/>'
    s += '<path d="M150 120 q-70 6 -110 26 q50 6 110 10z" fill="#78909c" stroke="#263238" stroke-width="3"/>'
    s += rect(400, 124, 12, 12, "#263238", "#263238", 0, 0) + '<circle cx="380" cy="130" r="5" fill="#263238"/>'
    for (x, y, tx, ty, a, txt) in [(90, 140, 60, 80, "middle", "horn (bending)"), (300, 120, 300, 80, "middle", "face (hardened)"), (406, 130, 470, 80, "start", "hardy hole"), (380, 130, 560, 110, "start", "pritchel hole"), (300, 280, 300, 330, "middle", "base / feet on a stump")]:
        s += line(x, y, tx, ty + (6 if ty < y else -14), "#607d8b", 1.5) + t(tx, ty, txt, 13, a, "600")
    s += t(560, 180, "Substitutes:", 15, "start", "700")
    for i, l in enumerate(["• a block of rail or heavy plate on end", "• a sledge head set in a stump", "• a large flat hard stone (use with care)", "• a short piece of thick shaft or axle", "Face height ≈ the smith's knuckles"]):
        s += t(480, 205 + i * 22, l, 13)
    return svg(720, 345, s)

def d_tools():
    s = t(360, 26, "Basic forge tools", 18, "middle", "700")
    # tongs
    s += line(60, 90, 300, 120, "#455a64", 7) + line(60, 130, 300, 110, "#455a64", 7)
    s += '<circle cx="300" cy="115" r="7" fill="#263238"/>' + line(300, 115, 345, 105, "#455a64", 9) + line(300, 115, 345, 125, "#455a64", 9)
    s += t(200, 160, "flat-jaw tongs: reins, rivet, jaws", 13, "middle", "600")
    s += t(200, 178, "jaws must grip the stock flat and tight", 12, "middle")
    # hammer
    s += rect(430, 70, 90, 34, "#90a4ae", "#263238", 2, 4) + rect(468, 104, 14, 90, "#8d6e63", "#5d4037", 2, 4)
    s += t(475, 215, "cross-peen hammer, 1–1.5 kg", 13, "middle", "600")
    s += '<polygon points="520,72 540,87 520,102" fill="#90a4ae" stroke="#263238" stroke-width="2"/>'
    # hardy, punch, drift, swage
    s += '<polygon points="80,300 120,300 110,270 90,270" fill="#78909c" stroke="#263238" stroke-width="2"/><rect x="92" y="300" width="16" height="30" fill="#78909c" stroke="#263238" stroke-width="2"/>'
    s += t(100, 350, "hardy (cutter)", 12, "middle", "600")
    s += rect(190, 250, 18, 70, "#90a4ae", "#263238", 2, 2) + '<polygon points="190,320 208,320 203,340 195,340" fill="#90a4ae" stroke="#263238" stroke-width="2"/>' + t(199, 360, "punch", 12, "middle", "600")
    s += '<polygon points="290,250 310,250 306,330 294,330" fill="#90a4ae" stroke="#263238" stroke-width="2"/>' + t(300, 350, "drift (tapered)", 12, "middle", "600")
    s += rect(380, 260, 120, 60, "#78909c", "#263238", 2, 2)
    for x in (395, 425, 460): s += f'<circle cx="{x}" cy="290" r="9" fill="#fff" stroke="#263238"/>'
    s += t(440, 345, "swage block / bolster", 12, "middle", "600")
    s += rect(560, 250, 30, 80, "#b0bec5", "#263238", 2, 2) + rect(590, 280, 70, 22, "#b0bec5", "#263238", 2, 2) + t(610, 350, "post (leg) vise", 12, "middle", "600")
    return svg(720, 370, s)

def d_heat():
    rows = [("Black red (dull light)", 426, 593, "#3e0d0d"), ("Very dark red", 594, 704, "#5a0f0f"), ("Dark red", 705, 814, "#8b1a10"), ("Cherry red", 815, 870, "#c0261a"),
            ("Light cherry red", 871, 981, "#e0451f"), ("Orange", 982, 1092, "#f57c00"), ("Yellow", 1093, 1258, "#fbc02d"), ("Yellow-white", 1259, 1314, "#fff176"), ("White", 1315, None, "#fffde7")]
    s = t(360, 26, "Heat colors of steel (view in shade, not sunlight)", 18, "middle", "700")
    for i, (nm, a, b, col) in enumerate(rows):
        y = 44 + i * 36
        s += rect(40, y, 180, 30, col, "#263238", 1.5, 3)
        rng = f"{a:,}–{b:,} °C" if b else f"{a:,}+ °C"
        f1 = round(a * 9 / 5 + 32); f2 = round(b * 9 / 5 + 32) if b else None
        rngf = f"{f1:,}–{f2:,} °F" if b else f"{f1:,}+ °F"
        s += t(235, y + 20, nm, 15, "start", "700") + t(450, y + 20, rng, 14) + t(590, y + 20, rngf, 14)
    s += t(360, 380, "Forging: orange–yellow · hardening carbon steel: about cherry red, just non-magnetic · welding: yellow-white", 12.5, "middle", "600")
    return svg(720, 392, s)

def d_temper():
    rows = [("Faint yellow", 176, "#f6eab0", "scrapers, razors"), ("Light straw", 205, "#ecd27a", "metal-cutting tools"), ("Dark straw", 226, "#d8ae55", "scribers, planer blades"),
            ("Brown", 260, "#a8743a", "drills, hammers, cold chisels"), ("Purple", 282, "#7c3f80", "punches, surgical tools"), ("Dark blue", 310, "#2e3f8f", "screwdrivers, wrenches"),
            ("Light blue", 337, "#5d8fd0", "springs, wood saws"), ("Grey-blue", 371, "#8a9aa8", "too soft for edges")]
    s = t(360, 26, "Tempering colors on bright (polished) carbon steel", 18, "middle", "700")
    for i, (nm, c_, col, use) in enumerate(rows):
        y = 44 + i * 38
        s += rect(40, y, 120, 32, col, "#263238", 1.5, 3)
        s += t(175, y + 21, nm, 15, "start", "700") + t(330, y + 21, f"{c_} °C / {round(c_*9/5+32)} °F", 14) + t(500, y + 21, use, 13)
    s += t(360, 362, "Harder ← → tougher. Polish a spot after hardening so you can see the colors run.", 13, "middle", "600")
    return svg(720, 375, s)

def d_hammer():
    s = t(360, 24, "The five basic forging moves", 18, "middle", "700")
    W = 140
    def panel(i, title, body):
        x = 4 + i * W
        return rect(x + 2, 40, W - 8, 300, "#fafafa", "#b0bec5", 1.5, 6) + t(x + W / 2 - 2, 62, title, 14, "middle", "700") + body
    # drawing out
    b = rect(20, 140, 100, 22, "#ff9800", "#bf360c", 2, 3) + arrow(70, 100, 70, 136, INK, 2) + t(70, 95, "hammer", 11, "middle")
    b += '<path d="M20 230 h60 q20 0 40 4 v14 q-20 4 -40 4 h-60z" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'
    b += t(70, 290, "longer + thinner", 12, "middle") + t(70, 306, "use peen or horn,", 12, "middle") + t(70, 322, "then flatten", 12, "middle")
    s += panel(0, "Drawing out", b)
    # upsetting
    x = W
    b = rect(x + 55, 100, 24, 90, "#ff9800", "#bf360c", 2, 3) + arrow(x + 67, 76, x + 67, 96) + line(x + 30, 192, x + 104, 192, INK, 4)
    b += '<path d="M%d 220 h24 v40 q14 6 14 26 h-52 q0 -20 14 -26z" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>' % (x + 55)
    b += t(x + 67, 306, "shorter + fatter;", 12, "middle") + t(x + 67, 322, "heat only the end", 12, "middle")
    s += panel(1, "Upsetting", b)
    # bending
    x = 2 * W
    b = '<path d="M%d 180 h60 q30 0 30 -30 v-50" fill="none" stroke="#ff9800" stroke-width="12"/>' % (x + 15)
    b += rect(x + 15, 186, 70, 30, "#78909c", "#263238", 2, 2) + arrow(x + 120, 80, x + 105, 110)
    b += t(x + 67, 260, "over the anvil edge", 12, "middle") + t(x + 67, 276, "or horn; heat only", 12, "middle") + t(x + 67, 292, "where it should bend", 12, "middle")
    s += panel(2, "Bending", b)
    # punching
    x = 3 * W
    b = rect(x + 25, 170, 90, 24, "#ff9800", "#bf360c", 2, 3) + rect(x + 62, 96, 16, 70, "#90a4ae", "#263238", 2, 2) + arrow(x + 70, 76, x + 70, 94)
    b += rect(x + 25, 196, 90, 20, "#78909c", "#263238", 2, 1) + rect(x + 62, 196, 16, 20, "#fff", "#263238", 1, 0)
    b += t(x + 70, 250, "drive halfway, flip,", 12, "middle") + t(x + 70, 266, "punch out the slug", 12, "middle") + t(x + 70, 282, "over the pritchel or", 12, "middle") + t(x + 70, 298, "hardy hole", 12, "middle")
    s += panel(3, "Punching", b)
    # drifting
    x = 4 * W
    b = '<path d="M%d 180 q45 -50 90 0 q-45 30 -90 0z" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>' % (x + 22)
    b += '<polygon points="%d,90 %d,90 %d,190 %d,190" fill="#90a4ae" stroke="#263238" stroke-width="2"/>' % (x + 60, x + 74, x + 72, x + 62)
    b += t(x + 67, 250, "tapered drift opens", 12, "middle") + t(x + 67, 266, "and sizes the hole", 12, "middle") + t(x + 67, 282, "without removing", 12, "middle") + t(x + 67, 298, "metal (eyes, handles)", 12, "middle")
    s += panel(4, "Drifting", b)
    return svg(708, 350, s)

def d_weld():
    s = t(360, 26, "Scarf (lap) forge weld, step by step", 18, "middle", "700")
    steps_ = ["1 Upset the ends a little", "2 Scarf: hammer each end to a short bevel", "3 Heat to yellow-white; flux at bright red", "4 Overlap fast, strike center then edges"]
    for i, st in enumerate(steps_):
        y = 60 + i * 72
        s += t(30, y + 22, st, 14, "start", "700")
        if i == 0:
            s += rect(380, y, 120, 26, "#ff9800", "#bf360c", 2, 3) + rect(520, y, 120, 26, "#ff9800", "#bf360c", 2, 3)
        elif i == 1:
            s += f'<polygon points="380,{y} 490,{y} 510,{y+26} 380,{y+26}" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'
            s += f'<polygon points="540,{y} 660,{y} 660,{y+26} 520,{y+26}" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'
        elif i == 2:
            s += f'<polygon points="380,{y} 490,{y} 510,{y+26} 380,{y+26}" fill="#fff59d" stroke="#f9a825" stroke-width="2"/>'
            for k in range(8): s += f'<circle cx="{440+k*8}" cy="{y-4}" r="2.5" fill="#90a4ae"/>'
            s += t(600, y + 18, "borax or fine sand", 13, "middle")
        else:
            s += f'<polygon points="380,{y+8} 520,{y+8} 540,{y+30} 380,{y+30}" fill="#fff59d" stroke="#f9a825" stroke-width="2"/>'
            s += f'<polygon points="490,{y} 640,{y} 640,{y+22} 470,{y+22}" fill="#fff59d" stroke="#f9a825" stroke-width="2" opacity="0.9"/>' + arrow(505, y - 26, 505, y - 2)
    s += t(360, 360, "Bevels must face each other so flux and slag squeeze out from the middle.", 13, "middle", "600")
    return svg(720, 375, s)

def d_spark():
    s = t(360, 26, "Spark test patterns (grinding wheel, dim light)", 18, "middle", "700")
    def burst(x, y, n, fork):
        o = ""
        for k in range(n):
            import math
            a = -0.5 + k * (1.0 / max(1, n - 1))
            L = 120 + (k % 3) * 20
            x2, y2 = x + L * math.cos(a), y + L * math.sin(a)
            o += line(x, y, x2, y2, "#f9a825", 2)
            for f in range(fork):
                fx, fy = x + L * (0.55 + 0.15 * f) * math.cos(a), y + L * (0.55 + 0.15 * f) * math.sin(a)
                o += line(fx, fy, fx + 14, fy - 10, "#f57f17", 1.5) + line(fx, fy, fx + 14, fy + 10, "#f57f17", 1.5)
        return o
    rows = [("Wrought iron", "long straight lines, leaf-shaped tails", 0), ("Mild steel", "long, a few small forks", 1), ("Medium-carbon", "more forking", 2), ("High-carbon", "bushy, many forks from the wheel", 4)]
    for i, (nm, d, f) in enumerate(rows):
        y = 70 + i * 75
        s += f'<circle cx="60" cy="{y}" r="24" fill="#b0bec5" stroke="#455a64" stroke-width="2"/>' + burst(84, y, 5, f)
        s += t(360, y - 6, nm, 15, "start", "700") + t(360, y + 14, d, 13)
    s += t(360, 372, "Cast iron: short dull-red sparks · high-speed steel: faint red, sparks at tip · 300-series stainless: few, no forks", 12.5, "middle")
    return svg(720, 385, s)

def d_cement():
    s = t(360, 26, "Pack carburizing / cementation box", 18, "middle", "700")
    s += rect(150, 70, 420, 220, "#cfd8dc", "#37474f", 4, 4)
    for r in range(4):
        y = 90 + r * 50
        s += rect(170, y, 380, 18, "#263238", "#263238", 0, 0)
        s += rect(185, y + 22, 350, 14, "#ff9800", "#bf360c", 2, 2)
    s += rect(150, 290, 420, 14, "#a1887f", "#4e342e", 2, 1) + t(360, 326, "box sealed with clay; heated at red-to-orange heat for hours (cementation: days)", 13, "middle")
    s += t(600, 100, "crushed charcoal", 13, "start", "600") + t(600, 116, "(+ hoof/horn,", 12, "start") + t(600, 131, "leather scraps)", 12, "start") + arrow(596, 105, 552, 100)
    s += t(600, 180, "wrought iron or", 13, "start", "600") + t(600, 196, "mild-steel parts", 13, "start", "600") + arrow(596, 186, 537, 166)
    s += t(360, 352, "Carbon enters the surface as carbon-monoxide gas; then quench to harden the skin.", 13, "middle")
    return svg(720, 365, s)

def d_industry():
    s = t(360, 26, "How bulk steel is made today (overview)", 18, "middle", "700")
    s += label_box(20, 60, 160, 70, ["Iron ore", "+ coke + limestone"], "#efebe9", 13)
    s += label_box(230, 60, 160, 70, ["Blast furnace", "molten pig iron ~4% C"], "#ffe0b2", 13)
    s += label_box(440, 60, 260, 70, ["Basic oxygen furnace", "oxygen lance burns out carbon"], "#bbdefb", 13)
    s += label_box(440, 170, 260, 70, ["Electric arc furnace", "melts mostly scrap"], "#c8e6c9", 13)
    s += label_box(230, 170, 160, 70, ["Scrap steel", "(recycled)"], "#e0e0e0", 13)
    s += label_box(230, 280, 260, 64, ["Ladle refining + continuous casting", "→ rolling mills → products"], "#f3e5f5", 13)
    s += arrow(180, 95, 228, 95) + arrow(390, 95, 438, 95) + arrow(390, 205, 438, 205) + arrow(570, 130, 570, 168, "#90a4ae") + t(580, 152, "some scrap", 11, "start")
    s += arrow(570, 240, 480, 278) + arrow(570, 130, 600, 130, "#ffffff", 0)
    s += t(20, 300, "Historic routes:", 13, "start", "700") + t(20, 318, "Bessemer converter (1856)", 12, "start") + t(20, 334, "open hearth (1860s–1990s)", 12, "start")
    return svg(720, 360, s)

def d_knife():
    s = t(360, 26, "Forging a simple knife blade (a tool)", 18, "middle", "700")
    st = [("1", "Cut a bar of high-carbon steel (e.g. leaf spring)", '<rect x="330" y="{y}" width="260" height="18" rx="2" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'),
          ("2", "Forge the point: hammer the corner back", '<polygon points="330,{y} 560,{y} 590,{y2} 330,{y2}" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'),
          ("3", "Draw the tang; forge bevels lightly", '<polygon points="330,{y} 420,{y} 420,{y0} 560,{y0} 595,{y2} 330,{y2}" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'),
          ("4", "Normalize 3×, file/grind bevels, harden, temper", '<polygon points="330,{y} 420,{y} 420,{y0} 560,{y0} 595,{y2} 330,{y2}" fill="#d8ae55" stroke="#6d4c41" stroke-width="2"/>')]
    for i, (n, txt, shape) in enumerate(st):
        y = 60 + i * 72
        s += f'<circle cx="40" cy="{y+9}" r="15" fill="#37474f"/>' + t(40, y + 14, n, 14, "middle", "700", "#fff") + t(66, y + 14, txt, 13.5, "start", "600")
        s += shape.format(y=y + 26, y0=y + 24, y2=y + 44)
    s += t(360, 362, "Edge thickness before hardening: about a coin's thickness — thin edges warp or crack in the quench.", 12.5, "middle")
    return svg(720, 375, s)

def d_nail():
    s = t(360, 26, "Hand-forged nail and wall hook", 18, "middle", "700")
    s += t(180, 60, "Nail with a nail header", 15, "middle", "700")
    s += '<polygon points="60,120 260,112 260,128 60,120" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>' + t(160, 150, "1 draw a 4-sided taper to a point", 12.5, "middle")
    s += rect(60, 190, 220, 26, "#78909c", "#263238", 2, 2) + rect(158, 190, 12, 26, "#fff", "#263238", 1, 0)
    s += '<polygon points="160,250 168,250 166,216 162,216" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>' + rect(152, 176, 24, 14, "#ff9800", "#bf360c", 2, 3) + arrow(164, 150 + 10, 164, 174)
    s += t(170, 270, "2 nick, drop into header, break off,", 12.5, "middle") + t(170, 286, "3 hammer the head (rosehead: 4 blows)", 12.5, "middle")
    s += t(530, 60, "S-hook / wall hook", 15, "middle", "700")
    s += '<path d="M470 120 q-40 0 -40 40 q0 40 40 40 h40 q40 0 40 40 q0 40 -40 40" fill="none" stroke="#ff9800" stroke-width="10"/>'
    s += t(560, 150, "taper both ends,", 12.5, "start") + t(560, 166, "scroll on the horn,", 12.5, "start") + t(560, 182, "bend in opposite", 12.5, "start") + t(560, 198, "directions", 12.5, "start")
    s += t(360, 330, "Mild steel or wrought iron is ideal: soft, easy to forge, no hardening needed.", 13, "middle", "600")
    return svg(720, 345, s)

def d_hinge():
    s = t(360, 26, "Strap hinge and pintle", 18, "middle", "700")
    s += '<path d="M120 150 h380 q30 0 40 18 q-10 18 -40 18 h-380z" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'
    s += '<circle cx="110" cy="168" r="22" fill="none" stroke="#bf360c" stroke-width="10"/>'
    for x in (220, 330, 440): s += f'<circle cx="{x}" cy="168" r="5" fill="#fff" stroke="#263238"/>'
    s += t(110, 215, "eye: thin the end, roll it", 12.5, "middle") + t(110, 231, "back over the pintle pin", 12.5, "middle")
    s += t(330, 130, "strap: punch nail/screw holes", 12.5, "middle")
    s += rect(50, 250, 120, 18, "#90a4ae", "#263238", 2, 2) + rect(98, 210, 14, 40, "#90a4ae", "#263238", 2, 2) + '<polygon points="50,250 30,259 50,268" fill="#90a4ae" stroke="#263238" stroke-width="2"/>'
    s += t(250, 268, "pintle: bar with an upset, upturned pin,", 12.5, "start") + t(250, 284, "pointed end driven into the post", 12.5, "start")
    return svg(720, 335, s)

def d_sandcast():
    s = t(360, 26, "Two-part sand mold (cross-section)", 18, "middle", "700")
    s += rect(150, 70, 420, 110, "#d7ccc8", "#5d4037", 3, 2) + rect(150, 180, 420, 110, "#bcaaa4", "#5d4037", 3, 2)
    s += t(590, 128, "cope (top)", 13, "start", "600") + t(590, 238, "drag (bottom)", 13, "start", "600")
    s += '<ellipse cx="360" cy="180" rx="90" ry="34" fill="#424242"/>'
    s += rect(250, 70, 22, 98, "#424242", "#424242", 0, 0) + '<polygon points="236,70 286,70 272,92 250,92" fill="#424242"/>' + t(262, 60, "pouring cup + sprue", 12.5, "middle")
    s += rect(440, 70, 22, 98, "#616161", "#616161", 0, 0) + t(452, 60, "riser / vent", 12.5, "middle")
    s += line(272, 166, 300, 176, "#424242", 8) + t(360, 186, "cavity", 13, "middle", "700", "#fff")
    s += t(360, 315, "Green sand: sand + about 5–11% clay + a little water; pack hard around a wooden pattern, then remove it.", 12.5, "middle")
    s += t(360, 333, "Iron must be fully melted (cupola furnace or crucible) — a Tier B/C job.", 12.5, "middle", "600")
    return svg(720, 345, s)

def d_wire():
    s = t(360, 26, "Drawing wire through a draw plate", 18, "middle", "700")
    s += rect(330, 60, 40, 200, "#90a4ae", "#263238", 3, 3)
    for i, r in enumerate([12, 10, 8, 6.5, 5, 4]):
        y = 80 + i * 32
        s += f'<polygon points="330,{y-r-6} 370,{y-r/2} 370,{y+r/2} 330,{y+r+6}" fill="#fff" stroke="#263238" stroke-width="1.5"/>'
    s += rect(120, 125, 210, 14, "#ff9800", "#bf360c", 2, 2) + '<polygon points="310,125 330,128 330,136 310,139" fill="#ff9800"/>'
    s += rect(370, 129, 240, 6, "#ff9800", "#bf360c", 1, 1) + rect(610, 112, 40, 40, "#8d6e63", "#4e342e", 2, 4) + t(630, 172, "tongs or winch", 12.5, "middle")
    s += arrow(640, 100, 690, 100, "#1565c0", 3) + t(690, 92, "pull", 12, "end")
    s += t(225, 165, "point the rod, grease it", 12.5, "middle") + t(350, 285, "hardened steel plate, holes taper toward the exit side", 12.5, "middle")
    s += t(360, 305, "Pull through each hole in turn; anneal (heat to red, cool slowly) when the wire gets springy.", 12.5, "middle")
    return svg(720, 320, s)

def d_rolling():
    s = t(360, 26, "Rolling: hot bar squeezed between turning rolls", 18, "middle", "700")
    s += '<circle cx="360" cy="110" r="70" fill="#b0bec5" stroke="#263238" stroke-width="3"/><circle cx="360" cy="270" r="70" fill="#b0bec5" stroke="#263238" stroke-width="3"/>'
    s += '<path d="M330 80 a40 40 0 0 1 60 0" fill="none" stroke="#263238" stroke-width="2"/>' + '<path d="M390 300 a40 40 0 0 1 -60 0" fill="none" stroke="#263238" stroke-width="2"/>'
    s += '<polygon points="120,172 300,172 360,180 360,180 300,208 120,208" fill="#ff9800" stroke="#bf360c" stroke-width="2"/>'
    s += rect(360, 182, 260, 16, "#ff9800", "#bf360c", 2, 2) + arrow(630, 190, 690, 190, "#1565c0", 3)
    s += t(210, 160, "thick, hot stock", 13, "middle") + t(500, 225, "thinner, longer", 13, "middle")
    s += t(360, 362, "Grooved rolls make bars and rods; a 'three-high' stand rolls back and forth without reversing.", 12.5, "middle")
    return svg(720, 375, s)
