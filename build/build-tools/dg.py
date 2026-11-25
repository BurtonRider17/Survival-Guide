import math
from base import svg, t, lead, arrow, box, INK, BLUE, LBLUE, RED, GRN, GROUND, GSTROKE, STEEL, AMBER, region_map, REGIONS

FIRE1 = "#ff9800"; FIRE2 = "#ffeb3b"; CLAY = "#d7b98e"; DARK = "#3b4752"; WOOD = "#c49a6c"; WOODD = "#8d6e63"

def flame(cx, base, w, h):
    return (f'<path d="M{cx-w/2},{base} C{cx-w/2},{base-h*0.5} {cx-w*0.15},{base-h*0.6} {cx},{base-h} C{cx+w*0.15},{base-h*0.6} {cx+w/2},{base-h*0.5} {cx+w/2},{base} Z" fill="{FIRE1}" opacity="0.85"/>'
            f'<path d="M{cx-w/4},{base} C{cx-w/4},{base-h*0.3} {cx},{base-h*0.4} {cx},{base-h*0.6} C{cx+w*0.05},{base-h*0.4} {cx+w/4},{base-h*0.3} {cx+w/4},{base} Z" fill="{FIRE2}" opacity="0.95"/>')

def coals(x0, x1, y, rows=2, r=7):
    s = ""
    for j in range(rows):
        n = int((x1-x0)/(2*r)) - j
        for i in range(n):
            cx = x0 + r + j*r + i*2*r
            col = ["#e65100", "#ff8f00", "#bf360c", "#ffb300"][(i+j) % 4]
            s += f'<circle cx="{cx}" cy="{y - j*r*1.6}" r="{r}" fill="{col}" stroke="#4e342e" stroke-width="0.6"/>'
    return s

# ------------------------------------------------------------ brake-drum forge
def brake_drum_forge():
    b = '<rect width="780" height="470" fill="#fafbfc"/>'
    b += f'<line x1="0" y1="440" x2="780" y2="440" stroke="{GSTROKE}" stroke-width="2"/>'
    # table/stand
    b += f'<rect x="190" y="206" width="380" height="10" fill="{STEEL}" stroke="{INK}"/>'
    for x in (205, 545):
        b += f'<rect x="{x}" y="216" width="10" height="224" fill="{STEEL}" stroke="{INK}"/>'
    b += f'<line x1="215" y1="380" x2="545" y2="380" stroke="{STEEL}" stroke-width="6"/>'
    # drum walls
    b += f'<path d="M240,110 L252,110 L252,194 L355,194 L355,206 L240,206 Z" fill="#5d6b75" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<path d="M520,110 L508,110 L508,194 L385,194 L385,206 L520,206 Z" fill="#5d6b75" stroke="{INK}" stroke-width="1.5"/>'
    # clay lining forming firepot
    b += f'<path d="M252,112 L252,194 L355,194 L355,186 C330,186 300,140 252,112 Z" fill="{CLAY}" stroke="#8d6e48"/>'
    b += f'<path d="M508,112 L508,194 L385,194 L385,186 C410,186 460,140 508,112 Z" fill="{CLAY}" stroke="#8d6e48"/>'
    # grate
    b += f'<rect x="352" y="182" width="36" height="5" fill="#222"/>'
    for x in (358, 366, 374, 382):
        b += f'<rect x="{x}" y="182" width="3" height="5" fill="#fff"/>'
    # fuel + fire
    b += coals(300, 460, 176, 3, 8)
    b += flame(380, 150, 60, 70) + flame(345, 158, 34, 40) + flame(415, 158, 34, 44)
    # workpiece
    b += f'<rect x="80" y="146" width="300" height="9" fill="#90a4ae" stroke="{INK}"/>'
    b += f'<rect x="300" y="146" width="80" height="9" fill="#ff7043" stroke="{INK}"/>'
    # tuyere pipe vertical
    b += f'<rect x="358" y="206" width="24" height="170" fill="#9e9e9e" stroke="{INK}" stroke-width="1.3"/>'
    # tee
    b += f'<rect x="352" y="292" width="36" height="30" fill="#8a8a8a" stroke="{INK}" stroke-width="1.3"/>'
    # horizontal air pipe to blower
    b += f'<rect x="388" y="296" width="210" height="22" fill="#9e9e9e" stroke="{INK}" stroke-width="1.3"/>'
    # gate valve
    b += f'<rect x="470" y="288" width="14" height="38" fill="{AMBER}" stroke="{INK}"/><line x1="477" y1="288" x2="477" y2="270" stroke="{INK}" stroke-width="2"/><circle cx="477" cy="268" r="6" fill="none" stroke="{INK}" stroke-width="2"/>'
    # ash dump cap
    b += f'<rect x="354" y="376" width="32" height="12" fill="#616161" stroke="{INK}"/>'
    # blower
    b += f'<circle cx="640" cy="307" r="38" fill="#cfd8dc" stroke="{INK}" stroke-width="1.5"/><circle cx="640" cy="307" r="12" fill="#fff" stroke="{INK}"/>'
    b += f'<rect x="598" y="296" width="20" height="22" fill="#cfd8dc" stroke="{INK}"/>'
    # air arrows
    b += arrow(560, 307, 400, 307, BLUE, 1.8, "arb") + arrow(370, 290, 370, 215, BLUE, 1.8, "arb")
    # labels
    b += t(560, 34, "1  Brake drum, open side UP", 10.5, weight="600") + lead(560, 38, 515, 120)
    b += t(560, 49, "   truck drum best (15–16 in);", 9.5) + t(560, 63, "   cast iron, sits in a steel table", 9.5)
    b += t(40, 40, "2  Clay / sand lining forms a bowl-shaped", 10.5, weight="600") + lead(150, 58, 270, 130)
    b += t(40, 54, "   firepot about 4–5 in deep (optional)", 9.5)
    b += t(40, 100, "Workpiece goes in sideways,", 9.5, weight="600") + t(40, 112, "just above the hottest spot", 9.5) + lead(100, 116, 120, 146)
    b += t(560, 160, "3  Grate over the drum hole:", 10.5, weight="600") + lead(560, 164, 390, 184)
    b += t(560, 174, "   ½ in (12 mm) holes drilled in", 9.5) + t(560, 186, "   steel plate, or a few bolts", 9.5)
    b += t(14, 246, "4  Tuyere: 1½–2 in", 10.5, weight="600") + lead(150, 250, 357, 250)
    b += t(14, 260, "   BLACK steel pipe + floor", 9.5) + t(14, 272, "   flange bolted to drum.", 9.5) + t(14, 286, "   NEVER galvanized pipe", 9.5, weight="700", fill=RED) + t(14, 298, "   (zinc fumes)", 9.5, weight="700", fill=RED)
    b += t(14, 340, "5  Tee + removable cap", 10.5, weight="600") + lead(150, 344, 354, 382)
    b += t(14, 354, "   = ash and clinker dump", 9.5)
    b += t(562, 236, "6  Gate valve / slide", 10.5, weight="600") + t(562, 250, "   controls the air", 9.5) + lead(560, 242, 484, 290)
    b += t(600, 368, "7  Air: hand-crank blower,", 10.5, weight="600") + t(600, 382, "   bellows, hair dryer,", 9.5) + t(600, 394, "   or small inflatable blower", 9.5)
    b += t(562, 422, "Stand: top of fire at", 9.5, italic=True) + t(562, 436, "about wrist height", 9.5, italic=True)
    b += t(10, 460, "Outdoors or in an open-sided shed only — burning coal or charcoal makes carbon monoxide.", 9.5, italic=True, fill=RED)
    return svg(780, 470, b, "Brake drum forge cross section")

