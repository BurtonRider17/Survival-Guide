import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect width="720" height="380" fill="#12313d"/>'
    s += '<line x1="360" y1="340" x2="360" y2="70" stroke="#cfd8dc" stroke-width="6"/><line x1="300" y1="340" x2="360" y2="70" stroke="#cfd8dc" stroke-width="3"/><line x1="420" y1="340" x2="360" y2="70" stroke="#cfd8dc" stroke-width="3"/>'
    for r in (40, 80, 120): s += f'<path d="M{360-r} {70-r*0.2} A{r} {r} 0 0 1 {360+r} {70-r*0.2}" fill="none" stroke="#e69b00" stroke-width="4" opacity="{1-r/200}"/>'
    s += '<rect x="80" y="230" width="160" height="100" rx="10" fill="#e6b54a"/><circle cx="125" cy="280" r="26" fill="#12313d"/><rect x="170" y="255" width="50" height="12" fill="#12313d"/><rect x="170" y="280" width="50" height="12" fill="#12313d"/><line x1="220" y1="230" x2="250" y2="150" stroke="#e6b54a" stroke-width="5"/>'
    s += '<rect x="500" y="250" width="160" height="80" fill="#1a3a5c" stroke="#cfd8dc" stroke-width="3" transform="rotate(-20 580 290)"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [("p1", "Part 1 · Radio Basics", [("why","1.1 Why radio matters when the grid is down"),("services","1.2 Which radio service to use"),("rules","1.3 Licenses and the emergency rule")]),
 ("p2", "Part 2 · Listening", [("nwr","2.1 NOAA Weather Radio and broadcast AM/FM"),("crystal","2.2 Build a crystal radio (no batteries)")]),
 ("p3", "Part 3 · Talking", [("frs","3.1 FRS and GMRS"),("cb","3.2 CB radio"),("ham","3.3 Amateur (ham) radio"),("ops","3.4 How to make a call; nets and schedules")]),
 ("p4", "Part 4 · Antennas", [("dipole","4.1 Build a wire dipole"),("vhf","4.2 VHF/UHF antennas and height")]),
 ("p5", "Part 5 · Power for Radios", [("power","5.1 Batteries and solar for radios")]),
 ("p6", "Part 6 · Signaling Without Radio", [("signal","6.1 Mirrors, fires, ground signals, whistles, Morse")]),
 ("p7", "Part 7 · Region-by-Region Notes", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_services():
    s = t(360, 28, "Typical range depends on antenna height and terrain", 17, "middle", "700")
    rows = [("FRS", "handheld, no license", 0.12, "#81c784"), ("GMRS", "licensed; repeaters extend range", 0.3, "#4db6ac"), ("CB (27 MHz)", "no license; skip on good days", 0.4, "#ffe082"), ("Ham VHF/UHF", "licensed; repeaters", 0.45, "#90caf9"), ("Ham HF", "licensed; hundreds to thousands of miles", 0.95, "#ce93d8")]
    for i, (n, d, f, col) in enumerate(rows):
        y = 60 + i*66
        s += t(20, y+30, n, 16, "start", "700") + rect(170, y+8, 520*f, 34, col, "#455a64", 1.5, 4) + t(178, y+60, d, 14, "start")
    s += t(360, 412, "Bars are a rough comparison only, not measured ranges.", 14, "middle", "600", "#8a5a00")
    return svg(720, 425, s)

def d_crystal():
    s = t(360, 28, "Crystal radio wiring (after the 91st Bristol Scouts design)", 17, "middle", "700")
    s += line(60, 60, 60, 160, INK, 3) + t(70, 70, "antenna: long wire, high up", 14, "start", "600")
    s += rect(150, 140, 60, 160, "#ffe0b2", "#8a5a00", 2, 6) + t(180, 320, "10 turns", 14, "middle", "600")
    s += rect(230, 140, 100, 160, "#ffccbc", "#8a5a00", 2, 6) + t(280, 320, "50 turns", 14, "middle", "600")
    for y in range(150, 296, 14): s += line(150, y, 210, y, "#8a5a00", 1) + line(230, y, 330, y, "#8a5a00", 1)
    s += t(240, 345, "both coils side by side on one 80 mm tube", 14, "middle")
    s += line(60, 160, 150, 160, INK, 2) + line(150, 290, 60, 290, INK, 2) + line(60, 290, 60, 360, INK, 2)
    for i, w in enumerate((40, 26, 12)): s += line(60-w/2, 360+i*8, 60+w/2, 360+i*8, INK, 3)
    s += t(90, 395, "ground: metal water pipe or rod", 14, "start", "600")
    s += line(330, 160, 485, 160, INK, 2) + line(330, 290, 660, 290, INK, 2)
    s += rect(380, 200, 40, 50, "#e8f3fb", "#1d5d8f", 2, 2) + line(400, 160, 400, 200, INK, 2) + line(400, 250, 400, 290, INK, 2)
    s += t(400, 125, "100 pF", 13, "middle", "600") + t(400, 142, "variable", 13, "middle", "600")
    s += '<polygon points="470,190 500,190 485,215" fill="#1f2a33"/>' + line(470, 215, 500, 215, INK, 3) + line(485, 160, 485, 190, INK, 2) + line(485, 215, 485, 235, INK, 2)
    s += t(485, 142, "diode", 13, "middle", "600")
    s += line(485, 235, 660, 235, INK, 2)
    s += line(560, 235, 560, 248, INK, 2) + rect(548, 248, 24, 30, "#fff", INK, 2, 2) + line(560, 278, 560, 290, INK, 2) + t(530, 268, "10 kΩ", 13, "end", "600")
    s += line(660, 235, 660, 245, INK, 2) + '<circle cx="660" cy="262" r="17" fill="#cfd8dc" stroke="#1f2a33" stroke-width="2"/>' + line(660, 279, 660, 290, INK, 2)
    s += t(660, 200, "crystal", 13, "middle", "600") + t(660, 217, "earpiece", 13, "middle", "600")
    return svg(720, 412, s)

def d_dipole():
    s = t(360, 28, "Half-wave wire dipole: total length (ft) = 468 ÷ MHz", 18, "middle", "700")
    s += rect(30, 90, 20, 250, "#8d6e63", "#5d4037", 2, 2) + rect(670, 90, 20, 250, "#8d6e63", "#5d4037", 2, 2) + t(40, 370, "tree / mast", 14, "start") + t(680, 370, "tree / mast", 14, "end")
    s += line(50, 100, 80, 100, "#795548", 2) + rect(80, 94, 16, 12, "#fff", INK, 2, 3) + line(96, 100, 350, 120, "#b85c38", 4) + rect(350, 112, 20, 16, "#37474f", INK, 2, 2) + line(370, 120, 624, 100, "#b85c38", 4) + rect(624, 94, 16, 12, "#fff", INK, 2, 3) + line(640, 100, 670, 100, "#795548", 2)
    s += t(220, 90, "leg = ¼ wave", 15, "middle", "600") + t(500, 90, "leg = ¼ wave", 15, "middle", "600")
    s += t(88, 135, "insulator", 13, "middle") + t(360, 150, "center insulator", 13, "middle")
    s += line(360, 128, 360, 340, "#1f2a33", 4) + t(372, 260, "coax feed line to radio", 14, "start", "600")
    s += rect(80, 300, 230, 70, "#f1f8f1", "#2e7d32") + t(195, 325, "Example, 7.2 MHz (40 m):", 14, "middle", "600") + t(195, 348, "468 ÷ 7.2 = 65 ft total", 14, "middle") + t(195, 366, "≈ 32½ ft per leg", 13, "middle")
    s += rect(430, 300, 240, 70, "#fff6e0") + t(550, 325, "Cut ~6 in long, then trim", 14, "middle", "600") + t(550, 348, "for lowest SWR " + "(ARRL)", 14, "middle")
    return svg(720, 400, s)

def d_ground():
    s = t(360, 28, "Ground-to-air signals (FM 21-76)", 18, "middle", "700")
    items = [("V", "Need assistance"), ("X", "Need medical help"), ("N", "No"), ("Y", "Yes"), ("↑", "Going this way")]
    for i, (sym, m) in enumerate(items):
        x = 80 + i*140
        s += rect(x-55, 60, 110, 120, "#eef4f7", "#1f4e5f", 2, 6) + t(x, 145, sym, 64, "middle", "800", "#c0392b") + t(x, 210, m, 14, "middle", "600")
    s += t(360, 260, "Make each symbol large — many feet long — with strong contrast:", 15, "middle", "600")
    s += t(360, 284, "logs or rocks on snow, trenches in sand, bright cloth on grass.", 15, "middle")
    s += t(360, 330, "Three fires in a triangle or a line = distress", 16, "middle", "700", "#c0392b")
    s += t(360, 360, "SOS in Morse:  · · ·   — — —   · · ·", 18, "middle", "700")
    return svg(720, 390, s)

R = {
 1: "Vast distances and few repeaters: <b>HF ham radio</b> is the main way to reach beyond line of sight. Long winter nights favor the lower HF bands. Batteries lose capacity in extreme cold — keep them warm; solar is weak in winter, so plan for hand-crank or larger battery banks.",
 2: "Mountains and dense forest block VHF/UHF; get antennas high on ridges. Coastal areas: marine VHF radios are common on boats. Earthquake planning: agree on check-in times and frequencies in advance.",
 3: "Flat open country gives VHF/UHF and CB good ground-wave range from tall antennas (grain elevators, windmill towers). Tornado season: NOAA Weather Radio is vital " + c(12) + ".",
 4: "Flat to rolling terrain; many ham clubs and repeaters exist now — learn who your local operators are while you can. NOAA Weather Radio for severe storms " + c(12) + ".",
 5: "Dense cities: many repeaters, but buildings block handhelds; go to rooftops. Rural New England and Atlantic Canada: hills and forest favor HF for longer links. Canadian operators are certified by ISED " + c(11) + ".",
 6: "Hurricanes: NOAA Weather Radio " + c(12) + ", AM broadcast receivers, and pre-planned GMRS/ham check-ins. Humidity corrodes connectors — seal them with tape or coax sealant.",
 7: "Flat and low: antennas on the tallest structures. Hurricanes and lightning: disconnect antennas from radios during storms.",
 8: "Dry, clear and open: mountaintop repeaters cover huge areas; line-of-sight from ridges is excellent. Signal mirrors work extremely well in the desert sun (6.1).",
 9: "Mountains block VHF/UHF; climb to ridges or use HF. Repeaters on peaks may stay up on solar power for a while after a grid failure.",
 10: "Many repeaters and active hams; wildfire and earthquake check-in plans matter. Ridge-top line-of-sight is excellent.",
 11: "Wide open desert: mirrors and HF for long distances; CB is widely used by truckers on highways.",
 12: "Mountainous terrain blocks VHF; HF and high antenna sites help. Local rules differ from U.S. and Canadian rules — the emergency principle of using any means to save life applies in practice.",
 13: "Islands and coasts: HF and marine VHF. Hurricanes: secure antennas or take them down before storms, and keep a spare wire antenna.",
}

def body():
    b = []
    b.append('<div class="pb"></div>' + h2("howto", "How to use this guide"))
    b.append('<p>When phones and internet go down, radio is how you get news, weather warnings, and help, and how your group stays in touch. This beginner guide covers which radios to get, how to build antennas and a battery-free crystal radio, how to power radios with batteries and solar, and how to signal for help without any radio at all.</p>')
    b.append('<p>Numbered sources ' + c(1) + ' are listed at the end and saved as PDFs in <b>Survival Info Sources/Radio/</b>. See the Electricity guide for building battery banks and solar systems.</p>')
    b.append(check("Get these now", ["A battery or hand-crank AM/FM/NOAA Weather Radio receiver " + c(12), "FRS or GMRS handhelds for your group (one per adult)", "A ham radio license study guide, and an HF or VHF/UHF ham transceiver if you can", "A CB radio for vehicles", "Wire, insulators and coax for antennas (Part 4); a cheap SWR meter", "Rechargeable batteries, a 12 V battery, a small solar panel and charge controller (Part 5)", "A signal mirror and a loud whistle for every pack (Part 6)", "Printed frequency lists and this guide"]))
    b.append(part("p1", "Part 1", "Radio Basics"))
    b.append(h2("why", "1.1 Why radio matters when the grid is down"))
    b.append(ul(["<b>Listening</b> (receive only) needs no license: news, weather, and what neighbors are saying.", "<b>Talking</b> within your group: across a farm, a neighborhood, or a valley.", "<b>Long distance</b>: amateur HF radio can reach hundreds to thousands of miles without any towers or internet."]))
    b.append(h2("services", "1.2 Which radio service to use"))
    b.append(table(["Service", "License (U.S.)", "Power limit", "Best for"], [
        ["FRS (22 channels)", "None", "2 W ERP on channels 1–7 and 15–22; 0.5 W on 8–14 " + c(4), "Short-range family use"],
        ["GMRS (same 22 channels + repeaters)", "Individual license required " + c(6), "Up to 50 W for mobile, base and repeater stations on main channels " + c(5), "Group comms, repeaters"],
        ["CB (40 channels, 27 MHz)", "None", "4 W AM/FM; 12 W PEP SSB " + c(3), "Vehicles, highways; Channel 9 is emergency only " + c(2)],
        ["Amateur (ham)", "Exam-based license " + c(7, 11), "Varies by class and band", "Everything from local to worldwide"]]))
    b.append(fig(d_services(), "<b>Figure 1.</b> Rough comparison of radio services. Real range depends on antennas, height, terrain and conditions."))
    b.append(h2("rules", "1.3 Licenses and the emergency rule"))
    b.append('<p>In normal times, follow the rules: GMRS needs a license " + c(6) + ", and transmitting on ham bands requires passing an exam (ARRL explains how in the U.S. " + c(7) + "; in Canada, ISED issues amateur certificates " + c(11) + "). Getting licensed now also means you will have practiced before you need it.</p>'.replace('" + c(6) + "', c(6)).replace('" + c(7) + "', c(7)).replace('" + c(11) + "', c(11)))
    b.append(tip("The emergency rule", "U.S. amateur rules say nothing in them prevents an amateur station from using any means of radio communication at its disposal to provide essential communication needs for the immediate safety of human life and protection of property when normal communication systems are not available " + c(1) + ". CB rules say every channel may be used for emergencies and operators must always give priority to emergency communications " + c(2) + "."))
    b.append(part("p2", "Part 2", "Listening"))
    b.append(h2("nwr", "2.1 NOAA Weather Radio and broadcast AM/FM"))
    b.append('<p><b>NOAA Weather Radio All Hazards</b> broadcasts warnings across the U.S. on seven VHF frequencies: 162.400, 162.425, 162.450, 162.475, 162.500, 162.525 and 162.550 MHz. It needs a special receiver or a scanner ' + c(12) + '. Many cheap hand-crank radios include it. AM broadcast stations travel much farther at night than in the day, so scan the AM band after dark for distant news.</p>')
    b.append(h2("crystal", "2.2 Build a crystal radio (no batteries)"))
    b.append('<p>A crystal radio runs only on the energy of the radio waves it picks up, so it works forever without batteries — but it only hears strong AM stations, quietly, in an earpiece ' + c(15, 14) + '. The diode acts as the detector, turning the radio signal into audio ' + c(14) + '.</p>')
    b.append(fig(d_crystal(), "<b>Figure 2.</b> Crystal radio, following the 91st Bristol Scout Group instructions " + c(15) + "."))
    b.append(steps(["Parts (from the Scout instructions): a signal diode, a 100 pF variable capacitor, a crystal earpiece, a 10 kΩ resistor, an 80 mm (about 3 in) tube, 3 m and 15 m of insulated wire, and a long antenna wire " + c(15) + ". Salvage parts from old radios and electronics.",
        "Wind a <b>10-turn</b> coil of the 3 m wire on the tube, turns tight against each other. Right next to it, wind a <b>50-turn</b> coil from the 15 m wire " + c(15) + ".",
        "Connect one end of the 10-turn coil to the antenna and the other end to ground — a metal water pipe or radiator " + c(15) + ".",
        "Connect the variable capacitor across the 50-turn coil; connect the diode and earpiece (with the resistor across the earpiece) as in Figure 2.",
        "Put up the antenna as long and as high as you can " + c(15) + ". Tune slowly with the capacitor in a quiet place. If you hear nothing, check every connection " + c(15) + "."]))
    b.append(part("p3", "Part 3", "Talking"))
    b.append(h2("frs", "3.1 FRS and GMRS"))
    b.append('<p>FRS and GMRS share 22 channels. FRS handhelds are limited to 2 W (0.5 W on channels 8–14) ' + c(4) + ' and fixed antennas, so range is short — often a mile or two in town, farther from hilltops. GMRS radios can use more power (up to 50 W on the main channels for mobile, base and repeater stations ' + c(5) + '), detachable antennas and repeaters. Agree on a primary and backup channel for your group now, and write them down.</p>')
    b.append(h2("cb", "3.2 CB radio"))
    b.append('<p>CB has 40 channels near 27 MHz, needs no license, and is limited to 4 W on AM and 12 W PEP on SSB ' + c(3) + '. <b>Channel 9 is only for emergencies and traveler assistance</b> ' + c(2) + '; channel 19 is widely used by truckers on highways. A CB with SSB and a good antenna reaches farther, and on some days signals skip hundreds of miles.</p>')
    b.append(h2("ham", "3.3 Amateur (ham) radio"))
    b.append(table(["Band", "U.S. range", "Use"], [["2 m (VHF)", "144–148 MHz " + c(8), "Local; handhelds and repeaters. 146.52 MHz is the national simplex calling frequency " + c(8)], ["70 cm (UHF)", "420–450 MHz " + c(8), "Local; repeaters"], ["40 m (HF)", "7.000–7.300 MHz " + c(8), "Regional day, long distance at night"], ["80 m (HF)", "3.500–4.000 MHz " + c(8), "Regional, best at night and in winter"], ["20 m (HF)", "14.000–14.350 MHz " + c(8), "Long distance, daytime"]]))
    b.append('<p>Most beginners start with a handheld 2 m/70 cm radio. HF is what you need to reach beyond your region with no infrastructure at all — a simple wire dipole (4.1) and a 12 V radio will do it.</p>')
    b.append(h2("ops", "3.4 How to make a call; nets and schedules"))
    b.append(steps(["Listen first to make sure the channel is free.", "Say who you are calling, then who you are: \"Base, this is Truck One.\"", "Keep it short. Say \"over\" when you want a reply, \"out\" when finished.", "For an emergency, say \"<b>Mayday, Mayday, Mayday</b>\" or \"<b>Emergency</b>\" and give: who you are, where you are, what happened, how many people, what help you need."]))
    b.append(tip("Schedules save batteries", "Agree on fixed check-in times (for example, on the hour for 10 minutes, at 8 am and 8 pm) and frequencies. Radios can stay off the rest of the time. Write down a primary, backup and emergency channel for each service."))
    b.append(part("p4", "Part 4", "Antennas"))
    b.append(h2("dipole", "4.1 Build a wire dipole"))
    b.append('<p>The antenna matters more than the radio. A half-wave dipole is two equal wires fed in the middle with coax. ARRL gives the total length as <b>468 ÷ frequency in MHz</b> (in feet); add about six inches for trimming to get the lowest SWR ' + c(9, 10) + '.</p>')
    b.append(fig(d_dipole(), "<b>Figure 3.</b> A wire dipole strung between two supports " + c(9) + "."))
    b.append(table(["Band", "Frequency", "Total length (468 ÷ MHz)", "Each leg"], [["80 m", "3.9 MHz", "120 ft", "60 ft"], ["40 m", "7.2 MHz", "65 ft", "32½ ft"], ["20 m", "14.2 MHz", "33 ft", "16½ ft"], ["CB", "27.2 MHz", "17.2 ft", "8.6 ft"]]))
    b.append(steps(["Cut two equal wires to half the total length each, plus a few inches.", "Tie each outer end through an insulator (plastic, ceramic, or a piece of PVC); tie rope from the insulator to trees or masts.", "Join the inner ends to a center insulator; solder the coax center conductor to one leg and the shield to the other.", "Raise it as high as you can, clear of metal and power lines.", "Check SWR; trim equal amounts from both ends until SWR is lowest at your frequency " + c(9) + "."]))
    b.append(danger("Power lines", "Never put up an antenna where it could fall onto or touch power lines — even 'dead' lines can be re-energized by generators. Disconnect antennas during lightning storms."))
    b.append(h2("vhf", "4.2 VHF/UHF antennas and height"))
    b.append('<p>VHF and UHF travel mostly line of sight, so <b>height beats power</b>: a handheld on a hilltop can outdo a powerful base station in a valley. Replace a handheld\'s stubby antenna with a longer one, use a car\'s roof-mounted antenna, or put a base antenna on the roof or a mast. Keep coax runs short and use good coax; long thin coax wastes much of your signal at these frequencies.</p>')
    b.append(part("p5", "Part 5", "Power for Radios"))
    b.append(h2("power", "5.1 Batteries and solar for radios"))
    b.append('<p>Most mobile and base radios run on about 12–13.8 V DC, so a 12 V battery is natural. Use the numbers on <b>your</b> radio\'s spec sheet (receive current and transmit current) and the energy formula from the Electricity guide: <b>watt-hours = volts × amps × hours</b>.</p>')
    b.append('<div class="formula"><b>Worked method (use your radio\'s real numbers):</b><span class="eq">Daily Wh = 12 V × (receive A × receive hours + transmit A × transmit hours)</span>Then size the battery for 2–3 days with no sun, and the solar panel to refill one day\'s use in your region\'s winter sun (see the Electricity guide for peak sun hours by region).</div>')
    b.append(ul(["Handhelds: carry spare battery packs, or AA battery cases charged from a small solar charger.", "Turn radios off between scheduled check-ins (3.4) — receive current adds up over 24 hours.", "Fuse the positive lead close to the battery.", "Keep a hand-crank receiver as a backup that needs no batteries at all."]))
    b.append(part("p6", "Part 6", "Signaling Without Radio"))
    b.append(h2("signal", "6.1 Mirrors, fires, ground signals, whistles, Morse"))
    b.append(ul(["<b>Signal mirror:</b> aim the reflected sunlight through a V made with your fingers at an aircraft or distant point; a mirror flash can be seen very far on a sunny day " + c(16) + ".", "<b>Fires and smoke:</b> three fires in a triangle or straight line are an international distress signal " + c(16) + ". Green leaves make white smoke (shows on dark backgrounds); rubber or oil makes black smoke (shows on snow) " + c(16) + ".", "<b>Ground-to-air symbols:</b> make them large and high-contrast (Figure 4) " + c(16) + ".", "<b>Whistle:</b> carries farther than a voice and takes less energy; three blasts is a common distress call.", "<b>Morse code:</b> SOS is · · · — — — · · · " + c(13) + "; it can be sent with a flashlight, mirror, whistle or radio key."]))
    b.append(fig(d_ground(), "<b>Figure 4.</b> Ground-to-air emergency symbols and distress signals " + c(16, 13) + "."))
    b.append(table(["Letter", "Morse " + c(13), "Letter", "Morse"], [["A", "· —", "N", "— ·"], ["B", "— · · ·", "O", "— — —"], ["C", "— · — ·", "P", "· — — ·"], ["D", "— · ·", "Q", "— — · —"], ["E", "·", "R", "· — ·"], ["F", "· · — ·", "S", "· · ·"], ["G", "— — ·", "T", "—"], ["H", "· · · ·", "U", "· · —"], ["I", "· ·", "V", "· · · —"], ["J", "· — — —", "W", "· — —"], ["K", "— · —", "X", "— · · —"], ["L", "· — · ·", "Y", "— · — —"], ["M", "— —", "Z", "— — · ·"]]))
    b.append(part("p7", "Part 7", "Region-by-Region Notes"))
    b.append(regions_html(R))
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Item", "Value"], [["NOAA Weather Radio", "162.400–162.550 MHz (7 channels) " + c(12)], ["CB emergency", "Channel 9 " + c(2)], ["Ham 2 m calling", "146.52 MHz " + c(8)], ["FRS power", "2 W (0.5 W ch 8–14) " + c(4)], ["CB power", "4 W AM/FM, 12 W PEP SSB " + c(3)], ["Dipole length", "468 ÷ MHz = feet " + c(9)], ["SOS", "· · · — — — · · · " + c(13)], ["Distress fires", "3 in a triangle or line " + c(16)]]))
    b.append('<p class="small">General information. Frequencies and rules are for the U.S. unless noted; Canada and Mexico have their own rules. Sources checked November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Radio & Communications", "Survival Info<br>Radio &amp;<br>Communications",
          "Weather and news radios, a crystal radio that needs no batteries, FRS, GMRS, CB and ham radio, building wire antennas, powering radios with batteries and solar, and signaling for help without a radio.",
          "Radio & Communications", TOC, cover_art(), "Medical · Sanitation · Fire · Water · Food · Electricity · Concrete · Tools · House · Bunkers")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Radio.pdf")
