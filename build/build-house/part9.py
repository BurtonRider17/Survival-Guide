from common import *
from diagrams import REGIONS, region_map

SUMMARY = [
 (1, "Permafrost; 3.5–10 ft", "40–80+", "Extreme cold, permafrost, wind, S. Alaska earthquakes", "Super-insulated frame, log, earth-bermed"),
 (2, "1–4 ft", "Coast 10–25; Cascades 100–400+", "Cascadia earthquake & tsunami, rain/rot, landslide, wildfire (east)", "Timber & stick frame, cedar; rainscreen"),
 (3, "1.5–6 ft", "20–50", "Tornado, blizzard, wind, hail, few trees", "Straw bale, earth-sheltered, sod (historic)"),
 (4, "1.5–5 ft", "20–60; lake belts 60–100+", "Tornado, ice storm, lake snow, floods, New Madrid quake", "Log, timber frame, cordwood, bale, stick"),
 (5, "2–6 ft", "30–80; mtns 100+", "Nor'easters, ice, heavy wet snow, hurricanes", "Timber frame, stone, log, cordwood"),
 (6, "0.5–2.5 ft", "5–20", "Hurricane, tornado, heat/humidity, termites, flood", "Raised wood frame, metal roof, brick"),
 (7, "None", "0", "Cat 4–5 hurricanes, surge, Formosan termites, heat", "Raised frame or block; hip metal roof"),
 (8, "0–3 ft", "0–40", "Heat, flash floods, drought, quakes (UT/NV), fire", "Adobe, rammed earth, bale, earthbag"),
 (9, "3–6 ft", "30–300+", "Deep snow, avalanche, wildfire, cold, wind", "Log, timber frame, bale (valleys), stone"),
 (10, "0–3 ft", "0 coast; Sierra 150–400+", "Earthquakes, wildfire, drought, mudslides", "Braced wood frame, plastered bale"),
 (11, "0–2 ft", "≈ 0", "Heat, drought, flash floods, coast hurricanes, quakes (Baja)", "Adobe, rammed earth, confined masonry"),
 (12, "None", "0", "Major earthquakes, volcanoes, hurricanes, landslides", "Confined masonry, bahareque, bamboo"),
 (13, "None", "0", "Hurricanes, earthquakes, volcanoes, floods, termites", "Bahareque, bamboo, raised frame, confined masonry")]

