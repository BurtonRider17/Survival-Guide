import sys, math; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#0d1b2a"/>'
    for i, (x, y) in enumerate([(80,60),(150,40),(230,70),(300,50),(420,30),(520,80),(610,50),(660,120),(40,140),(560,150)]): s += f'<circle cx="{x}" cy="{y}" r="{2 + i%3}" fill="#fff"/>'
    s += '<path d="M0 300 L140 190 L240 260 L360 150 L480 250 L600 180 L720 270 V380 H0z" fill="#1b4332"/>'
    s += '<circle cx="360" cy="270" r="80" fill="#eceff1" stroke="#90a4ae" stroke-width="6"/>'
    s += '<polygon points="360,200 375,270 360,340 345,270" fill="#c62828"/><polygon points="360,270 375,270 360,340 345,270" fill="#37474f"/>'
    s += t(360, 185, "N", 22, "middle", "800", "#eceff1")
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Maps", [("maps","1.1 Reading a topographic map"),("orient","1.2 Orienting the map")]),
 ("p2", "Part 2 · The Compass", [("comp","2.1 Azimuths and back azimuths"),("decl","2.2 Declination: magnetic vs. true north"),("metal","2.3 What throws a compass off"),("tech","2.4 Bypassing obstacles and aiming off")]),
 ("p3", "Part 3 · Distance: Pace Counting", [("pace","3.1 Finding your pace count"),("adjust","3.2 Adjusting for ground and weather")]),
 ("p4", "Part 4 · Without a Compass", [("sun","4.1 Shadow-stick method"),("watch","4.2 Watch method"),("stars","4.3 Stars: Polaris and the Southern Cross"),("moon","4.4 The moon, and improvised compasses")]),
 ("p5", "Part 5 · Traveling on Foot and by Bike", [("route","5.1 Planning a route"),("bike","5.2 Bicycles"),("bag","5.3 The go-bag")]),
 ("p6", "Part 6 · Crossing Water Safely", [("river","6.1 Choosing a crossing"),("ford","6.2 Fording: alone and in a group"),("bog","6.3 Floodwater, bogs and quicksand")]),
 ("p7", "Part 7 · Travel Hazards Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

DECL = [("Anchorage", 13.9), ("Seattle", 14.8), ("Calgary", 13.3), ("Los Angeles", 11.3), ("Salt Lake City", 10.7), ("Phoenix", 9.6), ("Denver", 7.5), ("Regina", 8.2), ("Chihuahua", 6.9), ("Mexico City", 3.9), ("Kansas City", 1.0), ("Houston", 1.7), ("Guatemala City", 0.1), ("Chicago", -4.2), ("Atlanta", -5.6), ("Havana", -5.8), ("Miami", -7.4), ("Toronto", -10.1), ("Boston", -13.9), ("San Juan", -13.7), ("Halifax", -16.1), ("Iqaluit", -23.9)]

def d_decl():
    s = t(360, 26, "Declination, late 2026 (+ = east, − = west)", 19, "middle", "700")
    x0 = 400; sc = 11
    s += line(x0, 40, x0, 40 + len(DECL)*22 + 6, "#263238", 2)
    for i, (k, v) in enumerate(DECL):
        y = 46 + i*22
        col = "#1e88e5" if v >= 0 else "#e53935"
        if v >= 0: s += rect(x0, y, v*sc, 16, col, "none", 0, 2) + t(x0 + v*sc + 6, y + 13, f"{v:+.1f}°", 13, "start", "700")
        else: s += rect(x0 + v*sc, y, -v*sc, 16, col, "none", 0, 2) + t(x0 + v*sc - 6, y + 13, f"{v:+.1f}°", 13, "end", "700")
        s += t(x0 - 8 if v >= 0 else x0 + 8, y + 13, k, 13, "end" if v >= 0 else "start")
    h = 46 + len(DECL)*22 + 20
    s += t(360, h, "Computed with NOAA/NGA World Magnetic Model 2025. It drifts each year.", 13, "middle", "600")
    return svg(720, h + 12, s)

def d_declrule():
    s = t(360, 28, "Which way to correct", 19, "middle", "700")
    for k, (lab, ang, txt1, txt2) in enumerate([("EAST declination (West Coast)", 15, "Compass needle points east of true north.", "Map→ground: SUBTRACT · Ground→map: ADD"), ("WEST declination (East Coast)", -15, "Compass needle points west of true north.", "Map→ground: ADD · Ground→map: SUBTRACT")]):
        cx = 180 + k*360
        s += line(cx, 230, cx, 70, "#263238", 4) + t(cx, 60, "True N ★", 14, "middle", "700")
        a = math.radians(ang); s += line(cx, 230, cx + 160*math.sin(a), 230 - 160*math.cos(a), "#c62828", 4) + t(cx + 175*math.sin(a), 230 - 170*math.cos(a), "MN", 14, "middle", "700", "#c62828")
        s += t(cx, 262, lab, 15, "middle", "700") + t(cx, 284, txt1, 13, "middle") + t(cx, 304, txt2, 13, "middle", "700")
    s += t(360, 335, "Memory aid: “East is least, west is best” — subtract east, add west when going from map (true) to compass (magnetic)", 13, "middle", "600")
    return svg(720, 350, s)

def d_contour():
    s = t(360, 28, "Contour lines: closer together = steeper", 19, "middle", "700")
    for i in range(6): s += f'<ellipse cx="{220 + i*22}" cy="210" rx="{170 - i*28}" ry="{120 - i*20}" fill="none" stroke="#8d6e63" stroke-width="2"/>'
    s += '<ellipse cx="335" cy="210" rx="8" ry="8" fill="#c62828"/>' + t(345, 200, "summit", 13, "start")
    s += t(60, 350, "gentle side: lines far apart", 14, "start", "600") + t(330, 350, "steep side: lines close", 14, "start", "600")
    s += '<path d="M460 300 L560 140 L660 300" fill="#d7ccc8" stroke="#6d4c41" stroke-width="3"/>' + t(560, 330, "the same hill side-on", 13, "middle")
    s += t(560, 70, "Contour interval (map margin)", 13, "middle", "700") + t(560, 88, "= height between lines", 13, "middle")
    return svg(720, 370, s)

def d_bypass():
    s = t(360, 28, "Box around an obstacle · aim off to a road or stream", 19, "middle", "700")
    s += line(40, 150, 120, 150, "#263238", 3) + arrow(120, 150, 120, 250) + arrow(120, 250, 270, 250) + arrow(270, 250, 270, 150) + arrow(270, 150, 340, 150)
    s += rect(140, 110, 110, 110, "#a5d6a7", "#2e7d32", 2, 8) + t(195, 170, "swamp", 14, "middle", "600")
    s += t(195, 290, "e.g. course 90°: go 180° 100 m,", 13, "middle") + t(195, 308, "90° 150 m, 360° 100 m, then 90° again", 13, "middle")
    s += line(420, 300, 700, 300, "#1e88e5", 6) + t(560, 325, "stream (a line you cannot miss)", 13, "middle", "600")
    s += '<circle cx="560" cy="300" r="10" fill="#c62828"/>' + t(560, 280, "goal", 13, "middle", "700")
    s += line(560, 60, 520, 300, "#263238", 3, "8 5") + arrow(560, 60, 522, 294) + t(470, 200, "aim 10° left", 13, "end", "600")
    s += t(600, 120, "on reaching the stream", 13, "start") + t(600, 138, "you KNOW to turn right", 13, "start", "700")
    return svg(720, 340, s)

def d_pace():
    s = t(360, 28, "Pace count: 1 pace = 1 natural step; count per 100 m", 19, "middle", "700")
    s += line(40, 130, 680, 130, "#8d6e63", 6) + t(40, 160, "start", 13, "start") + t(680, 160, "100 m", 13, "end", "700")
    for i in range(12): s += f'<ellipse cx="{70 + i*52}" cy="{118 if i%2 else 142}" rx="12" ry="6" fill="#455a64"/>'
    s += t(360, 195, "Walk a measured course on similar ground; 600 m course → total paces ÷ 6", 14, "middle", "600")
    s += line(240, 230, 240, 330, "#6d4c41", 3)
    for i in range(9): s += f'<circle cx="240" cy="{240 + i*10}" r="5" fill="{"#e69b00" if i < 4 else "#bdbdbd"}"/>'
    s += t(270, 260, "pebbles, knots or beads:", 14, "start", "700") + t(270, 280, "move one every 100 m —", 14, "start") + t(270, 300, "never trust memory", 14, "start")
    return svg(720, 345, s)

def d_shadow():
    s = t(360, 28, "Shadow-stick method (works anywhere on Earth)", 19, "middle", "700")
    s += rect(60, 60, 600, 250, "#fff8e1", "#e0c070", 2, 8)
    s += line(360, 260, 360, 120, "#5d4037", 8) + t(372, 120, "stick ~1 m", 13, "start")
    s += line(360, 260, 200, 200, "#9e9e9e", 4) + '<circle cx="200" cy="200" r="9" fill="#263238"/>' + t(200, 185, "1st mark = WEST", 14, "middle", "700")
    s += line(360, 260, 280, 160, "#bdbdbd", 4, "6 4") + '<circle cx="280" cy="160" r="9" fill="#c62828"/>' + t(300, 150, "2nd mark (10–15 min later) = EAST", 14, "start", "700", "#c62828")
    s += line(130, 237, 340, 132, "#1e88e5", 3) + t(120, 250, "W–E line", 13, "end", "600", "#1e88e5")
    s += t(360, 335, "Stand with the first mark on your left and the second on your right: you face NORTH", 14, "middle", "700")
    return svg(720, 350, s)

def d_stars():
    s = '<rect width="720" height="380" fill="#0d1b2a"/>' + t(360, 28, "Finding Polaris (north sky)", 19, "middle", "700", "#fff")
    dip = [(110, 250), (170, 240), (180, 300), (120, 310), (230, 280), (280, 285), (330, 310)]
    for x, y in dip: s += f'<circle cx="{x}" cy="{y}" r="6" fill="#fff"/>'
    s += f'<polyline points="{" ".join(f"{x},{y}" for x, y in [dip[0], dip[1], dip[2], dip[3], dip[0]])}" fill="none" stroke="#90a4ae" stroke-width="1.5"/>'
    s += f'<polyline points="{" ".join(f"{x},{y}" for x, y in [dip[2], dip[4], dip[5], dip[6]])}" fill="none" stroke="#90a4ae" stroke-width="1.5"/>'
    s += line(120, 310, 110, 250, "#ffd54f", 2) + line(110, 250, 75, 60, "#ffd54f", 2, "6 5")
    s += t(150, 340, "Big Dipper: pointer stars on the outer lip", 13, "middle", "600", "#fff")
    s += '<circle cx="80" cy="85" r="9" fill="#ffe082"/>' + t(100, 80, "POLARIS (≈5× the pointer gap)", 14, "start", "800", "#ffe082")
    cas = [(500, 120), (540, 160), (580, 125), (620, 165), (660, 120)]
    for x, y in cas: s += f'<circle cx="{x}" cy="{y}" r="6" fill="#fff"/>'
    s += f'<polyline points="{" ".join(f"{x},{y}" for x, y in cas)}" fill="none" stroke="#90a4ae" stroke-width="1.5"/>'
    s += t(580, 200, "Cassiopeia (“W”), opposite the Dipper;", 13, "middle", "600", "#fff") + t(580, 218, "Polaris lies straight out from its center star", 13, "middle", "", "#fff")
    s += t(360, 365, "Both circle Polaris counterclockwise and never set. Straight down from Polaris is true north.", 13, "middle", "600", "#fff")
    return svg(720, 380, s)

def d_ford():
    s = t(360, 28, "Fording swift water", 19, "middle", "700")
    s += rect(20, 50, 680, 260, "#bbdefb", "none", 0, 6)
    for i in range(6): s += arrow(40, 70 + i*40, 120, 70 + i*40, "#1565c0")
    s += t(80, 300, "current", 13, "middle", "600", "#0d47a1")
    s += '<circle cx="250" cy="180" r="18" fill="#ffcc80" stroke="#37474f" stroke-width="2"/>' + line(250, 180, 190, 150, "#6d4c41", 7) + t(250, 230, "pole planted upstream,", 13, "middle") + t(250, 248, "~7.5 cm thick, 2.1–2.4 m long", 13, "middle")
    s += line(420, 120, 640, 120, "#6d4c41", 7)
    for i, x in enumerate((440, 510, 580, 640)): s += f'<circle cx="{x}" cy="{120}" r="{14 + i*2}" fill="#ffcc80" stroke="#37474f" stroke-width="2"/>'
    s += t(440, 160, "lightest", 13, "middle", "700") + t(440, 176, "upstream", 13, "middle") + t(640, 160, "heaviest", 13, "middle", "700") + t(640, 176, "downstream", 13, "middle")
    s += t(540, 210, "group: pole parallel to the current;", 13, "middle") + t(540, 228, "the upstream person breaks the flow", 13, "middle")
    s += line(400, 290, 560, 230, "#263238", 3, "8 5") + t(600, 280, "cross angled downstream, ~45°", 13, "middle", "700")
    return svg(720, 320, s)

R = {
 1: "Declination is large and changes fast — about +14° to +15° in Anchorage and Yellowknife, about −24° at Iqaluit; near the magnetic pole compasses become unreliable " + c(3, 4) + ". Polaris is high overhead. Never wade very cold rivers; FM 21-76 warns it can be fatal — build a raft or find another way " + c(2) + ". Whiteout, sea ice and long darkness: travel in daylight, pace-count, and handrail along coasts and rivers " + c(1) + ".",
 2: "Declination about +15° east " + c(4) + ". Thick forest and cloud often hide sun and stars — rely on compass and handrails such as rivers and ridgelines " + c(1) + ". Rain-swollen rivers and tidal estuaries are dangerous crossings " + c(2) + ".",
 3: "Open, flat country with few landmarks: dead reckoning with compass and pace count matters " + c(1) + ". Declination ranges from about +8° in Saskatchewan to near 0° in Kansas " + c(4) + ". Blizzards and flash floods in creek beds " + c(6) + ".",
 4: "Declination a few degrees west (about −4° Chicago, −7.5° Detroit) " + c(4) + ". Roads and section lines form a grid of handrails. Floodwater over roads: 6 inches of moving water can knock you down " + c(6) + ".",
 5: "West declination of −10° to −16° " + c(4) + " — forget it and you will drift far off course. Rugged, forested hills; spring rivers run high and cold " + c(2) + ".",
 6: "Swamps, bayous and big rivers: cross where vegetation shows firm ground; avoid open mud " + c(2) + ". Hurricane flooding: never walk or drive into moving water " + c(6) + ".",
 7: "Flat, low terrain and few viewpoints; climb a tree or building to plan routes " + c(2) + ". Mangrove coasts: move at low tide and watch for crocodiles and alligators " + c(2) + ". Declination about −7° " + c(4) + ".",
 8: "Flash floods in dry washes and slot canyons can arrive from storms far away " + c(6) + ". Long distances between water. Declination about +10° " + c(4) + ".",
 9: "Steep terrain and avalanches: most slab avalanches start on slopes of 30° to 50° " + c(7) + " — stay off and out from under them in snow. Declination +7° to +13° " + c(4) + ". Snowmelt rivers are fast and cold " + c(2) + ".",
 10: "Declination about +11° to +13° " + c(4) + ". Mountain snow and avalanches in the Sierra " + c(7) + "; flash floods in desert areas " + c(6) + "; wildfire can close routes fast.",
 11: "Desert and sierra; arroyos flood suddenly " + c(6) + ". Declination about +4° to +7° " + c(4) + ".",
 12: "Highlands, volcanoes and deep barrancas — contour lines tell you where routes are possible " + c(1) + ". Declination about +3° to +4° " + c(4) + ". Rainy-season rivers rise quickly.",
 13: "Declination near 0° in Guatemala, about −6° in Cuba and −14° in Puerto Rico " + c(4) + ". Jungle hides the sky: use compass and streams as handrails " + c(1) + "; cross mangroves at low tide " + c(2) + ".",
}

def body():
    b = []
    b.append(part("p1", "Part 1", "Maps"))
    b.append('<p>Land navigation combines map reading, <b>dead reckoning</b> (compass direction plus measured distance) and <b>terrain association</b> (matching the land to the map) ' + c(1) + '. Get paper topographic maps of your area and routes now; print several copies and keep them dry.</p>')
    b.append(h2("maps", "1.1 Reading a topographic map"))
    b.append(fig(d_contour(), "The closer the contour lines, the steeper the slope " + c(1) + "."))
    b.append(ul(["Check the margin: scale, <b>contour interval</b> (height between lines), and the <b>declination diagram</b> showing true, grid and magnetic north " + c(1) + ".", "The declination diagram is not drawn to scale — use the number written beside it " + c(1) + ".", "Old maps may be out of date: new roads, missing bridges. Mark changes as you find them " + c(1) + "."]))
    b.append(h2("orient", "1.2 Orienting the map"))
    b.append('<p>A map is oriented when it lies flat with its north matching north on the ground ' + c(1) + '.</p>')
    b.append(steps(["<b>With a compass:</b> lay the compass edge along a north–south grid line, then turn map and compass together until the needle points to north — then correct for declination (2.2) " + c(1) + ".", "<b>By terrain association:</b> find features you can see — a hill, a road, a river bend — and turn the map until they line up with the land " + c(1) + "."]))
    b.append(tip("Keep your thumb on it", "As you walk, keep your thumb on your current position on the map so you never have to search the whole sheet " + c(1) + "."))

    b.append(part("p2", "Part 2", "The Compass"))
    b.append(h2("comp", "2.1 Azimuths and back azimuths"))
    b.append('<p>An <b>azimuth</b> is a direction measured clockwise from north, 0–360°. The <b>back azimuth</b> points the opposite way: add 180° if the azimuth is 180° or less; subtract 180° if it is more. Example: 115° → 295° ' + c(1) + '. Use back azimuths to return the way you came.</p>')
    b.append(h2("decl", "2.2 Declination: magnetic vs. true north"))
    b.append('<p>Declination is the angle between magnetic north (where the needle points) and true north; it is positive east and negative west, and <b>changes over time and with location</b> ' + c(3) + '. If you do not correct for it, directions between map and ground will be wrong by the full declination ' + c(1) + '. At 15°, that is about 270 m off course for every kilometer walked.</p>')
    b.append(fig(d_declrule(), "Apply the correction every time you move a direction between map and ground."))
    b.append(fig(d_decl(), "Declination values computed for late 2026 from the World Magnetic Model " + c(4) + "; use the figure on a current map if you have one."))
    b.append(h2("metal", "2.3 What throws a compass off"))
    b.append(table(["Keep the compass at least…", "from"], [["55 m", "High-tension power lines " + c(1)], ["18 m", "Cars, trucks and heavy machinery " + c(1)], ["10 m", "Telephone wires and barbed wire " + c(1)], ["½ m", "A steel helmet or tools " + c(1)]]))
    b.append(h2("tech", "2.4 Bypassing obstacles and aiming off"))
    b.append(fig(d_bypass(), "Right-angle detour and deliberate offset from FM 3-25.26 " + c(1) + "."))
    b.append(ul(["<b>Detour by right angles:</b> on a 90° course, turn to 180° for 100 m, then 90° for 150 m, then 360° for 100 m, then back on 90° — you are back on your line " + c(1) + ".", "<b>Deliberate offset:</b> when the goal is on a road or stream, aim about 10° to one side. Each degree moves you about 18 m sideways per 1,000 m; when you hit the line, you know which way to turn " + c(1) + ".", "<b>Handrails</b> are linear features — trails, fences, roads, streams — you can follow quickly. <b>Attack points</b> are easy landmarks near your goal (stream junctions, bridges, road crossings) to navigate the last stretch from " + c(1) + "."]))

    b.append(part("p3", "Part 3", "Distance: Pace Counting"))
    b.append(h2("pace", "3.1 Finding your pace count"))
    b.append(fig(d_pace(), "Pace count method from FM 3-25.26 " + c(1) + "."))
    b.append('<p>A pace is one natural step, about 30 inches. Learn how many paces you take in 100 meters by walking a measured course (100–600 m) on ground like the ground you will travel ' + c(1) + '. Keep track with pebbles, knots in a string, or marks in a notebook — never by memory ' + c(1) + '.</p>')
    b.append(h2("adjust", "3.2 Adjusting for ground and weather"))
    b.append(table(["Condition", "Effect on pace " + c(1)], [["Uphill", "Shorter (120 paces may become 130 or more)"], ["Downhill", "Longer"], ["Head wind / tail wind", "Shorter / longer"], ["Sand, gravel, mud, snow", "Shorter"], ["Falling snow, rain, ice", "Shorter"], ["Heavy clothing, poor-traction boots", "Shorter"], ["Fog, rain, darkness", "Shorter"]]))

    b.append(part("p4", "Part 4", "Without a Compass"))
    b.append('<p>The sun rises roughly east and sets roughly west, varying with the season. In the Northern Hemisphere the sun is due south at its highest point, and shadows move clockwise ' + c(2) + '.</p>')
    b.append(h2("sun", "4.1 Shadow-stick method"))
    b.append(fig(d_shadow(), "FM 21-76 shadow-tip method " + c(2) + "."))
    b.append(steps(["Push a straight stick about 1 m long into level ground; mark the tip of its shadow. <b>The first mark is always west</b> " + c(2) + ".", "Wait 10–15 minutes and mark the new tip " + c(2) + ".", "A line through the two marks runs roughly east–west " + c(2) + ".", "Stand with the first mark on your left and the second on your right — you face north, anywhere on Earth " + c(2) + "."]))
    b.append('<p>More accurate: mark a morning shadow tip, draw an arc through it around the stick, and mark where the afternoon shadow touches the arc again; the line between is east–west ' + c(2) + '.</p>')
    b.append(h2("watch", "4.2 Watch method"))
    b.append('<p>Northern Hemisphere: hold an analog watch flat, point the <b>hour hand at the sun</b>; halfway between the hour hand and 12 is south (the other end of that line is north). On daylight saving time, use halfway to 1 o\'clock. It is more accurate farther from the equator ' + c(2) + '. With a digital watch, draw a clock face with the time on paper ' + c(2) + '.</p>')
    b.append(h2("stars", "4.3 Stars: Polaris and the Southern Cross"))
    b.append(fig(d_stars(), "Big Dipper, Cassiopeia and Polaris from FM 21-76 " + c(2) + "."))
    b.append(ul(["Extend the line through the Big Dipper's two outer-lip \"pointer\" stars about <b>five times</b> their spacing to reach Polaris, the North Star " + c(2) + ".", "Cassiopeia's W sits opposite the Dipper; Polaris lies straight out from its center star. Both circle Polaris counterclockwise and never set " + c(2) + ".", "Polaris marks true north — no declination needed " + c(2) + ".", "South of the equator (or low on the southern horizon in the tropics) the Southern Cross points south: extend its long axis about five times its length and look straight down to the horizon " + c(2) + "."]))
    b.append(h2("moon", "4.4 The moon, and improvised compasses"))
    b.append(ul(["If the moon rises before sunset, its lit side faces west; if it rises after midnight, the lit side faces east " + c(2) + ".", "<b>Needle compass:</b> stroke a needle or razor blade in one direction only with silk, through your hair, or with a magnet; hang it from a thread or float it on a leaf or wood chip in still water. It lines up north–south " + c(2) + ". Check which end is north using the sun.", "Moss on the north side is <b>not</b> reliable — it can grow all round a tree " + c(2) + "."]))

    b.append(part("p5", "Part 5", "Traveling on Foot and by Bike"))
    b.append(h2("route", "5.1 Planning a route"))
    b.append(ul(["Study contour lines: follow ridges and valleys with gentle, evenly spaced contours; avoid tightly packed ones (cliffs) " + c(1) + ".", "Choose handrails and attack points before you start; write the azimuth and pace count for each leg " + c(1) + ".", "Plan water sources, shelter stops and bail-out routes. Travel in daylight when possible.", "Tell someone your route and return time; leave a note at home with the date and direction you went."]))
    b.append(h2("bike", "5.2 Bicycles"))
    b.append(ul(["A bicycle carries far more than a backpack and covers much more ground on roads and trails, with no fuel.", "Carry a pump, spare tubes and patch kit, tire levers, multi-tool, chain lube and a spare chain link.", "Load weight low on racks or panniers, not on your back. Walk the bike across fords, steep descents and debris.", "Roads are the best bike handrails; plan around closed bridges and choke points using your map (1.1)."]))
    b.append(h2("bag", "5.3 The go-bag"))
    b.append('<p>FEMA\'s basic kit list, adapted for carrying ' + c(5) + ':</p>')
    b.append(check("Ready.gov basic kit " + c(5), ["Water — one gallon per person per day for several days (carry less, plus a filter and purification tablets)", "Several days of non-perishable food; manual can opener", "Battery or hand-crank radio and NOAA Weather Radio; flashlight; extra batteries", "First aid kit; prescription medicines and glasses", "Whistle to signal for help; dust mask", "Plastic sheeting and duct tape; moist towelettes, garbage bags and ties", "Wrench or pliers to turn off utilities", "<b>Local maps</b>; phone with chargers and backup battery", "Cash; copies of important documents in a waterproof container", "Sleeping bag or warm blanket; a complete change of clothing", "Matches in a waterproof container; hygiene supplies"]))
    b.append(tip("Add for walking out", "A compass, your pace-count beads, sturdy broken-in shoes " + c(5) + ", rain gear, a hat, a knife, cordage, and a written list of meeting places and radio channels."))

    b.append(part("p6", "Part 6", "Crossing Water Safely"))
    b.append(h2("river", "6.1 Choosing a crossing"))
    b.append('<p>Look from high ground (or climb a tree) before you cross ' + c(2) + '.</p>')
    b.append(table(["Good places " + c(2), "Avoid " + c(2)], [["Where the river splits into several narrow channels", "Ledges of rock across the river (rapids, canyons)"], ["Upstream of a shallow bank or sandbar, so the current carries you to it", "Just above waterfalls or deep channels"], ["A line angled downstream, crossing the current at about 45°", "Slick rocky beds; eddies that pull you under"], ["Deep, slow water can be safer than fast shallow water", "Estuaries — wide, strong, tidal currents"]]))
    b.append(danger("Very cold water", "Do not swim or wade across a river when the water is very cold — it can be fatal. Build a raft, or wade only if just your feet get wet and dry them vigorously on the far bank " + c(2) + "."))
    b.append(h2("ford", "6.2 Fording: alone and in a group"))
    b.append(fig(d_ford(), "Pole and group methods from FM 21-76 Chapter 17 " + c(2) + "."))
    b.append(ul(["Keep footwear on for grip and to protect your feet " + c(2) + ". Bundle gear on top of your pack and make sure you can <b>slip the pack off instantly</b> — a stuck pack can drown a strong swimmer " + c(2) + ".", "<b>Alone:</b> use a strong pole, about 7.5 cm thick and 2.1–2.4 m long, planted on your upstream side; move the pole, then step below it, keeping it slanted so the current presses it against you " + c(2) + ".", "<b>Group:</b> hold one pole parallel to the current with the heaviest person downstream and the lightest upstream; the upstream person breaks the current " + c(2) + ".", "<b>Rope:</b> with three or more people and a rope three times the river's width, cross one at a time tied in and controlled by the others " + c(2) + ".", "<b>If swept away:</b> in shallow rapids, float on your back, feet downstream and up; in deep rapids, swim on your stomach angling toward shore. Never fight the current " + c(2) + "."]))
    b.append(h2("bog", "6.3 Floodwater, bogs and quicksand"))
    b.append(danger("Turn around, don't drown", "Just <b>6 inches of fast-moving floodwater can knock over an adult</b>; 12 inches carries away most cars and 2 feet carries away SUVs and trucks " + c(6) + ". Never walk, bike or drive into moving floodwater."))
    b.append(ul(["Do not try to walk upright across bogs, muskeg or quicksand — lifting your feet makes you sink. Go around, or bridge with logs and branches " + c(2) + ".", "If you must cross, lie face down with arms and legs spread and move slowly, pulling yourself along " + c(2) + ".", "Test suspicious sand with a stone: it sinks in quicksand " + c(2) + ".", "In swamps, vegetated areas are usually firmer than open mud " + c(2) + "."]))

    b.append(part("p7", "Part 7", "Travel Hazards Region by Region"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Value"], [["Back azimuth", "±180° " + c(1)], ["Declination", "East: subtract map→ground; West: add " + c(1, 3)], ["Offset", "≈18 m per degree per 1,000 m " + c(1)], ["Pace", "≈30 in; count per 100 m " + c(1)], ["Shadow stick", "First mark = west " + c(2)], ["Polaris", "≈5× the Dipper's pointer gap " + c(2)], ["Fording pole", "≈7.5 cm × 2.1–2.4 m " + c(2)], ["Crossing angle", "≈45° downstream " + c(2)], ["Floodwater", "6 in knocks you down; 12 in floats a car " + c(6)], ["Avalanche slopes", "30°–50° " + c(7)]]))
    b.append('<p class="small">General information for emergencies. Declination computed November 2026. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Navigation & Travel", "Survival Info<br>Navigation &amp;<br>Travel",
          "Map and compass, declination for every region, pace counting, finding direction by sun and stars, routes on foot and by bike, the go-bag, and crossing rivers safely — with travel hazards across North America.",
          "Navigation & Travel", TOC, cover_art(), "Radio · Defense · Water · Medical · Fire · Hunting · Bunkers")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Navigation.pdf")
