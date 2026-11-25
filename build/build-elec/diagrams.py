import math, json

FONT = "IBM Plex Sans, Arial, sans-serif"
INK = "#1f2a33"; BLUE = "#2f7fbf"; LBLUE = "#cfe6f7"; RED = "#c0392b"; GRN = "#2e7d32"
GROUND = "#e6dfc8"; GSTROKE = "#8a7d5a"; STEEL = "#7d8b96"; AMBER = "#e69b00"

def svg(w, h, body, title=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" '
            f'style="font-family:{FONT};max-height:100%" role="img" aria-label="{title}">'
            '<defs>'
            f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            f'<marker id="arb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>'
            f'<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
            '<pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#b9ad8a" stroke-width="1.2"/></pattern>'
            '<pattern id="ins" width="5" height="5" patternUnits="userSpaceOnUse"><circle cx="2.5" cy="2.5" r="1" fill="#b8a27a"/></pattern>'
            f'</defs>{body}</svg>')

def t(x, y, s, size=11, anchor="start", weight="normal", fill=INK, italic=False):
    st = ' font-style="italic"' if italic else ''
    lines = s.split("\n")
    if len(lines) == 1:
        return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}"{st}>{s}</text>'
    # multi-line: em-based line spacing so leading scales with the font
    body = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else 1.2}em">{ln}</tspan>' for i, ln in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}"{st}>{body}</text>'

def lead(x1, y1, x2, y2, col=INK):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="0.8"/><circle cx="{x2}" cy="{y2}" r="2" fill="{col}"/>'

