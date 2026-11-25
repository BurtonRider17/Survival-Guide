#!/usr/bin/env python3
"""Build Survival_Info_Index.pdf — the series index. Re-run when guides are added."""

from __future__ import annotations

import datetime
import html
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/workspace/survival-info")
HERE = Path(__file__).resolve().parent
OUT_PDF = ROOT / "Survival_Info_Index.pdf"
HTML = HERE / "index.html"
PNG_DIR = HERE / "png"

# Last-updated date shown in the index. Change this when you rebuild after a
# new guide is added.
LAST_UPDATED = "November 24, 2026"

# Add a dict here when a new guide is finished. Page counts are read from the
# PDF at build time with pdfinfo.
GUIDES = [
    {
        "filename": "Survival_Info_Water.pdf",
        "title": "Survival Info, Vol. 1: Water",
        "short": "Water",
        "summary": (
            "This beginner volume covers finding, treating, storing, and producing safe drinking water "
            "during a long-term grid-down disaster anywhere in North America. It starts with daily water "
            "needs, signs of dehydration, and field priorities, then shows how to find water from terrain, "
            "springs, rain, snow, solar stills, seeps, and household sources such as a water-heater tank. "
            "Treatment methods include boiling, filtration, EPA and CDC bleach doses, iodine, SODIS solar "
            "disinfection, and distillation, with a clear comparison of what each method can and cannot remove. "
            "Long-term chapters cover wells, rainwater cisterns, and spring boxes. Section 6 gives step-by-step "
            "instructions for building a large tank and pump system to restore running water to a house, including "
            "basic hot water, winterizing, and troubleshooting. A region-by-region guide runs from the Arctic to "
            "the Caribbean, and the sources are listed at the end."
        ),
    },
    {
        "filename": "Survival_Info_Food.pdf",
        "title": "Survival Info, Vol. 1: Food",
        "short": "Food",
        "summary": (
            "This companion beginner volume covers getting, growing, and preserving food through a long-term "
            "grid-down disaster. It opens with calories, nutrition priorities, and rationing, then a foraging "
            "section with a photo guide to beginner plants and their deadly lookalikes, a temperate North American "
            "foraging calendar, and insects. Fishing, trapping, hunting, field dressing, and food-safety rules "
            "follow, including cook temperatures for wild meat. Long-term production covers calorie crops, the "
            "Three Sisters, seed saving, chickens, and rabbits. Preservation includes drying, smoking, salting, "
            "pemmican, water-bath and pressure canning, fermenting, root cellars, freezing, grain storage, pest "
            "control, and a shelf-life table. A region-by-region guide, photo credits, and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Electricity.pdf",
        "title": "Survival Info, Vol. 1: Electricity & Fuel",
        "short": "Electricity",
        "summary": (
            "This volume is about keeping a household in power and fuel after the grid is gone. Part 1 covers "
            "electrical units, load sizing, DC versus AC, and safety — shock, arc flash, batteries, and carbon "
            "monoxide. Part 2 is the faster path: salvaged solar, battery banks, inverters, small wind, "
            "thermoelectric generators, generators, and non-electric heat and light. The two main long-term "
            "projects are Part 3, building a micro-hydro plant general enough for any creek (head and flow, "
            "intake and penstock, turbines, generators, wiring, freeze protection, and a worked example), and "
            "Part 4, making biodiesel from waste oil and oilseed crops, including titration, quality testing, "
            "methanol and lye, straight vegetable oil, cold-weather gelling, and wood gasification. A "
            "region-by-region guide and a quick-reference sheet close the book."
        ),
    },
    {
        "filename": "Survival_Info_Concrete.pdf",
        "title": "Survival Info, Vol. 1: Concrete & Masonry",
        "short": "Concrete",
        "summary": (
            "This volume is about turning a camp into a homestead with concrete, mortar, plaster, brick, and "
            "earth construction. It explains binders, aggregates, mix ratios, expected strength, and safety — "
            "cement and lime burns, silica dust, and kiln gases. Parts 2 and 3 cover salvaging cement, lime, "
            "sand, gravel, and steel, then making binders from scratch: finding limestone, burning and slaking "
            "lime, pozzolans and Roman-style concrete, hydraulic lime, and gypsum. Part 4 is brick and block "
            "making — clay testing, adobe versus fired brick, clamp kilns, compressed earth blocks, and bonds. "
            "Part 5 covers rammed earth, cob, adobe, earthbags, and dry stone without cement. Hands-on chapters "
            "cover mixing, forms, curing, and projects such as well rings, cisterns, footings, slabs, root cellars, "
            "and stove bases, then the masonry side of a small house. A region-by-region guide and sources finish "
            "the volume."
        ),
    },
    {
        "filename": "Survival_Info_Tools.pdf",
        "title": "Survival Info, Vol. 1: Tools & Blacksmithing",
        "short": "Tools",
        "summary": (
            "This volume is the foundation for every other guide: how to get, keep, and eventually make the tools "
            "a homestead needs. It starts with what to stockpile or salvage and how to care for tools — "
            "sharpening, rust prevention, rehafting, and saw setting and filing. Part 3 covers primitive and "
            "improvised tools: knapping, bone and antler, wood tools, cordage, a shaving horse, and a spring-pole "
            "lathe. The main project is blacksmithing: forge types and fuels, a brake-drum forge, charcoal making, "
            "anvils and tongs, identifying salvaged steel, heating colors, basic forging, forge welding, heat "
            "treating, and shop projects. Later parts cover cold working, salvage welding, woodworking joinery "
            "and green wood, and shop safety, including burns, carbon monoxide, zinc fumes, and quench-oil fires. "
            "A region-by-region guide points to local wood, steel, and stone."
        ),
    },
    {
        "filename": "Survival_Info_House.pdf",
        "title": "Survival Info, Vol. 1: House Building",
        "short": "House",
        "summary": (
            "This volume walks from an emergency shelter to a permanent small house. Part 1 covers the first "
            "night, site selection, sizing a cabin (including a 16×24 ft plan), and passive solar orientation. "
            "Part 2 covers hand tools, felling, and the hazards of salvaging abandoned buildings — asbestos, lead, "
            "and collapse. Foundations include frost depth by region. Wall systems compare log, timber frame, "
            "stick framing, cordwood, straw bale, cob, adobe, earthbag, rammed earth, and stone by climate. Later "
            "parts cover floors, roof framing and pitch, roofing, gutters and rainwater catchment, doors and "
            "windows, insulation, and moisture control. Heating and cooking include wood stoves, chimney safety, "
            "rocket mass heaters, and lighting without power. Sanitation covers outhouses, composting toilets, "
            "and greywater. A region-by-region guide and pointers to the Concrete and Water volumes close the book."
        ),
    },
    {
        "filename": "Survival_Info_Bunkers.pdf",
        "title": "Survival Info, Vol. 1: Bunkers of North America",
        "short": "Bunkers",
        "summary": (
            "This is a sourced directory of Cold War bunkers, missile silos, hotel and school shelters, private "
            "shelter communities, and bunker properties for sale across North America, plus a do-it-yourself "
            "guide to judging and restoring a degraded bunker. Part 1 covers 107 sites in the United States "
            "(including Puerto Rico), Canada, Mexico, Panama, Costa Rica, and Cuba. Every site has a detail card "
            "with published capabilities (power, water, hydroponics, entertainment, and other fields), an address, "
            "GPS coordinates, the nearest Interstate or freeway exit, and the straight-line distance in miles. "
            "Status includes museums, active government sites, closed facilities, and listings; sold properties "
            "stay in the guide, marked sold. Facts were checked in November 2026 and are not estimated when a "
            "source is silent. Part 2 covers field testing, bad air, confined-space entry, PPE, and hazards such "
            "as lead, asbestos, mold, hantavirus, PCBs, fuel leaks, radon, and structural failure, then a "
            "restoration sequence for dewatering, ventilation, power, water, and fire safety, and do-it-yourself "
            "repair of cracked or spalling concrete and rusted steel. An appendix lists "
            "the sources. Listings are checked monthly; new ones are added to the guide."
        ),
    },
    {
        "filename": "Survival_Info_Medical.pdf",
        "title": "Survival Info: Medical & First Aid",
        "short": "Medical",
        "summary": (
            "A beginner guide to caring for the sick and injured when there are no doctors, hospitals, or pharmacies. "
            "It covers building a medical kit and improvising supplies, the order of checks for an injured person, "
            "CPR, choking, and shock, then stopping serious bleeding with pressure, wound packing, and tourniquets. "
            "Wound cleaning, when to leave a wound open, infection signs, splinting fractures, sprains and "
            "dislocations, burns, and snake, insect, and animal bites follow. Illness chapters cover dehydration "
            "with the WHO home-made oral rehydration recipe, diarrhea, heat illness, hypothermia, and frostbite. "
            "Special situations include emergency childbirth basics and danger signs, dental emergencies, herbal "
            "remedies with NIH evidence and cautions, and cleaning and sterilizing instruments with boiling or a "
            "pressure canner. A region-by-region list of health risks and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Sanitation.pdf",
        "title": "Survival Info: Sanitation & Hygiene",
        "short": "Sanitation",
        "summary": (
            "A beginner guide to keeping disease away when sewers and running water stop. It explains how germs "
            "spread from feces and how hand-washing (including a tippy-tap) blocks them, then covers bucket toilets, "
            "trench latrines, latrine siting using Sphere humanitarian standards (30 m from water, pit bottom 1.5 m "
            "above the water table), pit and ventilated improved pit latrines, two-bin composting toilets, and using "
            "a gravity septic system without power. Further chapters cover greywater, garbage, flies, mosquitoes, "
            "and rodents; making soap from fat and lye, and lye from wood ashes; bathing, laundry, and menstrual "
            "hygiene; and handling and burying the dead following Red Cross and WHO guidance. A region-by-region "
            "guide and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Fire.pdf",
        "title": "Survival Info: Fire & Heating",
        "short": "Fire",
        "summary": (
            "A beginner guide to fire for heat, cooking, and light. It covers the fire triangle, tinder and "
            "kindling, fire lays, and putting fires out, then fire without matches: ferro rods, flint and steel, "
            "char cloth, lenses, batteries, the bow drill, and keeping fire going. Stove chapters explain rocket "
            "stoves built on Aprovecho's ten design principles, wood stoves and clearances, and fuel-saving "
            "cooking. A firewood chapter lists heat per cord for more than 30 North American species, plus EPA "
            "seasoning rules. Safety chapters cover do-it-yourself chimney cleaning, chimney fires, carbon "
            "monoxide, and house fire prevention. A region-by-region winter heating guide and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Radio.pdf",
        "title": "Survival Info: Radio & Communications",
        "short": "Radio",
        "summary": (
            "A beginner guide to staying informed and in touch when phones and internet are down. It compares FRS, "
            "GMRS, CB, and amateur radio, including power limits, licensing, and the amateur emergency rule, "
            "then covers NOAA Weather Radio frequencies and building a battery-free crystal radio. Talking chapters "
            "cover FRS/GMRS, CB with emergency channel 9, ham bands and the 146.52 MHz calling frequency, and "
            "how to make a call and run check-in schedules. Antenna chapters show how to build a wire dipole using "
            "ARRL's 468 ÷ MHz rule, with a cut table. Later parts cover battery and solar power for radios and "
            "signaling without radio: mirrors, distress fires, ground-to-air symbols, whistles, and Morse code. "
            "Region-by-region notes and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Preservation.pdf",
        "title": "Survival Info: Food Preservation & Storage",
        "short": "Preservation",
        "summary": (
            "A step-by-step canning and storage guide built on the USDA Complete Guide to Home Canning. It starts "
            "with botulism: why low-acid foods need a pressure canner, the pH 4.6 line, warning signs of spoiled "
            "jars, and safe disposal and bleach clean-up. Canning chapters cover jars, lids and headspace, "
            "boiling-water and pressure canner steps, altitude adjustments, a USDA processing-time table, and "
            "checking seals. Later parts cover sun drying, jerky made safely, storing dried food, dry-curing ham, "
            "smoking fish, sauerkraut and fermenting crocks, root-cellar storage groups, and long-term grain and "
            "bean storage with shelf-life data. Region-by-region notes, a quick-reference page, and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Hunting.pdf",
        "title": "Survival Info: Hunting, Trapping & Fishing",
        "short": "Hunting",
        "summary": (
            "A beginner guide to getting meat and fish without stores, based mainly on the U.S. Army survival "
            "manual FM 21-76. It opens with a note on game laws, then covers reading animal sign, snare and noose "
            "placement, twitch-up and treadle snares, squirrel poles, figure-4 and Paiute deadfalls, and bottle "
            "traps. Fishing chapters cover improvised hooks and gorges, stakeouts, gill nets, fish and tidal traps, "
            "spearing, and dangerous fish. The last parts cover field dressing, cooling meat in warm weather, "
            "butchering, small game, game diseases (tularemia, chronic wasting disease, trichinella, brucellosis), "
            "safe cooking temperatures, region-by-region notes, and sources."
        ),
    },
    {
        "filename": "Survival_Info_Defense.pdf",
        "title": "Survival Info: Defense & Security",
        "short": "Defense",
        "summary": (
            "A defensive-only guide to keeping a household and neighborhood safe, drawn from sheriff and police "
            "crime-prevention material, CPTED design guidance, the Neighborhood Watch Manual, and OPSEC training. "
            "It covers awareness and reporting suspicious activity, describing people and vehicles, hardening "
            "doors, jambs, strike plates, windows and sliding doors, quick-release security bars for fire escape, "
            "landscaping and lighting, and simple noise alarms (with a warning against booby traps). Group chapters "
            "cover watch rotations that protect sleep, organizing block captains, phone and radio trees, pair "
            "patrols that observe and report, pooling resources, and the five-step OPSEC process. Region-by-region "
            "notes and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Navigation.pdf",
        "title": "Survival Info: Navigation & Travel",
        "short": "Navigation",
        "summary": (
            "A beginner guide to finding your way and traveling safely without GPS, based on the Army map-reading "
            "manual FM 3-25.26 and NOAA magnetic data. It covers reading topographic maps and contour lines, "
            "orienting a map, azimuths and back azimuths, magnetic declination with a 2026 table of values for "
            "North American cities, compass interference, bypassing obstacles, and pace counting. Navigating "
            "without a compass covers the shadow-stick and watch methods, Polaris, the Southern Cross, and the "
            "moon, plus an improvised needle compass. Travel chapters cover route planning, bicycles, the go-bag, "
            "river crossings, floodwater, and bogs. Region-by-region notes and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Weather.pdf",
        "title": "Survival Info: Weather & Natural Disasters",
        "short": "Weather",
        "summary": (
            "A guide to forecasting without a weather service and surviving North America's natural disasters, "
            "based on NOAA, National Weather Service and Ready.gov (FEMA) material. It covers the ten basic cloud "
            "types, cloud sequences that signal rain or snow, lightning distance by flash-to-bang, and building a "
            "can or jar barometer and keeping a weather log. Disaster chapters cover lightning, tornado shelter, "
            "hurricane seasons and storm surge, floods and flash floods, wildfire defensible space, earthquakes "
            "(Drop, Cover, Hold On), tsunami warning signs, blizzards with a wind chill table, frostbite and "
            "hypothermia, and heat illness. Region-by-region hazards and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Gardening.pdf",
        "title": "Survival Info: Gardening & Seed Saving",
        "short": "Gardening",
        "summary": (
            "A vegetable-growing guide built on USDA, Natural Resources Canada, EPA and university extension "
            "sources. It covers hardiness zones in the US and Canada, planting by the last frost date and soil "
            "temperature with a crop table, the jar test for soil texture, raising pH safely with wood ash, beds "
            "and spacing, building and managing a hot compost pile, crop rotation by plant family, cover crops, "
            "saving seed from open-pollinated tomatoes, peppers, beans and peas, storing seed, and stretching the "
            "season with row covers, low tunnels, cold frames and manure hot beds. Region-by-region growing "
            "notes and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Livestock.pdf",
        "title": "Survival Info: Livestock & Small Animals",
        "short": "Livestock",
        "summary": (
            "A guide to keeping chickens, rabbits, goats and honey bees without a vet or feed store, based on "
            "university extension publications. It covers coop design and predators, feed and daily care, "
            "hatching eggs and candling, signs of healthy birds, coccidiosis, Marek's disease and biosecurity "
            "with 30-day quarantine; rabbit hutches, a breeding calendar, feed and Pasteurella; goat-tight "
            "fencing, breeding and kidding, and controlling the barberpole worm with eyelid checks and pasture "
            "rotation; and the Langstroth hive, apiary siting, winter honey stores and varroa mites. "
            "Region-by-region notes and sources close the book."
        ),
    },
    {
        "filename": "Survival_Info_Medicine.pdf",
        "title": "Survival Info: Medicine & Remedies",
        "short": "Medicine",
        "summary": (
            "A DIY guide to medicines when there is no pharmacy, doctor or hospital, with every claim sourced and "
            "honest about its limits. It covers stockpiling and storing medicines, what shelf-life research (the "
            "military SLEP program) says about potency past expiry and the exceptions that go bad (liquid "
            "antibiotics, insulin, nitroglycerin, epinephrine); preventing infection, honey wound care, and the "
            "signs of spreading infection and sepsis; the WHO oral rehydration solution; the history and hard "
            "limits of making penicillin, in a scarce-resources tier and an equipped-lab tier, with firm warnings "
            "on toxic moulds, allergy, dose and purity; willow bark and other evidence-backed plant painkillers, "
            "plus making salicylic acid and aspirin in a lab; and a medicinal-plant section with real photos and "
            "deadly look-alikes. No opioids or controlled-drug synthesis. Region-by-region notes and sources close "
            "the book."
        ),
    },
    {
        "filename": "Survival_Info_Chemistry.pdf",
        "title": "Survival Info: Chemistry",
        "short": "Chemistry",
        "summary": (
            "A deep, standalone guide to rebuilding chemical capability from salt, stone, wood, air and water, "
            "for knowledge retention if the chain of industry were ever broken. Every claim is sourced. It covers "
            "lab fundamentals and improvised glassware, pH and plant indicators, and safety; separation and "
            "purification in depth (simple, fractional, steam and vacuum distillation, recrystallisation, "
            "extraction, chromatography and titration); raw materials from the land (salt, the lime cycle, potash, "
            "saltpetre beds, sulfur, charcoal and destructive distillation, kelp for iodine); the bulk acids and "
            "alkalis (sulfuric by lead-chamber and contact, nitric, hydrochloric, acetic, soda and caustic soda by "
            "Solvay and chloralkali, ammonia); gases and elements; organic foundations with the named reactions; "
            "step-by-step drug syntheses with troubleshooting and purity checks (aspirin, salicylic acid, "
            "paracetamol, the -caines, sulfanilamide, ether, Dakin's, iodine, saline); scaling up and energy; and a "
            "tiered library of 23 US equipment patents saved as PDFs. Dual-use chemicals are covered for legitimate "
            "medical, lab, agricultural and industrial use only; no explosives, weapons or controlled-substance "
            "synthesis. Region-by-region notes and sources close the book."
        ),
    },
]


def page_count(pdf: Path) -> int:
    proc = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True)
    m = re.search(r"^Pages:\s+(\d+)\s*$", proc.stdout, re.M)
    if not m:
        raise RuntimeError(f"pdfinfo did not report Pages for {pdf}\n{proc.stdout}")
    return int(m.group(1))


def file_size_label(pdf: Path) -> str:
    n = pdf.stat().st_size
    if n >= 1024 * 1024:
        return f"{n / (1024 * 1024):.1f} MB"
    return f"{n / 1024:.0f} KB"


def cover_art() -> str:
    # Stylized stacked volumes and a simple North America outline, series colors.
    bars = []
    labels = ["Water", "Food", "Electricity", "Concrete", "Tools", "House", "Bunkers", "Medical", "Sanitation", "Fire", "Radio", "Preservation", "Hunting", "Defense", "Navigation", "Weather", "Gardening", "Livestock", "Medicine", "Chemistry"]
    colors = ["#2f7fbf", "#2e7d32", "#e69b00", "#6d4c41", "#7a5c2e", "#8a4b08", "#1f4e5f", "#c0392b", "#00897b", "#d35400", "#5e35b1", "#827717", "#4e342e", "#ad1457", "#0277bd", "#455a64", "#558b2f", "#a1887f", "#00838f", "#6a1b9a"]
    for i, (lab, col) in enumerate(zip(labels, colors)):
        y = 10 + i * 16.4
        bars.append(
            f'<rect x="40" y="{y}" width="310" height="16" rx="3" fill="{col}"/>'
            f'<text x="56" y="{y+12.5}" font-family="Barlow Condensed, sans-serif" '
            f'font-size="13" font-weight="700" fill="#fff">{html.escape(lab)}</text>'
        )
    # Stylized North America: Canada, US, Mexico, Central America, Caribbean hint
    map_svg = """
    <g transform="translate(400,8)">
      <path fill="#255868" d="M48,52 L72,38 L98,44 L128,28 L158,22 L188,30 L214,20 L248,36
        L268,58 L272,88 L258,118 L248,128 L230,122 L218,108 L200,98 L188,108
        L168,92 L152,98 L138,88 L118,96 L98,90 L78,98 L62,88 L50,70 Z"/>
      <path fill="#1c4452" d="M78,98 L98,90 L118,96 L138,88 L152,98 L168,92 L188,108
        L200,98 L218,108 L230,122 L248,128 L240,148 L222,168 L200,178 L182,198
        L168,186 L150,192 L132,178 L118,168 L98,172 L80,158 L70,138 L74,118 Z"/>
      <path fill="#255868" d="M150,192 L168,186 L182,198 L170,222 L152,238 L138,228 L142,210 Z"/>
      <path fill="#1c4452" d="M138,228 L152,238 L148,258 L132,272 L118,260 L124,242 Z"/>
      <circle cx="210" cy="70" r="3.5" fill="#e69b00"/>
      <circle cx="160" cy="140" r="3" fill="#e6b54a"/>
      <circle cx="128" cy="210" r="2.5" fill="#e6b54a"/>
    </g>
    """
    return (
        '<svg viewBox="0 0 720 340" width="100%" xmlns="http://www.w3.org/2000/svg">'
        + "".join(bars)
        + map_svg
        + "</svg>"
    )


CSS = r"""
@page {
  size: Letter;
  margin: 0.6in 0.7in 0.75in 0.7in;
  @bottom-left { content: "Survival Info · Series Index"; font: 8.5pt 'IBM Plex Sans'; color:#7a8691; }
  @bottom-right { content: counter(page); font: 600 10pt 'IBM Plex Sans'; color:#1f4e5f; }
}
@page cover { margin: 0; @bottom-left { content: none } @bottom-right { content: none } }
* { box-sizing: border-box; }
body {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 11pt;
  line-height: 1.48;
  color: #1f2a33;
  margin: 0;
}
.cover { page: cover; width: 8.5in; height: 11in; background: #12313d; color: #fff; position: relative; overflow: hidden; break-after: page; }
.cover .band { position:absolute; left:0; right:0; top: 0; height: 0.32in; background: #e69b00; }
.cover .series { position:absolute; left: 0.8in; top: 0.95in; font: 600 13pt 'Barlow Condensed'; letter-spacing: 4px; color:#e6b54a; text-transform: uppercase; }
.cover h1 { position:absolute; left: 0.8in; top: 1.3in; margin:0; font: 800 54pt/0.95 'Barlow Condensed'; color:#fff; letter-spacing: 0.5px; }
.cover .sub { position:absolute; left:0.8in; top: 3.55in; width: 6.8in; font: 400 14pt/1.45 'IBM Plex Sans'; color:#cfe0e6; }
.cover .art { position:absolute; left: 0.6in; right: 0.55in; top: 5.15in; }
.cover .foot { position:absolute; left:0.8in; right:0.8in; bottom: 0.65in; font-size: 10.5pt; color:#9fb6bf; border-top: 1px solid #3c6070; padding-top: 10px; }
h1.part {
  font: 800 28pt/1 'Barlow Condensed'; color: #fff; background: #1f4e5f;
  margin: 0 0 16px 0; padding: 14px 18px 12px; border-left: 10px solid #e69b00;
}
h1.part small { display:block; font: 600 11pt 'Barlow Condensed'; letter-spacing: 3px; color:#e6c27a; margin-bottom: 4px; text-transform: uppercase; }
h2 { font: 700 18pt/1.15 'Barlow Condensed'; color: #1f4e5f; margin: 18px 0 8px; padding-bottom: 3px; border-bottom: 2px solid #e69b00; break-after: avoid; }
h3 { font: 700 14pt/1.2 'Barlow Condensed'; color: #8a4b08; margin: 12px 0 4px; break-after: avoid; }
p { margin: 0 0 8px; }
ul { margin: 2px 0 10px; padding-left: 20px; }
li { margin-bottom: 4px; }
table { width: 100%; border-collapse: collapse; margin: 8px 0 14px; font-size: 10.5pt; break-inside: avoid; }
th { background: #1f4e5f; color: #fff; text-align: left; padding: 6px 8px; font-weight: 600; }
td { padding: 5px 8px; border-bottom: 1px solid #d5dde2; vertical-align: top; }
tr:nth-child(even) td { background: #f3f7f9; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
.mono { font-family: 'IBM Plex Mono', monospace; font-size: 10pt; }
.entry {
  border: 1px solid #c9d4da; border-radius: 6px; margin: 0 0 14px;
  break-inside: avoid; overflow: hidden;
}
.entry .eh {
  background: #12313d; color: #fff; padding: 8px 12px 7px;
  font: 700 16pt 'Barlow Condensed';
  display: flex; justify-content: space-between; align-items: baseline; gap: 12px;
}
.entry .eh .num {
  display: inline-block; background: #e69b00; color: #12313d;
  font: 700 12pt 'Barlow Condensed'; border-radius: 50%;
  width: 22px; height: 22px; line-height: 22px; text-align: center; margin-right: 8px;
}
.entry .meta { padding: 7px 12px 0; font-size: 10.5pt; color: #4b5a66; }
.entry .meta b { color: #1f4e5f; }
.entry .body { padding: 6px 12px 10px; }
.small { font-size: 10pt; color: #4b5a66; }
.pb { break-before: page; }
"""


def document(guides: list[dict]) -> str:
    total_pages = sum(g["pages"] for g in guides)
    n = len(guides)

    rows = []
    for i, g in enumerate(guides, 1):
        rows.append(
            "<tr>"
            f"<td class='num'>{i}</td>"
            f"<td>{html.escape(g['title'])}</td>"
            f"<td class='mono'>{html.escape(g['filename'])}</td>"
            f"<td class='num'>{g['pages']}</td>"
            "</tr>"
        )

    entries = []
    for i, g in enumerate(guides, 1):
        entries.append(
            f"<div class='entry' id='{html.escape(g['short'].lower())}'>"
            f"<div class='eh'><span><span class='num'>{i}</span>{html.escape(g['title'])}</span>"
            f"<span style='font:600 11pt IBM Plex Sans;color:#e6b54a'>{g['pages']} pages</span></div>"
            f"<div class='meta'>File: <b class='mono'>{html.escape(g['filename'])}</b>"
            f" &nbsp;·&nbsp; {html.escape(g['size_label'])}</div>"
            f"<div class='body'><p>{html.escape(g['summary'])}</p></div>"
            "</div>"
        )

    body = f'''
<section class="cover">
  <div class="band"></div>
  <div class="series">Survival Info · Long-Term Survival Guide Series · North America</div>
  <h1>Survival Info<br>Series Index</h1>
  <div class="sub">A one-volume map of the printed guides: what each one covers, how long it is, and how the source library is organized. Print this index and keep it with the set.</div>
  <div class="art">{cover_art()}</div>
  <div class="foot">Last updated {html.escape(LAST_UPDATED)}. &nbsp;{n} guides &nbsp;·&nbsp; {total_pages} pages in the set. &nbsp;Meant to be used when the internet is not available.</div>
</section>

<h1 class="part" style="break-before:auto"><small>Index</small>The Survival Info series</h1>

<p>Survival Info is a set of long-term, grid-down guides for North America. Each topic is its own PDF, written to be printed and kept as a paper copy. The series covers every North American region, from the Arctic to the Caribbean, including the United States (with Puerto Rico), Canada, Mexico, and, where it is relevant, Central America and Cuba. The guides are meant to grow more advanced over time. This index lists every volume that exists today, with a short summary of what is in it.</p>

<p>Text in the guides is set large enough to read by lamplight. Length is not limited: a volume is as long as the subject needs. Illustrations are drawn from code, not generated as artwork, and the food guide uses real plant-identification photographs. Every cited source is saved as a PDF in a companion source library, described below.</p>

<h2>Guides in this set</h2>
<table>
  <thead><tr><th class="num">#</th><th>Title</th><th>Filename</th><th class="num">Pages</th></tr></thead>
  <tbody>
    {''.join(rows)}
    <tr><td></td><td><b>Total</b></td><td></td><td class="num"><b>{total_pages}</b></td></tr>
  </tbody>
</table>
<p class="small">Page counts were read from each PDF with <span class="mono">pdfinfo</span> on {html.escape(LAST_UPDATED)}.</p>

<h2>How the series is organized</h2>
<p>Each finished guide is a single letter-size PDF in the Survival Info folder, named <span class="mono">Survival_Info_&lt;Topic&gt;.pdf</span> — for example, <span class="mono">Survival_Info_Water.pdf</span>. Drafts, when they exist, use a <span class="mono">_DRAFT</span> suffix and are not part of the numbered set. This index is <span class="mono">Survival_Info_Index.pdf</span>. When a new guide is added, this index should be rebuilt so the table, page counts, and summaries stay current.</p>
<p><b>Phone-friendly copies.</b> Some phone chat apps will not open PDFs larger than about 1 MB. Every guide over that size has a folder of smaller copies with the same pages. Split into several parts: <span class="mono">bunker-parts/</span> (four parts), <span class="mono">Water-parts/</span>, <span class="mono">Food-parts/</span>, <span class="mono">Electricity-parts/</span>, <span class="mono">Concrete-parts/</span>, <span class="mono">House-parts/</span>, <span class="mono">Medicine-parts/</span>, <span class="mono">Tools-parts/</span>, <span class="mono">Preservation-parts/</span>, <span class="mono">Fire-parts/</span>, <span class="mono">Navigation-parts/</span>, <span class="mono">Medical-parts/</span>, <span class="mono">Hunting-parts/</span>, <span class="mono">Defense-parts/</span>, <span class="mono">Sanitation-parts/</span>, <span class="mono">Gardening-parts/</span> and <span class="mono">Livestock-parts/</span>. One compact file: <span class="mono">Chemistry-parts/</span>, <span class="mono">Radio-parts/</span> and <span class="mono">Weather-parts/</span>. Photos and patent drawings in these copies are saved at a lower resolution; the text is unchanged. Parts after the first start with the guide cover.</p>
<p><b>US patent appendices.</b> Most guides now end with a &ldquo;US Patents &mdash; schematics by tech level&rdquo; appendix. It sorts real U.S. patents by the level of technology needed: Tier A (simple, hand-built), Tier B (workshop-built) and Tier C (industrial). Each card gives the number, inventor, grant date, status, what the patent teaches, which figures to copy, and the key drawing sheet at full width. Every patent PDF is saved in <span class="mono">Survival Info Sources/&lt;Guide&gt;/Patents/</span>. The Chemistry guide has its own patent section in Part 9. Bunkers has no patent appendix.</p>
<p>The Bunkers volume is updated on a monthly cycle. New listings are added to the guide; properties that sell stay in it and are marked sold. Time-on-market is not recorded.</p>

<h2>How the source library is organized</h2>
<p>Every source cited in a guide is saved, when the site allows, as a PDF in a folder named <span class="mono">Survival Info Sources/&lt;Guide&gt;/</span> — for example, <span class="mono">Survival Info Sources/Water/</span>. A URL that already points to a PDF is downloaded directly; an HTML page is printed to PDF. Captchas, logins, and block pages are not bypassed. Any source that could not be saved is listed, with the reason, in that folder’s <span class="mono">_could_not_save.txt</span>.</p>
<p>For delivery, each guide’s source folder is packed with Python’s <span class="mono">zipfile</span> module into <span class="mono">Sources_&lt;Guide&gt;.zip</span>. If the archive would be larger than 23 MiB (the practical attachment limit), it is split into <span class="mono">Sources_&lt;Guide&gt;_part1.zip</span>, <span class="mono">_part2.zip</span>, and so on, each under 23 MiB. Inside every zip the files sit in the same <span class="mono">Survival Info Sources/&lt;Guide&gt;/</span> subfolder. A few original source PDFs were larger than that limit; those were downsampled (images at about 150 dpi JPEG, text left as text) so the parts would fit.</p>

<h1 class="part"><small>The guides</small>What each volume covers</h1>
{''.join(entries)}

<p class="small">Last updated {html.escape(LAST_UPDATED)}. Rebuild this index from <span class="mono">build-index/build.py</span> when a guide is added or a page count changes.</p>
'''
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<title>Survival Info · Series Index</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )


def render_html(html_text: str, pdf: Path) -> None:
    HTML.write_text(html_text, encoding="utf-8")
    subprocess.run(
        [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf}",
            str(HTML),
        ],
        check=True,
        capture_output=True,
    )


def render_pngs(pdf: Path) -> None:
    PNG_DIR.mkdir(exist_ok=True)
    for old in PNG_DIR.glob("*.png"):
        old.unlink()
    subprocess.run(
        ["pdftoppm", "-png", "-r", "120", str(pdf), str(PNG_DIR / "page")],
        check=True,
    )


def main() -> int:
    os.chdir(HERE)
    loaded = []
    missing = []
    for g in GUIDES:
        path = ROOT / g["filename"]
        if not path.exists():
            missing.append(g["filename"])
            continue
        rec = dict(g)
        rec["pages"] = page_count(path)
        rec["size_label"] = file_size_label(path)
        rec["path"] = path
        loaded.append(rec)
        print(f"  {rec['filename']}: {rec['pages']} pages, {rec['size_label']}", flush=True)
    if missing:
        print("WARNING: missing guide PDFs:", ", ".join(missing), file=sys.stderr)
    if not loaded:
        print("No guides found.", file=sys.stderr)
        return 1

    html_text = document(loaded)
    render_html(html_text, OUT_PDF)
    render_pngs(OUT_PDF)
    pages = page_count(OUT_PDF)
    print(f"wrote {OUT_PDF}  {OUT_PDF.stat().st_size:,} bytes  {pages} pages", flush=True)
    print(f"PNG previews in {PNG_DIR}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
