import sys, math; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#37474f"/>'
    s += '<path d="M0 300 Q180 270 360 300 T720 300 V380 H0z" fill="#33691e"/>'
    s += '<ellipse cx="250" cy="120" rx="170" ry="60" fill="#90a4ae"/><ellipse cx="380" cy="100" rx="150" ry="70" fill="#b0bec5"/><ellipse cx="500" cy="130" rx="140" ry="55" fill="#78909c"/>'
    s += '<polygon points="400,160 370,230 395,230 360,300 430,210 402,210 430,160" fill="#ffeb3b"/>'
    for i in range(14): s += f'<line x1="{150+i*30}" y1="{180 + (i%3)*10}" x2="{140+i*30}" y2="{215 + (i%3)*10}" stroke="#bbdefb" stroke-width="3"/>'
    s += '<path d="M600 300 q-20 -60 10 -120 q25 60 -10 120z" fill="#eceff1" opacity=".7"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Reading the Sky", [("clouds","1.1 The ten basic clouds"),("seq","1.2 Cloud sequences that mean rain or snow"),("storm","1.3 Thunderstorm clouds and lightning distance")]),
 ("p2", "Part 2 · Air Pressure and a Homemade Barometer", [("baro","2.1 Build a can or jar barometer"),("read","2.2 Keeping a weather log")]),
 ("p3", "Part 3 · Storms: Thunder, Tornado, Hurricane", [("light","3.1 Lightning"),("torn","3.2 Tornadoes"),("hurr","3.3 Hurricanes and storm surge")]),
 ("p4", "Part 4 · Water and Fire", [("flood","4.1 Floods and flash floods"),("wild","4.2 Wildfire")]),
 ("p5", "Part 5 · Shaking Ground and the Sea", [("quake","5.1 Earthquakes: Drop, Cover, Hold On"),("tsu","5.2 Tsunamis")]),
 ("p6", "Part 6 · Cold and Heat", [("cold","6.1 Blizzards, wind chill, frostbite and hypothermia"),("heat","6.2 Extreme heat")]),
 ("p7", "Part 7 · Hazards Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_clouds():
    s = t(360, 26, "The ten basic clouds by height", 19, "middle", "700")
    bands = [("HIGH (ice crystals)", 50, "#e3f2fd"), ("MIDDLE", 170, "#eceff1"), ("LOW", 290, "#f5f5f5")]
    for lab, y, col in bands: s += rect(10, y, 700, 115 if y < 290 else 145, col, "#b0bec5", 1, 4) + t(20, y + 20, lab, 14, "start", "700", "#455a64")
    def puff(x, y, r, col="#fff"): return "".join(f'<circle cx="{x+dx}" cy="{y+dy}" r="{r*k}" fill="{col}" stroke="#90a4ae" stroke-width="1.5"/>' for dx, dy, k in [(-r, 4, .7), (0, -4, 1), (r, 4, .75)])
    # high
    s += "".join(f'<path d="M{60+i*30} {110-i*3} q30 -20 70 -10" fill="none" stroke="#78909c" stroke-width="2"/>' for i in range(3)) + t(110, 150, "Cirrus: wispy hair", 13, "middle", "600")
    s += "".join(f'<circle cx="{290+(i%6)*14}" cy="{90+(i//6)*12}" r="5" fill="#fff" stroke="#90a4ae"/>' for i in range(18)) + t(325, 150, "Cirrocumulus: tiny ripples", 13, "middle", "600")
    s += rect(470, 80, 220, 30, "#fff", "#cfd8dc", 1, 10) + '<circle cx="580" cy="95" r="22" fill="none" stroke="#ffb300" stroke-width="2"/><circle cx="580" cy="95" r="7" fill="#ffca28"/>' + t(580, 150, "Cirrostratus: veil, HALO", 13, "middle", "600")
    # mid
    s += "".join(puff(70 + (i%3)*45, 210 + (i//3)*28, 11) for i in range(6)) + t(115, 275, "Altocumulus: patches", 13, "middle", "600")
    s += rect(260, 200, 170, 45, "#b0bec5", "none", 0, 8) + '<circle cx="345" cy="222" r="9" fill="#eceff1" opacity=".8"/>' + t(345, 275, "Altostratus: gray sheet,", 13, "middle", "600") + t(345, 289, "sun as through frosted glass", 12, "middle")
    s += rect(480, 195, 210, 50, "#607d8b", "none", 0, 8) + "".join(line(500+i*20, 247, 494+i*20, 280, "#1e88e5", 2) for i in range(10)) + t(585, 296, "Nimbostratus: steady rain/snow", 13, "middle", "600")
    # low
    s += puff(110, 340, 26) + t(110, 395, "Cumulus: fair-weather puffs", 13, "middle", "600")
    s += '<g transform="translate(0,28)"><path d="M240 400 L250 330 Q260 300 290 300 Q300 270 330 285 Q360 260 380 300 L380 330 L390 400z" fill="#eceff1" stroke="#78909c" stroke-width="2"/><path d="M210 312 L410 312 L380 298 L240 298z" fill="#cfd8dc" stroke="#78909c"/></g>' + t(470, 330, "Cumulonimbus:", 13, "start", "700") + t(470, 346, "thunder, hail, tornadoes;", 13, "start") + t(470, 362, "flat anvil top", 13, "start")
    s += rect(470, 372, 220, 14, "#9e9e9e", "none", 0, 3) + t(580, 400, "Stratus / stratocumulus: low gray", 12, "middle", "600")
    return svg(720, 445, s)

def d_seq():
    s = t(360, 26, "Thickening, lowering cloud = steady rain or snow on the way", 18, "middle", "700")
    names = [("Cirrus", "#e3f2fd", 70), ("Cirrostratus", "#cfd8dc", 100), ("Altostratus", "#b0bec5", 150), ("Nimbostratus", "#607d8b", 200)]
    for i, (n, col, h) in enumerate(names):
        x = 30 + i*175
        s += rect(x, 270 - h, 150, h - 40, col, "#90a4ae", 1, 10) + t(x + 75, 290, n, 15, "middle", "700")
        if i < 3: s += arrow(x + 152, 200, x + 172, 200)
    s += '<circle cx="280" cy="210" r="22" fill="none" stroke="#ffb300" stroke-width="3"/>' + t(280, 250, "halo around sun/moon", 12, "middle")
    for i in range(8): s += line(570 + i*14, 232, 564 + i*14, 262, "#1e88e5", 2)
    s += t(360, 320, "Hours to a day or more:  cloud gets thicker → lower → darker → rain", 14, "middle", "600")
    return svg(720, 335, s)

def d_flash():
    s = t(360, 26, "Flash-to-bang: count seconds from lightning to thunder", 18, "middle", "700")
    s += '<polygon points="70,50 40,140 65,140 30,230 110,120 82,120 110,50" fill="#fdd835" stroke="#f57f17" stroke-width="2"/>'
    s += line(130, 200, 690, 200, "#455a64", 3)
    for k in range(0, 31, 5):
        x = 130 + k*18.5
        s += line(x, 192, x, 208, "#455a64", 2) + t(x, 228, f"{k} s", 13, "middle", "700") + t(x, 246, f"{k/5:.0f} mi", 13, "middle")
    s += rect(130, 160, 185, 26, "#ffcdd2", "none", 0, 4) + t(222, 178, "TAKE SHELTER NOW", 13, "middle", "800", "#b71c1c")
    s += t(410, 90, "Seconds ÷ 5 = miles  (÷ 3 = km)", 17, "start", "700") + t(410, 115, "Thunder carries only about 10 miles:", 14, "start") + t(410, 135, "if you hear it, you can be struck.", 14, "start", "700")
    return svg(720, 265, s)

def d_baro():
    s = t(360, 26, "Can or jar barometer (aneroid type)", 19, "middle", "700")
    s += rect(150, 130, 160, 200, "#cfd8dc", "#455a64", 4, 6) + t(230, 240, "glass jar or", 14, "middle") + t(230, 258, "tin can", 14, "middle")
    s += '<path d="M146 130 q84 -16 168 0" fill="#ef9a9a" stroke="#c62828" stroke-width="3"/>' + rect(144, 132, 172, 8, "#5d4037", "none", 0, 2)
    s += line(230, 122, 470, 104, "#fb8c00", 5) + t(120, 100, "balloon or plastic wrap,", 13, "end") + t(120, 116, "stretched tight, airtight", 13, "end") + arrow(124, 106, 180, 124)
    s += t(330, 90, "straw taped at the center", 13, "start", "600")
    s += rect(480, 50, 26, 120, "#fff8e1", "#8d6e63", 2, 2)
    for i, (lab, y) in enumerate([("HIGH", 64), ("", 84), ("start", 104), ("", 124), ("LOW", 150)]):
        s += line(480, y, 496, y, "#5d4037", 2) + t(514, y + 5, lab, 13, "start", "700")
    s += t(560, 200, "card on the wall", 13, "middle")
    s += rect(40, 350, 640, 70, "#e8f5e9", "#81c784", 1, 6)
    s += t(360, 375, "Pressure UP → wrap pushed down → straw tip RISES (usually fair)", 14, "middle", "700")
    s += t(360, 400, "Pressure DOWN → wrap bulges → straw tip FALLS (clouds, rain, storms)", 14, "middle", "700", "#b71c1c")
    return svg(720, 430, s)

def d_tornado():
    s = t(360, 26, "Where to shelter from a tornado", 19, "middle", "700")
    s += '<polygon points="40,140 250,60 460,140" fill="#a1887f" stroke="#4e342e" stroke-width="3"/>'
    s += rect(60, 140, 380, 120, "#fff8e1", "#4e342e", 3, 0) + rect(60, 260, 380, 80, "#d7ccc8", "#4e342e", 3, 0)
    s += rect(80, 160, 60, 40, "#bbdefb", "#455a64", 2, 0) + rect(360, 160, 60, 40, "#bbdefb", "#455a64", 2, 0) + t(110, 220, "windows ✗", 12, "middle", "700", "#c62828") + t(390, 220, "windows ✗", 12, "middle", "700", "#c62828")
    s += rect(210, 170, 80, 80, "#c8e6c9", "#2e7d32", 3, 0) + t(250, 205, "small", 12, "middle", "700") + t(250, 220, "interior", 12, "middle", "700") + t(250, 235, "room", 12, "middle", "700")
    s += rect(190, 275, 120, 55, "#a5d6a7", "#2e7d32", 3, 0) + t(250, 300, "BASEMENT", 13, "middle", "800") + t(250, 316, "lowest level", 12, "middle")
    s += t(480, 160, "1st choice: storm cellar,", 14, "start", "700") + t(480, 180, "safe room or basement", 14, "start", "700") + t(480, 215, "2nd: small windowless", 14, "start") + t(480, 235, "interior room on the", 14, "start") + t(480, 255, "lowest floor", 14, "start")
    s += t(480, 290, "Stay away from windows", 14, "start", "700", "#c62828")
    s += t(360, 370, "Cover head and neck; pull mattresses, blankets or furniture over you.", 14, "middle", "600")
    s += t(360, 392, "A car is NOT a safe shelter. Never hide under a bridge or overpass.", 14, "middle", "700", "#c62828")
    return svg(720, 405, s)

def d_season():
    s = t(360, 26, "When each hazard peaks (typical, North America)", 19, "middle", "700")
    months = "J F M A M J J A S O N D".split()
    x0, w = 200, 34
    for i, m in enumerate(months): s += t(x0 + i*w + w/2, 56, m, 14, "middle", "700")
    rows = [("Atlantic hurricanes", [(5, 10)], "#e53935", "Jun 1 – Nov 30"), ("E. Pacific hurricanes", [(4.5, 10)], "#fb8c00", "May 15 – Nov 30"),
            ("Tornadoes (peak)", [(2, 6)], "#8e24aa", "any month"), ("Blizzards", [(10, 11), (0, 3)], "#1e88e5", "late fall–spring"),
            ("Extreme heat", [(5, 8)], "#f4511e", "summer"), ("Wildfire (West)", [(5, 9)], "#6d4c41", "any dry spell"),
            ("Earthquakes / tsunamis", [(0, 11)], "#546e7a", "NO season")]
    for k, (lab, spans, col, note) in enumerate(rows):
        y = 70 + k*42
        s += t(190, y + 22, lab, 14, "end", "600")
        s += rect(x0, y + 6, 12*w, 26, "#f5f5f5", "#e0e0e0", 1, 3)
        for a, b in spans: s += rect(x0 + a*w, y + 6, (b - a + 1)*w if b >= a else w, 26, col, "none", 0, 3)
        s += t(x0 + 12*w + 8, y + 24, note, 12, "start", "700")
    s += t(360, 70 + len(rows)*42 + 20, "Hurricane dates: NOAA NHC. Other bars show typical peaks only; tornadoes can strike in any month.", 12, "middle")
    return svg(720, 70 + len(rows)*42 + 32, s)

def d_quake():
    s = t(360, 26, "Earthquake: DROP · COVER · HOLD ON", 19, "middle", "700")
    for i, (lab, sub) in enumerate([("DROP", "onto hands and knees"), ("COVER", "head and neck; get under a sturdy table"), ("HOLD ON", "until the shaking stops")]):
        x = 40 + i*230
        s += rect(x, 50, 200, 190, "#fff3e0", "#ef6c00", 2, 10) + t(x + 100, 220, lab, 18, "middle", "800", "#e65100")
        if i == 0: s += '<circle cx="140" cy="110" r="16" fill="#ffcc80" stroke="#37474f" stroke-width="2"/>' + '<path d="M95 175 L120 125 L170 125 L185 175" fill="none" stroke="#37474f" stroke-width="6"/>'
        if i == 1: s += rect(x + 20, 95, 160, 14, "#8d6e63", "#4e342e", 2, 2) + line(x + 30, 109, x + 30, 190, "#4e342e", 5) + line(x + 170, 109, x + 170, 190, "#4e342e", 5) + f'<circle cx="{x+100}" cy="150" r="15" fill="#ffcc80" stroke="#37474f" stroke-width="2"/>' + line(x + 80, 140, x + 120, 140, "#37474f", 5)
        if i == 2: s += rect(x + 20, 95, 160, 14, "#8d6e63", "#4e342e", 2, 2) + line(x + 30, 109, x + 30, 190, "#4e342e", 5) + line(x + 170, 109, x + 170, 190, "#4e342e", 5) + f'<circle cx="{x+90}" cy="150" r="15" fill="#ffcc80" stroke="#37474f" stroke-width="2"/>' + line(x + 100, 140, x + 165, 115, "#37474f", 5)
        s += t(x + 100, 262, sub if len(sub) < 30 else sub[:22], 12, "middle")
        if len(sub) >= 30: s += t(x + 100, 278, sub[22:].strip(), 12, "middle")
    s += t(360, 305, "Do NOT run outside and do not stand in doorways. Outside? Get away from buildings, trees and wires.", 13, "middle", "700", "#c62828")
    return svg(720, 320, s)

def windchill(T, V): return 35.74 + 0.6215*T - 35.75*V**0.16 + 0.4275*T*V**0.16

def d_windchill():
    temps = [30, 20, 10, 0, -10, -20, -30]; winds = [5, 10, 20, 30, 40]
    s = t(360, 26, "Wind chill (°F) — how cold it feels on bare skin", 19, "middle", "700")
    s += t(100, 62, "Wind mph ↓  Air °F →", 13, "middle", "700")
    for j, T in enumerate(temps): s += t(220 + j*72, 62, f"{T}°", 15, "middle", "700")
    for i, V in enumerate(winds):
        y = 74 + i*40
        s += t(100, y + 26, f"{V}", 15, "middle", "700")
        for j, T in enumerate(temps):
            w = windchill(T, V); col = "#e3f2fd" if w > -18 else ("#90caf9" if w > -32 else ("#42a5f5" if w > -45 else "#1565c0"))
            s += rect(186 + j*72, y, 68, 36, col, "#fff", 1, 3) + t(220 + j*72, y + 24, f"{w:.0f}", 15, "middle", "700", "#fff" if w <= -45 else INK)
    y = 74 + len(winds)*40 + 18
    s += t(360, y, "Computed with the NWS wind chill formula. Darker = frostbite comes faster (NWS chart shades 30, 10 and 5 minutes).", 12, "middle")
    return svg(720, y + 12, s)

R = {
 1: "Extreme cold and blizzards dominate: watch the wind chill and the signs of frostbite and hypothermia " + c(14, 15) + ". Southern Alaska is earthquake and tsunami country — strong shaking near the coast means go to high ground at once " + c(12, 13) + ".",
 2: "Earthquakes and tsunamis on the Cascadia coast and in BC: practise Drop, Cover, Hold On and know the way to ground 100 ft up or a mile inland " + c(12, 13) + ". Long winter rains bring floods and landslides " + c(9) + "; summer wildfire smoke " + c(11) + ".",
 3: "Tornado Alley: spring and early-summer supercells " + c(6) + ". Large hail, blizzards with near-zero visibility, and flash floods in creek beds " + c(9, 14) + ". Watch for towering cumulonimbus building in the west in the afternoon " + c(3) + ".",
 4: "Tornadoes, severe thunderstorms and river flooding in spring; lake-effect snow and bitter wind chill in winter " + c(6, 9, 15) + ".",
 5: "Nor'easters and blizzards, coastal flooding, and late-season hurricanes reaching New England and Atlantic Canada (Atlantic season June 1 – November 30) " + c(7, 8, 14) + ".",
 6: "Hurricanes and storm surge on the Gulf and Atlantic coasts — storm surge is historically the leading cause of US hurricane deaths " + c(7) + ". Tornadoes in spring and with landfalling hurricanes " + c(6, 7) + ". Summer heat and humidity " + c(16) + ".",
 7: "Hurricane exposure on every coast, June through November " + c(7, 8) + "; daily summer lightning storms — when thunder roars, go indoors " + c(4, 5) + ". Low ground floods fast " + c(9) + ".",
 8: "Extreme heat: heat stroke means body temperature above 103 °F and hot, dry skin " + c(16) + ". Summer monsoon storms send flash floods down dry washes " + c(9, 10) + ". Wildfire and dust storms " + c(11) + ".",
 9: "Afternoon mountain thunderstorms — get off peaks and ridges early " + c(4, 5) + "; blizzards and avalanches in winter " + c(14) + "; wildfire in dry summers " + c(11) + ".",
 10: "Earthquakes anywhere in the state " + c(12) + "; tsunamis on the coast " + c(13) + "; wildfire season with dry offshore winds " + c(11) + "; winter storms bring flooding and mudslides " + c(9) + ".",
 11: "Heat, drought and summer monsoon flash floods inland " + c(9, 16) + "; eastern Pacific hurricanes (May 15 – November 30) strike Baja California and the Pacific coast " + c(7, 8) + ".",
 12: "Strong earthquakes along the Pacific coast and in central Mexico " + c(12) + "; tsunamis on the Pacific coast " + c(13) + "; hurricanes from both the Pacific and the Gulf " + c(8) + ". Rainy-season floods and landslides " + c(9) + ".",
 13: "Hurricanes from June to November (Caribbean is part of the Atlantic basin) " + c(8) + "; earthquakes and tsunamis along the Pacific and Caribbean margins " + c(12, 13) + "; tropical downpours cause flash floods " + c(9) + ".",
}

def body():
    b = []
    b.append(part("p1", "Part 1", "Reading the Sky"))
    b.append('<p>With no forecasts, sirens or weather radio, <b>your own eyes and a homemade barometer are the warning system</b>. This guide shows how to read clouds and pressure, then what to do in each disaster North America faces. Everything here can be done by ordinary people with household materials.</p>')
    b.append(h2("clouds", "1.1 The ten basic clouds"))
    b.append(fig(d_clouds(), "The ten basic cloud types, grouped by height, as defined in the WMO International Cloud Atlas " + c(3) + "."))
    b.append(table(["Cloud", "Looks like", "What it tells you"], [
        ["Cirrus", "White, delicate filaments; always ice crystals", "Fair now; watch whether it thickens " + c(3)],
        ["Cirrostratus", "Thin milky veil; makes a <b>halo</b> around sun or moon", "Thickening high cloud; often the first sign of a wet spell " + c(3)],
        ["Altostratus", "Gray sheet; sun looks as if through frosted glass; no halo", "May drop light rain or virga " + c(3)],
        ["Nimbostratus", "Dark gray layer formed from thickening altostratus; blots out the sun", "Steady rain or snow; base lowers as it continues " + c(3)],
        ["Cumulus", "Puffy, flat dark base, cauliflower top", "Form in the morning on clear days and fade by evening " + c(3)],
        ["Cumulonimbus", "Huge tower, often an anvil top", "Thunder, lightning, heavy rain, <b>hail and tornadoes</b> " + c(3)],
        ["Stratus", "Uniform gray layer", "Drizzle or snow grains; blue sky when it breaks up " + c(3)]]))
    b.append(h2("seq", "1.2 Cloud sequences that mean rain or snow"))
    b.append(fig(d_seq(), "Nimbostratus forms from thickening altostratus; a halo comes from cirrostratus " + c(3) + "."))
    b.append(ul(["<b>Watch the trend, not one look.</b> High wisps that spread into a veil, then lower to a gray sheet that hides the sun, are the classic run-up to steady precipitation " + c(3) + ".",
                 "<b>Cumulus that keep growing taller</b> by early afternoon can become cumulonimbus — the cloud that makes hail and tornadoes " + c(3) + ".",
                 "Combine sky signs with your barometer (Part 2): <b>falling pressure plus thickening cloud</b> is a much stronger warning than either alone " + c(1, 17) + "."]))
    b.append(h2("storm", "1.3 Thunderstorm clouds and lightning distance"))
    b.append(fig(d_flash(), "Sound travels about a mile in 5 seconds; thunder is heard only about 10 miles away " + c(4) + "."))
    b.append(danger("If you can hear thunder, you are in range", "Thunder can be heard only about 10 miles from the strike, so hearing it means you are within striking distance and should get to a safe place immediately " + c(4) + ". Count from flash to thunder and divide by 5 for miles — but do your counting from shelter " + c(4) + "."))

    b.append(part("p2", "Part 2", "Air Pressure and a Homemade Barometer"))
    b.append('<p>Low pressure usually means stormy weather and high pressure usually means clear weather ' + c(17) + '. A barometer that only shows <b>whether pressure is rising or falling</b> is enough to forecast a day ahead.</p>')
    b.append(h2("baro", "2.1 Build a can or jar barometer"))
    b.append(fig(d_baro(), "The NOAA and South Carolina climate-office designs " + c(1, 2) + "."))
    b.append(steps(["Cover the top of a small metal can or glass jar with plastic wrap or a balloon with the narrow end cut off. Pull it <b>tight and airtight</b> and hold it with a rubber band " + c(1, 2) + ".",
                    "Lay a drinking straw flat with one end at the center of the cover and tape it down; the rest sticks out past the rim as a pointer " + c(1) + ".",
                    "Stand a card behind the straw (tape it to the can or to a wall) and mark where the tip points " + c(1, 2) + ".",
                    "Keep it out of the sun and away from heaters, in a spot where it won't be bumped " + c(17) + ".",
                    "Read it at the same time each day; mark the highest reading HIGH and the lowest LOW over the first week " + c(1, 2) + "."]))
    b.append(caution("It shows change, not numbers", "A homemade barometer shows relative changes only — it cannot match official readings " + c(17) + ". Temperature also affects the air in the jar, which is why it must stay out of direct sun and away from the stove."))
    b.append(h2("read", "2.2 Keeping a weather log"))
    b.append(table(["Barometer", "Sky", "Likely next 12–24 h"], [
        ["Rising", "Clearing, cumulus fading at evening", "Fair, calmer " + c(3, 17)],
        ["Steady", "No change", "More of the same"],
        ["Falling slowly", "High veil, halo, then gray sheet", "Steady rain or snow coming " + c(3, 17)],
        ["Falling fast", "Towering cumulus / dark masses", "Storms, strong wind — prepare now " + c(3, 17)]]))
    b.append(tip("Log it", "Each morning and evening write: date, time, straw position, sky, wind direction, and what weather followed. After a few weeks your own log becomes the best local forecast tool you have " + c(1, 17) + "."))

    b.append(part("p3", "Part 3", "Storms: Thunder, Tornado, Hurricane"))
    b.append(h2("light", "3.1 Lightning"))
    b.append(ul(["<b>When thunder roars, go indoors</b>: get into a building or a hard-roofed car " + c(5) + ".",
                 "Indoors, stay off anything wired to an outlet and avoid running water (plumbing conducts lightning) " + c(5) + ".",
                 "Trim or remove trees that could fall on your home " + c(5) + ".",
                 "Thunderstorms also bring flash floods, hail and damaging winds " + c(5) + "."]))
    b.append(h2("torn", "3.2 Tornadoes"))
    b.append(fig(d_tornado(), "Shelter choices from Ready.gov " + c(6) + "."))
    b.append(ul(["Best: a safe room or storm shelter. Next best: a <b>small, interior, windowless room or basement on the lowest level</b> of a sturdy building " + c(6) + ".",
                 "Cover your head and neck with your arms and put furniture and blankets around or on top of you " + c(6) + ".",
                 "In a car there is no safe option, only less dangerous ones: if the tornado is far away and visible, drive at right angles to its path; if caught, stay belted with your head below the windows, or lie in ground clearly lower than the road " + c(6) + ".",
                 "<b>Never shelter under a bridge or overpass</b> — little protection from debris " + c(6) + ".",
                 "Afterwards: stay clear of downed lines; wear thick-soled shoes, long pants and work gloves for clean-up " + c(6) + "."]))
    b.append(tip("Build a shelter now", "With no warning sirens, a dug-in storm cellar or a reinforced interior room is the single best tornado investment. See the Bunkers and Concrete guides for building methods."))
    b.append(h2("hurr", "3.3 Hurricanes and storm surge"))
    b.append(fig(d_season(), "Hurricane seasons from the National Hurricane Center " + c(8) + "; other peaks are typical patterns."))
    b.append(ul(["Atlantic season (including the Gulf and Caribbean): <b>June 1 – November 30</b>. Eastern Pacific: <b>May 15 – November 30</b> " + c(7, 8) + ".",
                 "<b>Storm surge</b> has historically been the leading cause of hurricane deaths in the US " + c(7) + ". If you live on low coastal ground, plan your route to high ground well before the season.",
                 "Hurricanes also bring flooding rain, wind, rip currents and tornadoes far inland " + c(7) + ".",
                 "Before the storm: clear drains and gutters, bring in loose outdoor items, and shutter windows (plywood works) " + c(7) + "."]))

    b.append(part("p4", "Part 4", "Water and Fire"))
    b.append(h2("flood", "4.1 Floods and flash floods"))
    b.append(danger("Turn around, don't drown", "Just <b>six inches of moving water can knock you down</b>, and one foot of moving water can sweep a vehicle away. Stay off bridges over fast-moving water " + c(9, 10) + "."))
    b.append(ul(["Floods are the most common disaster in the United States; flash floods can come without warning " + c(9) + ".",
                 "Move to higher ground or a higher floor " + c(9) + ". Where it rains, it can flood — flooding does not follow lines on a map " + c(9) + ".",
                 "In canyons and dry washes, a storm you cannot see upstream can send a wall of water — camp and shelter well above the channel " + c(9, 10) + "."]))
    b.append(h2("wild", "4.2 Wildfire"))
    b.append(ul(["Make a <b>fire-resistant zone at least 30 feet</b> around your home, free of leaves, debris and flammable material " + c(11) + ".",
                 "Have an outdoor water source with a hose that reaches every part of the property " + c(11) + ".",
                 "Pick one room you can seal from outside air for smoky days; close all doors and windows " + c(11) + ".",
                 "Know two ways out and leave early — wildfires spread quickly " + c(11) + "."]))
    b.append(tip("Signs of fire weather", "Hot, dry, windy days after a dry spell are the dangerous ones. Smoke columns, ash fall and an orange sky upwind mean prepare to leave."))

    b.append(part("p5", "Part 5", "Shaking Ground and the Sea"))
    b.append(h2("quake", "5.1 Earthquakes: Drop, Cover, Hold On"))
    b.append(fig(d_quake(), "Drop, Cover, Hold On, as taught by Ready.gov and the Earthquake Country Alliance " + c(12) + "."))
    b.append(ul(["Indoors: stay inside — do not run outside, and avoid doorways " + c(12) + ". In bed: lie face down and cover head and neck with a pillow " + c(12) + ".",
                 "No table nearby: crawl next to an interior wall away from windows, stay on your knees and bend over " + c(12) + ".",
                 "In a car: pull over, stop and set the parking brake. Outside: move to open ground away from buildings, trees, streetlights and power lines " + c(12) + ".",
                 "Prepare now: secure bookcases, water heaters and heavy items to the wall; keep heavy and breakable things on low shelves " + c(12) + "."]))
    b.append(h2("tsu", "5.2 Tsunamis"))
    b.append(danger("Natural warning = leave now", "A strong coastal earthquake, a loud roar from the ocean, or the sea suddenly <b>rising or draining to show the sea floor</b> are tsunami signs. Do not wait — go to high ground as far inland as possible " + c(13) + "."))
    b.append(ul(["Pick refuges <b>100 feet or more above sea level, or at least one mile inland</b> " + c(13) + ".",
                 "Tsunami waves can be 10–100 feet high and come in a series — the first wave is often not the largest, so stay away until the sea has been calm a long time " + c(13) + ".",
                 "If you are in a boat, go out to sea " + c(13) + "."]))

    b.append(part("p6", "Part 6", "Cold and Heat"))
    b.append(h2("cold", "6.1 Blizzards, wind chill, frostbite and hypothermia"))
    b.append(fig(d_windchill(), "Values computed from the NWS wind chill formula " + c(15) + "."))
    b.append(table(["Condition", "Signs", "What to do"], [
        ["Frostbite", "Numbness; white or grayish-yellow skin; firm or waxy skin", "Get to a warm room; soak in warm water or warm with body heat. <b>Do not massage</b> or use a heating pad " + c(14)],
        ["Hypothermia", "Shivering, exhaustion, confusion, fumbling hands, memory loss, slurred speech, drowsiness; below 95 °F is an emergency", "Warm room; warm the <b>center of the body first</b> — chest, neck, head, groin; keep dry and wrapped in blankets including head and neck " + c(14)]]))
    b.append(ul(["Limit time outside, dress in layers, and avoid overexertion shoveling snow — winter storms raise the risk of heart attacks " + c(14) + ".",
                 "Insulate, caulk and weather-strip; keep pipes from freezing " + c(14) + ".",
                 "<b>Generators and fuel-burning heaters outdoors only</b>, at least 20 feet from windows, doors and attached garages; carbon monoxide is colorless and odorless " + c(14) + "."]))
    b.append(h2("heat", "6.2 Extreme heat"))
    b.append(table(["Illness", "Signs", "What to do"], [
        ["Heat cramps", "Muscle pains or spasms in stomach, arms or legs", "Cool place; sip water " + c(16)],
        ["Heat exhaustion", "Heavy sweating, paleness, cramps, weakness, fast or weak pulse, dizziness, headache, fainting, nausea, vomiting", "Cool place; remove extra clothing; sip water " + c(16)],
        ["<b>Heat stroke</b>", "Body temperature above 103 °F; red, hot, dry skin with no sweat; rapid strong pulse; confusion or unconsciousness", "<b>Life-threatening.</b> Move to shade, remove outer clothing, cold wet cloths on head, neck, armpits and groin or soak clothing with cool water; raise the feet " + c(16)]]))
    b.append(ul(["Extreme heat causes more deaths each year than any other weather hazard " + c(16) + ".",
                 "Fans give a false sense of comfort and do not lower body temperature in extreme heat " + c(16) + ". Shade windows with drapes, shades or reflectors " + c(16) + "."]))

    b.append(part("p7", "Part 7", "Hazards Region by Region"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Value"], [["Flash-to-bang", "seconds ÷ 5 = miles " + c(4)], ["Thunder audible", "≈10 miles " + c(4)], ["Floodwater", "6 in knocks you down; 1 ft sweeps a car " + c(9)], ["Tornado shelter", "basement / interior windowless room, lowest floor " + c(6)], ["Hurricane season", "Atlantic Jun 1–Nov 30; E. Pacific May 15–Nov 30 " + c(8)], ["Wildfire zone", "≥ 30 ft cleared " + c(11)], ["Tsunami refuge", "≥ 100 ft up or 1 mile inland " + c(13)], ["Generator", "outdoors, ≥ 20 ft from openings " + c(14)], ["Hypothermia", "below 95 °F = emergency " + c(14)], ["Heat stroke", "above 103 °F, hot dry skin " + c(16)]]))
    b.append('<p class="small">General information for emergencies. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Weather & Natural Disasters", "Survival Info<br>Weather &amp;<br>Disasters",
          "Reading clouds, a homemade barometer, lightning distance, and what to do in tornadoes, hurricanes, floods, wildfires, earthquakes, tsunamis, blizzards and heat waves — across North America.",
          "Weather & Disasters", TOC, cover_art(), "Navigation · Fire · Medical · Water · House · Bunkers · Radio")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Weather.pdf")
