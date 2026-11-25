import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#3b2a1e"/>'
    s += '<rect x="0" y="300" width="720" height="80" fill="#6d4c41"/>'
    cols = ["#c0392b", "#e69b00", "#7cb342", "#d35400", "#8e24aa"]
    for i in range(5):
        x = 70 + i*120
        s += f'<rect x="{x}" y="150" width="90" height="150" rx="14" fill="{cols[i]}" stroke="#eceff1" stroke-width="4"/><rect x="{x-4}" y="134" width="98" height="22" rx="4" fill="#b0bec5" stroke="#78909c" stroke-width="2"/>'
        s += f'<rect x="{x+10}" y="200" width="70" height="40" rx="4" fill="#fff8e1"/>'
    s += '<path d="M40 60 h640" stroke="#a1887f" stroke-width="5"/>'
    for i in range(7): s += f'<path d="M{80+i*90} 60 v40" stroke="#a1887f" stroke-width="2"/><ellipse cx="{80+i*90}" cy="110" rx="14" ry="10" fill="#c62828"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Why Food Spoils — and Botulism", [("bot","1.1 Botulism: the deadly one"),("acid","1.2 Acid foods and low-acid foods"),("spoil","1.3 Spotting spoiled jars and getting rid of them")]),
 ("p2", "Part 2 · Canning", [("jars","2.1 Jars, lids and headspace"),("bw","2.2 Boiling-water canning step by step"),("pc","2.3 Pressure canning step by step"),("alt","2.4 Altitude adjustments"),("times","2.5 USDA process times"),("seal","2.6 Testing seals and storing jars")]),
 ("p3", "Part 3 · Drying", [("sun","3.1 Sun drying fruit"),("jerky","3.2 Jerky"),("drystore","3.3 Conditioning and storing dried food")]),
 ("p4", "Part 4 · Salting, Curing & Smoking", [("ham","4.1 Dry-curing a ham"),("fish","4.2 Brining and smoking fish")]),
 ("p5", "Part 5 · Fermenting", [("kraut","5.1 Sauerkraut"),("crock","5.2 Crocks, covers and weights")]),
 ("p6", "Part 6 · Root Cellars & Cold Storage", [("groups","6.1 The four storage groups"),("cellar","6.2 Running a root cellar")]),
 ("p7", "Part 7 · Long-Term Grain & Dry Storage", [("grain","7.1 Packing grain, rice and beans"),("life","7.2 How long it lasts")]),
 ("p8", "Part 8 · Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_acid():
    s = t(360, 28, "Acidity decides the method (pH scale)", 19, "middle", "700")
    for i in range(8):
        col = ["#c62828","#e53935","#ef6c00","#f9a825","#c0ca33","#7cb342","#43a047","#1e88e5"][i]
        s += rect(40 + i*80, 60, 80, 50, col, "#fff", 2, 0) + t(80 + i*80, 92, str(i+2), 18, "middle", "700", "#fff")
    x46 = 80 + (4.6-2)*80
    s += line(x46, 50, x46, 130, "#000", 5) + t(x46, 150, "pH 4.6", 18, "middle", "800")
    s += label_box(30, 170, 300, 120, ["ACID (pH 4.6 or lower)", "fruits, pickles, sauerkraut,", "jams, acidified tomatoes", "→ boiling-water canner OK"], "#fff3e0", 16)
    s += label_box(390, 170, 300, 120, ["LOW-ACID (above pH 4.6)", "all fresh vegetables, meat,", "poultry, fish, milk, soups", "→ PRESSURE CANNER ONLY"], "#e3f2fd", 16)
    s += t(360, 320, "Tomatoes and figs sit near 4.6 — add bottled lemon juice or citric acid", 16, "middle", "600")
    return svg(720, 340, s)

def d_bw():
    s = t(360, 28, "Boiling-water canner", 19, "middle", "700")
    s += '<path d="M150 90 h420 v260 q0 20 -20 20 h-380 q-20 0 -20 -20z" fill="#eceff1" stroke="#37474f" stroke-width="4"/>'
    s += rect(140, 70, 440, 22, "#90a4ae", "#37474f", 3, 6)
    s += rect(150, 120, 420, 228, "#bbdefb", "none", 0, 0)
    for i in range(4):
        x = 185 + i*95
        s += rect(x, 180, 70, 150, "#ffb74d", "#5d4037", 3, 12) + rect(x-2, 170, 74, 14, "#b0bec5", "#546e7a", 2, 3)
    s += line(160, 334, 560, 334, "#455a64", 6) + t(600, 340, "rack", 15, "start", "600")
    s += line(160, 130, 560, 130, "#1565c0", 2, "6 4") + t(600, 136, "water level", 15, "start", "600")
    s += arrow(620, 150, 620, 168, "#1565c0") + t(600, 190, "≥1 in over jars", 15, "start") + t(600, 210, "(2 in if > 30 min)", 15, "start")
    for i in range(6): s += f'<path d="M{200+i*65} 395 q8 -12 0 -24 q-8 -12 0 -24" fill="none" stroke="#e65100" stroke-width="4"/>'
    s += t(360, 420, "Keep a full, rolling boil the whole time — if it stops, restart the timing", 16, "middle", "600")
    return svg(720, 430, s)

def d_pc():
    s = t(360, 28, "Pressure canner: parts and the 10-minute vent", 19, "middle", "700")
    s += '<path d="M190 120 h340 v230 q0 20 -20 20 h-300 q-20 0 -20 -20z" fill="#eceff1" stroke="#37474f" stroke-width="4"/>'
    s += '<path d="M180 120 q180 -60 360 0z" fill="#b0bec5" stroke="#37474f" stroke-width="4"/>'
    s += '<circle cx="300" cy="92" r="22" fill="#fff" stroke="#37474f" stroke-width="4"/>' + line(300, 92, 312, 80, "#c62828", 3)
    s += rect(405, 70, 22, 22, "#455a64", "#263238", 2, 3)
    s += t(120, 70, "dial gauge", 16, "end", "700") + arrow(124, 66, 278, 86)
    s += t(600, 60, "vent / weight", 16, "start", "700") + arrow(596, 62, 430, 78)
    s += t(600, 112, "safety plug", 16, "start") + arrow(596, 112, 470, 112)
    s += rect(190, 310, 340, 40, "#bbdefb", "none", 0, 0) + t(360, 336, "2–3 in of hot water", 15, "middle", "600", "#0d47a1")
    for i in range(3): x = 230 + i*95; s += rect(x, 170, 70, 140, "#a5d6a7", "#2e7d32", 3, 12)
    s += flow(["Steam flows freely", "Vent 10 min", "Weight on / petcock shut", "Time at pressure", "Cool on its own to 0"], 720, 60, 14, "#fff8e1").replace('<svg', '<g').replace('</svg>', '</g>') if False else ""
    steps_ = ["1 Steam flows", "2 Vent 10 min", "3 Close vent", "4 Time at", "5 Cool by itself"]
    sub = ["freely", "full heat", "pressure builds", "pressure", "to zero"]
    for i in range(5):
        x = 10 + i*142
        s += rect(x, 390, 130, 60, "#fff8e1", "#e69b00", 2, 8) + t(x+65, 415, steps_[i], 15, "middle", "700") + t(x+65, 437, sub[i], 14, "middle")
        if i < 4: s += arrow(x+130, 420, x+142, 420)
    return svg(720, 470, s)

def d_head():
    s = t(360, 28, "Headspace: the gap between food and lid", 19, "middle", "700")
    data = [("¼ in", "jams & jellies", 12), ("½ in", "fruits & tomatoes", 24), ("1–1¼ in", "low-acid, pressure", 52)]
    for i, (h, lab, gap) in enumerate(data):
        x = 90 + i*210
        s += f'<rect x="{x}" y="70" width="110" height="200" rx="16" fill="#fff" stroke="#37474f" stroke-width="4"/>'
        s += rect(x+4, 70 + 10 + gap, 102, 186 - gap, ["#ef5350", "#ffb74d", "#81c784"][i], "none", 0, 12)
        s += rect(x-4, 58, 118, 16, "#b0bec5", "#546e7a", 2, 3)
        s += line(x+125, 76, x+125, 80+gap, "#c62828", 3) + line(x+118, 76, x+132, 76, "#c62828", 3) + line(x+118, 80+gap, x+132, 80+gap, "#c62828", 3)
        s += t(x+55, 300, h, 22, "middle", "800", "#c62828") + t(x+55, 326, lab, 16, "middle", "600")
    return svg(720, 345, s)

def d_alt():
    s = t(360, 28, "Dial-gauge pressure by altitude (most USDA foods)", 19, "middle", "700")
    vals = [("0–2,000 ft", 11), ("2,001–4,000", 12), ("4,001–6,000", 13), ("6,001–8,000", 14)]
    for i, (lab, v) in enumerate(vals):
        y = 60 + i*62
        s += t(170, y+30, lab, 16, "end", "600") + rect(180, y, v*32, 44, "#42a5f5", "#1565c0", 2, 4) + t(190 + v*32, y+30, f"{v} lb", 18, "start", "800")
    s += t(360, 330, "Weighted-gauge canner: 10 lb at 0–1,000 ft; 15 lb above 1,000 ft", 17, "middle", "700", "#c62828")
    s += t(360, 356, "Boiling-water times go UP with altitude (see each table)", 16, "middle")
    return svg(720, 370, s)

def d_sun():
    s = t(360, 28, "Sun-drying rack: two food-safe screens, off the ground", 19, "middle", "700")
    s += '<circle cx="640" cy="70" r="30" fill="#ffd54f"/>'
    s += rect(80, 250, 560, 20, "#9e9e9e", "#616161", 2, 2) + t(360, 300, "metal sheet or concrete underneath reflects heat", 16, "middle")
    for x in (110, 330, 590): s += rect(x, 190, 30, 60, "#8d6e63", "#5d4037", 2, 2)
    s += line(90, 190, 630, 190, "#455a64", 4) + line(90, 150, 630, 150, "#455a64", 2, "4 4")
    for i in range(9): s += f'<ellipse cx="{120+i*60}" cy="182" rx="22" ry="7" fill="#ffb74d"/>'
    s += t(90, 140, "cover screen / cheesecloth keeps out insects and birds", 15, "start", "600")
    s += t(360, 322, "shelf screen: stainless steel, Teflon-coated fiberglass or plastic", 15, "middle")
    s += t(360, 348, "NOT hardware cloth (zinc/cadmium), copper or aluminum screen", 16, "middle", "700", "#c62828")
    s += t(360, 374, "Fruit only · ≥ 85 °F · humidity under 60% · bring in at night", 16, "middle", "700")
    return svg(720, 390, s)

def d_jerky():
    s = t(360, 28, "Safe jerky: reach 160 °F, then dry", 19, "middle", "700")
    items = [("Freeze pork/game", "6 in or less thick,", "0 °F, 30+ days"), ("Slice ≤ ¼ in", "trim all fat", ""), ("Marinate", "in the cold", "1–2 h or overnight"), ("Boil strips", "in marinade", "5 minutes (160 °F)"), ("Dry at 140 °F", "until it bends", "and cracks")]
    for i, (a, b2, c2) in enumerate(items):
        x = 10 + i*142
        s += rect(x, 60, 130, 120, ["#e3f2fd","#fff3e0","#f3e5f5","#ffebee","#e8f5e9"][i], "#37474f", 2, 10)
        s += t(x+65, 95, a, 15, "middle", "700") + t(x+65, 125, b2, 14, "middle") + t(x+65, 147, c2, 14, "middle")
        if i < 4: s += arrow(x+130, 120, x+142, 120)
    s += t(360, 215, "Alternative to step 4: heat the finished dried strips in an oven to 160 °F", 15, "middle", "600")
    return svg(720, 230, s)

def d_fish():
    s = t(360, 28, "Smoked fish: the safety steps (PNW 238)", 19, "middle", "700")
    items = [("Brine", "1 cup salt :", "7 cups water, cold"), ("Rinse, air-dry", "until shiny", "pellicle (≥1 h)"), ("Smoke", "build heat", "gradually"), ("Cook", "thickest piece", "160 °F ≥ 30 min"), ("Keep cold", "38 °F or less", "or eat soon")]
    for i, (a, b2, c2) in enumerate(items):
        x = 10 + i*142
        s += rect(x, 60, 130, 120, ["#e3f2fd","#fffde7","#eceff1","#ffebee","#e0f7fa"][i], "#37474f", 2, 10)
        s += t(x+65, 95, a, 16, "middle", "700") + t(x+65, 125, b2, 14, "middle") + t(x+65, 147, c2, 14, "middle")
        if i < 4: s += arrow(x+130, 120, x+142, 120)
    s += t(360, 215, "Salt (≥ 3.5% water-phase salt) + heat + cold storage — all three are needed", 15, "middle", "600")
    return svg(720, 230, s)

def d_crock():
    s = t(360, 28, "Fermenting crock (cross-section)", 19, "middle", "700")
    s += '<path d="M200 80 h320 v290 q0 20 -20 20 h-280 q-20 0 -20 -20z" fill="#efebe9" stroke="#5d4037" stroke-width="5"/>'
    s += rect(206, 170, 308, 214, "#c5e1a5", "none", 0, 10)
    s += rect(206, 140, 308, 30, "#b3e5fc", "none", 0, 0)
    s += rect(230, 150, 260, 12, "#fff", "#455a64", 2, 4)
    s += '<path d="M240 150 q120 -70 240 0z" fill="#e1f5fe" stroke="#0277bd" stroke-width="3"/>'
    s += line(190, 70, 530, 70, "#8d6e63", 6)
    s += t(560, 72, "clean towel over top", 15, "start", "600")
    s += t(560, 118, "brine-filled bag (weight)", 15, "start") + arrow(556, 116, 470, 128)
    s += t(560, 158, "plate", 15, "start") + arrow(556, 156, 492, 156)
    s += t(560, 200, "brine: keep food", 15, "start", "600") + t(560, 220, "1–2 in under", 15, "start", "600") + arrow(556, 205, 516, 160)
    s += t(560, 290, "shredded cabbage", 15, "start") + t(560, 310, "+ salt", 15, "start")
    s += t(150, 130, "rim 4–5 in", 15, "end", "600") + t(150, 150, "above food", 15, "end", "600")
    s += t(360, 420, "1 gallon of crock per 5 lb of vegetables · 70–75 °F · 3–4 weeks", 16, "middle", "700")
    return svg(720, 430, s)

def d_groups():
    s = t(360, 28, "The four storage groups (WSU, MU Extension)", 19, "middle", "700")
    g = [("COLD & VERY MOIST", "32–40 °F · 90–95% RH", "carrots, beets, parsnips,", "turnips, rutabagas, leeks", "#b3e5fc"),
         ("COLD & MOIST", "32–40 °F · 80–90% RH", "potatoes (38–40 °F), apples,", "cabbage — fruit kept apart", "#c8e6c9"),
         ("COLD & DRY", "32–50 °F · 60–70% RH", "dry beans, storage onions,", "garlic", "#fff9c4"),
         ("COOL & DRY", "50–60 °F · 60–70% RH", "pumpkins, winter squash", "(sweet potatoes: ≥ 50 °F, moist)", "#ffe0b2")]
    for i, (a, b2, c1, c2, col) in enumerate(g):
        x = 20 + (i % 2)*350; y = 50 + (i // 2)*150
        s += rect(x, y, 330, 135, col, "#37474f", 2, 10) + t(x+165, y+30, a, 18, "middle", "800") + t(x+165, y+58, b2, 16, "middle", "700") + t(x+165, y+88, c1, 15, "middle") + t(x+165, y+110, c2, 15, "middle")
    return svg(720, 360, s)

def d_cellar():
    s = t(360, 28, "Simple root cellar: cold, damp, dark, ventilated", 19, "middle", "700")
    s += rect(0, 120, 720, 300, "#a1887f", "none", 0, 0) + rect(0, 110, 720, 12, "#7cb342", "none", 0, 0)
    s += rect(160, 160, 400, 230, "#efebe9", "#4e342e", 6, 4)
    s += rect(200, 100, 24, 90, "#90a4ae", "#455a64", 2, 0) + t(212, 92, "inlet (low)", 15, "middle", "600") + arrow(212, 120, 212, 360, "#1e88e5")
    s += rect(500, 70, 24, 100, "#90a4ae", "#455a64", 2, 0) + t(512, 62, "outlet (high)", 15, "middle", "600") + arrow(512, 175, 512, 85, "#c62828")
    for j in range(3): s += line(260, 220 + j*55, 470, 220 + j*55, "#6d4c41", 6)
    for j in range(3):
        for k in range(5): s += f'<ellipse cx="{280+k*42}" cy="{208+j*55}" rx="16" ry="10" fill="{["#ff8a65","#c5e1a5","#ffcc80"][j]}"/>'
    s += t(360, 410, "dirt floor or pans of water keep humidity high · screen vents against rodents", 15, "middle", "600", "#fff")
    s += t(600, 250, "thermometers", 15, "start", "600") + t(600, 270, "top and bottom", 15, "start")
    return svg(720, 425, s)

def d_bucket():
    s = t(360, 28, "Packing dry food for the long haul", 19, "middle", "700")
    s += '<path d="M220 90 h280 l-20 290 h-240z" fill="#eceff1" stroke="#37474f" stroke-width="4"/>' + rect(210, 72, 300, 22, "#90a4ae", "#37474f", 3, 4)
    s += '<path d="M250 110 h220 l-14 255 h-192z" fill="#cfd8dc" stroke="#78909c" stroke-width="3" stroke-dasharray="8 5"/>'
    for i in range(60): s += f'<ellipse cx="{265 + (i*37)%190}" cy="{150 + (i*53)%200}" rx="5" ry="3" fill="#d7b98e"/>'
    s += rect(340, 120, 40, 24, "#fff", "#c62828", 2, 4) + t(360, 137, "O₂", 14, "middle", "700", "#c62828")
    s += t(560, 100, "airtight lid", 15, "start", "600") + arrow(556, 96, 512, 84)
    s += t(560, 150, "oxygen absorber", 15, "start", "600") + arrow(556, 146, 382, 132)
    s += t(560, 210, "Mylar-type bag", 15, "start", "600") + arrow(556, 206, 466, 206)
    s += t(560, 270, "dry grain, rice,", 15, "start") + t(560, 290, "beans (≤ 10% moisture)", 15, "start")
    s += t(160, 200, "food-grade", 15, "end", "600") + t(160, 220, "bucket", 15, "end", "600")
    s += t(360, 415, "Cool (40–60 °F), dark, dry, off the floor, safe from rodents", 16, "middle", "700")
    return svg(720, 430, s)

PC = [["Snap & Italian beans (pieces)", "Hot or raw", "20 min", "25 min", c(4)],
      ["Carrots (sliced/diced)", "Hot or raw", "25", "30", c(4)],
      ["Corn, whole kernel", "Hot or raw", "55", "85", c(4)],
      ["White potatoes (cubed/whole)", "Hot", "35", "40", c(4)],
      ["Sweet potatoes", "Hot", "65", "90", c(4)],
      ["Dry beans or peas (soaked, boiled 30 min)", "Hot", "75", "90", c(4)],
      ["Chicken or rabbit, with bones", "Hot or raw", "65", "75", c(5)],
      ["Chicken or rabbit, without bones", "Hot or raw", "75", "90", c(5)],
      ["Meat strips/cubes (beef, pork, venison, bear, lamb)", "Hot or raw", "75", "90", c(5)],
      ["Ground or chopped meat", "Hot", "75", "90", c(5)],
      ["Meat stock (broth)", "Hot", "20", "25", c(5)],
      ["Fatty fish (salmon, trout, mackerel…)", "Raw", "100 (pints only)", "—", c(5)]]
BW = [["Crushed tomatoes (acidified)", "Hot", "Pints 35 · Quarts 45", "40 · 50", "45 · 55", "50 · 60", c(3)],
      ["Applesauce", "Hot", "Pints 15 · Quarts 20", "20 · 25", "20 · 30", "25 · 35", c(2)],
      ["Apples, sliced", "Hot", "Pints or quarts 20", "25", "30", "35", c(2)],
      ["Peaches, halved/sliced", "Hot", "Pints 20 · Quarts 25", "25 · 30", "30 · 35", "35 · 40", c(2)],
      ["Peaches, halved/sliced", "Raw", "Pints 25 · Quarts 30", "30 · 35", "35 · 40", "40 · 45", c(2)],
      ["Sauerkraut", "Hot", "Pints 10 · Quarts 15", "15 · 20", "15 · 20", "20 · 25", c(10)],
      ["Sauerkraut", "Raw", "Pints 20 · Quarts 25", "25 · 30", "30 · 35", "35 · 40", c(10)]]

R = {
 1: "Cold is your freezer for much of the year, and root cellars work very well in cold soils " + c(15) + " — but they still need a heat source (as little as a 100-watt bulb in the UAF guide) so produce does not freeze " + c(15) + ". Smoked and dried fish are staples; follow the brine-and-heat rules in 4.2 " + c(12) + ". CDC: people in Alaska with botulism usually got it from traditional fermented foods — boil home-fermented Alaska Native foods before eating " + c(6) + ".",
 2: "Damp, mild air makes sun drying unreliable — dry indoors near a stove. Salmon runs make smoking and pressure-canning fish the big jobs; PNW 238 was written for this region " + c(12) + ". Cool basements and garages make good cold rooms " + c(16) + ".",
 3: "Dry air and sun dry fruit well; hard winters make root cellars and cold storage easy. Prairie grain (wheat) stores for decades when kept dry and cool " + c(17, 18) + ". Protect stores from mice in grain country.",
 4: "Big gardens and orchards: pressure-can vegetables, ferment cabbage in fall (kraut needs 70–75 °F, so start before the house gets cold) " + c(10) + ", and use the root cellar for potatoes, carrots and apples " + c(14) + ".",
 5: "Classic root-cellar country; apples and cabbage store well cold and moist " + c(14, 16) + ". Fish and game can be salted, smoked or pressure canned. Plan curing for winter: Virginia Extension says early December is the best time to start curing hams under ambient conditions " + c(13) + ".",
 6: "Heat and humidity are the enemies. NCHFP notes high humidity in the South is a problem for outdoor drying " + c(8) + "; dry indoors. Keep canned food below 95 °F " + c(1) + " — store it in the coolest, lowest room. Dry-curing needs 36–40 °F " + c(13) + ", which only happens in winter here.",
 7: "Hot and humid all year: canning and well-sealed dry storage beat drying and curing. Jars stored above 95 °F lose quality and may spoil " + c(1) + ". Few places stay cold enough for a root cellar; grow crops you can harvest year-round instead.",
 8: "Ideal sun-drying weather (hot, dry, breezy) " + c(8) + ". Much of the region is above 1,000 ft: add canning time or pressure for altitude (2.4) " + c(1) + ". Daytime heat can spoil stored food — dig storage into the ground or use north-facing rooms.",
 9: "High altitude everywhere: use the altitude columns in every table, and run weighted-gauge canners at 15 lb above 1,000 ft " + c(1) + ". Cold, dry winters suit root cellars and long-term grain storage.",
 10: "The Central Valley is one of the best sun-drying places on earth — it produces much of the world's raisins " + c(8) + ". Mountain areas need altitude adjustments " + c(1) + ".",
 11: "Hot and dry; outdoor fruit drying works well " + c(8) + ". Heat in storage shortens shelf life — USU: shelf life halves for every 10.8 °F rise " + c(17) + ". Much of the plateau is high: adjust canning for altitude " + c(1) + ".",
 12: "Highland cities (Mexico City is far above 6,000 ft) need the highest altitude column in every canning table " + c(1, 2, 3) + "; lowlands are hot and humid. Dried and salted foods are traditional; keep them in sealed jars against moisture " + c(9) + ".",
 13: "Hot and humid: dried foods reabsorb moisture fast, so pack into small sealed jars you can use all at once " + c(9) + ". Store canned goods in the coolest spot (under 95 °F) " + c(1) + ". Salt-and-heat rules for smoked fish apply in any climate " + c(12) + ".",
}

def body():
    b = []
    b.append(part("p1", "Part 1", "Why Food Spoils — and Botulism"))
    b.append('<p>Preserving food means stopping the bacteria, yeasts and molds that rot it. Every method in this guide does that by taking away something they need: <b>heat</b> (canning), <b>water</b> (drying, salting), <b>warmth</b> (cold storage), or by adding <b>acid</b> (fermenting, pickling). Follow tested directions exactly — the times here are from the USDA <i>Complete Guide to Home Canning</i> and university Extension publications.</p>')
    b.append(h2("bot", "1.1 Botulism: the deadly one"))
    b.append('<p>The bacterium <i>Clostridium botulinum</i> can make a deadly toxin inside canned food. Its spores are on most fresh food and are harmless in air. They grow and make toxin in 3 to 4 days when they have all of these ' + c(1) + ':</p>')
    b.append(ul(["a moist, <b>low-acid</b> food;", "a temperature between <b>40 °F and 120 °F</b>;", "less than 2 percent oxygen — exactly the inside of a sealed jar."]))
    b.append(danger("You cannot see, smell or taste botulinum toxin", "Even a small taste of food containing the toxin can be deadly. Never taste food to check whether it is safe. <b>If in doubt, throw it out</b> " + c(6) + ". Home-canned vegetables are the most common cause of botulism outbreaks in the United States " + c(6) + "."))
    b.append(h2("acid", "1.2 Acid foods and low-acid foods"))
    b.append('<p>Botulinum spores are very hard to kill at boiling temperature. Low-acid foods must be heated to <b>240–250 °F</b>, which only a pressure canner at 10–15 pounds can reach ' + c(1) + '. Boiling low-acid food long enough to make it safe would take 7 to 11 hours ' + c(1) + '.</p>')
    b.append(fig(d_acid(), "Acid foods (pH 4.6 or lower) may go in a boiling-water canner; everything else needs a pressure canner " + c(1, 6) + "."))
    b.append(caution("Tomatoes need added acid", "Some tomatoes are slightly above pH 4.6. USDA: add <b>2 tablespoons bottled lemon juice or ½ teaspoon citric acid per quart</b> (1 tablespoon or ¼ teaspoon per pint) " + c(3) + ". Four tablespoons of 5% vinegar per quart also works but changes the flavor " + c(3) + "."))
    b.append(h2("spoil", "1.3 Spotting spoiled jars and getting rid of them"))
    b.append('<p>Check every jar before opening ' + c(1, 6) + ':</p>')
    b.append(check("Throw it out if…", ["the lid is loose, bulging or not curved down (not sealed)", "the jar leaks, or has streaks of dried food down the outside", "liquid or foam spurts out when you open it", "you see rising bubbles, cloudiness or unnatural color", "it smells wrong, or has mold (white, blue, black or green) on the food or lid"]))
    b.append('<p>Spoiled low-acid food (including tomatoes) may show little or no sign. Treat any suspect jar as containing botulinum toxin ' + c(1) + ':</p>')
    b.append(steps(["<b>Still sealed:</b> put the jar in a heavy garbage bag, close it, and put it in the trash or bury it in a landfill pit " + c(1) + ".", "<b>Unsealed, open or leaking:</b> wearing rubber or heavy plastic gloves, lay the jars and lids on their sides in a big pot, cover with at least 1 inch of water, put a lid on, bring to a boil and <b>boil 30 minutes</b>. Cool, then throw out jars, lids and food " + c(1) + ".", "<b>Clean up:</b> spray or wet anything the food touched with <b>1 part household bleach (5–6%) to 5 parts water</b>; leave 30 minutes; wipe up with paper towels and bag them; apply the bleach solution again for 30 minutes, then rinse and wash everything " + c(1) + "."]))
    b.append(danger("Boil home-canned food before eating", "CDC: boil home-canned tomatoes, foods containing them, <b>all low-acid home-canned foods</b> and all home-fermented Alaska Native foods before eating — <b>10 minutes</b> below 1,000 ft, plus 1 minute for each extra 1,000 ft " + c(6) + ". Heat destroys the toxin; it does not make a bulging or foul jar safe."))

    b.append(part("p2", "Part 2", "Canning"))
    b.append(h2("jars", "2.1 Jars, lids and headspace"))
    b.append(ul(["Use Mason-type threaded home-canning jars with two-piece self-sealing lids. Jars can be reused many times; USDA calls for <b>new flat lids each time</b> " + c(1) + ". Unused lids work well for at least 5 years from manufacture " + c(1) + " — <b>stockpile flat lids</b>; they are the part you cannot make.", "Not recommended: wire-bail jars with glass caps, zinc caps, and jars whose mouths do not take two-piece canning lids " + c(1) + ".", "Not recommended methods: open-kettle canning, ovens, microwaves, dishwashers, canning powders " + c(1) + ", and electric multi-cookers, even with a “canning” button " + c(6) + "."]))
    b.append(fig(d_head(), "Headspace lets food expand and a vacuum form " + c(1) + "."))
    b.append(h2("bw", "2.2 Boiling-water canning step by step"))
    b.append(fig(d_bw(), "The canner must be deep enough for at least 1 inch of briskly boiling water over the jars " + c(1) + "."))
    b.append(steps(["Fill the canner halfway with clean water. Preheat to <b>140 °F</b> for raw-packed food or <b>180 °F</b> for hot-packed food " + c(1) + ".", "Fill jars, leave the right headspace, wipe rims with a clean damp cloth, put on lids and bands.", "Lower jars upright on the rack. Add boiling water until it is <b>at least 1 inch over the jars</b> (2 inches if processing more than 30 minutes) " + c(1) + ".", "Cover, heat on high until the water boils vigorously, then start the timer " + c(1) + ".", "Keep it boiling the whole time. <b>If the boil stops, bring it back and start the timing over</b> " + c(1) + ". Add boiling water to keep the level up.", "When time is up, turn off the heat, take off the lid, wait <b>5 minutes</b>, then lift jars out " + c(1) + ".", "Set jars on a towel 1 inch apart and leave them undisturbed <b>12 to 24 hours</b> " + c(1) + "."]))
    b.append(tip("Sterilizing jars", "Jams, jellies and pickles processed less than 10 minutes go into sterile jars: boil empty jars upright, covered by 1 inch of water, for <b>10 minutes</b> below 1,000 ft, plus 1 minute per extra 1,000 ft " + c(1) + "."))
    b.append(h2("pc", "2.3 Pressure canning step by step"))
    b.append(fig(d_pc(), "All pressure canners must be vented for 10 minutes before pressurizing — trapped air lowers the temperature " + c(1) + "."))
    b.append(steps(["Put <b>2–3 inches of hot water</b> in the canner (more if a recipe says). Load filled jars on the rack. Fasten the lid " + c(1) + ".", "Leave the weight off the vent (or open the petcock). Heat on high until steam flows freely " + c(1) + ".", "Let steam flow for <b>10 minutes</b>, then put the weight on or close the petcock. Pressure builds in 3–5 minutes " + c(1) + ".", "Start timing when the dial reaches the right pressure, or when the weighted gauge jiggles or rocks as the maker describes " + c(1) + ".", "Adjust heat to hold steady pressure at or a little above the target. <b>If pressure drops below the target, bring it back up and start the full time over</b> " + c(1) + ".", "Turn off the heat and let the canner cool down by itself to zero. <b>Never force-cool</b> with water " + c(1) + ".", "When depressurized, remove the weight, wait 10 minutes, then open the lid tilted away from your face " + c(1) + ". Cool jars 12–24 hours on a towel " + c(1) + "."]))
    b.append(caution("Keep the canner accurate", "Check dial gauges every year. A gauge reading up to 2 pounds off can be corrected for; replace gauges off by more than 2 pounds " + c(1) + ". A weighted gauge needs no accuracy check " + c(1) + ". Keep gaskets clean and un-nicked, and never scratch or pick at the safety fuse " + c(1) + ". With no testing station, keep a spare weighted gauge and gasket for your model. CDC: use a canner that holds at least four 1-quart jars upright " + c(6) + "."))
    b.append(h2("alt", "2.4 Altitude adjustments"))
    b.append('<p>Water boils at lower temperatures as you go up, so sea-level times can leave food unsafe from 1,000 feet up. Use more time (boiling-water) or more pressure (pressure canner) for your altitude ' + c(1) + '. With no way to look it up, use a topographic map or road signs, and round up.</p>')
    b.append(fig(d_alt(), "Pressures used in USDA tables for vegetables, meat, poultry and fish " + c(4, 5) + "."))
    b.append(h2("times", "2.5 USDA process times"))
    b.append('<p><b>Pressure canner</b> — times are the same at every altitude; only the pressure changes (2.4). Pints / quarts ' + c(4, 5) + ':</p>')
    b.append(table(["Food", "Pack", "Pints", "Quarts", "Src"], PC))
    b.append('<p class="small">Meat: precook for hot pack; soak strong wild meat 1 hour in brine (1 tablespoon salt per quart) and rinse ' + c(5) + '. With venison for ground meat, add 1 part pork fat to 3–4 parts venison ' + c(5) + '. Fish must be bled and gutted within 2 hours of catching and kept on ice ' + c(5) + '. Do not pack fish with liquid ' + c(5) + '.</p>')
    b.append('<p><b>Boiling-water canner</b> — minutes by altitude ' + c(2, 3, 10) + ':</p>')
    b.append(table(["Food", "Pack", "0–1,000 ft", "1,001–3,000", "3,001–6,000", "Above 6,000", "Src"], BW))
    b.append('<p class="small">Crushed tomatoes may also be pressure canned: 15 minutes at 11 lb (dial, 0–2,000 ft) or 10 lb (weighted, 0–1,000 ft) ' + c(3) + '. For foods not listed, use only a USDA-tested recipe; never invent your own times ' + c(6) + '.</p>')
    b.append(h2("seal", "2.6 Testing seals and storing jars"))
    b.append(ul(["After 12–24 hours, take off the bands and test each lid: press the center (it must not spring up), tap with a spoon (a ringing sound means sealed; a dull sound means not), or look across it (it should curve down) " + c(1) + ".", "Unsealed jar: reprocess within 24 hours with a new lid, the same time; or refrigerate and eat within several days " + c(1) + ".", "Wash, label and date jars; store without bands in a clean, cool, dark, dry place — best at <b>50–70 °F</b>, <b>never above 95 °F</b>, not near stoves, pipes, attics or sunlight " + c(1, 6) + ".", "Can only what you will use in about 1 year " + c(6) + ".", "Freezing does not spoil jars unless they unseal; if they might freeze, wrap them in newspaper and blankets in heavy boxes " + c(1) + "."]))

    b.append(part("p3", "Part 3", "Drying"))
    b.append(h2("sun", "3.1 Sun drying fruit"))
    b.append('<p>Fruit is high in sugar and acid, so it can be dried outdoors when the weather is right. <b>Vegetables (except vine-dried beans) and meat should not be dried outdoors</b> — dry them indoors near a stove or in an oven where heat can be controlled ' + c(8) + '.</p>')
    b.append(fig(d_sun(), "Outdoor drying conditions and screens from NCHFP " + c(8) + "."))
    b.append(ul(["Needs hot, dry, breezy days: at least <b>85 °F</b>, humidity <b>below 60%</b>; it takes several days " + c(8) + ".", "Cover or bring fruit inside at night — cool night air adds moisture back " + c(8) + "."]))
    b.append(h2("jerky", "3.2 Jerky"))
    b.append(fig(d_jerky(), "NCHFP jerky method with a heating step to 160 °F " + c(7) + "."))
    b.append(ul(["<b>Pork and wild game can carry the trichinella parasite.</b> Before slicing, freeze pieces 6 inches thick or less at 0 °F or below for at least 30 days " + c(7) + ". (Freezing does not kill bacteria, and freezer power may be gone — then use the heating step and cook thoroughly.)", "If gut contents touched the meat when the animal was shot or dressed, do not make jerky from it; cook it thoroughly instead " + c(7) + ".", "Slice no thicker than ¼ inch and trim all fat — fat goes rancid " + c(7) + ".", "Heat to <b>160 °F</b>: boil strips in the marinade 5 minutes before drying, or heat the dried strips in an oven afterward " + c(7) + ".", "Dry at <b>140 °F</b> until a test piece cracks but does not break when bent — 10 to 24 hours if not pre-heated " + c(7) + "."]))
    b.append(h2("drystore", "3.3 Conditioning and storing dried food"))
    b.append(ul(["Cool completely first; warm food sweats and molds " + c(9) + ".", "<b>Condition fruit</b> (about 20% moisture): pack loosely in closed jars for 7–10 days, shaking daily; if moisture appears, dry it more " + c(9) + ".", "Vegetables should be brittle (about 10% moisture) and need no conditioning " + c(9) + ".", "Pack tightly in clean, dry, insect-proof containers, in amounts you will use at once " + c(9) + ".", "Most dried fruit keeps about <b>1 year at 60 °F, 6 months at 80 °F</b>; vegetables about half as long " + c(9) + ". Check often; re-dry damp food; throw out moldy food " + c(9) + "."]))

    b.append(part("p4", "Part 4", "Salting, Curing & Smoking"))
    b.append('<p>Salt pulls water out of meat and fish so microbes cannot grow; smoke adds flavor and some protection. Temperature control is the key to doing it safely.</p>')
    b.append(h2("ham", "4.1 Dry-curing a ham (Virginia Extension method)"))
    b.append(steps(["Chill the carcass below <b>40 °F</b> before cutting, and keep the ham below 40 °F until curing " + c(13) + ".", "Mix the cure for every 100 lb of fresh meat: <b>8 lb salt, 2 lb sugar, 2 oz saltpeter or sodium nitrite</b>. Salt alone is acceptable " + c(13) + ". Divide into two equal parts.", "Day 1: rub the first half into all lean surfaces; cover skin and fat; pack the exposed shank end and the area around the aitchbone (hip bone) well to prevent bone sour " + c(13) + ".", "Day 7: apply the second half " + c(13) + ".", "Keep hams on draining shelves at <b>36–40 °F</b> (check with a thermometer); avoid pine and other fragrant woods " + c(13) + ".", "Cure <b>1½ days per pound</b> of ham (or 7 days per inch of cushion depth) " + c(13) + ".", "Wash off the cure, then hold at 50–60 °F for about 14 days to equalize. Expect 8–10% shrink " + c(13) + "."]))
    b.append(caution("Cure only in cold weather", "Virginia Extension: early December is the best time to start curing under ambient conditions " + c(13) + ". Without refrigeration, you need steady 36–40 °F weather — warm spells spoil hams."))
    b.append(h2("fish", "4.2 Brining and smoking fish"))
    b.append(fig(d_fish(), "PNW 238: heat, salt and cold storage together keep home-smoked fish safe " + c(12) + "."))
    b.append(ul(["Brine: <b>1 cup non-iodized salt to 7 cups water</b> salts 2–3 lb of fish in about 1 hour; herring about 30 minutes; 2–3 inch salmon chunks about 2 hours. Start testing at 15 minutes per ½ inch of thickness. Do not let pieces overlap " + c(12) + ".", "Rinse and air-dry on a greased rack in a cool place until a shiny, tacky pellicle forms (at least 1 hour) " + c(12) + ".", "Smoke, then make sure the <b>thickest piece reaches at least 150 °F (preferably 160 °F) and stays there 30 minutes</b>. Small smokers may not get hot enough — finish in an oven " + c(12) + ".", "Keep smoked fish at <b>38 °F or less</b> " + c(12) + ". Without refrigeration, eat it soon, or pressure-can fish (2.5)."]))

    b.append(part("p5", "Part 5", "Fermenting"))
    b.append(h2("kraut", "5.1 Sauerkraut"))
    b.append(steps(["Use firm, fresh cabbage; start within 24–48 hours of harvest " + c(10) + ".", "Work 5 lb at a time: remove outer leaves and cores, shred about as thick as a quarter " + c(10) + ".", "Add <b>3 tablespoons canning or pickling salt per 5 lb</b>, mix with clean hands, pack firmly until juice is drawn out " + c(10) + ".", "If juice does not cover the cabbage, add boiled, cooled brine (<b>1½ tablespoons salt per quart</b> water) " + c(10) + ".", "Weight it down and cover with a towel (5.2). Ferment at <b>70–75 °F for 3–4 weeks</b>; at 60–65 °F it takes 5–6 weeks; below 60 °F it may not ferment; above 75 °F it may go soft " + c(10) + ".", "If you used jars as weights, check 2–3 times a week and remove any scum " + c(10) + ".", "Keep finished kraut covered and cold for months, or can it in a boiling-water canner (2.5) " + c(10) + "."]))
    b.append(h2("crock", "5.2 Crocks, covers and weights"))
    b.append(fig(d_crock(), "A 5-gallon crock holds about 25 lb of cabbage or cucumbers " + c(11) + "."))
    b.append(ul(["Use stone crocks or food-grade plastic or glass. Non-food-grade buckets only if lined with a food-grade bag — never garbage bags " + c(11) + ".", "Keep vegetables <b>1–2 inches under brine</b> with a plate weighted by water-filled jars, or a sealed food bag holding 3 quarts of water with 4½ tablespoons salt " + c(11) + ".", "Wash the crock, plate and jars in hot soapy water and rinse with very hot water first " + c(11) + "."]))

    b.append(part("p6", "Part 6", "Root Cellars & Cold Storage"))
    b.append('<p>Stored vegetables are alive and breathing; cold slows them down. Most keep best between <b>32 and 40 °F</b> with high humidity ' + c(15) + '. Choose late-maturing, good-keeping varieties and harvest as late as you can before a hard frost ' + c(15) + '.</p>')
    b.append(h2("groups", "6.1 The four storage groups"))
    b.append(fig(d_groups(), "Temperatures and relative humidity (RH) from WSU and MU Extension " + c(14, 16) + "."))
    b.append(ul(["<b>Keep fruit and vegetables apart.</b> Ripening apples and pears give off ethylene gas, which makes potatoes sprout early " + c(14) + ".", "Strong-smelling cabbage and turnips taint other food — store them away from the house or wrap them in newspaper " + c(14, 15) + ".", "Potatoes and onions need curing in a warm place first; onions and squash want dry, airy storage and mold in damp air " + c(15) + ".", "Pack root crops in moist sand, sawdust or peat, or in perforated plastic bags " + c(15) + ". Do not let anything freeze " + c(14) + "."]))
    b.append(h2("cellar", "6.2 Running a root cellar"))
    b.append(fig(d_cellar(), "Ventilation controls temperature and humidity; screen vents against rodents " + c(15) + "."))
    b.append(ul(["A dirt floor keeps humidity up; on concrete or wood, set out pans of water. A small, full cellar holds humidity better than a big, empty one " + c(15) + ".", "Warm air rises — the top is warmer. Put thermometers at several heights " + c(15) + ".", "Use the vents to let in cold outside air and let out damp, warm air; close them when it is warmer outside than inside, and in deep cold so nothing freezes.", "No cellar? An unheated back hall, enclosed porch, shed, or a walled-off room in the coldest (north/east) corner of a basement can work " + c(16) + "."]))

    b.append(part("p7", "Part 7", "Long-Term Grain & Dry Storage"))
    b.append(h2("grain", "7.1 Packing grain, rice and beans"))
    b.append(fig(d_bucket(), "Airtight food-grade containers with oxygen absorbers, kept cool and dark " + c(17, 18) + "."))
    b.append(ul(["<b>Temperature:</b> a steady <b>40–60 °F</b> is best; USU cites USDA that shelf life halves for every 10.8 °F rise " + c(17) + ".", "<b>Moisture:</b> food must be dry — about <b>10% moisture or less</b> " + c(17) + ".", "<b>Oxygen:</b> remove it with oxygen absorbers, dry ice (carbon dioxide) or nitrogen " + c(17) + ".", "<b>Containers:</b> #10 cans, sealable food buckets, lined drums, foil (Mylar-type) pouches, PETE bottles, or glass jars kept dark " + c(17, 18) + ". Rodents chew through plastic bags " + c(18) + ".", "<b>Insects:</b> freeze infested food at 0 °F for 3–4 days to kill insects, larvae and eggs " + c(17) + ". Wheat need not be oxygen-free unless insects are present " + c(18) + "."]))
    b.append(danger("Never seal moist food without oxygen", "Botulism poisoning may result if moist products are stored in packaging that removes oxygen. Only dry foods (about 10% moisture or less) go in with oxygen absorbers " + c(17, 19) + "."))
    b.append(h2("life", "7.2 How long it lasts"))
    b.append('<p>“Life-sustaining” shelf-life estimates for properly packaged dry foods stored cool, from BYU research ' + c(19) + ':</p>')
    b.append(table(["Food", "Years"], [["Wheat, white rice, corn, sugar", "30+"], ["Pinto beans, rolled oats, pasta, potato flakes, apple slices", "30"], ["Non-fat powdered milk, dehydrated carrots", "20"]]))
    b.append('<p>USU: rice in oxygen-free containers keeps up to 10 years at a constant 70 °F and up to 30 years in cooler storage ' + c(18) + '. A #10 can holds about 5.7 lb of rice ' + c(18) + '. Store wheat whole and grind it as needed — whole grain keeps far longer than flour ' + c(17) + '.</p>')

    b.append(part("p8", "Part 8", "Region by Region"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Value"], [["Low-acid foods", "Pressure canner only, 240–250 °F " + c(1)], ["Acid line", "pH 4.6 " + c(1)], ["Tomato acid", "2 Tbsp lemon juice or ½ tsp citric acid per quart " + c(3)], ["Vent pressure canner", "10 minutes " + c(1)], ["Dial pressure 0–2,000 ft", "11 lb (+1 lb per 2,000 ft) " + c(4, 5)], ["Weighted gauge", "10 lb ≤1,000 ft; 15 lb above " + c(4, 5)], ["Boil home-canned food", "10 min + 1 min per 1,000 ft " + c(6)], ["Store jars", "50–70 °F, never above 95 °F " + c(1)], ["Jerky", "160 °F, then dry at 140 °F " + c(7)], ["Smoked fish", "160 °F for 30 min; store ≤38 °F " + c(12)], ["Ham cure", "8 lb salt / 2 lb sugar / 2 oz nitrite per 100 lb; 36–40 °F " + c(13)], ["Sauerkraut", "3 Tbsp salt per 5 lb; 70–75 °F, 3–4 weeks " + c(10)], ["Root cellar", "32–40 °F, 80–95% RH for most crops " + c(14, 15)], ["Dry storage", "≤10% moisture, 40–60 °F, oxygen absorbers " + c(17)]]))
    b.append('<p class="small">General information for emergencies; follow tested recipes exactly. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Food Preservation & Storage", "Survival Info<br>Food<br>Preservation",
          "Water-bath and pressure canning with USDA times, botulism safety, drying and jerky, salting, curing and smoking, fermenting, root cellars and long-term grain storage — for every region of North America.",
          "Food Preservation", TOC, cover_art(), "Food · Hunting · Water · Fire · Medical · Sanitation · House · Bunkers")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Preservation.pdf")
