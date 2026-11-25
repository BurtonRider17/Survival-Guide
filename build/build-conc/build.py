import subprocess, html, csv, math, fitz
import cdiag as D, c1, c2, c3, c4
from ccss import CSS
from helpers import danger, caution, tip, check, table, fig
from readable import CSS_OVERRIDE

CSS2 = CSS + """
.cover { background: #2b2f33; }
.cover .band { background: #b5523b; }
.cover .series { color: #e0a37f; }
.cover .sub { color: #d9d4cf; }
h1.part { background: #3d4a52; border-left-color: #b5523b; }
h2 { color: #3d4a52; border-bottom-color: #b5523b; }
.toc .tp { color: #3d4a52; border-bottom-color: #b5523b; }
th { background: #3d4a52; }
.kpi div { background: #2b2f33; }
.kpi div b { color: #e0a37f; }
.toc { column-count: 2; column-gap: 22px; }
.cols2 > * { break-inside: auto; }
tr { break-inside: avoid; }
""" + CSS_OVERRIDE + """
.toc .tp { break-after: avoid; }
"""

def cover_art():
    b = '<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">'
    b += '<circle cx="600" cy="70" r="40" fill="#e69b00" opacity="0.9"/>'
    b += '<polygon points="0,380 0,150 110,80 200,140 300,60 420,170 520,120 720,210 720,380" fill="#3d4a52"/>'
    b += '<polygon points="0,380 0,250 160,230 360,270 560,255 720,280 720,380" fill="#556570"/>'
    # lime kiln
    b += '<polygon points="70,300 90,190 170,190 190,300" fill="#9e9e9e"/><path d="M110,300 v-30 q20,-22 40,0 v30z" fill="#3e2723"/><path d="M118,300 q6,-22 12,-6 q6,-18 12,6z" fill="#e69b00"/>'
    b += '<path d="M125,185 q-12,-20 6,-35 q16,-14 0,-35" fill="none" stroke="#cfd8dc" stroke-width="6" opacity="0.6"/>'
    # brick wall
    for r in range(8):
        off = 0 if r % 2 == 0 else 18
        for c in range(9):
            x = 250 + c * 36 - off
            if 240 <= x <= 530:
                b += f'<rect x="{x}" y="{330 - r*16}" width="33" height="13" fill="{"#b5523b" if (r+c)%3 else "#c96a4f"}"/>'
    b += '<rect x="236" y="196" width="310" height="10" fill="#c9cdd1"/>'
    # well ring stack
    for i in range(3):
        b += f'<ellipse cx="625" cy="{318 - i*26}" rx="52" ry="12" fill="#c9cdd1" stroke="#2b2f33" stroke-width="2"/><rect x="573" y="{294 - i*26}" width="104" height="24" fill="#c9cdd1"/><ellipse cx="625" cy="{294 - i*26}" rx="52" ry="12" fill="#dfe3e6" stroke="#2b2f33" stroke-width="2"/>'
    b += '<ellipse cx="625" cy="242" rx="38" ry="8" fill="#2b2f33"/>'
    # trowel
    b += '<polygon points="560,190 620,150 640,170" fill="#cfd8dc"/><line x1="630" y1="160" x2="660" y2="130" stroke="#8d6e45" stroke-width="7" stroke-linecap="round"/>'
    b += '</svg>'
    return b