# ------------------------------------------------------------ charcoal retort + pit
def charcoal_retort():
    b = '<rect width="780" height="420" fill="#fafbfc"/>'
    b += t(16, 24, "A  Double-barrel retort (best yield)", 12.5, weight="700", fill="#8a4b08")
    b += t(500, 24, "B  Pit method (no barrels)", 12.5, weight="700", fill="#8a4b08")
    gy = 330
    b += f'<rect x="0" y="{gy}" width="470" height="90" fill="{GROUND}"/>'
    # blocks
    for x in (70, 330):
        b += f'<rect x="{x}" y="{gy-26}" width="50" height="26" fill="#b0bec5" stroke="{INK}"/>'
    # outer drum lying horizontally
    b += f'<rect x="40" y="110" width="380" height="194" rx="10" fill="#78909c" stroke="{INK}" stroke-width="2"/>'
    b += f'<rect x="48" y="118" width="364" height="178" rx="6" fill="#455a64"/>'
    # fire under
    b += f'<rect x="48" y="250" width="364" height="46" fill="#3e2723"/>'
    for i in range(10):
        b += f'<rect x="{60+i*34}" y="{262+(i%2)*8}" width="30" height="10" rx="4" fill="{WOODD}"/>'
    for cx in (90, 160, 230, 300, 370):
        b += flame(cx, 266, 30, 34)
    # bars
    b += f'<line x1="48" y1="232" x2="412" y2="232" stroke="#222" stroke-width="4"/>'
    # inner drum
    b += f'<rect x="90" y="140" width="290" height="90" rx="8" fill="#b0bec5" stroke="{INK}" stroke-width="1.8"/>'
    for i in range(7):
        for j in range(3):
            b += f'<rect x="{102+i*39}" y="{150+j*26}" width="34" height="20" rx="9" fill="{WOOD}" stroke="{WOODD}" stroke-width="0.8"/>'
    # gas pipe from inner drum down into fire
    b += f'<path d="M380,185 L440,185 L440,280 L412,280" fill="none" stroke="#212121" stroke-width="7"/>'
    b += f'<path d="M380,185 L440,185 L440,280 L412,280" fill="none" stroke="#9e9e9e" stroke-width="3"/>'
    b += arrow(445, 230, 445, 270, RED, 1.4, "arr")
    # chimney
    b += f'<rect x="330" y="50" width="22" height="60" fill="#78909c" stroke="{INK}"/>'
    b += f'<path d="M341,48 C330,30 352,24 340,8" fill="none" stroke="#9e9e9e" stroke-width="3" opacity="0.7"/>'
    # fire door
    b += f'<rect x="34" y="250" width="10" height="44" fill="#212121"/>'
    b += t(150, 68, "1  Outer drum (55 US gal) = firebox", 10, weight="600") + lead(200, 72, 200, 112)
    b += t(110, 100, "2  Inner drum, lid sealed, packed tight", 9.5) + lead(160, 103, 160, 142)
    b += t(290, 352, "3  Gas pipe: wood gas", 9.5, weight="600") + t(290, 364, "   from the inner drum", 9.5) + t(290, 376, "   burns in the firebox", 9.5) + lead(400, 346, 438, 250)
    b += t(360, 68, "4  Chimney", 10, weight="600")
    b += t(10, 352, "5  Start fire in firebox; when the pipe jets flame,", 9.5, weight="600") + t(10, 364, "   the wood gas heats the barrel by itself.", 9.5)
    b += t(10, 380, "6  When the gas flame dies: seal every opening,", 9.5, weight="600") + t(10, 392, "   cool 12–24 h before opening (it can re-ignite).", 9.5)
    b += t(10, 408, "Yield ≈ 25–35% of dry wood weight.", 9.5, italic=True)
    # pit
    px = 500
    b += f'<rect x="{px-10}" y="120" width="290" height="300" fill="{GROUND}"/>'
    b += f'<path d="M{px+30},120 L{px+60},250 L{px+200},250 L{px+230},120 Z" fill="#3e2723" stroke="{GSTROKE}" stroke-width="1.5"/>'
    for j in range(5):
        for i in range(6 - (j == 0)):
            b += f'<rect x="{px+60+i*24 - j*5 + (j==0)*12}" y="{232-j*22}" width="22" height="14" rx="6" fill="#212121" stroke="#ff7043" stroke-width="1"/>'
    # tin / leaves layer
    b += f'<rect x="{px+20}" y="112" width="220" height="6" fill="#9e9e9e" stroke="{INK}"/>'
    b += f'<path d="M{px+10},112 Q{px+130},94 {px+250},112 Z" fill="#a1887f" stroke="{GSTROKE}"/>'
    b += t(px+130, 108, "earth 6 in+", 9, "middle", "600")
    b += t(px, 52, "1  Dig a trench 2–3 ft deep; burn wood", 9.5, weight="600") + t(px, 64, "   in layers until a bed of glowing coals", 9.5)
    b += t(px, 78, "2  Cover with sheet metal or green leaves,", 9.5, weight="600") + t(px, 90, "   then earth; seal every smoke leak", 9.5)
    b += t(px, 278, "3  Wait 1–3 days until cold; dig out.", 9.5, weight="600")
    b += t(px, 292, "   Yield only ≈ 10–20% of wood weight;", 9.5) + t(px, 304, "   some ash, some unburned 'brands'.", 9.5)
    b += t(px, 330, "Same principle as earth mounds:", 9.5, italic=True) + t(px, 342, "heat wood while starving it of air.", 9.5, italic=True)
    return svg(780, 420, b, "Charcoal retort and pit")

