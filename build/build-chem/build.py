import sys, math, csv, os
sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *

def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

EXTRA_CSS = """<style>
.rx{background:#eef3f6;border:1px solid #aebfc9;border-left:6px solid #37474f;border-radius:6px;padding:7px 12px;margin:9px 0;font-size:12pt;break-inside:avoid}
.rx .eq{font-family:'DejaVu Sans Mono',monospace;font-size:12.5pt;font-weight:700;color:#102027}
.rx .nt{font-size:10.5pt;color:#37474f;margin-top:3px}
.tierA{border-left:6px solid #2e7d32;background:#eaf6ea;padding:2px 12px;border-radius:5px;margin:8px 0}
.tierB{border-left:6px solid #1565c0;background:#eaf2fb;padding:2px 12px;border-radius:5px;margin:8px 0}
.tierC{border-left:6px solid #6a1b9a;background:#f3eafb;padding:2px 12px;border-radius:5px;margin:8px 0}
.tierA>h3,.tierB>h3,.tierC>h3{margin:9px 0 4px}
.tag{display:inline-block;font-size:9pt;font-weight:700;border-radius:4px;padding:1px 7px;color:#fff}
.tag.a{background:#2e7d32}.tag.b{background:#1565c0}.tag.c{background:#6a1b9a}
.pat{border:1px solid #c3ccd2;border-radius:7px;padding:7px 11px;margin:8px 0;background:#fff;break-inside:avoid}
.pat .no{font-weight:800;color:#102027}
.pat .ti{font-weight:600}
.pat .mt{font-size:10pt;color:#51606a;margin:2px 0}
.pat .st{display:inline-block;font-size:8.5pt;font-weight:700;border-radius:4px;padding:1px 6px;color:#fff;margin-left:4px}
.pat .st.exp{background:#546e7a}.pat .st.live{background:#c62828}
.dual{background:#fff8e1;border:1px solid #e0b400;border-left:6px solid #e0b400;border-radius:6px;padding:6px 12px;margin:8px 0;font-size:11pt}
</style>"""

def rx(eq, note=""):
    n = f'<div class="nt">{note}</div>' if note else ""
    return f'<div class="rx"><span class="eq">{eq}</span>{n}</div>'
def tierA(h, body): return f'<div class="tierA"><h3><span class="tag a">TIER A</span> {h}</h3>{body}</div>'
def tierB(h, body): return f'<div class="tierB"><h3><span class="tag b">TIER B</span> {h}</h3>{body}</div>'
def tierC(h, body): return f'<div class="tierC"><h3><span class="tag c">TIER C</span> {h}</h3>{body}</div>'
def dual(b): return f'<div class="dual"><b>Dual-use note.</b> {b}</div>'

# ---- patents ----
PATENTS = []
with open('/workspace/survival-info/build-chem/patents_manifest.tsv') as f:
    for row in csv.reader(f, delimiter='\t'):
        if len(row) >= 9:
            PATENTS.append(dict(num=row[0],tier=row[2],status=row[3],grant=row[4],inv=row[5],title=row[6],supports=row[7],figs=row[8]))

def pat_card(p):
    live = "live" if "force" in p["status"].lower() else "exp"
    return (f'<div class="pat"><span class="no">{p["num"]}</span> &mdash; <span class="ti">{p["title"]}</span>'
            f'<span class="st {live}">{p["status"]}</span>'
            f'<div class="mt">{p["inv"]} &middot; granted {p["grant"]}</div>'
            f'<div class="mt"><b>Teaches / supports:</b> {p["supports"]}</div>'
            f'<div class="mt"><b>Figures worth copying:</b> {p["figs"]}</div></div>')

def pats_in_tier(tier): return "".join(pat_card(p) for p in PATENTS if p["tier"]==tier)

# ---------------- cover ----------------
def cover_art():
    s = '<rect width="720" height="380" fill="#eaf1f4"/>'
    # distillation set-up silhouette
    s += '<polygon points="120,150 150,150 175,300 95,300" fill="#d6e8ef" stroke="#37474f" stroke-width="3"/>'
    s += '<rect x="122" y="138" width="26" height="14" fill="#90a4ae"/>'
    s += '<path d="M135 300 h0" />'
    s += '<path d="M60 280 h150 l-10 24 h-130 Z" fill="#ef9a9a"/>'  # heat source
    # condenser (angled)
    s += '<path d="M150 150 L360 90" stroke="#37474f" stroke-width="12" fill="none" stroke-linecap="round"/>'
    s += '<path d="M150 150 L360 90" stroke="#b3e5fc" stroke-width="6" fill="none" stroke-linecap="round"/>'
    # receiving flask
    s += '<polygon points="360,90 388,96 404,200 320,210" fill="#cfe8d0" stroke="#2e7d32" stroke-width="3"/>'
    # retort (round bottom with neck) on right
    s += '<circle cx="560" cy="250" r="60" fill="#d6e8ef" stroke="#37474f" stroke-width="3"/>'
    s += '<path d="M600 215 Q660 180 650 150" stroke="#37474f" stroke-width="10" fill="none" stroke-linecap="round"/>'
    s += '<path d="M600 215 Q660 180 650 150" stroke="#b3e5fc" stroke-width="5" fill="none" stroke-linecap="round"/>'
    s += '<path d="M512 258 a48 20 0 0 0 96 0 Z" fill="#a5d6a7"/>'
    for cx,cy in [(540,250),(560,244),(578,252),(566,262),(548,262)]: s += f'<circle cx="{cx}" cy="{cy}" r="6" fill="#2e7d32"/>'
    # flask icons top-left
    s += '<rect x="36" y="36" width="78" height="78" rx="10" fill="#6a1b9a"/>'
    s += '<path d="M60 52 h30 v16 l14 30 h-58 l14-30 Z" fill="#fff"/>'
    s += '<path d="M56 88 h42 l6 10 h-54 Z" fill="#ce93d8"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

# ---------------- diagrams ----------------
def d_tiers():
    s = t(375, 26, "Three tiers of sophistication \u2014 match the method to what you have", 17, "middle", "700")
    xs = [20, 260, 500]; cols = ["#eaf6ea","#eaf2fb","#f3eafb"]; strokes=["#2e7d32","#1565c0","#6a1b9a"]
    heads = ["TIER A \u2014 Improvised","TIER B \u2014 Workshop-built","TIER C \u2014 Industrial"]
    lines = [
      ["Fire, clay pots, scavenged jars","Wood ash, lime, salt, vinegar","Plant pH indicators","Pot-still spirits, soap, potash","Charcoal, crude lye, saltpetre beds"],
      ["Borosilicate glass, retorts","Thermometer, balance, pH paper","Bellows furnace, condensers","Distilled acids, electrolysis cells","Recrystallised reagents, titration"],
      ["Lead/stoneware chambers, towers","Contact & Ostwald catalysts","Haber-Bosch, chloralkali plant","Pressure vessels, vacuum pumps","Continuous fractionating columns"]]
    for i in range(3):
        s += rect(xs[i], 48, 210, 300, cols[i], strokes[i], 3, 10)
        s += t(xs[i]+105, 78, heads[i], 13.5, "middle", "800", strokes[i])
        for j,ln in enumerate(lines[i]):
            s += t(xs[i]+12, 112 + j*40, "\u2022 "+ln, 11, "start")
    s += t(375, 340, "Every tier is real chemistry. Higher tiers buy purity, yield and safety \u2014 not magic.", 11.5, "middle", "700", "#37474f")
    return svg(730, 360, s)