TOC = [("p1", "Part 1 · Basics: Concrete, Mortar, Plaster & Safety", [("what", "1.1 What concrete, mortar and plaster are"), ("roles", "1.2 Binder, aggregate and water"), ("ratios", "1.3 Mix ratios and water–cement ratio"), ("strength", "1.4 What strength to expect"), ("safety", "1.5 Safety: burns, dust, lifting, fire and gas")]),
       ("p2", "Part 2 · Finding & Salvaging Materials", [("cement", "2.1 Bagged cement and lime"), ("sand", "2.2 Sand and gravel; jar tests"), ("rca", "2.3 Recycled concrete and rubble"), ("steel", "2.4 Rebar, mesh and reinforcement"), ("water", "2.5 Water")]),
       ("p3", "Part 3 · Making Binders From Scratch", [("limestone", "3.1 Finding limestone; the vinegar test"), ("kiln", "3.2 Burning lime: a simple kiln"), ("slake", "3.3 Slaking quicklime; lime mortar and plaster"), ("pozz", "3.4 Pozzolans and Roman-style concrete"), ("hydraulic", "3.5 Hydraulic lime, natural cement, portland"), ("gypsum", "3.6 Gypsum plaster")]),
       ("p4", "Part 4 · Making Bricks & Blocks", [("clay", "4.1 Finding and testing clay"), ("temper", "4.2 Tempering clay"), ("mold", "4.3 Molding"), ("dry", "4.4 Drying"), ("adobe", "4.5 Adobe vs fired brick"), ("kilns", "4.6 Clamp, scove and updraft kilns"), ("firing", "4.7 Firing stages"), ("testbrick", "4.8 Testing fired bricks"), ("ceb", "4.9 Compressed earth blocks"), ("cmu", "4.10 Concrete blocks by hand"), ("laying", "4.11 Laying brick and block; bonds")]),
       ("p5", "Part 5 · Building Without Cement: Earth & Stone", [("rammed", "5.1 Rammed earth"), ("cob", "5.2 Cob and adobe"), ("earthbag", "5.3 Earthbags"), ("stone", "5.4 Dry stone"), ("soilcement", "5.5 Soil-cement and earth floors")]),
       ("p6", "Part 6 · Working With Concrete by Hand", [("mixing", "6.1 Mixing by hand"), ("forms", "6.2 Forms"), ("rebar", "6.3 Reinforcement in practice"), ("placing", "6.4 Placing and compacting"), ("curing", "6.5 Curing; cold and hot weather"), ("testing", "6.6 Testing strength simply")]),
       ("p7", "Part 7 · Projects", [("well", "7.1 Well rings and well caps"), ("cistern", "7.2 Cisterns and tanks"), ("footing", "7.3 Footings and foundations"), ("floor", "7.4 Slab floors"), ("cellar", "7.6 Root cellar walls"), ("stove", "7.7 Rocket stove and oven bases"), ("posts", "7.8 Fence posts")]),
       ("p8", "Part 8 · Building a Small Masonry House", [("site", "8.1 Site selection and drainage"), ("found", "8.2 Footings, foundations, frost depth by region"), ("walls", "8.4 Walls: choosing a system; floor plan"), ("openings", "8.5 Openings and lintels"), ("bond", "8.6 Bond beams, reinforcement, earthquakes"), ("roofatt", "8.7 Connecting the roof; wall section"), ("moisture", "8.8 Moisture control and insulation")]),
       ("p9", "Part 9 · Region-by-Region Guide", []),
       ("srcs", "Quick Reference & Sources", [])]

def toc_html(pages):
    out = ['<div class="toc">']
    for pid, title, subs in TOC:
        out.append(f'<a href="#{pid}" class="tp"><span>{html.escape(title)}</span><span class="dots"></span><span class="pg">{pages.get(pid, "00")}</span></a>')
        for sid, st in subs:
            out.append(f'<a href="#{sid}" class="ts"><span>{html.escape(st)}</span><span class="dots"></span><span class="pg">{pages.get(sid, "00")}</span></a>')
    out.append('</div>')
    return "\n".join(out)

def sources_html():
    rows = list(csv.reader(open("sources.tsv"), delimiter="\t"))
    groups = {"Concrete practice (Army, PCA, NRMCA, FHWA)": [], "Lime, pozzolans & Roman concrete": [], "Bricks, blocks & earth building": [], "Foundations, wells & tanks": [], "Geology & materials": [], "Safety": []}
    for u, t in rows:
        tl = t.lower()
        if any(k in tl for k in ["osha", "niosh", "cdc", "cameo"]): g = "Safety"
        elif any(k in tl for k in ["lime", "pozzolan", "roman", "repointing", "portland cement"]) and "pumice" not in tl and "utah" not in tl: g = "Lime, pozzolans & Roman concrete"
        elif any(k in tl for k in ["brick", "earth", "adobe", "earthbag", "rammed"]) : g = "Bricks, blocks & earth building"
        elif any(k in tl for k in ["foundation", "well", "tank", "residential code", "irc"]): g = "Foundations, wells & tanks"
        elif any(k in tl for k in ["usgs", "geolog", "jar", "pumice"]): g = "Geology & materials"
        else: g = "Concrete practice (Army, PCA, NRMCA, FHWA)"
        groups[g].append((u, t))
    out = []
    for g, items in groups.items():
        if not items: continue
        out.append(f'<h3>{g}</h3><ul class="src">' + "".join(f'<li>{html.escape(t)}<br><a href="{u}">{html.escape(u)}</a></li>' for u, t in items) + '</ul>')
    out.append('<h3>Recommended books (print copies are worth having)</h3><ul class="src"><li>Kosmatka &amp; Wilson, <i>Design and Control of Concrete Mixtures</i> (Portland Cement Association, 17th ed.).</li><li>Michael Wingate, <i>Small-scale Lime-burning: A Practical Introduction</i> (ITDG/Practical Action, 1985).</li><li>Vitruvius, <i>The Ten Books on Architecture</i>, Book II (lime, pozzolana, bricks).</li></ul>')
    return "\n".join(out)