# ------------------------------------------------------------ forge layout plan
def forge_layout():
    W, H = 780, 470
    b = f'<rect width="{W}" height="{H}" fill="#fafbfc"/>'
    # shed outline: back wall solid, sides open (dashed roof line)
    b += f'<rect x="90" y="40" width="520" height="350" fill="#f1ede3" stroke="{GSTROKE}" stroke-width="1.2" stroke-dasharray="8,5"/>'
    b += f'<rect x="90" y="36" width="520" height="8" fill="#6d4c41"/>'
    b += t(350, 30, "Back wall (masonry or metal-clad) — roof overhead, sides open for airflow", 9.5, "middle", italic=True)
    b += t(350, 410, "Floor: dirt, gravel, brick or concrete — never wood. Keep 10 ft (3 m) clear of dry grass and stored fuel.", 9.5, "middle", italic=True)
    # forge with hood
    b += f'<rect x="270" y="50" width="130" height="80" rx="6" fill="#b0bec5" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<circle cx="335" cy="90" r="24" fill="#ff7043" stroke="{INK}"/>'
    b += f'<rect x="318" y="44" width="34" height="14" fill="#5d4037"/>'
    b += t(335, 145, "FORGE + hood/chimney", 10, "middle", "700")
    # blower
    b += f'<circle cx="420" cy="92" r="14" fill="#cfd8dc" stroke="{INK}"/><text x="420" y="96" font-size="9" text-anchor="middle">air</text>'
    # anvil
    b += f'<path d="M300,230 L400,230 L400,214 L440,222 L400,250 L300,250 Z" fill="#455a64" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<rect x="300" y="226" width="100" height="28" fill="none"/>'
    b += t(350, 272, "ANVIL on stump", 10, "middle", "700")
    b += t(350, 285, "face at knuckle height", 9, "middle")
    # person
    b += f'<circle cx="350" cy="320" r="16" fill="#ffe0b2" stroke="{INK}"/><path d="M326,330 Q350,350 374,330" fill="none" stroke="{INK}" stroke-width="1.3"/>'
    b += t(350, 362, "Smith: one turn reaches forge, anvil, quench", 9, "middle", italic=True)
    # distance
    b += f'<line x1="250" y1="134" x2="250" y2="228" stroke="{INK}" stroke-width="1.2" marker-start="url(#ar)" marker-end="url(#ar)"/>'
    b += t(244, 176, "1 step", 9.5, "end", "700") + t(244, 188, "3–5 ft", 9.5, "end")
    # slack tub
    b += f'<circle cx="210" cy="95" r="26" fill="{LBLUE}" stroke="{BLUE}" stroke-width="1.5"/>' + t(210, 91, "Slack", 9, "middle", "600") + t(210, 105, "tub", 9, "middle", "600")
    # quench oil
    b += f'<rect x="130" y="210" width="60" height="44" rx="4" fill="#fff3c4" stroke="{AMBER}" stroke-width="1.5"/>' + t(160, 228, "Quench", 9, "middle", "600") + t(160, 240, "oil + LID", 9, "middle", "600")
    # tool rack
    b += f'<rect x="460" y="56" width="120" height="22" fill="#d7ccc8" stroke="{INK}"/>' + t(520, 71, "Tong / tool rack", 9, "middle", "600")
    # post vise and bench
    b += f'<rect x="470" y="200" width="120" height="50" fill="#d7ccc8" stroke="{INK}"/>' + t(530, 222, "Bench +", 9, "middle", "600") + t(530, 234, "post vise", 9, "middle", "600")
    # fuel bin
    b += f'<rect x="110" y="300" width="70" height="50" fill="#424242" stroke="{INK}"/>' + t(145, 322, "Fuel", 9, "middle", "600", "#fff") + t(145, 334, "(lidded)", 8.5, "middle", fill="#fff")
    # extinguisher, water
    b += f'<rect x="530" y="310" width="16" height="34" rx="5" fill="{RED}"/>' + t(556, 324, "Extinguisher (ABC)", 9, weight="600") + t(556, 336, "+ bucket of water / sand", 9)
    # wind
    b += arrow(650, 160, 620, 160, BLUE, 2, "arb") + t(655, 150, "Prevailing wind", 9.5, weight="600", fill=BLUE) + t(655, 163, "blows smoke away", 9, fill=BLUE) + t(655, 175, "from the work position", 9, fill=BLUE)
    b += t(470, 270, "Hardy, swage block,", 9, weight="600") + t(470, 282, "hot cuts near anvil", 9)
    b += t(640, 262, "Exit path kept clear", 9, weight="600", fill=GRN) + arrow(625, 274, 720, 274, GRN, 2)
    b += t(10, 58, "Slack tub:", 9, weight="600") + t(10, 71, "water for", 9) + t(10, 84, "cooling tools", 9) + lead(84, 76, 186, 90) + t(20, 220, "Oil fires:", 9, weight="600", fill=RED) + t(20, 232, "smother with", 9, fill=RED) + t(20, 244, "lid — no water", 9, fill=RED)
    return svg(W, H - 50, b, "Forge shop layout")

