import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#1a2433"/>'
    s += '<polygon points="360,60 560,180 560,330 160,330 160,180" fill="#37474f" stroke="#90a4ae" stroke-width="4"/>'
    s += rect(330, 230, 60, 100, "#5d4037", "#3e2723", 3, 2) + '<circle cx="378" cy="282" r="5" fill="#ffd54f"/>'
    s += rect(200, 210, 80, 60, "#ffe082", "#90a4ae", 3, 2) + rect(440, 210, 80, 60, "#ffe082", "#90a4ae", 3, 2)
    s += '<path d="M560 150 l40 -20" stroke="#cfd8dc" stroke-width="5"/><polygon points="600,120 640,100 660,170 600,150" fill="#fff59d" opacity=".35"/>'
    for i in range(14): s += line(20 + i*50, 330, 20 + i*50, 300, "#8d6e63", 6)
    s += line(0, 308, 720, 308, "#8d6e63", 4) + rect(0, 330, 720, 50, "#263238", "none", 0, 0)
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Awareness Comes First", [("base","1.1 Know what normal looks like"),("susp","1.2 What counts as suspicious"),("desc","1.3 Describing people and vehicles")]),
 ("p2", "Part 2 · Hardening the House", [("doors","2.1 Doors and door frames"),("windows","2.2 Windows and sliding doors"),("bars","2.3 Security bars — and getting out in a fire")]),
 ("p3", "Part 3 · Perimeter by Design", [("cpted","3.1 The CPTED principles"),("land","3.2 Landscaping, fences and sight lines")]),
 ("p4", "Part 4 · Lighting & Homemade Alarms", [("light","4.1 Lighting"),("alarm","4.2 Early-warning alarms you can build")]),
 ("p5", "Part 5 · Watch Schedules", [("sleep","5.1 Sleep is a security need"),("rota","5.2 Sample rotations"),("post","5.3 Standing a good watch")]),
 ("p6", "Part 6 · Organizing the Neighborhood", [("org","6.1 Structure: captains and coordinators"),("tree","6.2 Phone trees and radio nets"),("patrol","6.3 Patrols: watch and report, never confront"),("res","6.4 Pooling resources")]),
 ("p7", "Part 7 · OPSEC: Keeping Quiet About What You Have", [("five","7.1 The five-step OPSEC process"),("hide","7.2 Everyday OPSEC for a household")]),
 ("p8", "Part 8 · Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_door():
    s = t(360, 28, "Reinforcing the weakest point: the door frame", 19, "middle", "700")
    s += rect(80, 60, 200, 330, "#a1887f", "#5d4037", 4, 2) + t(180, 410, "solid wood or metal door", 15, "middle", "600")
    s += rect(280, 60, 40, 330, "#d7b98e", "#8a6d3b", 3, 0) + rect(320, 60, 60, 330, "#efebe9", "#9e9e9e", 2, 0)
    s += t(350, 50, "stud", 14, "middle", "600") + t(300, 50, "jamb", 14, "middle", "600")
    s += rect(240, 200, 70, 22, "#b0bec5", "#455a64", 2, 3) + t(170, 190, "deadbolt, hardened", 14, "middle", "700") + t(170, 208, "steel, 1-inch throw", 14, "middle")
    s += rect(284, 180, 16, 70, "#78909c", "#37474f", 2, 2)
    for y in (186, 200, 228, 242): s += line(292, y, 372, y, "#263238", 3)
    s += t(420, 190, "heavy 4- or 6-hole strike plate", 15, "start", "700") + t(420, 212, "screws at least 3 inches long,", 15, "start") + t(420, 232, "reaching into the stud", 15, "start")
    s += rect(280, 140, 10, 160, "#cfd8dc", "#78909c", 1, 1) + t(420, 290, "optional jamb brace (metal strip", 15, "start") + t(420, 310, "behind the trim) spreads the force", 15, "start")
    s += t(420, 120, "Most common break-in: a hard kick", 15, "start", "700", "#c62828") + t(420, 140, "that splits the wooden jamb", 15, "start", "700", "#c62828")
    return svg(720, 425, s)

def d_window():
    s = t(360, 28, "Pinning a double-hung window · stopping a sliding door", 19, "middle", "700")
    s += rect(60, 60, 240, 300, "#e3f2fd", "#455a64", 4, 2) + line(60, 210, 300, 210, "#455a64", 8)
    s += line(180, 200, 196, 222, "#c62828", 5) + '<circle cx="180" cy="200" r="5" fill="#c62828"/>'
    s += t(180, 390, "drill through the inner sash into (not", 14, "middle") + t(180, 408, "through) the outer one, angled down; drop in a nail", 14, "middle")
    s += rect(400, 80, 280, 260, "#e3f2fd", "#455a64", 4, 2) + line(540, 80, 540, 340, "#455a64", 4)
    s += line(410, 330, 530, 330, "#8d6e63", 10) + t(470, 360, "bar or dowel in the track", 14, "middle", "600")
    for x in (450, 540, 630): s += '<circle cx="%d" cy="88" r="5" fill="#263238"/>' % x
    s += t(540, 70, "screws in upper track stop lift-out", 14, "middle", "600")
    return svg(720, 420, s)

def d_cpted():
    s = t(360, 28, "CPTED around a house", 19, "middle", "700")
    s += rect(40, 50, 640, 340, "#e8f5e9", "#81c784", 2, 6)
    s += rect(260, 120, 200, 150, "#cfd8dc", "#455a64", 4, 4) + t(360, 200, "house", 16, "middle", "700")
    for x in (290, 400): s += rect(x, 120, 30, 10, "#ffe082", "#455a64", 1, 1)
    s += rect(345, 260, 30, 10, "#5d4037", "#3e2723", 1, 1)
    s += line(360, 270, 360, 390, "#bdbdbd", 22) + t(420, 370, "one clear, lit entrance path", 14, "start", "600")
    for x, y in ((120, 120), (600, 120), (120, 300), (600, 300)): s += f'<circle cx="{x}" cy="{y}" r="22" fill="#66bb6a"/>' + line(x, y+22, x, y+34, "#5d4037", 5)
    s += t(120, 170, "trees limbed up", 13, "middle") + t(120, 186, "7 ft", 13, "middle", "700")
    s += rect(240, 280, 90, 16, "#a5d6a7", "#2e7d32", 1, 6) + t(220, 320, "shrubs under 3 ft", 13, "end", "700")
    s += line(40, 50, 680, 50, "#8d6e63", 6) + line(40, 50, 40, 390, "#8d6e63", 6) + line(680, 50, 680, 390, "#8d6e63", 6)
    s += t(560, 80, "fence marks the line", 13, "middle", "600")
    s += '<polygon points="460,125 520,95 520,155" fill="#fff59d" opacity=".8"/>' + t(560, 230, "lights high, out of reach", 13, "middle", "600")
    s += t(360, 410, "See and be seen · guide people to one entrance · show it is cared for", 15, "middle", "700")
    return svg(720, 420, s)

def d_alarm():
    s = t(360, 28, "Simple noise alarms (warning only — never harm)", 19, "middle", "700")
    s += line(40, 260, 300, 260, "#c62828", 2, "6 4") + line(40, 200, 40, 280, "#5d4037", 8) + line(300, 160, 300, 280, "#5d4037", 8)
    s += line(300, 170, 320, 190, "#455a64", 2)
    for i in range(3): s += rect(310 + i*14, 190 + (i%2)*8, 14, 26, "#b0bec5", "#546e7a", 2, 3)
    s += t(170, 245, "light cord across a path, ankle high", 14, "middle", "600") + t(170, 300, "pulls a string of cans with pebbles", 14, "middle")
    s += rect(420, 160, 260, 120, "#eceff1", "#455a64", 2, 8) + t(550, 190, "Other quiet tripwires:", 15, "middle", "700")
    s += t(550, 215, "gravel paths that crunch", 14, "middle") + t(550, 238, "bells on gates and doors", 14, "middle") + t(550, 261, "battery door/motion chimes", 14, "middle")
    s += t(360, 330, "Mark them for your own people · keep them off roads and public paths", 15, "middle", "700", "#c62828")
    return svg(720, 345, s)

def d_rota():
    s = t(360, 28, "Night watch: 4 adults, 2-hour shifts, 10 PM – 6 AM", 19, "middle", "700")
    hrs = ["10 PM", "12 AM", "2 AM", "4 AM", "6 AM"]
    for i, h in enumerate(hrs): s += t(170 + i*125, 60, h, 14, "middle", "600")
    names = ["A", "B", "C", "D"]; cols = ["#90caf9", "#a5d6a7", "#ffcc80", "#ce93d8"]
    for r in range(4):
        y = 80 + r*55
        s += t(80, y+30, f"Adult {names[r]}", 15, "end", "700")
        s += rect(95, y, 500, 40, "#eceff1", "#cfd8dc", 1, 4)
        s += rect(170 + r*125, y, 125, 40, cols[r], "#37474f", 2, 4) + t(232 + r*125, y+26, "ON WATCH", 13, "middle", "700")
    s += t(360, 320, "Each adult stands one 2-hour watch and can still sleep about 7 hours", 15, "middle", "600")
    s += t(360, 345, "Rotate the order nightly so no one always gets the 2–4 AM shift", 15, "middle")
    return svg(720, 360, s)

def d_tree():
    s = t(360, 28, "Phone or radio tree (Neighborhood Watch model)", 19, "middle", "700")
    s += label_box(260, 50, 200, 50, ["Coordinator / base"], "#ffe082", 15)
    for i in range(3):
        x = 40 + i*240
        s += line(360, 100, x+80, 140, "#37474f", 2) + label_box(x, 140, 160, 50, [f"Block captain {i+1}"], "#bbdefb", 14)
        for j in range(3):
            xx = x - 10 + j*62
            s += line(x+80, 190, xx+25, 230, "#37474f", 1) + rect(xx, 230, 50, 36, "#e8f5e9", "#43a047", 2, 4) + t(xx+25, 253, "home", 12, "middle")
    s += t(360, 300, "Each person calls the next on the list; the last one calls back to confirm", 15, "middle", "600")
    s += t(360, 322, "One block captain for every 10–15 homes", 15, "middle", "700")
    return svg(720, 335, s)

def d_opsec():
    s = t(360, 28, "The OPSEC cycle", 19, "middle", "700")
    labels = [["1 Identify", "critical info"], ["2 Analyze", "threats"], ["3 Analyze", "vulnerabilities"], ["4 Assess", "risk"], ["5 Apply", "countermeasures"]]
    import math as m
    for i, (a, b2) in enumerate(labels):
        ang = -m.pi/2 + i*2*m.pi/5; x = 360 + 150*m.cos(ang); y = 200 + 130*m.sin(ang)
        s += rect(x-80, y-32, 160, 64, "#e3f2fd", "#1565c0", 2, 10) + t(x, y-6, a, 15, "middle", "700") + t(x, y+16, b2, 14, "middle")
    s += '<circle cx="360" cy="200" r="70" fill="none" stroke="#90a4ae" stroke-width="3" stroke-dasharray="8 6"/>'
    s += t(360, 196, "repeat as", 14, "middle") + t(360, 214, "things change", 14, "middle")
    return svg(720, 370, s)

R = {
 1: "Long dark winters mean long nights to watch; lights matter more, and snow shows every track around the house — check it each morning. Cold makes long outdoor watches dangerous: watch from a warm, dark window and rotate often (Part 5).",
 2: "Rain and dark winter evenings reduce visibility; keep shrubs low and paths lit " + c(1) + ". Dense forest around rural homes gives cover to anyone approaching — clear sight lines near the house.",
 3: "Open country: you can see far, and so can others — light discipline at night matters (7.2). Homes are far apart; organize by road or section with radios rather than door-to-door phone trees (6.2).",
 4: "Mix of cities, suburbs and farms. In suburbs, the block-captain model (6.1) fits naturally. Winter: plan watches from inside.",
 5: "Dense cities and old housing with weak wooden door frames — reinforce strike plates and jambs first " + c(2) + ". Row houses and apartments share walls: organize by building and floor.",
 6: "Hurricane shutters and plywood double as window protection; make sure every bedroom still has a way out in a fire " + c(5) + ". Heat makes daytime watches tiring — shorten shifts.",
 7: "Many homes have sliding glass doors: bar the track and stop lift-out " + c(2) + ". Storm shutters help, but keep fire exits usable " + c(5) + ".",
 8: "Heat by day, cold at night; long sight lines in open desert. Water sources are where people will gather — keep yours out of sight (7.2).",
 9: "Scattered mountain homes with one road in: a radio net and a road watch give early warning (6.2, 6.3). Snow records tracks.",
 10: "Wildfire country: do not let hardening block escape — fire is often a bigger threat than intruders " + c(5) + ". Dense suburbs suit Neighborhood Watch structure " + c(4) + ".",
 11: "Many homes already have bars on windows: confirm they have quick-release catches inside " + c(5) + ". Walled compounds give strong territorial definition " + c(3) + ".",
 12: "Dense colonias and walled homes; neighborhood networks are often already strong — build on them " + c(4) + ". Make sure barred windows open from inside " + c(5) + ".",
 13: "Hurricane shutters and barred windows are common; keep a quick way out in a fire " + c(5) + ". Island and village communities can organize quickly around existing leaders " + c(4) + ".",
}

def body():
    b = []
    b.append('<div class="box tip"><b class="t">What this guide is — and is not</b>This is a <b>defensive</b> guide: making your home harder to break into, seeing trouble early, organizing neighbors, and keeping quiet about your supplies. It contains no weapon-making instructions. The aim is to avoid confrontation entirely: a household or neighborhood that looks alert, organized and hard to enter is usually passed by.</div>')
    b.append(part("p1", "Part 1", "Awareness Comes First"))
    b.append(h2("base", "1.1 Know what normal looks like"))
    b.append('<p>Recognizing what is normal around you is the first step in recognizing what is not ' + c(4) + '. Learn your area: who lives where, which vehicles belong, when people come and go, which dogs bark at what. Burglars generally prefer empty homes with easy or hidden access and quick escape routes ' + c(1) + ', and most are not confrontational — they do not want contact with you ' + c(2) + '. Looking occupied and alert is a defense in itself.</p>')
    b.append(h2("susp", "1.2 What counts as suspicious"))
    b.append('<p>Neighborhood Watch defines it simply: <b>anything that feels uncomfortable or looks out of place</b> ' + c(4) + '. Examples from the Watch manual ' + c(4) + ':</p>')
    b.append(ul(["someone peering into cars or windows, or loitering near schools, parks or secluded areas;", "open or broken doors and windows at an empty home or business;", "people arriving or leaving at unusual hours, or several people who seem to be working together;", "someone tampering with electrical, gas or water systems with no clear reason;", "signs of forced entry or tampering with locks or alarms."]))
    b.append(h2("desc", "1.3 Describing people and vehicles"))
    b.append(ul(["<b>People:</b> clothing helps, but note things that cannot change — height, build, skin and eye color, scars, tattoos, moles. How many? " + c(4), "<b>Vehicles:</b> make (Ford, Toyota…), type (pickup, SUV), model if you can, color, damage, and plate. Write a plate down anywhere — paper, your hand, the dirt. A partial plate still helps. Say \"I'm not sure\" when you are not " + c(4) + ".", "<b>Report:</b> what happened, where, when (time and day), who, and any pattern you have noticed " + c(4) + ". In a grid-down world, report to your block captain or radio net (Part 6)."]))
    b.append(check("Notebook for the watch", ["Date, time and place", "Who: number of people, descriptions", "What they did, which way they went", "Vehicles: make, type, color, plate", "Who you told, and when"]))

    b.append(part("p2", "Part 2", "Hardening the House"))
    b.append('<p>Start your own security survey at the front door, then every door, window, lock and the landscaping ' + c(2) + '. Most doors and frames are weak; the most common entry is a <b>hard kick that breaks the wooden jamb</b> ' + c(1) + '.</p>')
    b.append(h2("doors", "2.1 Doors and door frames"))
    b.append(fig(d_door(), "Strike plate, screws and deadbolt specifications from Kansas City PD and Snohomish County Sheriff " + c(1, 2) + "."))
    b.append(ul(["Exterior doors should be <b>solid wood or metal-clad</b>; doors in poor condition are too weak " + c(1, 2) + ". A metal reinforcement collar strengthens the lock area " + c(2) + ".", "Replace the factory strike plate with a heavier <b>4- or 6-hole</b> plate fastened with <b>at least 3-inch screws</b> into the stud behind the jamb " + c(1, 2) + ".", "Deadbolt: <b>hardened steel bolt with a 1-inch throw</b>, one-piece housing, cylinder halves held by at least ¼-inch carriage bolts " + c(2) + ".", "A jamb brace — a metal strip behind the trim that the bolt passes through — spreads force along the frame " + c(2) + ".", "Fit a wide-angle door viewer (160–180°) and use it before opening " + c(1, 2) + ". If you do not recognize the person, do not open — but let them know someone is home " + c(2) + ".", "Rekey locks when you move in; you cannot know who has keys " + c(2) + "."]))
    b.append(caution("Double-cylinder deadbolts", "A deadbolt needing a key on both sides can trap you in a fire; Kansas City PD warns it can be a fire hazard and violate fire codes " + c(2) + ". If you use one beside glass, keep the key in the lock or right beside the door whenever anyone is home."))
    b.append(h2("windows", "2.2 Windows and sliding doors"))
    b.append(fig(d_window(), "Window pinning and sliding-door methods from Kansas City PD " + c(2) + "."))
    b.append(ul(["Double-hung window latches are easily pried. <b>Pin the window:</b> drill at a slight downward angle where the sashes overlap, through the inner sash and into (not through) the outer one, and drop in a strong nail. A second hole lets you pin it slightly open for air " + c(2) + ".", "Keyed slide locks work for vinyl and double-hung windows " + c(2) + ".", "Sliding doors can be pried or lifted out. Put a bar, dowel or track lock in the track, and drive pan-head screws into the upper track so the door slides but cannot be lifted out " + c(2) + ". Snohomish County also lists drop bars, dowels and pins " + c(1) + "."]))
    b.append(h2("bars", "2.3 Security bars — and getting out in a fire"))
    b.append(danger("Never trap yourself", "NFPA: security bars on windows and doors must have <b>quick-release devices</b> that open from inside immediately, without a key, tool or special knowledge. Everyone in the home must know how to work them, and you should practice escaping through each barred window " + c(5) + ". Keep two ways out of every room."))

    b.append(part("p3", "Part 3", "Perimeter by Design"))
    b.append(h2("cpted", "3.1 The CPTED principles"))
    b.append('<p>Crime Prevention Through Environmental Design (CPTED) uses the layout of a place to reduce opportunities for crime and make offenders feel at risk of being seen ' + c(3) + '. Three basic principles, plus two supporting ideas ' + c(3) + ':</p>')
    b.append(table(["Principle", "What it means at home"], [["Natural surveillance", "Windows, lighting and landscaping placed so occupants and passers-by can see — people are unlikely to try a crime if they may be observed " + c(3)], ["Natural access control", "Entrances, exits, fences, landscaping and lighting guide people to where you want them " + c(3)], ["Territorial reinforcement", "Clear property lines and a visible difference between public and private space — fences, paving, signs, plantings " + c(3)], ["Maintenance", "A cared-for property signals guardianship and deters offenders " + c(3)], ["Activity support", "Regular, legitimate activity by residents discourages crime in shared spaces " + c(3)]]))
    b.append(h2("land", "3.2 Landscaping, fences and sight lines"))
    b.append(fig(d_cpted(), "Shrub and tree heights from Snohomish County Sheriff; CPTED principles from Calgary Police " + c(1, 3) + "."))
    b.append(ul(["Prune shrubs <b>under 3 feet</b> and trim tree branches <b>7 feet off the ground</b> so no one can hide near doors and windows " + c(1) + ".", "Shrubs and trees should not block the view of doors and windows " + c(2) + ".", "Use fences, plantings and paths to steer visitors to one entrance you can watch " + c(3) + ".", "Keep the place looking occupied and maintained " + c(3) + "."]))

    b.append(part("p4", "Part 4", "Lighting & Homemade Alarms"))
    b.append(h2("light", "4.1 Lighting"))
    b.append(ul(["Light every entry; mount lights <b>high and out of reach</b>, such as under eaves, with motion lights at the sides and rear " + c(1, 2) + ".", "Use motion sensors and dawn-to-dusk photocells on outdoor lights " + c(1, 2) + ". Solar motion lights keep working without the grid.", "Inside lights, a radio, and timers give a lived-in look " + c(2) + ".", "Balance with OPSEC: in a long grid-down period, the only lit house on the street draws attention (7.2). Motion-triggered light at entrances is better than all-night floodlights."]))
    b.append(h2("alarm", "4.2 Early-warning alarms you can build"))
    b.append(fig(d_alarm(), "Noise makers give warning; they must never be built to injure."))
    b.append(ul(["<b>Can line:</b> a light cord across an approach at ankle height tied to a cluster of cans holding pebbles.", "<b>Bells</b> on gates and on the inside of doors; a stick or bottle balanced against a door that falls when it opens.", "<b>Gravel</b> on paths and under windows crunches underfoot.", "<b>Battery chimes:</b> magnetic door/window alarms and motion chimes run for months on batteries.", "<b>Dogs</b> are the oldest alarm of all — if you can feed one."]))
    b.append(danger("No booby traps", "Never rig anything that can injure — spikes, falling weights, electrified fences, or anything explosive. They hurt children, neighbors, rescuers and your own family, and are crimes in normal times. Alarms should only make noise or light."))

    b.append(part("p5", "Part 5", "Watch Schedules"))
    b.append(h2("sleep", "5.1 Sleep is a security need"))
    b.append('<p>A tired guard misses things and makes poor decisions. CDC: adults 18–60 need <b>7 or more hours</b> of sleep a day; teens 13–17 need 8–10 hours ' + c(7) + '. Plan watches so everyone still gets enough sleep; short shifts with a fresh person beat one exhausted person all night.</p>')
    b.append(h2("rota", "5.2 Sample rotations"))
    b.append(fig(d_rota(), "With four adults and 2-hour shifts, an 8-hour night is covered and everyone keeps most of their sleep."))
    b.append(table(["Adults available", "Night watch (10 PM–6 AM)", "Notes"], [["2", "Two 4-hour shifts, or alarms + one person sleeping near the door", "Rely on alarms (4.2) and a dog; watch only when there is a known threat"], ["3", "Shifts of about 2 h 40 min", "Each person loses under 3 hours of sleep"], ["4", "Four 2-hour shifts", "Rotate the order nightly"], ["6+ (two households)", "Pairs, 2-hour shifts", "One watches, one listens to the radio; swap halfway"]]))
    b.append(h2("post", "5.3 Standing a good watch"))
    b.append(ul(["Watch from inside, in the dark, from a window with a wide view — you can see out, others cannot see in.", "Keep a notebook (1.3), a light, and a way to wake the house quietly (a cord to a bell, a radio, a knock code).", "Hand over properly: what you saw, what changed, anything to check at first light.", "Agree beforehand what the watch does if something happens: wake everyone, lock up, call the net. <b>The watch observes and reports — it does not go out to confront</b> " + c(4) + "."]))

    b.append(part("p6", "Part 6", "Organizing the Neighborhood"))
    b.append('<p>One household cannot watch all night forever; a street can. The Neighborhood Watch model, built over decades by the National Sheriffs\' Association and U.S. Justice Department, is a ready-made structure ' + c(4) + '.</p>')
    b.append(h2("org", "6.1 Structure: captains and coordinators"))
    b.append(ul(["<b>Block captains:</b> one for every <b>10–15 houses</b>. They link residents to the coordinator, keep a current list of names, addresses and contacts, welcome newcomers, and talk with each neighbor often about problems and needs " + c(4) + ".", "<b>Coordinator:</b> keeps the master list (including vehicle descriptions), links captains and members, arranges training " + c(4) + ".", "Divide the area into small workable sections using streets or natural boundaries " + c(4) + ".", "Meet regularly; the manual suggests getting together every 3–6 months in normal times " + c(4) + " — far more often in a crisis."]))
    b.append(h2("tree", "6.2 Phone trees and radio nets"))
    b.append(fig(d_tree(), "Phone-tree method from the Neighborhood Watch Manual " + c(4) + "."))
    b.append(ul(["Urgent news goes to the top of the tree; each person calls the next on the list, skipping down until an adult answers; the last person calls the top to confirm " + c(4) + ". Practice it " + c(4) + ".", "When phones fail, use the same tree with runners or radios (FRS/GMRS) — see the Radio & Communications guide. Agree on channels, check-in times and simple code words.", "Use the tree to stop rumors as well as spread news " + c(4) + "."]))
    b.append(h2("patrol", "6.3 Patrols: watch and report, never confront"))
    b.append('<p>Neighborhood Watch patrols go out in <b>pairs</b> on set shifts and often notice what stationary watchers miss: lost children, stranded people, hazards, accidents ' + c(4) + '. The manual is clear: patrol members <b>do not have police powers, must not carry weapons or pursue vehicles, and should never confront suspicious persons</b>; they report by radio to a base station ' + c(4) + '. Carry flashlights at night ' + c(4) + '.</p>')
    b.append(h2("res", "6.4 Pooling resources"))
    b.append('<p>Make a neighborhood plan: who has a gas stove? A four-wheel-drive vehicle? Who has special needs? List your neighborhood\'s resources ' + c(4) + ' — medical skills, tools, radios, generators, wells, gardens. Shared work and shared watch make every household safer.</p>')

    b.append(part("p7", "Part 7", "OPSEC: Keeping Quiet About What You Have"))
    b.append('<p>Operations security (OPSEC) is the U.S. military\'s five-step process for identifying and protecting critical information ' + c(6, 8) + '. The same idea protects a household: if no one knows you have food, fuel and water, no one comes for them.</p>')
    b.append(h2("five", "7.1 The five-step OPSEC process"))
    b.append(fig(d_opsec(), "The five-step OPSEC process from CDSE and Marine Corps MCWP 3-40.9 " + c(6, 8) + "."))
    b.append(table(["Step", "Household version"], [["1 Identify critical information " + c(6), "How much food, water, fuel, medicine you have; where it is; when the house is empty"], ["2 Analyze threats " + c(6), "Who might want it — and how they would find out"], ["3 Analyze vulnerabilities " + c(6), "What gives you away: generator noise, cooking smells, lights, deliveries, talkative kids, social media"], ["4 Assess risk " + c(6), "Which leaks are most likely and most harmful"], ["5 Apply countermeasures " + c(6), "Fix the worst leaks first (7.2); review as things change"]]))
    b.append(h2("hide", "7.2 Everyday OPSEC for a household"))
    b.append(ul(["Do not talk about your stockpile outside a trusted circle; teach children the same.", "Never post supplies, routines or travel plans online. Kansas City PD even advises not telling delivery services you are away " + c(2) + ".", "Light discipline: blackout curtains in a dark neighborhood; no flashlights waved at windows.", "Noise: run generators briefly, in daytime, muffled and out of sight — and only outdoors, far from windows (carbon monoxide; see Fire & Heating).", "Smells carry: cook at normal mealtimes, and bury or burn food waste.", "Look like everyone else: same rationed look, same worn yard. Keep stores spread out and out of sight from doors and windows.", "Be generous strategically: sharing within your Watch group builds allies (6.4)."]))

    b.append(part("p8", "Part 8", "Region by Region"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Value"], [["Strike plate screws", "≥ 3 in, into the stud " + c(1, 2)], ["Deadbolt", "Hardened steel, 1-in throw " + c(2)], ["Door viewer", "160–180° " + c(1, 2)], ["Shrubs / tree limbs", "< 3 ft / 7 ft up " + c(1)], ["Security bars", "Quick-release inside; practice escape " + c(5)], ["Block captain", "1 per 10–15 homes " + c(4)], ["Patrols", "Pairs; observe and report, never confront " + c(4)], ["Adult sleep", "7+ hours " + c(7)], ["OPSEC", "Identify, threats, vulnerabilities, risk, countermeasures " + c(6)]]))
    b.append('<p class="small">General information for emergencies; defensive measures only. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Defense & Security", "Survival Info<br>Defense &amp;<br>Security",
          "Hardening doors and windows, designing a safer perimeter, lighting and homemade alarms, watch schedules, organizing the neighborhood, and keeping quiet about your supplies — a defensive guide for every region of North America.",
          "Defense & Security", TOC, cover_art(), "Radio · House · Fire · Medical · Food Preservation · Navigation · Bunkers")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Defense.pdf")
