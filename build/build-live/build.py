import sys, math; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def hen(x, y, k=1.0, col="#8d4a2b"):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{34*k}" ry="{24*k}" fill="{col}"/><circle cx="{x+30*k}" cy="{y-22*k}" r="{13*k}" fill="{col}"/>'
            f'<path d="M{x+26*k} {y-36*k} q4 -10 8 0 q4 -10 8 0" fill="#e53935"/><polygon points="{x+42*k},{y-24*k} {x+52*k},{y-20*k} {x+42*k},{y-17*k}" fill="#fbc02d"/>'
            f'<path d="M{x-34*k} {y-6*k} q-18 -20 -6 -34" fill="none" stroke="{col}" stroke-width="{8*k}"/><line x1="{x}" y1="{y+22*k}" x2="{x-4*k}" y2="{y+40*k}" stroke="#fbc02d" stroke-width="3"/><line x1="{x+10*k}" y1="{y+22*k}" x2="{x+12*k}" y2="{y+40*k}" stroke="#fbc02d" stroke-width="3"/>')

def cover_art():
    s = '<rect width="720" height="380" fill="#c5e1a5"/><rect y="270" width="720" height="110" fill="#8bc34a"/>'
    s += '<polygon points="470,170 580,100 690,170" fill="#8d6e63"/><rect x="480" y="170" width="200" height="110" fill="#d7ccc8" stroke="#5d4037" stroke-width="3"/><rect x="560" y="220" width="40" height="60" fill="#5d4037"/>'
    s += hen(150, 270, 1.4) + hen(300, 300, 1.1, "#f5f5f5") + hen(400, 260, 0.9, "#3e2723")
    s += '<rect x="40" y="160" width="60" height="70" rx="4" fill="#ffe082" stroke="#8d6e63" stroke-width="3"/><rect x="36" y="150" width="68" height="12" fill="#a1887f"/>'
    for i in range(5): s += f'<circle cx="{60 + i*14}" cy="{130 - (i%2)*8}" r="3" fill="#212121"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Chickens", [("why","1.1 Why chickens first"),("coop","1.2 The coop and predators"),("feed","1.3 Feed, water and daily care"),("hatch","1.4 Hatching your own chicks")]),
 ("p2", "Part 2 · Poultry Health", [("healthy","2.1 What a healthy bird looks like"),("dis","2.2 Coccidiosis, Marek's and other diseases"),("bio","2.3 Biosecurity and quarantine")]),
 ("p3", "Part 3 · Rabbits", [("hutch","3.1 Hutches and nest boxes"),("breed","3.2 Breeding calendar"),("rfeed","3.3 Feed, water and health")]),
 ("p4", "Part 4 · Goats", [("fence","4.1 Fences and shelter"),("kid","4.2 Breeding and kidding"),("worms","4.3 Barberpole worm: the number-one killer")]),
 ("p5", "Part 5 · Honey Bees", [("hive","5.1 The hive and the apiary"),("season","5.2 The bee year and winter stores"),("mites","5.3 Varroa mites")]),
 ("p6", "Part 6 · Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_coop():
    s = t(360, 26, "A safe coop: dry, ventilated, predator-proof", 19, "middle", "700")
    s += '<polygon points="90,120 330,50 570,120" fill="#a1887f" stroke="#4e342e" stroke-width="3"/>'
    s += rect(110, 120, 440, 220, "#fff8e1", "#4e342e", 3, 0)
    s += rect(130, 130, 70, 20, "#cfd8dc", "#455a64", 1, 2) + t(165, 145, "vent", 11, "middle", "700") + rect(460, 130, 70, 20, "#cfd8dc", "#455a64", 1, 2) + t(495, 145, "vent", 11, "middle", "700")
    s += line(140, 200, 330, 200, "#6d4c41", 8) + line(160, 240, 360, 240, "#6d4c41", 8) + t(250, 190, "roosts — up high", 13, "middle", "700")
    for i in range(3): s += rect(400 + i*48, 250, 44, 44, "#ffe0b2", "#6d4c41", 2, 2) + f'<ellipse cx="{422 + i*48}" cy="282" rx="9" ry="7" fill="#fff"/>'
    s += t(472, 312, "nest boxes", 13, "middle", "700") + t(472, 328, "1 per 4–5 hens", 12, "middle")
    s += rect(330, 280, 40, 60, "#5d4037", "none", 0, 0) + t(350, 356, "door: shut at dusk", 12, "middle", "700")
    s += t(330, 375, "Floor space: at least 3–5 sq ft per bird indoors", 14, "middle", "700")
    s += t(600, 170, "Threats:", 13, "start", "800", "#b71c1c") + t(600, 190, "raccoons, rats,", 12, "start") + t(600, 206, "owls, hawks, cats", 12, "start")
    s += t(600, 240, "No small holes;", 12, "start") + t(600, 256, "no woodpiles or", 12, "start") + t(600, 272, "junk nearby", 12, "start")
    return svg(720, 390, s)

def d_hatch():
    s = t(360, 26, "Incubating chicken eggs: 21 days at 99.5 °F", 19, "middle", "700")
    x0, sc = 50, 30
    s += rect(x0, 60, 18*sc, 40, "#ffe0b2", "#e65100", 2, 4) + t(x0 + 9*sc, 86, "Days 1–18: humidity 55–60% · TURN 5–6× a day", 14, "middle", "700")
    s += rect(x0 + 18*sc, 60, 3*sc, 40, "#ffcdd2", "#c62828", 2, 4) + t(x0 + 19.5*sc, 86, "hatch", 13, "middle", "800")
    for d in range(0, 22, 3): s += line(x0 + d*sc, 104, x0 + d*sc, 116) + t(x0 + d*sc, 132, str(d), 13, "middle", "700")
    s += arrow(x0 + 10*sc, 170, x0 + 10*sc, 104, "#1565c0") + t(x0 + 10*sc, 188, "Day 10: candle — remove clear (infertile) or dead eggs", 13, "middle", "700", "#1565c0")
    s += '<ellipse cx="160" cy="260" rx="38" ry="50" fill="#fffde7" stroke="#795548" stroke-width="3"/>' + t(160, 330, "clear = infertile", 12, "middle", "600")
    s += '<ellipse cx="300" cy="260" rx="38" ry="50" fill="#ffcc80" stroke="#795548" stroke-width="3"/><path d="M285 250 q15 -25 30 0 q-15 30 -30 0" fill="#6d4c41"/>' + "".join(f'<path d="M300 250 q{dx} {dy} {dx*2} {dy*1.6}" stroke="#c62828" stroke-width="1.5" fill="none"/>' for dx, dy in [(12, -10), (-12, -8), (10, 14), (-14, 12)]) + t(300, 330, "dark + veins = growing", 12, "middle", "600")
    s += t(440, 240, "Mark X and O on opposite", 13, "start") + t(440, 258, "sides to track turning.", 13, "start") + t(440, 288, "Store hatching eggs", 13, "start") + t(440, 306, "big end up.", 13, "start")
    return svg(720, 345, s)

def d_rabbit():
    s = t(360, 26, "Rabbit breeding calendar", 19, "middle", "700")
    x0, sc = 40, 9.5
    s += line(x0, 80, x0 + 66*sc, 80, "#455a64", 4)
    s += rect(x0, 64, 31*sc, 32, "#f8bbd0", "none", 0, 4) + t(x0 + 15*sc, 85, "gestation 31–32 days", 14, "middle", "700")
    s += rect(x0 + 31*sc, 64, 30*sc, 32, "#c5e1a5", "none", 0, 4) + t(x0 + 46*sc, 85, "nursing ≈30 days", 14, "middle", "700")
    marks = [(0, 0, "Day 0: breed", "take the doe to the buck's cage"), (28, 1, "Day 28: nest box in", ""), (31, 2, "Day 31–32: kindling (birth)", ""), (33, 3, "48 h after birth: count kits,", "remove any dead"), (61, 0, "≈Day 61: wean", "")]
    for d, row, a, b2 in marks:
        x = x0 + d*sc; y = 130 + row*36
        s += line(x, 96, x, y - 4, "#455a64", 1.5) + f'<circle cx="{x}" cy="80" r="6" fill="#c62828"/>'
        anc = "start" if d < 50 else "end"
        tx = x + 6 if anc == "start" else x - 6
        s += t(tx, y + 10, a + ("  — " + b2 if b2 else ""), 13, anc, "700")
    s += t(360, 290, "≈ 5 litters a year per doe; a good doe produces well for 2–3 years", 14, "middle", "600")
    s += t(360, 312, "Cage mesh: 1×2 in sides and top, ½×1 in floor", 13, "middle")
    return svg(720, 325, s)

def d_fence():
    s = t(360, 26, "Goat-tight fence: 5–6 high-tensile wires", 19, "middle", "700")
    for x in (80, 360, 640): s += rect(x - 8, 50, 16, 260, "#8d6e63", "#4e342e", 2, 2)
    hot = [True, False, True, False, False, True]
    for i, h in enumerate(hot):
        y = 290 - i*42
        s += line(80, y, 640, y, "#e53935" if h else "#607d8b", 4 if h else 3)
        s += t(660, y + 5, ("⚡ electrified" if h else "plain") + f" (wire {i+1})", 12, "start", "700" if h else "normal", "#c62828" if h else INK)
    s += line(40, 310, 700, 310, "#6d4c41", 4)
    s += t(360, 340, "Wires 1, 3 and top electrified. Woven wire also works with one hot wire inside.", 13, "middle", "600")
    return svg(720, 355, s)

def d_rotate():
    s = t(360, 26, "Rotating pasture against worms", 19, "middle", "700")
    for i in range(4):
        x = 30 + i*172
        s += rect(x, 50, 160, 140, "#a5d6a7" if i else "#66bb6a", "#2e7d32", 2, 6) + t(x + 80, 80, f"Paddock {i+1}", 14, "middle", "700")
        s += t(x + 80, 110, "goats here" if i == 0 else ("resting" if i else ""), 13, "middle", "700" if i == 0 else "normal")
        if i < 3: s += arrow(x + 150, 210, x + 182, 210, "#37474f", 3)
    s += t(110, 140, "≤ 5 days", 15, "middle", "800", "#1b5e20")
    s += t(360, 245, "Eggs in manure hatch into infective larvae after about 5 days → move on before then", 13, "middle", "600")
    s += t(360, 266, "Leave before grass is shorter than 6 in · rest each paddock about 2 months in summer", 13, "middle", "600")
    return svg(720, 280, s)

def d_eye():
    s = t(360, 26, "Check the inner lower eyelid for anemia", 19, "middle", "700")
    cols = [("#c62828", "red"), ("#e57373", "red-pink"), ("#f8bbd0", "pink"), ("#fce4ec", "pale pink"), ("#ffffff", "white")]
    for i, (col, lab) in enumerate(cols):
        x = 60 + i*125
        s += f'<ellipse cx="{x+50}" cy="100" rx="52" ry="30" fill="{col}" stroke="#795548" stroke-width="3"/>' + t(x + 50, 152, lab, 14, "middle", "700")
    s += arrow(110, 180, 610, 180, "#37474f", 3) + t(110, 205, "healthy", 13, "start", "700", "#2e7d32") + t(610, 205, "severe anemia: barberpole worm", 13, "end", "700", "#b71c1c")
    s += t(360, 235, "Also look for thin body, bottle jaw (swelling under the jaw) and weakness", 13, "middle")
    return svg(720, 250, s)

def d_hive():
    s = t(360, 26, "Langstroth hive (standard 10-frame boxes)", 19, "middle", "700")
    parts = [("outer cover", 20, "#90a4ae"), ("medium super, 6⅝ in deep:", 60, "#ffe082", "surplus honey you harvest"), ("deep, 9⅝ in:", 90, "#ffca28", "the bees' winter honey"), ("deep, 9⅝ in:", 90, "#ffb300", "brood nest (queen lays here)"), ("bottom board + entrance", 18, "#8d6e63")]
    y = 50
    for p in parts:
        lab, h, col = p[:3]
        s += rect(90, y, 240, h, col, "#5d4037", 2, 2)
        if len(p) > 3: s += t(350, y + h/2 - 3, lab, 14, "start", "700") + t(350, y + h/2 + 15, p[3], 14, "start")
        else: s += t(350, y + h/2 + 5, lab, 14, "start", "700")
        y += h
    s += rect(70, y, 280, 20, "#6d4c41", "none", 0, 0) + t(210, y + 15, "stand", 12, "middle", "700", "#fff")
    s += rect(150, y - 16, 120, 8, "#212121", "none", 0, 0)
    s += t(350, y + 50, "A filled deep box weighs over 70 lb.", 14, "start", "600")
    return svg(720, y + 70, s)

R = {
 1: "Extreme cold: choose heavy breeds for cold winters " + c(1) + ", keep coops well insulated with ventilation, and supply 12–14 hours of light for laying through the dark months; extra light needs power, so without it expect a winter laying pause " + c(1) + ". Rabbits need protection from temperature extremes " + c(5) + ". Bees are marginal this far north.",
 2: "Wet, mild climate: keep litter dry against coccidiosis (moist, warm litter speeds parasite eggs) " + c(3) + ". Barberpole worm thrives in warm, wet weather " + c(7) + "; rotate goat paddocks.",
 3: "Wind and cold: windbreaks and shelter; goats need an open shed of 10–12 sq ft per doe in extreme weather " + c(6) + ". Long distances from neighbors make quarantine easier " + c(4) + ".",
 4: "Cold winters: insulated coops, heavy breeds " + c(1) + "; rest goat pasture about 2 months in summer as in Minnesota trials " + c(7) + ". Bees need full winter stores — 40–80 lb per colony " + c(8) + ".",
 5: "Like the Great Lakes: insulate coops and plan for short winter days " + c(1) + "; heavy honey stores for long winters " + c(8) + ".",
 6: "Heat and humidity: shade and constant clean water — chickens cool by panting " + c(1) + ". Barberpole worm grows fastest at 86–96 °F " + c(7) + ": rotate paddocks every 5 days or less " + c(7) + ". Mississippi beekeepers treat first-year colonies for varroa in mid-summer " + c(9) + ".",
 7: "Hot and wet year-round: worms and coccidia never get a winter break " + c(3, 7) + ". Shade, ventilation and dry litter are essential " + c(1, 3) + ".",
 8: "Extreme heat: shade and water first; feed intake drops in summer heat " + c(1) + ". Goats suit dry brush country well, but still need tight fencing " + c(6) + ". Offer bees a shallow water pan with perches " + c(8) + ".",
 9: "Cold, high-altitude winters: insulated coops and windbreaks " + c(1) + "; bees need an east- or south-facing site with a northern windbreak " + c(8) + ".",
 10: "Mild coastal climate suits all four species; inland heat calls for shade and water " + c(1) + ". Ornamental plantings give bees a long honey flow " + c(8) + ".",
 11: "Dry heat: goats and chickens do well with shade and water " + c(1, 6) + ". Worm pressure rises after summer rains " + c(7) + ".",
 12: "Warm, wet season brings worm and coccidia pressure " + c(3, 7) + "; highland cold nights need sheltered coops " + c(1) + ".",
 13: "Tropical heat and rain: dry litter, shade and pasture rotation every 5 days or less " + c(3, 7) + ". Bee colonies can forage much of the year " + c(8) + ".",
}

def body():
    b = []
    b.append(part("p1", "Part 1", "Chickens"))
    b.append('<p>Small animals turn scraps, grass and brush into eggs, meat, milk, fiber and honey. This guide covers chickens, rabbits, goats and honey bees with no feed store, vet clinic or hatchery to call. For killing, butchering and cooling meat see the Hunting guide; for curing and canning see the Preservation guide.</p>')
    b.append(h2("why", "1.1 Why chickens first"))
    b.append(ul(["Hens start laying at about six months and continue five to 10 years, peaking in the first two " + c(1) + ".",
                 "A good hen lays roughly six eggs a week; production drops when hens molt in early fall and as days shorten — they need 12–14 hours of light to keep laying " + c(1) + ".",
                 "Medium to large breeds handle cold winters; dual-purpose breeds such as Rhode Island Red, Wyandotte and Orpington give both eggs and meat " + c(1) + "."]))
    b.append(h2("coop", "1.2 The coop and predators"))
    b.append(fig(d_coop(), "Coop needs from University of Minnesota Extension " + c(1) + "."))
    b.append(ul(["Protect from weather and predators; give at least <b>3–5 square feet per bird</b> indoors, one <b>nest box per 4–5 hens</b>, and high roosts " + c(1) + ".",
                 "Ventilation for fresh air, plus insulation in cold climates " + c(1) + ".",
                 "Main predators: raccoons, rats, owls, hawks and cats. Close every small hole, keep woodpiles and junk away, and <b>shut birds in at dusk</b>, letting them out each morning " + c(1) + "."]))
    b.append(h2("feed", "1.3 Feed, water and daily care"))
    b.append(ul(["A 6-pound hen eats roughly <b>3 pounds of feed a week</b>, more in winter and less in summer heat " + c(1) + ".",
                 "Chickens are omnivores — grains, fruit, vegetables, insects and kitchen scraps. Layers need <b>crushed oyster shell</b> (eggshell calcium) and <b>grit</b> for digestion " + c(1) + ". Scratch grains are a treat, not a full diet " + c(1) + ".",
                 "Clean water at all times, especially in summer when they cool themselves by panting " + c(1) + ".",
                 "Daily: feed, fresh water, collect eggs twice. Weekly: clean coop and pen " + c(1) + "."]))
    b.append(tip("Without bagged feed", "Free-range birds forage insects and greens; supplement with grain you grow (see Gardening and Food guides), kitchen scraps, and crushed baked eggshells for calcium. Expect fewer eggs than on balanced feed " + c(1) + "."))
    b.append(h2("hatch", "1.4 Hatching your own chicks"))
    b.append(fig(d_hatch(), "Times and settings from University of Maryland Extension " + c(2) + "."))
    b.append(table(["Bird", "Days", "Temperature", "Humidity"], [["Chicken", "21", "99.5 °F", "55–60% " + c(2)], ["Duck", "28", "99.5 °F", "55–60% " + c(2)], ["Turkey", "28", "99.5 °F", "55–60% " + c(2)], ["Goose", "30", "99.5 °F", "60% " + c(2)], ["Quail", "17–18", "99.5 °F", "55–60% " + c(2)]]))
    b.append(ul(["Turn eggs at least 5–6 times a day so embryos don't stick to the shell — a broody hen does it for you " + c(2) + ".",
                 "Candle after 10 days with a bright light in a dark room and remove infertile or dead eggs — they can spoil the hatch or explode " + c(2) + "."]))
    b.append(tip("Keep a broody hen", "With no power for an incubator, a broody hen is your incubator. Keep a few birds of a breed that still goes broody, and a rooster for fertile eggs."))

    b.append(part("p2", "Part 2", "Poultry Health"))
    b.append(h2("healthy", "2.1 What a healthy bird looks like"))
    b.append(ul(["Active and alert with bright eyes; pecking, scratching and dust-bathing (resting in shade on hot days); quiet talking through the day " + c(1) + ".",
                 "Droppings firm and grayish-brown with white urine salts; about one in ten is foamy, smellier and light brown — that's normal " + c(1) + ".",
                 "Warning signs: not running to food, wheezing or sneezing " + c(1) + "."]))
    b.append(h2("dis", "2.2 Coccidiosis, Marek's and other diseases"))
    b.append(table(["Disease", "Signs", "What you can do"], [
        ["Coccidiosis (gut parasite)", "Ruffled feathers, depression, <b>blood in droppings</b>, shivering, deaths, fewer eggs", "Birds eat the eggs from droppings; moist, warm litter speeds them — keep litter dry, avoid leaking drinkers " + c(3)],
        ["Marek's disease (herpes virus)", "Depression, poor coordination, paralysis of legs and wings, splayed legs, wasting; tumors", "No treatment. Spread by feather dander; vaccine given at day one prevents it — buy vaccinated chicks while you can " + c(3)],
        ["Roundworms", "Poor growth; worms in droppings", "Picked up from the ground; rotate runs and keep clean " + c(3)],
        ["Avian influenza", "Sudden deaths, respiratory signs", "Carried by wild birds — keep wild birds and their droppings away from your flock " + c(4)]]))
    b.append(h2("bio", "2.3 Biosecurity and quarantine"))
    b.append(steps(["<b>Quarantine new or returning birds at least 30 days</b>, at least 100 feet from your flock if possible, and care for them last " + c(4) + ".",
                    "Keep wild birds, rodents and pets out of pens " + c(4) + ".",
                    "Limit visitors; have dedicated boots for the poultry area " + c(4) + ".",
                    "Clean feeders and waterers often and the coop weekly " + c(1) + "."]))

    b.append(part("p3", "Part 3", "Rabbits"))
    b.append(h2("hutch", "3.1 Hutches and nest boxes"))
    b.append(ul(["All-metal cages are most sanitary: <b>1×2-inch mesh</b> sides and top, <b>½×1-inch</b> floor " + c(5) + ".",
                 "Rabbits do not tolerate temperature extremes — give shade, ventilation and protection from sun and rain " + c(5) + ".",
                 "A 12-hour light / 12-hour dark schedule keeps them breeding year-round " + c(5) + ".",
                 "Nest boxes of untreated wood, roomy enough for the doe but snug enough to keep kits together " + c(5) + "."]))
    b.append(h2("breed", "3.2 Breeding calendar"))
    b.append(fig(d_rabbit(), "Dates from Penn State Extension " + c(5) + "."))
    b.append(ul(["Always take the <b>doe to the buck's cage</b> — she will fight to defend her own " + c(5) + ".",
                 "Gestation 31–32 days; put the nest box in on day 28; check and count kits 48 hours after birth; remove the box 5–21 days after birth; wean at about 30 days " + c(5) + ".",
                 "Expect about five litters a year of 8–10 kits; a good doe produces well for 2–3 years " + c(5) + "."]))
    b.append(h2("rfeed", "3.3 Feed, water and health"))
    b.append(ul(["Feed either hay and grain or pellets; bucks and does without litters need about 6–8 oz of pellets a day, while pregnant and nursing does get all they will eat " + c(5) + ".",
                 "Fresh water daily — a doe and litter drink about 1 gallon a day in warm weather; small amounts of greens as treats " + c(5) + ".",
                 "The respiratory disease caused by <i>Pasteurella multocida</i> is a major killer of does; keep visitors out, and isolate sick or new rabbits immediately and disinfect their cages " + c(5) + ".",
                 "Manure can feed worms (vermicomposting) under the hutches and then the garden " + c(5) + "."]))

    b.append(part("p4", "Part 4", "Goats"))
    b.append(h2("fence", "4.1 Fences and shelter"))
    b.append(fig(d_fence(), "Goat-tight fence from Penn State Extension " + c(6) + "."))
    b.append(ul(["Goats are curious climbers and jumpers — fences must be tight " + c(6) + ".",
                 "Horns can tangle in woven wire and badly hurt a goat " + c(6) + ".",
                 "An open shed with <b>10–12 sq ft per doe</b> shelters them in extreme heat or cold " + c(6) + "."]))
    b.append(caution("No power for electric fence?", "Electric net and hot wires work only while energized " + c(6) + ". Plan for a solar fence charger (see the Electricity guide) or build tight woven-wire or wooden fences."))
    b.append(h2("kid", "4.2 Breeding and kidding"))
    b.append(ul(["Gestation <b>148–152 days</b>; wean kids at 2–3 months " + c(6) + ".",
                 "Many kids reach puberty by <b>four months</b> — separate young males and females at weaning to prevent unwanted pregnancies " + c(6) + ".",
                 "Replacement does can be bred at 65–70% of mature weight or one year old " + c(6) + "."]))
    b.append(h2("worms", "4.3 Barberpole worm: the number-one killer"))
    b.append(ul(["Internal parasites are a leading cause of death in sheep and goats; goats are more susceptible to them than other livestock " + c(6, 7) + ".",
                 "The barberpole worm attaches in the stomach and drinks blood, causing severe anemia; it thrives at 50–96 °F, fastest at 86–96 °F " + c(7) + ".",
                 "Dewormer resistance makes eradication unrealistic — and in a collapse you may have no dewormer at all. Prevention by grazing management is everything " + c(7) + "."]))
    b.append(fig(d_eye(), "The FAMACHA idea: eyelid color shows anemia " + c(7) + ". Keep individual records and cull goats that are always pale."))
    b.append(fig(d_rotate(), "Grazing rules from University of Minnesota Extension " + c(7) + "."))

    b.append(part("p5", "Part 5", "Honey Bees"))
    b.append(h2("hive", "5.1 The hive and the apiary"))
    b.append(fig(d_hive(), "Box sizes from University of Missouri Extension; deep-box weight from Mississippi State " + c(8, 9) + "."))
    b.append(ul(["Site: near nectar and pollen, facing <b>east or south with a windbreak to the north</b>; summer afternoon shade from deciduous trees is ideal " + c(8) + ".",
                 "Water: if there is no pond or stream, set out a shallow pan with stones or floating wood so bees can perch — they are poor swimmers " + c(8) + ".",
                 "In town, face the entrance about a foot from a tall fence or hedge so bees fly up and over people " + c(8) + ".",
                 "Gear: veil (strongly recommended for beginners), suit, gloves, hive tool and smoker " + c(9) + "."]))
    b.append(h2("season", "5.2 The bee year and winter stores"))
    b.append(ul(["A strong summer colony reaches about 75,000 bees; drones are expelled in fall " + c(8) + ".",
                 "Each colony needs about <b>40–80 lb of honey for itself</b> to overwinter and can produce 50–100 lb of surplus " + c(8) + ".",
                 "If boxes are light in fall, feed sugar syrup of <b>1 part water to 2 parts sugar</b> " + c(8) + ". Never harvest the brood-box stores " + c(8) + "."]))
    b.append(h2("mites", "5.3 Varroa mites"))
    b.append(ul(["Varroa mites are the most serious threat to honey bees: they feed on adults and pupae and spread viruses that kill colonies " + c(9) + ".",
                 "Mite numbers grow with the colony, so a booming first-year hive can carry dangerous loads by fall " + c(9) + ".",
                 "Non-chemical controls include drone trapping and brood breaks; soft chemicals include formic and oxalic acid and thymol — always follow labels " + c(9) + "."]))

    b.append(part("p6", "Part 6", "Region by Region"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Item", "Value"], [["Coop space", "3–5 sq ft per bird " + c(1)], ["Nest boxes", "1 per 4–5 hens " + c(1)], ["Hen feed", "≈3 lb/week " + c(1)], ["Laying light", "12–14 h/day " + c(1)], ["Chick incubation", "21 days, 99.5 °F, turn 5–6×/day " + c(2)], ["Poultry quarantine", "≥ 30 days " + c(4)], ["Rabbit gestation", "31–32 days; wean ≈30 days " + c(5)], ["Goat gestation", "148–152 days " + c(6)], ["Goat shelter", "10–12 sq ft per doe " + c(6)], ["Paddock move", "≤ 5 days; rest ≈2 months " + c(7)], ["Bee winter stores", "40–80 lb honey " + c(8)], ["Fall syrup", "1 water : 2 sugar " + c(8)]]))
    b.append('<p class="small">General information for emergencies. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Livestock & Small Animals", "Survival Info<br>Livestock &amp;<br>Small Animals",
          "Chickens, rabbits, goats and honey bees: housing, feed, breeding, hatching, common diseases, worms and mites, quarantine and biosecurity — with no vet or feed store, across North America.",
          "Livestock & Small Animals", TOC, cover_art(), "Food · Gardening · Hunting · Preservation · Medical · Sanitation · House")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Livestock.pdf")