# ------------------------------------------------------------ heat colors
HEAT = [("Black / no glow", "below 900", "below 480", "#2b2b2b", "#fff"),
        ("Faint red (dark room)", "900–1000", "480–540", "#43100a", "#fff"),
        ("Blood red", "1050", "565", "#62140b", "#fff"),
        ("Dark cherry", "1175", "635", "#8b1a0c", "#fff"),
        ("Cherry red", "1375", "745", "#b3220f", "#fff"),
        ("Bright cherry", "1450–1500", "790–815", "#d9330f", "#fff"),
        ("Orange", "1650", "900", "#f05a14", "#fff"),
        ("Yellow-\norange", "1800", "980", "#f88f1c", INK),
        ("Yellow", "1950–2000", "1065–1095", "#fbc531", INK),
        ("Light yellow", "2100–2200", "1150–1200", "#fde68a", INK),
        ("White / sparkling", "2300–2500", "1260–1370", "#fffbe8", INK)]

def heat_colors():
    W = 660; n = len(HEAT); x0 = 10; w = (W-20)/n
    H = 360
    b = f'<rect width="{W}" height="{H}" fill="#fafbfc"/>'
    b += t(10, 22, "Colors as seen in SHADE (not bright sunlight). Sunlight hides heat:", 10, weight="600")
    b += t(10, 37, "steel that looks dull red outdoors may actually be orange.", 10, weight="600")
    for i, (nm, f, c, col, tc) in enumerate(HEAT):
        x = x0 + i*w
        b += f'<rect x="{x:.1f}" y="50" width="{w:.1f}" height="100" fill="{col}" stroke="#666" stroke-width="0.5"/>'
        words = nm.replace("\n", " ").split(" ")
        if len(words) > 2: lines = [" ".join(words[:2]), " ".join(words[2:])]
        elif len(nm) > 8: lines = nm.replace("\n", " ").replace("-", "-\n").replace(" ", "\n").split("\n")
        else: lines = [nm]
        lines = [l for l in lines if l]
        for j, ln in enumerate(lines):
            b += t(x+w/2, 70+j*12, ln, 9, "middle", "700", tc)
        fa, _, fb = f.partition("–")
        if fb:
            b += t(x+w/2, 116, f"{fa}–", 9, "middle", "600", tc) + t(x+w/2, 127, f"{fb}°F", 9, "middle", "600", tc)
        else:
            b += t(x+w/2, 127, f"{f.replace('below ', '< ')}°F", 9, "middle", "600", tc)
        cc = c.replace("below ", "< ")
        b += t(x+w/2, 141, f"{cc}°C" if "–" not in cc else cc, 8, "middle", fill=tc)
    def span(i0, i1, y, label, col, sub=""):
        xa = x0 + i0*w + 4; xb = x0 + (i1+1)*w - 4
        s = f'<line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
        s += t((xa+xb)/2, y+16, label, 9.5, "middle", "700", col)
        if sub: s += t((xa+xb)/2, y+29, sub, 8.5, "middle", fill=col)
        return s
    b += span(0, 2, 168, "Danger zone: do not hammer", RED, "carbon steel cracks below red")
    b += span(4, 5, 168, "Harden carbon steel", GRN, "just past non-magnetic")
    b += span(6, 8, 168, "Best forging range", "#8a4b08", "drawing, upsetting, punching")
    b += span(9, 10, 168, "Forge welding", BLUE, "flux; sparks = burning")
    notes = ["• Mild steel and wrought iron forge happily from orange to light yellow; high-carbon",
             "   steel (files, springs) should stay ≤ bright yellow — it crumbles if burned.",
             "• Non-magnetic test: touch a magnet to the hot steel. When it stops sticking",
             "   (≈ cherry red, ~1414°F), carbon steel is at or near hardening temperature.",
             "• White heat with fizzing sparks means the steel is burning (oxidizing).",
             "   Burned steel cannot be saved — cut off that part."]
    for k, ln in enumerate(notes): b += t(10, 232 + k*16, ln.replace("   ", "\u00a0\u00a0\u00a0"), 9.5)
    b += t(10, 342, "Upper figure in each cell °F, lower °C. Temperatures are approximate; color perception varies.", 9, italic=True)
    return svg(W, H, b, "Steel heat colors chart")

# ------------------------------------------------------------ tempering colors
TEMPER = [("Pale yellow", 400, 205, "#efe2a6", "Scrapers, razors, metal-cutting tools (very hard)"),
          ("Light straw", 430, 220, "#e8cf78", "Knife edges (hard use), lathe bits, engraving tools"),
          ("Dark straw", 460, 238, "#d4a84a", "Wood chisels, plane irons, punches, taps, drills"),
          ("Brown / bronze", 490, 255, "#b07a3a", "Axes, hatchets, drawknives, general knives, shears"),
          ("Purple", 530, 277, "#6f3f7a", "Cold chisels, center punches, butcher knives, hammer faces"),
          ("Dark blue", 570, 300, "#2d3f8f", "Screwdrivers, springs, wood saws, machetes"),
          ("Light blue", 600, 315, "#5b86b8", "Springs, tough tools that bend rather than chip"),
          ("Gray-blue", 640, 340, "#8a9aa6", "Too soft for an edge — used only to soften (spring/annealing)")]

