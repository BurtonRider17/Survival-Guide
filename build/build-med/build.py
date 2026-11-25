import sys; sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import *

def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'

def cover_art():
    s = '<rect x="0" y="0" width="720" height="380" fill="#12313d"/>'
    s += '<rect x="250" y="40" width="220" height="300" rx="26" fill="#f4f1ea"/>'
    s += '<rect x="330" y="90" width="60" height="200" fill="#c0392b"/><rect x="260" y="160" width="200" height="60" fill="#c0392b"/>'
    s += '<rect x="80" y="230" width="120" height="90" rx="10" fill="#e6b54a"/><rect x="118" y="214" width="44" height="20" rx="5" fill="#e6b54a"/>'
    s += '<rect x="132" y="250" width="16" height="50" fill="#12313d"/><rect x="115" y="267" width="50" height="16" fill="#12313d"/>'
    s += '<path d="M540 320 q30 -120 60 -150 q30 30 20 150z" fill="#8bc34a"/><line x1="590" y1="320" x2="590" y2="190" stroke="#2e7d32" stroke-width="5"/>'
    s += '<circle cx="640" cy="90" r="38" fill="#e69b00"/>'
    return f'<svg viewBox="0 0 720 380" width="100%" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

TOC = [
 ("p1", "Part 1 · First Steps in Any Emergency", [("kit","1.1 Your medical kit and improvised supplies"),("assess","1.2 Checking an injured person (ABC)"),("cpr","1.3 Not breathing, choking, heart attack"),("shock","1.4 Shock")]),
 ("p2", "Part 2 · Injuries", [("bleed","2.1 Stopping serious bleeding"),("wound","2.2 Cleaning and closing wounds"),("infect","2.3 Wound infection"),("fract","2.4 Fractures and splinting"),("disloc","2.5 Sprains and dislocations"),("burns","2.6 Burns"),("bites","2.7 Bites and stings"),("eye","2.8 Eye injuries"),("spine","2.9 Neck and back injuries"),("elec","2.10 Electrical injuries"),("ivy","2.11 Poison ivy, oak and sumac"),("head","2.12 Head injuries"),("allergy","2.13 Severe allergic reactions")]),
 ("p3", "Part 3 · Illness & Environment", [("dehyd","3.1 Dehydration and home-made ORS"),("diarr","3.2 Diarrhea and vomiting"),("heat","3.3 Heat illness"),("cold","3.4 Hypothermia and frostbite")]),
 ("p4", "Part 4 · Special Situations", [("birth","4.1 Emergency childbirth basics"),("dental","4.2 Dental emergencies"),("herbs","4.3 Herbal remedies — with cautions"),("steril","4.4 Cleaning and sterilizing instruments")]),
 ("p5", "Part 5 · Region-by-Region Health Risks", []),
 ("srcs", "Quick Reference & Sources", [])]

def d_abc():
    return flow([["1 · SAFETY", "Is the scene safe for you? Fire, traffic, wires, falling debris"],
                 ["2 · RESPONSIVE?", "Tap shoulders and shout. Look, listen, feel for breathing"],
                 ["3 · MASSIVE BLEEDING?", "Stop it now: pressure, packing, tourniquet (Part 2.1)"],
                 ["4 · AIRWAY & BREATHING", "Head tilt–chin lift. Not breathing normally → CPR (1.3)"],
                 ["5 · CIRCULATION / SHOCK", "Pale, cold, clammy, fast pulse → lay flat, keep warm (1.4)"],
                 ["6 · HEAD-TO-TOE CHECK", "Look for fractures, burns, hidden wounds; write down what you find"]], bh=70)

def d_tourniquet():
    s = t(360, 30, "Tourniquet on an arm or leg", 18, "middle", "700")
    # leg
    s += '<path d="M60 150 L560 150 Q610 150 640 175 L660 210 L620 225 L590 200 L60 210 Z" fill="#f2d3b8" stroke="#1f2a33" stroke-width="2"/>'
    s += '<ellipse cx="430" cy="180" rx="26" ry="12" fill="#c0392b"/>' + t(430, 250, "wound", 15, "middle", "600", "#c0392b")
    s += rect(300, 138, 26, 84, "#1f2a33", "#1f2a33", 1, 3) + line(313, 132, 313, 228, "#e69b00", 6)
    s += t(313, 270, "tourniquet 2–3 in (5–8 cm) above wound,", 15, "middle") + t(313, 292, "never on a joint; tighten until bleeding stops", 15, "middle")
    s += arrow(313, 255, 313, 228) + arrow(430, 235, 430, 196, "#c0392b")
    s += t(150, 100, "toward heart", 15, "middle", "600") + arrow(220, 115, 70, 115)
    s += rect(470, 300, 230, 60, "#fff6e0") + t(585, 325, "Write the TIME on the", 15, "middle", "600") + t(585, 346, "person's forehead or tag", 15, "middle")
    return svg(720, 380, s)

def d_splint():
    s = t(360, 30, "Forearm splint: immobilize the joint above and below", 18, "middle", "700")
    s += rect(80, 120, 560, 26, "#d7b98e", "#8a6d3b", 2, 4) + t(360, 108, "rigid board, rolled magazine, sticks or SAM-type splint", 15, "middle")
    s += '<path d="M100 150 L560 150 Q600 152 620 165 L640 175 L620 190 L560 196 L100 196 Z" fill="#f2d3b8" stroke="#1f2a33" stroke-width="2"/>'
    s += rect(90, 146, 540, 8, "#e8f3fb", "#2f7fbf", 1, 2)
    for x in (140, 300, 460, 590):
        s += rect(x, 112, 22, 92, "none", "#2e7d32", 4, 3)
    s += t(150, 240, "padding between splint and skin", 15, "start") + arrow(200, 228, 200, 156, "#2f7fbf")
    s += t(420, 240, "ties above and below the break,", 15, "start") + t(420, 260, "not directly over it", 15, "start") + arrow(470, 226, 470, 204, "#2e7d32")
    s += t(700, 225, "leave fingers", 14, "end") + t(700, 243, "visible", 14, "end")
    s += rect(60, 290, 600, 70, "#f1f8f1", "#2e7d32") + t(360, 318, "Check fingers BEFORE and AFTER tying: color, warmth, feeling.", 15, "middle", "600")
    s += t(360, 342, "Cold, pale, blue, numb or tingling → loosen the ties.", 15, "middle")
    return svg(720, 380, s)

