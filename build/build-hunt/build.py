import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'
W = "#8d6e63"; WD = "#5d4037"

def cover_art():
    s = '<rect width="720" height="380" fill="#1b3a2f"/><rect y="290" width="720" height="90" fill="#2e5e4e"/>'
    s += '<path d="M0 300 q180 -30 360 0 t360 0 v80 h-720z" fill="#1565c0" opacity=".8"/>'
    for i in range(9): s += f'<polygon points="{40+i*80},290 {70+i*80},170 {100+i*80},290" fill="#0f2a20"/>'
    s += '<path d="M470 330 q40 -25 80 0 q-40 25 -80 0z M550 330 l20 -12 v24z" fill="#cfd8dc"/>'
    s += '<path d="M150 150 l20 -50 l10 30 l30 -40 l5 45" fill="none" stroke="#d7b98e" stroke-width="6"/>'
    s += '<circle cx="620" cy="80" r="34" fill="#ffe082"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Before You Start", [("law","1.1 The law, and when this guide applies"),("where","1.2 Reading sign: where to set traps")]),
 ("p2", "Part 2 · Snares", [("simple","2.1 Simple snare and drag noose"),("twitch","2.2 Twitch-up snare"),("treadle","2.3 Treadle snare"),("squirrel","2.4 Squirrel pole and noosing wand")]),
 ("p3", "Part 3 · Deadfalls & Other Traps", [("fig4","3.1 Figure-4 deadfall"),("paiute","3.2 Paiute deadfall"),("bottle","3.3 Bottle trap")]),
 ("p4", "Part 4 · Fishing Without a Store", [("hooks","4.1 Hooks and gorges"),("stake","4.2 Stakeout lines"),("net","4.3 Making and setting a gill net"),("ftrap","4.4 Fish traps and tidal traps"),("spear","4.5 Spearing fish"),("fsafe","4.6 Fish that can hurt you")]),
 ("p5", "Part 5 · Field Dressing & Butchering", [("dress","5.1 Field dressing big game"),("cool","5.2 Cooling the carcass"),("butcher","5.3 Skinning and cutting up"),("small","5.4 Small game, birds, snakes and fish")]),
 ("p6", "Part 6 · Game Diseases & Safe Handling", [("tul","6.1 Tularemia"),("cwd","6.2 Chronic wasting disease"),("trich","6.3 Trichinellosis"),("bruc","6.4 Brucellosis"),("cook","6.5 Cooking temperatures")]),
 ("p7", "Part 7 · Game & Fish Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_trail():
    s = t(360, 28, "Channel the animal into the snare", 19, "middle", "700")
    s += '<path d="M0 200 Q180 150 360 200 T720 200" fill="none" stroke="#d7ccc8" stroke-width="60"/>'
    s += t(80, 140, "trail or run", 16, "middle", "600")
    for i in range(6):
        s += line(180 + i*28, 140 + i*9, 196 + i*28, 152 + i*9, WD, 6) + line(180 + i*28, 270 - i*9, 196 + i*28, 258 - i*9, WD, 6)
    s += '<circle cx="380" cy="200" r="26" fill="none" stroke="#c62828" stroke-width="4"/>' + line(380, 174, 380, 120, "#c62828", 2) + rect(370, 110, 20, 14, W, WD, 2, 2)
    s += t(380, 100, "noose, head-high for the animal", 15, "middle", "600")
    s += t(240, 310, "funnel of sticks/brush narrows to just wider than the animal", 15, "middle")
    s += t(560, 280, "Few animals back up —", 15, "middle") + t(560, 300, "they keep going forward", 15, "middle")
    return svg(720, 330, s)

def d_drag():
    s = t(360, 28, "Drag noose", 19, "middle", "700")
    s += line(160, 330, 160, 130, WD, 10) + line(160, 140, 135, 110, WD, 8) + line(160, 140, 185, 110, WD, 8)
    s += line(560, 330, 560, 130, WD, 10) + line(560, 140, 535, 110, WD, 8) + line(560, 140, 585, 110, WD, 8)
    s += line(130, 122, 590, 122, W, 14) + t(360, 100, "crossmember resting loosely in the forks", 15, "middle", "600")
    s += line(360, 128, 360, 170, "#455a64", 3) + '<circle cx="360" cy="215" r="44" fill="none" stroke="#455a64" stroke-width="4"/>'
    s += line(0, 330, 720, 330, "#a1887f", 6) + t(360, 360, "animal run", 15, "middle")
    s += t(600, 230, "noose above the ground:", 15, "start", "600") + t(600, 250, "never low enough", 15, "start") + t(600, 270, "to step into", 15, "start")
    s += t(360, 395, "The animal pulls the bar free; it snags in brush and holds the animal", 15, "middle", "600")
    return svg(720, 410, s)

def d_twitch():
    s = t(360, 28, "Twitch-up snare (two forked sticks)", 19, "middle", "700")
    s += line(0, 380, 720, 380, "#a1887f", 6)
    s += '<path d="M110 380 Q110 120 380 110" fill="none" stroke="#6d4c41" stroke-width="12"/>' + t(160, 260, "bent sapling (power)", 15, "start", "700")
    s += line(380, 112, 380, 240, "#455a64", 3) + t(392, 170, "cord", 14, "start")
    s += line(400, 380, 400, 262, WD, 10) + line(400, 266, 432, 254, WD, 8)
    s += line(380, 240, 380, 270, WD, 8) + line(380, 268, 430, 248, WD, 8)
    s += t(450, 236, "hanging forked stick: its short leg", 14, "start", "600") + t(450, 254, "hooks under the stake's short leg", 14, "start")
    s += t(450, 310, "stake: long leg driven into ground,", 14, "start") + t(450, 328, "short leg cut flat", 14, "start")
    s += line(380, 262, 300, 290, "#455a64", 3) + '<circle cx="270" cy="320" r="32" fill="none" stroke="#c62828" stroke-width="4"/>' + t(270, 372, "noose over trail", 14, "middle", "600")
    s += t(360, 415, "Animal pulls the noose → sticks part → sapling springs up. Use dry sticks: sap glues green ones", 14, "middle", "600")
    return svg(720, 430, s)

def d_fig4():
    s = t(360, 28, "Figure-4 deadfall trigger (side view)", 19, "middle", "700")
    s += line(0, 380, 720, 380, "#a1887f", 6)
    s += line(330, 380, 330, 200, "#6d4c41", 12) + t(300, 300, "upright", 15, "end", "700") + t(300, 320, "(flat top, side notch)", 14, "end")
    s += line(220, 300, 460, 170, "#8d6e63", 12) + t(480, 160, "diagonal / release stick", 15, "start", "700") + t(480, 180, "(notch rests on upright top)", 14, "start")
    s += line(210, 300, 520, 300, "#a1887f", 12) + t(540, 305, "bait stick (bait on far end)", 15, "start", "700")
    s += '<circle cx="510" cy="300" r="12" fill="#e69b00"/>'
    s += '<polygon points="140,170 640,90 650,130 150,210" fill="#9e9e9e" stroke="#616161" stroke-width="3"/>' + t(400, 90, "heavy flat rock or log", 15, "middle", "700")
    s += t(360, 420, "Animal tugs the bait → bait stick slips from the upright notch → weight falls", 15, "middle", "600")
    return svg(720, 435, s)

def d_paiute():
    s = t(360, 28, "Paiute deadfall (easier to set than the figure-4)", 19, "middle", "700")
    s += line(0, 380, 720, 380, "#a1887f", 6)
    s += line(330, 380, 330, 220, "#6d4c41", 12) + t(300, 300, "upright", 15, "end", "700")
    s += line(240, 260, 460, 180, "#8d6e63", 12) + t(470, 170, "diagonal stick", 15, "start", "700")
    s += line(245, 262, 300, 330, "#455a64", 3) + rect(290, 325, 46, 10, W, WD, 2, 2) + t(220, 350, "cord to small catch stick", 14, "end", "600") + t(220, 368, "wrapped half round upright", 14, "end")
    s += line(336, 332, 520, 372, "#a1887f", 8) + t(540, 360, "thin bait stick", 15, "start", "700")
    s += '<polygon points="140,190 640,120 650,160 150,230" fill="#9e9e9e" stroke="#616161" stroke-width="3"/>' + t(400, 115, "drop weight", 15, "middle", "700")
    s += t(360, 420, "Animal disturbs the bait stick → catch stick releases → diagonal flies up → weight drops", 14, "middle", "600")
    return svg(720, 435, s)

def d_pole():
    s = t(360, 28, "Squirrel pole and bottle trap", 19, "middle", "700")
    s += rect(60, 50, 40, 330, "#795548", "#4e342e", 3, 4) + line(100, 380, 300, 70, "#8d6e63", 12)
    for k in range(5):
        x = 130 + k*34; y = 333 - k*53
        s += f'<circle cx="{x+12}" cy="{y-14}" r="13" fill="none" stroke="#455a64" stroke-width="3"/>'
    s += t(160, 410, "wire nooses 5–6 cm wide, 2.5 cm off the pole;", 14, "middle") + t(160, 428, "none within 45 cm of either end", 14, "middle")
    s += line(400, 300, 700, 300, "#a1887f", 6)
    s += '<path d="M520 300 L470 420 L630 420 L580 300" fill="#d7ccc8" stroke="#6d4c41" stroke-width="3"/>'
    s += rect(490, 270, 120, 14, W, WD, 2, 2) + '<circle cx="505" cy="292" r="6" fill="#9e9e9e"/><circle cx="595" cy="292" r="6" fill="#9e9e9e"/>'
    s += t(550, 255, "bark cover on small stones, 2.5–5 cm up", 14, "middle", "600")
    s += t(660, 380, "hole 30–45 cm deep,", 14, "start") + t(660, 398, "wider at bottom", 14, "start")
    return svg(720, 440, s)

def d_fishgear():
    s = t(360, 28, "Gorge, wooden hook and stakeout", 19, "middle", "700")
    s += line(60, 100, 200, 100, "#bcaaa4", 8) + line(60, 100, 50, 96, "#bcaaa4", 4) + line(200, 100, 210, 104, "#bcaaa4", 4) + line(130, 100, 130, 60, "#455a64", 2) + t(130, 140, "gorge: sharp both ends,", 14, "middle") + t(130, 158, "line tied at the middle", 14, "middle")
    s += line(300, 60, 300, 140, "#8d6e63", 10) + '<path d="M300 140 q0 20 25 10 l-10 -26" fill="none" stroke="#455a64" stroke-width="4"/>' + t(300, 180, "hardwood shank ~2.5 cm,", 14, "middle") + t(300, 198, "point (bone, wire, nail) lashed in notch", 14, "middle")
    s += rect(400, 60, 300, 220, "#bbdefb", "none", 0, 0) + line(400, 70, 700, 70, "#1565c0", 2, "6 4") + t(690, 90, "surface", 13, "end")
    s += line(450, 280, 460, 80, WD, 6) + line(650, 280, 640, 80, WD, 6) + line(458, 95, 642, 95, "#263238", 3)
    s += line(520, 95, 520, 160, "#263238", 2) + line(580, 95, 580, 160, "#263238", 2) + '<circle cx="520" cy="165" r="6" fill="#e69b00"/><circle cx="580" cy="165" r="6" fill="#e69b00"/>'
    s += t(550, 310, "two saplings, line just under the surface,", 14, "middle") + t(550, 328, "short baited lines that cannot tangle", 14, "middle")
    return svg(720, 345, s)

def d_net():
    s = t(360, 28, "Gill net: pairs of lines knotted to neighbors, row by row", 19, "middle", "700")
    s += line(60, 60, 660, 60, "#455a64", 5) + t(360, 50, "top line tied between two trees", 14, "middle", "600")
    xs = [80 + i*40 for i in range(15)]
    for r in range(5):
        y0 = 60 + r*50; y1 = y0 + 50
        for i, x in enumerate(xs):
            off = 20 if ((i + r) % 2 == 0) else -20
            s += line(x if r == 0 else x, y0, x + off, y1, "#6d4c41", 2)
        for i in range(len(xs)):
            if (i + r) % 2 == 0 and i + 1 < len(xs): s += f'<circle cx="{xs[i]+20}" cy="{y1}" r="4" fill="#c62828"/>'
    s += line(40, 200, 680, 200, "#1e88e5", 2, "8 6") + t(690, 205, "guideline", 13, "end", "600", "#1e88e5")
    s += t(360, 340, "Red dots = overhand knots. Move the guideline down to keep each row even.", 14, "middle", "600")
    return svg(720, 355, s)

def d_ftrap():
    s = t(360, 28, "Funnel fish basket and tidal stone trap", 19, "middle", "700")
    s += '<path d="M60 200 L260 140 L340 140 L340 260 L260 260 Z" fill="#fff8e1" stroke="#6d4c41" stroke-width="4"/>'
    s += '<path d="M60 200 L180 185 M60 200 L180 215 M180 185 L200 195 M180 215 L200 205" stroke="#6d4c41" stroke-width="4" fill="none"/>'
    for i in range(6): s += line(260 + i*15, 140, 260 + i*15, 260, "#8d6e63", 2)
    s += arrow(20, 200, 90, 200, "#1e88e5") + t(200, 290, "sticks lashed into a funnel; fish swim in", 14, "middle") + t(200, 308, "through the narrow end and cannot find the way out", 14, "middle")
    s += rect(390, 60, 320, 260, "#e3f2fd", "#90caf9", 2, 6) + rect(390, 230, 320, 90, "#ffe0b2", "none", 0, 0) + t(550, 305, "shore", 14, "middle", "600")
    s += '<path d="M420 230 L520 120 L640 230" fill="none" stroke="#757575" stroke-width="12" stroke-linecap="round"/>'
    s += t(550, 90, "low stone wall angled out from shore", 14, "middle", "600") + t(550, 160, "fish trapped here", 14, "middle") + t(550, 178, "as the tide falls", 14, "middle")
    return svg(720, 330, s)

def d_dress():
    s = t(360, 28, "Field dressing: cuts and order (deer on its back)", 19, "middle", "700")
    s += '<ellipse cx="360" cy="210" rx="250" ry="90" fill="#d7b98e" stroke="#8a6d3b" stroke-width="3"/>'
    s += '<ellipse cx="640" cy="190" rx="50" ry="34" fill="#d7b98e" stroke="#8a6d3b" stroke-width="3"/>' + t(640, 195, "head", 14, "middle", "600")
    s += line(170, 210, 540, 210, "#c62828", 4, "10 6")
    s += t(150, 215, "1", 22, "end", "800", "#c62828") + t(360, 245, "2  belly cut, breastbone → genitals, skin and muscle lifted together", 14, "middle", "700")
    s += '<circle cx="120" cy="210" r="16" fill="none" stroke="#c62828" stroke-width="4"/>' + t(120, 320, "1 Cut around anus,", 14, "middle", "600") + t(120, 338, "tie off the bung", 14, "middle")
    s += line(560, 160, 560, 260, "#c62828", 4, "6 4") + t(560, 320, "3 Free diaphragm,", 14, "middle", "600") + t(560, 338, "cut windpipe at throat", 14, "middle")
    s += t(360, 320, "4 Roll out lungs, heart, entrails —", 14, "middle", "600") + t(360, 338, "don't cut paunch or intestines", 14, "middle")
    s += t(360, 380, "Gloves on · clean knife often · prop cavity open · cool fast", 16, "middle", "700")
    return svg(720, 395, s)

R = {
 1: "Caribou, moose, hares, ptarmigan, waterfowl, seals and fish. <b>Never eat polar bear or bearded seal liver</b> — toxic levels of vitamin A " + c(1) + ". Bear, seal and walrus meat can carry trichinella — cook thoroughly; freezing may not kill wild-game species " + c(7) + ". Caribou and moose can carry brucellosis " + c(8) + ". Cold helps cooling but frozen-in-the-field carcasses are hard to butcher: dress and quarter quickly.",
 2: "Deer, elk, black bear, rabbits, grouse and huge salmon runs — fish traps and nets (Part 4) can feed families. Gut and bleed fish fast; it spoils quickly " + c(1) + ".",
 3: "Pronghorn, deer, rabbits, prairie dogs, upland birds and waterfowl; bison where present. CWD has been reported in wild deer in 36 U.S. states and in Canada — follow 6.2 " + c(6) + ". Rabbits and rodents die in tularemia outbreaks " + c(5) + ": never pick up a dead or sick one bare-handed.",
 4: "White-tailed deer, turkey, squirrels, rabbits, waterfowl and lake fish. Squirrel poles (2.4) work well in hardwood forests. Follow the CWD precautions in 6.2 " + c(6) + ".",
 5: "White-tailed deer, moose, black bear, snowshoe hare, grouse, and coastal and freshwater fish. Cook bear meat thoroughly (trichinella) " + c(7) + ".",
 6: "Deer, feral hogs, squirrels, rabbits, turkey, catfish and other river fish. Wild hogs carry brucellosis — wear gloves and eye protection when butchering " + c(8) + ". Watch catfish spines " + c(1) + ". Warm weather: cool carcasses within hours (5.2) " + c(3) + ".",
 7: "Deer, feral hogs, waterfowl, abundant fish. Some reef fish (barracuda and others) can carry ciguatera toxin; FM 21-76 lists several poisonous saltwater species " + c(1) + ". Heat spoils game fast — dress immediately and pack with ice if any exists " + c(3) + ".",
 8: "Mule deer, rabbits, quail, javelina, bighorn. Water sources concentrate game — set snares on trails to water " + c(1) + ". Check bottle traps carefully: snakes hide in them " + c(1) + ". Rabbits can carry tularemia " + c(5) + ".",
 9: "Elk, mule deer, moose, bighorn, grouse, trout. Follow the CWD precautions in 6.2 " + c(6) + ". Elk and moose can carry brucellosis " + c(8) + "; wear gloves.",
 10: "Deer, wild pigs, rabbits, quail, coastal fish and shellfish. See the Food guide for shellfish (paralytic shellfish poisoning) warnings.",
 11: "Deer, javelina, rabbits, quail, and coastal fish in the Gulf of California and Gulf of Mexico. Heat makes fast cooling critical " + c(3) + ".",
 12: "Deer, rabbits, iguanas, birds, abundant coastal and lake fish. Reptiles are good food but should be cooked " + c(1) + ".",
 13: "Fish and shellfish, iguanas, agouti and birds. Reef fish can carry ciguatera; do not eat barracuda raw " + c(1) + ". Saltwater fish caught near reefs or river mouths should be cooked " + c(1) + ".",
}

def body():
    b = []
    b.append(part("p1", "Part 1", "Before You Start"))
    b.append(h2("law", "1.1 The law, and when this guide applies"))
    b.append(caution("Legal notice", "In normal times, hunting, trapping, snaring and fishing are regulated by state, provincial and federal law: seasons, licenses, legal methods and protected species. Many devices in this guide (snares, deadfalls, gill nets, fish traps) are illegal for most people in most places. This guide describes them for a true survival emergency, when lawful options no longer exist. Until then, follow your local regulations."))
    b.append('<p>The U.S. Army survival manual notes that several well-placed traps can catch much more game than a person with a rifle is likely to shoot, and that fish are usually more plentiful than mammals and can be caught silently ' + c(1) + '. Traps work for you while you do other jobs. Check them at least daily — and always approach carefully: every mammal can bite, and a cornered or trapped animal will fight ' + c(1) + '.</p>')
    b.append(h2("where", "1.2 Reading sign: where to set traps"))
    b.append('<p>There is no trap that catches everything. Find out what lives in the area and set traps for that species ' + c(1) + '. Look for ' + c(1) + ':</p>')
    b.append(ul(["runs and trails, tracks, droppings;", "chewed or rubbed plants;", "nesting or roosting sites, feeding and watering places."]))
    b.append('<p>A <b>trail</b> is used by several species and is distinct; a <b>run</b> is smaller and used by one species. Set traps between bedding, feeding and watering areas ' + c(1) + '.</p>')
    b.append(fig(d_trail(), "Channelization narrows the trail to just wider than the animal for at least one body length before the trap " + c(1) + "."))
    b.append(check("Don't spook the animal", ["Build trap parts away from the site, then carry them in " + c(1) + ".", "Do not use freshly cut live wood: its sap smells like danger " + c(1) + ".", "Mask your scent: mud from rotting vegetation, smoke from a fire, or fluid from the gall and urine bladders of earlier kills. Not human urine " + c(1) + ".", "Or let a trap weather a few days untouched before setting it " + c(1) + ".", "Bait with something the animal knows but cannot easily find nearby; salt works well. Scatter a little around the trap " + c(1) + "."]))

    b.append(part("p2", "Part 2", "Snares"))
    b.append('<p>Traps and snares crush, choke, hang or entangle. The power is the animal\'s own struggle, gravity, or a bent sapling; the heart of every trap is the <b>trigger</b> ' + c(1) + '.</p>')
    b.append(h2("simple", "2.1 Simple snare and drag noose"))
    b.append(ul(["<b>Simple snare:</b> a noose over a trail or den hole, tied to a firmly planted stake. Hold it open with twigs or grass. Make the loop big enough to pass over the head. It usually does not kill, and cord may loosen and slip off — <b>wire is best</b> " + c(1) + ".", "<b>Drag noose:</b> two forked sticks either side of a run, a crossbar laid loosely across, the noose hung from it above head height " + c(1) + "."]))
    b.append(fig(d_drag(), "Head nooses should never hang low enough for an animal to step into " + c(1) + "."))
    b.append(h2("twitch", "2.2 Twitch-up snare"))
    b.append('<p>A twitch-up is a supple hardwood sapling, stripped of branches, bent over and held by a trigger ' + c(1) + '.</p>')
    b.append(fig(d_twitch(), "Two forked sticks, each with a long and short leg, lock together until pulled " + c(1) + "."))
    b.append(steps(["Bend the sapling and mark the spot on the trail under it " + c(1) + ".", "Drive the long leg of one forked stick into the ground there; cut its short leg parallel to the ground " + c(1) + ".", "Tie the long leg of the second forked stick to cord from the sapling; cut its short leg to hook under the first one " + c(1) + ".", "Hang a noose over the trail; bend the sapling and engage the two short legs " + c(1) + "."]))
    b.append(h2("treadle", "2.3 Treadle snare"))
    b.append('<p>For small game on a trail: a shallow hole covered by thin sticks resting on a horizontal bar held between two forked stakes. A noose powered by a twitch-up or hanging weight is spread over the sticks, and a short trigger stick held by line tension keeps the bar in place. When the animal steps on a cover stick, the bar drops, the trigger releases, and the noose catches the foot ' + c(1) + '. The disturbed trail makes animals wary, so channel them in ' + c(1) + '.</p>')
    b.append(h2("squirrel", "2.4 Squirrel pole and noosing wand"))
    b.append(fig(d_pole(), "Squirrel pole and bottle trap dimensions from FM 21-76 " + c(1) + "."))
    b.append(ul(["<b>Squirrel pole:</b> lean a long pole against a tree with lots of squirrel activity. Fix several wire nooses along it. Keep the end nooses 45 cm from the ends so a squirrel cannot get its feet on something solid and chew the wire. Several squirrels can be caught on one pole " + c(1) + ".", "<b>Noosing wand:</b> a pole with a wire or stiff-cord slip noose at the tip, slipped over a roosting bird or held over a den hole from a hiding place " + c(1) + ". It takes patience."]))

    b.append(part("p3", "Part 3", "Deadfalls & Other Traps"))
    b.append(h2("fig4", "3.1 Figure-4 deadfall"))
    b.append('<p>Three notched sticks hold up a weight heavy enough to kill or stun the animal immediately. Practice beforehand — the trigger needs close fits and exact angles ' + c(1) + '.</p>')
    b.append(fig(d_fig4(), "Schematic of the figure-4 trigger; see FM 21-76 Figure 8-12 for notch details " + c(1) + "."))
    b.append(danger("Deadfalls can injure you", "Set the weight last, and keep hands and feet out from under it. A trigger sensitive enough to catch game can drop on your fingers. Never set large deadfalls where people or pets may walk."))
    b.append(h2("paiute", "3.2 Paiute deadfall"))
    b.append(fig(d_paiute(), "The Paiute trigger uses a cord and a 5 cm catch stick " + c(1) + "."))
    b.append(steps(["Tie one end of a cord to the lower end of the diagonal stick; tie the other end to a 5 cm catch stick " + c(1) + ".", "Bring the cord halfway round the upright with the catch stick at a right angle " + c(1) + ".", "Set the bait stick with one end against the weight (or a peg) and the other against the catch stick " + c(1) + ".", "When the animal disturbs the bait stick, the catch stick releases and the weight drops " + c(1) + "."]))
    b.append(h2("bottle", "3.3 Bottle trap"))
    b.append('<p>For mice and voles: a hole 30–45 cm deep, wider at the bottom than the small top, covered by bark propped 2.5–5 cm up on stones. Rodents hide under the cover and fall in; the sloping walls stop them climbing out. <b>Snakes hide in these holes</b> — check carefully ' + c(1) + '.</p>')

    b.append(part("p4", "Part 4", "Fishing Without a Store"))
    b.append('<p>Fish feed heavily before a storm and seldom after one when water is muddy. They rest in eddies near rocks, in deep pools, under overhanging brush and around logs and weeds. Light attracts fish at night ' + c(1) + '.</p>')
    b.append(h2("hooks", "4.1 Hooks and gorges"))
    b.append('<p>Make hooks from pins, needles, wire, small nails, or wood, bone, thorns, flint or shell ' + c(1) + '. A <b>wooden hook</b>: a hardwood shank about 2.5 cm long and 6 mm thick, notched at one end, with a point of bone, wire or nail lashed in. A <b>gorge</b>: a small shaft sharp at both ends, tied at the middle and baited lengthwise; the fish swallows it ' + c(1) + '.</p>')
    b.append(fig(d_fishgear(), "Improvised hooks and a stakeout " + c(1) + "."))
    b.append(h2("stake", "4.2 Stakeout lines"))
    b.append('<p>Drive two supple saplings into the bottom with tops just under the surface, tie a line between them just below the surface, and hang two short baited lines that cannot wrap around the poles, each other, or slide along the main line ' + c(1) + '.</p>')
    b.append(h2("net", "4.3 Making and setting a gill net"))
    b.append(fig(d_net(), "Knot pattern from FM 21-76 Figure 8-19 " + c(1) + "."))
    b.append(steps(["Tie a strong top line between two trees. Hang many lines from it by doubling them over (girth hitches or prusik knots). The net length and mesh size set how many lines and how far apart " + c(1) + ".", "Row 1: tie lines 2 and 3 together with an overhand knot, then 4 and 5, 6 and 7, to the end " + c(1) + ".", "Row 2: tie 1 to 2, 3 to 4, and so on — always one line from a pair to one from the next pair " + c(1) + ".", "Tie a guideline across the trees as a gauge and move it down after each row so mesh stays even " + c(1) + ".", "Thread a strong line along the bottom edge. Set the net across part of a stream or along a shore where fish move " + c(1) + "."]))
    b.append(h2("ftrap", "4.4 Fish traps and tidal traps"))
    b.append(fig(d_ftrap(), "Fish basket and shore trap described in FM 21-76 " + c(1) + "."))
    b.append(ul(["<b>Fish basket:</b> sticks lashed with vines into a funnel; close the top leaving a hole just big enough for fish to swim in " + c(1) + ".", "<b>Tidal trap:</b> schools come in with the tide and move along the shore. Pick the spot at high tide, build at low tide: a low stone wall angled out from shore, or block rock pools and sandbar ditches as the tide falls " + c(1) + "."]))
    b.append(h2("spear", "4.5 Spearing fish"))
    b.append('<p>In waist-deep water with many large fish: sharpen a long straight sapling, or split the end, wedge it apart, and sharpen both prongs. Ease the point toward the fish, then push suddenly to pin it to the bottom. Hold it down and grab the fish by hand — do not lift it on the spear. Allow for refraction: fish are not quite where they appear ' + c(1) + '.</p>')
    b.append(h2("fsafe", "4.6 Fish that can hurt you"))
    b.append(ul(["There are no poisonous freshwater fish, but catfish spines cause painful punctures that quickly become infected " + c(1) + ".", "<b>Cook all freshwater fish</b> to kill parasites; also cook saltwater fish caught near reefs or freshwater outlets " + c(1) + ".", "Some saltwater fish have poisonous flesh, seasonally or always — FM 21-76 lists porcupine fish, triggerfish, cowfish, thorn fish, oilfish, red snapper, jack and puffer; barracuda may carry ciguatera " + c(1) + ".", "Spoiled fish: sunken eyes, odd smell or color, dents that stay when pressed, slimy body. Cooking does not make spoiled fish safe " + c(1) + "."]))

    b.append(part("p5", "Part 5", "Field Dressing & Butchering"))
    b.append(h2("dress", "5.1 Field dressing big game"))
    b.append(fig(d_dress(), "Order of cuts from Cornell Cooperative Extension " + c(2) + "."))
    b.append(steps(["Wear disposable gloves to reduce disease exposure " + c(2, 3) + ". Clean the knife often between cuts " + c(2) + ".", "Lay the animal on its back, front legs raised, hind legs spread, propped with rocks or sticks " + c(2) + ".", "Cut around the anus to free the bung; tie it off so feces cannot touch the meat " + c(2) + ".", "Cut along the midline from breastbone to genitals, lifting skin and muscle together. <b>Do not cut the paunch or intestines</b> " + c(2) + ".", "Cut the diaphragm free from the ribs; cut the windpipe and gullet at the base of the throat " + c(2) + ".", "Pull out lungs, heart and entrails. Bag the heart and liver and keep them cold " + c(2) + ".", "Remove dirt, hair, feces and bloodshot meat; wipe the cavity dry " + c(2, 3) + "."]))
    b.append(danger("Do not eat this animal", "If the organs smell offensive, or there is greenish discharge, black blood or blood clots in the muscle, do not eat meat from the carcass " + c(2, 3) + ". Do not eat animals that looked sick or acted strangely, or that you found dead " + c(6) + "."))
    b.append('<p>Inspect the heart and liver for worms or parasites. A healthy liver is smooth, wet and deep red or purple; discard a diseased-looking liver — the muscle meat may still be usable ' + c(1) + '.</p>')
    b.append(h2("cool", "5.2 Cooling the carcass"))
    b.append(ul(["Above 40 °F, harmful bacteria grow quickly; aim to chill the carcass surface to <b>40 °F or lower within 24 hours</b> " + c(3) + ". Cornell: cool quickly to 35–40 °F " + c(2) + ".", "Prop the cavity open with a clean stick or hang the carcass so air circulates. A carcass left on the ground holds heat " + c(2, 4) + ".", "In warm weather, pack the cavity with ice or clean snow sealed in plastic bags " + c(2, 3) + ". Quartering and wrapping in cheesecloth helps; avoid tarps and canvas, which hold heat " + c(4) + ".", "Keep it in the shade. Leave the hide on during transport to keep the meat clean " + c(2) + ".", "Age only at 40 °F or below, for 2–3 days at most " + c(2) + ".", "Use food-grade bags or buckets for cut meat — not dark trash bags " + c(3) + "."]))
    b.append(h2("butcher", "5.3 Skinning and cutting up"))
    b.append(ul(["Slit the hide from throat to tail, cutting around the sex organs. Slip the blade under the skin, edge up, so you cut only hide and keep hair off the meat " + c(1) + ".", "Cut along each leg to the body cut, pull the hide away, cutting connective tissue as needed; remove head and feet " + c(1) + ".", "Front legs have no joint to the body — cut through the muscle. Cut hindquarters off at the ball-and-socket hip joint " + c(1) + ".", "Remove the tenderloins along each side of the spine. Break ribs first, then cut through the breaks — easier on the knife " + c(1) + ".", "Use the heart, liver, kidneys, tongue and bones (for broth) " + c(1) + ". Preserve extra meat by canning, drying or smoking — see the Food Preservation guide."]))
    b.append(h2("small", "5.4 Small game, birds, snakes and fish"))
    b.append(ul(["<b>Small mammals:</b> cut the hide around the middle, put two fingers under each side and pull both halves off " + c(1) + ". Wear gloves for rabbits and hares (tularemia, 6.1) " + c(5) + ".", "<b>Birds:</b> pluck or skin, remove entrails (save heart, liver, and the craw of seed-eaters), cut off feet " + c(1) + ". Remove entrails and crop soon after killing and do not pile warm birds together " + c(4) + ". Boil scavenger birds at least 20 minutes " + c(1) + ".", "<b>Snakes:</b> cut off the head and bury it; slit the skin 15–20 cm, peel it back and pull it off; remove entrails; boil or roast in sections " + c(1) + ".", "<b>Fish:</b> clean as soon as possible; cut out gills and the blood vessels along the spine; gut fish over 10 cm; scale or skin. Boiling with skin on saves the most food value " + c(1) + "."]))

    b.append(part("p6", "Part 6", "Game Diseases & Safe Handling"))
    b.append(h2("tul", "6.1 Tularemia"))
    b.append('<p>A potentially serious bacterial illness. Rabbits, hares and rodents are especially susceptible and often die in large numbers in outbreaks. People catch it from tick and deer-fly bites, skin contact with infected animals, contaminated water, or breathing contaminated dust. It occurs in every U.S. state except Hawaii. Prevent it with insect repellent, <b>gloves when handling sick or dead animals</b>, and by not mowing over dead animals ' + c(5) + '. Most cases respond to antibiotics ' + c(5) + '.</p>')
    b.append(h2("cwd", "6.2 Chronic wasting disease (CWD)"))
    b.append('<p>A fatal prion disease of deer, elk and moose, reported in wild deer in 36 U.S. states and in Canada. It has never been reported in people, but scientists cannot rule it out; prions stay in soil for years ' + c(6) + '. CDC advice where CWD occurs ' + c(6) + ':</p>')
    b.append(ul(["Do not shoot, handle or eat animals that look sick or act strangely, or eat meat from animals found dead.", "Wear latex or rubber gloves when field dressing.", "Avoid handling internal organs, <b>especially the brain and spinal cord</b>.", "Use separate knives and tools — not your kitchen ones.", "If an animal tests positive, do not eat it."]))
    b.append(h2("trich", "6.3 Trichinellosis"))
    b.append('<p>Caused by worm larvae in raw or undercooked meat of <b>bear, wild boar, wildcat, fox, wolf, seal or walrus</b> (and pork) ' + c(7) + '. Even tasting raw meat while preparing it is a risk. Homemade jerky and sausage from these meats caused many past cases. <b>Curing, drying, smoking or microwaving alone does not reliably kill the worms</b>, and freezing may not kill the species found in wild game ' + c(7) + '. Cook to safe temperatures with a thermometer ' + c(7) + '.</p>')
    b.append(h2("bruc", "6.4 Brucellosis"))
    b.append('<p>Bacteria carried by bison, elk, caribou, moose and wild hogs (and livestock). Hunters catch it from undercooked meat, raw milk, or body fluids in the eyes, nose or mouth while dressing animals ' + c(8) + '. Wear rubber gloves, goggles, an apron and a mask when handling tissues; cook meat thoroughly; do not drink raw milk ' + c(8) + '.</p>')
    b.append(h2("cook", "6.5 Cooking temperatures"))
    b.append(table(["Meat", "Minimum internal temperature"], [["Game meat (NDSU)", "160 °F " + c(4)], ["Game birds", "165 °F " + c(4)], ["Whole cuts, steaks, roasts (Cornell)", "145 °F " + c(2)], ["Ground game meat", "160 °F " + c(2)], ["Soups, stews, leftovers", "165 °F " + c(2)], ["Jerky, before drying", "160 °F " + c(2)]]))
    b.append(tip("Bear, boar and other trichinella carriers", "Cook these to well done, check with a thermometer, and never taste them raw " + c(7) + ". Without a thermometer, cook until no pink remains and juices run clear, then cook longer."))

    b.append(part("p7", "Part 7", "Game & Fish Region by Region"))
    b.append('<p>Common game in each region and the special hazards to watch for. Learn local species now, while field guides and wildlife offices are available.</p>')
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Rule", "Value"], [["Snare wire", "Wire holds best " + c(1)], ["Squirrel-pole nooses", "5–6 cm, 2.5 cm off pole, 45 cm from ends " + c(1)], ["Bottle trap", "30–45 cm deep, cover 2.5–5 cm up " + c(1)], ["Wooden hook shank", "≈ 2.5 cm × 6 mm " + c(1)], ["Carcass cooling", "≤ 40 °F within 24 h " + c(3)], ["Aging", "≤ 40 °F, 2–3 days max " + c(2)], ["Game meat / birds", "160 °F / 165 °F " + c(4)], ["CWD", "Gloves, avoid brain & spine, separate knives " + c(6)], ["Polar bear / bearded seal liver", "Never eat " + c(1)]]))
    b.append('<p class="small">General information for emergencies. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Hunting, Trapping & Fishing", "Survival Info<br>Hunting,<br>Trapping &amp; Fishing",
          "Survival snares and deadfalls, homemade fishhooks, nets and fish traps, field dressing and butchering, and how to handle game safely (tularemia, CWD, trichinella, brucellosis) — region by region across North America.",
          "Hunting & Fishing", TOC, cover_art(), "Food Preservation · Food · Water · Fire · Medical · Sanitation · Tools · House")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Hunting.pdf")
