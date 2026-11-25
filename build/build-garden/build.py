import sys, math; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#dcedc8"/><rect y="250" width="720" height="130" fill="#6d4c41"/>'
    s += '<circle cx="610" cy="70" r="40" fill="#fdd835"/>'
    for r in range(3):
        y = 270 + r*35
        s += f'<path d="M20 {y} H700" stroke="#4e342e" stroke-width="6"/>'
    for i in range(9):
        x = 60 + i*75
        s += f'<path d="M{x} 270 V{180 - (i%3)*20}" stroke="#2e7d32" stroke-width="5"/>'
        s += f'<ellipse cx="{x-18}" cy="{215 - (i%3)*10}" rx="20" ry="9" fill="#43a047" transform="rotate(-30 {x-18} {215 - (i%3)*10})"/><ellipse cx="{x+18}" cy="{200 - (i%3)*10}" rx="20" ry="9" fill="#66bb6a" transform="rotate(30 {x+18} {200 - (i%3)*10})"/>'
        if i % 2 == 0: s += f'<circle cx="{x}" cy="{175 - (i%3)*20}" r="11" fill="#e53935"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Climate, Zones and Timing", [("zones","1.1 Hardiness zones in the US and Canada"),("frost","1.2 Planting by the last frost and soil temperature")]),
 ("p2", "Part 2 · Soil", [("jar","2.1 The jar test: what is your soil?"),("ash","2.2 Raising pH with wood ash"),("beds","2.3 Beds, spacing and walkways")]),
 ("p3", "Part 3 · Compost", [("comp","3.1 Building a compost pile"),("heat","3.2 Heat, turning and finishing")]),
 ("p4", "Part 4 · Crop Rotation and Cover Crops", [("rot","4.1 Rotating plant families"),("cover","4.2 Cover crops")]),
 ("p5", "Part 5 · Seed Saving", [("op","5.1 Open-pollinated vs. hybrid"),("save","5.2 Saving tomato, pepper, bean and pea seed"),("store","5.3 Storing seed and cleaning it")]),
 ("p6", "Part 6 · Season Extension", [("cover2","6.1 Row covers and low tunnels"),("frame","6.2 Cold frames and hot beds")]),
 ("p7", "Part 7 · Growing Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_zones():
    s = t(360, 26, "USDA zones = average coldest winter night (°F)", 19, "middle", "700")
    cols = ["#4a148c","#6a1b9a","#3949ab","#1e88e5","#039be5","#00acc1","#26a69a","#66bb6a","#9ccc65","#d4e157","#ffee58","#ffa726","#ef5350"]
    for z in range(1, 14):
        x = 22 + (z-1)*52; lo = -60 + (z-1)*10
        s += rect(x, 50, 50, 70, cols[z-1], "#fff", 1, 3) + t(x + 25, 92, str(z), 20, "middle", "800", "#fff")
        s += t(x + 25, 140, f"{lo}", 12, "middle", "700") + t(x + 25, 155, f"to {lo+10}", 11, "middle")
    s += t(360, 185, "Each zone is a 10 °F band; ‘a’ and ‘b’ split it into 5 °F halves", 14, "middle", "600")
    ex = [("Fairbanks area", 1, 3), ("Minneapolis", 4, 5), ("Denver / Boston", 6, 7), ("Atlanta / Dallas", 8, 8), ("Phoenix / Houston", 9, 10), ("Miami / Puerto Rico", 10, 13)]
    for k, (n, a, b) in enumerate(ex):
        y = 205 + k*26
        s += rect(22 + (a-1)*52, y, (b - a + 1)*52 - 2, 20, "#eceff1", "#90a4ae", 1, 4) + t(22 + (b)*52 + 6, y + 15, n, 13, "start", "600")
    s += t(360, 372, "Rough examples only — read your own zone from the official map before the grid goes down.", 12, "middle")
    return svg(720, 385, s)

def d_frost():
    s = t(360, 26, "When to plant, counted from your AVERAGE LAST SPRING FROST", 18, "middle", "700")
    x0 = 515; sc = 30
    s += line(335, 70, 700, 70, "#455a64", 3)
    for w in range(-6, 7, 2): s += line(x0 + w*sc, 62, x0 + w*sc, 78, "#455a64", 2) + t(x0 + w*sc, 98, f"{w:+d} wk" if w else "FROST", 13, "middle", "700", "#c62828" if w == 0 else INK)
    rows = [("HARDY", "peas, spinach, onions, cabbage,", "broccoli, lettuce, radish, turnip", -4, -2, "#1e88e5"), ("SEMI-HARDY", "beets, carrots, potatoes,", "chard, parsnips, cauliflower", -2, 0, "#26a69a"),
            ("TENDER", "snap beans, corn,", "cucumbers, summer squash", -0.4, 0.6, "#fb8c00"), ("VERY TENDER", "tomatoes, peppers, eggplant,", "melons, winter squash, lima beans", 2, 5, "#e53935")]
    for k, (h, a, b, w1, w2, col) in enumerate(rows):
        y = 120 + k*58
        s += rect(20, y - 6, 305, 52, "#fafafa", "#e0e0e0", 1, 4)
        s += t(30, y + 12, h, 15, "start", "800", col) + t(30, y + 28, a, 13, "start") + t(30, y + 43, b, 13, "start")
        s += rect(x0 + w1*sc, y + 8, (w2 - w1)*sc, 24, col, "none", 0, 4)
    s += line(x0, 104, x0, 350, "#c62828", 2, "6 5")
    s += t(360, 372, "Better still: plant when soil at 4 in deep, 8 a.m., reaches the crop's minimum (table below)", 13, "middle", "600")
    return svg(720, 385, s)

def d_jar():
    s = t(360, 26, "Jar test for soil texture", 19, "middle", "700")
    s += rect(80, 60, 150, 260, "#e3f2fd", "#455a64", 4, 14)
    s += rect(84, 250, 142, 66, "#d7a86e", "none", 0, 0) + rect(84, 195, 142, 55, "#a1887f", "none", 0, 0) + rect(84, 160, 142, 35, "#6d4c41", "none", 0, 0)
    for y, lab, when in [(283, "SAND", "mark after 1 minute"), (222, "SILT", "mark after 2 hours"), (177, "CLAY", "mark after 48 hours")]:
        s += arrow(300, y, 236, y) + t(310, y - 2, lab, 16, "start", "800") + t(310, y + 16, when, 13, "start")
    s += t(560, 90, "1. Fill a straight jar ⅓ with", 13, "middle") + t(560, 108, "sifted soil", 13, "middle")
    s += t(560, 136, "2. Add 1 tsp non-foaming", 13, "middle") + t(560, 154, "dishwasher detergent,", 13, "middle") + t(560, 172, "fill with water, shake hard", 13, "middle")
    s += t(560, 200, "3. Measure each layer;", 13, "middle") + t(560, 218, "% = layer ÷ total × 100", 13, "middle", "700")
    s += rect(430, 240, 260, 70, "#fff8e1", "#e0c070", 1, 6) + t(560, 265, "Loam ≈ a balance of all three:", 13, "middle", "700") + t(560, 285, "holds water but still drains", 13, "middle")
    return svg(720, 340, s)

def d_compost():
    s = t(360, 26, "Lasagna compost pile: 2–3 parts browns to 1 part greens", 18, "middle", "700")
    layers = [("4–6 in twigs / wood chips (air at base)", "#8d6e63"), ("greens: scraps, grass, coffee", "#7cb342"), ("browns: dry leaves, straw, cardboard", "#bcaaa4"),
              ("greens", "#7cb342"), ("browns", "#bcaaa4"), ("greens", "#7cb342"), ("4–8 in browns cap over food", "#bcaaa4")]
    y = 320
    for k, (lab, col) in enumerate(layers):
        h = 40 if k in (0, 6) else 28
        y -= h
        s += rect(80, y, 300, h, col, "#5d4037", 1, 0) + t(230, y + h/2 + 5, lab, 12, "middle", "700", "#fff" if col in ("#8d6e63", "#7cb342") else INK)
    s += t(230, 345, "about 3 ft × 3 ft × 3 ft or larger", 13, "middle", "600")
    s += t(420, 80, "Moist like a wrung-out sponge", 14, "start", "700") + t(420, 110, "Turn the outside in with a fork", 14, "start") + t(420, 140, "Smells bad → add browns, turn", 14, "start") + t(420, 170, "Not heating → add greens, turn", 14, "start") + t(420, 200, "Too dry → water and turn", 14, "start")
    s += rect(410, 225, 290, 95, "#ffebee", "#e57373", 1, 6) + t(555, 248, "NEVER add:", 14, "middle", "800", "#b71c1c") + t(555, 268, "meat, fish, bones, dairy, grease,", 12, "middle") + t(555, 285, "pet waste, diseased plants,", 12, "middle") + t(555, 302, "treated or painted wood", 12, "middle")
    return svg(720, 360, s)

def d_temp():
    s = t(360, 26, "Pile temperature over time: turn to keep it cooking", 18, "middle", "700")
    s += line(80, 300, 680, 300) + line(80, 300, 80, 50)
    def ty(f): return 300 - (f - 50)*2.0
    for f in (70, 90, 140, 160):
        s += line(80, ty(f), 680, ty(f), "#b0bec5", 1, "4 4") + t(72, ty(f) + 5, f"{f}°F", 12, "end", "700")
    s += rect(81, ty(140), 598, ty(90) - ty(140), "#c8e6c9", "none", 0, 0) + t(670, ty(115), "fastest: 90–140 °F", 13, "end", "700", "#2e7d32")
    s += rect(81, ty(175), 598, ty(160) - ty(175), "#ffcdd2", "none", 0, 0) + t(670, ty(167) + 4, "above 160 °F: microbes die, fire risk", 12, "end", "700", "#b71c1c")
    pts = [(80, 70), (120, 120), (160, 150), (220, 145), (280, 110), (300, 108), (340, 140), (400, 135), (460, 105), (480, 104), (530, 120), (600, 85), (680, 70)]
    s += '<polyline points="' + " ".join(f"{x},{ty(f)}" for x, f in pts) + '" fill="none" stroke="#e65100" stroke-width="4"/>'
    for x in (300, 480): s += arrow(x, 280, x, ty(108) + 8, "#1565c0") + t(x, 295, "turn", 12, "middle", "700", "#1565c0")
    s += t(670, ty(62), "below 70 °F and won't reheat after turning = done", 12, "end", "600")
    return svg(720, 320, s)

def d_rot():
    s = t(360, 26, "Four-bed rotation: each family moves one bed per year", 18, "middle", "700")
    beds = [("Pea family", "beans, peas", "#a5d6a7"), ("Mustard family", "cabbage, kale, broccoli, turnip", "#90caf9"), ("Nightshades", "tomato, pepper, potato, eggplant", "#ef9a9a"), ("Gourds + others", "squash, cucumber, corn, onions, carrots", "#ffe082")]
    pos = [(110, 60), (390, 60), (390, 220), (110, 220)]
    for (n, sub, col), (x, y) in zip(beds, pos):
        s += rect(x, y, 230, 120, col, "#5d4037", 3, 8) + t(x + 115, y + 50, n, 16, "middle", "800") + t(x + 115, y + 75, sub[:30], 12, "middle") + (t(x + 115, y + 92, sub[30:].strip(), 12, "middle") if len(sub) > 30 else "")
    s += arrow(342, 120, 386, 120, "#37474f", 4) + arrow(505, 182, 505, 216, "#37474f", 4) + arrow(386, 280, 342, 280, "#37474f", 4) + arrow(225, 216, 225, 182, "#37474f", 4)
    s += t(360, 365, "Same family back in the same bed only every 3–4 years. Keep a map of each year.", 14, "middle", "600")
    return svg(720, 380, s)

def d_seed():
    return flow([["Pick the best OPEN-POLLINATED plants", "vigorous, best-tasting; skip weak or off-type plants"],
                 ["Tomato: scoop seeds + gel into a jar with water", "swirl twice a day; seeds sink within about 5 days"],
                 ["Pour off, rinse, dry on paper", "peppers: dry seeds from fully ripe, wrinkling fruit"],
                 ["Beans/peas: leave pods on the plant until dry", "and rattling; dry 2 more weeks indoors"],
                 ["Store dry and cool (32–41 °F) in sealed glass", "label name, variety, date; use within a year"]], w=720, bh=60, gap=22)

def d_frame():
    s = t(360, 26, "Cold frame (sun-heated) and hot bed (manure-heated)", 18, "middle", "700")
    s += '<polygon points="80,270 80,180 330,130 330,270" fill="#bcaaa4" stroke="#5d4037" stroke-width="3"/>'
    s += line(80, 180, 330, 130, "#64b5f6", 7) + t(205, 140, "old window / clear lid", 13, "middle", "700")
    s += rect(80, 270, 250, 20, "#6d4c41", "none", 0, 0)
    for i in range(5): s += f'<path d="M{110+i*45} 268 v-25" stroke="#2e7d32" stroke-width="4"/><circle cx="{110+i*45}" cy="240" r="8" fill="#66bb6a"/>'
    s += arrow(30, 80, 120, 160, "#f9a825", 3) + t(30, 70, "sun from the SOUTH", 13, "start", "700")
    s += t(205, 315, "low side faces south; vent on sunny days", 13, "middle", "600")
    s += '<polygon points="400,270 400,180 650,130 650,270" fill="#bcaaa4" stroke="#5d4037" stroke-width="3"/>' + line(400, 180, 650, 130, "#64b5f6", 7)
    s += rect(400, 230, 250, 40, "#6d4c41", "none", 0, 0) + t(525, 255, "soil 4–6 in", 12, "middle", "700", "#fff")
    s += rect(400, 270, 250, 50, "#8d6e63", "#4e342e", 2, 0) + t(525, 300, "fresh manure layer = heat", 13, "middle", "700", "#fff")
    s += t(525, 345, "hot bed: buried fresh manure warms the roots", 13, "middle", "600")
    return svg(720, 360, s)

R = {
 1: "Very short, cool seasons: rely on hardy crops — peas, spinach, lettuce, radish, turnips, cabbage, potatoes " + c(3) + " — and on cold frames, row covers and hot beds " + c(11, 12, 13) + ". On the Canadian map Yellowknife is now zone 1b " + c(2) + ".",
 2: "Mild, wet winters let hardy crops grow most of the year under row covers " + c(11, 13) + ". Raise beds for drainage; acid soils may benefit from wood ash — test pH first, at most 10 lb per 100 sq ft per year " + c(9) + ".",
 3: "Hot summers and cold winters; strong drying winds. Plant hardy crops 2–4 weeks before the last frost and very tender crops 2+ weeks after " + c(3) + ". Windbreaks and mulch help; save seed from plants that thrived in your conditions " + c(10) + ".",
 4: "Zones about 3–6 " + c(1) + ". Classic four-bed rotation fits well " + c(4) + "; cold frames and low tunnels add weeks at each end " + c(11, 12) + ".",
 5: "Short to moderate seasons and often acidic soils — test before adding ash " + c(9) + ". Maine's extension recommends cold frames facing south to southeast and row covers to gain time " + c(12) + ".",
 6: "Long, hot summers: cool-season crops lose quality in heat " + c(3) + ", so grow them in fall, winter and early spring and keep summer for beans, corn, squash and tomatoes. Rotation is vital against soil pests and nematodes " + c(4, 5) + ".",
 7: "Zones about 9–11 " + c(1) + ". The main vegetable season is the cooler half of the year; summer heat and rain favor heat-lovers. Very hot soil can stop germination — check the maximum temperatures in the planting table " + c(3) + ".",
 8: "Two seasons: cool crops in fall–winter, warm crops in spring before peak heat " + c(3) + ". Hot soil stops germination of lettuce, peas and spinach above about 70 °F " + c(3) + ". Shade cloth and mulch save water.",
 9: "Short seasons at altitude and frost possible in any month in high valleys — Colorado's extension guide was written for these conditions " + c(3) + ". Use cold frames and row covers " + c(11, 13) + ".",
 10: "Mediterranean climate: cool crops through the mild, wet winter; warm crops in the dry summer with irrigation " + c(3) + ". Zones about 8–10 on the coast and much colder in the Sierra " + c(1) + ".",
 11: "Desert and high plateau: like the Desert Southwest, grow cool crops in the cool months and warm crops in spring and early summer " + c(3) + "; hot soil limits germination " + c(3) + ".",
 12: "Altitude, not latitude, sets the season: cool highlands suit hardy crops while lowlands suit heat-lovers " + c(3) + ". Plant with the rains; save seed from local open-pollinated varieties " + c(10) + ".",
 13: "Frost-free lowlands (zones 10–13 in Puerto Rico " + c(1) + "); timing follows wet and dry seasons. Heat limits cool-season crops " + c(3) + "; rotate to break soil pest cycles " + c(5) + ".",
}

def body():
    b = []
    b.append(part("p1", "Part 1", "Climate, Zones and Timing"))
    b.append('<p>A garden is the most reliable long-term food source once stores are gone. This guide covers growing vegetables from your own saved seed, building soil with compost and ash, and stretching the season with frames and covers — with no stores, labs or hired help. See the Food guide for calorie crops and the Preservation guide for keeping the harvest.</p>')
    b.append(h2("zones", "1.1 Hardiness zones in the US and Canada"))
    b.append(fig(d_zones(), "USDA zones are based on the average annual extreme minimum winter temperature, 1991–2020 " + c(1) + "."))
    b.append(ul(["The USDA map divides the US and Puerto Rico into 13 zones, each a 10 °F band of average coldest winter temperature, split into 5 °F half-zones ‘a’ and ‘b’ " + c(1) + ".",
                 "Canada has its own plant hardiness zone map from Natural Resources Canada, updated in 2025; many areas shifted half a zone or more — Yellowknife moved from zone 0b to 1b " + c(2) + ".",
                 "Zones matter most for perennials (fruit trees, berries, asparagus). For annual vegetables, the <b>frost dates and soil temperature</b> matter more " + c(3) + ".",
                 "<b>Before the internet goes:</b> write your zone and your average last spring and first fall frost dates on the inside cover of this guide."]))
    b.append(h2("frost", "1.2 Planting by the last frost and soil temperature"))
    b.append(fig(d_frost(), "Groups and timing from Colorado State University Extension " + c(3) + "."))
    b.append(table(["Crop", "Min. soil °F", "Depth", "Spacing", "Days to harvest"], [
        ["Peas", "40", "1 in", "4–6 in", "65 " + c(3)], ["Spinach", "40", "½ in", "4–6 in", "40 " + c(3)], ["Lettuce (leaf)", "35", "¼ in", "7–9 in", "60 " + c(3)],
        ["Radish", "40", "½ in", "2–3 in", "30 " + c(3)], ["Carrots", "40", "¼ in", "2–3 in", "70 " + c(3)], ["Beets", "40", "¾–1 in", "4–6 in", "60 " + c(3)],
        ["Potatoes", "45", "4–6 in", "12–15 in", "125 " + c(3)], ["Snap beans", "55", "1–1½ in", "6 in", "60 " + c(3)], ["Corn", "50", "1–1½ in", "12×30 in", "60–90 " + c(3)],
        ["Winter squash", "60", "1–1½ in", "36–48 in", "100 " + c(3)], ["Tomato (transplant)", "50", "¼ in", "24 in trellised", "65 from transplant " + c(3)]]))
    b.append(tip("Measuring soil temperature", "Measure at 8 a.m., 4 inches deep (beans at 6 inches), and plant when soil reaches the crop's minimum " + c(3) + ". Without a thermometer, wait for the frost date window above."))

    b.append(part("p2", "Part 2", "Soil"))
    b.append(h2("jar", "2.1 The jar test: what is your soil?"))
    b.append(fig(d_jar(), "Clemson Extension jar test " + c(8) + "."))
    b.append(ul(["<b>Sandy</b> soil drains fast and dries out: add compost every year to hold water.", "<b>Clay</b> soil holds water and packs hard: add compost, never work it wet, and use raised beds.", "Whatever the texture, <b>organic matter (compost)</b> is the fix — see Part 3. Block-style beds work best on soils improved to 4–5% organic matter " + c(3) + "."]))
    b.append(h2("ash", "2.2 Raising pH with wood ash"))
    b.append(ul(["Wood ash contains calcium, potassium, magnesium and trace elements, and acts like lime to raise pH on acid soils " + c(9) + ".",
                 "<b>Limit: no more than 10 lb per 100 sq ft per year.</b> Sift it, apply about two weeks before planting, on moist soil, raked in lightly " + c(9) + ".",
                 "<b>Do not use</b> on soils above pH 7.0, on blueberries, rhododendrons or azaleas, or at seeding time (salts burn seedlings) " + c(9) + ".",
                 "Never use ash from trash, cardboard, coal, barbecue charcoal or treated, painted or stained wood " + c(9) + "."]))
    b.append(caution("Ash is caustic", "Handle wood ash like lye or bleach: eye protection, gloves, dust mask, closed shoes; never spread on windy days " + c(9) + ". Too much in one spot can effectively sterilize the soil " + c(9) + "."))
    b.append(h2("beds", "2.3 Beds, spacing and walkways"))
    b.append('<p>Block or close-row beds <b>2–4 feet wide</b>, any length, with <b>2-foot walkways</b>, let you reach the middle without stepping on and compacting the soil ' + c(3) + '. Plants are spaced equally in all directions (e.g. beets 6 inches apart each way) ' + c(3) + '.</p>')

    b.append(part("p3", "Part 3", "Compost"))
    b.append(h2("comp", "3.1 Building a compost pile"))
    b.append(fig(d_compost(), "EPA backyard composting method " + c(6) + "."))
    b.append(steps(["Pick a spot with good drainage, easy to reach all year, with water nearby; sun or shade both work " + c(6) + ".",
                    "Start with a <b>4–6 inch layer of twigs or wood chips</b> for air and drainage " + c(6) + ".",
                    "Layer greens and browns like lasagna, using <b>at least two to three times as much brown as green by volume</b>; always bury food scraps under 4–8 inches of browns " + c(6) + ".",
                    "Keep it as moist as a wrung-out sponge and turn it from time to time " + c(6) + "."]))
    b.append(h2("heat", "3.2 Heat, turning and finishing"))
    b.append(fig(d_temp(), "Temperatures from Cornell's composting fact sheet " + c(7) + "; the curve is illustrative."))
    b.append(ul(["A well-kept backyard pile can reach 130–160 °F, which reduces pathogens and weed seeds " + c(6) + ".",
                 "Decomposition is fastest between 90 and 140 °F; above 160 °F the pile can kill its own microbes and even risk spontaneous combustion — turn it when it passes 140 °F " + c(7) + ".",
                 "When it no longer heats after turning and no food scraps show, let it cure at least four weeks. A tended pile is ready in about 3–5 months; untended, about a year " + c(6) + "."]))

    b.append(part("p4", "Part 4", "Crop Rotation and Cover Crops"))
    b.append(h2("rot", "4.1 Rotating plant families"))
    b.append(fig(d_rot(), "Plant families from UW–Madison Extension " + c(4) + "."))
    b.append(table(["Family", "Crops"], [["Nightshade", "tomato, pepper, potato, eggplant " + c(4)], ["Mustard (brassicas)", "cabbage, broccoli, kale, collards, radish, turnip, rutabaga " + c(4)], ["Gourd", "cucumber, melons, pumpkin, squash " + c(4)], ["Pea (legumes)", "beans, peas, soybean " + c(4)], ["Onion", "onion, garlic, leek, chives " + c(4)], ["Carrot", "carrot, celery, parsley, parsnip " + c(4)], ["Goosefoot", "beet, spinach, chard " + c(4)], ["Grass", "corn " + c(4)]]))
    b.append('<p>Do not plant the same family in the same spot more than once every <b>three to four years</b>; even changing families every year helps against pests and disease ' + c(4, 5) + '. Keep a written map of each year\'s beds ' + c(4) + '.</p>')
    b.append(h2("cover", "4.2 Cover crops"))
    b.append('<p>Sow a cover crop on beds that would otherwise sit bare, and include cover crops in the rotation — a cover crop counts as its family (for example, peas and clover are legumes) ' + c(4, 5) + '. Turn it into the soil before it sets seed.</p>')

    b.append(part("p5", "Part 5", "Seed Saving"))
    b.append(h2("op", "5.1 Open-pollinated vs. hybrid"))
    b.append(ul(["Save seed only from <b>open-pollinated</b> (including heirloom) varieties: their seed grows plants like the parent " + c(10) + ".",
                 "Seed from <b>hybrids</b> (such as ‘Big Boy’ or ‘Early Girl’ tomatoes) grows, but the plants are an unpredictable mix " + c(10) + ".",
                 "Easiest: <b>tomatoes, peppers, beans and peas</b> — they self-pollinate " + c(10) + ". Harder: corn and squash family, which cross-pollinate by wind or insects; carrots and beets need two seasons to make seed " + c(10) + "."]))
    b.append(caution("Stockpile the right seed now", "Hybrid seed packets are useless for a second generation. Buy open-pollinated varieties now (e.g. ‘Brandywine’ or ‘San Marzano’ tomato, ‘Kentucky Wonder’ or ‘Blue Lake’ bean, ‘Little Marvel’ pea) " + c(10) + "."))
    b.append(h2("save", "5.2 Saving tomato, pepper, bean and pea seed"))
    b.append(fig(d_seed(), "Steps from University of Minnesota Extension " + c(10) + "."))
    b.append(h2("store", "5.3 Storing seed and cleaning it"))
    b.append(ul(["Store in tightly sealed glass, cool and dry; <b>32–41 °F</b> is ideal " + c(10) + ".",
                 "Add a desiccant: silica gel, or 1–2 tablespoons of fresh powdered milk wrapped in cloth or tissue (works about six months) " + c(10) + ".",
                 "Label with name, variety and date; seed loses germination and vigor with age — plan to use it within a year and keep growing it out " + c(10) + ".",
                 "To clean suspect seed: 1 part 5.25% bleach to 4 parts water with a few drops of dish soap, 1 minute, then rinse 5 minutes in cool water " + c(10) + "."]))

    b.append(part("p6", "Part 6", "Season Extension"))
    b.append(h2("cover2", "6.1 Row covers and low tunnels"))
    b.append(ul(["Floating row covers keep plants about 5–10 °F warmer and give frost protection down to about 28 °F; they also block insects " + c(11, 12) + ".",
                 "On wire hoops (low tunnels) they give about 4–5 °F of frost protection " + c(13) + ".",
                 "Secure all edges against wind " + c(12) + ". Uncover for pollination of crops that need insects, and slit or open tunnels before temperatures inside top 90 °F " + c(12, 13) + "."]))
    b.append(h2("frame", "6.2 Cold frames and hot beds"))
    b.append(fig(d_frame(), "Cold frame and hot bed designs from extension handbooks " + c(12, 13) + "."))
    b.append(ul(["A cold frame is a bottomless box with a glass or clear plastic lid that opens for ventilation — an old window works " + c(12) + ".",
                 "Face it south to southeast on well-drained soil, with a wall or hedge to the north if possible; sinking it into the ground adds insulation " + c(12, 13) + ".",
                 "<b>Ventilate on sunny days</b> or it overheats; close it early enough each afternoon to hold heat for the night " + c(12, 13) + ".",
                 "Uses: harden off seedlings, start crops weeks early, grow salad greens into winter, store root crops " + c(11, 13) + ".",
                 "A <b>hot bed</b> adds heat from fresh manure buried beneath the root zone " + c(13) + "."]))

    b.append(part("p7", "Part 7", "Growing Region by Region"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Value"], [["Hardy crops", "2–4 wk before last frost " + c(3)], ["Very tender crops", "2+ wk after last frost " + c(3)], ["Soil temp", "8 a.m., 4 in deep " + c(3)], ["Compost mix", "2–3 browns : 1 green by volume " + c(6)], ["Compost heat", "best 90–140 °F; turn above 140 °F " + c(7)], ["Wood ash", "≤ 10 lb / 100 sq ft / yr; not above pH 7 " + c(9)], ["Rotation", "same family every 3–4 yr " + c(4)], ["Seed storage", "32–41 °F, sealed, dry " + c(10)], ["Row cover", "+5–10 °F, to ~28 °F " + c(11)], ["Beds", "2–4 ft wide, 2 ft paths " + c(3)]]))
    b.append('<p class="small">General information for emergencies. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Gardening & Seed Saving", "Survival Info<br>Gardening &amp;<br>Seed Saving",
          "Growing zones and frost dates, soil testing with a jar, compost, wood ash, crop rotation, saving your own seed, and stretching the season with row covers, cold frames and hot beds — for every region of North America.",
          "Gardening & Seed Saving", TOC, cover_art(), "Food · Preservation · Water · Sanitation · Tools · House · Weather")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Gardening.pdf")
