import sys, math, json, os
sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
P = json.load(open('photos.json'))
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

EXTRA_CSS = """<style>
.ph{border:1px solid #c9d4da;border-radius:7px;overflow:hidden;margin:6px 0;background:#fff;break-inside:avoid}
.ph img{width:100%;display:block}
.ph .cap{padding:6px 9px;font-size:10.5pt}
.ph .cap .nm{font-weight:700}.ph .cap .sci{font-style:italic;color:#466}
.ph .cap .cr{font-size:8.5pt;color:#678;margin-top:3px}
.ph .badge{display:inline-block;font-size:8.5pt;font-weight:700;color:#fff;background:#2e7d32;border-radius:4px;padding:1px 6px;margin-right:5px;vertical-align:1px}
.ph.bad .badge{background:#b71c1c}
.phgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.tierA{border-left:6px solid #1565c0;background:#eaf2fb;padding:2px 12px;border-radius:5px;margin:8px 0}
.tierB{border-left:6px solid #6a1b9a;background:#f3eafb;padding:2px 12px;border-radius:5px;margin:8px 0}
.tierA>h3,.tierB>h3{margin:9px 0 4px}
.tag{display:inline-block;font-size:9pt;font-weight:700;border-radius:4px;padding:1px 7px;color:#fff}
.tag.a{background:#1565c0}.tag.b{background:#6a1b9a}
</style>"""

def photo(k, name, idtext, bad=False, badge=None):
    p = P[k]; cls = "ph bad" if bad else "ph"
    b = badge or ("CAUTION" if bad else "ID PHOTO")
    art = p['artist'] or 'Wikimedia Commons'
    return (f'<div class="{cls}"><img src="{p["path"]}">'
            f'<div class="cap"><span class="badge">{b}</span> <span class="nm">{name}</span> <span class="sci">{p["sci"]}</span><br>{idtext}'
            f'<div class="cr">Photo: {art} · {p["license"]} · Wikimedia Commons</div></div></div>')

def tierA(h, body): return f'<div class="tierA"><h3><span class="tag a">TIER A</span> {h}</h3>{body}</div>'
def tierB(h, body): return f'<div class="tierB"><h3><span class="tag b">TIER B</span> {h}</h3>{body}</div>'

# ---------------- cover ----------------
def cover_art():
    s = '<rect width="720" height="380" fill="#e8f0f2"/>'
    # mortar & pestle
    s += '<ellipse cx="150" cy="300" rx="90" ry="26" fill="#90a4ae"/><path d="M70 230 Q150 360 230 230 Z" fill="#b0bec5" stroke="#546e7a" stroke-width="3"/>'
    s += '<rect x="150" y="150" width="18" height="110" rx="8" fill="#8d6e63" transform="rotate(20 159 205)"/><circle cx="195" cy="165" r="16" fill="#8d6e63"/>'
    # flask with green culture
    s += '<polygon points="430,150 460,150 500,290 390,290" fill="#cfe8d0" stroke="#2e7d32" stroke-width="3"/><rect x="432" y="138" width="26" height="16" fill="#90a4ae"/>'
    s += '<path d="M400 265 h100 l-8 25 h-84 Z" fill="#43a047"/>'
    for cx,cy in [(420,255),(445,248),(470,258),(458,268),(432,268)]: s += f'<circle cx="{cx}" cy="{cy}" r="7" fill="#2e7d32"/>'
    # willow branch
    s += '<path d="M560 70 Q640 120 600 300" fill="none" stroke="#6d4c41" stroke-width="5"/>'
    for i in range(7):
        yy = 110 + i*26
        s += f'<path d="M{600+ (i%2)*4} {yy} q34 8 60 -4" fill="#7cb342" stroke="#558b2f" stroke-width="1.5"/>'
        s += f'<path d="M{600- (i%2)*4} {yy+12} q-34 8 -60 -4" fill="#7cb342" stroke="#558b2f" stroke-width="1.5"/>'
    # cross (medical)
    s += '<rect x="40" y="40" width="70" height="70" rx="10" fill="#c62828"/><rect x="66" y="52" width="18" height="46" fill="#fff"/><rect x="52" y="66" width="46" height="18" fill="#fff"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

# ---------------- diagrams ----------------
def d_tiers():
    s = t(360, 26, "Two tiers — match the method to what you actually have", 18, "middle", "700")
    s += rect(30, 50, 320, 300, "#eaf2fb", "#1565c0", 3, 10)
    s += rect(370, 50, 320, 300, "#f3eafb", "#6a1b9a", 3, 10)
    s += t(190, 82, "TIER A — Scarce resources", 16, "middle", "800", "#1565c0")
    s += t(530, 82, "TIER B — A working lab", 16, "middle", "800", "#6a1b9a")
    for i,ln in enumerate(["Scavenged jars, trays, pots","Pressure cooker / canner for sterilizing","Home-poured agar plates","Crude mold broth, used on the skin only","Willow-bark tea, plant remedies","Honey dressings, clean water, rest"]):
        s += t(50, 118 + i*34, "•  " + ln, 13, "start")
    for i,ln in enumerate(["Autoclave, glassware, balance, pH meter","Shake flasks / small bioreactor","Solvents, acids, cold storage","Published fermentation + extraction","Potency assay vs a reference","Aspirin from salicylic acid"]):
        s += t(390, 118 + i*34, "•  " + ln, 13, "start")
    s += t(360, 338, "Neither tier makes a medicine as safe as a factory drug. Be honest about that.", 12, "middle", "700", "#b71c1c")
    return svg(720, 362, s)

def d_penhist():
    s = t(360, 26, "From a chance mould to a mass-produced drug", 18, "middle", "700")
    x0 = 50; x1 = 690; y = 70
    s += line(x0, y, x1, y, "#546e7a", 4)
    pts = [(1928,"Fleming: mould\nkills bacteria"),(1930,"Paine: crude\nfiltrate cures\neye infections"),(1940,"Florey & Chain:\ncures infected\nmice"),(1941,"First patients\ntreated"),(1943,"Peoria: cantaloupe\nstrain + deep tanks"),(1945,"Nobel Prize;\nmass production")]
    for i,(yr,lab) in enumerate(pts):
        x = x0 + (x1-x0)*i/(len(pts)-1)
        s += f'<circle cx="{x}" cy="{y}" r="7" fill="#c62828"/>' + t(x, y-14, str(yr), 13, "middle", "800")
        up = (i%2==0)
        yy = y + 30 if up else y + 30
        for j,ln in enumerate(lab.split("\n")):
            s += t(x, y + 34 + j*16, ln, 11.5, "middle", "600")
    return svg(720, 170, s)

def d_surface():
    s = t(360, 24, "Tier A: surface culture of a Penicillium mould", 17, "middle", "700")
    # step 1 isolate
    s += rect(30, 50, 200, 150, "#fff", "#1565c0", 2, 8) + t(130, 72, "1. Isolate one colony", 13, "middle", "800", "#1565c0")
    s += f'<circle cx="130" cy="135" r="48" fill="#f1f8e9" stroke="#558b2f" stroke-width="2"/>'
    for cx,cy,r in [(110,120,10),(150,128,13),(125,155,8),(148,150,6)]:
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#9ccc65" stroke="#33691e"/>'
    s += t(130, 192, "streak for single colonies", 10.5, "middle")
    # step 2 grow
    s += rect(260, 50, 200, 150, "#fff", "#1565c0", 2, 8) + t(360, 72, "2. Grow on liquid", 13, "middle", "800", "#1565c0")
    s += rect(300, 150, 120, 36, "#fff8e1", "#8d6e63", 2, 4)
    s += '<rect x="300" y="150" width="120" height="14" fill="#cfe8d0"/>'  # broth
    s += '<path d="M300 150 h120 v6 h-120Z" fill="#43a047"/>'  # mycelial mat
    s += t(360, 140, "shallow broth, mat on top", 10.5, "middle") + t(360, 196, "~20–24 °C, 6–10 days", 10.5, "middle")
    # step 3 harvest
    s += rect(490, 50, 200, 150, "#fff", "#1565c0", 2, 8) + t(590, 72, "3. Filter the broth", 13, "middle", "800", "#1565c0")
    s += '<polygon points="560,95 620,95 598,135 582,135" fill="none" stroke="#546e7a" stroke-width="2"/>'
    s += line(590, 135, 590, 165, "#546e7a", 2) + rect(565, 165, 50, 26, "#e3f2fd", "#1565c0", 2, 3)
    s += t(590, 184, "filtrate", 10.5, "middle") + t(590, 196, "keep cold, use fast", 10, "middle", "700", "#c62828")
    return svg(720, 210, s)

def d_zone():
    s = t(360, 24, "Did it work? A zone-of-inhibition test (Oxford cup method)", 16, "middle", "700")
    s += f'<circle cx="360" cy="150" r="110" fill="#d7ccc8" stroke="#6d4c41" stroke-width="3"/>'
    s += t(360, 44, "agar seeded with test bacteria", 11, "middle")
    cups = [(360,150,"your filtrate"),(300,110,""),(420,110,""),(320,195,""),(400,195,"")]
    for i,(x,yy,lab) in enumerate(cups):
        rz = 34 if i==0 else 20
        s += f'<circle cx="{x}" cy="{yy}" r="{rz}" fill="#f1f8e9" stroke="#9e9e9e" stroke-dasharray="3 3"/>'
        s += f'<circle cx="{x}" cy="{yy}" r="7" fill="#fff" stroke="#1565c0" stroke-width="2"/>'
    s += t(360, 150+54, "clear zone = bacteria killed", 11, "middle", "700", "#2e7d32")
    s += t(600, 120, "Bigger clear ring", 12, "start", "700") + t(600, 138, "= more penicillin.", 12, "start")
    s += t(600, 166, "Compare to a known", 12, "start") + t(600, 184, "reference if you have", 12, "start") + t(600, 202, "one.", 12, "start")
    return svg(720, 275, s)

def d_ferment():
    items = [["Spore stock of Penicillium chrysogenum (single isolated strain)"],
             ["Seed flask: corn steep liquor + lactose broth, shaken, ~24 °C"],
             ["Production culture: CSL + lactose; feed phenylacetic acid in SMALL doses; aerate; hold pH ~6.5–7"],
             ["Harvest broth ~6–8 days; filter out the mould"],
             ["Chill + acidify (pH ~2); extract into amyl/butyl acetate (cold, fast)"],
             ["Back-extract into pH-7 buffer; repeat to concentrate"],
             ["Dry to a crude sodium/potassium salt; assay potency; check sterility"]]
    return flow(items, 720, 60, 20, "#f3eafb")

def d_aspirin():
    s = t(360, 24, "Tier B: making aspirin from salicylic acid", 17, "middle", "700")
    s += label_box(30, 55, 170, 70, ["Salicylic acid", "(from wintergreen oil", "or willow)"], "#e8f5e9", 13)
    s += t(255, 80, "+ acetic", 12, "middle", "700") + t(255, 96, "anhydride", 12, "middle", "700") + t(255, 112, "(+ H2SO4 drops)", 11, "middle")
    s += arrow(205, 90, 320, 90, "#6a1b9a", 3)
    s += label_box(325, 55, 150, 70, ["Warm 10–15 min", "in a water bath", "~80 °C"], "#f3eafb", 12)
    s += arrow(480, 90, 560, 90, "#6a1b9a", 3)
    s += label_box(555, 55, 150, 70, ["Aspirin", "(acetylsalicylic", "acid) crystals"], "#e8f5e9", 13)
    s += t(360, 160, "Add water to kill excess anhydride · cool on ice · vacuum-filter · recrystallize from ethanol+water", 12, "middle", "600")
    s += t(360, 186, "Purity: ferric-chloride test (purple = leftover salicylic acid) · melting point near 135–136 °C", 12, "middle", "600")
    return svg(720, 205, s)

def d_salicin():
    s = t(360, 24, "One plant, a whole family of painkillers", 17, "middle", "700")
    boxes = [(60,"Willow / meadowsweet bark","#e8f5e9"),(300,"Salicin, salicylates","#e8f5e9"),(540,"Salicylic acid","#fff3e0")]
    for x,lab,col in boxes: s += label_box(x, 60, 150, 56, [lab], col, 12)
    s += arrow(210, 88, 298, 88, "#558b2f", 3) + arrow(450, 88, 538, 88, "#558b2f", 3)
    s += label_box(300, 150, 150, 56, ["Aspirin (acetyl-", "salicylic acid)"], "#e3f2fd", 12)
    s += arrow(615, 116, 420, 150, "#1565c0", 3)
    s += t(360, 225, "Same salicylate chemistry — so willow tea shares aspirin's cautions (bleeding, Reye's, ulcers).", 12, "middle", "700", "#b71c1c")
    return svg(720, 245, s)

def d_infection():
    s = t(360, 24, "Spreading infection: when a wound becomes an emergency", 16, "middle", "700")
    # arm
    s += '<rect x="120" y="120" width="420" height="70" rx="34" fill="#ffe0b2" stroke="#8d6e63" stroke-width="2"/>'
    s += f'<circle cx="150" cy="155" r="22" fill="#ef9a9a" stroke="#c62828" stroke-width="2"/>' + t(150, 210, "wound", 11, "middle", "700")
    # red streak
    s += line(170, 150, 470, 150, "#c62828", 5, "8 5") + t(470, 135, "red streak", 11, "middle", "700", "#c62828")
    s += f'<ellipse cx="500" cy="150" rx="26" ry="18" fill="#ef9a9a" stroke="#c62828" stroke-width="2"/>' + t(500, 205, "swollen gland", 11, "middle", "700")
    s += t(360, 250, "Red streak toward the armpit/groin, spreading redness, fever, pus, or confusion =", 12.5, "middle", "700")
    s += t(360, 270, "a life-threatening infection. This is exactly what antibiotics were invented for.", 12.5, "middle", "700", "#b71c1c")
    return svg(720, 288, s)