def d_glassware():
    s = t(375, 24, "Core glassware and improvised equivalents", 17, "middle", "700")
    items = [("Round-bottom flask","even heating","clay/copper pot"),
             ("Erlenmeyer flask","swirl, titrate","narrow jar"),
             ("Beaker","mixing","can, mug"),
             ("Condenser","recover vapour","coiled copper pipe"),
             ("Separatory funnel","liquid-liquid","jar + tap/siphon"),
             ("Buchner funnel","fast filtering","cloth over holed pot"),
             ("Graduated cylinder","volume","marked bottle"),
             ("Retort","distil solids","sealed pot + tube")]
    for i,(nm,use,imp) in enumerate(items):
        cx = 110 + (i%4)*180; cy = 70 + (i//4)*150
        s += rect(cx-80, cy, 160, 120, "#fff", "#37474f", 2, 8)
        s += t(cx, cy+24, nm, 12.5, "middle", "800", "#102027")
        s += t(cx, cy+48, "use: "+use, 10.5, "middle")
        s += t(cx, cy+78, "improvise:", 9.5, "middle", "700", "#2e7d32")
        s += t(cx, cy+96, imp, 10, "middle", "normal", "#2e7d32")
    return svg(730, 390, s)

def d_distill_simple():
    s = t(375, 22, "Simple distillation \u2014 one boiling point at a time", 16, "middle", "700")
    s += rect(70, 250, 120, 40, "#ef9a9a", "#b71c1c", 2, 6) + t(130, 275, "heat source", 11, "middle", "700")
    s += '<polygon points="95,170 165,170 185,250 75,250" fill="#d6e8ef" stroke="#37474f" stroke-width="2"/>'
    s += t(130, 300, "boiling flask", 10.5, "middle")
    s += '<path d="M60 150 l50 -8 a6 6 0 0 1 2 12 l-48 8 Z" fill="#fff" stroke="#37474f" stroke-width="2"/>'
    s += t(130, 140, "thermometer at side-arm = vapour temp", 10, "middle", "700", "#1565c0")
    # condenser
    s += '<path d="M165 172 L380 250" stroke="#90a4ae" stroke-width="18" fill="none" stroke-linecap="round"/>'
    s += '<path d="M165 172 L380 250" stroke="#b3e5fc" stroke-width="8" fill="none" stroke-linecap="round"/>'
    s += t(300, 150, "water-cooled condenser", 10.5, "middle", "700", "#0277bd")
    s += arrow(430, 300, 400, 258, "#0277bd", 2) + t(470, 310, "cooling water in", 9.5, "middle")
    s += arrow(250, 150, 285, 200, "#0277bd", 2) + t(230, 142, "water out", 9.5, "middle")
    # receiver
    s += '<polygon points="365,250 405,250 415,320 355,320" fill="#cfe8d0" stroke="#2e7d32" stroke-width="2"/>'
    s += t(385, 336, "receiver (distillate)", 10, "middle")
    return svg(730, 350, s)

def d_distill_frac():
    s = t(375, 22, "Fractional distillation \u2014 many 'plates' separate close boilers", 16, "middle", "700")
    s += rect(70, 250, 110, 36, "#ef9a9a", "#b71c1c", 2, 6) + t(125, 272, "heat", 11, "middle", "700")
    s += '<polygon points="95,200 155,200 172,250 78,250" fill="#d6e8ef" stroke="#37474f" stroke-width="2"/>'
    # column with packing
    s += rect(110, 70, 30, 130, "#eceff1", "#37474f", 2, 4)
    for y in range(80, 196, 14):
        s += line(112, y, 138, y+8, "#78909c", 2)
    s += t(125, 62, "packed column", 10, "middle", "700")
    s += t(230, 95, "Each theoretical plate = one", 10.5, "start")
    s += t(230, 112, "evaporation + condensation cycle.", 10.5, "start")
    s += t(230, 129, "More plates (taller/packed column)", 10.5, "start")
    s += t(230, 146, "= sharper split of close-boiling", 10.5, "start")
    s += t(230, 163, "liquids. >95% purity needs \u22653 plates", 10.5, "start")
    s += t(230, 180, "for a 20\u201330\u00b0C boiling-point gap.", 10.5, "start")
    # top condenser
    s += '<path d="M140 78 L330 150" stroke="#90a4ae" stroke-width="16" fill="none" stroke-linecap="round"/>'
    s += '<path d="M140 78 L330 150" stroke="#b3e5fc" stroke-width="7" fill="none" stroke-linecap="round"/>'
    s += '<polygon points="315,150 355,150 365,215 305,215" fill="#cfe8d0" stroke="#2e7d32" stroke-width="2"/>'
    s += t(335, 230, "light fraction", 10, "middle")
    return svg(730, 300, s)

def d_steam_distill():
    s = t(375, 22, "Steam distillation \u2014 recover heat-sensitive oils below 100\u00b0C", 16, "middle", "700")
    s += rect(50, 230, 110, 34, "#ef9a9a", "#b71c1c", 2, 6) + t(105, 251, "heat", 11, "middle", "700")
    s += '<polygon points="70,160 150,160 165,230 55,230" fill="#d6e8ef" stroke="#37474f" stroke-width="2"/>' + t(110, 250, "water boiler", 9.5, "middle")
    s += arrow(165, 150, 250, 150, "#78909c", 3) + t(205, 140, "steam", 9.5, "middle", "700")
    s += '<polygon points="250,150 330,150 345,235 235,235" fill="#e1f0d6" stroke="#558b2f" stroke-width="2"/>' + t(290, 250, "plant/aromatic charge", 9.5, "middle")
    s += '<path d="M345 150 L520 215" stroke="#90a4ae" stroke-width="16" fill="none" stroke-linecap="round"/>'
    s += '<path d="M345 150 L520 215" stroke="#b3e5fc" stroke-width="7" fill="none" stroke-linecap="round"/>'
    s += '<polygon points="505,215 550,215 560,285 495,285" fill="#fff" stroke="#37474f" stroke-width="2"/>'
    s += t(528, 258, "oil", 10, "middle", "700", "#8d6e63") + t(528, 274, "water", 9.5, "middle", "normal", "#0277bd")
    s += t(528, 300, "two layers separate", 9.5, "middle")
    s += t(375, 290, "Each component exerts its own vapour pressure, so the mix boils when the", 9.5, "middle", "normal", "#37474f")
    return svg(730, 320, s)

def d_recrystal():
    s = t(375, 22, "Recrystallisation \u2014 the workhorse solid purification", 16, "middle", "700")
    steps = [("1","Dissolve crude solid in the","minimum HOT solvent"),
             ("2","Hot-filter off insoluble","dirt and charcoal"),
             ("3","Cool slowly \u2014 pure crystals","grow, impurities stay dissolved"),
             ("4","Filter, wash cold, dry;","check melting point")]
    for i,(n,a,b) in enumerate(steps):
        x = 30 + i*175
        s += rect(x, 60, 150, 150, "#eef3f6", "#37474f", 2, 10)
        s += f'<circle cx="{x+24}" cy="86" r="15" fill="#6a1b9a"/>' + t(x+24, 91, n, 13, "middle", "800", "#fff")
        s += t(x+75, 120, a, 10, "middle")
        s += t(x+75, 138, b, 10, "middle")
        if i < 3: s += arrow(x+152, 135, x+173, 135, "#546e7a", 3)
    s += t(375, 234, "Yield is always <100%: some product stays in the mother liquor. Purity beats yield.", 11, "middle", "700", "#b71c1c")
    return svg(730, 254, s)

def d_extraction():
    s = t(375, 22, "Liquid\u2013liquid extraction \u2014 partition between two solvents", 16, "middle", "700")
    s += '<path d="M330 60 h90 v70 a45 45 0 0 1 -90 0 Z" fill="#fff" stroke="#37474f" stroke-width="2"/>'
    s += '<path d="M330 95 h90 v35 a45 45 0 0 1 -90 0 Z" fill="#cfe8d0" stroke="none"/>'
    s += '<rect x="330" y="60" width="90" height="35" fill="#e3f2fd"/>'
    s += '<path d="M370 168 l5 22 h4 l5 -22 Z" fill="#37474f"/>' + '<rect x="368" y="150" width="20" height="18" fill="#fff" stroke="#37474f" stroke-width="2"/>'
    s += t(500, 80, "organic layer (product)", 10.5, "start", "700", "#2e7d32")
    s += t(500, 112, "aqueous layer (salts, sugars)", 10.5, "start", "700", "#1565c0")
    s += t(120, 110, "K = [solute]organic", 12, "middle", "700")
    s += line(70, 118, 170, 118, "#37474f", 1)
    s += t(120, 134, "[solute]aqueous", 12, "middle", "700")
    s += t(120, 170, "Several small washes", 10.5, "middle")
    s += t(120, 186, "beat one big one.", 10.5, "middle")
    return svg(730, 210, s)

def d_tlc():
    s = t(375, 22, "Thin-layer chromatography \u2014 is it one compound or several?", 16, "middle", "700")
    s += rect(80, 60, 150, 190, "#fff", "#37474f", 2, 6)
    s += line(90, 220, 220, 220, "#90a4ae", 1)  # origin
    s += t(155, 238, "origin (spot here)", 9, "middle")
    s += line(90, 80, 220, 80, "#90a4ae", 1, "4 3")
    s += t(155, 74, "solvent front", 9, "middle")
    for sx,sy,col in [(120,150,"#6a1b9a"),(160,120,"#2e7d32"),(200,175,"#c62828")]:
        s += f'<ellipse cx="{sx}" cy="{sy}" rx="9" ry="6" fill="{col}"/>'
    s += t(360, 90, "Rf = distance spot moved", 11.5, "start", "700")
    s += line(355, 98, 560, 98, "#37474f", 1)
    s += t(360, 116, "distance solvent moved", 11.5, "start", "700")
    s += t(360, 150, "A pure compound = one spot.", 10.5, "start")
    s += t(360, 168, "Rf is reproducible in a given", 10.5, "start")
    s += t(360, 186, "solvent and identifies a substance", 10.5, "start")
    s += t(360, 204, "against a known reference spot.", 10.5, "start")
    return svg(730, 260, s)

def d_titration():
    s = t(375, 22, "Titration \u2014 measuring concentration with a standard solution", 16, "middle", "700")
    s += rect(150, 55, 16, 150, "#e3f2fd", "#37474f", 2, 3)
    s += t(158, 48, "burette", 9.5, "middle", "700")
    s += t(230, 90, "known 'standard' solution", 10, "start")
    s += '<polygon points="120,210 196,210 210,285 106,285" fill="#f8d7e3" stroke="#c2185b" stroke-width="2"/>'
    s += t(158, 300, "sample + indicator", 9.5, "middle")
    s += t(430, 120, "At the endpoint the indicator", 10.5, "start")
    s += t(430, 138, "changes colour. Moles of titrant", 10.5, "start")
    s += t(430, 156, "added = moles of analyte (by the", 10.5, "start")
    s += t(430, 174, "balanced equation), so you back-", 10.5, "start")
    s += t(430, 192, "calculate the unknown concentration.", 10.5, "start")
    s += t(430, 224, "A primary standard (e.g. dried", 10.5, "start", "700", "#2e7d32")
    s += t(430, 242, "Na2CO3) is pure, stable, known mass.", 10.5, "start", "700", "#2e7d32")
    return svg(730, 300, s)

def d_ph():
    s = t(375, 22, "Plant pH indicators \u2014 colour across the scale", 16, "middle", "700")
    cols = ["#c62828","#e53935","#fb8c00","#fdd835","#7cb342","#2e7d32","#00897b","#1e88e5","#3949ab","#5e35b1"]
    for i,col in enumerate(cols):
        x = 40 + i*66
        s += rect(x, 70, 62, 54, col, "#fff", 1, 4)
        s += t(x+31, 142, str(i+1), 11, "middle", "700")
    s += t(375, 60, "Red-cabbage juice (anthocyanin): red in acid \u2192 purple neutral \u2192 green/yellow in base", 10.5, "middle", "normal", "#37474f")
    s += t(375, 172, "Litmus from boiled lichen: red in acid, blue in base. Turmeric: yellow \u2192 red above pH ~8.", 11, "middle", "normal", "#37474f")
    return svg(730, 190, s)

def d_limecycle():
    s = t(375, 22, "The lime cycle \u2014 limestone to quicklime to slaked lime and back", 16, "middle", "700")
    nodes = [("Limestone","CaCO\u2083",120,150,"#d7ccc8"),("Quicklime","CaO",375,80,"#ffe0b2"),("Slaked lime","Ca(OH)\u2082",630,150,"#dcedc8"),("Carbonated","CaCO\u2083",375,250,"#d7ccc8")]
    for nm,fo,x,y,col in nodes:
        s += f'<ellipse cx="{x}" cy="{y}" rx="78" ry="40" fill="{col}" stroke="#5d4037" stroke-width="2"/>'
        s += t(x, y-4, nm, 12, "middle", "800") + t(x, y+16, fo, 12, "middle", "700", "#5d4037")
    s += arrow(190, 130, 310, 95, "#b71c1c", 3) + t(250, 100, "heat ~900\u00b0C (\u2212CO\u2082)", 9.5, "middle", "700", "#b71c1c")
    s += arrow(445, 95, 560, 130, "#1565c0", 3) + t(505, 100, "+ H\u2082O", 9.5, "middle", "700", "#1565c0")
    s += arrow(600, 185, 445, 235, "#2e7d32", 3) + t(540, 230, "+ CO\u2082 (air)", 9.5, "middle", "700", "#2e7d32")
    s += arrow(300, 235, 180, 185, "#5d4037", 3) + t(235, 230, "mined again", 9.5, "middle")
    return svg(730, 300, s)

def d_niterbed():
    s = t(375, 22, "Nitre bed \u2014 nitrate from manure, ash and time (for medical/food/fertiliser use)", 15, "middle", "700")
    s += rect(60, 70, 300, 150, "#efebe9", "#5d4037", 2, 8)
    for i,ln in enumerate(["Layer manure, straw, wood ash,","old mortar/lime and earth.","Keep moist, shaded, aerated.","Soil bacteria oxidise ammonia","\u2192 nitrites \u2192 nitrates over months."]):
        s += t(75, 100 + i*24, ln, 11, "start")
    s += arrow(365, 150, 400, 150, "#546e7a", 3)
    s += rect(405, 70, 290, 150, "#eef3f6", "#37474f", 2, 8)
    for i,ln in enumerate(["Leach beds with water \u2192 liquor.","Boil with wood-ash lye (K\u2082CO\u2083):","Ca(NO\u2083)\u2082 + K\u2082CO\u2083 \u2192 2KNO\u2083 + CaCO\u2083\u2193.","Filter, evaporate, crystallise KNO\u2083.","Recrystallise for purity."]):
        s += t(420, 100 + i*24, ln, 10.5, "start")
    return svg(730, 236, s)

def d_wood_distill():
    s = t(375, 22, "Destructive distillation of wood \u2014 one retort, many products", 16, "middle", "700")
    s += rect(60, 90, 150, 110, "#bcaaa4", "#4e342e", 2, 8) + t(135, 80, "sealed retort (no air)", 9.5, "middle", "700")
    s += t(135, 130, "WOOD", 13, "middle", "800", "#3e2723") + t(135, 155, "heated 400\u2013500\u00b0C", 10, "middle")
    s += rect(60, 205, 150, 22, "#ef9a9a", "#b71c1c", 1, 4) + t(135, 221, "fire below", 10, "middle", "700")
    s += arrow(212, 120, 260, 120, "#546e7a", 3)
    outs = [("Charcoal","stays in retort","#424242"),("Wood gas","burns (fuel)","#90a4ae"),("Pyroligneous acid","\u2192 acetic acid, methanol, acetone","#8d6e63"),("Wood tar / creosote","wood preservative","#4e342e")]
    for i,(nm,d,col) in enumerate(outs):
        y = 80 + i*34
        s += f'<rect x="270" y="{y}" width="18" height="18" fill="{col}"/>'
        s += t(298, y+14, nm+" \u2014 "+d, 11, "start", "700")
    s += t(375, 236, "Redistil pyroligneous acid to separate methanol, acetone and acetic acid (the first industrial source).", 9.5, "middle", "normal", "#37474f")
    return svg(730, 256, s)

def d_leadchamber():
    s = t(375, 22, "Sulfuric acid \u2014 the lead-chamber process (Tier C, historical)", 16, "middle", "700")
    s += '<polygon points="60,250 60,150 110,110 110,250" fill="#eceff1" stroke="#37474f" stroke-width="2"/>'
    s += t(85, 265, "sulfur/pyrite\nburner", 9, "middle")
    s += arrow(110, 160, 170, 160, "#546e7a", 3) + t(140, 150, "SO\u2082", 9.5, "middle", "700")
    for i in range(3):
        x = 175 + i*150
        s += rect(x, 110, 130, 140, "#cfd8dc", "#455a64", 2, 6)
        s += t(x+65, 100, f"lead chamber {i+1}", 9.5, "middle", "700")
        s += t(x+65, 175, "SO\u2082 + NO\u2082", 10, "middle")
        s += t(x+65, 195, "+ H\u2082O + O\u2082", 10, "middle")
    s += t(375, 285, "NO/NO\u2082 oxides carry oxygen to SO\u2082; lead resists the acid. Product ~65% H\u2082SO\u2084 ('chamber acid').", 10, "middle", "normal", "#37474f")
    s += rx("2 SO\u2082 + O\u2082 + 2 H\u2082O \u2192 2 H\u2082SO\u2084", "NO\u2093 oxides are the catalyst, regenerated each cycle (Glover &amp; Gay-Lussac towers recover them).")
    return svg(730, 305, s)

def d_contact():
    s = t(375, 22, "Sulfuric acid \u2014 the contact process (modern, higher purity)", 16, "middle", "700")
    flow_items = ["Burn S \u2192 SO\u2082","Dry gas","V\u2082O\u2085 catalyst 400\u2013450\u00b0C","SO\u2082 \u2192 SO\u2083","Absorb in H\u2082SO\u2084 \u2192 oleum","Dilute \u2192 98% acid"]
    for i,it in enumerate(flow_items):
        x = 20 + i*118
        s += rect(x, 70, 108, 80, "#eef3f6", "#6a1b9a", 2, 8)
        for j,ln in enumerate(it.split(" ")):
            pass
        s += t(x+54, 108, it, 9.3, "middle", "600")
        if i<5: s += arrow(x+110, 110, x+118, 110, "#546e7a", 3)
    s += rx("2 SO\u2082 + O\u2082 \u21cc 2 SO\u2083   (\u0394H &lt; 0)", "Exothermic + reversible \u2192 moderate temperature and a catalyst give best conversion (Le Chatelier). SO\u2083 is absorbed into acid, not water, to avoid a mist.")
    return svg(730, 215, s)

def d_ostwald():
    s = t(375, 22, "Nitric acid \u2014 Ostwald process and the saltpetre route", 16, "middle", "700")
    s += rx("4 NH\u2083 + 5 O\u2082 \u2192 4 NO + 6 H\u2082O", "Pt/Rh gauze catalyst, ~900\u00b0C (ammonia from Haber\u2013Bosch).")
    s += rx("2 NO + O\u2082 \u2192 2 NO\u2082 ;  3 NO\u2082 + H\u2082O \u2192 2 HNO\u2083 + NO", "Cool, oxidise, absorb in water in towers.")
    s += rx("KNO\u2083 + H\u2082SO\u2084 \u2192 KHSO\u2084 + HNO\u2083\u2191", "Historical lab route: gently distil saltpetre with sulfuric acid; condense the nitric acid vapour. Glass/stoneware only \u2014 nitric attacks most metals.")
    return svg(730, 190, s)

def d_chloralkali():
    s = t(375, 22, "Chloralkali electrolysis \u2014 chlorine, hydrogen and caustic soda from brine", 15, "middle", "700")
    s += rect(120, 70, 480, 170, "#e3f2fd", "#1565c0", 2, 10)
    s += rect(350, 70, 20, 170, "#cfd8dc", "#607d8b", 2, 2) + t(360, 258, "diaphragm / membrane", 9, "middle")
    s += line(200, 90, 200, 230, "#424242", 5) + t(200, 250, "anode (+)", 9.5, "middle", "700")
    s += line(520, 90, 520, 230, "#424242", 5) + t(520, 250, "cathode (\u2212)", 9.5, "middle", "700")
    s += t(200, 60, "Cl\u2082 \u2191", 12, "middle", "700", "#2e7d32")
    s += t(520, 60, "H\u2082 \u2191", 12, "middle", "700", "#c62828")
    s += t(235, 160, "brine (NaCl)", 10, "start")
    s += t(430, 160, "NaOH forms here", 10, "start", "700", "#1565c0")
    s += rx("2 NaCl + 2 H\u2082O \u2192 Cl\u2082 + H\u2082 + 2 NaOH", "The diaphragm/membrane keeps chlorine and caustic apart so they do not react back.")
    return svg(730, 300, s)

def d_solvay():
    s = t(375, 22, "Solvay process \u2014 soda ash (Na\u2082CO\u2083) from salt and limestone", 16, "middle", "700")
    s += rx("CaCO\u2083 \u2192 CaO + CO\u2082   (lime kiln)")
    s += rx("NaCl + NH\u2083 + CO\u2082 + H\u2082O \u2192 NaHCO\u2083\u2193 + NH\u2084Cl", "CO\u2082 bubbled through ammoniated brine; sodium bicarbonate is least soluble and drops out.")
    s += rx("2 NaHCO\u2083 \u2192 Na\u2082CO\u2083 + H\u2082O + CO\u2082\u2191   (calcined)")
    s += rx("2 NH\u2084Cl + CaO \u2192 2 NH\u2083 + CaCl\u2082 + H\u2082O", "Ammonia is recovered and recycled \u2014 the elegance of the process. Compare the older Leblanc route (salt+H\u2082SO\u2084\u2192salt cake, then coal+limestone) which wastes HCl and sulfur.")
    return svg(730, 230, s)

def d_gasprep():
    s = t(375, 22, "Preparing and collecting common gases", 16, "middle", "700")
    rows = [("Chlorine Cl\u2082","MnO\u2082 + 4 HCl \u2192 MnCl\u2082 + Cl\u2082 + 2 H\u2082O","downward delivery; TOXIC","#2e7d32"),
            ("Hydrogen H\u2082","Zn + 2 HCl \u2192 ZnCl\u2082 + H\u2082","over water; FLAMMABLE","#c62828"),
            ("Oxygen O\u2082","2 H\u2082O\u2082 \u2192 2 H\u2082O + O\u2082 (MnO\u2082 cat.)","over water","#1565c0"),
            ("Carbon dioxide CO\u2082","CaCO\u2083 + 2 HCl \u2192 CaCl\u2082 + H\u2082O + CO\u2082","downward; denser than air","#6a1b9a")]
    for i,(nm,eq,coll,col) in enumerate(rows):
        y = 55 + i*58
        s += rect(20, y, 160, 48, "#fff", col, 2, 6) + t(100, y+20, nm, 11.5, "middle", "800", col) + t(100, y+40, coll, 9, "middle")
        s += rect(190, y, 520, 48, "#eef3f6", "#90a4ae", 1, 6)
        s += t(205, y+30, eq, 11.5, "start", "700")
    return svg(730, 300, s)

def d_ethanol():
    s = t(375, 22, "Ethanol \u2014 fermentation, distillation, and breaking the azeotrope", 15, "middle", "700")
    for i,(lab,sub) in enumerate([("Sugar/starch","mash + yeast"),("Fermented wash","~8\u201314% ethanol"),("Pot/column still","distil"),("95.6% azeotrope","constant-boiling"),("Dry with CaO/3\u00c5","anhydrous >99%")]):
        x = 20 + i*142
        s += rect(x, 60, 128, 74, "#eef3f6", "#2e7d32", 2, 8)
        s += t(x+64, 90, lab, 10.3, "middle", "700")
        s += t(x+64, 112, sub, 9.3, "middle")
        if i<4: s += arrow(x+130, 97, x+142, 97, "#546e7a", 3)
    s += rx("C\u2086H\u2081\u2082O\u2086 \u2192 2 C\u2082H\u2085OH + 2 CO\u2082", "Yeast; keep below ~35\u00b0C. Distillation alone cannot pass 95.6% ethanol \u2014 that is an azeotrope. Dry over quicklime (CaO) or molecular sieve, or use an entrainer (benzene historically; safer options exist), to reach anhydrous ethanol.")
    return svg(730, 215, s)

def d_ester():
    s = t(375, 22, "Named organic reactions \u2014 the toolbox behind the medicines", 15, "middle", "700")
    rows = [("Esterification","acid + alcohol \u21cc ester + water (acid catalyst)"),
            ("Saponification","ester + NaOH \u2192 soap (salt of fatty acid) + glycerol"),
            ("Nitration","ArH + HNO\u2083/H\u2082SO\u2084 \u2192 ArNO\u2082 + H\u2082O"),
            ("Reduction","ArNO\u2082 + [H] (Sn/Fe + acid) \u2192 ArNH\u2082 (aniline-type)"),
            ("Acetylation","ArNH\u2082/ArOH + (CH\u2083CO)\u2082O \u2192 amide/ester + acetic acid"),
            ("Diazotisation","ArNH\u2082 + HNO\u2082 (0\u20135\u00b0C) \u2192 ArN\u2082\u207a ; couple \u2192 azo dye")]
    for i,(nm,eq) in enumerate(rows):
        y = 50 + i*38
        s += rect(20, y, 180, 32, "#f3eafb", "#6a1b9a", 1, 6) + t(110, y+21, nm, 11, "middle", "800", "#6a1b9a")
        s += t(215, y+21, eq, 11, "start", "600")
    return svg(730, 290, s)

def d_aspirin():
    s = t(375, 22, "Worked example \u2014 aspirin from salicylic acid (acetylation)", 15, "middle", "700")
    for i,(lab,sub) in enumerate([("Salicylic acid","+ acetic anhydride"),("Warm ~85\u00b0C","few drops H\u2082SO\u2084/H\u2083PO\u2084 cat."),("Cool, add water","crystals form"),("Filter, recrystallise","from hot water/ethanol"),("Check purity","FeCl\u2083 \u2212ve; m.p. 135\u2013136\u00b0C")]):
        x = 20 + i*142
        s += rect(x, 58, 128, 78, "#fff", "#6a1b9a", 2, 8)
        s += t(x+64, 88, lab, 10.2, "middle", "700")
        s += t(x+64, 110, sub, 9.0, "middle")
        if i<4: s += arrow(x+130, 96, x+142, 96, "#546e7a", 3)
    s += rx("C\u2086H\u2084(OH)COOH + (CH\u2083CO)\u2082O \u2192 C\u2086H\u2084(OCOCH\u2083)COOH + CH\u2083COOH", "The phenol \u2013OH is acetylated. Theoretical yield from 10 g salicylic acid \u2248 13 g aspirin; expect less after recrystallisation.")
    return svg(730, 215, s)

def d_furnace():
    s = t(375, 22, "Heat sources, by temperature reached", 16, "middle", "700")
    bars = [("Candle / oil lamp",300,"#ffd54f"),("Wood fire",600,"#ffb74d"),("Charcoal + natural draft",900,"#ff8a65"),("Charcoal + forced bellows",1300,"#ff7043"),("Coke / blast furnace",1600,"#e64a19"),("Electric arc / kiln",2000,"#b71c1c")]
    maxw = 520
    for i,(nm,tC,col) in enumerate(bars):
        y = 55 + i*38
        w = int(maxw * tC/2000)
        s += t(20, y+18, nm, 11, "start", "700")
        s += rect(185, y, w, 26, col, "#546e7a", 1, 4)
        s += t(185+w+8, y+18, f"~{tC}\u00b0C", 10.5, "start", "700")
    s += t(375, 290, "Forced air (bellows/blower) is the single biggest upgrade: it turns a wood fire into a metal-melting forge.", 9.5, "middle", "normal", "#37474f")
    return svg(730, 305, s)

def d_patent_tiers():
    s = t(375, 24, "Patent library \u2014 lab & process equipment, by tier of sophistication", 15, "middle", "700")
    cols = [("TIER A","Improvised / simple","#2e7d32"),("TIER B","Workshop-built","#1565c0"),("TIER C","Industrial","#6a1b9a")]
    counts = {tt:sum(1 for p in PATENTS if p["tier"]==tt) for tt in ("A","B","C")}
    for i,(hd,sub,col) in enumerate(cols):
        x = 30 + i*230
        s += rect(x, 55, 210, 110, "#fff", col, 3, 10)
        s += t(x+105, 90, hd, 15, "middle", "800", col)
        s += t(x+105, 116, sub, 11, "middle")
        s += t(x+105, 146, f'{counts[["A","B","C"][i]]} patents', 12, "middle", "700")
    s += t(375, 192, "Every entry below lists number, title, inventor, grant date, likely status, what it teaches and the figures to copy.", 9.5, "middle", "normal", "#37474f")
    return svg(730, 210, s)

def d_bunsen():
    s = t(375, 22, "How a Bunsen burner works \u2014 air collar sets the flame", 16, "middle", "700")
    # base
    s += rect(150, 300, 150, 22, "#90a4ae", "#546e7a", 2, 4) + t(225, 316, "weighted base", 9.5, "middle")
    # gas inlet + needle valve
    s += line(300, 311, 380, 311, "#546e7a", 8) + t(430, 315, "gas inlet / needle valve (gas flow)", 10, "start", "700")
    # barrel (vertical tube)
    s += rect(212, 120, 26, 182, "#cfd8dc", "#455a64", 2, 3) + t(150, 210, "barrel", 10.5, "end", "700")
    # air collar with holes
    s += rect(204, 250, 42, 30, "#b0bec5", "#37474f", 2, 3)
    for hx in (210, 222, 234): s += f'<circle cx="{hx}" cy="265" r="4" fill="#263238"/>'
    s += t(430, 268, "air collar: rotate to open/close air holes", 10, "start", "700", "#1565c0")
    s += t(430, 286, "(more air = hotter blue flame; less = yellow)", 9.5, "start", "normal", "#1565c0")
    # flame cones
    s += '<path d="M225 120 C205 70 245 70 225 120 Z" fill="none"/>'
    s += '<path d="M212 120 Q225 28 238 120 Z" fill="#64b5f6" stroke="#1565c0" stroke-width="1.5"/>'
    s += '<path d="M219 120 Q225 70 231 120 Z" fill="#1565c0"/>'
    s += t(300, 60, "outer cone (complete combustion, ~1500\u00b0C)", 10, "start", "700", "#1565c0")
    s += t(300, 96, "inner cone (unburnt gas+air)", 10, "start", "normal", "#37474f")
    s += t(430, 210, "gas and air mix in the barrel, then burn at the top", 10, "start")
    return svg(730, 332, s)

def d_pressurecooker():
    s = t(375, 22, "Pressure cooker / autoclave \u2014 cutaway (the home steriliser)", 16, "middle", "700")
    # pot body
    s += rect(170, 120, 390, 190, "#cfd8dc", "#546e7a", 3, 10)
    # water level
    s += rect(176, 250, 378, 54, "#bbdefb", "none", 0, 0) + line(176, 250, 554, 250, "#1565c0", 2, "5 4")
    s += t(300, 244, "water (makes steam)", 9.5, "middle", "normal", "#1565c0")
    # rack
    s += line(210, 240, 520, 240, "#78909c", 4)
    for rx2 in range(230, 520, 40): s += line(rx2, 236, rx2, 244, "#78909c", 3)
    s += t(200, 232, "rack holds instruments above water", 9.5, "start", "700")
    # lid
    s += rect(160, 96, 410, 26, "#b0bec5", "#37474f", 3, 6)
    # gasket
    s += rect(168, 118, 394, 7, "#e53935", "none", 0, 2) + t(590, 124, "gasket (seal)", 9.5, "start", "700", "#b71c1c")
    # lid lock / clamp
    s += rect(150, 92, 16, 34, "#455a64", "#263238", 2, 2) + rect(564, 92, 16, 34, "#455a64", "#263238", 2, 2)
    s += t(120, 88, "lid lock", 9.5, "middle", "700")
    # weighted regulator
    s += rect(300, 74, 40, 22, "#424242", "#000", 1, 3) + line(320, 96, 320, 86, "#424242", 4)
    s += t(360, 80, "weighted pressure regulator (rocks & vents at set pressure)", 9.5, "start", "700")
    # safety valve
    s += f'<circle cx="430" cy="86" r="9" fill="#ef6c00" stroke="#000"/>' + t(448, 72, "safety / relief valve", 9.5, "start", "700", "#ef6c00")
    s += t(375, 326, "Trapped steam raises the boiling point to ~121\u00b0C at ~15 psi \u2014 hot enough to sterilise. Relief valve prevents over-pressure.", 9.5, "middle", "normal", "#37474f")
    return svg(730, 344, s)

def d_electrolysis():
    s = t(375, 22, "A simple electrolysis cell \u2014 splitting a compound with current", 16, "middle", "700")
    # power source
    s += rect(40, 150, 70, 60, "#fff", "#37474f", 2, 6) + t(75, 178, "DC", 14, "middle", "800") + t(75, 198, "power", 10, "middle")
    s += t(75, 230, "battery / dynamo", 9.5, "middle")
    # wires
    s += line(110, 165, 250, 165, "#c62828", 3) + t(180, 158, "+", 13, "middle", "800", "#c62828")
    s += line(110, 195, 500, 195, "#1565c0", 3)
    s += line(500, 195, 500, 250, "#1565c0", 3) + t(180, 188, "\u2212", 15, "middle", "800", "#1565c0")
    s += line(250, 165, 250, 250, "#c62828", 3)
    # cell (beaker)
    s += '<path d="M210 250 h300 v120 a10 10 0 0 1 -10 10 h-280 a10 10 0 0 1 -10 -10 Z" fill="#e3f2fd" stroke="#37474f" stroke-width="2"/>'
    s += t(360, 345, "electrolyte (e.g. acidified water)", 10, "middle")
    # electrodes
    s += rect(246, 250, 8, 95, "#424242", "none", 0, 0) + t(250, 366, "anode (+)", 9.5, "middle", "700", "#c62828")
    s += rect(496, 250, 8, 95, "#424242", "none", 0, 0) + t(500, 366, "cathode (\u2212)", 9.5, "middle", "700", "#1565c0")
    # gas bubbles + collection
    for by in (300, 320, 340): s += f'<circle cx="262" cy="{by}" r="4" fill="#fff" stroke="#90a4ae"/>' + f'<circle cx="488" cy="{by}" r="4" fill="#fff" stroke="#90a4ae"/>'
    s += t(300, 262, "O\u2082 \u2191", 12, "middle", "700", "#2e7d32")
    s += t(452, 262, "H\u2082 \u2191 (twice the volume)", 11, "start", "700", "#c62828")
    s += t(600, 300, "Water: 2 H\u2082O \u2192 2 H\u2082 + O\u2082.", 10, "middle", "700")
    s += t(600, 320, "Brine instead gives Cl\u2082", 9.5, "middle")
    s += t(600, 336, "+ H\u2082 + NaOH (Part 4.5).", 9.5, "middle")
    return svg(730, 382, s)


# ---------------- TOC ----------------
TOC = [
 ("p1","Part 1 \u00b7 Lab Fundamentals",[("tiers","1.1 Three tiers of sophistication"),("glass","1.2 Glassware & improvised equivalents"),("heat","1.3 Heating, cooling & stirring"),("meas","1.4 Measuring mass, volume & temperature"),("phlab","1.5 pH & plant indicators"),("filt","1.6 Filtration & drying agents"),("safe","1.7 Safety culture, PPE & first aid"),("waste","1.8 Ventilation & waste disposal")]),
 ("p2","Part 2 \u00b7 Separation & Purification",[("dsimple","2.1 Simple distillation"),("dfrac","2.2 Fractional distillation"),("dsteam","2.3 Steam distillation"),("dvac","2.4 Vacuum distillation"),("recry","2.5 Recrystallisation"),("extr","2.6 Extraction & partition"),("chrom","2.7 Chromatography & melting point"),("titr","2.8 Titration & standard solutions")]),
 ("p3","Part 3 \u00b7 Raw Materials from the Land",[("salt","3.1 Salt & brine"),("lime","3.2 Limestone & the lime cycle"),("potash","3.3 Wood ash & potash"),("niter","3.4 Saltpetre beds"),("sulfur","3.5 Sulfur sources"),("carbon","3.6 Charcoal, coal & destructive distillation"),("iodine","3.7 Kelp & iodine")]),
 ("p4","Part 4 \u00b7 Acids & Alkalis",[("sulf","4.1 Sulfuric acid: lead-chamber & contact"),("nitr","4.2 Nitric acid"),("hcl","4.3 Hydrochloric & acetic acids"),("phos","4.4 Phosphoric acid"),("alkali","4.5 Soda, caustic soda & potash"),("ammonia","4.6 Ammonia")]),
 ("p5","Part 5 \u00b7 Gases & Elements",[("gases","5.1 Chlorine, hydrogen, oxygen, CO\u2082"),("halo","5.2 Iodine, bromine, phosphorus"),("store","5.3 Collection, storage & hazards")]),
 ("p6","Part 6 \u00b7 Organic Chemistry Foundations",[("ferm","6.1 Ethanol: fermentation to anhydrous"),("named","6.2 The named reactions"),("mech","6.3 Mechanisms behind the medicines")]),
 ("p7","Part 7 \u00b7 Worked Syntheses (Walkthroughs)",[("wsal","7.1 Salicylic acid & aspirin"),("wpara","7.2 Paracetamol & the -caines"),("wsulfa","7.3 Sulfanilamide"),("wether","7.4 Ether, Dakin's, iodine & saline"),("wqc","7.5 Verifying purity")]),
 ("p8","Part 8 \u00b7 Scaling Up & Energy",[("furn","8.1 Furnaces & heat sources"),("press","8.2 Pressure vessels & their dangers"),("mat","8.3 Corrosion-resistant materials"),("note","8.4 The lab notebook & teaching the next generation")]),
 ("p9","Part 9 \u00b7 US Patents for Lab & Process Equipment",[("ptintro","9.1 How to read and use these"),("pta","9.2 Tier A \u2014 improvised/simple"),("ptb","9.3 Tier B \u2014 workshop-built"),("ptc","9.4 Tier C \u2014 industrial")]),
 ("p10","Part 10 \u00b7 Region by Region",[]),
 ("srcs","Quick Reference & Sources",[]),
]

def body():
    b = [EXTRA_CSS]
    # ---------- Part 1 ----------
    b.append(part("p1","Part 1","Lab Fundamentals"))
    b.append('<p>This guide exists for one reason: to <b>keep chemical know-how alive</b>. If the chain of factories, power grids and trained chemists were ever broken, the information here is the ladder back up \u2014 how to make, purify and prove the acids, alkalis, solvents and medicines that a modern world takes for granted, starting from salt, stone, wood, air and water. It goes much deeper than the Medicine guide\u2019s summaries: full processes, the principles underneath them, balanced equations, rough yields, equipment, temperatures and catalysts, step-by-step procedures, troubleshooting, and how each thing was first done at small scale before modern plants existed.</p>')
    b.append(danger("This is a reference, not a licence to improvise","Every process here involves corrosive acids, toxic or flammable chemicals, high heat, pressure or electricity. A book can preserve knowledge; it cannot make the chemistry safe. Work only with real ventilation, eye and skin protection, the correct materials, and a tested procedure. Scale down, go slow, and never run a reaction you do not understand. Nothing here is medical advice, and no product described should be dosed into a person or animal."))
    b.append('<p class="dual" style="font-weight:600">Deliberate exclusions, stated plainly: this guide contains <b>no explosives formulations or weaponisation, no chemical-weapon agents, no controlled-substance or opioid synthesis, and no dosing experiments.</b> A few chemicals here are dual-use (for example nitric acid and saltpetre); they are covered only for legitimate medical, laboratory, agricultural and industrial purposes, and the text says so where they appear.</p>')
    b.append(h2("tiers","1.1 Three tiers of sophistication"))
    b.append('<p>Throughout, methods are sorted into three tiers so you can match ambition to resources. <b>Tier A</b> is improvised: fire, clay, scavenged containers, plant materials. <b>Tier B</b> is a real but modest lab: borosilicate glass, a balance, a thermometer, a furnace with forced air. <b>Tier C</b> is industrial: chambers, towers, catalysts, pressure vessels and electrolysis cells. Every tier is genuine chemistry; the higher tiers buy you purity, yield and safety, not magic.</p>')
    b.append(fig(d_tiers(), "The same target chemical can often be reached at any tier. Start at the lowest tier that gives acceptable purity for the job."))
    b.append(h2("glass","1.2 Glassware and improvised equivalents"))
    b.append('<p>Borosilicate glass is the chemist\u2019s best friend: it resists thermal shock and most acids '+c(26)+'. Where you have none, improvise \u2014 but know each substitute\u2019s limits (metal reacts with acids; earthenware can be glazed for acid work; copper tolerates heat but not strong oxidisers).</p>')
    b.append(fig(d_glassware(), "Match the vessel to the job. Improvised gear works for Tier A; precise or corrosive work needs glass or stoneware."))
    b.append(h2("heat","1.3 Heating, cooling and stirring"))
    b.append(ul([
      "<b>Gentle, even heat</b> comes from a water bath (up to 100\u00b0C), a sand bath (to ~300\u00b0C) or an oil bath. Direct flame cracks glass and chars organics \u2014 avoid it for distillations.",
      "<b>Cooling</b>: an ice bath (0\u00b0C), ice + salt (down to \u221220\u00b0C), or simply a long water-cooled condenser for refluxing vapours.",
      "<b>Stirring</b>: hand-swirling, a glass rod, or a boiling chip to prevent bumping. A simple magnetic stirrer is a Tier-B luxury.",
      "<b>Reflux</b> \u2014 boiling a mixture under a vertical condenser so vapour returns \u2014 lets you hold a reaction at its boiling point for hours without losing solvent.",
    ]))
    b.append('<p>The classic laboratory flame is the <b>Bunsen burner</b> (Robert Bunsen, 1855): gas enters at the base, mixes with air drawn through an adjustable collar, and burns at the top of a barrel. Open the air and you get a hot, clean, pale-blue flame; close it and you get a cooler, luminous yellow flame. Bunsen famously <b>never patented</b> his burner, so the closest patent record is the later improved burners in Part 9.</p>')
    b.append(fig(d_bunsen(), "The air collar is the whole trick: it sets how much air pre-mixes with the gas, and so the flame temperature. A plain blowpipe or a pinched gas pipe is the Tier-A substitute."))
    b.append(h2("meas","1.4 Measuring mass, volume and temperature"))
    b.append('<p>Quantitative chemistry needs numbers. A <b>balance</b> gives mass (and so moles, via molar mass); a <b>graduated cylinder</b> gives volume; a <b>thermometer</b> tracks reaction and vapour temperature. Keep a set of known masses to check a home-made balance. Stoichiometry \u2014 the mole ratios in a balanced equation \u2014 tells you how much of each reactant to weigh and how much product to expect.</p>')
    b.append(tip("Moles make it simple","moles = mass \u00f7 molar mass. A balanced equation gives the ratio of moles reacting. Convert back to grams or millilitres (using density) at the end. Always identify the <i>limiting reagent</i> \u2014 the one that runs out first sets the maximum yield."))
    b.append(h2("phlab","1.5 pH and plant indicators"))
    b.append('<p>You do not need a meter to measure acidity. Red-cabbage juice is a broad-range indicator: red in acid, purple near neutral, green to yellow in base, because its anthocyanin pigment changes structure with pH '+c(9,10)+'. Litmus comes from boiling certain lichens; turmeric turns red above about pH 8.</p>')
    b.append(fig(d_ph(), "Boil chopped red cabbage, strain, and keep the deep purple liquor. A few drops report pH by colour across the whole scale."))
    b.append(h2("filt","1.6 Filtration and drying agents"))
    b.append('<p>Separate solids from liquids by <b>gravity filtration</b> (folded paper or cloth in a funnel) or, faster, <b>vacuum filtration</b> (a Buchner funnel over a flask under suction). Dry solids in warm air or a desiccator; dry liquids with a drying agent that grabs water without reacting \u2014 anhydrous calcium chloride, magnesium sulfate, or quicklime for ethanol '+c(20)+'.</p>')
    b.append(h2("safe","1.7 Safety culture, PPE and first aid"))
    b.append(caution("Minimum protection","Splash goggles, acid-resistant gloves, an apron, closed shoes, tied-back hair. Keep a running water supply within reach. Never eat, drink or work alone with dangerous reagents. Label everything \u2014 an unlabelled bottle is a future accident."))
    b.append(check("Chemical first aid (while someone fetches help, where help exists)",[
      "Acid or base on skin: flush with copious running water for 15+ minutes; remove soaked clothing.",
      "Acid or base in eye: flush eye with water for 15+ minutes, lids held open.",
      "Fire: smother small fires; sand bucket for burning metals; never water on burning oil or reactive metals.",
      "Inhaled fumes: get to fresh air at once; chlorine and nitrogen oxides can injure lungs hours later \u2014 rest and watch.",
      "Swallowed chemical: do NOT induce vomiting for acids/alkalis/petroleum; rinse mouth, sip water if conscious.",
    ]))
    b.append(h2("waste","1.8 Ventilation and waste disposal"))
    b.append('<p>Many reactions release toxic or flammable gas (chlorine, HCl fumes, nitrogen oxides, hydrogen). Work outdoors or under a <b>fume hood</b> \u2014 a hooded, vented bench that pulls fumes away from your face (see the 1906 chemical-desk patent in Part 9). Neutralise acid waste with lime or soda before disposal; never pour incompatible wastes together; keep oxidisers away from fuels.</p>')

    # ---------- Part 2 ----------
    b.append(part("p2","Part 2","Separation & Purification"))
    b.append('<p>Making a chemical is half the battle; <b>purifying</b> it and <b>proving</b> it is pure is the other half. Separation exploits differences in boiling point, solubility, or affinity for a surface.</p>')
    b.append(h2("dsimple","2.1 Simple distillation"))
    b.append('<p>Distillation separates liquids by boiling point: heat the mixture, the lower-boiling component vaporises first, a cooled condenser turns it back to liquid, and you collect it in a receiver '+c(47)+'. Put the thermometer bulb at the side-arm so it reads the <i>vapour</i> temperature \u2014 that tells you what is actually coming over.</p>')
    b.append(fig(d_distill_simple(), "Simple distillation works when boiling points differ by roughly 25\u00b0C or more, and the impurity is non-volatile."))
    b.append(caution("Prevent bumping and over-pressure","Add boiling chips, never fill a flask more than two-thirds, and never heat a closed system \u2014 always leave a vent path or you build dangerous pressure."))
    b.append(h2("dfrac","2.2 Fractional distillation"))
    b.append('<p>Close-boiling liquids need a <b>fractionating column</b> packed with glass beads, rings or coils. Each repeated evaporation-condensation step inside the column is a <i>theoretical plate</i>; more plates give a sharper separation. Reaching above ~95% purity for a 20\u201330\u00b0C boiling-point gap needs at least three theoretical plates '+c(1,3)+'.</p>')
    b.append(fig(d_distill_frac(), "A taller, better-packed column = more theoretical plates = cleaner cuts. Reflux ratio (how much you return vs collect) also controls sharpness."))
    b.append(h2("dsteam","2.3 Steam distillation"))
    b.append('<p>Heat-sensitive, water-insoluble substances (essential oils, some organics) can be carried over by steam below 100\u00b0C. Because each immiscible component exerts its own vapour pressure, the mixture boils when the <i>sum</i> of pressures reaches atmospheric \u2014 so it distils cool enough not to char '+c(2)+'. The distillate separates into an oil layer and a water layer.</p>')
    b.append(fig(d_steam_distill(), "Steam distillation: pass steam through the plant charge; collect and separate the two layers."))
    b.append(h2("dvac","2.4 Vacuum distillation"))
    b.append('<p>Lowering the pressure lowers the boiling point, so high-boiling or heat-sensitive liquids can be distilled without decomposing '+c(3)+'. A hand or rotary vacuum pump, a strong (round-bottom) flask that will not implode, and a cold trap are the essentials. See the vacuum-dehydration patent in Part 9.</p>')
    b.append(h2("recry","2.5 Recrystallisation"))
    b.append('<p>The standard way to purify a solid: dissolve the crude in the minimum volume of hot solvent, hot-filter off insoluble dirt, then cool slowly. Pure crystals grow while soluble impurities stay dissolved in the mother liquor '+c(5)+'. Choose a solvent that dissolves the product hot but little cold.</p>')
    b.append(fig(d_recrystal(), "Recrystallisation trades yield for purity \u2014 some product always stays dissolved. That is the price of clean crystals."))
    b.append(h2("extr","2.6 Extraction and partition"))
    b.append('<p>Shake a mixture with two immiscible solvents (say water and an organic solvent) and each solute distributes between them according to its <b>partition coefficient</b> K '+c(4)+'. Several small extractions remove more than one large one. A separatory funnel (or improvised jar and tap) lets you draw off the lower layer.</p>')
    b.append(fig(d_extraction(), "Partition lets you pull a product out of a messy water layer into a clean organic layer, or vice versa."))
    b.append(h2("chrom","2.7 Chromatography and melting point"))
    b.append('<p><b>Thin-layer chromatography</b> (TLC) spots a tiny sample on a coated plate and runs it in solvent; each compound travels a characteristic fraction of the way (its R<sub>f</sub>), so one spot means one compound '+c(6)+'. <b>Column chromatography</b> scales the same idea to separate grams '+c(7)+'. A sharp <b>melting point</b> at the literature value is a classic identity-and-purity test for a solid.</p>')
    b.append(fig(d_tlc(), "TLC is the fastest way to ask: did my reaction work, and is the product one substance or a mixture?"))
    b.append(h2("titr","2.8 Titration and standard solutions"))
    b.append('<p>To measure how concentrated an acid or base is, titrate it against a <b>standard solution</b> of accurately known concentration, using an indicator to spot the endpoint '+c(8)+'. A <i>primary standard</i> (pure, stable, weighable \u2014 e.g. dried sodium carbonate) lets you standardise your working solutions. From the balanced equation and the volume used, back-calculate the unknown.</p>')
    b.append(fig(d_titration(), "Titration turns a colour change into a concentration \u2014 the backbone of quantitative analysis without instruments."))

    # ---------- Part 3 ----------
    b.append(part("p3","Part 3","Raw Materials from the Land"))
    b.append('<p>Every reagent traces back to something you can dig, burn, evaporate or grow. This part covers the feedstocks; Part 4 turns them into acids and alkalis.</p>')
    b.append(h2("salt","3.1 Salt and brine"))
    b.append('<p>Sodium chloride \u2014 from seawater evaporation, salt springs or rock salt \u2014 is the master feedstock. It gives chlorine, hydrogen and caustic soda by electrolysis (Part 4.5), hydrochloric acid, and sodium carbonate via the Solvay process. Purify crude salt by dissolving, filtering and recrystallising.</p>')
    b.append(h2("lime","3.2 Limestone and the lime cycle"))
    b.append('<p>Heating limestone (calcium carbonate) drives off carbon dioxide to give <b>quicklime</b> (CaO); adding water gives <b>slaked lime</b> (calcium hydroxide); exposure to air slowly carbonates it back. This lime cycle underpins mortar, water treatment, and dozens of reactions.</p>')
    b.append(rx("CaCO\u2083 \u2192(heat ~900\u00b0C) CaO + CO\u2082\u2191 ;  CaO + H\u2082O \u2192 Ca(OH)\u2082", "The lime kiln is one of the oldest chemical reactors \u2014 see the 1882 hydraulic-lime patent in Part 9."))
    b.append(fig(d_limecycle(), "The lime cycle: a renewable source of a cheap, strong base and a CO\u2082 feedstock."))
    b.append(h2("potash","3.3 Wood ash and potash"))
    b.append('<p>Leaching hardwood ashes with water and boiling down the liquor gives <b>potash</b> (impure potassium carbonate); further purification by calcining gives whiter <b>pearl ash</b> '+c(13,14)+'. Potash is a base, a source of potassium salts, and (with lime) a way to make caustic potash (KOH) for soft soap.</p>')
    b.append(h2("niter","3.4 Saltpetre beds"))
    b.append('<p>Potassium nitrate forms where nitrogen-rich organic matter decays with air, lime and ash present: soil bacteria oxidise ammonia to nitrate, which is leached out and crystallised '+c(11,12)+'.</p>')
    b.append(dual("Saltpetre (potassium nitrate) is dual-use. This guide covers it only for its <b>legitimate</b> roles \u2014 nitrogen fertiliser, a traditional food curing salt, a source of nitrate for making nitric acid for laboratory and medical glassware cleaning, and heat-treatment salts. It gives no explosive formulations or ratios."))
    b.append(fig(d_niterbed(), "A nitre bed converts waste nitrogen into nitrate over months \u2014 the pre-industrial source of nitrates for fertiliser and nitric acid."))
    b.append(h2("sulfur","3.5 Sulfur sources"))
    b.append('<p>Sulfur comes from volcanic deposits, from roasting metal sulfide ores (pyrite), or historically by melting and separating native sulfur from its gangue '+c(45)+'. It is the feedstock for sulfuric acid (Part 4.1).</p>')
    b.append(h2("carbon","3.6 Charcoal, coal and destructive distillation"))
    b.append('<p>Heating wood or coal <b>without air</b> (destructive distillation) leaves a carbon-rich solid and drives off valuable volatiles. From wood you get charcoal plus <b>pyroligneous acid</b> \u2014 the first industrial source of acetic acid, methanol and acetone '+c(15,16)+'. From coal you get coke plus <b>coal tar</b>, the historic source of phenol, benzene and aniline dye feedstocks.</p>')
    b.append(fig(d_wood_distill(), "One sealed retort and a fire yield charcoal, fuel gas, acetic acid/methanol/acetone, and tar. Redistil the liquor to separate the organics."))
    b.append(h2("iodine","3.7 Kelp and iodine"))
    b.append('<p>Burning seaweed to ash, leaching it, and treating the liquor liberates iodine \u2014 historically the main source before mineral brines '+c(48)+'. Iodine makes antiseptic tincture and Lugol\u2019s solution (Part 7.4).</p>')

    # ---------- Part 4 ----------
    b.append(part("p4","Part 4","Acids & Alkalis in Depth"))
    b.append('<p>The bulk acids and bases are the hardest things for a small operation to make well, and the most important. Here is how each was first made and how it is made now.</p>')
    b.append(h2("sulf","4.1 Sulfuric acid \u2014 lead-chamber and contact"))
    b.append('<p>Sulfuric acid is the keystone industrial chemical. Two routes matter. The older <b>lead-chamber process</b> burns sulfur to SO\u2082, then oxidises it to acid inside lead-lined chambers using nitrogen oxides as a recyclable catalyst, giving roughly 65% acid '+c(28,45)+'. The modern <b>contact process</b> passes dried SO\u2082 over a vanadium(V) oxide catalyst at 400\u2013450\u00b0C to make SO\u2083, which is absorbed into existing acid (to avoid a choking mist) and then diluted to 98% '+c(27,34)+'.</p>')
    b.append(fig(d_leadchamber(), "Lead-chamber process: lead resists sulfuric acid; NO/NO\u2082 ferry oxygen to the SO\u2082. Recovery towers recycle the nitrogen oxides."))
    b.append(fig(d_contact(), "Contact process: a reversible, exothermic step, so a moderate temperature and a catalyst give the best balance of rate and conversion (Le Chatelier)."))
    b.append(h2("nitr","4.2 Nitric acid"))
    b.append('<p>Two routes again. The <b>historical lab route</b> gently distils saltpetre with sulfuric acid and condenses the nitric acid vapour \u2014 glass or stoneware only, because hot nitric attacks most metals '+c(46)+'. The industrial <b>Ostwald process</b> catalytically oxidises ammonia over platinum to NO, then NO\u2082, then absorbs it in water '+c(29)+'.</p>')
    b.append(fig(d_ostwald(), "Nitric acid: from ammonia (Ostwald) or from saltpetre + sulfuric acid (the old distillation)."))
    b.append(dual("Nitric acid is dual-use. It is covered here only for legitimate uses: making laboratory reagents, cleaning and passivating glassware and stainless steel, metal etching and refining, and the medicinal/analytical nitrates. No energetic-material preparations are given."))
    b.append(h2("hcl","4.3 Hydrochloric and acetic acids"))
    b.append('<p><b>Hydrochloric acid</b>: historically a by-product of the Leblanc salt-cake step; simply made by treating salt with sulfuric acid and dissolving the hydrogen chloride gas in water (NaCl + H\u2082SO\u2084 \u2192 NaHSO\u2084 + HCl\u2191). <b>Acetic acid</b>: from oxidising ethanol (vinegar fermentation) or from the pyroligneous acid of wood distillation; concentrate by distillation. <b>Acetic anhydride</b> (needed for acetylation) is made industrially from acetic acid via ketene; it is the harder reagent to make and often the limiting step for aspirin.</p>')
    b.append(rx("2 CH\u2083COOH \u2192 (CH\u2083CO)\u2082O + H\u2082O", "Acetic anhydride from acetic acid (via ketene, CH\u2082=C=O, industrially). Store away from moisture \u2014 it hydrolyses back to acetic acid."))
    b.append(h2("phos","4.4 Phosphoric acid"))
    b.append('<p>Made by treating phosphate rock (or bone ash, calcium phosphate) with sulfuric acid (the wet process), or by burning phosphorus to P\u2082O\u2085 and hydrating it (the thermal process, higher purity). A mild acid catalyst and a buffering agent in medicine.</p>')
    b.append(h2("alkali","4.5 Soda, caustic soda and potash"))
    b.append('<p>Sodium carbonate (soda ash) came first from the wasteful <b>Leblanc</b> process and then the elegant <b>Solvay</b> process, which recycles its ammonia '+c(30,31,32)+'. Caustic soda (NaOH) and chlorine are made together by <b>electrolysis of brine</b> (the chloralkali process); a diaphragm or membrane keeps the chlorine and caustic from recombining '+c(30)+'. Potash gives caustic potash (KOH) by the lime causticising reaction.</p>')
    b.append(fig(d_solvay(), "Solvay process: salt + limestone + recycled ammonia \u2192 soda ash, with ammonia regenerated by lime."))
    b.append(fig(d_chloralkali(), "Chloralkali electrolysis: one cell makes chlorine, hydrogen and caustic soda at once. See the diaphragm- and membrane-cell patents in Part 9."))
    b.append(h2("ammonia","4.6 Ammonia"))
    b.append('<p>Historically recovered from the destructive distillation of coal (ammoniacal liquor) and from Solvay recovery. The <b>Haber-Bosch</b> process fixes atmospheric nitrogen: N\u2082 + 3 H\u2082 \u21cc 2 NH\u2083 over an iron catalyst at high pressure and ~400\u2013450\u00b0C '+c(33)+'. It is the hardest process here to reproduce at small scale because of the pressures involved \u2014 a true Tier-C undertaking.</p>')
    b.append(rx("N\u2082 + 3 H\u2082 \u21cc 2 NH\u2083   (\u0394H &lt; 0)", "High pressure favours the smaller gas volume (fewer moles) of ammonia; moderate temperature balances rate against the unfavourable equilibrium at high heat (Le Chatelier) "+c(34)+"."))

    # ---------- Part 5 ----------
    b.append(part("p5","Part 5","Gases & Elements"))
    b.append(h2("gases","5.1 Chlorine, hydrogen, oxygen and carbon dioxide"))
    b.append('<p>The four workhorse gases are each made by a simple reaction and collected by a method suited to their density and solubility '+c(17,18)+'.</p>')
    b.append(fig(d_gasprep(), "Collect gases denser than air (Cl\u2082, CO\u2082) by downward delivery; collect H\u2082 and O\u2082 over water. Chlorine is toxic \u2014 outdoors or fume hood only."))
    b.append(danger("Chlorine and hydrogen","Chlorine gas damages the lungs at low concentrations \u2014 never breathe it. Hydrogen forms explosive mixtures with air \u2014 no flames nearby, and test small. Oxygen supercharges any fire."))
    b.append('<p>Hydrogen and oxygen can also be made by <b>electrolysis of water</b> (acidified so it conducts): direct current splits water, hydrogen collecting at the cathode in twice the volume of oxygen at the anode. The same apparatus, run on brine, is the chloralkali cell of Part 4.5; run to make hydrogen peroxide, it is the antiseptic route of the Medicine guide.</p>')
    b.append(fig(d_electrolysis(), "A simple electrolysis cell: DC source, two electrodes, a conducting electrolyte, and gas collected over each electrode. See the water-electrolysis and electrolytic-peroxide patents in Part 9."))
    b.append(h2("halo","5.2 Iodine, bromine and phosphorus"))
    b.append('<p><b>Iodine</b> from kelp or brine (Part 3.7), purified by sublimation (it goes straight from solid to vapour and back). <b>Bromine</b> from seawater bitterns by chlorine displacement \u2014 extremely corrosive and toxic, handle only with full protection. <b>Phosphorus</b> is made by strongly heating phosphate rock with carbon and silica in a furnace (a demanding Tier-C reduction); covered here for matches, phosphoric acid and phosphates only.</p>')
    b.append(h2("store","5.3 Collection, storage and hazards"))
    b.append('<p>Store reactive gases dissolved or as stable salts rather than as compressed gas where possible. Keep oxidisers (chlorine, nitric acid, saltpetre) physically apart from fuels and organics. Vent every reaction that generates gas.</p>')

    # ---------- Part 6 ----------
    b.append(part("p6","Part 6","Organic Chemistry Foundations"))
    b.append(h2("ferm","6.1 Ethanol: fermentation to anhydrous"))
    b.append('<p>Yeast ferments sugars to ethanol and CO\u2082; distillation concentrates it, but <b>only to 95.6%</b> \u2014 the ethanol-water azeotrope, a constant-boiling mixture that ordinary distillation cannot pass '+c(19,21)+'. To reach anhydrous (>99%) ethanol, dry the 95% spirit over quicklime (CaO) or a 3\u00c5 molecular sieve, or break the azeotrope with an entrainer '+c(20)+'. Ethanol is solvent, antiseptic, fuel, and a reagent for esters and ether.</p>')
    b.append(fig(d_ethanol(), "Fermentation \u2192 distillation stalls at 95.6%; a drying step gives anhydrous ethanol. See Carlson's extractive-distillation patents in Part 9."))
    b.append(h2("named","6.2 The named reactions"))
    b.append('<p>A handful of reaction types build almost every small-molecule medicine. Learn these and the syntheses in Part 7 become variations on a theme.</p>')
    b.append(fig(d_ester(), "The organic toolbox. Each is a general transformation; the medicines in Part 7 are specific cases."))
    b.append(h2("mech","6.3 Mechanisms behind the medicines"))
    b.append(ul([
      "<b>Esterification</b> (acid + alcohol) and its reverse, <b>hydrolysis</b>/<b>saponification</b> (ester + base \u2192 soap + alcohol), explain aspirin, benzocaine and soap "+c(24)+".",
      "<b>Nitration</b> then <b>reduction</b> converts an aromatic ring to an amine (ArH \u2192 ArNO\u2082 \u2192 ArNH\u2082) \u2014 the gateway to sulfa drugs, local anaesthetics and dyes.",
      "<b>Acetylation</b> caps a reactive \u2013NH\u2082 or \u2013OH, used to make paracetamol and aspirin "+c(36,37)+".",
      "<b>Diazotisation and azo coupling</b> turn an aromatic amine into a brilliant dye, and historically into sulfa-drug intermediates "+c(22,23)+".",
    ]))

    # ---------- Part 7 ----------
    b.append(part("p7","Part 7","Worked Syntheses \u2014 Step-by-Step with Troubleshooting"))
    b.append('<p class="tierC" style="font-weight:600">This whole part is Tier B/C: it assumes a working lab with ventilation, glassware, heat, cooling and reagents. Its purpose is <b>knowledge retention</b> \u2014 these are the published routes by which humanity first made its most important medicines, explained in more detail than the Medicine guide. Nothing here is a kitchen project, and no product should ever be dosed into a person or animal.</p>')
    b.append(danger("Before any synthesis","Every route below uses corrosive acids, toxic or flammable reagents, and heat. Work with proper ventilation, protection, the right glassware, and the original published procedure in front of you. Verify purity (Part 7.5) before you even call something by the drug\u2019s name."))
    b.append(h2("wsal","7.1 Salicylic acid and aspirin"))
    b.append('<p><b>Salicylic acid</b> is made industrially by the <b>Kolbe-Schmitt</b> reaction: dry sodium phenoxide is heated under CO\u2082 pressure (~100\u00b0C, several atmospheres), carboxylating the ring; acidifying gives salicylic acid '+c(35)+'. At small scale it can also be obtained by hydrolysing methyl salicylate (oil of wintergreen) with sodium hydroxide, then acidifying.</p>')
    b.append('<p><b>Aspirin</b> (acetylsalicylic acid) is then made by acetylating salicylic acid with acetic anhydride and a trace of acid catalyst '+c(36)+'.</p>')
    b.append(fig(d_aspirin(), "Aspirin by acetylation: warm, cool, crash out with water, filter, recrystallise, then prove purity."))
    b.append(steps([
      "Weigh salicylic acid; add acetic anhydride (slight excess) and a few drops of phosphoric or sulfuric acid as catalyst.",
      "Warm to about 85\u00b0C in a water bath for 10\u201315 minutes, swirling. Do not overheat.",
      "Cool; add cold water to destroy excess anhydride and crash out crystals.",
      "Vacuum-filter, wash with a little cold water.",
      "Recrystallise from hot water (or water/ethanol), cool slowly, filter and dry.",
      "Verify: a negative iron(III) chloride test (no purple = no leftover phenol) and a sharp melting point of 135\u2013136\u00b0C.",
    ]))
    b.append(caution("Troubleshooting aspirin","No crystals? Scratch the flask, cool further, or add a seed crystal. Purple with FeCl\u2083? Unreacted salicylic acid remains \u2014 recrystallise again. Low, wide melting point? Impure or wet \u2014 dry fully and re-purify. Yield from 10 g salicylic acid is about 13 g in theory; expect noticeably less after purification."))
    b.append(h2("wpara","7.2 Paracetamol and the local anaesthetics"))
    b.append('<p><b>Paracetamol</b> (acetaminophen) is made by acetylating 4-aminophenol with acetic anhydride '+c(37)+'. <b>Benzocaine</b> is the ethyl ester of 4-aminobenzoic acid, made by acid-catalysed esterification '+c(38)+'. <b>Procaine</b> and <b>lidocaine</b> build on the same amine-and-amide/ester chemistry '+c(39)+'; lidocaine is an amide (more stable) rather than an ester.</p>')
    b.append(dual("Local anaesthetics are covered for knowledge-retention only. They are dangerous if injected impure or mis-dosed; this guide gives no dosing. Several steps genuinely need an industrial chemical supply behind them."))
    b.append(h2("wsulfa","7.3 Sulfanilamide"))
    b.append('<p>The first sulfa drug. The classic route protects aniline as acetanilide, chlorosulfonates it to a sulfonyl chloride, treats that with ammonia to the sulfonamide, then removes the protecting group by hydrolysis '+c(40)+'. It is a clean teaching example of protect \u2192 functionalise \u2192 deprotect, and of why a sequence matters.</p>')
    b.append(h2("wether","7.4 Ether, Dakin\u2019s solution, iodine tincture and saline"))
    b.append(ul([
      "<b>Diethyl ether</b>: heat ethanol with excess sulfuric acid near 140\u00b0C \u2014 the acid dehydrates two ethanol molecules into ether and water "+c(41)+". Extremely flammable, forms explosive peroxides on storage; no flames, store dark and cool with an antioxidant.",
      "<b>Dakin\u2019s solution</b>: dilute sodium hypochlorite buffered with sodium bicarbonate to near-neutral pH for wound irrigation "+c(42)+". Hypochlorite comes from passing chlorine into cold sodium hydroxide.",
      "<b>Iodine tincture / Lugol\u2019s</b>: dissolve iodine (and potassium iodide, which greatly increases solubility) in water or alcohol "+c(43)+".",
      "<b>Normal saline</b>: 9 g of purified sodium chloride per litre of sterile (boiled) water, 0.9% "+c(44)+".",
    ]))
    b.append(danger("Ether","Diethyl ether is one of the most dangerous things in this guide to make and store: its vapour is heavier than air, travels along benches to a distant flame, and it forms shock-sensitive peroxides over time. If you make it, make little, use it quickly, and never store it long."))
    b.append(h2("wqc","7.5 Verifying purity"))
    b.append('<p>For every solid product: recrystallise, then confirm identity and purity by a sharp <b>melting point</b> at the literature value and, where possible, a single <b>TLC spot</b> against a reference '+c(5,6)+'. For a reagent solution, <b>titrate</b> to find its real concentration '+c(8)+'. Never trust a synthesis by appearance alone.</p>')

    # ---------- Part 8 ----------
    b.append(part("p8","Part 8","Scaling Up & Energy"))
    b.append(h2("furn","8.1 Furnaces and heat sources"))
    b.append('<p>Chemistry is limited by the temperature you can reach and hold. A wood fire struggles past 600\u00b0C; <b>forced air</b> from a bellows or blower turns the same charcoal into a 1300\u00b0C forge; coke and electric kilns go higher still. Forced draft is the single biggest and cheapest upgrade.</p>')
    b.append(fig(d_furnace(), "Match the heat source to the job: lime burning needs ~900\u00b0C, glass and metal melting far more. See the sterilising, lime-kiln and furnace patents in Part 9."))
    b.append(h2("press","8.2 Pressure vessels and their dangers"))
    b.append(danger("Pressure kills","A ruptured pressure vessel is a bomb regardless of its contents. Any closed, heated system (autoclaves, Haber-type reactors, Kolbe-Schmitt carbonation) must have a tested relief valve or burst disc, a pressure gauge, and a barrier between it and people. Never improvise a pressure vessel from unrated pipe or containers."))
    b.append('<p>Steam sterilisers (autoclaves) and small reactors are the common pressure vessels in a lab. The sterilising-apparatus patents in Part 9 show proper chamber, jacket and valve design \u2014 study them before building anything that holds pressure.</p>')
    b.append('<p>The humble <b>pressure cooker</b> is the Tier-A autoclave: trapped steam raises the boiling point to about 121°C at ~15 psi, hot enough to sterilise instruments and media — exactly the method the Medicine guide gives for sterilising surgical tools. A weighted regulator holds the pressure and a safety valve prevents a burst. Part 9 collects real autoclave and pressure-cooker patents.</p>')
    b.append(fig(d_pressurecooker(), "Pressure-cooker/autoclave cutaway: sealing gasket, lid lock, weighted pressure regulator, safety relief valve, rack above the water line. The same physics scales up to a laboratory autoclave."))
    b.append(h2("mat","8.3 Corrosion-resistant materials"))
    b.append('<p>Match the material to the chemical '+c(25)+':</p>')
    b.append(table(["Material","Good for","Avoid"],[
      ["Borosilicate glass","Most acids, heat shock, observation "+c(26),"Hydrofluoric acid, strong hot alkali"],
      ["Lead","Dilute/medium sulfuric acid (lead chamber)","Nitric acid, acetic acid"],
      ["Stoneware / glazed ceramic","Strong acids incl. nitric, storage","Thermal shock, impact"],
      ["Stainless steel","Many organics, water, dilute bases","Chloride and halogen acids (pitting)"],
      ["Copper","Heat, non-oxidising duties, condensers","Strong oxidisers, ammonia, nitric acid"],
      ["Cast iron / 'Duriron' silicon iron","Hot concentrated sulfuric, nitric service","Hydrochloric acid"],
    ]))
    b.append(h2("note","8.4 The lab notebook and teaching the next generation"))
    b.append('<p>Knowledge survives only if it is written down and taught. Keep a bound <b>lab notebook</b>: date, aim, exact quantities, observations, yields, what went wrong. Record failures \u2014 they are the most valuable entries. Teach by apprenticeship: let a learner weigh, titrate and distil under supervision until the technique is in their hands, not just on paper. A single surviving notebook of tested procedures is worth more than any one batch of product.</p>')

    # ---------- Part 9: Patents ----------
    b.append(part("p9","Part 9","US Patents for Lab & Process Equipment"))
    b.append('<p>Patents are public disclosures: in exchange for protection, the inventor must describe the apparatus fully enough for others to build it, usually with detailed drawings. That makes them an unmatched library of <b>how to build equipment</b> \u2014 from an improvised still to an industrial electrolysis cell. The patents below were pulled from Google Patents and saved as PDFs alongside this guide, sorted by tier of sophistication. Groups covered include stills and condensers, fractionating columns, vacuum and filtration gear, autoclaves and pressure cookers, laboratory and Bunsen-type burners, furnaces and kilns, electrolytic and chloralkali cells, borosilicate (Pyrex-type) glass and glassware fabrication, sulfuric and nitric acid apparatus.</p>')
    b.append(h2("ptintro","9.1 How to read and use these"))
    b.append('<p>Each entry lists the patent number, title, inventor, grant date, and whether it is likely <b>expired</b> (older than ~20 years from filing) or possibly still <b>in force</b> \u2014 given purely as information. A patent being in force does not stop you reading it or building one for your own non-commercial survival use; it chiefly restricts commercial manufacture and sale. For each, the summary says what it teaches, which process in this guide it supports, and which drawing figures are worth copying. The full PDFs are in the "Patents" folder of the saved sources.</p>')
    b.append(fig(d_patent_tiers(), "The patent library spans all three tiers. Older patents often show the clearest, most buildable apparatus; modern ones show the best current designs."))
    b.append(h2("pta","9.2 Tier A \u2014 improvised / simple apparatus"))
    b.append('<p>Simple apparatus you could build with basic tools and materials: burners and the household pressure cooker that doubles as an autoclave.</p>')
    b.append(caution("Some classics were never patented","Several everyday pieces have no patent to cite because their inventors never filed one or they predate practical patenting: Robert Bunsen never patented his 1855 burner, Emil Erlenmeyer never patented his 1860 conical flask, and the plain beaker, test tube and Hofmann voltameter (water-electrolysis apparatus) are likewise unpatented public-domain designs. Where that is the case this guide says so and cites the closest improved apparatus instead."))
    ta = pats_in_tier("A")
    b.append(ta if ta.strip() else '<p class="small">(No patents classified Tier A in this set; the simplest buildable designs appear under Tier B.)</p>')
    b.append(h2("ptb","9.3 Tier B \u2014 workshop-built apparatus"))
    b.append('<p>Apparatus a competent workshop could fabricate: balances, hoods, sterilisers, vacuum and distillation gear.</p>')
    b.append(pats_in_tier("B"))
    b.append(h2("ptc","9.4 Tier C \u2014 industrial apparatus and processes"))
    b.append('<p>Plant-scale apparatus: distillation and fractionation, electrolytic cells, acid manufacture, water stills and gas separation.</p>')
    b.append(pats_in_tier("C"))

    # ---------- Part 10: Region ----------
    b.append(part("p10","Part 10","Region by Region"))
    b.append('<p>Feedstocks vary with geography. This is a rough guide to what each North American region most readily offers the improvising chemist \u2014 salt, limestone, wood for charcoal and potash, sulfur, brine and seaweed.</p>')
    b.append(regions_html(REGIONS))

    # ---------- Quick ref & sources ----------
    b.append(part("srcs","Quick Reference","Key Numbers & Sources"))
    b.append(h2("qref","Quick reference"))
    b.append(table(["Thing","Key fact"],[
      ["Ethanol azeotrope","95.6% ethanol by distillation; dry with CaO/sieve for anhydrous "+c(19,20)],
      ["Fractional distillation","\u22653 theoretical plates for >95% purity at 20\u201330\u00b0C bp gap "+c(1)],
      ["Lime cycle","CaCO\u2083 \u2192(900\u00b0C) CaO \u2192(+H\u2082O) Ca(OH)\u2082 "+c(45)],
      ["Contact process","V\u2082O\u2085 catalyst, 400\u2013450\u00b0C, absorb SO\u2083 into acid "+c(27)],
      ["Chloralkali","2 NaCl + 2 H\u2082O \u2192 Cl\u2082 + H\u2082 + 2 NaOH "+c(30)],
      ["Aspirin check","FeCl\u2083 negative; m.p. 135\u2013136\u00b0C "+c(36)],
      ["Normal saline","9 g NaCl per litre (0.9%) "+c(44)],
      ["Patents saved","23 equipment patents, Tiers A/B/C, in the Patents folder"],
    ]))
    b.append('<p class="small">General reference for knowledge retention when no chemical industry or professional is available. It is not professional, medical or safety advice and does not replace proper training, equipment or real medicine where any is reachable. Dual-use chemicals are covered for legitimate medical, laboratory, agricultural and industrial use only. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Chemistry", "Survival Info<br>Chemistry",
          "Rebuilding chemical capability from salt, stone, wood, air and water: lab fundamentals, separation and purification, raw materials, the bulk acids and alkalis, gases and elements, organic foundations, worked drug syntheses, scaling up \u2014 plus a tiered library of US equipment patents. DIY across North America, every claim sourced.",
          "Chemistry", TOC, cover_art(), "Medicine &amp; Remedies · Medical &amp; First Aid · Sanitation · Preservation · Water")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Chemistry.pdf")
