import subprocess, html, csv, math, fitz
import part1, part2, part3, part4, part5, part6, part7, part8, part9
from common import table, check, danger, tip, caution
from part_css import CSS

def cover_art():
    b = '<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">'
    b += '<circle cx="600" cy="80" r="40" fill="#e69b00" opacity="0.9"/>'
    for i in range(12):
        a = i*math.pi/6
        b += f'<line x1="{600+50*math.cos(a):.1f}" y1="{80+50*math.sin(a):.1f}" x2="{600+64*math.cos(a):.1f}" y2="{80+64*math.sin(a):.1f}" stroke="#e69b00" stroke-width="4" stroke-linecap="round"/>'
    b += '<polygon points="0,380 0,150 110,70 200,130 300,50 420,160 520,120 720,230 720,380" fill="#1c4452"/>'
    b += '<polygon points="270,80 300,50 330,82 315,78 300,90 285,76" fill="#e8f1f8" opacity="0.85"/>'
    b += '<polygon points="0,380 0,250 160,215 360,260 520,250 720,290 720,380" fill="#255868"/>'
    # trees
    for x, s in [(60, 1.0), (95, 0.8), (130, 1.1), (620, 0.9), (655, 1.2), (690, 0.8)]:
        b += f'<polygon points="{x},{250-70*s} {x-22*s},{250} {x+22*s},{250}" fill="#2e6b4f"/><rect x="{x-3}" y="250" width="6" height="12" fill="#5d4037"/>'
    # log cabin
    cx, base = 300, 300
    for k in range(7):
        y = base - 12 - k*12
        b += f'<rect x="{cx}" y="{y}" width="190" height="12" rx="6" fill="#b8895a" stroke="#6d4c41" stroke-width="1.2"/>'
        b += f'<circle cx="{cx-2}" cy="{y+6}" r="7" fill="#e3c79c" stroke="#6d4c41"/><circle cx="{cx+192}" cy="{y+6}" r="7" fill="#e3c79c" stroke="#6d4c41"/>'
    b += f'<polygon points="{cx-25},{base-84} {cx+95},{base-160} {cx+215},{base-84}" fill="#7d8b96" stroke="#12313d" stroke-width="2"/>'
    b += f'<rect x="{cx+150}" y="{base-180}" width="20" height="60" fill="#b85c38" stroke="#12313d"/>'
    b += f'<path d="M{cx+160},{base-185} q -10 -20 5 -35 q 12 -12 0 -30" fill="none" stroke="#cfd8dc" stroke-width="5" opacity="0.7" stroke-linecap="round"/>'
    b += f'<rect x="{cx+30}" y="{base-60}" width="30" height="26" fill="#ffd54f" stroke="#6d4c41" stroke-width="2"/><rect x="{cx+130}" y="{base-60}" width="30" height="26" fill="#ffd54f" stroke="#6d4c41" stroke-width="2"/>'
    b += f'<rect x="{cx+80}" y="{base-70}" width="30" height="58" fill="#5d4037"/>'
    b += f'<rect x="{cx-15}" y="{base-12}" width="220" height="12" fill="#9e9e9e"/>'
    # woodpile + barrel
    for i in range(4):
        for j in range(3 - (i>1)):
            b += f'<circle cx="{540+j*14+(i%2)*7}" cy="{290-i*12}" r="6.5" fill="#e3c79c" stroke="#6d4c41"/>'
    b += '<rect x="230" y="262" width="32" height="38" rx="4" fill="#5fb3e6" stroke="#cfe6f7"/><path d="M228,262 L264,262" stroke="#cfe6f7" stroke-width="3"/>'
    b += '</svg>'
    return b