def d_ors():
    s = t(360, 32, "Home-made oral rehydration solution (WHO)", 19, "middle", "700")
    s += rect(60, 70, 170, 210, "#cfe6f7", "#2f7fbf") + t(145, 175, "1 litre", 22, "middle", "700") + t(145, 202, "safe water", 16, "middle") + t(145, 226, "(boiled & cooled)", 14, "middle")
    s += t(260, 180, "+", 36, "middle", "700")
    s += rect(290, 110, 160, 130, "#fff") + t(370, 165, "6 level", 20, "middle", "700") + t(370, 190, "teaspoons", 16, "middle") + t(370, 214, "SUGAR", 16, "middle", "700")
    s += t(480, 180, "+", 36, "middle", "700")
    s += rect(510, 110, 160, 130, "#fff") + t(590, 165, "½ level", 20, "middle", "700") + t(590, 190, "teaspoon", 16, "middle") + t(590, 214, "SALT", 16, "middle", "700")
    s += t(360, 315, "Stir until dissolved. Give small sips often. Make fresh each day.", 16, "middle", "600")
    s += t(360, 342, "Lightly salted rice water may be used instead of water (WHO).", 15, "middle")
    return svg(720, 370, s)

def d_canner():
    s = t(360, 30, "Pressure canner used as a steam sterilizer", 18, "middle", "700")
    s += rect(220, 90, 280, 230, "#cfd8dc", "#1f2a33", 3, 18) + rect(200, 70, 320, 30, "#90a4ae", "#1f2a33", 3, 8)
    s += line(360, 70, 360, 45, "#1f2a33", 6) + '<circle cx="420" cy="58" r="16" fill="#fff" stroke="#1f2a33" stroke-width="3"/>' + line(420, 58, 430, 48, "#c0392b", 3)
    s += rect(240, 280, 240, 20, "#8d6e63", "#1f2a33", 2, 3) + t(360, 274, "rack keeps items off the bottom", 13, "middle")
    s += '<path d="M232 300 L488 300 L488 315 L232 315 Z" fill="#5fb3e6"/>'
    for x in (280, 340, 400): s += rect(x, 170, 40, 90, "#fff", "#2f7fbf", 2, 3)
    s += t(360, 160, "instruments wrapped in clean cloth", 13, "middle")
    s += t(560, 60, "gauge: 15 psi ≈ 121 °C (250 °F)", 15, "start", "600") + arrow(556, 56, 438, 58)
    s += t(40, 200, "water in bottom", 14, "start") + t(40, 220, "(per canner manual)", 14, "start") + arrow(120, 228, 232, 306)
    s += rect(40, 335, 640, 36, "#fff6e0") + t(360, 359, "Vent steam first, then hold pressure for the full time; dry before opening wraps.", 15, "middle", "600")
    return svg(720, 380, s)

def d_birth():
    return flow([["1 · PREPARE", "Wash hands, clean surface, boiled string/ties and blade, warm cloths"],
                 ["2 · BABY BORN", "Dry baby at once, keep skin-to-skin on mother, cover both"],
                 ["3 · BREATHING?", "If not crying/breathing: rub back, clear mouth & nose, then give breaths"],
                 ["4 · CORD", "Tie in two places, cut between ties with boiled blade; never pull cord"],
                 ["5 · PLACENTA", "Wait for it to come out on its own; keep it to check it is complete"],
                 ["6 · AFTER", "Rub the womb firm, put baby to breast, watch for heavy bleeding"]], bh=70)

R = {
 1: "<b>Main risks:</b> hypothermia and frostbite most of the year; carbon monoxide from heaters in closed shelters; isolation (no outside help for weeks). <b>Plan:</b> wool and windproof layers, insulated sleeping systems, a rewarming plan (3.4), and a larger kit because resupply is slow. Bears and dog bites are real hazards around camps and food stores.",
 2: "<b>Main risks:</b> wet-cold hypothermia (it can happen above freezing in rain and wind), wound infection in damp conditions, earthquake crush injuries. <b>Plan:</b> keep dressings dry in sealed bags; practice splinting for earthquake injuries (2.4). Coastal shellfish may carry toxins after algal blooms — follow the Food guide.",
 3: "<b>Main risks:</b> blizzard cold injuries, summer heat, tornado debris wounds, farm-machinery injuries, rattlesnakes in the south and west. <b>Plan:</b> tourniquets and wound-packing material in every vehicle and shop; heat and cold kits by season.",
 4: "<b>Main risks:</b> cold snaps and ice falls (wrist and hip fractures), summer heat waves, ticks (Lyme disease) in woods and grass. <b>Plan:</b> do daily tick checks; keep splinting supplies; remove ticks by gripping close to the skin and pulling steadily.",
 5: "<b>Main risks:</b> deep cold and ice, chimney/heater carbon monoxide, ticks (Lyme is common in the Northeast), crowded-city disease spread. <b>Plan:</b> CO safety (see Fire &amp; Heating guide when available), tick checks, strict hand-washing and latrine distance (Sanitation guide).",
 6: "<b>Main risks:</b> heat and humidity (heat stroke, dehydration), hurricanes and floods (dirty wounds, waterborne diarrhea), venomous snakes (copperhead, cottonmouth, rattlesnakes, coral snake), fire ants. <b>Plan:</b> ORS supplies (3.1), clean every flood-water wound well (2.2), snakebite first aid (2.7).",
 7: "<b>Main risks:</b> severe heat, hurricanes, mosquitoes, flood wounds, coral snakes and rattlesnakes, marine stings. <b>Plan:</b> shade, water and ORS; mosquito nets and repellent; never close a flood-water wound tight.",
 8: "<b>Main risks:</b> extreme heat and dehydration, scorpions, rattlesnakes, very cold desert nights, few water sources. <b>Plan:</b> work early and late in the day; carry ORS ingredients; shake out boots and bedding; plan for cold nights too.",
 9: "<b>Main risks:</b> falls and fractures in steep terrain, altitude, sudden storms with hypothermia, wildfire smoke and burns, rattlesnakes at lower elevations. <b>Plan:</b> splints and a way to carry a casualty; boil water longer at altitude (see Water guide).",
 10: "<b>Main risks:</b> wildfire burns and smoke, earthquake crush injuries, heat inland, rattlesnakes. <b>Plan:</b> burn dressings and lots of clean water (2.6); masks or cloth against smoke; splinting supplies.",
 11: "<b>Main risks:</b> desert heat and dehydration, scorpions (some Mexican species are dangerous), rattlesnakes, scarce water. <b>Plan:</b> ORS and shade; shake out shoes and bedding; carry a casualty in the cool of the day.",
 12: "<b>Main risks:</b> heat, altitude in the central highlands, mosquito-borne illness in lowlands, diarrheal disease from unsafe water, earthquakes, venomous snakes and scorpions. <b>Plan:</b> treat all drinking water (Water guide), ORS supplies, mosquito nets.",
 13: "<b>Main risks:</b> hurricanes, flooding, heat, mosquito-borne disease, diarrheal disease (cholera has occurred in the region), venomous snakes in Central America. <b>Plan:</b> ORS — the WHO notes ORS successfully treats most cholera patients" + c(5) + "; mosquito nets; clean water.",
}

