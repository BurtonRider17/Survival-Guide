import subprocess, re, html, fitz, csv
import diagrams as D, part1, part3, part4, part5
from part_css import CSS
from readable import CSS_OVERRIDE
from diagrams import INK

def cover_art():
    # simple stylized motif: mountain stream, penstock, powerhouse, sun, wind turbine, oil drum
    b = '<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">'
    b += '<circle cx="610" cy="70" r="42" fill="#e69b00" opacity="0.9"/>'
    for i in range(12):
        import math
        a = i*math.pi/6
        b += f'<line x1="{610+52*math.cos(a):.1f}" y1="{70+52*math.sin(a):.1f}" x2="{610+66*math.cos(a):.1f}" y2="{70+66*math.sin(a):.1f}" stroke="#e69b00" stroke-width="4" stroke-linecap="round"/>'
    b += '<polygon points="0,380 0,120 90,60 170,110 260,40 360,150 470,220 720,250 720,380" fill="#1c4452"/>'
    b += '<polygon points="0,380 0,200 120,170 300,230 450,280 720,300 720,380" fill="#255868"/>'
    b += '<path d="M150,108 C200,150 250,170 300,200 S420,270 470,290 L720,310" fill="none" stroke="#5fb3e6" stroke-width="6" opacity="0.85"/>'
    b += '<polyline points="180,120 280,190 380,250 445,288" fill="none" stroke="#cfd8dc" stroke-width="7"/>'
    b += '<rect x="440" y="262" width="60" height="40" fill="#f4f1ea"/><polygon points="434,262 470,238 506,262" fill="#b85c38"/>'
    b += '<rect x="560" y="268" width="80" height="50" fill="#f4f1ea"/><polygon points="552,268 600,236 648,268" fill="#6d4c41"/>'
    b += '<rect x="575" y="246" width="30" height="16" fill="#1a3a5c" transform="rotate(-34 590 254)"/>'
    b += '<line x1="680" y1="300" x2="680" y2="150" stroke="#cfd8dc" stroke-width="4"/>'
    for a in (0, 120, 240):
        b += f'<line x1="680" y1="150" x2="680" y2="105" stroke="#fff" stroke-width="5" stroke-linecap="round" transform="rotate({a+15} 680 150)"/>'
    b += '<circle cx="680" cy="150" r="5" fill="#fff"/>'
    b += '<rect x="70" y="285" width="36" height="50" rx="4" fill="#e6b54a"/><line x1="70" y1="300" x2="106" y2="300" stroke="#12313d" stroke-width="2"/><line x1="70" y1="320" x2="106" y2="320" stroke="#12313d" stroke-width="2"/>'
    b += '<path d="M130,330 q8,-30 0,-50 q14,10 14,30 q0,12 -14,20z" fill="#c5e1a5"/><circle cx="160" cy="290" r="10" fill="#e6b54a"/><line x1="160" y1="300" x2="160" y2="335" stroke="#8bc34a" stroke-width="3"/>'
    b += '</svg>'
    return b