def arrow(x1, y1, x2, y2, col=INK, w=1.4, m="ar", dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" marker-end="url(#{m})"{d}/>'

def box(x, y, w, h, label, fill="#ffffff", stroke=INK, size=11, sw=1.3, weight="600", sub=None, rx=5):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    lines = label.split("\n")
    n = len(lines) + (len(sub.split("\n")) if sub else 0)
    y0 = y + h/2 - (n-1)*size*0.6 + size*0.35
    # one text element, em-based line steps, so leading scales with the font
    sp = "".join(f'<tspan x="{x+w/2}" dy="{0 if i == 0 else 1.2}em">{ln}</tspan>' for i, ln in enumerate(lines))
    if sub:
        k = size / (size - 1.5)
        sp += "".join(f'<tspan x="{x+w/2}" dy="{1.2*k:.3f}em" font-size="{size-1.5}" font-weight="normal" fill="#44525e">{ln}</tspan>' for ln in sub.split("\n"))
    s += f'<text x="{x+w/2}" y="{y0:.1f}" font-size="{size}" text-anchor="middle" font-weight="{weight}" fill="{INK}">{sp}</text>'
    return s

# ---------------------------------------------------------------- 1 micro-hydro layout
def hydro_layout():
    b = ""
    b += '<rect x="0" y="0" width="780" height="380" fill="#f4f9fd"/>'
    # ground
    gpts = [(0,80),(170,80),(260,130),(380,200),(500,290),(780,300)]
    poly = " ".join(f"{x},{y}" for x,y in gpts) + " 780,380 0,380"
    b += f'<polygon points="{poly}" fill="{GROUND}" stroke="{GSTROKE}" stroke-width="1.5"/>'
    # stream on plateau
    b += f'<rect x="0" y="66" width="128" height="14" fill="{BLUE}" opacity="0.75"/>'
    b += t(10, 60, "Stream", 11, weight="600", fill=BLUE)
    # natural stream continuing down hill (thin, behind)
    b += f'<path d="M140,84 C200,100 230,140 300,165 S420,250 470,300 L780,312" fill="none" stroke="{BLUE}" stroke-width="3" opacity="0.45"/>'
    # weir
    b += f'<rect x="128" y="58" width="9" height="24" fill="#9aa5ad" stroke="{INK}"/>'
    # forebay tank with screen
    b += f'<rect x="146" y="50" width="36" height="32" fill="#fff" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<rect x="147" y="60" width="34" height="21" fill="{BLUE}" opacity="0.55"/>'
    b += '<line x1="152" y1="52" x2="152" y2="81" stroke="#333" stroke-width="1.2" stroke-dasharray="2,2"/>'
    b += f'<path d="M137,66 L146,66" stroke="{BLUE}" stroke-width="5"/>'
    # penstock
    pen = [(180,78),(262,124),(382,194),(486,272),(506,282)]
    b += '<polyline points="' + " ".join(f"{x},{y}" for x,y in pen) + f'" fill="none" stroke="#3b4752" stroke-width="7" stroke-linejoin="round"/>'
    b += '<polyline points="' + " ".join(f"{x},{y}" for x,y in pen) + f'" fill="none" stroke="#7f8f9b" stroke-width="3" stroke-linejoin="round"/>'
    # valve near turbine
    b += '<circle cx="486" cy="272" r="5" fill="#fff" stroke="#000"/>'
    # powerhouse
    b += f'<rect x="500" y="250" width="66" height="44" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<polygon points="494,250 533,226 572,250" fill="#b85c38" stroke="{INK}"/>'
    b += f'<circle cx="520" cy="278" r="11" fill="#cfd8dc" stroke="{INK}"/>'
    b += f'<rect x="537" y="270" width="20" height="16" fill="{AMBER}" stroke="{INK}"/>'
    b += t(547, 282, "G", 9, "middle", "700")
    # tailrace
    b += f'<path d="M520,294 C530,308 560,312 600,310" fill="none" stroke="{BLUE}" stroke-width="4"/>'
    # transmission to house (buried cable)
    b += f'<path d="M566,262 L640,262 L640,296 L700,296 L700,268" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="6,3"/>'
    # house
    b += f'<rect x="680" y="226" width="86" height="70" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<polygon points="672,226 723,190 774,226" fill="#6d4c41" stroke="{INK}"/>'
    b += f'<rect x="690" y="262" width="22" height="24" fill="#90a4ae" stroke="{INK}"/>'
    b += t(701, 278, "BAT", 7, "middle", "700", "#fff")
    b += f'<rect x="718" y="236" width="18" height="16" fill="#fff" stroke="{INK}"/>' + t(727,247,"C",8,"middle","700")
    b += f'<rect x="742" y="236" width="18" height="16" fill="#fff" stroke="{INK}"/>' + t(751,247,"INV",6,"middle","700")
    b += f'<rect x="740" y="266" width="20" height="20" fill="#ffccbc" stroke="{INK}"/>' + t(750,279,"DL",7,"middle","700")
    # gross head dimension
    b += '<line x1="182" y1="60" x2="630" y2="60" stroke="#555" stroke-dasharray="4,3" stroke-width="0.9"/>'
    b += '<line x1="530" y1="278" x2="630" y2="278" stroke="#555" stroke-dasharray="4,3" stroke-width="0.9"/>'
    b += f'<line x1="620" y1="62" x2="620" y2="276" stroke="{INK}" stroke-width="1.4" marker-start="url(#ar)" marker-end="url(#ar)"/>'
    b += t(626, 160, "GROSS HEAD", 11, weight="700") + t(626, 174, "vertical drop from", 9.5) + t(626, 186, "forebay water surface", 9.5) + t(626, 198, "to turbine nozzle", 9.5)
    # labels
    b += t(64, 128, "1  Intake weir + screen", 10.5, weight="600") + lead(110, 124, 133, 80)
    b += t(64, 141, "   (diverts part of flow)", 9.5)
    b += t(160, 26, "2  Forebay / settling tank", 10.5, weight="600") + lead(200, 30, 172, 52)
    b += t(160, 39, "   keeps pipe inlet submerged, drops silt", 9.5)
    b += t(330, 140, "3  Penstock (pressure pipe)", 10.5, weight="600") + lead(330, 144, 318, 160)
    b += t(330, 153, "   buried for UV + frost protection;", 9.5) + t(330, 165, "   no high humps (air traps)", 9.5)
    b += t(380, 236, "Shut-off valve", 9.5) + lead(445, 240, 482, 270)
    b += t(436, 345, "4  Powerhouse: turbine + generator (G)", 10.5, weight="600") + lead(500, 336, 520, 290)
    b += t(580, 330, "5  Tailrace returns ALL water to stream", 10.5, weight="600") + lead(600, 322, 596, 311)
    b += t(560, 362, "6  Transmission cable (buried, in conduit)", 10.5, weight="600") + lead(640, 353, 640, 296)
    b += t(682, 214, "7  House", 10.5, weight="700", fill="#fff")
    b += t(676, 318, "C = controller  INV = inverter", 8.5) + t(676, 329, "BAT = batteries  DL = dump load", 8.5)
    b += t(10, 372, "Net head = gross head − pipe friction losses (design for ≤10% loss).", 9.5, italic=True)
    return svg(780, 380, b, "Micro-hydro system layout")

# ---------------------------------------------------------------- 2 Pelton
def pelton():
    cx, cy, R = 220, 175, 105
    b = '<rect x="0" y="0" width="760" height="360" fill="#fafbfc"/>'
    # housing
    b += f'<path d="M{cx-150},{cy+150} L{cx-150},{cy-60} A150,150 0 0 1 {cx+150},{cy-60} L{cx+150},{cy+150}" fill="none" stroke="#8d99a3" stroke-width="2" stroke-dasharray="7,4"/>'
    b += t(cx+118, cy-118, "Housing", 10, fill="#5b6770")
    # disc
    b += f'<circle cx="{cx}" cy="{cy}" r="{R-18}" fill="#e3e8ec" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="16" fill="#9fb0bc" stroke="{INK}"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="6" fill="{INK}"/>'
    # pitch circle
    b += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{RED}" stroke-width="0.9" stroke-dasharray="5,4"/>'
    # buckets
    N = 18
    for i in range(N):
        th = 2*math.pi*i/N + math.pi/2
        px, py = cx + R*math.cos(th), cy + R*math.sin(th)
        ux, uy = math.sin(th), -math.cos(th)     # motion direction
        nx, ny = math.cos(th), math.sin(th)      # radial outward
        def P(u, n):
            return f"{px+u*ux+n*nx:.1f},{py+u*uy+n*ny:.1f}"
        d = (f"M{P(-6,22)} Q{P(16,24)} {P(12,2)} Q{P(16,-20)} {P(-6,-18)} "
             f"Q{P(4,-8)} {P(5,2)} Q{P(4,12)} {P(-6,22)} Z")
        b += f'<path d="{d}" fill="#90a4ae" stroke="{INK}" stroke-width="1"/>'
        b += f'<line x1="{P(0,-18)}".split(",")[0] />' if False else ""
    # nozzle + pipe (jet tangent to pitch circle at bottom, moving +x)
    jy = cy + R
    b += f'<rect x="0" y="{jy-14}" width="70" height="28" fill="#5d6d78" stroke="{INK}"/>'
    b += f'<polygon points="70,{jy-14} 112,{jy-5} 112,{jy+5} 70,{jy+14}" fill="#5d6d78" stroke="{INK}"/>'
    b += f'<polygon points="30,{jy-4} 100,{jy-1.5} 100,{jy+1.5} 30,{jy+4}" fill="#cfd8dc" stroke="{INK}" stroke-width="0.7"/>'
    b += f'<rect x="112" y="{jy-4}" width="{cx-112-4}" height="8" fill="{BLUE}" opacity="0.85"/>'
    b += arrow(cx-80, jy+26, cx-30, jy+26, BLUE, 1.6, "arb")
    b += t(cx-90, jy+42, "Jet  v ≈ 0.97·√(2gH)", 10, fill=BLUE, weight="600")
    # splash down
    b += f'<path d="M{cx+5},{jy+12} q8,20 2,44 M{cx+18},{jy+10} q14,20 12,44" stroke="{BLUE}" fill="none" stroke-width="1.5" stroke-dasharray="3,3"/>'
    # rotation arrow (bottom moves right => counter-clockwise on screen)
    b += f'<path d="M{cx+40},{cy-40} A56,56 0 0 0 {cx-40},{cy-40}" fill="none" stroke="{INK}" stroke-width="1.6" marker-end="url(#ar)"/>'
    b += t(cx, cy-62, "rotation", 10, "middle", italic=True)
    # labels left
    b += t(4, jy-30, "Nozzle + spear valve", 10.5, weight="600") + t(4, jy-18, "(spear adjusts flow)", 9.5)
    b += t(cx+122, cy+40, "Pitch circle — jet", 10, fill=RED) + t(cx+122, cy+52, "is tangent to it", 10, fill=RED)
    b += lead(cx+120, cy+42, cx+R*math.cos(0.45), cy+R*math.sin(0.45), RED)
    b += t(cx-148, cy-100, "Runner (disc", 10.5, weight="600") + t(cx-148, cy-88, "+ split buckets)", 10.5, weight="600")
    b += t(cx-30, 350, "Water drops freely into tailrace — runner must sit ABOVE tailwater", 9.5, "middle", italic=True)
    # inset: bucket seen from jet
    ox, oy = 470, 40
    b += f'<rect x="{ox}" y="{oy}" width="280" height="290" rx="8" fill="#fff" stroke="#b0bec5"/>'
    b += t(ox+140, oy+20, "One bucket, seen from the jet", 11.5, "middle", "700")
    bx, by = ox+140, oy+140
    b += f'<path d="M{bx},{by-70} C{bx-30},{by-72} {bx-75},{by-50} {bx-80},{by} C{bx-75},{by+55} {bx-30},{by+72} {bx},{by+70} C{bx+30},{by+72} {bx+75},{by+55} {bx+80},{by} C{bx+75},{by-50} {bx+30},{by-72} {bx},{by-70} Z" fill="#cfd8dc" stroke="{INK}" stroke-width="1.4"/>'
    b += f'<ellipse cx="{bx-38}" cy="{by}" rx="32" ry="55" fill="#a7b6bf" stroke="#546e7a"/>'
    b += f'<ellipse cx="{bx+38}" cy="{by}" rx="32" ry="55" fill="#a7b6bf" stroke="#546e7a"/>'
    b += f'<line x1="{bx}" y1="{by-66}" x2="{bx}" y2="{by+66}" stroke="{INK}" stroke-width="2.2"/>'
    b += f'<path d="M{bx-14},{by-70} L{bx},{by-56} L{bx+14},{by-70}" fill="#fff" stroke="{INK}"/>'
    b += f'<circle cx="{bx}" cy="{by}" r="9" fill="{BLUE}" opacity="0.85"/>'
    b += f'<path d="M{bx-6},{by+4} C{bx-40},{by+40} {bx-80},{by+30} {bx-96},{by-6}" fill="none" stroke="{BLUE}" stroke-width="2" marker-end="url(#arb)"/>'
    b += f'<path d="M{bx+6},{by+4} C{bx+40},{by+40} {bx+80},{by+30} {bx+96},{by-6}" fill="none" stroke="{BLUE}" stroke-width="2" marker-end="url(#arb)"/>'
    b += t(bx, oy+222+12, "Splitter ridge divides the jet; each half", 9.5, "middle")
    b += t(bx, oy+234+12, "turns ~165° and leaves sideways/backward,", 9.5, "middle")
    b += t(bx, oy+246+12, "giving up most of its energy.", 9.5, "middle")
    b += t(bx, oy+262+14, "Notch (top) lets the jet reach the next bucket.", 9.5, "middle", italic=True)
    b += t(bx+18, oy+46, "notch", 9, fill="#444")
    b += t(bx-12, by+20, "jet", 9, "end", fill=BLUE, weight="600")
    return svg(760, 360, b, "Pelton wheel")

# ---------------------------------------------------------------- 3 measuring head
def head_measure():
    b = '<rect x="0" y="0" width="780" height="330" fill="#fafbfc"/>'
    def g(x):  # ground profile
        return 40 + 0.52*(x-20) + 10*math.sin(x/37.0)
    pts = [(x, g(x)) for x in range(20, 521, 5)]
    b += '<polygon points="' + " ".join(f"{x},{y:.1f}" for x,y in pts) + f' 520,330 20,330" fill="{GROUND}" stroke="{GSTROKE}" stroke-width="1.5"/>'
    x0 = 40; L = 112; total = 0; hs = []
    xi, yi = x0, g(x0)
    b += f'<rect x="20" y="{yi-12:.1f}" width="30" height="8" fill="{BLUE}" opacity="0.7"/>'
    b += t(22, yi-18, "Intake water level", 9.5, fill=BLUE, weight="600")
    for i in range(4):
        xe = xi + L
        ye = g(xe)
        # board
        b += f'<rect x="{xi}" y="{yi-5:.1f}" width="{L}" height="5" fill="#a1785c" stroke="#5d4037" stroke-width="0.8"/>'
        # level on board
        b += f'<rect x="{xi+L/2-16}" y="{yi-12:.1f}" width="32" height="7" fill="#ffd54f" stroke="#795548" stroke-width="0.8"/>'
        b += f'<circle cx="{xi+L/2}" cy="{yi-8.5:.1f}" r="2" fill="#4caf50"/>'
        # stick
        b += f'<line x1="{xe}" y1="{yi-5:.1f}" x2="{xe}" y2="{ye:.1f}" stroke="#37474f" stroke-width="3"/>'
        h = ye - yi
        hs.append(h)
        b += f'<line x1="{xe+9}" y1="{yi:.1f}" x2="{xe+9}" y2="{ye:.1f}" stroke="{RED}" stroke-width="1.1" marker-start="url(#arr)" marker-end="url(#arr)"/>'
        b += t(xe+14, (yi+ye)/2+4, f"h{i+1}", 11, weight="700", fill=RED)
        xi, yi = xe, ye
    b += f'<rect x="{xi-14}" y="{yi-22:.1f}" width="28" height="22" fill="#fff" stroke="{INK}"/>' + t(xi, yi-7, "T", 10, "middle", "700")
    b += t(xi-60, yi+26, "Turbine site", 10, weight="600")
    b += t(30, 300, "Gross head = h1 + h2 + h3 + h4 + …", 12, weight="700")
    b += t(30, 318, "Board must be dead level each time;", 9.5) + t(30, 333, "measure from the board's underside straight down.", 9.5)
    b += t(150, 40, "Straight board (8–12 ft / 2.5–3.5 m)", 9.5) + lead(200, 44, 120, g(40)-4)
    b += t(270, 90, "Carpenter's level", 9.5) + lead(300, 94, 262, g(152)-10)
    b += t(400, 128, "Measuring stick held plumb", 9.5) + lead(400, 132, 376, g(376)-20)
    # gauge method panel
    ox = 545
    b += f'<rect x="{ox}" y="12" width="225" height="326" rx="8" fill="#fff" stroke="#b0bec5"/>'
    b += t(ox+112, 32, "Hose + pressure gauge", 12, "middle", "700")
    b += f'<path d="M{ox+30},60 C{ox+70},70 {ox+80},150 {ox+120},190 S{ox+160},230 {ox+160},236" fill="none" stroke="{GRN}" stroke-width="5"/>'
    b += f'<rect x="{ox+18}" y="50" width="26" height="12" fill="{BLUE}" opacity="0.7"/>'
    b += t(ox+20, 46, "Hose end under water", 9, fill=BLUE)
    b += f'<circle cx="{ox+160}" cy="254" r="17" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    b += f'<line x1="{ox+160}" y1="254" x2="{ox+170}" y2="244" stroke="{RED}" stroke-width="2"/>'
    b += t(ox+120, 288, "Gauge at turbine site", 9.5, "middle")
    b += t(ox+14, 116, "No flow (end", 9.5) + t(ox+14, 130, "capped), purge", 9.5) + t(ox+14, 144, "all air bubbles", 9.5)
    b += t(ox+112, 308, "ft of head = psi × 2.31", 10.5, "middle", "700", RED)
    b += t(ox+112, 324, "m of head = kPa ÷ 9.81", 10.5, "middle", "700", RED)
    return svg(780, 345, b, "Measuring head")

# ---------------------------------------------------------------- 4 solar wiring
def solar_wiring():
    b = '<rect x="0" y="0" width="780" height="330" fill="#fafbfc"/>'
    # PV panel
    b += f'<rect x="20" y="30" width="120" height="76" fill="#1a3a5c" stroke="{INK}" stroke-width="1.5"/>'
    for i in range(1,6): b += f'<line x1="{20+i*20}" y1="30" x2="{20+i*20}" y2="106" stroke="#6d8fb3" stroke-width="0.7"/>'
    for j in range(1,4): b += f'<line x1="20" y1="{30+j*19}" x2="140" y2="{30+j*19}" stroke="#6d8fb3" stroke-width="0.7"/>'
    b += t(80, 22, "Solar panel(s)", 11, "middle", "700")
    def fuse(x, y, lab, vert=False):
        if vert:
            return f'<rect x="{x-6}" y="{y-13}" width="12" height="26" rx="3" fill="#fff3e0" stroke="{AMBER}" stroke-width="1.6"/><line x1="{x}" y1="{y-13}" x2="{x}" y2="{y+13}" stroke="{AMBER}" stroke-width="1"/>' + t(x+10, y+4, lab, 9, fill="#8a5a00", weight="600")
        return f'<rect x="{x-13}" y="{y-6}" width="26" height="12" rx="3" fill="#fff3e0" stroke="{AMBER}" stroke-width="1.6"/><line x1="{x-13}" y1="{y}" x2="{x+13}" y2="{y}" stroke="{AMBER}" stroke-width="1"/>' + t(x, y-10, lab, 9, "middle", fill="#8a5a00", weight="600")
    # wires PV -> breaker -> controller
    b += f'<polyline points="120,106 120,140 200,140" fill="none" stroke="{RED}" stroke-width="2.5"/>'
    b += f'<polyline points="40,106 40,170 260,170" fill="none" stroke="#111" stroke-width="2.5"/>'
    b += fuse(215, 140, "PV breaker / disconnect")
    b += f'<line x1="228" y1="140" x2="260" y2="140" stroke="{RED}" stroke-width="2.5"/>'
    # controller
    b += box(260, 120, 120, 70, "Charge\ncontroller", "#e8f5e9", GRN, 11, sub="MPPT or PWM")
    # controller -> battery
    b += f'<polyline points="380,140 470,140 470,215" fill="none" stroke="{RED}" stroke-width="2.5"/>'
    b += fuse(420, 140, "Fuse")
    b += f'<polyline points="380,170 440,170 440,235 455,235" fill="none" stroke="#111" stroke-width="2.5"/>'
    # battery
    b += f'<rect x="455" y="215" width="110" height="70" rx="4" fill="#90a4ae" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<rect x="465" y="207" width="16" height="8" fill="#111"/><rect x="539" y="207" width="16" height="8" fill="{RED}"/>'
    b += t(510, 255, "Battery bank", 11.5, "middle", "700", "#fff") + t(510, 270, "12 / 24 / 48 V", 9.5, "middle", fill="#fff")
    b += t(547, 203, "+", 12, "middle", "700", RED) + t(473, 203, "−", 12, "middle", "700")
    # battery -> inverter
    b += f'<polyline points="547,207 547,190 600,190" fill="none" stroke="{RED}" stroke-width="3.5"/>'
    b += fuse(575, 190, "Main fuse ≤18 cm")
    b += f'<line x1="588" y1="190" x2="620" y2="190" stroke="{RED}" stroke-width="3.5"/>'
    b += f'<polyline points="473,207 473,196 500,196 500,300 610,300 610,230 620,230" fill="none" stroke="#111" stroke-width="3.5"/>'
    b += box(620, 170, 100, 74, "Inverter", "#e3f2fd", BLUE, 11.5, sub="DC → 120/230 V AC")
    b += f'<line x1="720" y1="207" x2="745" y2="207" stroke="{INK}" stroke-width="2"/>'
    b += box(690, 40, 80, 56, "AC loads", "#fff", INK, 10.5, sub="via AC breaker")
    b += f'<polyline points="745,207 750,207 750,96" fill="none" stroke="{INK}" stroke-width="2" marker-end="url(#ar)"/>'
    # DC loads from controller load terminal
    b += box(270, 30, 100, 50, "DC loads", "#fff", INK, 10.5, sub="lights, radio")
    b += f'<line x1="320" y1="120" x2="320" y2="80" stroke="{RED}" stroke-width="2"/>'
    b += fuse(320, 100, "", vert=True) + t(330, 104, "Fuse", 9, fill="#8a5a00", weight="600")
    # ground
    b += f'<polyline points="670,244 670,312 300,312 300,190" fill="none" stroke="{GRN}" stroke-width="1.8" stroke-dasharray="5,3"/>'
    b += f'<line x1="150" y1="312" x2="300" y2="312" stroke="{GRN}" stroke-width="1.8" stroke-dasharray="5,3"/><line x1="150" y1="312" x2="150" y2="300" stroke="{GRN}" stroke-width="1.8" stroke-dasharray="5,3"/>'
    b += f'<line x1="80" y1="106" x2="80" y2="312" stroke="{GRN}" stroke-width="1.8" stroke-dasharray="5,3"/><line x1="80" y1="312" x2="150" y2="312" stroke="{GRN}" stroke-width="1.8" stroke-dasharray="5,3"/>'
    b += f'<line x1="138" y1="300" x2="162" y2="300" stroke="{GRN}" stroke-width="2"/><line x1="142" y1="294" x2="158" y2="294" stroke="{GRN}" stroke-width="2"/><line x1="146" y1="288" x2="154" y2="288" stroke="{GRN}" stroke-width="2"/>'
    b += t(170, 326, "Equipment ground (green, dashed) → ground rod", 9.5, fill=GRN, weight="600")
    # legend
    b += f'<line x1="20" y1="240" x2="45" y2="240" stroke="{RED}" stroke-width="3"/>' + t(50, 244, "Positive (+)", 9.5)
    b += f'<line x1="20" y1="258" x2="45" y2="258" stroke="#111" stroke-width="3"/>' + t(50, 262, "Negative (−)", 9.5)
    b += t(20, 210, "Connect battery to controller", 9.5, weight="700", fill=RED) + t(20, 222, "BEFORE connecting panels.", 9.5, weight="700", fill=RED)
    return svg(780, 330, b, "Solar battery inverter wiring")

# ---------------------------------------------------------------- 5 series vs parallel
def batt(x, y, lab="12 V\n100 Ah"):
    s = f'<rect x="{x}" y="{y}" width="56" height="44" rx="3" fill="#b0bec5" stroke="{INK}" stroke-width="1.2"/>'
    s += f'<rect x="{x+5}" y="{y-6}" width="10" height="6" fill="{RED}"/><rect x="{x+41}" y="{y-6}" width="10" height="6" fill="#111"/>'
    s += t(x+10, y-9, "+", 10, "middle", "700", RED) + t(x+46, y-9, "−", 11, "middle", "700")
    s += t(x+28, y+20, lab.split("\n")[0], 10, "middle", "700") + t(x+28, y+33, lab.split("\n")[1], 9, "middle")
    return s

def series_parallel():
    b = '<rect x="0" y="0" width="780" height="300" fill="#fafbfc"/>'
    W = 2.4
    # Series panel
    b += t(125, 20, "SERIES: voltage adds", 12.5, "middle", "700")
    xs = [20, 82, 144, 206]; y = 70
    for x in xs: b += batt(x, y)
    for i in range(3):
        b += f'<path d="M{xs[i]+46},{y-6} C{xs[i]+50},{y-26} {xs[i+1]+6},{y-26} {xs[i+1]+10},{y-6}" fill="none" stroke="{INK}" stroke-width="{W}"/>'
    b += f'<polyline points="{xs[0]+10},{y-6} {xs[0]+10},{y-40} 40,{y-40}" fill="none" stroke="{RED}" stroke-width="{W}"/>'
    b += f'<polyline points="{xs[3]+46},{y-6} {xs[3]+46},{y-40} 230,{y-40}" fill="none" stroke="#111" stroke-width="{W}"/>'
    b += t(26, y-44, "+ out", 9.5, fill=RED, weight="600") + t(210, y-44, "− out", 9.5, weight="600")
    b += t(125, 140, "4 × 12 V 100 Ah  →  48 V, 100 Ah", 11, "middle", "700", BLUE)
    b += t(125, 155, "(4.8 kWh)  + of one to − of the next", 9.5, "middle")
    # Parallel panel
    ox = 275
    b += t(ox+125, 20, "PARALLEL: amp-hours add", 12.5, "middle", "700")
    for x in [ox+20, ox+82, ox+144, ox+206]: b += batt(x, y)
    b += f'<line x1="{ox+30}" y1="{y-22}" x2="{ox+216}" y2="{y-22}" stroke="{RED}" stroke-width="{W}"/>'
    for x in [ox+20, ox+82, ox+144, ox+206]:
        b += f'<line x1="{x+10}" y1="{y-6}" x2="{x+10}" y2="{y-22}" stroke="{RED}" stroke-width="{W}"/>'
        b += f'<line x1="{x+46}" y1="{y-6}" x2="{x+46}" y2="{y-34}" stroke="#111" stroke-width="{W}"/>'
    b += f'<line x1="{ox+66}" y1="{y-34}" x2="{ox+252}" y2="{y-34}" stroke="#111" stroke-width="{W}"/>'
    b += f'<polyline points="{ox+30},{y-22} {ox+30},{y-50}" fill="none" stroke="{RED}" stroke-width="{W}"/>'
    b += f'<polyline points="{ox+252},{y-34} {ox+252},{y-50}" fill="none" stroke="#111" stroke-width="{W}"/>'
    b += t(ox+36, y-50, "+ out (first battery)", 9, fill=RED, weight="600") + t(ox+246, y-50, "− out (last)", 9, "end", weight="600")
    b += t(ox+125, 140, "4 × 12 V 100 Ah  →  12 V, 400 Ah", 11, "middle", "700", BLUE)
    b += t(ox+125, 155, "(4.8 kWh)  take + and − from opposite ends", 9.5, "middle")
    # 2S2P
    ox2 = 560
    b += t(ox2+105, 20, "SERIES-PARALLEL (2S2P)", 12.5, "middle", "700")
    ya, yb = 62, 128
    for yy in (ya, yb):
        b += batt(ox2+40, yy) + batt(ox2+120, yy)
        b += f'<path d="M{ox2+86},{yy-6} C{ox2+92},{yy-22} {ox2+124},{yy-22} {ox2+130},{yy-6}" fill="none" stroke="{INK}" stroke-width="{W}"/>'
    b += f'<polyline points="{ox2+50},{ya-6} {ox2+50},{ya-16} {ox2+18},{ya-16} {ox2+18},{yb-14} {ox2+50},{yb-14} {ox2+50},{yb-6}" fill="none" stroke="{RED}" stroke-width="{W}"/>'
    b += f'<polyline points="{ox2+166},{ya-6} {ox2+166},{ya-16} {ox2+196},{ya-16} {ox2+196},{yb-14} {ox2+166},{yb-14} {ox2+166},{yb-6}" fill="none" stroke="#111" stroke-width="{W}"/>'
    b += t(ox2+4, ya+70, "+", 12, "middle", "700", RED) + t(ox2+208, ya+70, "−", 12, "middle", "700")
    b += t(ox2+105, 196, "4 × 12 V 100 Ah → 24 V, 200 Ah", 11, "middle", "700", BLUE)
    b += t(ox2+105, 211, "(4.8 kWh) two 24 V strings in parallel", 9.5, "middle")
    # rules
    b += f'<rect x="20" y="228" width="740" height="64" rx="6" fill="#fff8e1" stroke="{AMBER}"/>'
    b += t(34, 248, "Rules: use identical batteries (same type, capacity, age, state of charge) in a bank. Keep parallel strings to 3 or fewer.", 10)
    b += t(34, 264, "Make all interconnect cables the same length and gauge. Fuse each parallel string. Same total energy either way:", 10)
    b += t(34, 280, "watt-hours = volts × amp-hours. Higher system voltage = lower current = thinner, cheaper, safer cables.", 10)
    return svg(780, 300, b, "Series vs parallel battery wiring")

# ---------------------------------------------------------------- 6 biodiesel flow
def biodiesel_flow():
    b = '<rect x="0" y="0" width="780" height="400" fill="#fafbfc"/>'
    bw, bh = 132, 64
    row1 = [(20, "1 Collect oil", "veg oil, fryer oil,\nrendered fat", "#fff"),
            (175, "2 Filter + dewater", "strain; heat & settle;\nwater < 0.1%", "#fff"),
            (330, "3 Titrate", "measure free fatty\nacids → lye dose", "#fff"),
            (485, "4 Heat oil", "48–55 °C (120–130 °F)\nnever above 60 °C", "#fff")]
    for x, a, s, f in row1:
        b += box(x, 30, bw, bh, a, f, INK, 11, sub=s)
    for i in range(3):
        b += arrow(row1[i][0]+bw, 62, row1[i+1][0]-2, 62)
    # methoxide
    b += box(620, 125, 145, 74, "METHOXIDE", "#ffebee", RED, 11.5, sw=2.2, sub="methanol (20% of oil vol.)\n+ NaOH or KOH, mixed\nin a closed container")
    b += t(692, 115, "⚠ toxic · caustic · flammable", 9.5, "middle", "700", RED)
    # reactor
    b += box(485, 220, bw, 70, "5 React", "#e3f2fd", BLUE, 11.5, sub="add methoxide to oil;\nmix ~1 h at 50–55 °C")
    b += arrow(551, 94, 551, 218)
    b += f'<polyline points="692,199 692,255 619,255" fill="none" stroke="{RED}" stroke-width="1.6" marker-end="url(#arr)"/>'
    # settle
    b += box(330, 220, bw, 70, "6 Settle", "#fff", INK, 11.5, sub="8–24 h; glycerin\nsinks to bottom")
    b += arrow(485, 255, 464, 255)
    b += box(330, 320, bw, 56, "Glycerin layer", "#fff3e0", AMBER, 10.5, sub="~20% of volume;\ncontains methanol + lye")
    b += arrow(396, 290, 396, 318, AMBER, 1.6)
    # wash
    b += box(175, 220, bw, 70, "7 Wash", "#fff", INK, 11.5, sub="gentle water mist/\nbubble wash ×3–4")
    b += arrow(330, 255, 309, 255)
    b += box(175, 320, bw, 56, "Wash water", "#fff3e0", AMBER, 10.5, sub="soapy, alkaline;\ndispose safely")
    b += arrow(241, 290, 241, 318, AMBER, 1.6)
    # dry
    b += box(20, 220, bw, 70, "8 Dry", "#fff", INK, 11.5, sub="heat ~50 °C open-top\nuntil crystal clear")
    b += arrow(175, 255, 154, 255)
    b += box(20, 125, bw, 64, "9 Test", "#e8f5e9", GRN, 11.5, sub="3/27 methanol test,\nwash test, clarity")
    b += arrow(86, 220, 86, 191)
    b += box(175, 125, bw, 64, "10 Filter + store", "#e8f5e9", GRN, 11, sub="≤5 µm filter; sealed,\ncool, dark, full")
    b += arrow(152, 157, 173, 157)
    b += t(20, 395, "Failed 3/27 test → re-process (second-stage reaction) rather than burning it in an engine.", 9.5, italic=True)
    b += t(330, 132, "Oil (triglyceride) + 3 methanol", 9.5, weight="600") + t(330, 145, "→ 3 biodiesel (methyl esters)", 9.5, weight="600") + t(330, 158, "  + glycerin   [lye = catalyst]", 9.5, weight="600")
    return svg(780, 400, b, "Biodiesel process flow")

# ---------------------------------------------------------------- 8 turbine selection chart
def turbine_chart():
    W, H = 780, 380
    L, R, T, B = 70, 600, 20, 330
    import math
    def X(q):  # q in L/s, log 1..2000
        return L + (math.log10(q) - 0) / (math.log10(2000)) * (R - L)
    def Y(h):  # head m, log 1..500
        return B - (math.log10(h)) / math.log10(500) * (B - T)
    b = f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fafbfc"/>'
    b += f'<defs><clipPath id="plot"><rect x="{L}" y="{T}" width="{R-L}" height="{B-T}"/></clipPath></defs>'
    b += f'<rect x="{L}" y="{T}" width="{R-L}" height="{B-T}" fill="#fff" stroke="{INK}"/>'
    for q in [1,2,5,10,20,50,100,200,500,1000,2000]:
        b += f'<line x1="{X(q):.1f}" y1="{T}" x2="{X(q):.1f}" y2="{B}" stroke="#e0e0e0"/>' + t(X(q), B+15, str(q), 9.5, "middle")
    for h in [1,2,5,10,20,50,100,200,500]:
        b += f'<line x1="{L}" y1="{Y(h):.1f}" x2="{R}" y2="{Y(h):.1f}" stroke="#e0e0e0"/>' + t(L-6, Y(h)+3, str(h), 9.5, "end")
    b += t((L+R)/2, B+34, "Design flow (litres per second)   [1 L/s ≈ 15.9 US gpm]", 10.5, "middle", "600")
    b += f'<text x="20" y="{(T+B)/2}" font-size="10.5" font-weight="600" text-anchor="middle" transform="rotate(-90 20 {(T+B)/2})">Net head (metres)   [1 m = 3.28 ft]</text>'
    zones = [("Pelton", [(1,15),(1,500),(100,500),(100,60),(25,20),(5,15)], "#1565c0"),
             ("Turgo", [(5,10),(5,150),(200,150),(200,20),(60,10)], "#6a1b9a"),
             ("Crossflow", [(20,3),(20,60),(1000,60),(1000,5),(300,3)], "#2e7d32"),
             ("Propeller / Kaplan", [(80,1.2),(80,12),(2000,15),(2000,1.2)], "#e65100"),
             ("Waterwheel", [(50,1),(50,6),(800,6),(800,1)], "#795548")]
    g = f'<g clip-path="url(#plot)">'
    for name, pts, col in zones:
        dash = ' stroke-dasharray="5,3"' if name == "Waterwheel" else ""
        g += '<polygon points="' + " ".join(f"{X(q):.1f},{Y(h):.1f}" for q,h in pts) + f'" fill="{col}" fill-opacity="0.13" stroke="{col}" stroke-width="1.6"{dash}/>'
    # power lines at 50% efficiency
    for P, lab in [(100,"100 W"),(1000,"1 kW"),(10000,"10 kW"),(100000,"100 kW")]:
        q1, q2 = 1, 2000
        h1, h2 = P/(9.81*0.5*q1/1), P/(9.81*0.5*q2/1)
        # P = 9.81 * Q(L/s) * H * 0.5  -> H = P/(4.905 Q)
        h1, h2 = P/(4.905*q1), P/(4.905*q2)
        g += f'<line x1="{X(q1):.1f}" y1="{Y(h1):.1f}" x2="{X(q2):.1f}" y2="{Y(h2):.1f}" stroke="#555" stroke-width="1" stroke-dasharray="2,3"/>'
    g += '</g>'
    b += g
    for P, lab in [(100,"100 W"),(1000,"1 kW"),(10000,"10 kW"),(100000,"100 kW")]:
        # label where line crosses head=2.5 or flow such that inside
        h = 300 if P >= 10000 else (60 if P==1000 else 12)
        q = P/(4.905*h)
        if q < 1.3: h = P/(4.905*1.6); q = 1.6
        b += t(X(q)+3, Y(h)-3, lab, 9, fill="#444", italic=True)
    b += t(X(2.2), Y(260), "PELTON", 11, weight="700", fill="#1565c0")
    b += t(X(22), Y(110), "TURGO", 11, weight="700", fill="#6a1b9a")
    b += t(X(150), Y(35), "CROSSFLOW", 11, weight="700", fill="#2e7d32")
    b += t(X(250), Y(9), "PROPELLER / KAPLAN", 11, weight="700", fill="#e65100")
    b += t(X(60), Y(1.4), "waterwheel", 10, weight="700", fill="#795548", italic=True)
    # side notes
    nx = 615
    b += t(nx, 40, "How to read", 11.5, weight="700")
    notes = ["Find your net head (up)", "and usable flow (across).", "Turbines whose zone", "contains that point are", "candidates.", "", "Dotted lines: electrical", "output at 50% overall", "water-to-wire efficiency.", "", "Zones overlap and are", "approximate; always", "check the maker's", "rated range."]
    for i, n in enumerate(notes): b += t(nx, 60+i*14, n, 10)
    return svg(W, H, b, "Turbine selection chart")

# ---------------------------------------------------------------- 9 hydro electrical systems
def hydro_systems():
    b = '<rect x="0" y="0" width="780" height="290" fill="#fafbfc"/>'
    b += t(190, 22, "A. Battery-based (most home systems)", 12, "middle", "700")
    b += box(10, 50, 100, 56, "Turbine +\nPM alternator", "#e3f2fd", BLUE, 10)
    b += box(140, 50, 92, 56, "Rectifier or", "#fff", INK, 10, sub="hydro-rated\nMPPT ctrl")
    b += box(262, 50, 100, 56, "Battery bank", "#cfd8dc", INK, 10.5, sub="12/24/48 V DC")
    b += arrow(110, 78, 138, 78) + arrow(232, 78, 260, 78)
    b += box(262, 140, 100, 50, "Diversion\ncontroller", "#e8f5e9", GRN, 10)
    b += box(262, 220, 100, 50, "Dump load", "#ffccbc", RED, 10.5, sub="water/air heater")
    b += arrow(312, 106, 312, 138) + arrow(312, 190, 312, 218)
    b += box(140, 150, 92, 50, "Inverter", "#fff", INK, 10.5, sub="→ 120/240 V AC")
    b += f'<polyline points="262,98 250,98 250,175 234,175" fill="none" stroke="{INK}" stroke-width="1.4" marker-end="url(#ar)"/>'
    b += box(10, 150, 100, 50, "House loads", "#fff", INK, 10.5)
    b += arrow(140, 175, 112, 175)
    b += t(10, 232, "Battery covers short peaks far above", 9.5) + t(10, 244, "turbine output; excess energy goes", 9.5) + t(10, 256, "to the dump load once batteries are full.", 9.5) + t(10, 268, "Works with as little as 100–300 W.", 9.5, weight="600")
    b += '<line x1="392" y1="10" x2="392" y2="280" stroke="#b0bec5" stroke-width="1.5"/>'
    ox = 410
    b += t(ox+180, 22, "B. AC-direct (larger sites, ≥ ~2–3 kW)", 12, "middle", "700")
    b += box(ox, 60, 110, 56, "Turbine +\nAC generator", "#e3f2fd", BLUE, 10, sub="60 Hz (50 Hz MX/CA*)")
    b += box(ox+140, 60, 100, 56, "ELC", "#e8f5e9", GRN, 11, sub="electronic load\ncontroller")
    b += box(ox+270, 60, 90, 56, "House loads", "#fff", INK, 10.5, sub="direct AC")
    b += arrow(ox+110, 88, ox+138, 88) + arrow(ox+240, 88, ox+268, 88)
    b += box(ox+140, 160, 100, 50, "Ballast load", "#ffccbc", RED, 10.5, sub="heaters")
    b += arrow(ox+190, 116, ox+190, 158)
    b += t(ox, 236, "ELC keeps total load constant: as house loads turn", 9.5) + t(ox, 248, "off it diverts the same power to the ballast, holding", 9.5) + t(ox, 260, "speed, voltage and frequency steady. Turbine must", 9.5) + t(ox, 272, "cover the biggest peak, including motor starting.", 9.5, weight="600")
    return svg(780, 290, b, "Hydro electrical systems")

# ---------------------------------------------------------------- 10 rocket stove
def rocket_stove():
    b = '<rect x="0" y="0" width="520" height="330" fill="#fafbfc"/>'
    # outer can
    b += f'<rect x="150" y="80" width="210" height="220" fill="url(#ins)" stroke="{INK}" stroke-width="2"/>'
    # inner L-shaped tube: horizontal feed from left x=60..230, y 230-280 ; vertical riser x=230..280 up to y=80
    b += f'<path d="M60,230 L230,230 L230,80 L280,80 L280,280 L60,280 Z" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    # shelf
    b += f'<line x1="60" y1="262" x2="200" y2="262" stroke="#555" stroke-width="3"/>'
    # sticks
    for i, y in enumerate([244, 251, 256]):
        b += f'<rect x="{30+i*6}" y="{y-3}" width="190" height="6" rx="3" fill="#8d6e63" stroke="#4e342e" stroke-width="0.7"/>'
    # flame
    b += f'<path d="M200,256 C215,230 240,236 245,200 C252,170 240,140 255,110 C262,140 270,170 262,200 C258,230 262,240 252,262 Z" fill="#ff9800" opacity="0.8"/>'
    b += f'<path d="M226,252 C238,232 250,220 252,190 C258,215 254,236 244,258 Z" fill="#ffeb3b" opacity="0.9"/>'
    # air arrow under shelf
    b += arrow(70, 272, 190, 272, BLUE, 1.6, "arb")
    b += t(20, 318, "Air enters under the shelf", 9.5, fill=BLUE, weight="600")
    # pot supports and pot
    b += f'<rect x="215" y="66" width="8" height="14" fill="#333"/><rect x="287" y="66" width="8" height="14" fill="#333"/>'
    b += f'<path d="M190,66 L320,66 L310,22 L200,22 Z" fill="#455a64" stroke="{INK}"/>'
    b += f'<path d="M180,90 L180,30 M330,90 L330,30" stroke="#8d99a3" stroke-width="3"/>'
    # hot gas arrows
    b += f'<path d="M255,76 C250,60 220,62 200,50" fill="none" stroke="{RED}" stroke-width="1.4" marker-end="url(#arr)"/>'
    b += f'<path d="M255,76 C262,60 292,62 312,50" fill="none" stroke="{RED}" stroke-width="1.4" marker-end="url(#arr)"/>'
    # labels
    b += t(370, 40, "Pot sits on supports with a", 9.5) + t(370, 52, "small gap (~1–2 cm)", 9.5)
    b += t(370, 74, "Pot skirt forces hot gas", 9.5) + t(370, 86, "along the pot sides", 9.5) + lead(368, 82, 331, 70)
    b += t(370, 130, "Insulated riser (chimney)", 10, weight="700") + t(370, 142, "≈ 2–3× as tall as feed is long", 9.5) + lead(368, 134, 280, 140)
    b += t(370, 180, "Insulation: wood ash,", 9.5) + t(370, 192, "perlite, vermiculite —", 9.5) + t(370, 204, "never plain concrete", 9.5) + lead(368, 188, 330, 200)
    b += t(10, 200, "Fuel magazine:", 10, weight="700") + t(10, 212, "push sticks in", 9.5) + t(10, 224, "as they burn", 9.5)
    b += t(10, 342, "Outdoor use or under a well-ventilated roof only — burning wood makes carbon monoxide.", 9.5, italic=True, fill=RED)
    return svg(520, 330, b, "Rocket stove cross section")

# ---------------------------------------------------------------- 7 map
def albers(lon, lat, lon0=-100, lat0=40, p1=20, p2=60):
    r = math.radians
    n = (math.sin(r(p1)) + math.sin(r(p2)))/2
    C = math.cos(r(p1))**2 + 2*n*math.sin(r(p1))
    rho0 = math.sqrt(C - 2*n*math.sin(r(lat0)))/n
    rho = math.sqrt(C - 2*n*math.sin(r(lat)))/n
    th = n*r(lon - lon0)
    return rho*math.sin(th), rho0 - rho*math.cos(th)

def clip(poly, test, inter):
    out = []
    for i in range(len(poly)):
        a, b2 = poly[i-1], poly[i]
        ia, ib = test(a), test(b2)
        if ib:
            if not ia: out.append(inter(a, b2))
            out.append(b2)
        elif ia:
            out.append(inter(a, b2))
    return out

def clip_lat(poly, lat, keep_above):
    test = (lambda p: p[1] >= lat) if keep_above else (lambda p: p[1] < lat)
    def inter(a, b2):
        f = (lat - a[1])/(b2[1]-a[1]); return (a[0]+f*(b2[0]-a[0]), lat)
    return clip(poly, test, inter)

def clip_lon(poly, lon, keep_east):
    test = (lambda p: p[0] >= lon) if keep_east else (lambda p: p[0] < lon)
    def inter(a, b2):
        f = (lon - a[0])/(b2[0]-a[0]); return (lon, a[1]+f*(b2[1]-a[1]))
    return clip(poly, test, inter)

REGIONS = {
 1: ("Arctic & Subarctic", "#b3e5fc"), 2: ("Pacific NW & BC", "#4db6ac"), 3: ("Prairies & Great Plains", "#ffe082"),
 4: ("Great Lakes & Midwest", "#aed581"), 5: ("Northeast & Atlantic Canada", "#81c784"), 6: ("Southeast & Gulf", "#ffab91"),
 7: ("Florida", "#f48fb1"), 8: ("Desert SW & Great Basin", "#ffcc80"), 9: ("Rocky Mountains", "#bcaaa4"),
 10: ("California", "#ce93d8"), 11: ("Northern Mexico", "#e6c07a"), 12: ("Central & Southern Mexico", "#c5e1a5"),
 13: ("Central America & Caribbean", "#80deea")}

US = {1:["Alaska"],2:["Washington","Oregon"],3:["North Dakota","South Dakota","Nebraska","Kansas","Oklahoma"],
      4:["Minnesota","Wisconsin","Michigan","Iowa","Illinois","Indiana","Ohio","Missouri"],
      5:["Maine","New Hampshire","Vermont","Massachusetts","Rhode Island","Connecticut","New York","New Jersey","Pennsylvania","Delaware","Maryland","District of Columbia"],
      6:["Virginia","West Virginia","Kentucky","Tennessee","North Carolina","South Carolina","Georgia","Alabama","Mississippi","Louisiana","Arkansas"],
      7:["Florida"],8:["Nevada","Utah","Arizona","New Mexico"],9:["Montana","Idaho","Wyoming","Colorado"],10:["California"]}
CA = {1:["Yukon","Northwest Territories","Nunavut"],2:["British Columbia"],5:["New Brunswick","Nova Scotia","Prince Edward Island"]}
CA_SPLIT = {"Alberta":3,"Saskatchewan":3,"Manitoba":3,"Ontario":4,"Québec":5,"Newfoundland and Labrador":5}
CAM = ["GTM","BLZ","SLV","HND","NIC","CRI","PAN","CUB","JAM","HTI","DOM","PRI","BHS","TTO","VIR","VGB","AIA","KNA","ATG","MSR","DMA","LCA","VCT","GRD","BRB","CYM","TCA","ABW","CUW","MAF","SXM","BLM"]

def rings(geom):
    if geom["type"] == "Polygon": return [geom["coordinates"][0]]
    return [p[0] for p in geom["coordinates"]]

def region_map():
    import os
    d = os.path.dirname(os.path.abspath(__file__))
    S = json.load(open(os.path.join(d, "states.geojson")))
    K = json.load(open(os.path.join(d, "countries.geojson")))
    shapes = []  # (region, ring lonlat)
    def fix(ring):
        return [((lo-360) if lo > 0 else lo, la) for lo, la in ring]
    for f in S["features"]:
        p = f["properties"]; nm = p["name"]; a3 = p["adm0_a3"]
        if a3 == "USA":
            if nm == "Hawaii": continue
            for rg, names in US.items():
                if nm in names:
                    for r_ in rings(f["geometry"]): shapes.append((rg, fix(r_)))
            if nm == "Texas":
                for r_ in rings(f["geometry"]):
                    r_ = fix(r_)
                    shapes.append((3, clip_lon(r_, -97.5, False))); shapes.append((6, clip_lon(r_, -97.5, True)))
        elif a3 == "CAN":
            for rg, names in CA.items():
                if nm in names:
                    for r_ in rings(f["geometry"]): shapes.append((rg, fix(r_)))
            if nm in CA_SPLIT:
                for r_ in rings(f["geometry"]):
                    r_ = fix(r_)
                    shapes.append((1, clip_lat(r_, 55.5, True))); shapes.append((CA_SPLIT[nm], clip_lat(r_, 55.5, False)))
    for f in K["features"]:
        a3 = f["properties"]["ADM0_A3"]
        if a3 == "MEX":
            for r_ in rings(f["geometry"]):
                shapes.append((11, clip_lat(r_, 23.0, True))); shapes.append((12, clip_lat(r_, 23.0, False)))
        elif a3 in CAM:
            for r_ in rings(f["geometry"]): shapes.append((13, r_))
        elif a3 == "GRL":
            for r_ in rings(f["geometry"]): shapes.append((1, r_))
        elif a3 in ("COL","VEN","ECU","RUS","SPM","BMU"):
            for r_ in rings(f["geometry"]): shapes.append((0, fix(r_)))
    proj = []
    for rg, ring in shapes:
        if len(ring) < 3: continue
        proj.append((rg, [albers(lo, la) for lo, la in ring]))
    # view window in projected coords
    xs = [albers(-168, 60)[0], albers(-52, 50)[0]]
    x0, x1 = albers(-170, 55)[0]-0.02, albers(-52, 47)[0]
    y0, y1 = albers(-100, 4.0)[1], albers(-100, 75)[1]
    W, H = 780, 640
    sc = min(W/(x1-x0), H/(y1-y0))
    def P(x, y): return ((x-x0)*sc, H-(y-y0)*sc)
    body = f'<rect width="{W}" height="{H}" fill="#e8f1f8"/><g stroke="#ffffff" stroke-width="0.6" stroke-linejoin="round">'
    for rg, pts in proj:
        col = REGIONS[rg][1] if rg else "#d6d6d6"
        body += '<path d="M' + " L".join(f"{P(x,y)[0]:.1f},{P(x,y)[1]:.1f}" for x,y in pts) + f'Z" fill="{col}"/>'
    body += '</g>'
    labels = {1:(-125,64),2:(-123.5,49.5),3:(-102,46),4:(-89,43),5:(-71,46),6:(-86,34),7:(-81.6,28),8:(-113,36),9:(-108,43),10:(-120,37.5),11:(-106,28),12:(-99,19),13:(-82,14.5)}
    for k, (lo, la) in labels.items():
        x, y = P(*albers(lo, la))
        body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="#fff" stroke="{INK}" stroke-width="1.3"/>' + t(x, y+4, str(k), 11, "middle", "700")
    body += t(10, H-10, "Boundaries simplified along state/province lines (Texas split at ~97.5°W; Canada & Mexico split by latitude). Albers equal-area projection.", 9, italic=True)
    return svg(W, H, body, "Region map of North America")

# ======================= revised versions (override earlier defs) =======================
def hydro_layout():
    b = '<rect x="0" y="0" width="780" height="400" fill="#f4f9fd"/>'
    gpts = [(0,80),(170,80),(260,130),(380,200),(500,290),(780,300)]
    poly = " ".join(f"{x},{y}" for x,y in gpts) + " 780,400 0,400"
    b += f'<polygon points="{poly}" fill="{GROUND}" stroke="{GSTROKE}" stroke-width="1.5"/>'
    b += f'<rect x="0" y="66" width="128" height="14" fill="{BLUE}" opacity="0.75"/>'
    b += t(10, 60, "Stream", 11, weight="600", fill=BLUE)
    b += f'<path d="M140,84 C200,100 230,140 300,165 S420,250 470,300 L780,312" fill="none" stroke="{BLUE}" stroke-width="3" opacity="0.45"/>'
    b += f'<rect x="128" y="58" width="9" height="24" fill="#9aa5ad" stroke="{INK}"/>'
    b += f'<rect x="146" y="50" width="36" height="32" fill="#fff" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<rect x="147" y="60" width="34" height="21" fill="{BLUE}" opacity="0.55"/>'
    b += '<line x1="152" y1="52" x2="152" y2="81" stroke="#333" stroke-width="1.2" stroke-dasharray="2,2"/>'
    b += f'<path d="M137,66 L146,66" stroke="{BLUE}" stroke-width="5"/>'
    pen = [(180,78),(262,124),(382,194),(486,272),(506,282)]
    b += '<polyline points="' + " ".join(f"{x},{y}" for x,y in pen) + '" fill="none" stroke="#3b4752" stroke-width="7" stroke-linejoin="round"/>'
    b += '<polyline points="' + " ".join(f"{x},{y}" for x,y in pen) + '" fill="none" stroke="#7f8f9b" stroke-width="3" stroke-linejoin="round"/>'
    b += '<circle cx="486" cy="272" r="5" fill="#fff" stroke="#000"/>'
    b += f'<rect x="500" y="250" width="66" height="44" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<polygon points="494,250 533,226 572,250" fill="#b85c38" stroke="{INK}"/>'
    b += f'<circle cx="520" cy="278" r="11" fill="#cfd8dc" stroke="{INK}"/>'
    b += f'<rect x="537" y="270" width="20" height="16" fill="{AMBER}" stroke="{INK}"/>' + t(547, 282, "G", 9, "middle", "700")
    b += f'<path d="M520,294 C530,308 560,312 600,310" fill="none" stroke="{BLUE}" stroke-width="4"/>'
    b += f'<path d="M566,262 L650,262 L650,300 L700,300 L700,290" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="6,3"/>'
    b += f'<rect x="680" y="226" width="90" height="70" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<polygon points="672,226 725,190 778,226" fill="#6d4c41" stroke="{INK}"/>'
    b += f'<rect x="688" y="262" width="22" height="24" fill="#90a4ae" stroke="{INK}"/>' + t(699, 278, "BAT", 7, "middle", "700", "#fff")
    b += f'<rect x="716" y="236" width="20" height="16" fill="#fff" stroke="{INK}"/>' + t(726,247,"C",8,"middle","700")
    b += f'<rect x="742" y="236" width="20" height="16" fill="#fff" stroke="{INK}"/>' + t(752,247,"INV",6,"middle","700")
    b += f'<rect x="742" y="266" width="20" height="20" fill="#ffccbc" stroke="{INK}"/>' + t(752,279,"DL",7,"middle","700")
    b += t(725, 216, "7 House", 10, "middle", "700", "#fff")
    # gross head dimension at x=600
    b += '<line x1="182" y1="60" x2="610" y2="60" stroke="#555" stroke-dasharray="4,3" stroke-width="0.9"/>'
    b += '<line x1="530" y1="278" x2="610" y2="278" stroke="#555" stroke-dasharray="4,3" stroke-width="0.9"/>'
    b += f'<line x1="600" y1="62" x2="600" y2="276" stroke="{INK}" stroke-width="1.4" marker-start="url(#ar)" marker-end="url(#ar)"/>'
    b += t(612, 110, "GROSS HEAD", 11, weight="700") + t(612, 124, "vertical drop from the", 9.5) + t(612, 136, "forebay water surface", 9.5) + t(612, 148, "down to the turbine nozzle", 9.5)
    b += t(40, 128, "1  Intake weir + screen", 10.5, weight="600") + lead(100, 132, 132, 80)
    b += t(40, 141, "   diverts only part of the flow", 9.5)
    b += t(190, 26, "2  Forebay / settling tank", 10.5, weight="600") + lead(200, 30, 172, 52)
    b += t(190, 39, "   keeps pipe inlet submerged, drops silt", 9.5)
    b += t(330, 140, "3  Penstock (pressure pipe)", 10.5, weight="600") + lead(330, 144, 318, 160)
    b += t(330, 153, "   buried for UV + frost protection;", 9.5) + t(330, 165, "   avoid humps (air traps)", 9.5)
    b += t(444, 212, "Shut-off valve (close slowly)", 9.5) + lead(462, 216, 483, 267)
    b += t(300, 336, "4  Powerhouse: turbine + generator (G)", 10.5, weight="600") + lead(420, 328, 515, 292)
    b += t(300, 352, "5  Tailrace returns ALL water to the stream", 10.5, weight="600") + lead(520, 344, 585, 311)
    b += t(300, 368, "6  Transmission cable (buried, in conduit)", 10.5, weight="600") + lead(520, 360, 650, 300)
    b += t(600, 336, "C = controller", 9) + t(600, 348, "INV = inverter", 9) + t(690, 336, "BAT = batteries", 9) + t(690, 348, "DL = dump load", 9)
    b += t(10, 392, "Net head = gross head − pipe friction losses (design for ≤10% loss).  Not to scale.", 9.5, italic=True)
    return svg(780, 400, b, "Micro-hydro system layout")

_old_pelton = pelton
def pelton():
    s = _old_pelton()
    return s

def pelton():
    cx, cy, R = 220, 175, 105
    b = '<rect x="0" y="0" width="760" height="360" fill="#fafbfc"/>'
    b += f'<path d="M{cx-150},{cy+150} L{cx-150},{cy-60} A150,150 0 0 1 {cx+150},{cy-60} L{cx+150},{cy+150}" fill="none" stroke="#8d99a3" stroke-width="2" stroke-dasharray="7,4"/>'
    b += t(cx+118, cy-118, "Housing", 10, fill="#5b6770")
    b += f'<circle cx="{cx}" cy="{cy}" r="{R-20}" fill="#e3e8ec" stroke="{INK}" stroke-width="1.3"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="16" fill="#9fb0bc" stroke="{INK}"/><circle cx="{cx}" cy="{cy}" r="6" fill="{INK}"/>'
    N = 18
    for i in range(N):
        th = 2*math.pi*i/N + math.pi/2
        px, py = cx + R*math.cos(th), cy + R*math.sin(th)
        ux, uy = math.sin(th), -math.cos(th)
        nx, ny = math.cos(th), math.sin(th)
        def P(u, n): return f"{px+u*ux+n*nx:.1f},{py+u*uy+n*ny:.1f}"
        # arm from disc to cup
        b += f'<path d="M{P(-3,-22)} L{P(5,-22)} L{P(5,-10)} L{P(-3,-10)} Z" fill="#78909c" stroke="{INK}" stroke-width="0.7"/>'
        # cup: semicircle bulging toward +u (rotation direction), open face toward -u (facing the oncoming jet)
        r1, r2 = 15, 10.5
        b += f'<path d="M{P(-4,r1)} A{r1},{r1} 0 0 0 {P(-4,-r1)} Z" fill="#78909c" stroke="{INK}" stroke-width="1"/>'.replace("A15,15 0 0 0", "A15,15 0 0 1") if False else ""
        pts_o = " ".join(P(-4 + r1*math.sin(a), r1*math.cos(a)) for a in [k*math.pi/12 for k in range(13)])
        pts_i = " ".join(P(-4 + r2*math.sin(a), r2*math.cos(a)) for a in [k*math.pi/12 for k in range(12, -1, -1)])
        b += f'<polygon points="{pts_o} {pts_i}" fill="#607d8b" stroke="{INK}" stroke-width="0.9"/>'
        b += f'<polygon points="{pts_i}" fill="#cfd8dc" stroke="none"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{RED}" stroke-width="0.9" stroke-dasharray="5,4"/>'
    jy = cy + R
    b += f'<rect x="0" y="{jy-14}" width="70" height="28" fill="#5d6d78" stroke="{INK}"/>'
    b += f'<polygon points="70,{jy-14} 112,{jy-5} 112,{jy+5} 70,{jy+14}" fill="#5d6d78" stroke="{INK}"/>'
    b += f'<polygon points="30,{jy-4} 100,{jy-1.5} 100,{jy+1.5} 30,{jy+4}" fill="#cfd8dc" stroke="{INK}" stroke-width="0.7"/>'
    b += f'<rect x="112" y="{jy-4}" width="{cx-112-6}" height="8" fill="{BLUE}" opacity="0.85"/>'
    b += arrow(cx-80, jy+26, cx-30, jy+26, BLUE, 1.6, "arb")
    b += t(cx-90, jy+42, "Jet  v ≈ 0.97·√(2gH)", 10, fill=BLUE, weight="600")
    b += f'<path d="M{cx+5},{jy+16} q8,20 2,40 M{cx+18},{jy+14} q14,20 12,40" stroke="{BLUE}" fill="none" stroke-width="1.5" stroke-dasharray="3,3"/>'
    b += f'<path d="M{cx+40},{cy-40} A56,56 0 0 0 {cx-40},{cy-40}" fill="none" stroke="{INK}" stroke-width="1.6" marker-end="url(#ar)"/>'
    b += t(cx, cy-62, "rotation", 10, "middle", italic=True)
    b += t(4, jy-44, "Nozzle + spear valve", 10.5, weight="600") + t(4, jy-30, "(spear adjusts flow)", 9.5)
    b += t(cx+128, cy+44, "Pitch circle — jet", 10, fill=RED) + t(cx+128, cy+58, "is tangent to it", 10, fill=RED)
    b += lead(cx+126, cy+46, cx+R*math.cos(0.42), cy+R*math.sin(0.42), RED)
    b += t(4, 22, "Runner: disc + cups", 10.5, weight="600") + t(4, 36, "(cups open toward", 9.5) + t(4, 50, "the oncoming jet)", 9.5)
    b += t(cx-20, 352, "Water drops freely into the tailrace — runner must sit ABOVE tailwater", 9.5, "middle", italic=True)
    ox, oy = 470, 40
    b += f'<rect x="{ox}" y="{oy}" width="280" height="290" rx="8" fill="#fff" stroke="#b0bec5"/>'
    b += t(ox+140, oy+20, "One bucket, seen from the jet", 11.5, "middle", "700")
    bx, by = ox+140, oy+140
    b += f'<path d="M{bx},{by-70} C{bx-30},{by-72} {bx-75},{by-50} {bx-80},{by} C{bx-75},{by+55} {bx-30},{by+72} {bx},{by+70} C{bx+30},{by+72} {bx+75},{by+55} {bx+80},{by} C{bx+75},{by-50} {bx+30},{by-72} {bx},{by-70} Z" fill="#cfd8dc" stroke="{INK}" stroke-width="1.4"/>'
    b += f'<ellipse cx="{bx-38}" cy="{by}" rx="32" ry="55" fill="#a7b6bf" stroke="#546e7a"/><ellipse cx="{bx+38}" cy="{by}" rx="32" ry="55" fill="#a7b6bf" stroke="#546e7a"/>'
    b += f'<line x1="{bx}" y1="{by-66}" x2="{bx}" y2="{by+66}" stroke="{INK}" stroke-width="2.2"/>'
    b += f'<path d="M{bx-14},{by-70} L{bx},{by-56} L{bx+14},{by-70}" fill="#fff" stroke="{INK}"/>'
    b += f'<circle cx="{bx}" cy="{by}" r="9" fill="{BLUE}" opacity="0.85"/>'
    b += f'<path d="M{bx-6},{by+4} C{bx-40},{by+40} {bx-80},{by+30} {bx-96},{by-6}" fill="none" stroke="{BLUE}" stroke-width="2" marker-end="url(#arb)"/>'
    b += f'<path d="M{bx+6},{by+4} C{bx+40},{by+40} {bx+80},{by+30} {bx+96},{by-6}" fill="none" stroke="{BLUE}" stroke-width="2" marker-end="url(#arb)"/>'
    b += t(bx, oy+234, "Splitter ridge divides the jet; each half", 9.5, "middle")
    b += t(bx, oy+248, "turns ~165° and leaves sideways/backward,", 9.5, "middle")
    b += t(bx, oy+262, "giving up most of its energy.", 9.5, "middle")
    b += t(bx, oy+280, "Notch (top) lets the jet reach the next bucket.", 9.5, "middle", italic=True)
    b += t(bx+18, oy+46, "notch", 9, fill="#444")
    b += t(bx-12, by+22, "jet", 9, "end", fill=BLUE, weight="600")
    return svg(760, 360, b, "Pelton wheel")

def solar_wiring():
    b = '<rect x="0" y="0" width="780" height="340" fill="#fafbfc"/>'
    b += f'<rect x="20" y="30" width="120" height="76" fill="#1a3a5c" stroke="{INK}" stroke-width="1.5"/>'
    for i in range(1,6): b += f'<line x1="{20+i*20}" y1="30" x2="{20+i*20}" y2="106" stroke="#6d8fb3" stroke-width="0.7"/>'
    for j in range(1,4): b += f'<line x1="20" y1="{30+j*19}" x2="140" y2="{30+j*19}" stroke="#6d8fb3" stroke-width="0.7"/>'
    b += t(80, 22, "Solar panel(s)", 11, "middle", "700")
    def fuse(x, y, lab, vert=False):
        if vert:
            return f'<rect x="{x-6}" y="{y-13}" width="12" height="26" rx="3" fill="#fff3e0" stroke="{AMBER}" stroke-width="1.6"/><line x1="{x}" y1="{y-13}" x2="{x}" y2="{y+13}" stroke="{AMBER}"/>' + t(x+10, y+4, lab, 9, fill="#8a5a00", weight="600")
        return f'<rect x="{x-13}" y="{y-6}" width="26" height="12" rx="3" fill="#fff3e0" stroke="{AMBER}" stroke-width="1.6"/><line x1="{x-13}" y1="{y}" x2="{x+13}" y2="{y}" stroke="{AMBER}"/>' + t(x, y-10, lab, 9, "middle", fill="#8a5a00", weight="600")
    R_, K_ = RED, "#111"
    def wire(pts, col, w=2.5): return '<polyline points="' + " ".join(f"{x},{y}" for x,y in pts) + f'" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/>'
    # PV to controller
    b += wire([(120,106),(120,140),(240,140)], R_) + fuse(180, 140, "PV breaker")
    b += wire([(40,106),(40,172),(240,172)], K_)
    b += box(240, 118, 110, 72, "Charge\ncontroller", "#e8f5e9", GRN, 11, sub="MPPT or PWM")
    # battery
    bx, by = 430, 205
    b += f'<rect x="{bx}" y="{by}" width="130" height="66" rx="4" fill="#90a4ae" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<rect x="{bx+8}" y="{by-8}" width="18" height="8" fill="#111"/><rect x="{bx+102}" y="{by-8}" width="18" height="8" fill="{RED}"/>'
    b += t(bx+65, by+32, "Battery bank", 11.5, "middle", "700", "#fff") + t(bx+65, by+47, "12 / 24 / 48 V", 9.5, "middle", fill="#fff")
    b += t(bx+3, by-12, "−", 13, "middle", "700") + t(bx+126, by-12, "+", 13, "middle", "700", RED)
    # controller -> battery
    b += wire([(350,140),(536,140),(536,by-8)], R_) + fuse(395, 140, "Fuse")
    b += wire([(350,172),(444,172),(444,by-8)], K_)
    # battery -> inverter
    b += wire([(548,by-8),(548,160),(608,160),(608,195),(630,195)], R_, 3.5) + fuse(578, 160, "Main fuse")
    b += wire([(434,by-8),(434,190),(415,190),(415,292),(618,292),(618,235),(630,235)], K_, 3.5)
    b += box(630, 175, 125, 76, "Inverter", "#e3f2fd", BLUE, 11.5, sub="DC → 120/240 V AC")
    b += box(670, 40, 96, 56, "AC loads", "#fff", INK, 10.5, sub="via AC breaker")
    b += f'<line x1="700" y1="175" x2="700" y2="98" stroke="{INK}" stroke-width="2" marker-end="url(#ar)"/>'
    b += box(245, 30, 100, 50, "DC loads", "#fff", INK, 10.5, sub="lights, radio")
    b += f'<line x1="295" y1="118" x2="295" y2="80" stroke="{RED}" stroke-width="2"/>' + fuse(295, 99, "Fuse", vert=True)
    # ground
    G = f'stroke="{GRN}" stroke-width="1.8" stroke-dasharray="5,3" fill="none"'
    b += f'<polyline points="80,106 80,318 680,318 680,251" {G}/><line x1="295" y1="190" x2="295" y2="318" {G.replace(" fill=\"none\"","")}/>'
    b += f'<line x1="148" y1="318" x2="148" y2="306" stroke="{GRN}" stroke-width="2"/>'
    b += f'<line x1="136" y1="306" x2="160" y2="306" stroke="{GRN}" stroke-width="2"/><line x1="140" y1="300" x2="156" y2="300" stroke="{GRN}" stroke-width="2"/><line x1="144" y1="294" x2="152" y2="294" stroke="{GRN}" stroke-width="2"/>'
    b += t(170, 333, "Equipment ground (green, dashed): panel frames, controller & inverter chassis → ground rod", 9.5, fill=GRN, weight="600")
    b += f'<line x1="100" y1="236" x2="125" y2="236" stroke="{RED}" stroke-width="3"/>' + t(130, 240, "Positive (+)", 9.5)
    b += f'<line x1="100" y1="254" x2="125" y2="254" stroke="#111" stroke-width="3"/>' + t(130, 258, "Negative (−)", 9.5)
    b += f'<rect x="96" y="268" width="14" height="10" rx="2" fill="#fff3e0" stroke="{AMBER}" stroke-width="1.5"/>' + t(130, 277, "Fuse / breaker", 9.5)
    b += t(100, 204, "Connect battery to controller", 9.5, weight="700", fill=RED) + t(100, 218, "BEFORE connecting the panels.", 9.5, weight="700", fill=RED)
    b += t(452, 128, "Main fuse: as close to battery + as possible", 8.5, fill="#8a5a00") if False else ""
    return svg(780, 340, b, "Solar battery inverter wiring")

def series_parallel():
    b = '<rect x="0" y="0" width="780" height="310" fill="#fafbfc"/>'
    W = 2.4; y = 88
    b += t(125, 18, "SERIES: voltage adds", 12.5, "middle", "700")
    xs = [20, 82, 144, 206]
    for x in xs: b += batt(x, y)
    for i in range(3):
        b += f'<path d="M{xs[i]+46},{y-6} C{xs[i]+50},{y-26} {xs[i+1]+6},{y-26} {xs[i+1]+10},{y-6}" fill="none" stroke="{INK}" stroke-width="{W}"/>'
    b += f'<polyline points="{xs[0]+10},{y-6} {xs[0]+10},{y-40} 40,{y-40}" fill="none" stroke="{RED}" stroke-width="{W}"/>'
    b += f'<polyline points="{xs[3]+46},{y-6} {xs[3]+46},{y-40} 230,{y-40}" fill="none" stroke="#111" stroke-width="{W}"/>'
    b += t(26, y-46, "+ out", 9.5, fill=RED, weight="600") + t(212, y-46, "− out", 9.5, weight="600")
    b += t(125, 156, "4 × 12 V 100 Ah  →  48 V, 100 Ah", 11, "middle", "700", BLUE)
    b += t(125, 171, "(4.8 kWh)  + of one to − of the next", 9.5, "middle")
    ox = 275
    b += t(ox+125, 18, "PARALLEL: amp-hours add", 12.5, "middle", "700")
    for x in [ox+20, ox+82, ox+144, ox+206]: b += batt(x, y)
    b += f'<line x1="{ox+30}" y1="{y-22}" x2="{ox+216}" y2="{y-22}" stroke="{RED}" stroke-width="{W}"/>'
    for x in [ox+20, ox+82, ox+144, ox+206]:
        b += f'<line x1="{x+10}" y1="{y-6}" x2="{x+10}" y2="{y-22}" stroke="{RED}" stroke-width="{W}"/>'
        b += f'<line x1="{x+46}" y1="{y-6}" x2="{x+46}" y2="{y-34}" stroke="#111" stroke-width="{W}"/>'
    b += f'<line x1="{ox+66}" y1="{y-34}" x2="{ox+252}" y2="{y-34}" stroke="#111" stroke-width="{W}"/>'
    b += f'<line x1="{ox+30}" y1="{y-22}" x2="{ox+30}" y2="{y-50}" stroke="{RED}" stroke-width="{W}"/>'
    b += f'<line x1="{ox+252}" y1="{y-34}" x2="{ox+252}" y2="{y-50}" stroke="#111" stroke-width="{W}"/>'
    b += t(ox+36, y-50, "+ out (first)", 9, fill=RED, weight="600") + t(ox+246, y-50, "− out (last)", 9, "end", weight="600")
    b += t(ox+125, 156, "4 × 12 V 100 Ah  →  12 V, 400 Ah", 11, "middle", "700", BLUE)
    b += t(ox+125, 171, "(4.8 kWh)  take + and − from opposite ends", 9.5, "middle")
    ox2 = 560
    b += t(ox2+105, 18, "SERIES-PARALLEL (2S2P)", 12.5, "middle", "700")
    ya, yb = 62, 128
    for yy in (ya, yb):
        b += batt(ox2+40, yy) + batt(ox2+120, yy)
        b += f'<path d="M{ox2+86},{yy-6} C{ox2+92},{yy-22} {ox2+124},{yy-22} {ox2+130},{yy-6}" fill="none" stroke="{INK}" stroke-width="{W}"/>'
    b += f'<polyline points="{ox2+50},{ya-6} {ox2+50},{ya-16} {ox2+18},{ya-16} {ox2+18},{yb-14} {ox2+50},{yb-14} {ox2+50},{yb-6}" fill="none" stroke="{RED}" stroke-width="{W}"/>'
    b += f'<polyline points="{ox2+166},{ya-6} {ox2+166},{ya-16} {ox2+196},{ya-16} {ox2+196},{yb-14} {ox2+166},{yb-14} {ox2+166},{yb-6}" fill="none" stroke="#111" stroke-width="{W}"/>'
    b += t(ox2+8, ya+70, "+", 13, "middle", "700", RED) + t(ox2+206, ya+70, "−", 13, "middle", "700")
    b += t(ox2+105, 196, "4 × 12 V 100 Ah → 24 V, 200 Ah", 11, "middle", "700", BLUE)
    b += t(ox2+105, 211, "(4.8 kWh) two 24 V strings in parallel", 9.5, "middle")
    b += f'<rect x="20" y="232" width="740" height="66" rx="6" fill="#fff8e1" stroke="{AMBER}"/>'
    b += t(34, 252, "Rules: use identical batteries (same type, capacity, age, state of charge) in a bank. Keep parallel strings to 3 or fewer.", 10)
    b += t(34, 268, "Make all interconnect cables the same length and gauge. Fuse each parallel string. Same total energy either way:", 10)
    b += t(34, 284, "watt-hours = volts × amp-hours. Higher system voltage = lower current = thinner, cheaper, safer cables.", 10)
    return svg(780, 310, b, "Series vs parallel battery wiring")

_old_rocket = rocket_stove
def rocket_stove():
    s = _old_rocket()
    s = s.replace('viewBox="0 0 520 330"', 'viewBox="0 0 520 350"').replace('height="330" fill="#fafbfc"', 'height="350" fill="#fafbfc"')
    return s

_old_chart = turbine_chart
def turbine_chart():
    s = _old_chart()
    return s