def body():
    b = []
    b.append('<div class="pb"></div>' + h2("howto", "How to use this guide"))
    b.append('<p>This is a beginner guide for caring for sick and injured people when there are <b>no hospitals, no doctors, no ambulances and no pharmacies</b>. Everything in it can be done by an ordinary person with a kit you put together now and supplies you can improvise later. It does not replace training — if you can still take a first-aid or CPR class before things go wrong, do it.</p>')
    b.append('<p>Small numbers in brackets like this ' + c(1) + ' point to the numbered sources at the end. Every source was saved as a PDF in the folder <b>Survival Info Sources/Medical/</b>. The single most useful book to print and keep is <b>Where There Is No Doctor</b> from Hesperian ' + c(1) + ', which is free online; its companions <b>Where There Is No Dentist</b> ' + c(2) + ' and <b>A Book for Midwives</b> ' + c(3) + ' cover teeth and childbirth in much more depth than this guide can.</p>')
    b.append(danger("Know your limits", "Some problems — a ruptured appendix, a deep chest or belly wound, a baby stuck in the birth canal, a severe head injury — cannot be fixed with first aid. In a grid-down world, your job is to keep the person alive, comfortable and clean, prevent infection, and give their body the best chance to heal. Red boxes mark things that can kill; amber boxes mark common mistakes; blue boxes are tips; green boxes are checklists."))
    b.append(table(["Priority", "What to learn first"], [
        ["1 · Today", "Stop bleeding (2.1), CPR and choking (1.3), shock (1.4)"],
        ["2 · This week", "Clean wounds (2.2), splint a limb (2.4), treat burns (2.6), make ORS (3.1)"],
        ["3 · This month", "Recognize infection (2.3), heat and cold illness (3.3–3.4), sterilize tools (4.4)"],
        ["4 · Long term", "Childbirth basics (4.1), dental care (4.2), study the Hesperian books (1–3)"]]))
    # Part 1
    b.append(part("p1", "Part 1", "First Steps in Any Emergency"))
    b.append(h2("kit", "1.1 Your medical kit and improvised supplies"))
    b.append('<p>Build a kit now while stores are open. Keep it in a waterproof box, and keep a smaller kit in every vehicle and go-bag. Write the date on anything that expires and rotate it.</p>')
    b.append(check("Core kit (build it now)", ["Tourniquets (commercial windlass type, 2 or more) and compressed gauze or plain rolled gauze for wound packing", "Sterile gauze pads, non-stick pads, rolled bandages, elastic bandages, triangular bandages (slings)", "Medical tape, adhesive bandages of all sizes, butterfly/strip closures", "Nitrile gloves (lots), safety glasses, face masks", "Tweezers, fine scissors, trauma shears, a sewing needle set, magnifier, headlamp", "Thermometer, a watch with a second hand, notebook and pencil (write down what you did and when)", "Malleable (SAM-type) splint or materials for splints; padding", "Oral rehydration salt packets, plus sugar and salt for home-made ORS (3.1)", "Over-the-counter pain/fever medicines you already know you tolerate, antihistamine, antidiarrheal, hydrocortisone cream, antibiotic ointment, clove oil for toothache", "Soap, plain unscented bleach, alcohol, a large pot with lid or a pressure canner for sterilizing (4.4)", "A printed copy of Where There Is No Doctor " + c(1) + " and this guide"]))
    b.append(h3x := '<h3>Improvised supplies</h3>')
    b.append(table(["Need", "Improvise with"], [
        ["Dressings", "Clean cotton cloth (sheets, T-shirts) boiled for several minutes, dried in the sun and stored in a clean sealed bag; sanitary pads make excellent absorbent dressings"],
        ["Bandages", "Strips of boiled cloth, pillowcases, socks with the toe cut off, plastic wrap over a dressing on a burn"],
        ["Splints", "Boards, sticks, rolled newspaper or magazines, cardboard folded in a U shape, a pillow for an ankle, the uninjured leg (buddy splint)"],
        ["Sling", "Triangle of cloth, a shirt pinned up, a belt"],
        ["Irrigation", "A clean plastic bottle with a small hole in the cap, or a syringe, to squirt clean water into a wound"],
        ["Stretcher", "Two poles through the sleeves of two or three buttoned coats, or a blanket rolled around two poles"],
        ["Tourniquet", "Only if no commercial one: a wide band of cloth (at least 1.5 in / 4 cm) tied around the limb with a stick twisted to tighten it. Thin cord or wire cuts the skin and fails"]]))
    b.append(h2("assess", "1.2 Checking an injured person (ABC)"))
    b.append('<p>Follow the same order every time so you never miss the thing that kills first. Massive bleeding can kill in minutes, so it is checked before breathing in modern trauma care ' + c(25) + '.</p>')
    b.append(fig(d_abc(), "<b>Figure 1.</b> The order of checks for any injured person."))
    b.append(tip("Write it down", "Record the time of injury, what you found, what you did (for example, the time a tourniquet was put on), pulse and breathing every 15 minutes, and how much the person drank and urinated. In a long emergency these notes guide every decision."))
    b.append(h2("cpr", "1.3 Not breathing, choking, heart attack"))
    b.append('<h3>CPR for an adult</h3>')
    b.append(steps(["Check the person responds. If not, and they are not breathing normally (gasping does not count), start CPR " + c(22) + ".",
        "Kneel beside them. Put the heel of one hand on the center of the chest, between the nipples, other hand on top.",
        "Push hard and fast: about 2 inches (5 cm) deep, 100–120 times a minute, letting the chest come all the way back up " + c(22) + ".",
        "If you are trained, give 2 rescue breaths after every 30 compressions; if not, do hands-only compressions.",
        "Keep going until the person breathes, you are too exhausted to continue, or it is clearly hopeless."]))
    b.append(caution("CPR without a hospital", "CPR keeps blood moving but rarely restarts a heart without a defibrillator and hospital care. It is most worth doing after drowning, lightning, suffocation or a short choking episode, especially in children. Decide as a group, ahead of time, how long you will continue."))
    b.append('<h3>Choking</h3>')
    b.append('<p>If the person can cough or speak, let them cough. If they cannot breathe, speak or cough, stand behind them, make a fist just above the navel, grab it with your other hand and give quick inward-and-upward thrusts until the object comes out ' + c(23) + '. If they become unconscious, lower them to the ground and begin CPR; look in the mouth for the object before giving breaths.</p>')
    b.append('<h3>Heart attack</h3>')
    b.append('<p>Warning signs include chest pressure or pain that may spread to the arm, jaw or back, shortness of breath, sweating, nausea and lightheadedness ' + c(24) + '. Have the person rest sitting up, loosen tight clothing, and keep them calm. MedlinePlus notes that many experts recommend chewing and swallowing an aspirin (a full 325 mg dose or an 81 mg low dose) — but only for someone who is not allergic to aspirin and has no condition that makes aspirin dangerous for them ' + c(24) + '. Begin CPR if they stop breathing.</p>')
    b.append(h2("shock", "1.4 Shock"))
    b.append('<p>Shock means the body is not getting enough blood flow. It follows heavy bleeding, bad burns, severe diarrhea, serious infection or severe allergic reactions. Signs: pale, cold, clammy skin; fast weak pulse; fast breathing; confusion, anxiety or fainting; thirst ' + c(10) + '.</p>')
    b.append(steps(["Stop any bleeding first.", "Lay the person flat. If there is no head, neck, back or leg injury, raise the feet about 12 inches (30 cm) " + c(10) + ".", "Keep them warm with blankets under and over them — the ground steals heat.", "Do not give food or drink if they are vomiting, unconscious or likely to need surgery; otherwise small sips of ORS (3.1) help when shock is from fluid loss.", "Check breathing and pulse often."]))
    # Part 2
    b.append(part("p2", "Part 2", "Injuries"))
    b.append(h2("bleed", "2.1 Stopping serious bleeding"))
    b.append('<p>Bright red spurting blood, blood pooling on the ground, or blood soaking through clothing is life-threatening. Act within seconds. The American College of Surgeons\' <b>Stop the Bleed</b> program teaches three tools: <b>pressure, wound packing and tourniquets</b> ' + c(25) + '.</p>')
    b.append(steps(["Put on gloves if you have them (a plastic bag works) — but do not delay.",
        "<b>Press:</b> put a dressing or cloth on the wound and press down hard with both hands, using your body weight. Do not lift to look " + c(8) + ".",
        "<b>Pack:</b> for a deep wound in the armpit, groin, neck or a large muscle, stuff gauze or clean cloth firmly into the wound, right down to where the blood comes from, then press hard on top " + c(25) + ".",
        "<b>Tourniquet:</b> for life-threatening bleeding from an arm or leg that pressure does not control, place a tourniquet high and tight above the wound and tighten until the bleeding stops (Figure 2) " + c(25) + ".",
        "If blood soaks through, add more cloth on top — do not remove the first layer " + c(8) + ".",
        "Once bleeding stops, bandage firmly and treat for shock (1.4)."]))
    b.append(fig(d_tourniquet(), "<b>Figure 2.</b> Tourniquet placement. A properly tightened tourniquet hurts; that is normal. Do not loosen it to 'check' — that can restart deadly bleeding."))
    b.append(danger("Tourniquets", "A tourniquet saves a life at the risk of a limb. Use one only for bleeding that will kill. Never put it over a joint. Without a hospital, the decision to loosen it later (to see if pressure and packing can now control the bleeding) is a hard judgment call; Where There Is No Doctor covers serious bleeding in its first-aid chapter " + c(1) + ". Note the time it was applied."))
    b.append(h2("wound", "2.2 Cleaning and closing wounds"))
    b.append('<p>When there are no antibiotics or hospitals on hand, <b>infection is one of the biggest dangers of any wound</b>. Cleaning is the most important thing you can do.</p>')
    b.append(steps(["Wash your hands with soap and water.", "Stop bleeding with pressure.",
        "Rinse the wound with lots of clean water — drinkable, boiled-and-cooled, or disinfected water (see the Water guide and " + c(26) + "). Squirt it in with force from a bottle or syringe to wash out dirt; MedlinePlus advises rinsing a puncture under running water for 5 minutes " + c(9) + ".",
        "Wash the skin around the wound with soap; pick out dirt and splinters with boiled tweezers " + c(9) + ".",
        "Cover with a clean dressing. Change it every day, or sooner if it is wet or dirty."]))
    b.append('<h3>Should you close it?</h3>')
    b.append('<p>Closing a dirty wound traps germs inside and can cause a deadly infection. Hesperian advises closing only wounds that are <b>clean and recent</b>, and leaving bites, punctures, crush injuries and dirty wounds <b>open</b> so they can drain ' + c(1) + '. Close a clean, gaping cut with tape strips (butterfly closures) pulling the edges together; if it needs stitches and you have never sutured, an open wound kept clean usually heals well, just with a wider scar.</p>')
    b.append(caution("Punctures and tetanus", "Deep, dirty puncture wounds (nails, thorns, animal bites) carry a risk of tetanus " + c(9) + ". MedlinePlus lists not having had a tetanus shot in the last 10 years as a reason to get care " + c(9) + " — so get a booster now while clinics are open, for every member of your group."))
    b.append(h2("infect", "2.3 Wound infection"))
    b.append(table(["Sign", "What it means"], [
        ["Redness, swelling, heat and pain getting <b>worse</b> after the first 2 days", "Local infection"],
        ["Pus, a bad smell", "Infection; the wound must drain"],
        ["Red streaks going up the limb, swollen tender lumps in the armpit or groin", "Infection is spreading — serious"],
        ["Fever, chills, fast heartbeat, confusion", "Infection may be in the blood — life-threatening"],
        ["Dark, bubbly, foul skin with crackling under it", "Gas gangrene — extreme emergency"]]))
    b.append(steps(["Open the wound if it was closed, so pus can drain. Remove tape strips or stitches over the infected part.", "Soak or apply hot wet cloths (as hot as is comfortable, not burning) for 20 minutes several times a day " + c(1) + ".", "Keep the part raised and resting.", "Keep cleaning with boiled water and changing dressings.", "Antibiotics, if you have them, are for spreading infection, fever or deep wounds; Where There Is No Doctor has dosing tables and warnings " + c(1) + "."]))
    b.append(h2("fract", "2.4 Fractures and splinting"))
    b.append('<p>Signs of a broken bone: pain, swelling, bruising, a bent or out-of-place limb, inability to use it, or bone through the skin ' + c(11) + '. Treat any suspected fracture as broken.</p>')
    b.append(steps(["Check circulation below the injury (color, warmth, feeling, pulse).", "Cover any open wound with a clean dressing. Do not push bone back in " + c(11) + ".",
        "Splint it as you found it, unless circulation is cut off (see the caution below).", "The splint must reach past the joint above and the joint below the break " + c(12) + ". Pad it well.",
        "Tie it on firmly but not tight; recheck circulation after tying and every hour " + c(12) + ".", "Raise the limb and apply cold (cold water cloths) to reduce swelling."]))
    b.append(fig(d_splint(), "<b>Figure 3.</b> A forearm splint. The same rule — past the joint above and below — applies to every limb."))
    b.append(caution("When there is no hospital", "If the hand or foot below a badly bent break is cold, blue and pulseless, gentle, steady pulling along the line of the limb to straighten it may restore circulation; Where There Is No Doctor describes how to set simple fractures and make casts " + c(1) + ". Thigh-bone (femur), pelvis, spine and skull fractures are very serious; keep the person still and lying flat, and move them on a rigid stretcher."))
    b.append('<p><b>Healing time.</b> Simple arm fractures need several weeks of immobilization; leg fractures longer. Keep the person fed, hydrated and moving the uninjured parts to prevent weakness and blood clots.</p>')
    b.append(h2("disloc", "2.5 Sprains and dislocations"))
    b.append('<p><b>Sprains:</b> rest, cold cloths, an elastic wrap for support, and raising the limb. A sprain that cannot bear weight after several days may be a fracture — splint it.</p>')
    b.append('<p><b>Dislocations</b> (a joint knocked out of place — shoulder, finger, kneecap) look deformed and are very painful. MedlinePlus advises splinting in the position found and not trying to put it back ' + c(13) + '. Where no help will ever arrive, Where There Is No Doctor shows a method for putting a dislocated shoulder back: the person lies face down on a table with the arm hanging down, sometimes with a weight tied to the wrist, and relaxes until the joint slips back in ' + c(1) + '. Afterward, keep it in a sling for several weeks. Stop if it causes severe pain or numbness.</p>')
    b.append(h2("burns", "2.6 Burns"))
    b.append(steps(["Stop the burning: smother flames, remove hot clothing and jewelry (not clothing stuck to the skin).",
        "Cool the burn with cool — not ice — water. MedlinePlus says to keep a minor burn under cool water for at least 5 to 30 minutes " + c(14) + ".",
        "Cover loosely with a clean, dry, non-stick dressing or clean plastic wrap.", "Do not break blisters. Do not put butter, oil or grease on a burn.",
        "Give lots of fluids (ORS) to anyone with a large burn — they lose much water through the burned skin.", "Watch closely for infection (2.3)."]))
    b.append(table(["Depth", "Looks like", "Care"], [
        ["Superficial (1st degree)", "Red, painful, no blisters (like sunburn)", "Cool water, aloe gel (4.3), keep clean"],
        ["Partial thickness (2nd degree)", "Blisters, red/wet, very painful", "Cool, cover, don't pop blisters; change dressings daily"],
        ["Full thickness (3rd degree)", "White, brown or black, leathery; may not hurt", "Cover, fluids, treat for shock; very high infection risk"]]))
    b.append(danger("Burns that kill", "Burns to the face or airway (singed nose hair, hoarse voice, soot in the mouth), burns covering a large part of the body, and electrical burns are life-threatening " + c(14) + ". Keep the person warm, give fluids if they can swallow, and watch breathing."))
    b.append(h2("bites", "2.7 Bites and stings"))
    b.append('<h3>Snakebite</h3>')
    b.append('<p>Keep the person calm and still, remove rings and tight clothing, and keep the bitten part at heart level in a loose splint ' + c(19) + '. MedlinePlus is clear on what <b>not</b> to do: no tourniquet, no ice, no cutting the bite, no sucking out venom ' + c(19) + '. Carry the person rather than letting them walk if you can. Most bites by North American snakes are survivable with rest and care.</p>')
    b.append('<h3>Bee and insect stings</h3>')
    b.append('<p>Scrape a bee stinger out sideways with a fingernail or card; wash the area and apply cold ' + c(20) + '. Watch for a severe allergic reaction — swelling of the face or throat, wheezing, fainting — which needs epinephrine if anyone in your group has an auto-injector.</p>')
    b.append('<h3>Animal bites</h3><p>Wash every animal bite very thoroughly with soap and running water for several minutes, leave it open, and watch for infection. Any wild animal acting strangely, or a bat, may carry rabies; once symptoms appear, rabies is almost always fatal, so avoiding such animals is your best defense ' + c(1) + '.</p>')
    b.append(h2("eye", "2.8 Eye injuries"))
    b.append(steps(["Wash your hands before touching the eye or eyelid " + c(35) + ".", "Tiny objects like sand often wash out with blinking and tears. Don\'t rub the eye or squeeze the lids " + c(35) + ".", "In good light, have the person look up, down and side to side. Pull the lower lid down to look under it; to check the upper lid, fold it gently over a clean cotton swab while the person looks down " + c(35) + ".", "Flush an object off the lid or eye with clean water, or lift it from the lid with a second moist swab " + c(35) + "."]))
    b.append(danger("Objects stuck in the eye, chemicals in the eye", "Never pull out an object stuck in the eye; cover both eyes loosely (a paper cup over the injured eye) so they move less. For chemicals, flush the eye with large amounts of clean water right away and keep flushing for a long time " + c(35) + "."))
    b.append(h2("spine", "2.9 Neck and back injuries"))
    b.append('<p>Suspect a spinal injury after falls, vehicle crashes, diving into shallow water or a heavy blow, especially with neck or back pain, numbness, tingling or weakness. MedlinePlus says: do not move the person unless it is absolutely necessary (for example, fire or to help them breathe); hold the head and neck in the position found; do not straighten, bend or twist the neck; and do not let them get up and walk ' + c(37) + '.</p>')
    b.append(steps(["Kneel at the head and hold it still in line with the body.", "If you must roll the person (vomiting, choking on blood), use at least two people and keep head, neck and back in line as you roll " + c(37) + ".", "If the person must be moved, put them on a rigid board or door, pad both sides of the head (rolled blankets) and tie them on.", "If they are unresponsive and not breathing, do chest compressions without changing the position of the neck " + c(37) + "."]))
    b.append(h2("elec", "2.10 Electrical injuries"))
    b.append(steps(["Turn off the power first if you can do so safely — unplug, pull the fuse, or switch off the breaker. Turning off the appliance alone may not stop the current " + c(36) + ".", "Do not go near anyone touching downed high-voltage lines " + c(36) + ".", "If the current can't be turned off, stand on something dry and push the person away with a dry non-conducting object like a broom, chair or rubber mat — never anything wet or metal " + c(36) + ".", "Check breathing; start CPR if needed (1.3) " + c(36) + ".", "Treat burns (2.6): there may be a small entry and exit burn with deep damage between."]))
    b.append(caution("Generators and back-feeding", "A generator connected to house wiring without a transfer switch can energize 'dead' power lines and kill someone working on them. See the Electricity guide."))
    b.append(h2("ivy", "2.11 Poison ivy, oak and sumac"))
    b.append('<p>The plant oil soaks into skin quickly, so wash the skin with soap and warm water, ideally within 30 minutes, and scrub under the fingernails ' + c(38) + '. Wash clothing, shoes and tools, and bathe pets that touched the plants ' + c(38) + '. Cool compresses ease itching; calamine lotion and hydrocortisone cream help ' + c(38) + '. A rash around the eyes, face or genitals, or trouble breathing after burning the plants, is serious.</p>')
    b.append(h2("head", "2.12 Head injuries"))
    b.append('<p>Symptoms of a head injury can appear right away or develop slowly over hours or days; the head may look fine while bleeding or swelling builds inside the skull ' + c(39) + '. Treat any serious head injury as a possible neck injury too (2.9) ' + c(39) + '.</p>')
    b.append(danger("Danger signs after a head injury " + c(39), "Very sleepy; behaving strangely or speech that makes no sense; severe headache or stiff neck; a seizure; pupils of unequal size; unable to move an arm or leg; losing consciousness, even briefly; vomiting more than once."))
    b.append(steps(["Check airway, breathing and circulation; start CPR if needed " + c(39) + ".", "Keep the person lying still with head and shoulders slightly raised if there is no neck injury; keep them warm.", "Control scalp bleeding with firm pressure using a clean cloth. If you suspect a skull fracture (soft or sunken spot, fluid from nose or ears), do not press directly on the wound or remove debris; cover it with clean gauze " + c(39) + ".", "Keep watching breathing and alertness, and keep checking for the danger signs above over the following hours and days, since symptoms can appear late " + c(39) + ". Write down changes.", "Rest from hard work for days afterward; a second blow before healing is dangerous."]))
    b.append(h2("allergy", "2.13 Severe allergic reactions"))
    b.append('<p>Anaphylaxis is a sudden, severe allergic reaction; MedlinePlus warns it can worsen very quickly and lead to death within 15 minutes without treatment ' + c(40) + '. Warning signs include trouble breathing or wheezing, swelling of the face, eyes or tongue, hives all over, dizziness, vomiting, and a very hoarse or whispered voice or coarse breathing sounds, which warn of throat swelling ' + c(40) + '.</p>')
    b.append(steps(["Check airway and breathing; start CPR if needed " + c(40) + ".", "If the person has an epinephrine auto-injector, help them use it right away.", "Remove the cause if you can — scrape out a bee stinger " + c(40) + ".", "Lay them flat with legs raised (unless breathing is easier sitting up) and keep them warm, as for shock (1.4).", "For mild reactions (a few hives, itching): calm the person, avoid the allergen, apply cool compresses and hydrocortisone cream; antihistamines help " + c(40) + "."]))
    b.append(tip("Stock up", "Anyone in your group with a known severe allergy should keep several epinephrine auto-injectors (check expiry dates) and everyone should know where they are."))
    # Part 3
    b.append(part("p3", "Part 3", "Illness & Environment"))
    b.append(h2("dehyd", "3.1 Dehydration and home-made ORS"))
    b.append('<p>Diarrhea, vomiting, heat and fever all drain water and salts. Dehydration kills small children and elders fastest.</p>')
    b.append(table(["Signs of dehydration " + c(15)], [["Thirst, dry mouth, little or dark urine"], ["Sunken eyes; in a baby, a sunken soft spot on the head"], ["Skin that stays tented when pinched"], ["Dizziness, weakness, confusion; fast pulse"]]))
    b.append('<p><b>Oral rehydration solution (ORS)</b> is a mix of water, sugar and salt that the gut absorbs even during diarrhea. If you have WHO ORS packets, mix one in 1 litre of clean water. If not, the WHO gives this home recipe ' + c(5) + ':</p>')
    b.append(fig(d_ors(), "<b>Figure 4.</b> Home-made ORS. Measure carefully: too much salt is harmful. Adding a little orange juice or mashed banana adds potassium " + c(6) + "."))
    b.append(steps(["Give small sips every few minutes — a spoonful at a time for a child who is vomiting.", "Keep breastfeeding babies.", "Rice water, thin cereal gruels and soups also help rehydrate " + c(6) + ".", "Continue until urine is pale and frequent again."]))
    b.append(h2("diarr", "3.2 Diarrhea and vomiting"))
    b.append('<p>Most diarrhea in disasters comes from dirty water, dirty hands and flies. Prevention is in the Water guide and the Sanitation guide. Treatment is mainly <b>fluids and food</b>: keep giving ORS and keep eating soft foods as soon as possible ' + c(7) + '.</p>')
    b.append(danger("Danger signs with diarrhea", "Blood in the stool, high fever, large amounts of 'rice-water' stool (possible cholera), a baby or elder who cannot drink, or signs of severe dehydration. Push ORS hard and keep the person isolated, with their waste kept away from water sources " + c(5) + "."))
    b.append(h2("heat", "3.3 Heat illness"))
    b.append(table(["Condition", "Signs", "What to do"], [
        ["Heat cramps", "Painful muscle cramps after sweating", "Rest in shade, drink ORS or salted fluids " + c(16)],
        ["Heat exhaustion", "Heavy sweating, pale clammy skin, headache, nausea, weakness", "Shade, lie down, loosen clothes, cool wet cloths, fluids " + c(16)],
        ["Heat stroke", "Hot skin, confusion, collapse, seizures; may stop sweating", "EMERGENCY: cool fast — wet the whole body and fan, cool water on neck, armpits, groin " + c(16)]]))
    b.append(h2("cold", "3.4 Hypothermia and frostbite"))
    b.append('<p><b>Hypothermia</b> (body too cold): shivering, clumsiness, slurred speech, confusion; in severe cases shivering stops ' + c(17) + '. Move the person out of wind and wet, replace wet clothes with dry ones, insulate them from the ground, cover the head, and warm the trunk first (skin-to-skin in a sleeping bag works). If they cannot be brought indoors, get them out of the wind and use a blanket to insulate them from the cold ground ' + c(17) + '. Move a severely cold person with as little exertion as possible ' + c(17) + '.</p>')
    b.append('<p><b>Frostbite:</b> numb, white or grayish-yellow, hard skin. Treat hypothermia first. Do not rub the area. If you can keep it from refreezing, soak it in warm (never hot) water — MedlinePlus gives 104–108 °F (40–42.2 °C) for 15–30 minutes ' + c(18) + '. If refreezing is likely, wait until you reach a warm, safe place, because thawing and refreezing does more damage ' + c(18) + '.</p>')
    # Part 4
    b.append(part("p4", "Part 4", "Special Situations"))
    b.append(h2("birth", "4.1 Emergency childbirth basics"))
    b.append('<p>Most births go well without help, and the helper\'s main jobs are <b>cleanliness, warmth, patience and watching for danger signs</b>. Anyone who may attend a birth should read <b>A Book for Midwives</b> ' + c(3) + ' and the WHO manual ' + c(4) + '.</p>')
    b.append(fig(d_birth(), "<b>Figure 5.</b> The basic steps of an uncomplicated birth."))
    b.append(steps(["Let labor progress on its own; encourage walking, drinking and urinating in early labor " + c(3) + ".", "When the head appears, support it gently; do not pull on the baby.", "Dry and warm the baby right away and place it skin-to-skin on the mother.", "Tie and cut the cord with boiled string and a boiled blade " + c(3) + ".", "The placenta usually follows within a short time. Never pull hard on the cord " + c(4) + ".", "After the placenta, rub the top of the womb (through the belly) until it feels firm, and put the baby to the breast — both help the womb clamp down and slow bleeding " + c(3) + "."]))
    b.append(danger("Danger signs in childbirth", "Heavy bleeding (soaking cloths quickly), labor that goes on for many hours without progress, a baby coming arm or bottom first, the cord coming out before the baby, fits (seizures), high fever after birth. These are the leading killers of mothers; A Book for Midwives and the WHO manual describe what can be done " + c(3, 4) + "."))
    b.append(h2("dental", "4.2 Dental emergencies"))
    b.append(table(["Problem", "What to do"], [
        ["Toothache", "Rinse with warm salt water; a little clove oil on cotton against the tooth eases pain " + c(2)],
        ["Swollen face / abscess", "Warm salt water rinses; this is a serious infection that can spread — Where There Is No Dentist describes treatment " + c(2)],
        ["Knocked-out tooth", "Hold by the crown only, do not scrub the root; put it back in the socket and bite on cloth, or keep it in milk or saliva " + c(21)],
        ["Broken tooth", "Rinse, cold cloth for swelling, protect sharp edges with soft wax " + c(21)],
        ["Prevention", "Brush twice a day (a chewed twig works), floss, limit sugar — it is the best dental care when no dentist exists " + c(2)]]))
    b.append(h2("herbs", "4.3 Herbal remedies — with cautions"))
    b.append('<p>Plants can ease some symptoms, but most herbal claims are weakly tested and some herbs are harmful. Use this table from the U.S. NIH National Center for Complementary and Integrative Health ' + c(28) + ' as a guide to <b>what is known and what to watch for</b>. Never use an herb you cannot identify with certainty (see the Food guide for plant identification).</p>')
    b.append(table(["Herb", "Common use", "What the evidence says", "Cautions"], [
        ["Aloe vera gel (leaf inside)", "Minor burns, skin", "Topical gel may help some skin conditions; evidence for burns is mixed " + c(29), "Oral aloe latex can cause cramps and diarrhea " + c(29)],
        ["Garlic", "Infections, heart", "Not proven to treat infections " + c(30), "May increase bleeding risk, especially with blood thinners " + c(30)],
        ["Tea tree oil", "Skin fungus, acne", "Some evidence for acne and fungal skin infections " + c(31), "<b>Poisonous if swallowed.</b> Can irritate skin " + c(31)],
        ["Chamomile", "Upset stomach, sleep", "Limited evidence " + c(32), "Allergic reactions in people allergic to ragweed-family plants " + c(32)],
        ["Peppermint oil", "Gut cramps (IBS), headache", "Some evidence for IBS symptoms " + c(33), "Can cause heartburn " + c(33)],
        ["Echinacea", "Colds", "Mixed evidence " + c(34), "Allergic reactions possible " + c(34)]]))
    b.append(caution("Herbs and pregnancy, children and medicines", "Many herbs have not been tested in pregnancy, nursing or small children, and some interact with medicines " + c(28) + ". When in doubt, don't."))
    b.append(h2("steril", "4.4 Cleaning and sterilizing instruments"))
    b.append('<p>Dirty instruments spread infection from person to person. Always <b>clean first, then disinfect or sterilize</b>: scrub off all blood and dirt with soap and a brush, rinse, then use heat. Germs hide under dried blood, so cleaning matters as much as heat.</p>')
    b.append(table(["Method", "How", "Notes"], [
        ["Boiling", "Fully cover cleaned instruments in water, bring to a hard boil and keep boiling with the lid on", "Disinfection, not true sterilization — some bacterial spores survive boiling"],
        ["Pressure canner (steam)", "Rack, water per manual, vent steam, hold 15 psi; CDC uses 121 °C (250 °F) for 30 min for wrapped items in gravity steam sterilizers " + c(27), "The best sterilizing method available at home"],
        ["Dry oven", "Clean, dry metal tools in an oven; CDC lists dry heat of 170 °C (340 °F) for 60 minutes " + c(41), "Only for metal and glass"],
        ["Flame", "Hold a needle or blade tip in a flame until it glows red", "Quick for needles and splinter removal; dulls blades"],
        ["Chemical", "Soak in alcohol or diluted bleach", "Disinfects surfaces and tools but is not sterilization; rinse with boiled water"]]))
    b.append(fig(d_canner(), "<b>Figure 6.</b> A pressure canner can serve as a steam sterilizer. Follow the canner's own manual for water level and safe venting."))
    b.append(tip("Hand-washing", "Wash hands with soap and clean water for at least 20 seconds before and after caring for anyone, and after using the latrine. A tippy-tap (hanging jug tipped by a foot lever) saves water — see the Sanitation guide."))
    # Part 5
    b.append(part("p5", "Part 5", "Region-by-Region Health Risks"))
    b.append('<p>The same first aid works everywhere, but each region has its own most likely injuries and illnesses. Stock and train for yours.</p>')
    b.append(regions_html(R))
    # appendix
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Situation", "First action"], [
        ["Spurting bleeding", "Hard pressure → pack → tourniquet on a limb (2.1)"],
        ["Not breathing", "CPR: 100–120 compressions a minute, 2 in (5 cm) deep (1.3)"],
        ["Choking", "Abdominal thrusts (1.3)"],
        ["Pale, cold, clammy", "Shock: lay flat, legs up, keep warm (1.4)"],
        ["Any wound", "Flush with lots of clean water; leave dirty wounds open (2.2)"],
        ["Burn", "Cool water 5–30 min, cover loosely (2.6)"],
        ["Diarrhea", "ORS: 1 L water + 6 level tsp sugar + ½ level tsp salt (3.1)"],
        ["Hot, confused", "Heat stroke: cool the whole body now (3.3)"],
        ["Cold, confused", "Hypothermia: dry, insulate, warm the trunk (3.4)"],
        ["Instruments", "Scrub, then boil or (best) pressure-canner steam (4.4)"]]))
    b.append('<p class="small">This guide is general information for emergency situations when no medical care exists. It is not a substitute for medical training or care. When doctors, clinics or hospitals are available, use them. All sources were checked in November 2026.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Medical & First Aid", "Survival Info<br>Medical &amp;<br>First Aid",
          "Beginner first aid and long-term care when there are no doctors or hospitals: bleeding, wounds, fractures, burns, infection, dehydration, childbirth, teeth, herbs and sterilizing — region by region across North America.",
          "Medical & First Aid", TOC, cover_art(), "Water · Food · Electricity · Concrete · Tools · House · Bunkers")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Medical.pdf")