def quickref():
    q = ['<h1 class="part" id="srcs"><small>Appendix</small>Quick Reference &amp; Sources</h1>']
    q.append(table(["Item", "Value"], [
        ["Concrete mixes (C:S:G by volume)", "1:2:3 structural, tanks, rings · 1:2:4 footings, slabs · 1:3:6 mass fill"],
        ["Water", "5–6 US gal per 94-lb bag (w/c ≈ 0.45–0.55); less if sand is wet"],
        ["Yield", "1 bag (94 lb, 1 ft³) of 1:2:3 → ~4 ft³ concrete; ≈ 7 bags per yd³ (≈ 390 kg cement per m³)"],
        ["Volume", "yd³ = L(ft) × W(ft) × depth(in) ÷ 324 · 1 yd³ = 27 ft³ = 0.765 m³ · concrete ≈ 150 lb/ft³ (2,400 kg/m³)"],
        ["Mortars", "Type N 1 cement : 1 lime : 6 sand · Type S 1 : ½ : 4½ · lime mortar 1 putty : 3 sand · lime–pozzolan 1 : 2–3"],
        ["Rebar & cover", "#3 = ⅜ in, #4 = ½ in · cover 3 in against earth, 1½–2 in weather, ¾ in inside · lap ≈ 40–60 diameters"],
        ["Curing", "Moist 7 days minimum (14 for tanks); keep above 50 °F (10 °C); protect from freezing until ≥ 500 psi"],
        ["Lime burning", "900–1,000 °C for 2–4 days; 1.75–1.8 kg stone → 1 kg quicklime; add lime to water, never water to lime"],
        ["Gypsum", "Calcine at 150–180 °C (300–350 °F); sets in 10–30 min; indoor only"],
        ["Brick firing", "Water-smoke slowly to ~120 °C, then up to 900–1,100 °C; soak 12–24 h; cool 2–7 days · absorption < 15–20%"],
        ["Footing width", "Load (lb/ft) ÷ soil bearing (psf) · clay 1,500 · sand 2,000 · gravel 3,000 · 1-story grouted masonry on clay: 16 in (IRC Table R403.1)"],
        ["Grade & base", "Ground falls 6 in in first 10 ft · floor ≥ 8 in above grade · earth walls on 12–18 in stem wall"],
        ["Tank volume", "US gal = 5.875 × D² × H (ft) · L = 785 × D² × H (m)"],
        ["Emergencies", "Cement/lime in eye: flush 15+ min with clean water, get help · CO symptoms: headache, dizziness → fresh air"]]))
    q.append('<p class="small">This guide is general information for emergency preparedness and education. Masonry, kilns, quicklime, heavy lifting and excavations can injure or kill, and structures that fail can kill the people inside. In normal times, follow local building codes, obtain permits, and use licensed engineers and builders where required. All figures are typical values and rules of thumb for small one-story buildings; verify against the sources below and local practice. URLs checked November 2026.</p>')
    q.append('<h2>Sources</h2>')
    q.append('<div class="srccols">' + sources_html() + '</div>')
    return "\n".join(q)