def d_antisep():
    s = t(360, 24, "Antiseptics ladder: what you can make vs what you must stockpile", 15, "middle", "700")
    rows = [
        ("Chlorine bleach solution / Dakin's", "MAKEABLE", "#2e7d32"),
        ("Calcium hypochlorite (HTH) solution", "MAKEABLE", "#2e7d32"),
        ("Electrolysed brine (bleach)", "LAB / FIELD", "#1565c0"),
        ("Ethanol 70% (distil + dilute)", "MAKEABLE", "#2e7d32"),
        ("Iodine tincture / Lugol's (need iodine + KI)", "IF STOCKED", "#f9a825"),
        ("Povidone-iodine (needs povidone polymer)", "STOCKPILE", "#b71c1c"),
        ("Hydrogen peroxide 3%", "STOCKPILE", "#b71c1c"),
        ("Chlorhexidine", "STOCKPILE", "#b71c1c"),
    ]
    y = 46
    for lab, tag, col in rows:
        s += rect(30, y, 470, 30, "#f4f7f8", "#c9d4da", 1, 6)
        s += t(42, y+20, lab, 12.5, "start")
        s += rect(510, y, 180, 30, col, col, 0, 6)
        s += t(600, y+20, tag, 12, "middle", "800", "#fff")
        y += 38
    return svg(720, y+6, s)

def d_sterilize():
    s = t(360, 24, "Sterilising instruments: heat is the one you can always get", 15, "middle", "700")
    cols = [
        ("BOILING", "#0277bd", ["Rolling boil","at least 10-20 min","Kills germs but","NOT all spores","Last resort only"]),
        ("STEAM / PRESSURE", "#2e7d32", ["Pressure cooker","121 C = 15 psi","30 min wrapped","15 min at 132 C","Spores killed"]),
        ("DRY / CHEMICAL", "#6a1b9a", ["Dry heat oven,","or soak in 0.5%","chlorine / 70%","alcohol as a","backup only"]),
    ]
    x = 30
    for title, col, lines in cols:
        s += rect(x, 46, 210, 230, "#f4f7f8", col, 2, 10)
        s += rect(x, 46, 210, 34, col, col, 0, 10)
        s += t(x+105, 69, title, 13, "middle", "800", "#fff")
        for i, ln in enumerate(lines):
            s += t(x+105, 112 + i*32, ln, 12, "middle")
        x += 230
    s += t(360, 294, "Clean off all blood and tissue first - dirt protects germs from heat and chemicals.", 11.5, "middle", "700", "#b71c1c")
    return svg(720, 310, s)

def d_ether():
    s = t(360, 22, "Diethyl ether by distillation - and why it can kill you", 15, "middle", "700")
    # flask
    s += '<polygon points="90,150 130,150 150,250 70,250 Z" fill="#dcedf5" stroke="#1565c0" stroke-width="2"/>'
    s += t(110, 275, "ethanol +", 11, "middle") + t(110, 290, "sulfuric acid", 11, "middle")
    s += t(110, 138, "heat ~140 C", 11, "middle", "700", "#c62828")
    # tube to condenser
    s += line(150, 170, 330, 170, "#1565c0", 3)
    s += '<rect x="330" y="150" width="200" height="40" rx="8" fill="#cfe8f5" stroke="#0277bd" stroke-width="2"/>'
    s += t(430, 145, "water-cooled condenser", 11, "middle", "700")
    s += line(530, 180, 610, 240, "#1565c0", 3)
    s += '<polygon points="585,240 635,240 630,290 590,290 Z" fill="#e8eef2" stroke="#455" stroke-width="2"/>'
    s += t(610, 310, "ether (collect cold)", 11, "middle", "700")
    s += t(360, 345, "FLAMMABLE: flash point below room temp; vapour + air EXPLODES. Forms shock-sensitive peroxides in storage.", 11.5, "middle", "800", "#b71c1c")
    return svg(720, 362, s)


def d_precursor():
    s = t(360, 22, "Precursor chain: which basic materials unlock which medicines", 15, "middle", "700")
    def box(x,y,w,txt,col,tcol="#102a33",fs=10.5):
        o = rect(x,y,w,30,col,"#30505c",1.2,6)
        o += t(x+w/2, y+19, txt, fs, "middle","700",tcol)
        return o
    colA, colB, colC = "#e3eef2", "#eef0d8", "#f3e3ef"
    # Column headers
    s += t(110, 52, "RAW MATERIALS", 11.5, "middle","800","#30505c")
    s += t(360, 52, "INDUSTRIAL REAGENTS", 11.5, "middle","800","#6b6b1f")
    s += t(620, 52, "MEDICINES", 11.5, "middle","800","#6a1b9a")
    feed = ["Salt (NaCl)","Air + water","Sulfur / pyrite","Limestone","Coal tar","Ethanol (ferment)","Cinchona bark","Kelp / brine"]
    reag = ["Sulfuric acid","Nitric acid","NaOH / Na2CO3","Chlorine / bleach","Ammonia (Haber)","Phenol","Acetic anhydride","Iodine"]
    drug = ["Antiseptics","Salicylic acid / aspirin","Paracetamol","Benzocaine / procaine","Lidocaine","Sulfanilamide","Chloramphenicol","Quinine (extracted)"]
    y0 = 66; dy = 40
    for i,x in enumerate(feed): s += box(30, y0+i*dy, 160, x, colA)
    for i,x in enumerate(reag): s += box(280, y0+i*dy, 170, x, colB)
    for i,x in enumerate(drug): s += box(540, y0+i*dy, 170, x, colC)
    # a few representative arrows (feed->reag)
    def arow(x1,y1,x2,y2,col="#8aa0a8"):
        return line(x1,y1,x2,y2,col,1.6)
    # salt -> NaOH/chlorine ; air/water -> ammonia/nitric ; sulfur -> sulfuric ; coal tar -> phenol
    s += arow(190, y0+15, 280, y0+2*dy+15)   # salt -> NaOH
    s += arow(190, y0+15, 280, y0+3*dy+15)   # salt -> chlorine
    s += arow(190, y0+dy+15, 280, y0+4*dy+15) # air+water -> ammonia
    s += arow(190, y0+dy+15, 280, y0+dy+15)   # air+water -> nitric
    s += arow(190, y0+2*dy+15, 280, y0+15)    # sulfur -> sulfuric
    s += arow(190, y0+4*dy+15, 280, y0+5*dy+15) # coal tar -> phenol
    # reag -> drug representative
    s += arow(450, y0+3*dy+15, 540, y0+15)    # chlorine -> antiseptics
    s += arow(450, y0+5*dy+15, 540, y0+dy+15) # phenol -> salicylic
    s += arow(450, y0+5*dy+15, 540, y0+2*dy+15) # phenol -> paracetamol
    s += arow(450, y0+6*dy+15, 540, y0+2*dy+15) # acetic anhydride -> paracetamol
    s += arow(450, y0+15, 540, y0+4*dy+15)    # sulfuric -> lidocaine (via xylidine)
    s += arow(450, y0+4*dy+15, 540, y0+5*dy+15) # ammonia -> sulfanilamide
    s += arow(450, y0+7*dy+15, 540, y0+15)    # iodine -> antiseptics
    yend = y0 + 8*dy + 6
    s += t(360, yend+16, "Simplified. Almost every drug on the right needs several reagents in the middle, and the", 10.5,"middle","400","#444")
    s += t(360, yend+30, "middle column needs heavy industry to make at scale. The text gives each full chain.", 10.5,"middle","400","#444")
    return svg(720, yend+40, s)

# ---------------- regions ----------------
R = {
 1: "Few woody plants, but <b>willows</b> (Salix, incl. diamondleaf and tealeaf willow) grow along water and carry salicin " + c(52) + ". Stock trade-good medicines; the short season gives little else " + c(34) + ".",
 2: "<b>Pacific willows</b>, red elderberry (cook only — raw is toxic " + c(44) + "), and abundant conifers (needle tea, vitamin C). Damp climate: watch wounds closely for infection " + c(16) + ".",
 3: "Willows along rivers; wild mint and bee balm. Dry air is kind to a medicine stockpile " + c(1) + ". Honey from prairie hives for dressings " + c(13) + ".",
 4: "Black willow " + c(52) + ", elderberry (cooked), feverfew gone wild in old gardens " + c(42) + ". <b>Poison and water hemlock grow here</b> — never confuse them with wild carrot " + c(47) + ".",
 5: "Black willow, meadowsweet, and elderberry. Beekeeping is common — keep honey for wound care " + c(13, 14) + ".",
 6: "Willows, elderberry, and a long growing season for ginger and cayenne (capsaicin) " + c(43, 37) + ". Heat and humidity are hard on stored drugs — keep them cool and dry " + c(1, 2) + ".",
 7: "Grow ginger and peppers year-round " + c(43) + ". Heat/humidity degrade medicines fast; rotate and shade your stock " + c(1) + ". Elderberry (cooked) is common.",
 8: "Goodding's and other desert willows along washes " + c(52) + "; cactus for clean pulp dressings. Dry heat helps storage but keep drugs out of hot cars " + c(1) + ".",
 9: "Mountain willows at altitude " + c(52) + "; elderberry (cooked). Cold, dry storage is easy; nitroglycerin and insulin still need protection " + c(7, 10) + ".",
 10: "Willows along streams; grow ginger, peppers, feverfew " + c(43, 42) + ". <b>Water hemlock</b> is deadly in wet meadows " + c(47) + ".",
 11: "Desert willows; grow peppers and ginger " + c(43) + ". Keep a cool, dark store for medicines " + c(1) + ".",
 12: "Highland herbs plus cultivated ginger and chiles " + c(43) + "; elderberry species (cook) " + c(44) + ". Honey is widely available for dressings " + c(13) + ".",
 13: "Year-round ginger, peppers, aloe; tropical heat destroys stored drugs quickly — buy small, rotate often " + c(1, 2) + ". Boil water and guard every wound against infection " + c(15, 16) + ".",
}

TOC = [
 ("p1","Part 1 · How to Use This Guide",[("tiers","1.1 The two tiers"),("scope","1.2 Scope, honesty and limits"),("xref","1.3 What is in the First-Aid guide instead")]),
 ("p2","Part 2 · Stockpiling & Storage",[("stock","2.1 What to stockpile"),("store","2.2 Storage conditions"),("expiry","2.3 Do expired drugs still work?"),("except","2.4 The exceptions that go bad")]),
 ("p3","Part 3 · Infection, Wounds & Rehydration",[("prevent","3.1 Preventing infection"),("honey","3.2 Honey and wound care"),("spread","3.3 Spotting spreading infection and sepsis"),("ors","3.4 Oral rehydration solution")]),
 ("p4","Part 4 · Penicillin: The Story",[("hist","4.1 From Fleming to Peoria")]),
 ("p5","Part 5 · Penicillin — Tier A (Scarce)",[("surfA","5.1 Surface culture, step by step"),("assayA","5.2 Checking whether it works"),("useA","5.3 How the crude filtrate was used")]),
 ("p6","Part 6 · Penicillin — Tier B (Lab)",[("fermB","6.1 Submerged fermentation"),("extB","6.2 Extraction and a crude salt"),("qcB","6.3 Quality, sterility and limits")]),
 ("p7","Part 7 · Why Home Antibiotics Are Dangerous",[("mold","7.1 Toxic moulds and mycotoxins"),("allergy","7.2 Allergy and anaphylaxis"),("dose","7.3 Dose, purity and injection"),("yield","7.4 The yield reality")]),
 ("p8","Part 8 · Painkillers — Willow & Salicylates",[("willhist","8.1 Willow, meadowsweet and aspirin"),("willid","8.2 Identifying willows"),("willA","8.3 Tier A: harvesting and preparing"),("willdose","8.4 Dose and contraindications")]),
 ("p9","Part 9 · Painkillers — Tier B (Lab)",[("salB","9.1 Salicylic acid from wintergreen"),("aspB","9.2 Aspirin synthesis"),("aspqc","9.3 Purity checks and safety")]),
 ("p10","Part 10 · Other Plant Remedies",[("ginger","10.1 Ginger, feverfew"),("caps","10.2 Capsaicin and topical relief"),("elder","10.3 Elderberry and cranberry"),("lookalike","10.4 Deadly look-alikes")]),
 ("p11","Part 11 · Surgical Antiseptics & Disinfectants",[("chlor","11.1 Chlorine"),("dakin","11.2 Dakin's solution"),("alc","11.3 Alcohol"),("iod","11.4 Iodine"),("hp","11.5 Hydrogen peroxide"),("phenol","11.6 Phenol / carbolic acid"),("chx","11.7 Chlorhexidine"),("lime","11.8 Lime & lye")]),
 ("p12","Part 12 · Sterilising Instruments & Surgical Prep",[("steril","12.1 Sterilising instruments"),("hands","12.2 Surgical hand antisepsis"),("saline","12.3 Saline & sterile water")]),
 ("p13","Part 13 · Life-Saving Medicines & What to Stock",[("fluids","13.1 Fluids & IV realities"),("bleed","13.2 Stopping bleeding & TXA"),("pph","13.3 Postpartum haemorrhage"),("stockonly","13.4 Drugs you can only stockpile"),("oxy","13.5 Oxygen")]),
 ("p14","Part 14 · Anaesthesia & Antibiotics Beyond Penicillin",[("local","14.1 Local anaesthetics"),("general","14.2 General anaesthesia"),("otherabx","14.3 Antibiotics beyond penicillin"),("cantmake","14.4 Honest limits")]),
 ("p15","Part 15 · Synthesising Medicines in an Equipped Lab",[("slab","15.1 The lab & proving purity"),("sprec","15.2 The precursor chain"),("schem","15.3 Supporting chemistry"),("sloc","15.4 Local anaesthetics"),("ssulfa","15.5 Sulfonamides"),("sanalg","15.6 Analgesics & antipyretics"),("squin","15.7 Quinine from cinchona"),("schlor","15.8 Antibiotics synthetic vs fermented"),("sbio","15.9 Insulin, epinephrine, oxytocin"),("slim","15.10 Honest limits")]),
 ("p16","Part 16 · Region by Region",[]),
 ("srcs","Quick Reference & Sources",[]),
]