def tempering_colors():
    W = 780; rh = 30; y0 = 54
    b = f'<rect width="{W}" height="{y0 + rh*len(TEMPER) + 70}" fill="#fafbfc"/>'
    b += t(20, 22, "Polish the hardened steel bright, reheat slowly, and quench (or pull from heat) when the edge reaches the color you want.", 10, weight="600")
    b += t(20, 38, "Colors are a thin oxide film: they creep from the hot area toward the edge. Harder ↑ more brittle   ·   Softer ↓ tougher.", 9.5)
    for i, (nm, f, c, col, use) in enumerate(TEMPER):
        y = y0 + i*rh
        b += f'<rect x="20" y="{y}" width="150" height="{rh-4}" rx="3" fill="{col}" stroke="#777" stroke-width="0.6"/>'
        tc = "#fff" if i in (4, 5) else INK
        b += t(95, y+17, nm, 10, "middle", "700", tc)
        b += t(250, y+17, f"{f}°F", 10.5, "end", "700") + t(310, y+17, f"{c}°C", 10, "end")
        b += t(330, y+17, use, 10)
    yb = y0 + rh*len(TEMPER)
    # arrow hardness
    b += f'<line x1="188" y1="{y0+4}" x2="188" y2="{yb-8}" stroke="{INK}" stroke-width="1.6" marker-end="url(#ar)"/>'
    b += t(20, yb+20, "Kitchen-oven method (most even): 1 hour at the target temperature, cool, repeat once. Check oven with a thermometer.", 9.5)
    b += t(20, yb+36, "Values are typical for plain carbon steels (files, springs, 10xx); alloy steels can need different temperatures.", 9, italic=True)
    return svg(W, yb + 50, b, "Tempering colors chart")

# ------------------------------------------------------------ sharpening angles
def wedge(cx, top, ang_l, ang_r, L, fill="#90a4ae", convex=False):
    # edge at (cx, top+L) pointing down; sides at given angles from vertical
    ex, ey = cx, top + L
    xl = ex - L*math.tan(math.radians(ang_l)); xr = ex + L*math.tan(math.radians(ang_r))
    if convex:
        d = f'M{xl:.1f},{top} Q{xl+ (ex-xl)*0.15:.1f},{ey-L*0.25:.1f} {ex},{ey} Q{xr-(xr-ex)*0.15:.1f},{ey-L*0.25:.1f} {xr:.1f},{top} Z'
    else:
        d = f'M{xl:.1f},{top} L{ex},{ey} L{xr:.1f},{top} Z'
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="1.3"/>'

def arc_label(cx, cy, a1, a2, r, txt):
    # angles measured from straight up (negative left)
    p1 = (cx + r*math.sin(math.radians(a1)), cy - r*math.cos(math.radians(a1)))
    p2 = (cx + r*math.sin(math.radians(a2)), cy - r*math.cos(math.radians(a2)))
    return f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{r},{r} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{RED}" stroke-width="1.3"/>' + t(cx, cy - r - 6, txt, 10, "middle", "700", RED)

def sharpening_angles():
    W, H = 780, 380
    b = f'<rect width="{W}" height="{H}" fill="#fafbfc"/>'
    items = [
        ("Slicing knife", "15–20° per side", "(30–40° included)", 17.5, 17.5, False),
        ("Utility / camp knife", "20–25° per side", "(40–50° included)", 22.5, 22.5, False),
        ("Chisel, plane iron", "25° bevel + 30° micro", "flat back, one bevel", 0, 27, False),
        ("Felling axe", "convex edge, ≈ 30–35°", "included at the edge", 16, 16, True),
        ("Hoe, shovel, spade", "30–45°, one bevel", "file the inside face", 0, 40, False),
        ("Cold chisel", "60–70° included", "(30–35° per side)", 32.5, 32.5, False)]
    cw = W/len(items)
    for i, (nm, a, sub, al, ar, cv) in enumerate(items):
        cx = cw*i + cw/2
        ta, tb = math.tan(math.radians(al)), math.tan(math.radians(ar))
        L = min(150, cw*0.78/(ta+tb))
        ey = 225; top = ey - L
        ex = cx - L*(tb - ta)/2
        b += t(cx, 40, nm, 11, "middle", "700")
        b += wedge(ex, top, al, ar, L, convex=cv)
        r = min(40, L*0.55)
        a1 = -al if not cv else -17; a2 = ar if not cv else 17
        p1 = (ex + r*math.sin(math.radians(a1)), ey - r*math.cos(math.radians(a1)))
        p2 = (ex + r*math.sin(math.radians(a2)), ey - r*math.cos(math.radians(a2)))
        b += f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{r},{r} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{RED}" stroke-width="1.6"/>'
        b += t(cx, ey + 26, a, 10, "middle", "700", RED)
        b += t(cx, ey + 40, sub, 9.5, "middle")
    b += t(20, 296, "How to hold an angle by hand: 1 in (25 mm) wide blade — raise the spine about 1/3 in (8 mm) off the stone for ≈ 20°; about 1/4 in (6 mm) for ≈ 15°.", 9.5)
    b += t(20, 312, "Marker trick: color the bevel with a marker or soot; after a few strokes you can see whether you are hitting the edge, the heel, or the whole bevel.", 9.5)
    b += t(20, 328, "Thinner angle = sharper but weaker. Go steeper for chopping, hard/frozen wood, bone, or dirty work; thinner for slicing and carving.", 9.5)
    b += t(20, 352, "Angles are typical starting points; for any tool, the best guide is the factory bevel — match it.", 9, italic=True)
    return svg(W, 362, b, "Sharpening angles by tool")