TOC = [("p1", "Part 1 · Planning: Shelter First, Then a Home", [("stages", "1.1 From emergency shelter to permanent home"), ("site", "1.2 Choosing a site"), ("size", "1.3 Sizing a small house and floor plans"), ("solar", "1.4 Passive solar orientation")]),
       ("p2", "Part 2 · Tools, Timber & Salvage", [("tools", "2.1 Hand tools"), ("felling", "2.2 Felling and working timber"), ("salvage", "2.3 Salvaging materials safely: asbestos, lead, collapse")]),
       ("p3", "Part 3 · Foundations", [("ftypes", "3.1 Foundation types"), ("frost", "3.2 Frost depth by region")]),
       ("p4", "Part 4 · Wall Systems", [("compare", "4.1 Comparing wall systems by climate"), ("log", "4.2 Log cabins: notching and chinking"), ("timber", "4.3 Timber framing basics"), ("stick", "4.4 Stick framing with salvaged lumber"), ("cordwood", "4.5 Cordwood masonry"), ("straw", "4.6 Straw bale"), ("earth", "4.7 Earthen walls: cob, adobe, earthbag, rammed earth"), ("stone", "4.8 Stone walls")]),
       ("p5", "Part 5 · Floors, Roofs & Rainwater", [("floors", "5.1 Floors and joist spans"), ("roofs", "5.2 Roof framing: rafters, trusses, span tables"), ("pitch", "5.3 Roof pitch for rain and snow"), ("roofing", "5.4 Roofing materials"), ("gutters", "5.5 Gutters and rainwater catchment")]),
       ("p6", "Part 6 · Doors, Windows, Insulation & Moisture", [("doors", "6.1 Doors"), ("windows", "6.2 Windows, salvaged glass and shutters"), ("insulation", "6.3 Insulation from natural and salvaged materials"), ("moisture", "6.4 Ventilation and moisture control")]),
       ("p7", "Part 7 · Heating, Cooking & Lighting", [("stoves", "7.1 Wood stoves"), ("chimney", "7.2 Chimney safety and clearances"), ("rocket", "7.3 Rocket mass heaters"), ("cooking", "7.4 Cooking without power"), ("lighting", "7.5 Lighting basics")]),
       ("p8", "Part 8 · Sanitation", [("outhouse", "8.1 The outhouse (pit privy)"), ("compost", "8.2 Composting toilets"), ("greywater", "8.3 Greywater")]),
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

GROUPS = [
 ("Military & government building manuals", ["fm 5-426", "fm 21-76", "building with logs", "cmhc", "wood handbook", "forest products", "american wood council"]),
 ("Earthen, straw, log & historic construction", ["nps ", "getty", "cenapred", "earthen", "strawbale", "straw building", "cordwood", "earthbag", "cal-earth"]),
 ("Foundations, cold climates & hazards", ["frost", "permafrost", "cold climate", "fema", "firewise", "asce", "hurricane", "ready.gov", "ncei", "soil survey"]),
 ("Building science, energy & moisture", ["passive solar", "insulation", "energy star", "building america", "solution center", "building science", "mold", "radon"]),
 ("Health & safety: asbestos, lead, fire, CO", ["asbestos", "lead", "hantavirus", "osha", "burn wise", "stove", "nfpa", "chimney", "rocket", "carbon monoxide", "home fires"]),
 ("Sanitation & water", ["outhouse", "humanure", "septic", "greywater", "graywater", "sanitation", "rainwater"])]

def sources_html():
    rows = list(csv.reader(open("sources.tsv"), delimiter="\t"))
    groups = {g: [] for g, _ in GROUPS}; other = []
    for u, t in rows:
        tl = t.lower()
        for g, keys in GROUPS:
            if any(k in tl for k in keys):
                groups[g].append((u, t)); break
        else: other.append((u, t))
    if other: groups["Other"] = other
    out = []
    for g, items in groups.items():
        if not items: continue
        out.append(f'<h3 class="sg">{g}</h3><ul class="srcl">' + "".join(f'<li>{html.escape(t)}<br><a href="{u}">{html.escape(u)}</a></li>' for u, t in items) + '</ul>')
    out.append('<h3>Recommended books (print copies are worth having)</h3><ul class="src"><li>B. Allan Mackie, <i>Building with Logs</i> and <i>Notches of All Kinds</i>.</li><li>Tedd Benson, <i>Building the Timber Frame House</i> (Scribner).</li><li>Rob Roy, <i>Cordwood Building: A Comprehensive Guide</i> (New Society).</li><li>Chris Magwood &amp; Peter Mack, <i>Straw Bale Building</i> (New Society).</li><li>Ianto Evans, Michael G. Smith &amp; Linda Smiley, <i>The Hand-Sculpted House</i> (cob) (Chelsea Green).</li><li>Ianto Evans &amp; Leslie Jackson, <i>Rocket Mass Heaters</i> (Cob Cottage Co.).</li><li>Joseph Jenkins, <i>The Humanure Handbook</i>.</li><li>Lloyd Kahn, <i>Shelter</i> (Shelter Publications).</li><li>Edward Mazria, <i>The Passive Solar Energy Book</i> (Rodale).</li></ul>')
    return "\n".join(out)

def quickref():
    q = ['<h1 class="part" id="srcs"><small>Appendix</small>Quick Reference &amp; Sources</h1>']
    q.append(check("Build sequence for a core cabin (one season)", [
        "Month 0: choose site (water, drainage, sun, flood, fire); gather tools; start felling and salvage",
        "Month 1: clear and lay out (3-4-5, water level); dig and build foundation; collect stone, sand, clay",
        "Month 2: sill and floor framing; walls (logs, studs, bales on a frame…) up to plate height",
        "Month 3: roof framing and roofing <b>before</b> anything else gets wet; chimney or Class A stack; gutters to a cistern",
        "Month 4: doors, windows, shutters; stove installed with clearances and CO alarm; outhouse or compost toilet",
        "Month 5+: insulation (ceiling first), chinking/plaster, interior; woodshed full of seasoned wood before the first frost"]))
    q.append(table(["Rule / conversion", "Value"], [
        ["Length / area", "1 m = 3.281 ft; 1 in = 25.4 mm; 1 m² = 10.76 ft²; 1 acre = 4,047 m²"],
        ["Load", "1 psf = 47.9 Pa (0.048 kPa); 1 kPa = 20.9 psf; roof snow ≈ 0.7 × ground snow"],
        ["Square corners", "3-4-5 triangle; equal diagonals"],
        ["Roof pitch", "angle = arctan(rise ÷ 12): 4:12 = 18°, 6:12 = 27°, 8:12 = 34°, 12:12 = 45°"],
        ["Sun angle at noon", "90° − latitude ± 23.45° (June +, December −)"],
        ["Rain yield", "623 US gal per inch of rain per 1,000 ft²; 1 L per mm per m²"],
        ["Firewood", "1 cord = 4 × 4 × 8 ft = 128 ft³ = 3.62 m³ stacked"],
        ["Clearances", "Unlisted stove 36 in to combustibles; single-wall pipe 18 in; chimney 3 ft above roof and 2 ft above anything within 10 ft"],
        ["Outhouse", "≥ 100 ft (30 m) from wells/water, downhill; pit bottom ≥ 4 ft (1.2 m) above high water table"],
        ["Wood above ground", "≥ 8 in (20 cm) above soil; ≥ 18 in (45 cm) in termite country under floors"],
        ["Log settling", "Leave 2–3 in (5–8 cm) above doors and windows in green-log walls"]]))
    q.append('<p class="small">This guide is general information for emergency preparedness and education. Construction, tree felling, demolition and hazardous materials can injure or kill. In normal times, follow local building, fire and health codes, obtain permits, and use licensed professionals and engineers where required — especially for earthquake, hurricane, heavy-snow and permafrost sites. All spans and figures are typical or conservative values; verify against the sources below. Span tables were computed for this guide from published wood design values and are not a substitute for an engineer. URLs checked November 2026.</p>')
    q.append('<h2>Sources</h2>')
    q.append(sources_html())
    return "\n".join(q)

def document(pages):
    import common; common.FIG[0] = 0
    body = []
    body.append(f'''<section class="cover"><div class="band"></div><div class="series">Survival Info · Grid-Down Guide Series · North America</div>
<h1>Survival Info<br>Vol. 1: House<br>Building</h1>
<div class="sub">Build a home with hand tools and salvaged or natural materials — from a one-night emergency shelter to a permanent, warm, dry house — with region-by-region methods for all of North America.</div>
<div class="art">{cover_art()}</div>
<div class="foot">Companion volumes: Food · Water · Electricity &amp; Fuel · Concrete &amp; Masonry. &nbsp;Print this guide and keep a paper copy — it is meant to be used when the internet is not available.</div></section>''')
    body.append('<h2 style="margin-top:0">Contents</h2>' + toc_html(pages))
    body.append('<div class="pb"></div><h2 style="margin-top:0">How to use this guide</h2>')
    body.append('<p>Read <b>Part 1</b> first: it covers getting through the first night, choosing a site, and planning a small house you can actually finish. <b>Part 2</b> covers tools, felling and the serious hazards of salvaging from abandoned buildings. <b>Parts 3–6</b> follow the order of construction — foundation, walls, floor and roof, then openings, insulation and moisture control. <b>Part 7</b> covers safe heat, cooking and light, and <b>Part 8</b> sanitation, which keeps a household alive as surely as walls do. <b>Part 9</b> tells you which methods and materials fit your region and what hazards to design for. Concrete, lime, brick making and masonry walls are covered in depth in the companion <i>Concrete &amp; Masonry</i> volume; drinking-water treatment is in the <i>Water</i> volume.</p>')
    body.append(table(["Priority", "Goal", "Typical way to get there"], [
        ["1 · First night", "Out of wind and wet, insulated from the ground", "Vehicle, tarp, debris hut, one heated room of an existing building"],
        ["2 · First weeks", "Safe heat, cooking, sanitation", "Wall tent or room with stove and chimney; outhouse; water source"],
        ["3 · First season", "Weather-tight core cabin with a roof that sheds water", "12×16 to 16×24 ft cabin; wood stove; full woodshed"],
        ["4 · Years 1–3", "Comfortable, durable home", "Insulation, more rooms, root cellar, cistern, outbuildings"]]))
    body.append(danger("Safety first — everywhere in this guide", "Red boxes mark hazards that can kill: falling trees, collapsing buildings, asbestos, lead, carbon monoxide, chimney fires, falls from roofs, earthquakes and storms. Read them before starting a project. Amber boxes mark things that commonly ruin a building or waste a season’s work. Blue boxes are tips; green boxes are checklists to tick off."))
    body.append(check("Start-now list (while stores are open)", [
        "Felling axe, bow saw, two-man crosscut saw, wedges, sledge, drawknife, froe, chisels, brace and bits, hand saws, files and sharpening stones",
        "Chainsaw, spare chains, files, bar oil, fuel stabilizer, and chainsaw PPE (helmet with face screen, chaps, gloves, ear protection)",
        "Nails (16d, 8d), screws, gasketed roofing screws, metal straps and hurricane ties, anchor bolts, rebar tie wire, hinges",
        "Roofing: metal panels, underlayment, flashing; tarps; rolls of plastic sheet; caulk",
        "P100 respirators, safety glasses, hard hats, heavy gloves, first-aid kit, tetanus booster",
        "Wood or cook stove, Class A chimney kit, stovepipe, CO and smoke alarms (battery), fire extinguishers",
        "Salvaged windows, rigid foam boards and batts; a few bags of cement and lime (see Concrete &amp; Masonry)",
        "Printed copies of this guide and the key sources at the end"]))
    for p in (part1, part2, part3, part4, part5, part6, part7, part8, part9):
        body.append(p.build())
    body.append(quickref())
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Survival Info, Vol. 1: House Building</title><style>{CSS}</style></head><body>' + "\n".join(body) + '</body></html>'

def render(pages, out):
    open("guide.html", "w").write(document(pages))
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={out}", "guide.html"], check=True, capture_output=True)

if __name__ == "__main__":
    out = "/workspace/survival-info/Survival_Info_House.pdf"
    render({}, "pass1.pdf")
    doc = fitz.open("pass1.pdf")
    ids = []
    for pid, t, subs in TOC:
        ids.append(pid); ids += [s for s, _ in subs]
    links = []
    for pno in range(min(4, len(doc))):
        for l in doc[pno].get_links():
            if "page" in l and l["page"] >= 0:
                links.append(l["page"] + 1)
    pages = dict(zip(ids, links))
    print(len(ids), len(links))
    render(pages, out)
    d = fitz.open(out)
    d.set_metadata({"title": "Survival Info, Vol. 1: House Building", "author": "Survival Info series", "subject": "Grid-down house building guide for North America"})
    d.save(out + ".tmp"); d.close()
    import os; os.replace(out + ".tmp", out)
    print("pages:", fitz.open(out).page_count)