R = [
 (1, "Log (spruce, birch for interior) in the forested subarctic; super-insulated stick frame (double stud walls with 10–14 in of cellulose, sawdust or salvaged batts) where lumber is available; traditional sod-and-driftwood or earth-bermed houses on the treeless coast. Small, compact, two-story or loft; arctic entry; small north windows, larger south windows (low sun).",
  "−40 to −50° cold, months of darkness, permafrost, strong winds and drifting, wildfire in the boreal forest, very large earthquakes in southern Alaska, short building season.",
  "The highest anywhere: ceilings R-60+, walls R-40+, floor R-30+ over a ventilated crawl. Post-and-pad or piles with adjustable jacks on a gravel pad; keep the ground frozen (CCHRC). Insulated, heat-traced or buried water lines; keep the stove going."),
 (2, "Abundant timber: stick frame, timber frame and log; western red cedar for shakes, siding and sills. East of the Cascades and in the BC interior: log and straw bale. Big roofs with 2–3 ft overhangs and gutters are essential west of the mountains.",
  "Constant winter rain and rot; mold; the Cascadia subduction zone (magnitude-9 earthquake and coastal tsunami), landslides on steep wet slopes, wildfire and drought in the interior and late summer; heavy mountain snow.",
  "Moderate (walls R-20, ceiling R-38–49); rainscreen siding and breathable walls. Wood-frame walls well braced and bolted to footings for earthquakes; avoid unreinforced masonry, cob and adobe on the coast. Build above tsunami inundation zones on the outer coast."),
 (3, "Straw bale (abundant wheat straw — historic Nebraska Sandhills bale houses still stand), earth-bermed or earth-sheltered houses into south-facing slopes, rammed earth; sod houses were the original prairie homes. Timber is scarce — salvage lumber from towns and farm buildings; use river-bottom cottonwood only for temporary work.",
  "Tornadoes, blizzards and ground blizzards, −30 to −40° cold in the north, very high winds, hail, drought and grass fires, scarce firewood.",
  "High (walls R-30+, ceilings R-49–60); passive solar heating is very effective under the sunny winter skies. Every house needs a tornado shelter: a below-ground cellar or a reinforced room. Dense shelterbelts on the north and west; low profile, strong roof ties."),
 (4, "Log and timber frame from hardwood and pine forests in the north; cordwood (historic in Wisconsin and Ontario); straw bale; stick frame from the vast stock of abandoned buildings in towns. Fieldstone and brick for foundations and chimneys.",
  "Cold snowy winters, lake-effect snow belts (Michigan, Ontario, NY), ice storms, tornadoes, spring river floods (Mississippi, Ohio, Red River), humid summers; the New Madrid seismic zone in Missouri, Arkansas, Tennessee and Kentucky.",
  "Walls R-20–30, ceilings R-49; vapor retarder on the warm side in the north. Snow-load rafters (Part 5) in lake belts. Build above flood levels; brace and tie houses in the New Madrid zone; tornado cellar in the southern part."),
 (5, "Timber frame (the New England tradition), log in the north woods, fieldstone everywhere, cordwood; abundant salvage in the dense urban corridor. Steep roofs (8:12–12:12) with metal or cedar shakes shed heavy wet snow.",
  "Long cold winters, nor'easters, ice storms that bring down trees, hurricanes tracking up the coast, coastal flooding, heavy wet snow, humid summers, deep frost.",
  "Walls R-20–30, ceilings R-49; airlock entries. Strong rafters and snow raking; tie roofs down on the coast. Place the house away from tall trees that can fall on it in ice storms; stone and brick need inside insulation."),
 (6, "Raised wood frame houses on brick or stone piers (good airflow, flood and termite protection), with metal roofs, deep porches and high ceilings — the “dogtrot” and “shotgun” traditions; brick where clay is abundant; log in the Appalachians and Ozarks.",
  "Hurricanes on the Gulf and Atlantic coasts, tornadoes (“Dixie Alley”), extreme humidity, mold, very heavy subterranean termite pressure (Formosan termites on the Gulf coast), river and coastal floods, ice storms inland.",
  "Moderate (walls R-13–20, ceiling R-30–38) plus shade, ventilation and a light-colored or radiant-barrier roof. No interior plastic vapor barrier. Termite shields, durable heartwood or treated sills, keep wood 18 in (45 cm) off the ground and inspect for mud tubes. Hurricane straps and hip roofs on the coast."),
 (7, "The Florida “cracker house”: a raised wood frame on piers with a steep metal roof, wide porches, a central breezeway and windows on all sides; or concrete block (CBS) where cement is available (see Concrete &amp; Masonry). Hip roofs strapped to walls.",
  "Category 4–5 hurricanes and storm surge, frequent flooding, Formosan and drywood termites, heat and humidity, lightning, sinkholes in limestone areas, no frost.",
  "Roof insulation and shade matter most; minimal wall insulation. Build well above surge and flood levels (FEMA P-499) on deep piers; shutters for every opening; continuous load path from roof to foundation. Termite-resistant wood or steel; never leave wood debris near the house."),
 (8, "Adobe and rammed earth (Pueblo and Hispanic traditions), straw bale with earthen or lime plaster, earthbag domes and walls, stone. Thick mass walls; flat earthen roofs on vigas are traditional but need constant maintenance — a pitched metal roof over mass walls is more forgiving.",
  "Extreme summer heat with cold nights, flash floods in arroyos, water scarcity, intense sun and UV, wildfire, earthquakes along the Wasatch Front and in Nevada; desert subterranean termites; cold snowy winters in the Great Basin and high desert.",
  "Low desert: mass walls, deep shade, light roofs, night ventilation, ceiling insulation R-30–38. High desert/Great Basin: insulated mass (bale or insulated adobe) and passive solar. Keep earthen walls on stone footings with drainage. Seismic bond beams in Utah and Nevada."),
 (9, "Log (lodgepole pine is one of the best log species), timber frame, straw bale in the valleys, stone. Steep metal roofs on stout rafters; generous overhangs protect logs from rain and sun.",
  "Very heavy snow loads (100–300+ psf at high elevations — check the ASCE hazard tool), avalanche paths, wildfire, −30 to −40° cold, strong chinook and downslope winds, intense UV, some earthquakes (Montana, Idaho, Utah, Yellowstone).",
  "Walls R-25–30+, ceiling R-49–60. Size rafters for local snow (Part 5); don't build below avalanche chutes or at the top of steep forested slopes. Ember-resistant roof and vents, defensible space."),
 (10, "Braced wood frame (the most earthquake-tolerant common system), plastered straw bale (performs well in tests), with metal or tile roofs. Earthen buildings only with reinforcement and bond beams (Getty guidelines). Stone and adobe historic in the missions — many collapsed in earthquakes.",
  "Major earthquakes on the San Andreas and many other faults, wildfire (especially wind-driven fall fires), drought, mudslides after fires, coastal fog and rot, very heavy snow in the Sierra, subterranean and drywood termites in the south.",
  "Mild climates need moderate insulation (ceiling R-38, walls R-13–21). Anchor bolts, hold-downs and plywood shear walls; strap water heaters and tanks. Ember-resistant vents (⅛ in mesh), metal roof, no wood fences touching the house, 30 m defensible space."),
 (11, "Adobe (traditional), rammed earth, stone, and confined masonry (block or brick with concrete tie-columns and beams); palapa and ramada shade structures of palm, carrizo cane and ocotillo; flat roofs on vigas.",
  "Extreme heat and drought, monsoon flash floods, hurricanes on the Pacific (Baja, Sonora, Sinaloa) and Gulf (Tamaulipas) coasts, earthquakes in Baja California, cold winters in the Chihuahua and Sierra Madre highlands.",
  "Thick mass walls, small shaded openings, courtyards, light roofs with insulation; cross-ventilation at night. Reinforce heavy walls with bond beams; keep adobe off the ground on stone footings."),
 (12, "Confined masonry (as CENAPRED's safe self-build guide shows), bahareque (timber or bamboo frame with woven cane and mud — flexible and earthquake-resistant), bamboo (otate) and wood; adobe with seismic reinforcement in the highlands; palm-thatch palapas on the coasts.",
  "Large earthquakes (Mexico City 1985 and 2017), active volcanoes (Popocatépetl, Colima), hurricanes on both coasts, intense rainy-season downpours, landslides and floods, termites in the lowlands.",
  "Highlands: mass walls and passive solar for cool nights. Lowlands: raised, shaded, ventilated, light buildings. Follow CENAPRED: firm ground away from slopes and riverbanks, stone/concrete footings, castillos and dalas tying every wall, light well-tied roofs."),
 (13, "Bahareque and bamboo (guadua grows in Central America), raised timber frame, confined masonry; palm thatch is traditional but blows away in hurricanes — use well-strapped metal roofs on hip frames, with thatch only for outbuildings.",
  "Hurricanes, earthquakes (Guatemala 1976, Haiti 2010), volcanoes, very heavy rain, floods and landslides, salt-air corrosion, intense termites and rot.",
  "Shade and ventilation, not insulation. Raise floors 0.5–1 m on piers; hip roofs at 4:12–6:12 with short eaves; shutters; continuous ties from roof to foundation. Avoid unreinforced block and adobe; use stainless or galvanized fasteners near the sea.")]