def body():
    b = [EXTRA_CSS]
    # ---------- Part 1 ----------
    b.append(part("p1","Part 1","How to Use This Guide"))
    b.append('<p>This guide is about medicines when there is no pharmacy, doctor or hospital to fall back on — the same world the rest of the <i>Survival Info</i> series assumes. It covers two very different situations, side by side, and it is honest about a hard truth: <b>nothing you make at home is as safe or as reliable as a factory-made drug</b>. Where this guide describes historical and laboratory methods for making antibiotics and painkillers, it does so because the information itself is worth preserving — not because a kitchen-brewed drug is ever a good substitute for the real thing.</p>')
    b.append(h2("tiers","1.1 The two tiers"))
    b.append('<p>Every how-to section is split into two tiers so you can match the method to what you actually have:</p>')
    b.append(fig(d_tiers(), "Tier A assumes scavenged gear; Tier B assumes a surviving, equipped laboratory."))
    b.append(ul(["<b>Tier A — Scarce resources:</b> jars, trays and pots you scavenged, a pressure cooker for sterilizing, home-poured agar, and plants you can gather. Results are crude and unmeasured.",
                 "<b>Tier B — A working lab:</b> you have found an intact lab or clinic — glassware, an autoclave, a balance, solvents, acids, cold storage and a way to measure things. You can follow published procedures much more closely, but the dangers do not disappear."]))
    b.append(h2("scope","1.2 Scope, honesty and limits"))
    b.append(danger("Read this first", "Home-made antibiotics and painkillers can <b>kill</b> — through toxic moulds, allergic shock, wrong doses, contamination, and liver or stomach damage. The methods here are historical and educational. If any real medicine, clinic or pharmacy is reachable, use it instead. This guide does <b>not</b> cover opioids, the opium poppy, or the synthesis of any controlled drug, and will not."))
    b.append(ul(["Everything medical here is for a true collapse where no professional care exists.",
                 "Every factual claim is sourced; sources are listed at the end and saved as PDFs alongside this guide.",
                 "We cover willow bark and other <b>evidence-backed</b> plants — not folklore — and we flag the plants that will poison you."]))
    b.append(h2("xref","1.3 What is in the First-Aid guide instead"))
    b.append('<p>To avoid repeating the companion <b>Medical &amp; First Aid</b> guide, this guide points to it rather than duplicating it. The First-Aid guide covers bleeding control, wounds and basic wound infection, CPR and choking, shock, fractures and splints, burns, bites, childbirth, dental emergencies, sterilizing instruments, and a set of NCCIH-backed herbal remedies (aloe, garlic, tea tree, chamomile, peppermint, echinacea). This guide adds the harder, more dangerous ground: <b>stockpiling, making antibiotics, and making painkillers</b>.</p>')
    b.append(tip("Companion guides", "Use this guide with <b>Medical &amp; First Aid</b> (wounds, splints, childbirth), <b>Sanitation &amp; Hygiene</b> (clean water, handwashing, soap), <b>Food</b> and <b>Gardening</b> (growing ginger, peppers, herbs), and <b>Preservation</b> (drying and storing)."))

    # ---------- Part 2 ----------
    b.append(part("p2","Part 2","Stockpiling & Storage"))
    b.append('<p>The single most useful thing you can do about medicine before a collapse is <b>stock up and store it well</b>. A deep, well-kept cabinet of ordinary drugs beats any home brew.</p>')
    b.append(h2("stock","2.1 What to stockpile"))
    b.append(table(["Category","Examples","Why"],[
        ["Pain / fever","Acetaminophen, ibuprofen, aspirin "+c(39,40,41),"Pain, fever, inflammation; aspirin also for suspected heart attack (First-Aid guide)"],
        ["Allergy","Diphenhydramine, loratadine; an epinephrine auto-injector if prescribed "+c(8),"Allergic reactions and anaphylaxis"],
        ["Gut","Oral rehydration salts, loperamide, antacids, bismuth "+c(20),"Diarrhea and dehydration are major killers"],
        ["Skin / wound","Antiseptic, antibiotic ointment, medical honey, clean dressings, tape "+c(13,14),"Prevent and treat wound infection"],
        ["Antibiotics","Only as legally prescribed/obtained; note expiry "+c(18),"Serious infections — see allergy cautions"],
        ["Personal / chronic","Your own prescriptions, insulin, inhalers, nitroglycerin "+c(7,10),"Chronic conditions do not pause in a crisis"],
        ["Tools","Thermometer, gloves, tweezers, scissors, blood-pressure cuff","Assessment and clean procedures"]]))
    b.append(h2("store","2.2 Storage conditions"))
    b.append(ul(["Store medicines in a <b>cool, dry, dark</b> place — a drawer, box or closet shelf, away from the stove and sink "+c(1)+".",
                 "The <b>bathroom cabinet is one of the worst places</b>: heat and moisture from showers break drugs down faster "+c(1)+".",
                 "Keep drugs in their <b>original containers</b>; leave the package insert and keep the cotton ball <i>out</i> (it pulls in moisture) "+c(1)+".",
                 "Do not store medicines in a car glove box — it gets too hot, cold and damp "+c(1)+".",
                 "Throw out anything that has changed color, smell or texture, or whose tablets are cracked, stuck together or smell of vinegar (aspirin breaking down) "+c(1,39)+"."]))
    b.append(h2("expiry","2.3 Do expired drugs still work?"))
    b.append('<p>The expiration date is the last day the maker guarantees full potency in the sealed container — not the day a drug becomes poison '+c(2,6)+'. The U.S. military faced the cost of throwing out huge stockpiles, so the FDA and Department of Defense ran the <b>Shelf-Life Extension Program (SLEP)</b>, testing stored drugs for years past their dates '+c(3)+'.</p>')
    b.append(ul(["In the SLEP analysis of 122 drug products, <b>about 88% of lots were extended an average of 66 months</b> (5.5 years) past their original expiry — but the extra life was highly variable lot to lot "+c(4)+".",
                 "A separate study found many active ingredients still present 28–40 years after expiry in sealed containers "+c(5)+".",
                 "Honest takeaway: a <b>solid tablet or capsule kept cool and dry is usually still largely potent</b> well past its date, though no one can promise full strength without testing "+c(4,6)+". In a true emergency a slightly weak painkniller is better than none; a <b>weak antibiotic is riskier</b> because under-dosing breeds resistance and may fail to clear the infection "+c(2)+"."]))
    b.append(caution("This is not a license to hoard junk", "SLEP results come from <b>sealed</b> products in <b>controlled storage</b>, tested lot by lot "+c(3,4)+". Your bathroom shelf is neither sealed nor controlled. Rotate your stock, and when a drug really matters, fresh is best."))
    b.append(h2("except","2.4 The exceptions that go bad"))
    b.append('<p>Some medicines genuinely lose potency or turn unsafe and must <b>not</b> be relied on past date or outside their storage range:</p>')
    b.append(table(["Drug","Problem","What the evidence says"],[
        ["Liquid / reconstituted antibiotics","Water lets them break down fast","Mixed amoxicillin suspension is discarded after ~14 days; keep refrigerated "+c(11)],
        ["Tetracycline (old formulations)","Degradation products can harm kidneys","Store tightly closed, discard outdated; don't use old tetracycline "+c(12)],
        ["Nitroglycerin (sublingual)","Volatile — evaporates once the bottle is opened","Keep in the original amber glass, tightly capped; potency falls fastest in heat and when carried in a pocket "+c(9,10)],
        ["Insulin","Heat and freezing destroy it","Refrigerate 36–46 °F; opened or unopened vials/pens last ~28 days at 59–86 °F; never use frozen insulin "+c(7)],
        ["Epinephrine auto-injectors","Potency drops with age/heat; may discolor","Replace on schedule; if the only one is expired and the liquid is clear, it may still help in anaphylaxis "+c(8)],
        ["EpiPen, eye drops, biologics","Sterility and potency limited","Treat dates seriously; discard discolored or cloudy solutions "+c(8)]]))
    b.append(fig(d_penhist(), "A century of antibiotics began with one contaminated plate "+c(21,23)+"."))

    # ---------- Part 3 ----------
    b.append(part("p3","Part 3","Infection, Wounds & Rehydration"))
    b.append('<p>Most deaths in a collapse come not from dramatic injuries but from <b>infection and dehydration</b>. Preventing and spotting them early saves far more lives than any home-made drug.</p>')
    b.append(h2("prevent","3.1 Preventing infection"))
    b.append(ul(["<b>Clean hands and clean water</b> prevent more infection than any medicine — see the Sanitation guide. Wash hands before touching any wound.",
                 "Irrigate wounds with clean (boiled and cooled, or disinfected) water, remove dirt, and cover with a clean dressing (First-Aid guide).",
                 "Keep wounds dry between dressing changes; watch them daily.",
                 "Vaccinate while you still can — tetanus especially."]))
    b.append(h2("honey","3.2 Honey and wound care"))
    b.append('<p>Honey is one of the few traditional wound treatments with real clinical evidence behind it.</p>')
    b.append(ul(["A Cochrane review found <b>high-quality evidence that honey heals partial-thickness burns faster</b> than conventional dressings (about 4–5 days faster), and moderate evidence it beats antiseptic-plus-gauze on wounds infected after surgery "+c(13)+".",
                 "For many other wound types the evidence is low-quality and mixed, so honey is a reasonable field dressing, not a miracle "+c(13)+".",
                 "<b>Medical-grade honey is gamma-irradiated</b> to kill <i>Clostridium</i> spores that raw honey can carry; raw honey is a fallback, not equivalent "+c(14)+".",
                 "<b>Never give honey to an infant under 1 year</b> — it can cause infant botulism "+c(48)+"."]))
    b.append(tip("How honey works", "Honey draws fluid out of the wound by osmosis, is acidic, and slowly releases hydrogen peroxide; some honeys (e.g. Leptospermum/manuka) have extra antibacterial activity "+c(14)+". Apply to a clean wound, cover, and change when it dilutes with fluid."))
    b.append(h2("spread","3.3 Spotting spreading infection and sepsis"))
    b.append(fig(d_infection(), "A red streak from a wound toward the body is a medical emergency "+c(17)+"."))
    b.append(ul(["<b>Cellulitis</b> (spreading skin infection): expanding redness, warmth, swelling, pain, often with fever and chills "+c(16)+".",
                 "<b>Lymphangitis</b>: a <b>red streak</b> running from the wound toward the armpit or groin, with tender swollen glands — it can spread to the bloodstream quickly "+c(17)+".",
                 "<b>Sepsis</b> (bloodstream infection, life-threatening): fever or low temperature, chills, fast heartbeat, fast breathing, and especially <b>confusion or a drop in alertness</b>; blood pressure falls and organs fail "+c(15)+".",
                 "Sepsis most endangers infants, older adults and the chronically ill "+c(15)+". These are the infections antibiotics were invented to stop — and the reason the rest of this guide exists."]))
    b.append(h2("ors","3.4 Oral rehydration solution"))
    b.append('<p>Diarrhea kills by dehydration. A simple home oral rehydration solution (ORS) treats most cases — the WHO notes ORS can treat the great majority of even cholera patients '+c(20)+'. (The First-Aid guide covers assessing and treating dehydration in detail.)</p>')
    b.append(check("WHO home ORS recipe "+c(20),[
        "<b>1 litre</b> of clean, safe (boiled and cooled, or disinfected) water",
        "<b>½ level teaspoon of salt</b>",
        "<b>6 level teaspoons of sugar</b>",
        "Stir until dissolved. It should taste no saltier than tears. Sip frequently; give small amounts often to children.",
        "Lightly salted rice water or a cereal gruel works too "+c(20)]))
    b.append(danger("Get the salt right", "Too much salt is dangerous, especially for children. Use level teaspoons, taste it, and if it is saltier than tears, make a new batch "+c(20)+"."))

    # ---------- Part 4 ----------
    b.append(part("p4","Part 4","Penicillin: The Story"))
    b.append(h2("hist","4.1 From Fleming to Peoria"))
    b.append(ul(["In <b>1928</b>, Alexander Fleming returned to his London lab to find a <i>Penicillium</i> mould had contaminated a culture plate and killed the staphylococci around it; he named the active substance <b>penicillin</b> "+c(21,23)+".",
                 "Fleming noted the mould juice inhibited staph, strep, gonococci, meningococci and diphtheria, but could not isolate or stabilize the active compound "+c(26)+".",
                 "In <b>1930</b> in Sheffield, pathologist <b>Cecil George Paine</b> obtained Fleming's mould, grew crude 'brews' in meat broth, and used the filtrate to <b>cure babies of gonococcal eye infection</b> (ophthalmia neonatorum) and an adult's pneumococcal eye infection — the first documented clinical use of penicillin "+c(24,25)+".",
                 "In <b>1940</b> at Oxford, <b>Florey, Chain and Heatley</b> purified penicillin, showed it cured mice given lethal streptococcus, and devised a potency assay; human trials followed in 1941 "+c(26,27,28)+".",
                 "Yields were tiny — about <b>150 flasks of surface culture</b> for one small dose "+c(27)+". The breakthrough came in the US.",
                 "At the USDA lab in <b>Peoria, Illinois</b>, scientists switched to <b>deep-tank (submerged) fermentation</b> fed with <b>corn steep liquor</b>, and found a super-productive strain on a <b>mouldy cantaloupe</b> from a local market. Yields soared, and penicillin was ready in quantity to treat Allied wounded by D-Day in 1944 "+c(21,22)+".",
                 "Fleming, Florey and Chain shared the <b>1945 Nobel Prize</b> "+c(23)+"."]))
    b.append(tip("Why the history matters here", "Every home method below is a scaled-down version of this story: Tier A is Paine's and Fleming's crude broth; Tier B is Oxford-to-Peoria fermentation and extraction. Knowing the history tells you what is realistic — and what is not."))

    # ---------- Part 5 ----------
    b.append(part("p5","Part 5","Penicillin — Tier A (Scarce)"))
    b.append(danger("Before you start", "Crude mould filtrate is <b>not a measured drug</b>. It was used historically on the surface of the body (eyes, skin) — never injected or swallowed as a brew. Read Part 7 on toxic moulds, allergy and dosing <b>before</b> attempting any of this. If real antibiotics are reachable, stop and use them."))
    b.append(h2("surfA","5.1 Surface culture, step by step"))
    b.append('<p>This mirrors Paine (1930) and the pre-Peoria Oxford method: grow a <i>Penicillium</i> mould on a shallow liquid surface and keep the filtered broth '+c(24,27)+'.</p>')
    b.append(fig(d_surface(), "Isolate one mould colony, grow it on shallow broth, filter and chill "+c(27,28)+"."))
    b.append(tierA("Obtaining and isolating the mould", steps([
        "<b>Find a blue-green <i>Penicillium</i> mould.</b> Historically the best strains came from mouldy <b>cantaloupe</b> and citrus "+c(21)+". The common blue-green mould on bread, fruit and cheese rinds is often <i>Penicillium</i>, but you cannot tell species by eye — see the danger box below.",
        "<b>Sterilize everything</b> you will reuse with a pressure cooker (a canner reaches ~121 °C / 15 psi, the same as a lab autoclave: 121 °C for 15 min) "+c(29)+". Boil-only is weaker; pressure is far better.",
        "<b>Pour agar plates</b> (Tier A agar: boil water with a little sugar and plain gelatin/agar from seaweed; a defined recipe is below in Tier B). Let them set in clean, covered dishes.",
        "<b>Streak for single colonies:</b> touch the mould with a flamed wire, then drag it across the plate in a zig-zag, reflaming between passes, so individual spores grow into separate colonies.",
        "<b>Pick one blue-green colony</b> that looks and smells like Penicillium and transfer it to a fresh plate or broth. Working from a single isolated colony is how you avoid a mixed, possibly toxic culture "+c(32)+"."])))
    b.append(tierA("Growing and harvesting", steps([
        "Make a <b>shallow broth</b> in sterilized flat vessels (jars, trays, dishes). Even plain nutrient broth works; a defined mineral-salts (Czapek-Dox-type) medium with a sugar can give more "+c(29)+".",
        "Inoculate with a spore suspension (shake the sporing mould in a little sterile water) and <b>do not disturb the vessels</b> — rocking breaks the mat and lowers yield "+c(27)+".",
        "Incubate around <b>20–25 °C</b> (the optimum for <i>Penicillium</i>) "+c(29)+". A delicate mat appears within a day or two, thickens, and turns blue-green over roughly a week as the culture matures and penicillin builds in the broth "+c(27)+".",
        "<b>Harvest the liquid under the mat</b>, filter it through clean cloth/paper to remove the mould, and keep the filtrate "+c(27)+".",
        "<b>Keep it cold and use it quickly.</b> Penicillin is unstable — stable only around pH 5–8 and destroyed by acid, alkali and warmth; cold slows the loss "+c(28)+"."])))
    b.append(h2("assayA","5.2 Checking whether it works"))
    b.append(fig(d_zone(), "A clear ring where bacteria cannot grow shows antibacterial activity "+c(27)+"."))
    b.append('<p>Heatley\'s "Oxford cup" assay is simple enough to copy roughly '+c(27)+':</p>')
    b.append(steps(["Seed an agar plate evenly with a test bacterium. Paine used a mild <i>Staphylococcus</i>, deliberately not a virulent strain "+c(24)+".",
                    "Set short open-ended cylinders (cut glass tube) upright on the agar and fill them with your filtrate; include one with a known reference if you have any "+c(27)+".",
                    "Incubate ~12–16 h. A <b>clear ring</b> around a cylinder means the filtrate stopped bacterial growth; a <b>bigger ring = more penicillin</b> "+c(27)+".",
                    "No ring means too little active penicillin (or none) — the broth is not usable as an antibacterial "+c(27)+"."]))
    b.append(caution("Handle test bacteria carefully", "Growing bacteria on plates means growing germs. Use a mild organism, keep plates sealed, wash hands, and destroy old plates by boiling or burning. Never culture material from a serious infection without need."))
    b.append(h2("useA","5.3 How the crude filtrate was used"))
    b.append('<p>Historically, before anyone could purify it, crude penicillin filtrate was applied <b>to the surface</b> of infected tissue:</p>')
    b.append(ul(["Paine soaked pads in the broth and applied them to skin infections (with poor results on deep pustules), then used drops in infected eyes <b>with striking success</b> "+c(24,25)+".",
                 "Fleming himself suggested the mould juice might be a useful <b>antiseptic for application to infected wounds</b>, and noted that injecting broth into animals was no more toxic than plain broth — but that is a long way from a safe human injectable "+c(26)+".",
                 "<b>Topical, surface use only</b> for any home filtrate. The next part explains why swallowing or injecting a crude brew is a different and far more dangerous matter."]))

    # ---------- Part 6 ----------
    b.append(part("p6","Part 6","Penicillin — Tier B (Lab)"))
    b.append('<p>If you have reached an intact laboratory, you can follow the published route from Oxford and Peoria much more closely. This is still demanding, low-yield work, and the safety limits in Part 7 still apply in full.</p>')
    b.append(h2("fermB","6.1 Submerged fermentation"))
    b.append(fig(d_ferment(), "The industrial route, in outline, from published fermentation and extraction work "+c(22,27,32)+"."))
    b.append(tierB("Strain and medium", ul([
        "Use an isolated <b><i>Penicillium chrysogenum</i></b> (the Peoria/modern production species), grown from a single colony and kept as a spore stock "+c(32)+".",
        "<b>Defined medium (Czapek-Dox type):</b> per litre, sucrose 30 g, NaNO<sub>3</sub> 3 g, K<sub>2</sub>HPO<sub>4</sub> 1 g, MgSO<sub>4</sub>·7H<sub>2</sub>O 0.5 g, KCl 0.5 g, FeSO<sub>4</sub>·7H<sub>2</sub>O 0.01 g, agar 13 g (for plates), pH ~7.2 — the Oxford group used a similar mineral-salts medium with a sugar and added yeast extract to speed growth "+c(29,27)+".",
        "<b>Production medium (Peoria route):</b> add <b>corn steep liquor</b> as the nitrogen/nutrient source and <b>lactose</b> as the slow carbon source — this is what multiplied yields in the 1940s "+c(22,32)+".",
        "<b>Side-chain precursor:</b> feed <b>phenylacetic acid</b> in small, repeated doses to make penicillin G and raise yield; it is toxic in large amounts, so it is fed little and often "+c(30,31)+"."])))
    b.append(tierB("Running the culture", ul([
        "Autoclave the medium (121 °C, 15 min) and inoculate from a shaken seed flask "+c(27)+".",
        "Grow <b>submerged with aeration and agitation</b> (shake flasks or a small stirred/sparged bioreactor), around <b>24 °C</b>, holding pH near <b>6.5–7</b>, for roughly 6–8 days "+c(22,27)+".",
        "Follow pH and (if you can) an activity assay; penicillin production peaks around neutral pH and can then fall "+c(27)+".",
        "Wild and lab <i>P. chrysogenum</i> on corn-steep-liquor/lactose media have produced on the order of <b>1–2.5 g/L</b> in studies — useful context for what 'a good batch' even means "+c(32)+"."])))
    b.append(h2("extB","6.2 Extraction and a crude salt"))
    b.append('<p>Chain\'s group worked out how to pull unstable penicillin out of the broth '+c(28)+':</p>')
    b.append(tierB("Back-extraction (as published)", steps([
        "Filter out the mould. Keep everything <b>cold</b> — penicillin is destroyed by acid, alkali and heat "+c(28)+".",
        "<b>Acidify</b> the cold filtrate to about pH 2 and immediately <b>extract into an organic solvent</b> (amyl or butyl acetate; ether was used historically) — the penicillin acid moves into the solvent "+c(28)+".",
        "<b>Back-extract into water</b> by shaking with a neutral (pH ~7) buffer or dilute alkali — the penicillin salt moves back into water, now cleaner and more concentrated "+c(28)+".",
        "Repeat the acid/neutral cycle to concentrate and purify "+c(28)+".",
        "<b>Dry gently</b> (freeze-drying was the Oxford breakthrough) to a <b>crude brown sodium or potassium salt</b> — still impure, but highly active "+c(28)+"."])))
    b.append(danger("Solvent safety", "Amyl acetate, butyl acetate and especially ether are <b>highly flammable</b> and their vapors are harmful. Work with excellent ventilation, no flames or sparks, eye protection and gloves. Ether can form explosive peroxides on storage. This is lab work, not kitchen work."))
    b.append(h2("qcB","6.3 Quality, sterility and limits"))
    b.append(tierB("Quality checks", ul([
        "<b>Potency:</b> run the agar zone-of-inhibition assay against a seeded plate, ideally versus a <b>reference penicillin</b>, to estimate strength "+c(27)+". The historical 'Oxford unit' was defined by the ring size "+c(26)+".",
        "<b>Identity (if equipped):</b> thin-layer chromatography can show a penicillin spot, and melting point/other tests help — but you will not reach pharmaceutical purity "+c(32)+".",
        "<b>Sterility:</b> any product for injection must be sterile and <b>pyrogen-free</b> (free of fever-causing microbial debris). You almost certainly cannot guarantee this at home or in a field lab — which is the heart of the danger in Part 7."])))
    b.append(caution("Even a good lab batch is not a pharmacy vial", "A crude salt of uncertain purity, strength and sterility is not the same as a tested, labelled, sterile drug. Dose, allergy and contamination risks all remain — read Part 7."))

    # ---------- Part 7 ----------
    b.append(part("p7","Part 7","Why Home Antibiotics Are Dangerous"))
    b.append('<p>This part is the spine of the whole antibiotic section. Read it even if you skip the methods.</p>')
    b.append(h2("mold","7.1 Toxic moulds and mycotoxins"))
    b.append(ul(["You <b>cannot identify a mould species by eye</b>. Blue-green does not guarantee <i>Penicillium</i>, and not every <i>Penicillium</i> makes useful penicillin "+c(32)+".",
                 "Many common moulds produce <b>mycotoxins</b> — natural poisons that are chemically stable, survive processing, and cause everything from acute poisoning to immune suppression, kidney damage, liver damage and <b>cancer</b> "+c(19)+".",
                 "Aflatoxins (from <i>Aspergillus</i>) damage DNA and cause liver cancer; ochratoxin A (from <i>Aspergillus</i> and some <i>Penicillium</i>) harms kidneys; others include patulin and fumonisins "+c(19)+".",
                 "A contaminated or misidentified culture can therefore <b>poison you while you think you are treating an infection</b>. This is the single biggest reason moldy-bread 'antibiotics' are a myth."]))
    b.append(h2("allergy","7.2 Allergy and anaphylaxis"))
    b.append(ul(["Penicillin allergy can cause an <b>immediate, life-threatening anaphylactic reaction</b> (IgE-mediated, like anaphylaxis) or severe delayed reactions that injure skin, organs and blood cells "+c(18)+".",
                 "About 10% of people report a penicillin allergy; most are not truly allergic — but you have <b>no way to test this safely at home</b>, and a true reaction can kill in minutes "+c(18)+".",
                 "A crude, impure brew adds further unknown proteins and mould material that can themselves trigger allergic shock.",
                 "If you ever use any penicillin, you must have <b>epinephrine ready</b> and know the signs of anaphylaxis (First-Aid guide). Never give it to someone with a known penicillin or severe drug allergy "+c(18)+"."]))
    b.append(h2("dose","7.3 Dose, purity and injection"))
    b.append(ul(["Factory penicillin is a <b>measured, pure, sterile</b> dose. A home filtrate or crude salt has <b>unknown strength and unknown purity</b>, so you cannot dose it — too little breeds resistance and fails; too much or too impure harms "+c(2,27)+".",
                 "<b>Injecting or drinking crude broth is extremely dangerous.</b> Non-sterile material injected into the body can cause bloodstream infection, abscesses and fatal reactions to pyrogens; crude material by mouth is both unreliable and risky.",
                 "Historical crude filtrate was used <b>on surfaces</b> (eyes, skin). That it was 'no more toxic than broth' in Fleming's animal tests does not make a home injectable safe "+c(26)+"."]))
    b.append(h2("yield","7.4 The yield reality"))
    b.append(danger("The honest bottom line", "Oxford needed ~150 flasks of surface culture for one small dose "+c(27)+", and a single patient needed on the order of a million Oxford units "+c(26)+". Home surface culture yields a weak, variable, impure filtrate. It may help a surface infection as it did in 1930 — but it is <b>not</b> a dependable cure for a serious systemic infection, and it can poison or shock the person you are trying to help. Prevent infection, stockpile real antibiotics, and treat any home brew as a desperate last resort, used on the skin, by someone who understands these risks."))

    # ---------- Part 8 ----------
    b.append(part("p8","Part 8","Painkillers — Willow & Salicylates"))
    b.append(h2("willhist","8.1 Willow, meadowsweet and aspirin"))
    b.append(fig(d_salicin(), "Willow and meadowsweet bark lead, chemically, straight to aspirin "+c(38)+"."))
    b.append(ul(["The pain- and fever-relieving power of <b>willow bark</b> has been known since antiquity; in the 1800s chemists isolated <b>salicylic acid</b> from it "+c(38)+".",
                 "In <b>1897</b>, Felix Hoffmann at Bayer acetylated salicylic acid to make <b>acetylsalicylic acid — aspirin</b>, gentler on the stomach than raw salicylic acid "+c(38)+". (The name traces partly to <i>Spiraea</i>, the old genus of meadowsweet, another salicylate plant.)",
                 "So willow tea, meadowsweet and aspirin are the <b>same chemical family</b>. That is good news (willow really can ease pain) and a warning (willow shares aspirin's dangers) "+c(34,35)+"."]))
    b.append('<p>What the evidence actually shows for willow bark:</p>')
    b.append(ul(["Standardized willow at <b>120 or 240 mg salicin per day is probably better than placebo</b> for low-back pain short-term (moderate-quality evidence); 240 mg was about as good as a dose of a prescription anti-inflammatory in one low-quality trial "+c(37)+".",
                 "Evidence for osteoarthritis is mixed, and willow has <b>not</b> been shown to work for rheumatoid arthritis; there are no good fever trials "+c(34)+".",
                 "Topical <b>capsicum (cayenne)</b> cream/plaster probably helps chronic low-back pain too "+c(37)+" (see Part 10)."]))
    b.append(h2("willid","8.2 Identifying willows"))
    b.append('<div class="phgrid">')
    b.append(photo("blackwillow","Black willow","Long, narrow, finely toothed leaves, green on both sides; shrubby to large tree along water. Across the eastern US and Canada "+c(52)+".",badge="WILLOW"))
    b.append(photo("whitewillow","White willow","Narrow leaves with fine silky white hairs beneath, giving a pale look. A classic salicin-bearing willow "+c(35)+".",badge="WILLOW"))
    b.append('</div>')
    b.append(ul(["Willows (<i>Salix</i>) grow <b>along streams, ponds and wet ground</b> across North America, from Arctic dwarf willows to large black willows "+c(52)+".",
                 "Look for <b>long, narrow leaves</b>, often finely toothed; slender flexible twigs; and catkins ('pussy willow') in spring.",
                 "Use the <b>bark of young twigs and branches</b> in spring, when salicin is highest. Many willow species contain salicin, but the <b>amount varies a lot</b> between species, plants and seasons "+c(36)+"."]))
    b.append(caution("Willows are safe to confuse with each other, mostly", "Different willows vary in strength, but the genus is not deadly. The real danger plants are elsewhere — see the look-alikes in Part 10, especially the hemlocks, which are nothing like willow but kill foragers who mistake them for other plants "+c(47)+"."))
    b.append(h2("willA","8.3 Tier A: harvesting and preparing"))
    b.append(tierA("Willow-bark tea (decoction)", steps([
        "Cut young twigs/branches; peel or scrape the <b>inner bark</b> (the greenish layer) "+c(35)+".",
        "Dry it, then use roughly <b>1–3 g of chopped bark per cup</b> (about 150 mL) of water; or boil ~4 g covered for ~15 minutes — the traditional decoction "+c(35)+".",
        "Drink up to <b>3 times a day, after meals</b> to reduce stomach upset "+c(35)+".",
        "<b>Reality check:</b> bark salicin varies, and 6–12 g of bark as a tea often will <b>not</b> reach the 120–240 mg salicin shown to work in trials "+c(36,37)+". Willow tea is a mild analgesic, not a reliable aspirin substitute."])))
    b.append(tierB("Willow tincture (if you have alcohol)", ul([
        "Steep chopped inner bark in strong drinking alcohol for a few weeks, shaking daily, then strain. Alcohol pulls out more salicylates than water and stores longer.",
        "Strength is still unknown without assay; start low and treat it like a weak aspirin with the same cautions below."])))
    b.append(h2("willdose","8.4 Dose and contraindications"))
    b.append('<p>Reputable references give these ranges for standardized willow bark:</p>')
    b.append(table(["Form","Amount","Notes"],[
        ["Comminuted bark, as tea","1–3 g in ~150 mL boiling water, up to 3×/day "+c(35),"Traditional use"],
        ["Decoction","~4 g boiled 15 min, 3×/day after meals "+c(35),"Traditional use"],
        ["Standardized salicin","~120–240 mg salicin/day "+c(37),"The dose with trial evidence for back pain"],
        ["Duration","≤4 weeks for joint pain; see a clinician after 3 days of fever or 1 day of headache "+c(35),"If care were available"]]))
    b.append(danger("Willow bark contraindications (it is aspirin's cousin)",
        "Do <b>not</b> use willow bark in: <b>children or teens</b> (risk of Reye's syndrome, which links salicylates in a viral illness to brain and liver damage) "+c(33,35)+"; people with <b>aspirin/NSAID allergy or salicylate-sensitive asthma</b> "+c(35)+"; <b>active stomach ulcers</b> or a <b>bleeding tendency / use of blood thinners</b> (salicylates increase bleeding) "+c(34,35)+"; <b>pregnancy</b> (especially the third trimester) and breastfeeding "+c(35)+"; and <b>G6PD deficiency</b> or severe liver/kidney disease "+c(35)+". Stop well before any surgery. Reported harms include anaphylaxis in an aspirin-allergic woman and a fatal case in a toddler given willow tea plus acetaminophen "+c(34)+"."))

    # ---------- Part 9 ----------
    b.append(part("p9","Part 9","Painkillers — Tier B (Lab)"))
    b.append('<p>With a lab you can make <b>aspirin</b> itself — a standard undergraduate chemistry exercise. This is ordinary, legal teaching chemistry. (No controlled drugs, and no opioids, are covered.)</p>')
    b.append(h2("salB","9.1 Salicylic acid from wintergreen"))
    b.append(fig(d_aspirin(), "Salicylic acid plus acetic anhydride gives aspirin "+c(50,51)+"."))
    b.append(tierB("Salicylic acid by hydrolysing oil of wintergreen", steps([
        "Oil of wintergreen is ~98% <b>methyl salicylate</b> "+c(49)+". Reflux a measured amount with excess <b>aqueous NaOH</b> (e.g. ~2 g oil with 25 mL of 2 M NaOH) for about <b>30 minutes</b>, using anti-bumping granules and a condenser "+c(49)+".",
        "Cool, then add <b>HCl (or dilute H<sub>2</sub>SO<sub>4</sub>) dropwise</b> until just acidic; salicylic acid precipitates "+c(49)+".",
        "Vacuum-filter, wash with ice-cold water, recrystallize from hot water, and dry "+c(49)+".",
        "Pure salicylic acid melts near <b>159–161 °C</b> "+c(49)+". (Willow/meadowsweet-derived salicylates are a plant source of the same acid, but wintergreen oil is by far the easiest starting point.)"])))
    b.append(h2("aspB","9.2 Aspirin synthesis"))
    b.append(tierB("Acetylation to aspirin (standard student procedure)", steps([
        "In a dry flask, mix about <b>2 g salicylic acid</b> with about <b>5 mL acetic anhydride</b> and <b>a few drops of concentrated sulfuric acid</b> (catalyst); swirl "+c(50,51)+".",
        "Warm in a <b>water bath (~80 °C) for ~10–15 minutes</b> "+c(50,51)+".",
        "Let it cool; <b>add water (e.g. ~50 mL)</b> to destroy the excess acetic anhydride, then cool on ice and <b>vacuum-filter</b> the crude aspirin "+c(50,51)+".",
        "<b>Recrystallize</b>: dissolve in a little warm ethanol, add hot water, cool slowly then on ice, and filter "+c(50,51)+".",
        "Air-dry the crystals "+c(50,51)+"."])))
    b.append(h2("aspqc","9.3 Purity checks and safety"))
    b.append(tierB("Checking purity", ul([
        "<b>Ferric chloride test:</b> add a drop of 1% FeCl<sub>3</sub> to a little of your product in water. A <b>purple/violet color means leftover salicylic acid</b> (a phenol); pure aspirin gives essentially no color "+c(50,51)+".",
        "<b>Melting point:</b> pure aspirin melts around <b>135–136 °C</b>; a low or broad melting range means impurity "+c(50,51)+".",
        "Recrystallize again if the ferric-chloride test is strongly colored or the melting point is off "+c(50,51)+"."])))
    b.append(danger("Reagent safety",
        "<b>Acetic anhydride</b> is corrosive and its vapor severely irritates eyes and airways; <b>concentrated sulfuric acid</b> causes severe burns; <b>ethanol and petroleum solvents are flammable</b>. Work in good ventilation (fume hood if possible), wear goggles and gloves, add acid to water (never water to acid), keep solvents away from flames, and add water to the reaction <b>only after cooling</b> to control the exothermic decomposition of excess anhydride "+c(50,51)+"."))
    b.append(caution("Dose home-made aspirin like aspirin", "If you ever use aspirin you synthesized, all the aspirin cautions apply: not for children/teens (Reye's) "+c(33)+", not with ulcers or bleeding risk, and watch for allergy "+c(39)+". Standard adult aspirin dosing and warnings are on the label of commercial aspirin "+c(39)+"."))

    # ---------- Part 10 ----------
    b.append(part("p10","Part 10","Other Plant Remedies"))
    b.append('<p>A few other plants have real evidence behind them. Use real ID, and know the deadly look-alikes.</p>')
    b.append(h2("ginger","10.1 Ginger and feverfew"))
    b.append('<div class="phgrid">')
    b.append(photo("ginger","Ginger (rhizome)","The knobby underground stem used fresh, dried or as tea. Grown in warm regions and indoors "+c(43)+".",badge="REMEDY"))
    b.append(photo("feverfew","Feverfew","Daisy-like flowers, feathery aromatic leaves; an escaped garden plant. A member of the ragweed family "+c(42)+".",badge="REMEDY"))
    b.append('</div>')
    b.append(ul(["<b>Ginger</b> helps nausea and vomiting, including in pregnancy, and may ease menstrual cramps and knee osteoarthritis; side effects are mild (heartburn, mouth irritation) "+c(43)+".",
                 "<b>Feverfew</b> may help <b>prevent migraine</b> (mixed evidence). Chewing fresh leaves can cause mouth sores; ragweed-sensitive people may react; it may slow clotting; <b>not in pregnancy</b> (affects uterine contractions) "+c(42)+"."]))
    b.append(h2("caps","10.2 Capsaicin and topical relief"))
    b.append('<div class="phgrid">')
    b.append(photo("capsicum","Cayenne / hot pepper","Capsaicin is the heat in hot peppers. Grow in warm regions; dry and powder the ripe pods "+c(37)+".",badge="REMEDY"))
    b.append(photo("cranberry","Cranberry","Low creeping bog shrub; tart red berries. Juice/supplements may reduce recurrent UTIs "+c(45)+".",badge="REMEDY"))
    b.append('</div>')
    b.append(ul(["<b>Topical capsaicin</b> (cayenne cream or plaster) probably helps chronic low-back pain and other local pain; it works by depleting pain-signal chemicals in nerves "+c(37)+".",
                 "Make a simple rub by steeping cayenne powder in oil; <b>test on a small patch</b>, keep it away from eyes and broken skin, and wash hands after — it burns mucous membranes."]))
    b.append(h2("elder","10.3 Elderberry and cranberry"))
    b.append('<div class="phgrid">')
    b.append(photo("elderberry","Common elderberry","Clusters of tiny white flowers, then small dark berries. <b>Cook the berries</b> — raw berries, leaves and stems are toxic "+c(44)+".",badge="COOK FIRST"))
    b.append(photo("redelder","Red elderberry","Western/boreal species with bright red berries in a domed cluster. Treat as toxic unless properly prepared "+c(44)+".",badge="COOK FIRST"))
    b.append('</div>')
    b.append(ul(["<b>Elderberry</b> may modestly relieve cold/flu symptoms (small studies); it is not proven for other uses "+c(44)+".",
                 "<b>Raw or unripe elderberries and the leaves/stems contain cyanide-producing compounds</b> that cause nausea, vomiting and severe diarrhea — <b>cooking destroys them</b> "+c(44)+".",
                 "<b>Cranberry</b> may reduce the risk of recurrent UTIs in some women (evidence inconsistent); it is <b>not</b> a treatment for an active UTI "+c(45)+"."]))
    b.append(h2("lookalike","10.4 Deadly look-alikes"))
    b.append(danger("These plants kill foragers", "The wild-carrot/parsley family contains some of North America's deadliest plants. Never gather a 'wild herb' you cannot identify with total certainty."))
    b.append('<div class="phgrid">')
    b.append(photo("poisonhemlock","Poison hemlock","Smooth hollow stems with <b>purple-red blotches</b>, lacy fern-like leaves, musty smell. All parts deadly "+c(47)+".",bad=True,badge="DEADLY"))
    b.append(photo("waterhemlock","Water hemlock","Wet-ground plant, often called the most toxic in North America; causes rapid seizures and death "+c(47)+".",bad=True,badge="DEADLY"))
    b.append('</div>')
    b.append('<div class="phgrid">')
    b.append(photo("wildginger","Wild ginger (do NOT use)","North American wild ginger (<i>Asarum</i>) is <b>not</b> culinary ginger. Related plants contain <b>aristolochic acid</b>, a potent kidney toxin and carcinogen "+c(46)+".",bad=True,badge="AVOID"))
    b.append(photo("penicillium","Penicillium mould","Blue-green mould like this produced penicillin — but you cannot tell safe from toxic species by eye "+c(19,32)+".",bad=True,badge="CAUTION"))
    b.append('</div>')
    b.append(ul(["<b>Poison hemlock</b> (<i>Conium</i>): smooth, hollow, purple-spotted stems and a mousy smell; symptoms progress fast and any delay raises the risk of death "+c(47)+".",
                 "<b>Water hemlock</b> (<i>Cicuta</i>): grows in wet ground and is often described as the most poisonous plant in North America "+c(47)+".",
                 "<b>Do not use North American wild ginger (<i>Asarum</i>) medicinally.</b> Aristolochic acid (in the related birthworts and some <i>Asarum</i>) causes irreversible kidney damage and urinary-tract cancers "+c(46)+". Culinary ginger (<i>Zingiber</i>) in Part 10.1 is a different, safe plant."]))

    # ---------- Part 11: Antiseptics & Disinfectants ----------
    b.append(part("p11","Part 11","Surgical Antiseptics & Disinfectants"))
    b.append('<p>Before antibiotics, the single biggest life-saver in surgery was stopping germs from getting into wounds in the first place. Most of that still works, and most of it you can actually make or improvise. This is the most practical chapter in the guide: clean water, chlorine, alcohol and iodine save more lives in a collapse than any home-brewed drug.</p>')
    b.append(fig(d_antisep(), "Rough guide: green = you can make it from scavenged materials; blue = needs power or a little kit; amber = only if you stocked the raw material; red = realistically a stockpile item."))

    b.append(h2("chlor","11.1 Chlorine - the workhorse disinfectant"))
    b.append('<p>Chlorine (as sodium or calcium hypochlorite) kills bacteria, viruses and fungi fast, is cheap, and can be made or stretched from common supplies. It is the backbone of water treatment, surface disinfection and wound irrigation '+c(56)+'.</p>')
    b.append(tierA("From household bleach", '<p>Use plain, <b>unscented</b> household bleach (5-9% sodium hypochlorite); never scented, "splashless" or laundry-additive types '+c(54)+'.</p>'+ul([
        "<b>Surface disinfectant:</b> 5 tablespoons (1/3 cup) bleach per gallon, or 4 tsp per quart, of room-temperature water; leave surfaces visibly wet for at least 1 minute "+c(54)+".",
        "<b>Strong 0.5% chlorine</b> (body-fluid spills, cleaning): 1 part 5% bleach to 9 parts water "+c(55)+".",
        "<b>General dilution formula:</b> parts of water per part of bleach = (% chlorine in bleach / % wanted) - 1. Example: 3.5% bleach to 0.5% = (3.5/0.5)-1 = 6 parts water "+c(55)+".",
        "Make it <b>fresh daily</b> - chlorine solutions weaken within 24 hours; store in the shade, not sunlight "+c(54,55)+"."])))
    b.append(tierA("From calcium hypochlorite (HTH / pool shock)", '<p>High-test calcium hypochlorite (65-70% available chlorine) is far more stable than liquid bleach - it loses roughly 0.01% strength a day versus 20-50% in a few weeks for warm liquid bleach - so it is the better thing to <b>store</b> '+c(83)+'.</p>'+ul([
        "To make a 0.5% chlorine solution: dissolve about <b>14 g HTH powder per litre</b> of water (formula: (% wanted / % in powder) x 1000 g per litre) "+c(55)+".",
        "For drinking water, EPA's method: 1 heaping teaspoon HTH in 2 gallons of water to make a stock, then add 1 part stock to 100 parts water to be disinfected "+c(58)+".",
        "Store HTH sealed, cool, dark and dry, away from anything organic or flammable "+c(83)+"."])))
    b.append(tierB("Making chlorine from salt and electricity", '<p>If you have DC power and salt you can generate sodium hypochlorite on site by <b>electro-chlorination</b>: passing current through brine (salt water) produces a dilute bleach at the electrodes '+c(85)+'. Field systems use clean salt and softened water, a power source/rectifier, and electrodes; <b>always test the available-chlorine strength before using it</b> '+c(84,85)+'. This is how many water plants and some field clinics make their own disinfectant.</p>'))
    b.append(danger("Never mix bleach with acids, ammonia or other cleaners", "Mixing hypochlorite with acid (vinegar, toilet cleaners, descalers) or with ammonia releases chlorine or chloramine gas, which can injure or kill in an enclosed space. Mix bleach only with water, in a ventilated area "+c(54,56)+"."))

    b.append(h2("dakin","11.2 Dakin's solution - buffered chlorine for wounds"))
    b.append('<p>Plain bleach is too harsh and too alkaline for open tissue. In World War I, surgeon Alexis Carrel and chemist Henry Dakin developed a <b>buffered, dilute sodium-hypochlorite wound irrigant</b> that disinfects without destroying healthy tissue - it saved countless limbs and lives in the trenches '+c(64)+'. The trick is removing the free caustic alkali with a buffer (originally boric acid; baking soda today) '+c(64)+'.</p>')
    b.append(tierA("Dakin's from household bleach", ul([
        "<b>Quarter-strength (0.025%)</b>, the common tissue-safe wound strength: to make ~1 litre, mix about <b>6 mL (a bit over 1 tsp) of 5.25% bleach + ~994 mL boiled, cooled water + 1/2 tsp baking soda</b> "+c(53)+".",
        "Stronger versions (0.5% full strength, 0.125-0.25% half/quarter) are used for heavier contamination or debridement but are more irritating - use the weakest that controls the wound "+c(53)+".",
        "<b>Use it fresh</b> and discard opened solution after 48 hours; keep it out of light "+c(53)+".",
        "Dakin's original trench recipe: dissolve sodium carbonate (washing soda) in water, add chlorinated lime, let it settle, siphon off the clear liquid, then add just enough boric acid to neutralise it - about 0.5% hypochlorite, keeps about a week "+c(64)+"."])))
    b.append(tip("Clean the wound first","Chlorine and every other antiseptic are partly neutralised by blood, pus and dirt "+c(56)+", so irrigate out gross contamination before applying a disinfectant."))

    b.append(h2("alc","11.3 Alcohol for skin and hands"))
    b.append('<p>Ethanol and isopropanol are rapidly lethal to bacteria (including TB), fungi and most viruses, though <b>they do not kill spores</b> '+c(56)+'. They are the mainstay of skin prep and hand antisepsis.</p>')
    b.append(caution("Why 70% beats 95%", "Counter-intuitively, 60-90% alcohol kills better than near-pure alcohol. Water is needed to denature microbial proteins; absolute (95-100%) alcohol dries and coagulates the outer proteins into a shell that protects the organism inside. Aim for about 70% "+c(56)+"."))
    b.append('<p>If you distil your own spirits (see the Food Preservation guide), you can dilute strong ethanol down to ~70% for antisepsis. The WHO publishes two <b>local-production hand-rub formulas</b> you can mix if you have the ingredients '+c(57)+':</p>')
    b.append(steps([
        "<b>Formula I (per litre):</b> 833 mL ethanol 96% + 42 mL hydrogen peroxide 3% + 14.5 mL glycerol 98%, then top up to 1000 mL with boiled, cooled water. Final: ~80% ethanol "+c(57)+".",
        "<b>Formula II (per litre):</b> 751 mL isopropyl alcohol 99.8% + 42 mL H2O2 3% + 14.5 mL glycerol 98%, topped to 1000 mL. Final: ~75% isopropanol "+c(57)+".",
        "The hydrogen peroxide kills spores in the bottles; the glycerol stops your skin cracking. <b>Quarantine filled bottles 72 hours</b> before use "+c(57)+".",
        "Check the final strength with an alcohol hydrometer if you have one (target 75-85%) "+c(57)+"."]))
    b.append(danger("Alcohol is extremely flammable", "Ethanol 80% and isopropanol 75% have flash points below 20 C - the vapour ignites near room temperature. Mix and store away from any flame, spark or hot surface, in a cool, ventilated place "+c(57)+"."))

    b.append(h2("iod","11.4 Iodine - tincture, Lugol's and povidone-iodine"))
    b.append('<p>Iodine is a broad-spectrum antiseptic and water disinfectant. You cannot realistically manufacture elemental iodine in a collapse, so the raw iodine/iodide is a <b>stockpile item</b> - but a little goes a long way and it stores well.</p>')
    b.append(ul([
        "<b>Tincture of iodine (2%):</b> for skin prep, and to disinfect water - about 5 drops of 2% tincture per litre (10 if cloudy), wait 30 minutes "+c(58,59)+". Avoid long-term use, and in pregnancy, thyroid disease or iodine allergy "+c(58)+".",
        "<b>Lugol's / strong iodine solution:</b> 5 g iodine + 10 g potassium iodide per 100 mL (5% iodine, 10% KI). The iodide lets the iodine dissolve in water "+c(60)+". If you have iodine crystals and KI, you can mix Lugol's; it is both an antiseptic concentrate and a water-treatment stock.",
        "<b>Povidone-iodine (Betadine):</b> the gentlest surgical-prep form, but it needs the carrier polymer <b>povidone</b>, which you cannot make at home - <b>stockpile it</b> "+c(61)+"."]))

    b.append(h2("hp","11.5 Hydrogen peroxide - mostly a stockpile item"))
    b.append('<p>Household 3% hydrogen peroxide is a useful mild disinfectant and is part of the WHO hand-rub recipe above. <b>You cannot make meaningful hydrogen peroxide at home.</b> Industrially it is produced by repeatedly hydrogenating and oxidising an anthraquinone over a palladium catalyst, then vacuum-concentrating it - pressurised hydrogen, special catalysts and reactors '+c(82)+'. Concentrated peroxide is also dangerously unstable: metals, dirt and organics make it decompose explosively '+c(82)+'. Stock the 3% solution, keep it cool and dark, and accept it will slowly weaken.</p>')
    b.append(caution("Peroxide on open wounds", "Hydrogen peroxide is useful for cleaning dirty surfaces and gear, but it damages healthy tissue and is no longer recommended for routine irrigation of healing wounds - dilute chlorine (Dakin's), saline or clean water are kinder "+c(53)+"."))

    b.append(h2("phenol","11.6 Phenol / carbolic acid - history, and a warning"))
    b.append('<p>Joseph Lister introduced <b>carbolic acid (phenol)</b> antiseptic surgery in 1867, spraying and dressing wounds with it and dramatically cutting post-operative deaths - the birth of antiseptic surgery '+c(62)+'. But phenol is <b>caustic and systemically poisonous</b>: it causes painless white skin burns that turn to blistering and necrosis, and can be absorbed to cause collapse, dark urine, and organ damage '+c(63)+'. It is not something to brew or splash around. Know the history; use milder modern antiseptics (chlorine, iodine, alcohol) instead '+c(63)+'.</p>')

    b.append(h2("chx","11.7 Chlorhexidine - stockpile, not makeable"))
    b.append('<p>Chlorhexidine gluconate is an excellent, long-lasting skin and surgical-scrub antiseptic (often combined with alcohol). It is a synthesised compound you cannot produce without a chemical plant - <b>buy and store it</b> while you can. It is a core item on any medical stockpile list '+c(56)+'.</p>')

    b.append(h2("lime","11.8 Lime and lye for sanitation"))
    b.append('<p>For latrines, floors, spills and body disposal, lime is the classic cheap disinfectant. <b>Quicklime (calcium oxide)</b>, made by burning limestone (see the Concrete &amp; Lime guide), reacts with water to give <b>slaked lime (calcium hydroxide)</b>, a strong alkali that raises pH and suppresses pathogens; <b>chlorinated lime</b> (bleaching powder) was used by Semmelweis in 1847 to stop childbed fever and is the parent of modern bleach '+c(64)+'. <b>Lye (potassium hydroxide) from wood ash</b> - covered in the Sanitation guide for soap-making - is likewise a powerful cleaner. Handle all of these with care: they burn skin and eyes.</p>')

    # ---------- Part 12: Sterilising & Surgical Prep ----------
    b.append(part("p12","Part 12","Sterilising Instruments & Surgical Prep"))
    b.append('<p>A trained surgeon with sterile instruments, clean hands and clean fluids can do life-saving work even without a hospital. These are the supporting skills that make surgery survivable.</p>')
    b.append(fig(d_sterilize(), "Heat is the most reliable way to sterilise and the one you can always improvise. Chemical soaks are a backup, not an equal."))

    b.append(h2("steril","12.1 Sterilising instruments"))
    b.append(ul([
        "<b>Boiling</b> kills germs but not all bacterial spores: a rolling boil for 10-20 minutes is a <b>last resort</b> for cleaning instruments when nothing better exists.",
        "<b>Steam under pressure</b> (a pressure cooker or canner acting as an autoclave) is the real answer. Clinical standard: <b>121 C for 30 minutes</b> for wrapped instruments, or <b>132 C for 15 minutes</b>, plus drying time "+c(79)+". A 15-psi pressure cooker reaches ~121 C.",
        "<b>Dry heat</b> (an oven, ~160-170 C for 1-2 hours) works for metal that water would rust.",
        "<b>Chemical soaks</b> - 0.5% chlorine or 70% alcohol - are only a backup when heat is impossible; alcohol does not kill spores "+c(56)+".",
        "<b>Always scrub off all blood and tissue first.</b> Organic matter shields germs from both heat and chemicals "+c(56)+"."]))

    b.append(h2("hands","12.2 Surgical hand antisepsis"))
    b.append('<p>WHO defines surgical hand preparation: remove rings/watches, clean under the nails, then either scrub with an antiseptic soap (chlorhexidine or povidone-iodine) or - preferred - apply an <b>alcohol-based hand-rub</b>, keeping hands wet for the full rub time and letting them air-dry before gloving '+c(57)+'. The hand-rub formulas in Part 11.3 are exactly what WHO designed for this.</p>')

    b.append(h2("saline","12.3 Making saline and sterile water"))
    b.append('<p><b>Normal saline is 0.9% salt: 9 g (about 1.5 level teaspoons) of pure salt per litre of water</b> '+c(66)+'. For rinsing wounds and eyes, dissolve that in water that has been <b>boiled for the recommended time and cooled with the lid on</b>, in a sterilised container. This is fine for <b>external irrigation</b>.</p>')
    b.append(danger("Do NOT infuse homemade fluid into a vein", "Wound-rinse saline is not IV fluid. Intravenous fluids must be sterile AND pyrogen-free - free of the bacterial cell-wall fragments (pyrogens) that survive boiling and cause fever, shock and death when injected. Homemade solutions, even if boiled, can carry pyrogens and particles; infusing them risks fatal sepsis and reactions "+c(66)+". IV fluids are a stockpile item, not a DIY one."))

    # ---------- Part 13: Life-Saving Medicines ----------
    b.append(part("p13","Part 13","Life-Saving Medicines & What to Stock"))
    b.append('<p>This chapter is about the drugs that most directly keep people alive - and an honest accounting of which ones you can make, which you can only stockpile, and how to store them. The frame is the WHO <b>Essential Medicines List</b>: the medicines a basic health system most needs '+c(65)+'. In a collapse, the ones below matter most.</p>')

    b.append(h2("fluids","13.1 Fluids: rehydration and IV realities"))
    b.append(ul([
        "<b>Oral rehydration (ORS)</b> is the single biggest life-saver for diarrhoea and is fully DIY: <b>1 litre clean water + 1/2 tsp salt + 6 tsp sugar</b> "+c(20)+" (full detail in Part 3.4). Give by mouth whenever the person can swallow.",
        "<b>Normal saline (0.9% NaCl)</b> and <b>Ringer's lactate / Hartmann's</b> are the standard IV fluids. Ringer's per litre contains roughly sodium 131, potassium 5, calcium 2, chloride 111 and lactate 29 mmol "+c(66)+" - it cannot be improvised safely.",
        "<b>IV fluids must be stockpiled</b>, not made (see Part 12.3). Rotate stock and keep it from freezing."]))

    b.append(h2("bleed","13.2 Stopping bleeding: tourniquets, packing, tranexamic acid"))
    b.append('<p>Haemorrhage kills fast and is one place where simple action saves lives. The American College of Surgeons "Stop the Bleed" steps: ensure safety and call for help, then <b>apply firm direct pressure</b>; if it keeps bleeding, <b>pack the wound tightly with gauze</b> (haemostatic gauze if you have it) and keep pressing; for a severe arm or leg bleed, <b>apply a tourniquet 2-3 inches above the wound</b> (not over a joint) and tighten until bleeding stops '+c(80)+'.</p>')
    b.append(ul([
        "<b>Haemostatic gauze</b> (kaolin- or chitosan-impregnated) and commercial tourniquets are cheap stockpile items that punch far above their weight "+c(80)+".",
        "<b>Tranexamic acid (TXA)</b> reduces death from bleeding if given early. For major trauma or postpartum haemorrhage: <b>1 g IV over 10 minutes</b>, repeated once if bleeding continues, given <b>within 3 hours</b> of injury or birth - later doses do not help "+c(77,78)+". TXA is stable, cheap, and worth stocking."]))

    b.append(h2("pph","13.3 Childbirth emergencies: postpartum haemorrhage"))
    b.append('<p>Bleeding after birth is a leading cause of maternal death and is very treatable with drugs that store reasonably well. WHO recommends, to prevent and treat postpartum haemorrhage '+c(77)+':</p>')
    b.append(ul([
        "<b>Oxytocin 10 IU</b> intramuscular is first choice - but it needs a cold chain and degrades in heat "+c(77)+".",
        "<b>Heat-stable carbetocin 100 mcg</b> where the cold chain is unreliable "+c(77)+".",
        "<b>Misoprostol 400-600 mcg</b> by mouth where neither is available - it is a tablet that stores at room temperature, making it the most collapse-friendly option "+c(77)+".",
        "Plus uterine massage, the bleeding measures above, and TXA within 3 hours "+c(77,78)+"."]))

    b.append(h2("stockonly","13.4 The drugs you can only stockpile"))
    b.append('<p>Be honest: the following are life-saving and essentially impossible to make outside a pharmaceutical plant. Stock them, store them well, and rotate them.</p>')
    b.append(table(["Medicine","What it saves","Storage"],[
        ["Epinephrine (adrenaline)","Anaphylaxis, cardiac arrest","Cool, dark; discolours when degraded; auto-injectors expire "+c(8)],
        ["Insulin","Type 1 diabetes (fatal without it)","Fridge; ~28 days at room temp; never frozen "+c(7)],
        ["Lidocaine","Local anaesthesia for procedures","Room temp, protect from light "+c(67)],
        ["Oxytocin","Postpartum bleeding","Cold chain; heat-sensitive "+c(77)],
        ["Tranexamic acid","Trauma/childbirth bleeding","Room temp; long shelf life "+c(78)],
        ["Misoprostol","Postpartum bleeding","Room temp, dry; moisture-sensitive "+c(77)],
        ["Aspirin","Suspected heart attack, pain/fever","Cool, dry; smells of vinegar when degraded "+c(39)],
        ["Antibiotics (most)","Serious infection","Cool, dry; see Part 14 "+c(1)],
    ]))

    b.append(h2("oxy","13.5 Oxygen"))
    b.append('<p>Supplemental oxygen saves lives in pneumonia, trauma and childbirth. You cannot bottle meaningful medical oxygen by hand, but the two real-world routes are worth knowing: a <b>pressure-swing-adsorption (PSA) concentrator</b> pulls room air through zeolite beds that trap nitrogen and pass ~90-96% oxygen - it only needs electricity, no refilling '+c(81)+'; and <b>water electrolysis</b> can make high-purity oxygen but is power-hungry and also makes explosive hydrogen '+c(81)+'. A concentrator plus a reliable power source is the realistic survival answer; keep it and spare filters.</p>')

    # ---------- Part 14: Anaesthesia & Antibiotics ----------
    b.append(part("p14","Part 14","Anaesthesia & Antibiotics Beyond Penicillin"))
    b.append('<p>Two of the hardest problems in collapse surgery: controlling pain so an operation is possible, and treating infection when penicillin is not enough. Here is what the published record shows - with a clear line between what can be made and what must be stocked.</p>')

    b.append(h2("local","14.1 Local anaesthetics"))
    b.append('<p><b>Lidocaine</b> is the workhorse local anaesthetic: an amide that blocks nerve sodium channels, numbing a small area for stitching, lancing or minor surgery '+c(67)+'. It is on the WHO Essential Medicines List '+c(67)+'. You cannot synthesise it in a collapse - <b>stockpile it</b>. Know the safe limits: plain lidocaine up to about <b>4.5 mg/kg (max ~300 mg)</b>, or <b>7 mg/kg (max ~500 mg)</b> with epinephrine; overdose causes seizures and cardiac arrest '+c(67)+'. Its older cousin procaine (Novocain) dates to 1905 '+c(67)+'. If you have <b>nothing</b>, the historical field fallbacks are crude but real: <b>cold</b> (ice/snow to numb an area) and firm <b>pressure/nerve compression</b> - far inferior, but better than nothing for the briefest procedures.</p>')

    b.append(h2("general","14.2 General anaesthesia - history and hazards"))
    b.append(fig(d_ether(), "Diethyl ether is the one general anaesthetic with a genuinely old, published, small-scale synthesis - and it is frighteningly dangerous to make and use."))
    b.append('<p><b>Diethyl ether</b> was first made by Valerius Cordus around 1540 by distilling ethanol with sulfuric acid, and was the first widely successful surgical anaesthetic - publicly demonstrated by Morton in Boston in 1846 (Crawford Long had used it in 1842) '+c(69,70)+'. The published preparation is acid-catalysed dehydration: ethanol plus sulfuric acid, held near <b>140 C</b> (classically about 5 parts alcohol to 9 parts concentrated sulfuric acid, distilling off the ether) '+c(68,69)+'. Above ~140 C the reaction instead makes ethene '+c(68)+'.</p>')
    b.append(danger("Ether is extraordinarily dangerous", "Ether vapour has a flash point below room temperature and forms explosive mixtures with air - a spark or flame near the still can detonate it. On storage it slowly forms shock-sensitive peroxides that can explode. And dosing an anaesthetic by guesswork risks killing the patient. This is documented history, not a recommended home procedure "+c(69)+"."))
    b.append('<p><b>Chloroform</b> followed ether but is more dangerous: it can trigger fatal heart rhythms and liver damage. The teenager Hannah Greener died under chloroform in 1848; John Snow traced such deaths to vapour that was too concentrated and stressed careful dilution and gradual induction '+c(72,71)+'. <b>Ketamine</b> is the modern collapse-relevant anaesthetic - a WHO essential medicine, cheap, with a wide safety margin that preserves breathing and blood pressure, and not under international narcotic control '+c(73)+' - but it is a manufactured drug you can only <b>stockpile</b>, stored securely.</p>')

    b.append(h2("otherabx","14.3 Antibiotics beyond penicillin"))
    b.append('<p>Penicillin (Parts 4-7) is only one family. The others matter, and most cannot be made at home:</p>')
    b.append(ul([
        "<b>Sulfonamides</b> were the first broadly effective antibacterials: Gerhard Domagk showed the dye Prontosil cured streptococcal infection in mice (1932) and people, published 1935; the active part, sulfanilamide, had been synthesised back in 1908 "+c(74)+". They are synthesised drugs - stockpile.",
        "<b>Streptomycin</b>, the first drug to treat tuberculosis, was isolated in 1943 by Albert Schatz in Selman Waksman's lab from the soil actinomycete <i>Streptomyces griseus</i> "+c(75)+". Like penicillin it comes from fermentation - but purifying an injectable, correctly dosed aminoglycoside from a soil microbe is far beyond kitchen means.",
        "<b>Most antibiotics</b> (cephalosporins, tetracyclines, macrolides, metronidazole, ciprofloxacin and the rest) are industrial fermentation or synthesis products. The realistic plan is to <b>stockpile a broad set</b>, stored cool and dry, and use them correctly and sparingly "+c(1)+".",
    ]))
    b.append(danger("Do not take 'fish' or other animal antibiotics", "Antibiotics sold for aquarium fish, birds or livestock are NOT approved for human use. They are not held to human standards for purity, potency, dose or labelling; taking them risks the wrong drug or dose, contamination, delayed proper care, and resistance "+c(76)+". They are not a safe substitute for human antibiotics."))

    b.append(h2("cantmake","14.4 Honest limits: what truly cannot be made outside a factory"))
    b.append('<p>To be rigorous: in a realistic collapse, with no pharmaceutical plant, you <b>cannot</b> safely produce injectable antibiotics, insulin, epinephrine, lidocaine, ketamine, oxytocin, chlorhexidine, povidone, concentrated hydrogen peroxide, modern IV fluids, or pure chloroform/ether at clinical quality. What you realistically CAN do: make and dilute <b>chlorine and alcohol antiseptics</b>, buffer <b>Dakin\'s solution</b>, prepare <b>iodine</b> from stocked crystals, <b>sterilise instruments with heat</b>, mix <b>ORS</b>, make <b>wound-rinse saline</b>, use <b>honey and willow</b>, and attempt <b>crude topical penicillin</b> as a last resort. Everything else is a stockpile decision made now, before it is needed. Store it cool, dark, dry and rotated '+c(1,2)+'.</p>')

    # ---------- Part 15: Synthesising Medicines in an Equipped Lab ----------
    b.append(part("p15","Part 15","Synthesising Medicines in an Equipped Lab"))
    b.append('<p class="tierB" style="font-weight:600">This whole chapter is <b>Tier B</b>: it assumes a working chemistry lab with fume extraction, glassware, heat, cooling and reagents. Its real purpose is <b>knowledge retention</b> &mdash; if the thread of industrial chemistry were ever broken, these are the published routes by which humanity first made its most important medicines. None of this is a kitchen project, and several steps honestly need an entire chemical industry standing behind them. Where that is true, this chapter says so plainly.</p>')
    b.append(danger("Read this before any synthesis","Every route below uses corrosive acids, toxic or flammable reagents, and reactions that give off heat and gas. Work only with proper ventilation, eye and skin protection, the right glassware, and the original published procedure in front of you. A survival guide can preserve the knowledge; it cannot make the chemistry safe. Do not attempt dosing any product in people or animals."))

    b.append(h2("slab","15.1 The lab, and how you prove a drug is pure"))
    b.append('<p>A medicine is only as safe as it is pure. Four classic techniques, needing no electronics, let a chemist make and check a drug:</p>')
    b.append(ul([
        "<b>Distillation</b> &mdash; separating liquids by boiling point (how ether, ethanol, nitric acid and solvents are purified).",
        "<b>Recrystallisation</b> &mdash; dissolving a crude solid in the minimum hot solvent, then cooling so pure crystals form while impurities stay in solution. This is the workhorse purification for nearly every solid drug below "+c(93)+".",
        "<b>Melting point</b> &mdash; a pure solid melts sharply at a known temperature; a wide or low melting range signals impurity. Benzocaine melts near 92 C "+c(86)+", paracetamol near 169-171 C "+c(93,94)+", aspirin near 135-136 C "+c(50)+".",
        "<b>Thin-layer chromatography (TLC)</b> &mdash; a drop of product on a coated plate, run in solvent, shows whether one compound or several are present. Column chromatography scales the same idea up.",
    ]))
    b.append('<p>You also need: a heat source and water/ice baths, round-bottom flasks and condensers, a separatory funnel, a Buchner funnel and vacuum for filtration, a balance, pH paper, and above all a <b>fume hood</b>.</p>')

    b.append(h2("sprec","15.2 The precursor chain"))
    b.append(fig(d_precursor(), "Follow any medicine back and you reach salt, air, water, sulfur, limestone, coal tar, ethanol or plant bark. The hard part is the middle: the bulk acids, bases and reagents that only heavy industry makes cheaply."))

    b.append(h2("schem","15.3 Supporting chemistry: the acids, bases and feedstocks"))
    b.append('<p>None of the drugs below can be made without these bulk chemicals. They are the true foundation &mdash; and most need industrial plant, which is the honest limit of self-sufficiency.</p>')
    b.append(ul([
        "<b>Sulfuric acid</b> (the esterifications, nitrations, chlorosulfonations): the modern <b>contact process</b> burns sulfur to SO2, oxidises it to SO3 over a vanadium(V) oxide catalyst near 450 C, then absorbs it into acid "+c(100)+". The older <b>lead-chamber process</b> used nitrogen-oxide catalysis to give a weaker (~65%) acid and can be built more simply "+c(100)+".",
        "<b>Nitric acid</b> (nitration, making p-aminophenol feedstock): the <b>Ostwald process</b> oxidises ammonia over platinum-rhodium gauze to NO, then to NO2, absorbed in water "+c(100)+".",
        "<b>Hydrochloric acid</b>: a by-product of many of these processes, or from salt + sulfuric acid; used in hydrolyses and salt formation.",
        "<b>Sodium hydroxide and sodium carbonate</b> (neutralisations, Kolbe-Schmitt, soap): the <b>chloralkali</b> electrolysis of brine gives NaOH, chlorine and hydrogen together "+c(101)+"; soda ash comes from the <b>Solvay process</b> (brine + ammonia + CO2), which replaced the older polluting <b>Leblanc process</b> "+c(102)+".",
        "<b>Ammonia</b> (nitric acid, sulfonamides, many intermediates): the <b>Haber-Bosch process</b> combines nitrogen from air with hydrogen over a promoted iron catalyst at roughly 400-500 C and 150-300 bar "+c(103)+". This single reaction underpins both fertiliser and much of pharmaceutical chemistry, and it genuinely needs high-pressure industrial plant.",
        "<b>Phenol</b> (salicylic acid, paracetamol feedstock, antiseptic history): historically distilled from <b>coal tar</b> (caustic-soda extraction of the carbolic fraction); today almost all comes from the <b>cumene process</b> "+c(105)+".",
        "<b>Ethanol, acetic acid and acetic anhydride</b> (esterifications, acetylations): ethanol by fermentation and distillation (see Food Preservation guide); acetic anhydride is an industrial product and is itself a controlled precursor in many places.",
        "<b>Elemental iodine</b> (antiseptics, Lugol's): historically leached from burnt <b>kelp ash</b> and liberated with sulfuric acid and an oxidiser; today mostly from <b>Chilean caliche</b> (iodate reduced with sulfite) or from iodide-rich brines "+c(104)+".",
    ]))
    b.append(danger("Concentrated acids and reactive reagents","Concentrated sulfuric, nitric and hydrochloric acids cause severe burns and react violently with water (always add acid to water, never the reverse). Nitrations are exothermic and can run away or explode if overheated. Chlorine and ammonia are toxic gases. Treat every one with the respect an industrial chemist would."))

    b.append(h2("sloc","15.4 Local anaesthetics"))
    b.append('<p>The ester and amide local anaesthetics are among the most achievable synthetic drugs, which is why two of them are standard undergraduate preparations.</p>')
    b.append('<p><b>Benzocaine</b> (ethyl 4-aminobenzoate) &mdash; the classic <b>Fischer esterification</b>: reflux <i>p</i>-aminobenzoic acid (PABA) in excess 95% ethanol with a little concentrated sulfuric acid for about 60-75 minutes, cool, then neutralise carefully with sodium carbonate to pH 9 so the free base precipitates; recrystallise from ethanol/water. Pure benzocaine melts at ~92 C '+c(86)+'.</p>')
    b.append('<p><b>Procaine</b> (Novocaine) &mdash; Alfred Einhorn\'s 1905 route does <b>not</b> esterify PABA directly. It starts from <i>p</i>-nitrobenzoic acid, converts it to the acid chloride, esterifies that with 2-(diethylamino)ethanol to give "nitrocaine", then <b>reduces the nitro group</b> (historically tin + HCl) to the amine, giving procaine '+c(89,90)+'. Benzocaine and procaine were the first safe synthetic replacements for cocaine as a local anaesthetic '+c(90)+'.</p>')
    b.append('<p><b>Lidocaine</b> (the modern amide workhorse) &mdash; Nils L&ouml;fgren\'s two-step 1943 route:</p>')
    b.append(steps([
        "<b>Chloroacetylation:</b> dissolve 2,6-dimethylaniline (2,6-xylidine) in glacial acetic acid, cool to ~10 C, and add chloroacetyl chloride slowly with stirring; add sodium acetate solution to precipitate 2-chloro-N-(2,6-dimethylphenyl)acetamide (the chloroamide) "+c(87,88)+".",
        "<b>Amination:</b> reflux the chloroamide with excess diethylamine in toluene for several hours; the diethylamine displaces the chloride. Filter off the diethylammonium chloride, wash, dry, and remove the toluene "+c(87,88)+".",
        "<b>Salt formation:</b> treat the free base with ethereal hydrogen chloride to give water-soluble lidocaine hydrochloride; recrystallise and check purity "+c(87,88)+".",
    ]))
    b.append(danger("Chloroacetyl chloride and 2,6-xylidine","Chloroacetyl chloride is corrosive, reacts violently with water, and its liquid and vapour are acutely harmful &mdash; use a fume hood and cooling throughout. 2,6-Xylidine is toxic. These steps are routine in a teaching lab only because of that equipment "+c(87)+"."))

    b.append(h2("ssulfa","15.5 Sulfonamides"))
    b.append('<p>The sulfa drugs were the first broadly effective antibacterials (Domagk\'s Prontosil, 1932-35) '+c(74)+', and sulfanilamide is a classic multi-step undergraduate synthesis from <b>acetanilide</b>:</p>')
    b.append(steps([
        "<b>Chlorosulfonation:</b> add chlorosulfonic acid to dry acetanilide (the acetyl group protects the amine and directs to the para position); the mixture gives off HCl gas and, on pouring onto ice, precipitates <i>p</i>-acetamidobenzenesulfonyl chloride, m.p. ~140 C "+c(91,92)+".",
        "<b>Amidation:</b> treat the sulfonyl chloride with concentrated aqueous ammonia to form <i>p</i>-acetamidobenzenesulfonamide "+c(91,92)+".",
        "<b>Hydrolysis:</b> reflux in dilute HCl to remove the acetyl group (the sulfonamide survives), then neutralise with sodium carbonate/bicarbonate to precipitate sulfanilamide; recrystallise "+c(91,92)+".",
    ]))
    b.append('<p><b>Sulfapyridine and sulfadiazine</b> follow the same first two steps, but the sulfonyl chloride is condensed with 2-aminopyridine or 2-aminopyrimidine instead of ammonia before the final deprotection &mdash; giving the longer-acting sulfonamides used for pneumonia and wound infection '+c(92)+'.</p>')
    b.append(danger("Chlorosulfonic acid","Chlorosulfonic acid is one of the most aggressive reagents in this guide: it reacts explosively with water, fumes HCl, and causes severe burns. The classic procedure is done behind a hood with a gas trap and careful quenching onto ice "+c(92)+"."))

    b.append(h2("sanalg","15.6 Analgesics and antipyretics"))
    b.append('<p><b>Salicylic acid</b> (the parent of aspirin, and an antiseptic/keratolytic itself) &mdash; the industrial <b>Kolbe-Schmitt reaction</b>: dry sodium phenoxide (from phenol + NaOH) is heated with carbon dioxide under pressure (classically ~100 C to absorb CO2, then ~120-160 C under several atmospheres), and the product is acidified to salicylic acid '+c(95)+'.</p>')
    b.append('<p><b>Aspirin</b> (acetylsalicylic acid) is then made by acetylating salicylic acid with acetic anhydride and a trace of acid &mdash; covered step by step in <b>Part 9</b>; check purity with the ferric-chloride test and a melting point near 135-136 C '+c(50,51)+'.</p>')
    b.append('<p><b>Paracetamol / acetaminophen</b> &mdash; the simple, high-yield step is <b>acetylation of <i>p</i>-aminophenol</b>: dissolve <i>p</i>-aminophenol in water, add acetic anhydride, warm (~70-80 C) with stirring for ~10 minutes, cool in ice to crystallise, filter and recrystallise from hot water; pure paracetamol melts at ~169-171 C '+c(93,94)+'. The harder part is making the <i>p</i>-aminophenol feedstock, classically from phenol by <b>nitration</b> to nitrophenol and <b>reduction</b>, or from nitrobenzene &mdash; steps that need nitric acid and controlled reductions '+c(93)+'.</p>')

    b.append(h2("squin","15.7 Antimalarial: quinine from cinchona bark"))
    b.append('<p>Malaria is a mass killer, and quinine is the one great antimalarial you can <b>extract</b> rather than synthesise. The total synthesis of quinine is a famous feat of chemistry but is hopelessly impractical outside a research lab &mdash; so the survival route is extraction from <b>cinchona bark</b> '+c(96)+'.</p>')
    b.append(steps([
        "Macerate dried, powdered cinchona bark with milk of lime (calcium hydroxide) and a little caustic soda to free the alkaloids from their salts "+c(97)+".",
        "Extract the freed alkaloids into a solvent (historically hot toluene or alcohol), warming and repeating to pull out as much as possible "+c(97)+".",
        "Shake the solvent with dilute acid (HCl or sulfuric) to move the alkaloids into the water layer as their salts; separate "+c(96,97)+".",
        "Raise the pH, filter and dry the crude alkaloid; purify by charcoal treatment and fractional crystallisation (quinine sulfate crystallises well) "+c(96,97)+".",
    ]))
    b.append(caution("Dosing and other alkaloids","Cinchona bark contains several alkaloids (quinine, quinidine, cinchonine) in varying amounts, so potency varies batch to batch and overdose (cinchonism: ringing ears, vision changes, heart effects) is a real danger. This is knowledge retention, not a license to self-dose "+c(96)+"."))

    b.append(h2("schlor","15.8 Antibiotics: the one you can synthesise, and the ones you cannot"))
    b.append('<p><b>Chloramphenicol</b> is the great exception: the first naturally occurring antibiotic to be made entirely by chemical synthesis, by Mildred Rebstock at Parke-Davis in 1949 '+c(98)+'. The classic industrial route starts from <b><i>p</i>-nitroacetophenone</b>: brominate it, convert the bromide to an amino-ketone, acetylate, condense with formaldehyde to add the second carbon-oxygen arm, reduce the ketone, resolve the active <i>threo</i> isomer, and finally attach the dichloroacetyl group '+c(98,99)+'. It is a genuine multi-step synthesis &mdash; achievable in a real lab, and worth preserving because it needs no fermentation.</p>')
    b.append(caution("Chloramphenicol\'s real risks","Chloramphenicol can cause fatal aplastic anaemia and, in newborns, grey-baby syndrome. It is a reserve antibiotic for good reason "+c(99)+"."))
    b.append('<p><b>Penicillin</b> is made by fermentation &mdash; see Parts 4-7. <b>Streptomycin and the tetracyclines</b> likewise come from culturing soil microbes (<i>Streptomyces</i>) and then purifying a correctly dosed, injectable product '+c(75)+'. Growing the mould or actinomycete is conceivable; reliably purifying and dosing the drug is the part that defeats a home lab. Most other antibiotics are industrial synthesis or fermentation products &mdash; the honest plan for them is the stockpile (Part 13.4).</p>')

    b.append(h2("sbio","15.9 Knowledge retention: insulin, epinephrine, oxytocin"))
    b.append('<p>These three keep people alive and sit at the edge of what any post-collapse chemist could do. The routes are recorded here so the knowledge is not lost &mdash; with an honest note on what each truly needs.</p>')
    b.append(ul([
        "<b>Insulin.</b> In 1921 Banting and Best extracted insulin from animal pancreas: tie off the pancreatic duct so the digestive tissue wastes away, then extract the surviving islet tissue (chilled, acid-alcohol) and inject it "+c(106)+". <b>Animal-pancreas extraction is the only remotely field-possible route</b>, and even that needs cold, careful purification and a way to judge potency. Modern insulin is <b>recombinant</b>: the human gene is expressed in <i>E. coli</i> or yeast, which needs molecular biology, fermentation and chromatography &mdash; a full biotech industry "+c(106)+".",
        "<b>Epinephrine (adrenaline).</b> Jokichi Takamine first crystallised it from adrenal glands in 1901 "+c(107)+"; Friedrich Stolz then synthesised it (via adrenalone) in 1904-06, making manufacture possible "+c(107)+". Extraction from animal adrenal glands is the historical field route; the synthesis is achievable in a real lab but the drug degrades fast and must be kept cold and dark.",
        "<b>Oxytocin</b> (for postpartum bleeding, Part 13.3). Vincent du Vigneaud achieved the <b>first synthesis of a peptide hormone</b> in 1953 &mdash; building the nine-amino-acid chain and closing its disulfide ring &mdash; winning the 1955 Nobel Prize "+c(108)+". Peptide synthesis needs protected amino acids and careful coupling; it is firmly industrial, so oxytocin (and heat-stable carbetocin) stay stockpile items.",
    ]))

    b.append(h2("slim","15.10 Honest limits"))
    b.append('<p>To be rigorous about this entire chapter: with a <b>real but isolated lab</b> and the bulk reagents already in hand, a trained chemist could plausibly make <b>benzocaine, procaine, lidocaine, sulfanilamide, salicylic acid, aspirin, paracetamol and chloramphenicol</b>, and <b>extract quinine</b> from bark. What defeats even a good lab without industry behind it: making the <b>bulk acids, ammonia and phenol</b> at scale, producing <b>injectable-grade purity and sterility</b>, and anything <b>biological</b> &mdash; insulin, epinephrine and oxytocin at clinical quality, and reliable antibiotics by fermentation. For all of those, the realistic answer remains: understand the route, keep the knowledge, and <b>stockpile the finished drug</b> while it can still be bought '+c(1,2)+'. Excluded by design throughout: opioids and poppy processing, any controlled-drug synthesis (including ketamine), and any dosing experiments on people or animals.</p>')

    # ---------- Part 16: Region ----------
    b.append(part("p16","Part 16","Region by Region"))
    b.append('<p>Where to find willows and other useful plants, and what storage challenge each region brings.</p>')
    b.append(regions_html(R))

    # ---------- Appendix ----------
    b.append(part("srcs","Appendix","Quick Reference & Sources"))
    b.append(table(["Item","Value"],[
        ["Medicine storage","Cool, dry, dark; not the bathroom "+c(1)],
        ["Expired solid tablets","Often largely potent past date if sealed/cool; variable "+c(4,6)],
        ["Goes bad: insulin","Fridge; ~28 days at room temp; never frozen "+c(7)],
        ["Goes bad: nitroglycerin","Amber glass, tightly capped, cool "+c(9,10)],
        ["WHO ORS","1 L water + ½ tsp salt + 6 tsp sugar "+c(20)],
        ["No honey for","Infants under 1 year (botulism) "+c(48)],
        ["Sepsis red flags","Confusion, fast breathing, red streak, fever+chills "+c(15,17)],
        ["Penicillin surface culture","~20–24 °C, ~6–7 days; filter; keep cold "+c(27)],
        ["Penicillin precursor (lab)","Phenylacetic acid, fed in small doses "+c(30,31)],
        ["Willow dose (evidence)","120–240 mg salicin/day for back pain "+c(37)],
        ["Willow: never for","Children/teens, bleeding, ulcers, aspirin allergy, pregnancy "+c(33,35)],
        ["Aspirin purity checks","FeCl3 test negative; m.p. ~135–136 °C "+c(50,51)],
        ["Deadly look-alikes","Poison & water hemlock; avoid Asarum "+c(46,47)]]))
    b.append('<p class="small">General information for emergencies when no professional medical care is available. It is not medical advice and does not replace a clinician, pharmacist or real medicine where any is reachable. Sources checked November 2026.</p>')
    b.append('<h2>Photo credits</h2>')
    b.append('<p class="small">All photographs are from Wikimedia Commons under their stated licenses; CC BY and CC BY-SA licenses require attribution, given in each caption (see creativecommons.org/licenses). Images were resized for print but not otherwise altered. Each file\'s page is at commons.wikimedia.org/wiki/File:&lt;file name&gt;. Köhler and other historical botanical plates, where used, are in the public domain.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Medicine & Remedies", "Survival Info<br>Medicine &amp;<br>Remedies",
          "Stockpiling and storing medicines; the history and hard limits of making penicillin; willow bark and other evidence-backed plant painkillers; infection, sepsis and rehydration — DIY across North America, with honest warnings and every claim sourced.",
          "Medicine & Remedies", TOC, cover_art(), "Medical &amp; First Aid · Sanitation · Food · Gardening · Preservation")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Medicine.pdf")
