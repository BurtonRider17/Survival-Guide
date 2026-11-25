import subprocess, html, csv, math, fitz
import dg as D, c1, c2, c3, c4
from part_css import CSS
from readable import CSS_OVERRIDE
from helpers import *

def cover_art():
    b = '<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">'
    b += '<polygon points="0,380 0,150 110,80 200,140 300,60 420,170 520,120 620,190 720,150 720,380" fill="#1c4452"/>'
    b += '<polygon points="0,380 0,250 160,220 340,260 520,240 720,270 720,380" fill="#255868"/>'
    # forge glow
    b += '<circle cx="560" cy="250" r="70" fill="#e69b00" opacity="0.18"/><circle cx="560" cy="250" r="40" fill="#e69b00" opacity="0.3"/>'
    b += '<rect x="500" y="260" width="120" height="70" fill="#5d6b75"/><rect x="490" y="250" width="140" height="14" fill="#7d8b96"/>'
    b += '<path d="M530,252 C535,215 555,225 560,190 C568,220 588,215 590,252 Z" fill="#ff9800"/><path d="M548,252 C552,232 560,236 562,215 C568,236 574,236 574,252 Z" fill="#ffeb3b"/>'
    # anvil
    b += '<path d="M200,250 L360,250 L360,232 L420,240 L362,268 L330,268 L320,290 L345,315 L215,315 L240,290 L230,268 L200,268 Z" fill="#cfd8dc" stroke="#12313d" stroke-width="2"/>'
    b += '<rect x="245" y="315" width="90" height="40" fill="#8d6e63"/>'
    # hammer
    b += '<g transform="rotate(-28 300 180)"><rect x="290" y="120" width="12" height="110" rx="5" fill="#c49a6c"/><rect x="270" y="105" width="56" height="22" rx="3" fill="#e6b54a"/></g>'
    # glowing bar on anvil
    b += '<rect x="250" y="244" width="120" height="6" fill="#ff7043"/>'
    # axe
    b += '<g transform="rotate(20 110 280)"><rect x="104" y="200" width="12" height="150" rx="5" fill="#c49a6c"/><path d="M96,200 L130,200 L150,190 L160,240 L130,232 L96,232 Z" fill="#e6b54a"/></g>'
    # saw
    b += '<path d="M630,345 Q665,285 705,345" fill="none" stroke="#e6b54a" stroke-width="5"/>'
    b += '<line x1="630" y1="345" x2="705" y2="345" stroke="#cfd8dc" stroke-width="3"/>'
    b += "".join(f'<path d="M{632+i*6},346 l3,5 l3,-5" fill="none" stroke="#cfd8dc" stroke-width="1.2"/>' for i in range(12))
    b += '</svg>'
    return b