TOC = [("p1", "Part 1 · Electricity Basics & Safety", [("units","1.1 Volts, amps, watts, watt-hours"),("load","1.2 Sizing your household load"),("dcac","1.3 DC vs AC"),("safety","1.4 Safety: shock, arc flash, batteries, CO")]),
       ("p2", "Part 2 · Simple Energy", [("solar","2.1 Solar: salvaging and small systems"),("batteries","2.2 Battery banks"),("inverters","2.3 Inverters and wiring"),("mechanical","2.4 Alternators, bicycle generators, salvaged motors"),("wind","2.5 Small wind turbines"),("teg","2.6 Thermoelectric generators"),("gen","2.7 Generators and fuel storage"),("nonelec","2.8 Non-electric alternatives")]),
       ("p3", "Part 3 · Micro-Hydro (main project)", [("site","3.1 Site assessment: head and flow"),("power","3.2 The hydro power formula"),("civil","3.3 Intake, screen and penstock"),("turbines","3.4 Choosing a turbine"),("gen-hydro","3.5 Generators, controllers, dump loads"),("trans","3.6 Transmission wiring and voltage drop"),("ground","3.7 Grounding, freeze protection, maintenance, permits"),("anysite","3.8 Matching the design to your stream"),("sample","3.9 Worked example")]),
       ("p4", "Part 4 · Making Your Own Diesel (main project)", [("feed","4.1 Feedstocks"),("titrate","4.2 Titration"),("process","4.3 The process step by step"),("testing","4.4 Quality testing"),("supply","4.5 Methanol and lye supply"),("crops","4.6 Growing and pressing oil crops"),("svo","4.7 Straight vegetable oil"),("cold","4.8 Cold-weather gelling"),("store-bd","4.9 Storing homemade fuel"),("woodgas","4.10 Wood gasification")]),
       ("p5", "Part 5 · Region-by-Region Guide", []),
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
    groups = {"Micro-hydro": [], "Solar, wind & batteries": [], "Biodiesel, oil crops & fuel": [], "Safety, codes & permits": [], "Non-electric & other": []}
    for u, t in rows:
        tl = t.lower()
        if "hydro" in tl and "ferc" not in tl: g = "Micro-hydro"
        elif any(k in tl for k in ["wind", "solar prod", "pvwatts", "solar radiation", "battery"]): g = "Solar, wind & batteries"
        elif any(k in tl for k in ["biodiesel", "oil", "canola", "titration", "wood gas", "oilseed"]): g = "Biodiesel, oil crops & fuel"
        elif any(k in tl for k in ["cdc", "niosh", "nfpa", "ferc"]): g = "Safety, codes & permits"
        else: g = "Non-electric & other"
        groups[g].append((u, t))
    out = []
    for g, items in groups.items():
        if not items: continue
        out.append(f'<h3>{g}</h3><ul class="src">' + "".join(f'<li>{html.escape(t)}<br><a href="{u}">{html.escape(u)}</a></li>' for u, t in items) + '</ul>')
    out.append('<h3>Recommended books (print copies are worth having)</h3><ul class="src"><li>Scott Davis, <i>Microhydro: Clean Power from Water</i> (New Society Publishers, 2003).</li><li>Adam Harvey et al., <i>Micro-Hydro Design Manual: A Guide to Small-Scale Water Power Schemes</i> (ITDG/Practical Action Publishing, 1993).</li><li>Hugh Piggott, <i>A Wind Turbine Recipe Book</i> (self-published, metric and imperial editions).</li><li>Joshua Tickell, <i>From the Fryer to the Fuel Tank</i> (Tickell Energy, 3rd ed., 2003).</li><li>Dan Chiras, <i>Power from the Sun</i> and <i>The Homeowner’s Guide to Renewable Energy</i> (New Society Publishers).</li></ul>')
    return "\n".join(out)

def quickref():
    q = ['<h1 class="part" id="srcs"><small>Appendix</small>Quick Reference &amp; Sources</h1>']
    q.append(part1.table(["Conversion / rule", "Value"], [
        ["Power", "W = V × A; 1 hp = 746 W; 1 kW = 3,412 BTU/h"], ["Energy", "Wh = W × h; battery Wh = V × Ah"],
        ["Hydro power", "W = head (m) × flow (L/s) × 9.81 × 0.5  ≈  head (ft) × flow (gpm) ÷ 10"],
        ["Water pressure", "1 psi = 2.31 ft of head; 1 m of head = 9.81 kPa = 1.42 psi"],
        ["Flow", "1 L/s = 15.85 US gpm; 1 ft³/s (cfs) = 448.8 gpm = 28.3 L/s"],
        ["Length", "1 m = 3.281 ft; 1 km = 0.621 mi"], ["Volume", "1 US gal = 3.785 L; 1 cord = 128 ft³ = 3.62 m³"],
        ["Voltage drop", "V = 2 × L(ft) × I × R(Ω/1000 ft) ÷ 1000"], ["Wind power", "W = 0.5 × 1.225 × area(m²) × v³ × 0.25"],
        ["Solar daily energy", "Wh/day ≈ panel W × peak sun hours × 0.75"],
        ["Biodiesel recipe", "per litre oil: 200 mL methanol + (3.5–5.5 + titration) g NaOH, 1 h at 50–55 °C"],
        ["CO safety", "Generators outdoors, 20+ ft (6 m) from doors/windows/vents; CO alarms on every level"]]))
    q.append('<p class="small">This guide is general information for emergency preparedness and education. Electrical, fuel and chemical work can injure or kill. In normal times, follow local electrical and fire codes, obtain required permits, and use licensed professionals where required. All figures are typical values; verify against equipment manuals and the sources below. URLs checked November 2026.</p>')
    q.append('<h2>Sources</h2>')
    q.append('<div class="srccols">' + sources_html() + '</div>')
    return "\n".join(q)

def document(pages):
    body = []
    body.append(f'''<section class="cover"><div class="band"></div><div class="series">Survival Info · Grid-Down Guide Series · North America</div>
<h1>Survival Info<br>Vol. 1: Electricity<br>&amp; Fuel</h1>
<div class="sub">Build a micro-hydro plant to power a house, make your own diesel fuel, and use simpler energy sources — solar, batteries, wind, generators and non-electric heat and light — region by region across North America.</div>
<div class="art">{cover_art()}</div>
<div class="foot">Companion volumes: Food · Water. &nbsp;Print this guide and keep a paper copy — it is meant to be used when the internet is not available.</div></section>''')
    body.append('<h2 style="margin-top:0">Contents</h2>' + toc_html(pages))
    body.append('<div class="pb"></div><h2 style="margin-top:0">How to use this guide</h2>')
    body.append('<p>Start with <b>Part 1</b> to learn the basic units and safety rules, then build a small system from <b>Part 2</b> — a few solar panels and a battery bank give you lights, communications and refrigeration quickly and teach you the skills needed for bigger projects. <b>Part 3 (micro-hydro)</b> and <b>Part 4 (diesel fuel)</b> are the long-term projects: they take weeks to months of planning, measurement and building, so start them early while materials are still available. <b>Part 5</b> tells you which sources and crops fit your region.</p>')
    body.append(part1.table(["Priority", "Goal", "Typical way to get there"], [
        ["1 · First week", "Light, phone/radio charging, safe heat and cooking", "Stored batteries, small solar kit, wood stove, rocket stove, lamps"],
        ["2 · First month", "Refrigeration, water pumping, medical devices", "Solar + battery bank + pure-sine inverter; generator for peaks"],
        ["3 · First season", "Steady 24-hour power", "Micro-hydro (if you have a stream) or larger solar/wind system"],
        ["4 · First year+", "Fuel for tractor, truck, generator", "Biodiesel from waste oil and fat; then grow and press oilseed crops"]]))
    body.append(part1.danger("Safety first — everywhere in this guide", "Red boxes mark hazards that can kill: electric shock, battery explosions and fires, carbon monoxide, falls, methanol poisoning and lye burns. Read them before starting a project. Amber boxes mark things that commonly damage equipment or ruin a batch. Blue boxes are tips; green boxes are checklists to tick off."))
    body.append(part1.check("Start-now shopping list (while stores are open)", ["Multimeter, clamp ammeter, crimpers, assorted DC fuses and breakers, battery cable and lugs", "Solar panels, MPPT charge controller, LiFePO4 or golf-cart batteries, pure-sine inverter-charger", "CO alarms (battery), fire extinguishers, safety glasses, chemical goggles, nitrile/butyl gloves", "Fuel stabilizer, diesel biocide, approved fuel cans, spare fuel and oil filters", "Methanol (sealed drums), NaOH or KOH (sealed), phenolphthalein, isopropyl alcohol, scale (0.1 g), graduated syringes", "Oilseed (sunflower, canola, camelina) for your region; a hand-cranked screw press", "PVC/HDPE pipe and fittings, pressure gauge, garden hose and a level for measuring head", "Printed copies of this guide and the key sources at the end"]))
    body.append(part1.build(D))
    body.append(part1.build2(D))
    body.append(part3.build(D))
    body.append(part4.build(D))
    body.append(part5.build(D))
    body.append(quickref())
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Survival Info, Vol. 1: Electricity &amp; Fuel</title><style>{CSS + CSS_OVERRIDE}</style></head><body>' + "\n".join(body) + '</body></html>'

def render(pages, out):
    open("guide.html", "w").write(document(pages))
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={out}", "guide.html"], check=True, capture_output=True)

def link_pages(pdf):
    doc = fitz.open(pdf)
    pages = {}
    for pno in range(min(4, len(doc))):
        for l in doc[pno].get_links():
            if l.get("kind") == fitz.LINK_GOTO or "page" in l:
                # find which TOC anchor this is by text in rect
                txt = doc[pno].get_textbox(l["from"]).strip()
                pages[txt.split("\n")[0]] = l["page"] + 1
    return doc, pages

if __name__ == "__main__":
    import os
    out = "/workspace/survival-info/Survival_Info_Electricity.pdf"
    render({}, "pass1.pdf")
    doc = fitz.open("pass1.pdf")
    # map ids -> pages via named destinations order: TOC links appear in same order as TOC entries
    ids = []
    for pid, t, subs in TOC:
        ids.append(pid); ids += [s for s, _ in subs]
    links = []
    for pno in range(min(4, len(doc))):
        for l in doc[pno].get_links():
            if "page" in l and l["page"] >= 0:
                links.append(l["page"] + 1)
    pages = dict(zip(ids, links))
    print(len(ids), len(links), pages)
    render(pages, out)
    print("pages:", fitz.open(out).page_count)