# ------------------------------------------------------------ axe rehafting
def axe_rehafting():
    W, H = 780, 430
    b = f'<rect width="{W}" height="{H}" fill="#fafbfc"/>'
    # Panel A: side section of head on handle
    b += t(20, 24, "A  Section through the eye", 11.5, weight="700", fill="#8a4b08")
    hx = 150
    # handle
    b += f'<path d="M{hx-22},400 L{hx-20},140 L{hx-26},90 L{hx+26},90 L{hx+20},140 L{hx+22},400 Z" fill="{WOOD}" stroke="{INK}" stroke-width="1.3"/>'
    for k in range(5):
        b += f'<path d="M{hx-14+k*7},395 L{hx-12+k*6},100" stroke="#a47c52" stroke-width="0.7" fill="none"/>'
    # head (eye walls) tapered: wider at top
    b += f'<path d="M{hx-26},90 L{hx-20},160 L{hx-60},160 L{hx-60},88 Z" fill="#607d8b" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<path d="M{hx+26},90 L{hx+20},160 L{hx+60},160 L{hx+60},88 Z" fill="#607d8b" stroke="{INK}" stroke-width="1.3"/>'
    # protrusion above head
    b += f'<rect x="{hx-26}" y="80" width="52" height="10" fill="{WOOD}" stroke="{INK}"/>'
    # kerf + wedge
    b += f'<path d="M{hx-1},80 L{hx+1},80 L{hx},150 Z" fill="#3e2723"/>'
    b += f'<path d="M{hx-7},72 L{hx+7},72 L{hx},128 Z" fill="#e6c27a" stroke="{INK}"/>'
    b += t(hx+70, 70, "Wood wedge (dry hardwood)", 9.5, weight="600") + t(hx+70, 82, "driven into the kerf", 9.5) + lead(hx+68, 74, hx+5, 86)
    b += t(hx+70, 112, "Kerf ⅔–¾ of eye depth", 9.5) + lead(hx+68, 108, hx+1, 140)
    b += t(hx+70, 136, "Eye flares wider at top;", 9.5) + t(hx+70, 148, "wedge spreads wood into it", 9.5) + lead(hx+68, 140, hx+40, 100)
    b += t(hx+70, 186, "Trim flush, leave ⅛ in", 9.5) + t(hx+70, 198, "(3 mm) proud", 9.5)
    b += t(hx-30, 300, "Shoulder fits", 9.5, "end") + t(hx-30, 312, "tight below", 9.5, "end") + t(hx-30, 324, "eye, no gaps", 9.5, "end")
    # Panel B: top view
    bx = 580
    b += t(bx-80, 24, "B  Top view of eye", 11.5, weight="700", fill="#8a4b08")
    b += f'<path d="M{bx-150},70 L{bx-40},58 L{bx+60},58 L{bx+80},65 L{bx+80},95 L{bx+60},102 L{bx-40},102 L{bx-150},90 Z" fill="#607d8b" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<ellipse cx="{bx+10}" cy="80" rx="42" ry="14" fill="{WOOD}" stroke="{INK}"/>'
    b += f'<line x1="{bx-30}" y1="80" x2="{bx+50}" y2="80" stroke="#e6c27a" stroke-width="5"/>'
    b += f'<line x1="{bx-6}" y1="68" x2="{bx+26}" y2="92" stroke="#455a64" stroke-width="3"/>'
    b += t(bx-150, 126, "Wood wedge runs the full length of the eye;", 9.5) + t(bx-150, 138, "optional steel wedge at 45° across it.", 9.5)
    b += t(bx-152, 80, "bit", 9, "end", italic=True) + t(bx+86, 84, "poll", 9, italic=True)
    # Panel C: grain orientation
    cx = 450; cy = 230
    b += t(cx-80, 186, "C  Handle end grain", 11.5, weight="700", fill="#8a4b08")
    b += f'<ellipse cx="{cx}" cy="{cy+20}" rx="44" ry="20" fill="#e8d3b0" stroke="{INK}"/>'
    for k in range(-3, 4):
        b += f'<line x1="{cx-40}" y1="{cy+20+k*5}" x2="{cx+40}" y2="{cy+20+k*5}" stroke="#a47c52" stroke-width="1"/>'
    b += f'<ellipse cx="{cx}" cy="{cy+20}" rx="44" ry="20" fill="none" stroke="{INK}" stroke-width="1.3"/>'
    b += t(cx, cy+56, "GOOD: growth rings run", 9.5, "middle", "700", GRN) + t(cx, cy+68, "front-to-back, parallel to the head", 9.5, "middle", fill=GRN)
    b += t(cx, cy+82, "(no grain running out at the shoulder)", 9, "middle", italic=True)
    # Panel D: hang check
    dx = 600
    b += t(dx-40, 186, "D  Check the hang", 11.5, weight="700", fill="#8a4b08")
    b += f'<line x1="{dx-40}" y1="330" x2="{dx+170}" y2="330" stroke="{GSTROKE}" stroke-width="2"/>'
    b += f'<path d="M{dx-10},330 C{dx+40},300 {dx+100},300 {dx+150},318 L{dx+160},310 L{dx+165},330" fill="none" stroke="{WOODD}" stroke-width="9" stroke-linecap="round"/>'
    b += f'<path d="M{dx-26},286 L{dx-4},286 L{dx+8},330 L{dx-14},330 Z" fill="#607d8b" stroke="{INK}"/>'
    b += f'<circle cx="{dx+2}" cy="330" r="4" fill="{RED}"/><circle cx="{dx+164}" cy="330" r="4" fill="{RED}"/>'
    b += t(dx-40, 354, "Laid on a flat table, the edge and the", 9.5) + t(dx-40, 366, "knob should both touch. Sight down the", 9.5) + t(dx-40, 378, "handle from the knob: the edge must line", 9.5) + t(dx-40, 390, "up with the handle's center line.", 9.5)
    b += t(20, 420, "Steps: saw off old handle → drive the wood plug out the TOP of the eye → shave new handle to fit → seat by striking the butt → wedge → oil.", 9.5, italic=True)
    return svg(W, H, b, "Axe rehafting")