def intro():
    b = []
    b.append('<div class="pb"></div><h2 style="margin-top:0">How to use this guide</h2>')
    b.append('<p>Concrete and masonry turn a camp into a homestead: a lined well that doesn’t collapse, a cistern, a root cellar, a dry floor, a fire-proof stove base, fence posts that don’t rot and, eventually, a house that will stand for generations. <b>Part 1</b> explains how these materials work and how to stay safe. <b>Part 2</b> covers salvage — the fastest way to get cement, lime, sand, gravel and steel. <b>Part 3</b> shows how to make binders from rock and fire when salvage runs out, and <b>Part 4</b> how to make bricks and blocks. <b>Part 5</b> covers earth and stone building with no binder at all. <b>Parts 6 and 7</b> are hands-on: mixing, forming, curing and specific projects. <b>Part 8</b> covers the masonry side of a small house (with framing, roofing and insulation in the companion <b>House Building</b> volume), and <b>Part 9</b> tells you what materials and weather to expect in your region.</p>')
    b.append('<div class="kpi"><div><b>94 lb = 1 ft³</b>one US bag of portland cement</div><div><b>~7 bags</b>cement per cubic yard of 1:2:3 concrete</div><div><b>900 °C</b>to burn limestone into quicklime</div><div><b>7+ days</b>keep new concrete wet</div></div>')
    b.append(table(["Priority", "Goal", "Typical way to get there"], [
        ["1 · First weeks", "Secure what exists", "Collect bagged cement, lime, rebar, mesh, block, brick and tools; store dry; mark sand/gravel and limestone sources"],
        ["2 · First season", "Water and food storage", "Line and cap the well; build a cistern; build a root cellar; stove and oven bases"],
        ["3 · First year", "Make your own materials", "Test local clay and stone; build a lime kiln and a brick clamp; collect pozzolans; make blocks"],
        ["4 · Years 1–3", "Permanent buildings", "Footings, slabs and walls for a small masonry house, barns and storage; fence posts"]]))
    b.append(danger("Safety first — everywhere in this guide", "Red boxes mark hazards that can kill or maim: <b>quicklime and cement burns and blindness</b>, silica dust, kiln fires and carbon monoxide, trench collapse, falling loads, and buildings that fall down. Amber boxes mark common mistakes that ruin work. Blue boxes are tips; green boxes are checklists."))
    b.append(check("Start-now stockpile (while stores are open)", [
        "Portland cement (rotate stock), Type S hydrated lime (stores for years), masonry cement; heavy plastic bags or drums to keep them dry",
        "Rebar (#3, #4), welded wire mesh, cattle panels, tie wire, chicken wire and hardware cloth; anchor bolts and hurricane straps",
        "Tools: shovels, square-point shovel, hoe, wheelbarrow, mortar box, buckets, trowels, floats, levels (4 ft and torpedo), string line, tape, rebar bender/cutter, sledge, cold chisels, tamper",
        "Safety gear: sealed goggles, P100/N95 respirators, nitrile and gauntlet gloves, rubber boots, eyewash bottles, CO alarm",
        "Plastic sheeting, tarps, burlap; plywood and 2× lumber for forms; vegetable oil for form release",
        "Hand-press for compressed earth blocks (optional), steel block and brick molds; fire bricks; a kiln thermometer or pyrometric cones if you can get them",
        "Printed copies of this guide and the key sources (FM 5-428 / TM 3-34.44, Practical Action lime and brick briefs)"]))
    return "\n".join(b)

def document(pages):
    body = [f'''<section class="cover"><div class="band"></div><div class="series">Survival Info · Grid-Down Guide Series · North America</div>
<h1>Survival Info<br>Vol. 1: Concrete<br>&amp; Masonry</h1>
<div class="sub">Find and salvage materials, burn your own lime, make bricks and blocks, mix and cure concrete by hand, build wells, cisterns, cellars and foundations — and the masonry for a small house — region by region across North America.</div>
<div class="art">{cover_art()}</div>
<div class="foot">Companion volumes: Water · Food · Electricity &amp; Fuel · House Building. &nbsp;Print this guide and keep a paper copy — it is meant to be used when the internet is not available.</div></section>''']
    body.append('<h2 style="margin-top:0">Contents</h2>' + toc_html(pages))
    body.append(intro())
    body += [c1.part1(D), c1.part2(D), c1.part3(D), c2.part4(D), c2.part5(D), c3.part6(D), c3.part7(D), c4.part8(D), c4.part9(D), quickref()]
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Survival Info, Vol. 1: Concrete &amp; Masonry</title><style>{CSS2}</style></head><body>' + "\n".join(body) + '</body></html>'

def render(pages, out):
    open("guide.html", "w").write(document(pages))
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={out}", "guide.html"], check=True, capture_output=True)

if __name__ == "__main__":
    out = "/workspace/survival-info/Survival_Info_Concrete.pdf"
    render({}, "pass1.pdf")
    doc = fitz.open("pass1.pdf")
    ids = []
    for pid, t, subs in TOC:
        ids.append(pid); ids += [s for s, _ in subs]
    links = []
    for pno in range(min(4, len(doc))):
        for l in doc[pno].get_links():
            if "page" in l and l["page"] >= 0: links.append(l["page"] + 1)
    pages = dict(zip(ids, links))
    print(len(ids), len(links))
    render(pages, out)
    d2 = fitz.open(out)
    print("pages:", d2.page_count)