TOC = [("p1", "Part 1 · The Essential Tool Kit", [("kit","1.1 What to stockpile or salvage first"),("salvage","1.2 Where to salvage tools and steel")]),
       ("p2", "Part 2 · Tool Care", [("sharpen","2.1 Sharpening"),("rust","2.2 Rust prevention and cleaning"),("handles","2.3 Handles and rehafting"),("saws","2.4 Saw setting and filing")]),
       ("p3", "Part 3 · Primitive & Improvised Tools", [("stone","3.1 Stone tools and knapping basics"),("bone","3.2 Bone, antler and shell"),("woodtools","3.3 Wood tools"),("cordage","3.4 Cordage"),("horse","3.5 Shaving horse and spring-pole lathe")]),
       ("p4", "Part 4 · Blacksmithing (main section)", [("forges","4.1 Forge types and fuels"),("drum","4.2 Build a brake-drum forge"),("charcoal","4.3 Making charcoal"),("layout","4.4 Forge shop layout"),("anvil","4.5 Anvils, hammers and tongs"),("steel","4.6 Steel basics and identifying salvaged steel"),("heat","4.7 Heating colors"),("ops","4.8 Basic forging operations"),("weld","4.9 Forge welding"),("ht","4.10 Heat treating"),("projects","4.11 Projects")]),
       ("p5", "Part 5 · Metalworking Without a Forge & Salvage Welding", [("cold","5.1 Cold working"),("welding","5.2 Salvage welding notes")]),
       ("p6", "Part 6 · Woodworking for Construction", [("joinery","6.1 Joinery"),("green","6.2 Green woodworking"),("pegs","6.3 Making pegs")]),
       ("p7", "Part 7 · Safety in the Shop and at the Forge", []),
       ("p8", "Part 8 · Region-by-Region Guide", []),
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
    groups = {"Blacksmithing, metallurgy & welding": [], "Tools, axes, saws & wood": [], "Charcoal": [], "Safety & health": [], "Stone sources & primitive tools": []}
    for u, t in rows:
        tl = t.lower()
        if "fao" in tl: g = "Charcoal"
        elif any(k in tl for k in ["osha", "niosh", "zinc", "fume", "carbon monoxide", "burns", "nfpa"]): g = "Safety & health"
        elif any(k in tl for k in ["abana", "foxfire", "machine tools", "welding", "steel", "ferrous", "farm mechanics"]): g = "Blacksmithing, metallurgy & welding"
        elif any(k in tl for k in ["obsidian", "flint", "survival", "knife river", "rock collecting"]): g = "Stone sources & primitive tools"
        else: g = "Tools, axes, saws & wood"
        groups[g].append((u, t))
    out = []
    for g, items in groups.items():
        if not items: continue
        out.append(f'<h3>{g}</h3><ul class="src">' + "".join(f'<li>{html.escape(t)}<br><a href="{u}">{html.escape(u)}</a></li>' for u, t in items) + '</ul>')
    out.append('<h3>Recommended books (print copies are worth having)</h3><ul class="src"><li>Alexander Weygers, <i>The Complete Modern Blacksmith</i> (Ten Speed Press).</li><li>Jack Andrews, <i>New Edge of the Anvil: A Resource Book for the Blacksmith</i> (Skipjack Press).</li><li>Mark Aspery, <i>Mastering the Fundamentals of Blacksmithing</i> (vols. 1–3).</li><li>Eliot Wigginton (ed.), <i>Foxfire 5</i> (ironmaking, blacksmithing) and <i>Foxfire 3</i> and <i>4</i> (traditional crafts and tools).</li><li>Drew Langsner, <i>Green Woodworking</i>; Jack Sobon, <i>Timber Frame Construction</i>.</li><li>John Whittaker, <i>Flintknapping: Making and Understanding Stone Tools</i> (University of Texas Press).</li></ul>')
    return "\n".join(out)

def quickref():
    q = ['<h1 class="part" id="srcs"><small>Appendix</small>Quick Reference &amp; Sources</h1>']
    q.append(table(["Rule / value", "Number"], [
        ["Non-magnetic point (Curie) of steel", "≈ 1,414°F (768°C) — near hardening heat for carbon steel"],
        ["Hardening heat, common carbon steels", "≈ 1,450–1,550°F (790–845°C): just past non-magnetic"],
        ["Stop hammering", "Below dull red ≈ 1,100°F (590°C)"],
        ["Forge welding heat", "≈ 2,300–2,500°F (1,260–1,370°C): light yellow to white, flux bubbling"],
        ["Quench oil", "Warm canola/vegetable oil ≈ 120–130°F (50°C); metal can with lid; never water on oil fire"],
        ["Temper colors", "Straw 430–460°F knives/chisels · bronze 490°F axes · purple 530°F cold chisels · blue 570°F springs"],
        ["Edge angles", "Knife 15–25°/side · chisel 25°+30° micro · axe convex ≈ 30–35° incl. · cold chisel 60–70° incl."],
        ["Anvil size", "≈ 50 × hammer weight; face at knuckle height"],
        ["Charcoal yield", "Retort ≈ 25–35% of dry wood weight; pit/mound ≈ 10–20%"],
        ["Rivet length", "Grip thickness + 1.5 × rivet diameter"],
        ["Wood drying", "≈ 1 year per inch (25 mm) of thickness, air-dried under cover"],
        ["Zinc fume", "Never heat galvanized steel; remove zinc with vinegar first; OSHA limit 5 mg/m³ (8 h)"]]))
    q.append('<p class="small">This guide is general information for emergency preparedness and education. Forging, welding, grinding, charcoal making and edged tools can cause serious injury, fire, and poisoning. Learn from experienced instructors where possible, follow local fire rules and burn bans, respect property and protected archaeological sites, and verify temperatures and procedures for your specific steel against the sources below. All figures are typical values. URLs checked November 2026.</p>')
    q.append('<h2>Sources</h2>')
    q.append('<div class="srccols">' + sources_html() + '</div>')
    return "\n".join(q)

def document(pages):
    body = []
    body.append(f'''<section class="cover"><div class="band"></div><div class="series">Survival Info · Grid-Down Guide Series · North America</div>
<h1>Survival Info<br>Vol. 1: Tools<br>&amp; Blacksmithing</h1>
<div class="sub">Stockpile and care for the hand tools that build, farm and repair; make primitive tools from stone, bone and wood; set up a forge, make charcoal, and turn salvaged steel into tools — region by region across North America.</div>
<div class="art">{cover_art()}</div>
<div class="foot">Companion volumes: Water · Food · Electricity &amp; Fuel · Concrete &amp; Masonry · House Building. &nbsp;Print this guide and keep a paper copy — it is meant to be used when the internet is not available.</div></section>''')
    body.append('<h2 style="margin-top:0">Contents</h2>' + toc_html(pages))
    body.append('<div class="pb"></div><h2 style="margin-top:0">How to use this guide</h2>')
    body.append('<p>Tools are the foundation of every other volume in this series: you cannot dig a well, build a house, cut firewood, grow a field or repair a micro-hydro turbine without them. Start with <b>Part 1</b> to gather a kit while stores and salvage are plentiful, and learn <b>Part 2</b> (tool care) right away — it multiplies the life of everything you own. <b>Part 4 (blacksmithing)</b> is the long-term project: it lets a community make and repair tools from scrap steel for generations. <b>Part 8</b> tells you what wood, steel and stone your region offers.</p>')
    body.append(table(["Priority", "Goal", "Typical way to get there"], [
        ["1 · First week", "Cut firewood, dig, make basic repairs", "Axes, saws, shovels, hammers already on hand; sharpen them; files and oil"],
        ["2 · First month", "Keep tools working; build and garden", "Rehaft broken handles, set and file saws, salvage tools (Part 1), cordage"],
        ["3 · First season", "Make simple iron goods", "Brake-drum forge, charcoal retort, improvised anvil; hooks, nails, tongs"],
        ["4 · First year+", "Make and repair edged tools; build with joinery", "Steel ID, heat treatment, forge welding, knives and chisels, axe and farm-tool repair; timber framing"]]))
    body.append(danger("Safety first — everywhere in this guide", "Red boxes mark hazards that can kill or maim: burns, carbon monoxide, zinc fumes from galvanized steel, quench-oil fires, flying chips and arc flash. Read them before starting a project. Amber boxes mark things that commonly ruin tools or work. Blue boxes are tips; green boxes are checklists to tick off."))
    body.append(check("Start-now shopping list (while stores are open)", [
        "Files (many), whetstones, axe puck, diamond plate; saw files and a saw set; hacksaw blades by the box",
        "Spare axe, hammer and shovel handles with wedges; boiled linseed oil, paste wax, light oil",
        "Brace and auger bits, hand drill, twist bits, taps and dies, rivets, bar stock (¼–½ in round and square mild steel)",
        "Blacksmith coal (sealed bags) or a few drums for charcoal; borax for flux; canola oil for quenching",
        "Anvil (or rail/steel block), 2½ lb cross-peen hammer, tongs, post vise, hand-crank blower",
        "Safety glasses (several), face shield, leather gloves and apron, ear plugs, CO alarms, ABC extinguishers, burn dressings",
        "Welding: small stick welder, E6011/E6013/E7018 rods in sealed containers, helmet, leather jacket",
        "Printed copies of this guide and the Forest Service ax and saw manuals"]))
    body.append(c1.part1(D)); body.append(c1.part2(D)); body.append(c2.part3(D)); body.append(c2.part4a(D))
    body.append(c3.part4b(D)); body.append(c3.part5(D)); body.append(c3.part6(D)); body.append(c3.part7(D))
    body.append(c4.part8(D)); body.append(quickref())
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Survival Info, Vol. 1: Tools &amp; Blacksmithing</title><style>{CSS + CSS_OVERRIDE}</style></head><body>' + "\n".join(body) + '</body></html>'

def render(pages, out):
    open("guide.html", "w").write(document(pages))
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={out}", "guide.html"], check=True, capture_output=True)

if __name__ == "__main__":
    out = "/workspace/survival-info/Survival_Info_Tools.pdf"
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
    print(len(ids), len(links), pages)
    render(pages, out)
    print("pages:", fitz.open(out).page_count)