def build():
    h = ['<h1 class="part" id="p9"><small>Part 9</small>Region-by-Region Guide for North America</h1>']
    h.append('<p>Find your region on the map, then read its card for the best building methods and materials, the climate hazards to design for, and insulation and structural priorities. The regions match the other volumes of this series. Ground snow loads are rough ranges in pounds per square foot (1 psf ≈ 0.048 kPa) — local values vary hugely with elevation; use the ASCE Hazard Tool or local code values for your exact site while they are available.</p>')
    h.append(fig(region_map(), "Regions used in this guide (same as the Electricity &amp; Fuel volume).", "max-width:62%"))
    h.append('<div class="legend">' + "".join(f'<div><span class="c" style="background:{c}"></span>{k} {n}</div>' for k, (n, c) in REGIONS.items()) + '</div>')
    h.append(table(["#", "Region", "Frost depth", "Ground snow (psf)", "Main hazards", "Best wall systems"],
        [[str(k), REGIONS[k][0], a, b, c, d] for k, a, b, c, d in SUMMARY], cls="brk", widths=["3%", "17%", "12%", "15%", "29%", "24%"]))
    h.append('<div class="regions">')
    for k, meth, haz, ins in R:
        nm, col = REGIONS[k]
        h.append(f'<div class="region"><div class="rh" style="background:{col}"><span class="n">{k}</span>{nm}</div><div class="rb"><p><b>Best methods &amp; materials:</b> {meth}</p><p><b>Climate hazards:</b> {haz}</p><p><b>Insulation &amp; design:</b> {ins}</p></div></div>')
    h.append('</div>')
    return "\n".join(h)
