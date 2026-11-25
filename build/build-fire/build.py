import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#12313d"/>'
    s += '<rect x="260" y="150" width="200" height="170" rx="8" fill="#37474f"/><rect x="340" y="40" width="40" height="110" fill="#455a64"/>'
    s += '<rect x="290" y="200" width="140" height="90" rx="6" fill="#263238"/><path d="M330 285 q-10 -40 20 -70 q0 30 15 30 q10 -25 0 -45 q45 35 25 85z" fill="#e69b00"/><path d="M345 285 q0 -25 15 -40 q10 25 15 40z" fill="#ffd54f"/>'
    for i in range(4): s += f'<rect x="{80+i*8}" y="{300-i*28}" width="120" height="24" rx="12" fill="#8d6e63" stroke="#5d4037" stroke-width="3"/>'
    s += '<path d="M600 320 l20 -60 l20 60z" fill="#e69b00"/><path d="M560 320 h120" stroke="#6d4c41" stroke-width="8"/>'
    for i in range(6): s += f'<circle cx="{560+i*25}" cy="{80+(i%2)*20}" r="3" fill="#fff"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Fire Basics", [("tri","1.1 Fuel, heat, air: the fire triangle"),("tinder","1.2 Tinder, kindling and fuel"),("lays","1.3 Building and putting out a fire")]),
 ("p2", "Part 2 · Fire Without Matches", [("ferro","2.1 Ferro rods, flint and steel"),("lens","2.2 Lenses and batteries"),("bow","2.3 Bow drill"),("ember","2.4 Keeping and carrying fire")]),
 ("p3", "Part 3 · Stoves", [("rocket","3.1 Rocket stoves"),("wood","3.2 Wood stoves for heat"),("cook","3.3 Cooking efficiently")]),
 ("p4", "Part 4 · Firewood", [("species","4.1 Which wood burns best"),("season","4.2 Cutting, splitting and seasoning"),("howmuch","4.3 How much wood you need")]),
 ("p5", "Part 5 · Fire & Carbon Monoxide Safety", [("chimney","5.1 Chimney care and chimney fires"),("co","5.2 Carbon monoxide"),("house","5.3 House fire prevention and escape")]),
 ("p6", "Part 6 · Winter Heating Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_triangle():
    s = t(360, 30, "The fire triangle: remove any side and the fire dies", 18, "middle", "700")
    s += '<polygon points="360,70 140,360 580,360" fill="#fff3e0" stroke="#e69b00" stroke-width="6"/>'
    s += t(360, 270, "FIRE", 34, "middle", "800", "#c0392b")
    s += t(200, 200, "HEAT", 20, "end", "700") + t(200, 224, "spark, flame, sun", 14, "end")
    s += t(520, 200, "AIR", 20, "start", "700") + t(520, 224, "oxygen, draft", 14, "start")
    s += t(360, 392, "FUEL — tinder, kindling, wood", 20, "middle", "700")
    return svg(720, 410, s)

def d_lays():
    s = t(360, 28, "Two basic fire lays", 18, "middle", "700")
    # teepee
    s += '<ellipse cx="190" cy="320" rx="70" ry="12" fill="#d7ccc8"/>'
    for dx in (-60, -30, 0, 30, 60): s += line(190+dx, 320, 190, 120, "#6d4c41", 7)
    s += '<ellipse cx="190" cy="300" rx="26" ry="16" fill="#ffe082" stroke="#e69b00" stroke-width="2"/>'
    s += t(190, 360, "Teepee: quick, hot start", 16, "middle", "700") + t(190, 384, "tinder in center, sticks leaning in", 14, "middle")
    # log cabin
    for i in range(5):
        y = 310 - i*28
        if i % 2 == 0: s += rect(440, y, 200, 20, "#8d6e63", "#5d4037", 2, 8)
        else: s += rect(452, y-4, 22, 28, "#8d6e63", "#5d4037", 2, 8) + rect(606, y-4, 22, 28, "#8d6e63", "#5d4037", 2, 8)
    s += '<ellipse cx="540" cy="300" rx="26" ry="14" fill="#ffe082" stroke="#e69b00" stroke-width="2"/>'
    s += t(540, 360, "Log cabin: long, steady fire", 16, "middle", "700") + t(540, 384, "good coals for cooking", 14, "middle")
    return svg(720, 400, s)

def d_bow():
    s = t(360, 28, "Bow drill parts", 18, "middle", "700")
    s += rect(120, 300, 480, 30, "#d7b98e", "#8a6d3b", 2, 4) + t(360, 360, "fireboard (dry softwood, e.g. cedar, willow, cottonwood)", 15, "middle")
    s += '<polygon points="350,300 370,300 380,330 340,330" fill="#5d4037"/>' + t(250, 395, "notch cut to the center of the burn hole; ember forms here on a leaf or bark", 14, "middle")
    s += rect(350, 120, 20, 180, "#bcaaa4", "#5d4037", 2, 6) + t(400, 230, "spindle (straight, dry, thumb-thick)", 15, "start")
    s += rect(310, 100, 100, 22, "#795548", "#3e2723", 2, 6) + t(420, 108, "handhold (bearing block, hard wood/stone)", 15, "start")
    s += '<path d="M120 190 Q360 120 600 190" fill="none" stroke="#6d4c41" stroke-width="8"/>' + line(120, 190, 600, 190, "#1f2a33", 2)
    s += t(120, 170, "bow (arm-length stick)", 15, "start") + t(560, 215, "cord loops once around spindle", 15, "end")
    return svg(720, 410, s)

def d_rocket():
    s = t(360, 28, "Rocket stove (cross-section)", 18, "middle", "700")
    s += rect(200, 110, 300, 250, "#cfd8dc", "#455a64", 3, 4) + t(350, 380, "outer can or brick box, filled with insulation (ash, perlite, vermiculite)", 14, "middle")
    s += '<path d="M310 120 L310 300 L230 300 L230 250 L270 250 L270 120 Z" fill="none" stroke="none"/>'
    s += rect(300, 110, 60, 200, "#fff", "#1f2a33", 3, 0) + rect(200, 250, 100, 60, "#fff", "#1f2a33", 3, 0)
    s += line(210, 268, 300, 268, "#6d4c41", 5) + line(210, 282, 300, 282, "#6d4c41", 5) + t(150, 240, "fuel feed:", 14, "end", "600") + t(150, 258, "sticks on a shelf,", 14, "end") + t(150, 276, "air flows under", 14, "end") + arrow(155, 295, 215, 296, "#2f7fbf")
    s += '<path d="M318 300 q-6 -60 12 -110 q10 50 18 110z" fill="#e69b00"/>'
    s += rect(280, 70, 100, 30, "#37474f", "#1f2a33", 2, 4) + t(330, 60, "pot", 14, "middle", "600")
    s += line(300, 100, 300, 110, "#1f2a33", 3) + line(360, 100, 360, 110, "#1f2a33", 3) + t(560, 100, "small gap under pot", 14, "start") + arrow(556, 98, 365, 105)
    s += t(560, 190, "combustion chimney:", 14, "start", "600") + t(560, 208, "about 3× taller than wide", 14, "start") + arrow(556, 200, 365, 200)
    s += t(560, 290, "feed, chamber and gaps", 14, "start") + t(560, 308, "about the same area", 14, "start")
    return svg(720, 400, s)

def d_clear():
    s = t(360, 26, "Keep anything that can burn 3 feet (1 m) from heat sources", 18, "middle", "700")
    s += rect(300, 150, 120, 140, "#455a64", "#263238", 3, 6) + rect(345, 70, 30, 80, "#607d8b", "#263238", 2, 0) + t(360, 230, "stove", 16, "middle", "700", "#fff")
    s += rect(220, 290, 280, 20, "#bdbdbd", "#616161", 2, 2) + t(360, 378, "non-combustible floor pad (stone, brick, metal) under and in front", 14, "middle")
    s += '<circle cx="360" cy="210" r="150" fill="none" stroke="#c0392b" stroke-width="3" stroke-dasharray="10 8"/>'
    s += rect(20, 160, 80, 120, "#ce93d8", "#6a1b9a", 2, 4) + t(60, 300, "curtains,", 14, "middle") + t(60, 318, "furniture", 14, "middle")
    s += rect(620, 200, 80, 80, "#d7b98e", "#8a6d3b", 2, 4) + t(660, 300, "wood box", 14, "middle")
    s += t(360, 405, "Ashes go in a metal can with a lid, outdoors, away from the house", 15, "middle", "600")
    return svg(720, 420, s)

R = {
 1: "<b>Heating is life or death</b> for most of the year. Wood is plentiful in the boreal forest (spruce, birch, aspen, tamarack) but absent on the tundra — there, people historically relied on oil lamps and very small, well-insulated shelters. Insulate first, heat one small room, and dry wood a full season ahead; cold dry air seasons wood well in summer. Ice fog and still air trap smoke and CO near the ground.",
 2: "Long, damp, mild winters: steady low heat rather than extreme cold. Wood dries slowly in wet air — store it under a roof with open sides (EPA) " + c(3) + " and cut a year ahead. Douglas-fir, alder and maple are common; cedar is easy kindling but low heat " + c(5) + ".",
 3: "<b>Severe cold and wind</b>, few trees. Wind chill drives heat loss " + c(13) + ". Plant and protect shelterbelts and woodlots now; burn ash, elm, cottonwood and hackberry from river bottoms " + c(5) + "; keep a stockpile larger than you think. Insulate, block wind, and heat one room.",
 4: "Cold snowy winters with good hardwoods — oak, maple, ash, hickory, black locust — some of the best firewood in North America " + c(5) + ". Emerald ash borer has killed many ash trees: standing dead ash is ready firewood but brittle and dangerous to fell.",
 5: "Long cold winters; excellent hardwoods (oak, maple, beech, birch) " + c(5) + ". Many older houses have chimneys — inspect and clean them before relying on them (5.1). Cities have little wood: plan for one heated room and salvaged wood.",
 6: "Mild-to-cool winters with occasional hard freezes; oak, hickory, pine abundant. Humidity slows seasoning — split and stack early. Summer heat is the bigger danger: cook outdoors on a rocket stove to keep houses cool.",
 7: "Little heating needed; cooking fuel and keeping houses cool matter more. Cook outdoors on rocket stoves (3.1); use dead palm fronds and pine only as kindling. Hurricane debris provides plenty of wood — let it dry.",
 8: "Cold desert nights and real winters at elevation; hot days. Pinyon and juniper are dense, high-heat woods " + c(5) + " but grow slowly — harvest dead wood first. Solar heat through south windows during the day, insulation at night.",
 9: "Long, cold mountain winters; lodgepole pine, Douglas-fir, aspen, Gambel oak (very high heat per cord) " + c(5) + ". Beetle-killed pine is abundant and dry. At altitude, fires burn differently and CO risk rises for people with heart or lung disease " + c(9) + ".",
 10: "Mild coastal winters, cold mountain winters; wildfire is a constant concern — follow strict outdoor fire safety (1.3). Oak is excellent fuel " + c(5) + ".",
 11: "Desert: cold nights, hot days. Mesquite and other desert hardwoods are dense but scarce; use rocket stoves to stretch fuel (3.1).",
 12: "Highlands get cold at night; lowlands are warm. Fuelwood shortages are common — rocket and plancha stoves, designed with Aprovecho's principles, were developed for exactly these conditions " + c(2) + ".",
 13: "Heating is rarely needed; fuel-efficient cooking matters. Improved cookstoves built on the same principles (such as stoves in Honduras and Nicaragua) cut wood use and smoke " + c(2) + ".",
}

SPECIES = [("Osage-orange","32.9","Excellent"),("Gambel oak","30.7","—"),("White oak","29.1","Excellent"),("Black locust","27.9","Excellent"),("Beech","27.5","—"),("Pinyon","27.1","—"),("Apple","27.0","Excellent"),("Honeylocust","26.7","Excellent"),("Bur oak","26.2","Excellent"),("Sugar & other maples","25.5","Excellent"),("Red oak","24.6","Excellent"),("White ash","24.2","Excellent"),("Black walnut","22.2","Excellent"),("Rocky Mtn juniper","21.8","Fair"),("Tamarack (larch)","21.8","Fair"),("Lodgepole pine","21.1","Fair"),("Birch","20.8","Fair"),("Douglas-fir","20.7","Good"),("Green ash","20.0","Excellent"),("American elm","20.0","Fair"),("Hemlock","19.3","—"),("Silver maple","19.0","Fair"),("Western redcedar","18.2","Fair"),("Quaking aspen","18.2","—"),("Willow","17.6","Poor"),("Alder","17.5","—"),("Ponderosa pine","16.2","Fair"),("White pine","15.9","—"),("Cottonwood","15.8","Fair"),("Spruce","15.5","Fair"),("Basswood","13.8","Fair"),("Eastern redcedar","13.0","Fair")]

def body():
    b = []
    b.append('<div class="pb"></div>' + h2("howto", "How to use this guide"))
    b.append('<p>Fire gives heat, cooked food, safe water and light. This beginner guide shows how to start a fire without matches, build efficient stoves, choose and season firewood, and stay safe from chimney fires and carbon monoxide — the silent killer of people heating closed rooms in a disaster. Part 6 explains winter heating for each North American region.</p>')
    b.append('<p>Numbered sources ' + c(1) + ' are listed at the end and saved as PDFs in <b>Survival Info Sources/Fire/</b>. See the Electricity guide for wood gasification and generators, and the House guide for chimneys, rocket mass heaters and insulation.</p>')
    b.append(check("Stock up now", ["Ferro rods (several), strike-anywhere matches in a waterproof jar, butane lighters, a magnifying lens", "Battery-powered CO alarms and smoke alarms with spare batteries " + c(15, 10), "Fire extinguishers; a metal ash can with lid; a chimney brush sized to your flue", "Axe, splitting maul, wedges, bow saw, files to sharpen them (see the Tools guide)", "Cotton balls and petroleum jelly, or other fire starters, in a sealed container", "Two winters of seasoned firewood if you heat with wood"]))
    b.append(part("p1", "Part 1", "Fire Basics"))
    b.append(h2("tri", "1.1 Fuel, heat, air: the fire triangle"))
    b.append('<p>A fire needs <b>fuel, heat and air (oxygen)</b>. Take any one away and it goes out ' + c(1) + '. Most failed fires have too little air (packed too tight), too much moisture in the fuel, or too big a jump from tinder to large wood.</p>')
    b.append(fig(d_triangle(), "<b>Figure 1.</b> The fire triangle."))
    b.append(h2("tinder", "1.2 Tinder, kindling and fuel"))
    b.append(table(["Stage", "Size", "Examples"], [["Tinder", "Hair-thin, fluffy, bone dry", "Birch bark, dry grass, cattail fluff, cedar bark rubbed to fibers, fatwood shavings, cotton with petroleum jelly, char cloth " + c(1)], ["Kindling", "Pencil to thumb thickness", "Dry dead twigs snapped off standing trees (they snap cleanly), split softwood"], ["Fuel", "Wrist-size and up", "Split, seasoned firewood (Part 4)"]]))
    b.append(tip("Find dry wood in the rain", "Dead branches still on trees, the inside of split logs, and fatwood (resin-soaked pine stumps) are dry when the ground is soaked. Collect twice as much tinder and kindling as you think you need before you strike a spark."))
    b.append(h2("lays", "1.3 Building and putting out a fire"))
    b.append(fig(d_lays(), "<b>Figure 2.</b> Teepee and log-cabin fire lays."))
    b.append(ul(["Clear a spot down to bare soil, away from overhanging branches, tents and dry grass. Smokey Bear\'s guidance: stay at least 15 feet from tents, vegetation and low branches, and avoid windy spots " + c(12) + ".", "Put tinder in the center, kindling over it, light from the upwind side, and add larger wood gradually.", "<b>Put it out completely:</b> drown, stir, drown again, and feel — if it is too hot to touch, it is too hot to leave. Don\'t rely on dirt or sand alone " + c(12) + "."]))
    b.append(part("p2", "Part 2", "Fire Without Matches"))
    b.append(h2("ferro", "2.1 Ferro rods, flint and steel"))
    b.append('<p>A <b>ferrocerium rod</b> throws very hot sparks when scraped with the back of a knife or a striker, even when wet. Hold the striker still on top of the tinder and pull the rod back so you don\'t knock the tinder apart. <b>Flint and steel</b>: strike a high-carbon steel striker down a sharp edge of flint, quartz or chert so sparks fall on char cloth, which catches a glowing ember; fold it into a tinder bundle and blow gently into flame ' + c(1) + '.</p>')
    b.append(tip("Make char cloth", "Pack squares of 100% cotton cloth in a small metal tin with a nail hole in the lid. Set it in the fire. Smoke will jet from the hole; when it stops, remove the tin and let it cool closed. The cloth should be black but not falling apart."))
    b.append(h2("lens", "2.2 Lenses and batteries"))
    b.append(ul(["<b>Lens:</b> a magnifying glass, the lens from binoculars or a camera, or even a clear water-filled bottle can focus sunlight to a tiny bright point on dark tinder or char cloth " + c(1) + ". Needs bright sun.", "<b>Battery:</b> FM 21-76 describes attaching a wire to each battery terminal and touching the bare ends together next to the tinder to make a spark " + c(1) + ". Fine steel wool touched across a 9-volt battery's terminals also glows and lights tinder. Keep steel wool away from batteries in your pack."]))
    b.append(h2("bow", "2.3 Bow drill"))
    b.append('<p>The bow drill is the most reliable friction method, but it takes practice — learn it <b>before</b> you need it ' + c(1) + '.</p>')
    b.append(fig(d_bow(), "<b>Figure 3.</b> Bow drill set. All wooden parts must be completely dry."))
    b.append(steps(["Carve a shallow pit near the edge of the fireboard and a matching point on the spindle.", "Loop the bow cord once around the spindle; put the spindle in the pit and press down with the handhold, your wrist braced against your shin.", "Saw the bow back and forth with long, steady strokes until the pit is black and smoking. Then cut a pie-slice notch from the edge into the center of the burned pit.", "Drill again, faster and with more pressure, until fine black dust fills the notch and keeps smoking on its own — that is your ember.", "Tip the ember into a tinder bundle, fold the bundle around it, and blow gently until it bursts into flame."]))
    b.append(h2("ember", "2.4 Keeping and carrying fire"))
    b.append('<p>Starting fires uses scarce supplies, so keep one going. Bank a stove at night by raking coals together and adding a large, dense piece of wood with the air nearly closed (but never so closed that it smolders and smokes heavily, which builds creosote — 5.1). To carry fire, put live coals in a metal can with a few holes and pack it with dry punky wood or tinder fungus.</p>')
    b.append(part("p3", "Part 3", "Stoves"))
    b.append(h2("rocket", "3.1 Rocket stoves"))
    b.append('<p>A rocket stove burns the ends of small sticks in an insulated chimney, giving a hot, clean fire with far less wood than an open fire. It follows Dr. Larry Winiarski\'s ten design principles, published by Aprovecho Research Center ' + c(2) + '.</p>')
    b.append(fig(d_rocket(), "<b>Figure 4.</b> A rocket stove built on Aprovecho's principles " + c(2) + "."))
    b.append(table(["Aprovecho principle " + c(2), "What it means for your build"], [["Insulate around the fire", "Pack ash, perlite, vermiculite or other light heat-proof material around the chamber"], ["Short insulated chimney above the fire, about 3× taller than wide", "e.g., a 4 in (10 cm) chamber about 12 in (30 cm) tall"], ["Burn only the tips of the sticks", "Push sticks in as they burn; the rest stays cool and doesn\'t smoke"], ["Heat level set by how many sticks", "More sticks = more heat"], ["Good draft; not too much excess air", "Keep openings small"], ["Same cross-section area throughout", "Feed opening, chamber and gaps about the same size"], ["Use a grate or shelf under the sticks", "Air passes under the fuel"], ["Insulate the heat path; small gaps at the pot", "A skirt around the pot with a narrow gap forces heat against it"]]))
    b.append(steps(["Make an L-shaped tube: use a large can or stovepipe elbow, or bricks/stones, with a 4 in (10 cm) opening.", "Set it inside a larger can or box and fill around it with insulation (wood ash works).", "Put a metal shelf in the feed opening so sticks sit on top and air flows underneath.", "Set three small supports on top so the pot sits just above the chimney with a small gap.", "Light a little paper and twigs in the chamber, then feed sticks horizontally."]))
    b.append(h2("wood", "3.2 Wood stoves for heat"))
    b.append(ul(["EPA says an open wood-burning fireplace is a very inefficient way to heat a home, because its draft pulls warm air up the chimney " + c(11) + "; a closed stove with a good chimney does far better.", "Place it on a non-combustible floor pad and keep anything that can burn at least <b>3 feet (1 m)</b> away " + c(8) + ".", "Never start a fire with gasoline, kerosene or charcoal lighter fluid " + c(3) + ".", "Burn hot, small fires of dry wood rather than smoldering big loads; smoke is wasted fuel and builds creosote " + c(3, 2) + ".", "Do not burn trash, plastics, painted or treated wood " + c(3) + "."]))
    b.append(fig(d_clear(), "<b>Figure 5.</b> Clearances around a stove " + c(8) + "."))
    b.append(danger("Never heat with these indoors", "No charcoal grills, camp stoves, generators, or gas ovens for heating inside a home, garage or tent. They produce carbon monoxide " + c(9, 10) + ". USFA: never use an oven to heat your home " + c(8) + "."))
    b.append(h2("cook", "3.3 Cooking efficiently"))
    b.append(ul(["Aprovecho notes that improving heat transfer to the pot is the most important factor in reducing fuel use " + c(2) + ". Use lids, a pot skirt, and pots that fit the fire.", "Use a <b>retained-heat cooker</b> (hay box): bring food to a boil, then nest the covered pot in a box packed with blankets, hay or sleeping bags for several hours to finish cooking without fuel.", "Soak beans and grains overnight to shorten cooking time.", "Cook outdoors in summer to keep the house cool."]))
    b.append(part("p4", "Part 4", "Firewood"))
    b.append(h2("species", "4.1 Which wood burns best"))
    b.append('<p>Dense hardwoods give the most heat per cord. Values below are <b>million BTU per cord of dry wood</b> and overall quality ratings from Utah State University Extension ' + c(5) + '. (A cord is a stack 4 × 4 × 8 ft, 128 cubic feet.)</p>')
    b.append(table(["Species", "Heat per dry cord (million BTU)", "Overall quality"], [list(x) for x in SPECIES]))
    b.append(tip("Use softwoods smartly", "Pines, spruces, fir and cedar light easily and burn fast — great kindling and fine fuel in a stove that is burned hot, but they give less heat per load. Many species throw sparks " + c(5) + "; use a screen in open fires."))
    b.append(h2("season", "4.2 Cutting, splitting and seasoning"))
    b.append(ul(["EPA: burn only dry, split, well-seasoned wood; season it for <b>at least six months</b>; it burns best below <b>20 percent moisture</b> " + c(3) + ".", "Seasoned wood is darker, weighs less, and sounds hollow when knocked against another piece " + c(3) + "; cracks in the end grain are another sign.", "Store wood outdoors, off the ground, with only the top covered — covering the sides traps moisture " + c(3) + ".", "Split wood dries much faster than whole rounds. Cut to stove length, split, and stack in single rows with air between.", "Felling trees is dangerous: see the Tools and House guides for safe felling."]))
    b.append(h2("howmuch", "4.3 How much wood you need"))
    b.append('<p>Wood use depends on climate, house size, insulation and stove. Measure it: count how many armloads or wheelbarrows you burn on a cold week, and multiply by the length of your heating season. Then cut more — a hard winter or wet wood can double use. Heat one well-insulated room instead of a whole house to cut wood needs dramatically.</p>')
    b.append(part("p5", "Part 5", "Fire & Carbon Monoxide Safety"))
    b.append(h2("chimney", "5.1 Chimney care and chimney fires"))
    b.append('<p>Wood smoke leaves <b>creosote</b>, a tar that coats the chimney and can catch fire. NFPA and USFA recommend cleaning and inspecting chimneys every year ' + c(7, 8) + '. With no chimney sweeps, do it yourself:</p>')
    b.append(steps(["Let the stove go cold. Seal the stove door or fireplace opening with plastic and tape.", "From the roof (tie off — falls kill) or from below, run a brush sized to your flue up and down the whole length.", "Clean out the soot and creosote from the bottom; check for cracks, loose bricks, rust-through and blockages (bird nests).", "Check more often (monthly in heavy use) if you burn softwood or let fires smolder."]))
    b.append(danger("Chimney fire", "Signs: a loud roaring or rumbling, dense smoke, flames or sparks shooting from the chimney top. Get everyone out, close the stove air controls if you can do so safely, and watch the roof and attic for spread. Inspect the chimney for damage before using it again."))
    b.append(h2("co", "5.2 Carbon monoxide"))
    b.append('<p>Carbon monoxide (CO) is an invisible, odorless gas from any burning fuel. It replaces oxygen in the blood ' + c(9) + '. Symptoms include headache, dizziness, weakness, nausea, vomiting, confusion, drowsiness and fainting — often mistaken for the flu ' + c(9) + '. Pets often show symptoms before people do ' + c(9) + '.</p>')
    b.append(ul(["Install battery-operated CO detectors " + c(10) + " — put one near every sleeping area and check the batteries.", "Run generators outdoors only, never inside a home, basement or garage, and well away from doors, windows and vents " + c(10) + ".", "If anyone has symptoms, or the alarm sounds, get everyone into fresh air immediately and open the house up.", "Young children, older adults, pregnant women, people with heart or lung disease, and people at high altitude are most at risk " + c(9) + "."]))
    b.append(h2("house", "5.3 House fire prevention and escape"))
    b.append(ul(["A fire can become life-threatening in two minutes; smoke and toxic gases kill more people than flames " + c(14) + ".", "Working smoke alarms greatly increase survival " + c(14) + "; keep spare batteries.", "Plan two ways out of every room and a meeting place; practice at night.", "Keep candles and lamps away from curtains and children; never leave them burning unattended.", "Store fuel (kerosene, gasoline, propane) outside the house."]))
    b.append(part("p6", "Part 6", "Winter Heating Region by Region"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Value"], [["Seasoning time", "≥ 6 months; < 20% moisture " + c(3)], ["Clearance from heat sources", "≥ 3 ft (1 m) " + c(8)], ["Chimney cleaning", "At least yearly " + c(7, 8)], ["Rocket stove chamber", "≈ 3× taller than wide " + c(2)], ["Cord", "4 × 4 × 8 ft = 128 ft³"], ["Campfire clearance", "≥ 15 ft from tents and vegetation " + c(12)], ["Put out a fire", "Drown, stir, drown, feel " + c(12)]]))
    b.append('<p class="small">General information for emergencies. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Fire & Heating", "Survival Info<br>Fire &amp;<br>Heating",
          "Fire without matches, rocket stoves and wood stoves, choosing and seasoning firewood, chimney and carbon-monoxide safety, and winter heating for every region of North America.",
          "Fire & Heating", TOC, cover_art(), "Medical · Sanitation · Water · Food · Electricity · Concrete · Tools · House · Bunkers")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Fire.pdf")