# ------------------------------------------------------------ saw teeth
def saw_teeth():
    W, H = 780, 300
    b = f'<rect width="{W}" height="{H}" fill="#fafbfc"/>'
    def teeth(x0, y0, n, pitch, h, rake):
        # rake angle measured from vertical on cutting (front) face; teeth cut moving left
        pts = [(x0, y0)]
        for i in range(n):
            xb = x0 + i*pitch
            tipx = xb + h*math.tan(math.radians(rake))
            pts += [(tipx, y0 - h), (xb + pitch, y0)]
        return '<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="none" stroke="{INK}" stroke-width="1.6"/>'
    b += t(20, 24, "A  Rip-saw teeth (cut WITH the grain)", 11, weight="700", fill="#8a4b08")
    b += f'<rect x="20" y="90" width="330" height="40" fill="#cfd8dc"/>' + teeth(20, 90, 11, 30, 24, 3)
    b += t(20, 150, "Front face ≈ 0–5° from vertical; filed straight across", 9.5) + t(20, 162, "(0° fleam) → each tooth is a tiny chisel.", 9.5)
    b += t(420, 24, "B  Crosscut teeth (cut ACROSS the grain)", 11, weight="700", fill="#8a4b08")
    b += f'<rect x="420" y="90" width="330" height="40" fill="#cfd8dc"/>' + teeth(420, 90, 11, 30, 24, 15)
    b += t(420, 150, "Front face ≈ 15° rake; file held at 20–25° fleam", 9.5) + t(420, 162, "so each tooth is a knife point that severs fibers.", 9.5)
    # set top view
    b += t(20, 200, "C  Set (view looking down on the teeth)", 11, weight="700", fill="#8a4b08")
    b += f'<rect x="20" y="232" width="330" height="10" fill="#90a4ae" stroke="{INK}"/>'
    for i in range(11):
        x = 25 + i*30; dy = -7 if i % 2 == 0 else 7
        b += f'<rect x="{x}" y="{232+dy}" width="16" height="10" fill="#607d8b" stroke="{INK}" stroke-width="0.8"/>'
    b += t(20, 270, "Teeth bent alternately left/right so the kerf is wider than", 9.5) + t(20, 282, "the plate: total set ≈ 1¼–1½ × plate thickness for green wood.", 9.5)
    b += t(420, 200, "D  Order of work", 11, weight="700", fill="#8a4b08")
    steps = ["1  Joint: run a flat file lightly along the tips", "2  Set: saw set or punch, every other tooth", "3  File: same strokes and angle on each tooth", "4  Side-dress: one light stone pass per side", "   if the saw pulls to one side"]
    for i, st in enumerate(steps):
        b += t(432 if st.startswith("   ") else 420, 222 + i*14, st.strip(), 9.5)
    return svg(W, H, b, "Saw teeth and set")

# ------------------------------------------------------------ spark test
def spark_test():
    W, H = 780, 270
    b = f'<rect width="{W}" height="{H}" fill="#1b1f24"/>'
    import random
    def stream(x0, y0, L, nlines, col, bursts, burst_size, forks=0, seed=1):
        rnd = random.Random(seed); s = ""
        for i in range(nlines):
            a = math.radians(rnd.uniform(-6, 6)); l = L*rnd.uniform(0.6, 1.0)
            x1 = x0 + l*math.cos(a); y1 = y0 + l*math.sin(a)
            s += f'<line x1="{x0}" y1="{y0}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="1.1" opacity="0.9"/>'
            for _ in range(forks):
                fx = x0 + (x1-x0)*rnd.uniform(0.7, 1.0); fy = y0 + (y1-y0)*(fx-x0)/(x1-x0 + 1e-6)
                s += f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{fx+8:.1f}" y2="{fy+rnd.uniform(-5,5):.1f}" stroke="{col}" stroke-width="1"/>'
            for _ in range(bursts):
                fpos = rnd.uniform(0.35, 0.95); bx = x0 + (x1-x0)*fpos; by = y0 + (y1-y0)*fpos
                for k in range(6):
                    ang = rnd.uniform(0, 2*math.pi); r = burst_size*rnd.uniform(0.5, 1)
                    s += f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx+r*math.cos(ang):.1f}" y2="{by+r*math.sin(ang):.1f}" stroke="#fff3b0" stroke-width="0.9"/>'
        return s
    rows = [("Mild / low-carbon steel", "long straw-yellow streaks, few forks", 300, 10, "#ffcc66", 0, 0, 2),
            ("Medium carbon (axles, rebar)", "more forks and small bursts", 270, 12, "#ffd27a", 1, 6, 1),
            ("High carbon (files, springs)", "bright, bushy, many starbursts", 230, 16, "#fff0a0", 3, 9, 0),
            ("Cast iron", "short, dull red, few small bursts", 120, 12, "#e5733a", 1, 4, 0)]
    for i, (nm, d, L, nl, col, bu, bs, fk) in enumerate(rows):
        y = 40 + i*60
        b += f'<rect x="20" y="{y-14}" width="44" height="28" fill="#90a4ae"/>'
        b += stream(64, y, L, nl, col, bu, bs, fk, seed=i+3)
        b += t(420, y-4, nm, 11, weight="700", fill="#fff") + t(420, y+11, d, 9.5, fill="#cfd8dc")
    b += t(20, 262, "Grind with a hand grinder in dim light; compare with known samples (a new nail = mild; an old file = high carbon). Wear eye protection.", 9.5, fill="#cfd8dc", italic=True)
    return svg(W, H, b, "Spark test patterns")

