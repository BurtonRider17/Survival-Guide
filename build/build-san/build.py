import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#12313d"/>'
    s += '<rect x="90" y="120" width="150" height="200" fill="#8d6e63"/><polygon points="80,120 165,70 250,120" fill="#6d4c41"/><rect x="140" y="180" width="50" height="140" fill="#4e342e"/>'
    s += '<path d="M330 120 h120 v40 h-20 v100 h-80 v-100 h-20z" fill="#5fb3e6"/><circle cx="390" cy="300" r="8" fill="#5fb3e6"/><circle cx="410" cy="330" r="6" fill="#5fb3e6"/>'
    s += '<rect x="520" y="200" width="120" height="70" rx="10" fill="#f4f1ea"/><rect x="540" y="180" width="80" height="24" rx="6" fill="#e6b54a"/><circle cx="560" cy="290" r="14" fill="#f4f1ea" opacity="0.6"/><circle cx="600" cy="300" r="10" fill="#f4f1ea" opacity="0.5"/>'
    s += '<circle cx="640" cy="80" r="36" fill="#e69b00"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Why Sanitation Saves Lives", [("why","1.1 How disease spreads: the F-diagram"),("hands","1.2 Hand-washing")]),
 ("p2", "Part 2 · Toilets", [("first","2.1 The first days: bucket toilets and trench latrines"),("site","2.2 Where to put a latrine"),("pit","2.3 Pit latrines and VIP latrines"),("compost","2.4 Composting toilets"),("septic","2.5 Using a house toilet and septic system without power")]),
 ("p3", "Part 3 · Water, Waste & Pests", [("grey","3.1 Greywater"),("trash","3.2 Garbage and food waste"),("pests","3.3 Flies, mosquitoes and rodents")]),
 ("p4", "Part 4 · Soap & Personal Hygiene", [("soap","4.1 Making soap"),("ashlye","4.2 Lye from wood ashes"),("body","4.3 Bathing, laundry, teeth, menstruation")]),
 ("p5", "Part 5 · Care of the Dead", [("dead","5.1 Handling and burying the dead")]),
 ("p6", "Part 6 · Region-by-Region Guide", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_fdiagram():
    s = t(360, 30, "How germs in feces reach a new mouth — and where to block them", 17, "middle", "700")
    s += label_box(20, 160, 130, 70, ["FECES"], "#d7ccc8", 18)
    paths = ["Fingers", "Flies", "Fields", "Fluids (water)", "Food"]
    for i, p in enumerate(paths):
        y = 60 + i*62
        s += label_box(250, y, 170, 46, [p], "#eef4f7", 16)
        s += arrow(150, 195, 248, y+23)
        s += arrow(420, y+23, 560, 195)
    s += label_box(560, 160, 140, 70, ["NEW", "PERSON"], "#ffe0b2", 17)
    s += rect(190, 50, 30, 320, "#c8e6c9", "#2e7d32", 2, 4) + t(205, 395, "toilets", 13, "middle", "600", "#2e7d32")
    s += rect(470, 50, 30, 320, "#bbdefb", "#2f7fbf", 2, 4) + t(485, 395, "hand-washing, safe water, covered food", 13, "middle", "600", "#2f7fbf")
    return svg(720, 410, s)

def d_site():
    s = t(360, 28, "Latrine siting (Sphere minimum standards)", 18, "middle", "700")
    s += line(20, 230, 700, 230, "#6d4c41", 3)
    s += '<path d="M20 330 Q360 310 700 330 L700 400 L20 400 Z" fill="#bbdefb"/>' + t(520, 380, "groundwater table", 14, "middle", "600", "#1d5d8f")
    s += rect(80, 150, 60, 80, "#a1887f") + '<polygon points="70,150 110,120 150,150" fill="#6d4c41"/>' + rect(90, 230, 40, 70, "#5d4037", "#3e2723", 2, 0)
    s += t(110, 110, "latrine", 15, "middle", "600")
    s += line(110, 300, 110, 330, "#c0392b", 2) + t(120, 320, "pit bottom ≥ 1.5 m (5 ft) above water table", 14, "start", "600", "#c0392b")
    s += rect(560, 170, 40, 60, "#90a4ae") + rect(570, 230, 20, 110, "#cfd8dc") + t(580, 160, "well / spring", 15, "middle", "600")
    s += arrow(150, 80, 550, 80, "#2e7d32") + arrow(550, 80, 150, 80, "#2e7d32") + t(350, 70, "at least 30 m (100 ft) — more in limestone or cracked rock", 15, "middle", "600", "#2e7d32")
    s += t(350, 270, "downhill from the well, never uphill or upwind of homes", 14, "middle")
    return svg(720, 410, s)

def d_vip():
    s = t(360, 28, "Ventilated improved pit (VIP) latrine — cross-section", 18, "middle", "700")
    s += '<rect x="0" y="230" width="720" height="140" fill="#d7ccc8"/>'
    s += rect(200, 230, 260, 130, "#8d6e63", "#3e2723", 2, 0) + t(330, 330, "pit", 18, "middle", "700", "#fff")
    s += rect(170, 210, 320, 22, "#9e9e9e", "#424242", 2, 2) + t(330, 226, "slab with squat hole + lid", 13, "middle", "600", "#fff")
    s += rect(220, 90, 200, 120, "none", "#424242", 3, 0) + t(320, 120, "dark shelter", 14, "middle", "600")
    s += rect(430, 50, 28, 162, "#455a64", "#263238", 2, 0) + t(470, 60, "vent pipe, black, above roof", 14, "start", "600")
    s += rect(424, 38, 40, 12, "#fff", "#c0392b", 2, 1) + t(470, 84, "fly screen on top: flies go to the light", 14, "start", "600", "#c0392b")
    s += t(470, 108, "and die trapped at the screen", 14, "start", "600", "#c0392b")
    s += arrow(444, 200, 444, 56, "#2f7fbf") + t(520, 170, "wind draws odor up the pipe", 14, "start")
    s += t(360, 396, "When the pit is nearly full: fill with soil, plant a tree, dig a new pit", 15, "middle", "600")
    return svg(720, 410, s)

def d_bucket():
    s = t(360, 28, "Two-bucket toilet and compost bins", 18, "middle", "700")
    s += rect(40, 110, 120, 150, "#e3f2fd", "#1d5d8f", 2, 8) + t(100, 95, "toilet bucket", 15, "middle", "600") + t(100, 190, "cover each use", 13, "middle") + t(100, 210, "with sawdust", 13, "middle")
    s += rect(200, 140, 90, 120, "#d7b98e", "#8a6d3b", 2, 8) + t(245, 125, "cover", 15, "middle", "600") + t(245, 200, "sawdust,", 13, "middle") + t(245, 218, "leaves, ash", 13, "middle")
    s += arrow(300, 200, 370, 200)
    s += rect(380, 120, 140, 160, "#a1887f", "#4e342e", 2, 4) + t(450, 105, "bin 1: filling", 15, "middle", "600") + t(450, 200, "add straw &", 13, "middle", "600", "#fff") + t(450, 218, "food scraps", 13, "middle", "600", "#fff")
    s += rect(550, 120, 140, 160, "#6d4c41", "#3e2723", 2, 4) + t(620, 105, "bin 2: resting", 15, "middle", "600") + t(620, 200, "leave untouched", 13, "middle", "600", "#fff") + t(620, 218, "1–2 years", 13, "middle", "600", "#fff")
    s += rect(40, 310, 650, 70, "#fff6e0") + t(365, 338, "Finished compost goes to trees and non-food plants first.", 15, "middle", "600") + t(365, 362, "Never put fresh waste on vegetables.", 15, "middle")
    return svg(720, 400, s)

def d_tippy():
    s = t(360, 28, "Tippy-tap: a hands-free hand-washing station", 18, "middle", "700")
    s += line(150, 360, 150, 80, "#6d4c41", 8) + line(570, 360, 570, 80, "#6d4c41", 8) + line(140, 80, 580, 80, "#6d4c41", 8)
    s += '<path d="M300 120 h70 v20 h20 v100 h-110 v-100 h20z" fill="#bbdefb" stroke="#1d5d8f" stroke-width="2" transform="rotate(-12 335 180)"/>'
    s += line(330, 82, 330, 125, INK, 2) + t(420, 150, "jug with small hole near cap", 14, "start", "600")
    s += line(300, 230, 300, 340, INK, 2) + rect(260, 340, 100, 14, "#8d6e63", "#3e2723", 2, 2) + t(370, 352, "foot pedal stick pulls string, tips jug", 14, "start", "600")
    s += rect(470, 120, 50, 40, "#fff59d", "#f9a825", 2, 6) + t(495, 185, "soap on", 13, "middle") + t(495, 202, "a string", 13, "middle")
    s += t(360, 395, "Gravel under the station keeps mud and mosquitoes down.", 15, "middle", "600")
    return svg(720, 410, s)

R = {
 1: "<b>Frozen ground</b> makes digging pits impossible much of the year: use bucket toilets with plenty of cover material and store the buckets frozen until a thaw, then compost or bury. Permafrost and thin soils mean waste does not break down quickly — keep it well away from water. Keep hands and dishes clean with heated water; hand-washing is often skipped in the cold, which spreads illness.",
 2: "<b>Wet ground and high water tables</b> in river valleys: pits can flood and contaminate wells. Build raised or lined latrines in wet sites, as Sphere recommends for high water tables " + c(2) + ". Plenty of rain for hand-washing barrels; lots of sawdust and leaves for cover material.",
 3: "Deep soils dig easily; farm wells are common — keep latrines at least 30 m (100 ft) away and downhill " + c(2) + ". Wind carries odor and dust: site latrines downwind. Winter freezing slows composting; summer heat speeds it.",
 4: "Many shallow wells and high water tables near lakes and rivers; spring floods. Watch for frozen ground in winter (use buckets). Hardwood ash is plentiful for lye soap (4.2).",
 5: "Dense cities lose sewer service without power at pumping stations; plan bucket toilets for apartments and townhouses. Rocky soils and ledge make pits hard — use bucket and compost systems. Hardwood ash for soap.",
 6: "<b>Heat, humidity, flooding</b>: flies breed fast, pits flood in hurricanes, cholera-type outbreaks are possible after floods. Use lids and VIP vent pipes " + c(3) + ", raise latrines in flood zones, and push hand-washing. Bury the dead well away from water (5.1).",
 7: "Very high water table and sandy soil almost everywhere: pit latrines can contaminate groundwater quickly. Prefer bucket/compost toilets and raised containment " + c(2) + ". Mosquito control (3.3) is critical.",
 8: "Dry soils are good for latrines, but water for hand-washing is scarce — use a tippy-tap (1.2) or ash rubs " + c(3) + ". Composting needs added moisture. Greywater is valuable for trees (3.1).",
 9: "Rocky, thin soils in mountains; fractured rock lets waste travel far — increase distance from springs " + c(2) + ". Cold winters freeze pits and slow compost. Snowmelt can carry waste into streams.",
 10: "Drought: save every drop of greywater for trees. Earthquakes can break sewer and septic lines — plan bucket toilets. Wildfire ash is a hand-washing scrub in a pinch.",
 11: "Desert north: dry soils, scarce water — dry toilets and ash for hand-washing. Keep latrines away from any well or cistern.",
 12: "Central highlands: dense towns with old sewers; mountain springs at risk from uphill latrines. Lowlands: heat, mosquitoes, and diarrheal disease risk — push safe water and hand-washing.",
 13: "Hurricanes, floods and high water tables: raised or lined latrines, lids, and strong mosquito control. Cholera has occurred in the region; the WHO notes it spreads through water and food contaminated with feces " + c(9) + ".",
}

def body():
    b = []
    b.append('<div class="pb"></div>' + h2("howto", "How to use this guide"))
    b.append('<p>When water stops running and sewers stop working, <b>human waste becomes one of the biggest killers</b> in a disaster. The World Health Organization notes that poor sanitation is linked to diarrheal diseases such as cholera and dysentery, as well as typhoid, intestinal worms and polio ' + c(8) + '. This beginner guide shows how to keep waste, dirty water, garbage and pests away from people, how to make soap, and how to care for the dead — all with your own hands and local materials.</p>')
    b.append('<p>Small numbers in brackets ' + c(1) + ' point to the numbered sources at the end; every source was saved as a PDF in <b>Survival Info Sources/Sanitation/</b>. Distances and numbers here mostly come from the <b>Sphere Handbook</b>, the minimum standards used by aid workers in disasters around the world ' + c(1, 2) + '.</p>')
    b.append(table(["Priority", "Goal"], [["Day 1", "A bucket toilet or trench latrine; a hand-washing station with soap or ash"], ["Week 1", "Proper latrine site 30 m (100 ft) from water; garbage pit; fly control"], ["Month 1", "Pit or VIP latrine, or a two-bin composting system; greywater area"], ["Long term", "Make soap from fat and lye; rotate latrine pits; maintain compost"]]))
    b.append(part("p1", "Part 1", "Why Sanitation Saves Lives"))
    b.append(h2("why", "1.1 How disease spreads: the F-diagram"))
    b.append('<p>Germs in feces reach a new person by five routes: <b>fingers, flies, fields (soil), fluids (water) and food</b>. Toilets stop germs at the source; hand-washing, safe water and covered food stop them before they reach a mouth ' + c(10) + '.</p>')
    b.append(fig(d_fdiagram(), "<b>Figure 1.</b> The F-diagram. The green barrier (toilets) blocks all five routes at once."))
    b.append('<p>Sphere notes that children\'s feces are often more dangerous than adults\', because children carry more excreta-related infections — so dispose of children\'s and babies\' waste in the toilet too ' + c(2) + '.</p>')
    b.append(h2("hands", "1.2 Hand-washing"))
    b.append('<p>Sphere says the importance of washing hands after using the toilet and before eating and preparing food "cannot be over-estimated," and that soap <b>or an alternative such as ash</b> should be used, with water kept near the toilet ' + c(3) + '. Wash all surfaces of both hands, including between fingers and under nails, and rinse in running water (pour from a jug, or use the tippy-tap below). CDC recommends scrubbing for at least 20 seconds ' + c(19) + '.</p>')
    b.append(fig(d_tippy(), "<b>Figure 2.</b> A tippy-tap uses very little water and nobody touches the jug with dirty hands."))
    b.append(check("Hand-washing moments", ["After using the toilet or cleaning a child", "Before preparing food, eating or feeding a child", "After handling garbage, animals, raw meat or the dead", "Before and after caring for a sick or injured person"]))
    b.append(part("p2", "Part 2", "Toilets"))
    b.append(h2("first", "2.1 The first days: bucket toilets and trench latrines"))
    b.append('<p>Sphere says the first priority after a disaster is to stop open defecation and set up defecation areas and toilets right away ' + c(2) + '.</p>')
    b.append('<h3>Bucket toilet (indoors or out)</h3>')
    b.append(steps(["Use a 5-gallon (20 L) bucket with a tight lid; a toilet seat fits on top or line the house toilet bowl with a strong bag.", "After each use, cover waste completely with a scoop of dry cover material: sawdust, wood shavings, dry leaves, peat, shredded paper or wood ash. This stops smell and flies.", "Keep urine separate if you can (a second container) — the bucket fills more slowly and smells less.", "Empty the bucket into a covered pit, trench or compost bin (2.4) before it is too heavy to carry. Wash it with soap and water and keep the wash water out of drinking water."]))
    b.append('<h3>Shallow trench latrine</h3>')
    b.append('<p>Dig a trench about 1 ft (30 cm) wide and 2–3 ft (60–90 cm) deep, with the soil piled beside it. Each user squats over the trench and covers their waste with a shovel of soil. When the trench is filled to within 1 ft (30 cm) of the top, fill it with soil, mound it, and dig a new one. Site it as in 2.2.</p>')
    b.append(h2("site", "2.2 Where to put a latrine"))
    b.append(fig(d_site(), "<b>Figure 3.</b> Sphere minimum distances for pits, trenches and soakaways when soil cannot be tested " + c(2) + "."))
    b.append(ul(["At least <b>30 m (100 ft)</b> from any well, spring or other groundwater source, and the bottom of the pit at least <b>1.5 m (5 ft) above the water table</b> " + c(2, 3) + ".",
                 "Increase the distance in cracked rock or limestone; it can be less in fine soils " + c(2) + ".",
                 "Never uphill or upwind of homes, and not near food storage or cooking areas " + c(2) + ".",
                 "In flood areas or high water tables, make the pit watertight or build a raised toilet " + c(2) + ".",
                 "Close enough to use at night: Sphere aims for no more than 50 m from each dwelling, and at least one toilet per 20 people " + c(4) + ". Light the path, and make it safe for women and children " + c(3) + "."]))
    b.append(h2("pit", "2.3 Pit latrines and VIP latrines"))
    b.append('<p>A <b>pit latrine</b> is a covered hole with a slab and a shelter. A <b>ventilated improved pit (VIP)</b> latrine adds a vent pipe with a fly screen; together with a lid on the squat hole, it keeps flies and odor down ' + c(3) + '. Hesperian\'s Community Guide to Environmental Health shows how to build several kinds ' + c(10) + '.</p>')
    b.append(fig(d_vip(), "<b>Figure 4.</b> VIP latrine. Keep the shelter dark inside so flies leaving the pit head for the light at the screened vent pipe."))
    b.append(steps(["Pick the site (2.2). Dig a pit about 3 ft (1 m) across and as deep as is safe and stays above the water table.", "In loose soil, line the top of the pit with stones, logs or bricks so the edge does not collapse.", "Make a strong slab (wood planks, or a reinforced concrete slab — see the Concrete guide) with a squat hole and a tight lid.", "Build a shelter for privacy and rain. For a VIP, add a wide vent pipe rising above the roof with a fly screen on top.", "Keep the slab clean. When the pit is nearly full, fill it with soil, and move the shelter to a new pit."]))
    b.append(caution("Pit safety", "Deep pits can cave in on the digger. Shore loose soil, never dig alone, and keep children away from open pits. Gases in old pits can suffocate — never climb into a used pit."))
    b.append(h2("compost", "2.4 Composting toilets"))
    b.append('<p>A composting system turns bucket-toilet waste into soil, which is useful where you cannot dig pits (frozen ground, rock, high water tables) or want the fertility back. Hesperian describes ecological sanitation toilets that separate or compost waste ' + c(10) + '.</p>')
    b.append(fig(d_bucket(), "<b>Figure 5.</b> Two-bin system: fill one bin, then let it rest untouched while the second bin fills."))
    b.append(steps(["Build two bins from pallets or boards, each about 4 × 4 ft (1.2 × 1.2 m), with a lid or roof, on soil away from water (2.2 distances).", "Empty toilet buckets into the center of bin 1 and cover with straw, leaves or sawdust. Food scraps can go in too.", "When bin 1 is full, cover it thickly and leave it untouched. Start filling bin 2.", "Let the full bin rest a long time. The WHO excreta-use guidelines call for long storage before use — about 1.5 to 2 years at ordinary temperatures for dry storage " + c(7) + ".", "Use finished compost on fruit trees, firewood trees and non-food plants first."]))
    b.append(danger("Human waste is not garden fertilizer — until it is fully treated", "Fresh or partly composted human waste carries worm eggs and germs. Do not put it on vegetables, and never on crops eaten raw " + c(7) + "."))
    b.append(h2("septic", "2.5 Using a house toilet and septic system without power"))
    b.append('<p>If your house has a <b>septic system that drains by gravity</b>, the toilet can still be flushed by pouring a bucket of water quickly into the bowl. Systems with a pump (mound systems, lift stations) stop working without power. In town, sewer lift stations also stop when power fails, and sewage can back up — switch to bucket toilets.</p>')
    b.append(ul(["Use greywater (dishwater, bath water) for flushing, not drinking water.", "EPA's rule of thumb: flush nothing but human waste and toilet paper — never cooking grease, wipes or feminine products " + c(17) + ". Keep sawdust and other cover material out of a septic system too.", "Protect the drainfield: don't drive or park on it " + c(17) + ".", "A full septic tank must be pumped out eventually; without a pump truck, plan to switch to pits or composting before that point."]))
    b.append(part("p3", "Part 3", "Water, Waste & Pests"))
    b.append(h2("grey", "3.1 Greywater"))
    b.append('<p>Greywater is used water from washing, bathing and laundry — not toilet waste. It carries far fewer germs than sewage but is not clean ' + c(7) + '.</p>')
    b.append(ul(["Use mild soap (your own homemade soap is fine) and avoid bleach and harsh chemicals in water going to plants.", "Pour it onto mulch basins around fruit trees, shrubs and firewood trees, under a layer of mulch so nobody touches it and it does not pool.", "Do not spray it, store it for more than a day (it turns foul), or put it on vegetables eaten raw " + c(7) + ".", "Keep it away from wells and springs and do not let it pool — standing water breeds mosquitoes."]))
    b.append(h2("trash", "3.2 Garbage and food waste"))
    b.append(table(["Waste", "What to do"], [["Food scraps", "Feed to chickens or pigs, or compost (2.4); never leave in the open"], ["Paper, cardboard", "Use as compost cover, fire-starter or insulation"], ["Plastic, metal, glass", "Wash and reuse; store clean; what can't be used goes in a covered pit"], ["Medical waste, sharps", "Put in a thick bottle, seal and bury deep away from water"], ["Batteries, oil, chemicals", "Store sealed in a dry place; don't burn or bury near water"]]))
    b.append('<p>Dig a garbage pit downwind and away from water and homes; cover each day\'s garbage with soil to keep flies and rats out.</p>')
    b.append(h2("pests", "3.3 Flies, mosquitoes and rodents"))
    b.append(ul(["<b>Flies</b> breed in feces and rotting food: lids on latrines, cover material on buckets, covered garbage, and screened food " + c(3) + ".", "<b>Mosquitoes</b> breed in still water: empty, cover or drain anything holding water (buckets, tires, gutters, barrels); screen rain barrels; sleep under nets.", "<b>Rats and mice</b> follow food and garbage: store food in metal or thick plastic containers; keep garbage covered; clear brush and junk piles near the house. See the Bunkers guide for safe cleanup of rodent droppings."]))
    b.append(part("p4", "Part 4", "Soap & Personal Hygiene"))
    b.append(h2("soap", "4.1 Making soap"))
    b.append('<p>Soap is made by reacting <b>fat</b> with <b>lye</b> (sodium hydroxide, NaOH, or potassium hydroxide, KOH, from wood ash). Any good animal fat and some vegetable fats work; mineral oil cannot be used ' + c(14) + '. Stock up on lye (sodium hydroxide) now while stores sell it.</p>')
    b.append(danger("Lye burns skin and blinds eyes", "Wear eye protection, gloves, long sleeves and shoes. <b>Always add lye to cold water, never water to lye</b> — it gets very hot. Work outdoors or with good ventilation, and keep children and animals away. Do not use aluminum or tin containers; lye attacks them " + c(16, 14) + "."))
    b.append('<h3>The 1970 Utah State extension no-boil recipe ' + c(14) + '</h3>')
    b.append(table(["Ingredient", "Amount"], [["Clean rendered fat", "5½ pounds"], ["Lye (one standard can, as sold then)", "1 can"], ["Cold water", "2½ pints"], ["Borax (laundry soap only, optional)", "2 tablespoons"]]))
    b.append('<p class="small">The bulletin used "one can lye" without giving its weight; check the weight on your container and use a soap (saponification) chart to match lye to your fat if you can. Using a little less lye than the full amount is safer — extra fat makes a milder soap, extra lye burns ' + c(16) + '.</p>')
    b.append(steps(["Clean the fat: heat it until just boiling and strain through several layers of cloth. Salty, rancid or dirty fat can be washed by boiling with about four times as much water, cooling, and lifting off the clean fat cake " + c(14) + ".",
        "Slowly add the lye to the cold water in an enamel, glass or heavy plastic pan, stirring until dissolved. Let it cool " + c(14) + ".",
        "Melt the fat and let it cool to the right temperature. The bulletin gives pairs: good lard 85 °F with lye water at 75 °F; equal lard and tallow 110 °F with lye water at 85 °F; straight tallow 130 °F with lye water at 95 °F " + c(14) + ".",
        "Pour the lye solution slowly into the fat, stirring with a wooden paddle until it thickens like honey and a drip leaves a trace on the surface " + c(14, 16) + ".",
        "Pour into a cloth-lined wooden box or mold, cover and insulate for a day, then cut into bars.",
        "Cure the bars in a dry, airy place for several weeks before use — 2 to 6 weeks for cold-process soap " + c(16) + "."]))
    b.append(h2("ashlye", "4.2 Lye from wood ashes"))
    b.append('<p>Before the 1800s, lye came from ashes. Ash lye is potassium hydroxide (KOH) and makes a <b>soft soap</b>, with less predictable results than store-bought lye ' + c(16) + '.</p>')
    b.append(steps(["Save white ashes from <b>hardwood</b> fires (not painted, treated or plywood scraps), kept dry.", "Boil water and soak the ashes in it; you can run several batches of ashes through the same water " + c(16) + ".", "Let the ash settle or drip it through a barrel with a straw-and-gravel filter at the bottom, and collect the brown liquid.", "Boil the liquid down until an egg or a potato will float in it — this is the traditional strength test " + c(16) + ".", "Use it with fat as in 4.1, cooking the mixture (hot process) until it turns to a soft, jelly-like soap."]))
    b.append(caution("Strength varies", "Ash lye strength changes every batch. Test a small batch first; soap that stings or feels slippery-burning has too much lye — cook it longer with more fat."))
    b.append(h2("body", "4.3 Bathing, laundry, teeth, menstruation"))
    b.append(ul(["<b>Bathing:</b> a sponge bath with a basin of warm water and soap uses very little water. Wash the face, hands, armpits, groin and feet daily if you can; this prevents skin infections and rashes.", "<b>Laundry:</b> wash in a tub with a plunger or washboard; rinse well; dry in sun. Boil cloth diapers, menstrual cloths and bandages.", "<b>Teeth:</b> brush daily; a chewed twig works. See the Medical guide, section 4.2.", "<b>Menstruation:</b> Sphere notes women and girls need suitable materials and privacy for washing and drying cloths " + c(3) + ". Washable cloth pads, boiled and sun-dried, last for years.", "<b>Lice and scabies</b> spread in crowded shelters: wash bedding in hot water and dry it in the sun; comb hair with a fine comb. Where There Is No Doctor covers treatment " + c(11) + "."]))
    b.append(part("p5", "Part 5", "Care of the Dead"))
    b.append(h2("dead", "5.1 Handling and burying the dead"))
    b.append('<p>The Red Cross and WHO state that the bodies of people killed by injuries, drowning or fire in a disaster <b>do not cause epidemics</b>; the living are far more likely to spread disease ' + c(12, 13) + '. The exceptions are deaths from certain infectious diseases such as cholera, Ebola or Marburg ' + c(13) + '. The real risk is bodies <b>near or in water supplies</b>, which can contaminate the water with feces ' + c(13) + '.</p>')
    b.append(steps(["Wear gloves (or plastic bags) and wash hands with soap afterward " + c(13) + ".", "Record who the person is, where and when they were found, and keep their belongings with a label — families will want to know " + c(12) + ".", "Wrap the body in a sheet or bag. Lime powder does not speed decomposition and disinfecting bodies is not needed " + c(13) + ".", "Bury about <b>1.5 m (5 ft) deep</b> and <b>at least 200 m (650 ft) from streams, lakes, springs, beaches and drinking-water wells</b> " + c(12) + ".", "For several bodies, use one layer only (not stacked), leave about 0.4 m (16 in) between them, and mark each grave " + c(12) + "."]))
    b.append(danger("Deaths from infectious disease", "If someone died of severe diarrhea (possible cholera) or another contagious illness, handle the body as little as possible, wear gloves, keep body fluids away from water, wash hands thoroughly, and bury promptly far from water " + c(13) + "."))
    b.append(part("p6", "Part 6", "Region-by-Region Guide"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Number"], [["Latrine from well or spring", "≥ 30 m (100 ft) " + c(2)], ["Pit bottom above water table", "≥ 1.5 m (5 ft) " + c(2)], ["Toilets", "≥ 1 per 20 people; ≤ 50 m from homes " + c(4)], ["Grave depth", "~1.5 m (5 ft) " + c(12)], ["Grave from water sources", "≥ 200 m (650 ft) " + c(12)], ["Dry compost storage before use", "~1.5–2 years " + c(7)], ["Soap cure (cold process)", "2–6 weeks " + c(16)], ["Hand scrub", "≥ 20 seconds " + c(19)]]))
    b.append('<p class="small">General information for emergencies. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Sanitation & Hygiene", "Survival Info<br>Sanitation &amp;<br>Hygiene",
          "Toilets, latrines and composting, greywater, garbage and pests, homemade soap, and care of the dead — keeping disease away when sewers and running water stop, region by region across North America.",
          "Sanitation & Hygiene", TOC, cover_art(), "Medical · Water · Food · Electricity · Concrete · Tools · House · Bunkers")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Sanitation.pdf")