# ------------------------------------------------------------ shaving horse + pole lathe
def shaving_horse():
    W, H = 780, 330
    b = f'<rect width="{W}" height="{H}" fill="#fafbfc"/>'
    gy = 290
    b += f'<line x1="0" y1="{gy}" x2="780" y2="{gy}" stroke="{GSTROKE}" stroke-width="2"/>'
    b += t(20, 24, "A  Shaving horse (foot-operated vise)", 11, weight="700", fill="#8a4b08")
    # bench
    b += f'<rect x="40" y="200" width="320" height="16" fill="{WOOD}" stroke="{INK}"/>'
    for x in (55, 330):
        b += f'<line x1="{x}" y1="216" x2="{x-10}" y2="{gy}" stroke="{WOODD}" stroke-width="8"/>'
    # ramp/bridge
    b += f'<path d="M180,200 L300,150 L310,160 L200,200 Z" fill="#d7b98e" stroke="{INK}"/>'
    b += f'<line x1="265" y1="166" x2="275" y2="200" stroke="{WOODD}" stroke-width="6"/>'
    # swinging arm
    b += f'<line x1="292" y1="132" x2="240" y2="270" stroke="{WOODD}" stroke-width="8"/>'
    b += f'<rect x="264" y="124" width="60" height="16" fill="{WOODD}" stroke="{INK}" transform="rotate(-22 294 132)"/>'
    b += f'<circle cx="262" cy="214" r="4" fill="#222"/>'
    b += f'<line x1="215" y1="270" x2="265" y2="270" stroke="{WOODD}" stroke-width="8"/>'
    # workpiece
    b += f'<line x1="230" y1="182" x2="345" y2="134" stroke="#e6c27a" stroke-width="9"/>'
    # seat person simplified
    b += f'<circle cx="110" cy="120" r="16" fill="#ffe0b2" stroke="{INK}"/><line x1="110" y1="136" x2="120" y2="196" stroke="{INK}" stroke-width="3"/>'
    b += f'<path d="M120,196 L190,210 L235,268" fill="none" stroke="{INK}" stroke-width="3"/>'
    b += f'<line x1="112" y1="150" x2="200" y2="170" stroke="{INK}" stroke-width="2.5"/>'
    b += f'<line x1="196" y1="160" x2="206" y2="182" stroke="#455a64" stroke-width="4"/>'
    b += t(140, 60, "Drawknife: pull toward you", 9.5, weight="600") + lead(170, 64, 200, 168)
    b += t(250, 92, "Dumbhead clamps work", 9.5, weight="600") + lead(300, 110, 300, 126)
    b += t(250, 106, "against the ramp", 9.5)
    b += t(270, 250, "Pivot pin", 9.5) + lead(268, 246, 263, 216)
    b += t(130, 286, "Push foot bar → jaws close", 9.5, weight="600")
    # pole lathe
    px = 430
    b += t(px, 24, "B  Spring-pole lathe", 11, weight="700", fill="#8a4b08")
    b += f'<path d="M{px+20},40 Q{px+180},20 {px+330},70" fill="none" stroke="{WOODD}" stroke-width="7"/>'
    b += f'<line x1="{px+20}" y1="40" x2="{px+20}" y2="{gy}" stroke="{WOODD}" stroke-width="6"/>'
    b += f'<line x1="{px+200}" y1="40" x2="{px+200}" y2="186" stroke="#555" stroke-width="1.5"/>'
    b += f'<rect x="{px+60}" y="190" width="270" height="12" fill="{WOOD}" stroke="{INK}"/>'
    for x in (px+80, px+300):
        b += f'<rect x="{x}" y="150" width="16" height="40" fill="{WOODD}" stroke="{INK}"/>'
        b += f'<line x1="{x}" y1="202" x2="{x}" y2="{gy}" stroke="{WOODD}" stroke-width="7"/>'
    b += f'<rect x="{px+96}" y="160" width="204" height="18" rx="9" fill="#e6c27a" stroke="{INK}"/>'
    b += f'<path d="M{px+200},160 C{px+190},164 {px+190},176 {px+200},180 C{px+210},176 {px+210},164 {px+200},160" fill="none" stroke="#555" stroke-width="1.5"/>'
    b += f'<line x1="{px+200}" y1="180" x2="{px+200}" y2="268" stroke="#555" stroke-width="1.5"/>'
    b += f'<path d="M{px+150},272 L{px+260},262" stroke="{WOODD}" stroke-width="7"/>'
    b += t(px+40, 64, "Springy pole pulls the cord back up", 9.5)
    b += t(px+208, 216, "Cord: 2–3 turns", 9.5)
    b += t(px+150, 254, "Treadle", 9.5, weight="600")
    b += t(px+40, 140, "Centers", 9.5, weight="600") + lead(px+70, 144, px+86, 160)
    b += t(px+20, 300, "Treadle down = work spins toward you = cut.", 9.5, italic=True) + t(px+20, 314, "Tool cuts only on the down-stroke.", 9.5, italic=True)
    return svg(W, H, b, "Shaving horse and spring pole lathe")

# ------------------------------------------------------------ joinery
def joinery():
    W, H = 780, 300
    b = f'<rect width="{W}" height="{H}" fill="#fafbfc"/>'
    b += t(20, 24, "A  Pegged mortise & tenon (draw-bored)", 11, weight="700", fill="#8a4b08")
    # post vertical
    b += f'<rect x="60" y="40" width="70" height="230" fill="#e8d3b0" stroke="{INK}" stroke-width="1.3"/>'
    # mortise (dashed)
    b += f'<rect x="60" y="120" width="56" height="60" fill="none" stroke="{INK}" stroke-dasharray="4,3"/>'
    # beam horizontal with tenon
    b += f'<path d="M130,110 L330,110 L330,190 L130,190 L130,180 L116,180 L116,120 L130,120 Z" fill="{WOOD}" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<line x1="130" y1="120" x2="130" y2="180" stroke="{INK}" stroke-dasharray="3,2"/>'
    # holes: post hole and offset tenon hole
    b += f'<circle cx="95" cy="150" r="7" fill="#fff" stroke="{INK}"/>'
    b += f'<circle cx="100" cy="150" r="7" fill="none" stroke="{RED}" stroke-dasharray="2,2"/>'
    b += t(150, 64, "Tenon ≈ ⅓ of beam thickness", 9.5) + lead(150, 68, 124, 124)
    b += t(150, 222, "Peg hole in tenon drilled ~⅛ in (3 mm)", 9.5) + t(150, 234, "closer to the shoulder; the tapered peg", 9.5) + t(150, 246, "pulls the joint tight", 9.5) + lead(148, 226, 95, 156)
    b += t(150, 262, "Pegs: split (not sawn) dry oak/locust, ¾–1 in", 9.5)
    # lap joint
    lx = 430
    b += t(lx, 24, "B  Half-lap (shown pulled apart)", 11, weight="700", fill="#8a4b08")
    b += f'<path d="M{lx},70 L{lx+150},70 L{lx+150},90 L{lx+90},90 L{lx+90},110 L{lx},110 Z" fill="{WOOD}" stroke="{INK}"/>'
    b += f'<path d="M{lx+90},90 L{lx+150},90 L{lx+150},70 L{lx+260},70 L{lx+260},110 L{lx+90},110 Z" fill="#e8d3b0" stroke="{INK}" transform="translate(0,40)"/>'
    b += t(lx, 172, "Each piece cut to half depth; peg or nail.", 9.5)
    b += t(lx, 200, "C  Other workhorse joints", 11, weight="700", fill="#8a4b08")
    for i, s in enumerate(["Bird’s-mouth: rafter seat on wall plate (cut ≤ ⅓ depth)", "Scarf joint: splice beams end-to-end (length ≥ 4× depth)", "Saddle notch: round-log corners", "Wedged through-tenon: chairs, stools, tool handles"]):
        b += t(lx, 222 + i*15, "• " + s, 9.5)
    return svg(W, H, b, "Basic wood joinery")
