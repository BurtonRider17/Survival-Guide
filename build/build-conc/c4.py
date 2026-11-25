from helpers import danger, caution, tip, check, table, fig
from basediag import REGIONS

FROST = [(1, "Permafrost (continuous/discontinuous); seasonal frost 5–10+ ft", "Do not thaw permafrost: gravel pads, ventilated crawlspace, posts/piles, adjustable cribbing"),
         (2, "Coast 12–18 in; BC/WA/OR interior 24–48 in", "Seismic detailing everywhere west of the Cascades"),
         (3, "Kansas/Oklahoma 18–36 in; Dakotas/Nebraska 42–60 in; Canadian Prairies 4–8 ft", "Expansive clays: deeper footings, gravel under slabs"),
         (4, "36–48 in south; 48–60 in Minnesota, Wisconsin, northern Michigan, Ontario", "Frost-protected shallow footings save digging"),
         (5, "36–48 in; 48–60+ in Maine, northern New England, Quebec, New Brunswick", "Leda (Champlain Sea) clays are unstable when disturbed"),
         (6, "12–18 in; 18–30 in in the Appalachians", "Termites, heavy rain — raise floors"),
         (7, "None — but footings ≥ 12 in below grade on firm soil", "High water table, sinkholes, flood elevations"),
         (8, "Low deserts 6–12 in; high plateaus and Great Basin 18–36 in", "Flash floods in washes; expansive and collapsible soils"),
         (9, "36–48 in; 48–60+ in high valleys of Montana, Wyoming, Colorado", "Deep snow loads; expansive clays on the Front Range"),
         (10, "Coast and valleys ~12 in; foothills 18 in; Sierra and northeast 24–36+ in", "Earthquakes — reinforce everything"),
         (11, "Lowlands none; Chihuahua–Durango plateau 12–24 in", "Heat, limited water for mixing and curing"),
         (12, "None (frost only on high peaks) — found on firm soil 18–24 in down", "Earthquakes, hurricanes, rainy-season floods"),
         (13, "None — found on firm soil 18–24 in down", "Hurricanes, earthquakes, salt air")]

def part8(D):
    h = ['<h1 class="part" id="p8"><small>Part 8</small>Building a Small Masonry House</h1>']
    h.append('<p>This part covers the <b>masonry and concrete side</b> of a small, durable house: choosing and draining the site, footings and foundations, the slab, walls, openings, bond beams and the connection to the roof. For framing, roof structure and covering, doors and windows, insulation and interior work in depth, see the companion volume <b>Survival Info, Vol. 1: House Building</b>. A small, simple rectangular house (about 16–24 ft wide) with thick walls, a light roof and few, moderate openings is the most forgiving design for amateur builders — and the easiest to make strong against wind, snow and earthquakes.</p>')
    h.append('<h2 id="site">8.1 Site selection and drainage</h2>')
    h.append(check("Choosing a building site", [
        "High, gently sloping ground that sheds water — never a valley floor, dry wash, floodplain or the foot of a slope where runoff collects; look for flood debris lines and ask about past floods",
        "Firm, undisturbed soil: avoid fill, peat, organic muck, very soft clay, and the edges of cuts and steep slopes; dig test holes to below footing depth and check for water seeping in",
        "Close (but not too close) to water, materials (stone, sand, clay, timber) and fields; at least 100 ft (30 m) from wells to latrines and animal pens",
        "Winter sun on the long side (south in North America); shelter from prevailing winter wind; clear of big trees that could fall on the roof; defensible space from wildfire",
        "Check for sinkholes (karst areas), landslide scars, and expansive clays (wide cracks in dry season, sticky when wet)"]))
    h.append('<p><b>Drainage is the single biggest factor in how long a masonry house lasts.</b> Grade the ground to fall away from the walls at least 6 in in the first 10 ft (5%, the IRC minimum). Put a perforated pipe (or a trench of clean gravel, a “French drain”) beside the footing, wrapped in fabric or straw and running downhill to daylight. Uphill of the house, dig a shallow swale to divert surface runoff around it. Gutters or a gravel “drip edge” under the eaves keep roof water away from the base of the walls.</p>')
    h.append('<h2 id="found">8.2 Footings and foundations</h2>')
    h.append('<p>The footing must (1) sit below frost depth (or be protected by insulation), (2) rest on firm, undisturbed soil, and (3) be wide enough that the soil can carry the load. Masonry walls are heavy — an 8 in grouted block wall weighs about 80 lb per square foot of wall, an 18 in rammed earth wall about 200 — so footings for masonry houses are wider than those for wood frames.</p>')
    h.append('<div class="formula"><span class="eq">Footing width (ft) = load per foot of wall (lb/ft) ÷ allowable soil pressure (lb/ft²)</span>Load = wall weight (height × weight per ft² of wall) + share of roof, snow and floor. Example: 10 ft of 8 in grouted block (800 lb/ft) + roof and snow (500 lb/ft) = 1,300 lb/ft on clay (1,500 psf) → 0.87 ft → use a <b>16–20 in</b> wide footing. 18 in rammed earth: 2,000 + 500 = 2,500 lb/ft → 1.7 ft → <b>24 in</b>.</div>')
    h.append(table(["Soil (IRC Table R401.4.1)", "Allowable pressure"], [
        ["Crystalline bedrock (granite etc.)", "12,000 psf (575 kPa)"], ["Sedimentary rock (limestone, sandstone, shale)", "4,000 psf (190 kPa)"],
        ["Sandy gravel, gravel", "3,000 psf (145 kPa)"], ["Sand, silty sand, clayey sand, silty gravel", "2,000 psf (95 kPa)"],
        ["Clay, sandy clay, silty clay, clayey silt", "1,500 psf (72 kPa)"], ["Peat, organic soil, fill, soft wet clay", "Don’t build on it — dig through to firm soil"]]))
    h.append('<p><b>Typical footings for a one-story masonry house</b>: 16–24 in (400–600 mm) wide, 8–12 in (200–300 mm) thick, 2–3 #4 bars continuous, bottom below frost line. Under a 2-story or earth-walled house: 24–30 in wide. Interior bearing walls and stove/chimney bases need their own footings. Build a <b>stem wall</b> (concrete, block, or stone in mortar) from the footing up to at least 8 in above finished grade — 12–18 in for earth walls.</p>')
    h.append(table(["#", "Region", "Typical frost depth for footings (check local practice)", "Foundation notes"],
        [[str(k), REGIONS[k][0], a, b] for k, a, b in FROST], cls="brk"))
    h.append(tip("Frost-protected shallow foundations (FPSF)", "Instead of digging 4–5 ft to get below frost, lay rigid foam insulation (extruded polystyrene) vertically on the outside of the stem wall and horizontally out 1–4 ft from it, just under the ground surface. The house’s heat and the earth’s warmth keep the soil under the footing unfrozen, so footings can be as shallow as 16 in even in severe climates. Used in over a million Scandinavian homes; see the HUD/NAHB <i>Design Guide for Frost-Protected Shallow Foundations</i> for insulation tables. Works for heated buildings on non-permafrost ground; unheated buildings need more insulation."))
    h.append('<h2 id="slab">8.3 The slab floor</h2>')
    h.append('<p>A slab-on-grade (Part 7.4) is the simplest floor for a masonry house: build the footings and stem walls, backfill and compact gravel inside, lay vapor barrier and insulation, and pour the slab inside the stem walls, or pour a <b>monolithic slab</b> with thickened edges (footing and slab in one pour — common in warm climates). Keep the finished floor at least 8 in above outside grade. In flood, termite or very wet areas, a raised wood floor on masonry piers or a crawlspace with vents may be better — see the House Building volume.</p>')
    h.append('<h2 id="walls">8.4 Walls: choosing a system</h2>')
    h.append(table(["Wall system", "Thickness", "Needs", "Pros", "Cons / limits"], [
        ["<b>Concrete block (CMU)</b>, reinforced and grouted", "8 in", "Cement for blocks, mortar, grout; rebar", "Fast, strong, termite- and fire-proof; easy to reinforce", "Poor insulation; uses the most cement"],
        ["<b>Fired brick</b>", "8–13 in (2–3 wythes)", "Clay, fuel, lime or cement mortar", "Durable, can be made locally, handsome", "Fuel-hungry; needs reinforcement in seismic zones"],
        ["<b>Stone in mortar</b>", "16–24 in", "Lime or cement mortar; lots of labor", "Uses free fieldstone; lasts centuries", "Slow; heavy footings; hard to reinforce"],
        ["<b>Slip-formed stone</b>", "12–18 in", "Short movable forms, stone, some concrete", "Stone face, concrete core; needs little skill", "Uses cement (less than solid concrete)"],
        ["<b>Poured concrete</b> (salvaged forms)", "6–8 in", "Much cement, forms, rebar", "Very strong", "Most cement and formwork"],
        ["<b>Rammed earth</b>", "12–24 in", "Suitable soil, forms, labor", "Little or no cement; great mass", "Must stay dry; heavy labor"],
        ["<b>Adobe / CEB</b>", "10–14 in", "Soil, molds or press", "No fuel; owner-buildable", "Dry climates, needs bond beam & good base"],
        ["<b>Earthbag</b>", "15–18 in", "Bags, barbed wire, soil", "Cheapest, fastest; domes possible", "Needs plaster quickly (UV); buttresses"]]))
    h.append('<p><b>Rules that apply to every wall</b>: keep walls straight and plumb; tie corners and intersections (interlock units or bend steel round the corner); provide a cross wall, buttress or pilaster at least every ~20 wall-thicknesses for masonry (13 ft for 8 in block) and every 8–10 thicknesses of height and length for earth walls; keep unreinforced walls one story. <b>Slip forming</b> (an old owner-builder method): set 18–24 in high wood forms on both faces, place flat-faced stones against the form, fill behind with stiff concrete, and move the forms up each day.</p>')
    h.append(fig(D.floor_plan(), "<b>Figure 14. Example plan: 20 × 24 ft (6.1 × 7.3 m) one-story masonry house</b> (~380 ft² / 35 m² inside with 8 in walls). Compact rectangle, one interior bearing wall to shorten roof spans, openings away from corners, masonry hearth, cellar hatch, porch slab and cistern fed by the roof.", "max-width:74%"))
    h.append('<h2 id="openings">8.5 Openings and lintels</h2>')
    h.append('<p>Every opening weakens a wall. Keep openings at least 2 ft (600 mm) from corners and from each other; keep total openings under about one-third of any wall’s length (less for earth walls and in earthquake zones). Span them with:</p>')
    h.append(table(["Opening width", "Reinforced concrete lintel (wall width)", "Bearing each end"], [
        ["Up to 4 ft (1.2 m)", "6 in deep, 2 #4 bars 1½ in above the bottom", "8 in (200 mm) minimum"],
        ["4–6 ft (1.2–1.8 m)", "8 in deep, 2 #4 bars", "8 in"],
        ["6–8 ft (1.8–2.4 m)", "12–16 in deep (or a 2-course grouted block lintel), 2 #5 bars + stirrups", "12 in"]]))
    h.append('<p>Cast lintels in place in a form propped from below (leave props 7–14 days), or precast them on the ground and lift them in. Bond-beam blocks or U-blocks filled with grout make good lintels in block walls. For earth walls, hardwood or doubled timber lintels (depth ≈ span ÷ 10, bearing 12–18 in each side) are common; set them on a mortar pad. <b>Arches</b> of brick or stone need no steel but push sideways — keep at least 2 ft of solid wall beside them and buttress the ends of arcades. These spans are conservative rules of thumb for one-story houses with light roofs.</p>')
    h.append('<h2 id="bond">8.6 Bond beams, reinforcement and earthquakes</h2>')
    h.append('<p>A <b>bond beam</b> (ring beam, collar beam) is a continuous reinforced band around the top of all walls. It ties the walls into a box so they can’t peel apart, spreads roof loads, and anchors the roof. It is the most important single detail in a masonry house — and the one most often missing in buildings that collapse in earthquakes and hurricanes.</p>')
    h.append('<ul><li><b>Concrete bond beam</b>: full wall width × 6–8 in deep (8–12 in on earth walls), 2 #4 bars (4 #4 on walls 12 in or thicker), continuous with 24 in laps and bent bars around corners. Cast in U-blocks on block walls or in a form on top of earth/brick walls.</li>'
             '<li><b>Timber bond beam</b> for earth walls where cement is scarce: two 2×6 or larger planks laid flat, cross-blocked into a ladder, lapped and bolted at corners, pinned down into the wall.</li>'
             '<li><b>Vertical steel</b>: in block walls, #4 bars in grouted cells at every corner, both sides of each opening, and every 4 ft (2 ft in high seismic zones), hooked into the footing and the bond beam.</li>'
             '<li><b>Confined masonry</b> (standard in Mexico and Central America: <i>castillos</i> and <i>dalas</i>): build the brick or block wall first with toothed edges, then cast reinforced concrete tie-columns (6–8 in square, 4 #3 bars with ties every 6–8 in) against it at corners and openings, and a bond beam on top. It uses less steel and formwork than a frame and performs well in earthquakes.</li>'
             '<li>In earthquake zones (Alaska, Pacific coast, California, Utah/Nevada fault zones, Mexico, Central America, Caribbean): one story, symmetrical plan, small openings, light roof, and no unreinforced masonry or adobe gable walls. Heavy roofs and unreinforced walls kill people.</li></ul>')
    h.append('<h2 id="roofatt">8.7 Connecting the roof</h2>')
    h.append('<p>Roofs fail by lifting off in high wind and by sliding off in earthquakes. Cast <b>anchor bolts</b> (½ in × 10 in J-bolts, at least 7 in into concrete) into the bond beam every 4–6 ft and within 12 in of each corner and plate splice. Bolt a treated wood sill plate (or two) to them over a strip of tar paper or plastic, then tie every rafter or truss to the plate with steel straps or hurricane ties — in hurricane areas, use straps cast directly into the bond beam. Keep the roof light (metal sheets, shingles, thatch) unless you are building a true masonry vault. Rafter design, roof pitch and snow loads are covered in the House Building volume.</p>')
    h.append(fig(D.wall_section(), "<b>Figure 15. Wall section for a block-walled house on a slab</b>, showing the masonry and drainage details that matter most. Earth walls use the same principles with a taller stem wall, capillary break, lime plaster and wider overhangs.", "max-width:76%"))
    h.append('<h2 id="moisture">8.8 Moisture control and insulation (masonry side)</h2>')
    h.append('<div class="cols2"><div><h3>Keep water out of the masonry</h3><ul><li><b>Good boots</b>: stem wall ≥ 8 in above grade (12–18 in for earth); a capillary break (slate, tar paper, plastic, or a dense mortar layer) between footing/stem and wall so ground moisture can’t wick up.</li><li><b>Good hat</b>: roof overhangs 18–24 in for masonry, 24–36 in for earth walls; flashing and drips over windows; sills sloped outward.</li><li>Damp-proof the outside of below-grade walls (bitumen, cement render, or plastic) and drain at the footing.</li><li><b>Let walls breathe</b>: earth, soft brick and lime-mortared stone must be plastered with lime or earth, not cement stucco or paint that traps moisture and causes the wall to rot from inside.</li></ul></div>'
             '<div><h3>Insulation and thermal mass</h3><p>Masonry stores heat but is a poor insulator: about R-0.1 per inch for concrete, R-0.2 for brick, R-0.25 for rammed earth (an 18 in rammed-earth wall ≈ R-4; a modern code wall is R-13 to R-20+). In deserts with big day–night swings, thick unshielded mass works well. <b>In cold climates, insulate the outside of the masonry</b> (rigid foam, straw-clay, pumice/scoria concrete, or a second wall with a filled cavity) so the mass stays inside the warm envelope, and insulate the slab edge and the attic heavily. Details of insulation systems are in <b>Survival Info, Vol. 1: House Building</b>.</p></div></div>')
    h.append(check("Masonry house build sequence", [
        "Site, layout with batter boards and strings, check diagonals equal (square)",
        "Dig footing trenches below frost line to firm soil; drain lines; inspect for soft spots",
        "Footings with rebar and vertical dowels; cure 3–7 days",
        "Stem walls, damp-proofing, perimeter drain, backfill with gravel",
        "Under-slab plumbing/drains, gravel, vapor barrier, insulation, slab; cure 7 days",
        "Walls course by course, vertical steel and grout, lintels as openings are reached",
        "Bond beam with anchor bolts all round; cure 7 days before loading",
        "Roof (see House Building volume), then plaster, floors and finishes"]))
    return "\n".join(h)

R = [
 (1, "Limestone in the Hudson Bay Lowlands, Mackenzie Valley and Arctic islands, and parts of Yukon and Alaska; shells limited. Pozzolan: <b>Alaska volcanic ash</b> (Aleutians, Alaska Peninsula — Katmai/Novarupta 1912 ash, Cook Inlet volcanoes). Clay: glacial and silty permafrost soils. Sand & gravel: <b>abundant</b> in eskers, outwash and river bars.",
     "Permafrost (thawed ground sinks), −40° cold, building season only June–August, extreme freeze–thaw, scarce fuel for kilns on the tundra.",
     "Keep heat out of frozen ground: gravel pads, ventilated crawlspaces, timber cribbing or posts on adjustable blocks. Use concrete mainly for small precast items cured indoors or under heated tents. Earth-sheltered sod-and-timber buildings; stone for stoves and heat banks."),
 (2, "Limestone on Texada and Vancouver Islands, San Juan Islands (historic Roche Harbor lime kilns), NE Washington; shells in oyster beds and middens. Pozzolan: <b>abundant</b> — Cascade ash and pumice (Mazama, Mount St. Helens, Newberry). Clay: glacial-marine and river clays. Sand & gravel: <b>abundant</b> glacial outwash and rivers.",
     "Long rainy winters (slow lime carbonation, mold, eroding earth walls), mild freeze–thaw, <b>Cascadia megaquake</b> and crustal faults, landslides.",
     "Reinforced block or concrete with bond beams; lime + volcanic ash mortars and plasters; big overhangs; cob and earth only with stone bases and lime plaster. Plenty of timber for forms and kiln fuel."),
 (3, "Limestone and chalk: Kansas Flint Hills (“post rock”), Niobrara chalk (KS, NE, SD), Manitoba Tyndall stone, Oklahoma. Pozzolan: <b>volcanic ash beds</b> from Yellowstone eruptions in Nebraska and Kansas (e.g., Pearlette ash). Clay: abundant, often <b>expansive bentonite</b>. Sand & gravel: Platte, Arkansas and other rivers; glacial in the north.",
     "Deep frost, blizzards, wind, hail, <b>tornadoes</b>, expansive clays that heave and shrink, scarce wood for kilns.",
     "Deep or frost-protected footings; reinforced concrete storm shelter/root cellar; rammed earth and sod; limestone fence posts; burn chalk with straw, corn cobs or coal. Fly ash at coal plants."),
 (4, "<b>Abundant limestone and dolomite</b>: Niagara Escarpment, Indiana (Bedford), Ohio, Iowa, Illinois, Missouri, Wisconsin, southern Ontario. Shells: freshwater mussels (minor). Pozzolan: none natural — use crushed brick, calcined clay, fly ash. Clay: glacial till and lake clays (historic brickyards everywhere). Sand & gravel: <b>abundant</b> glacial outwash, eskers, fresh-water lake beaches.",
     "Deep frost (3–5 ft), severe freeze–thaw and road-salt damage, wet springs, tornadoes.",
     "Best all-round region for lime kilns and fired brick. Use low water–cement ratios and long curing for frost durability; stockpile air-entrained cement/admixture while available. Fieldstone foundations."),
 (5, "Limestone and marble: Vermont marble, Hudson Valley (Rosendale natural-cement rock), Lehigh Valley PA (“cement belt”), St. Lawrence Lowlands, Nova Scotia (limestone and <b>gypsum</b>); Atlantic oyster and clam shells. Pozzolan: none natural. Clay: Hudson River and glacial-marine clays (sensitive Leda clay in Ottawa/St. Lawrence valleys). Sand & gravel: abundant glacial deposits.",
     "Severe freeze–thaw, 4–5 ft frost, nor’easters, salt spray on coasts, dense population (salvage competition).",
     "<b>Fieldstone</b> everywhere — dry-stone walls and stone foundations; lime from marble and limestone; natural cement from clayey “cement rock”; fired brick from river clays. Wash beach sand thoroughly."),
 (6, "Limestone: Appalachian valleys (TN, KY, VA, AL), Nashville Basin, Kentucky Bluegrass, Selma chalk (AL, MS); <b>oyster shell</b> along the Gulf and Atlantic (historic <b>tabby</b> of Georgia and the Carolinas: lime + shell + sand). Pozzolan: none natural — <b>rice husk ash</b> (Arkansas, Louisiana, Mississippi), brick dust. Clay: red Piedmont and coastal-plain clays (excellent brick). Sand & gravel: coastal plain sand, Mississippi and Piedmont river gravel.",
     "Heat and humidity (hot-weather concreting), hurricanes, heavy rain, termites, mild frost (12–18 in).",
     "Fired brick and lime from shell or limestone; tabby walls on the coast; confined or reinforced block with bond beams for hurricanes; raised floors in flood zones."),
 (7, "Limestone <b>everywhere</b> (Ocala, Miami oolite, Key Largo coral rock) and <b>coquina</b> (shell rock — Castillo de San Marcos); shells abundant. Pozzolan: none. Clay: scarce (some in north Florida). Sand: abundant but fine and uniform; gravel scarce — use crushed limestone or coquina.",
     "Hurricanes (wind and surge), high water table, flooding, <b>sinkholes</b> (karst), salt air and salty sand, heat and humidity.",
     "Shell or limestone lime; tabby and coquina blocks; reinforced block walls with bond beams and tie-columns (Florida building practice); floors above flood level; wash all sand and keep salt out of reinforced work."),
 (8, "Limestone: Great Basin ranges (NV, UT), Grand Canyon region (Kaibab, Redwall), <b>caliche</b> in soils everywhere; <b>gypsum</b> (White Sands NM, Utah, Nevada). Pozzolan: <b>abundant</b> — Jemez/Bandelier tuff and pumice (NM), San Francisco volcanic field (AZ), Utah tephra (Rush Valley). Clay: excellent adobe soils. Sand & gravel: alluvial fans and washes (well graded).",
     "Heat, intense sun and drying winds, <b>very little water</b> for mixing and curing, flash floods, monsoon storms, big day–night swings, freezing at altitude.",
     "<b>Adobe and rammed earth</b> (the regional tradition), lime–pozzolan mortars and plasters, gypsum for interior plaster. Cure under wet sand, plastic and shade; mix at dawn. Thick mass walls suit the climate."),
 (9, "Limestone: Madison and other Paleozoic limestones across MT, WY, CO, ID; gypsum in WY and CO. Pozzolan: <b>Yellowstone ash and tuffs</b>, Snake River Plain cinders and scoria (lightweight aggregate), San Juan volcanic field (CO). Clay: variable; expansive bentonite on the Front Range plains. Sand & gravel: <b>abundant</b> rivers and glacial outwash.",
     "Deep frost, short building season, heavy snow loads, high UV, wildfire, expansive soils, cold-weather curing.",
     "Stone and concrete with frost-protected or deep footings; scoria/pumice concrete for better insulation; earth-sheltered buildings on south slopes; plan pours for June–September."),
 (10, "Limestone: limited — Sierra foothill marble (many historic lime kilns, e.g., Santa Cruz), Mojave limestones. Shells on the coast. Pozzolan: <b>abundant</b> — Nomlaki tuff (Sacramento Valley), Shasta/Lassen, Long Valley/Mono, Clear Lake volcanics; diatomite (Lompoc). Clay: valley clays (mission adobe tradition). Sand & gravel: rivers and alluvial fans.",
     "<b>Earthquakes</b> (critical), wildfire, drought, long dry season (good for building), coastal salt.",
     "Reinforced block, confined masonry or reinforced earthbag only — unreinforced adobe and brick collapse in quakes. Lime–pozzolan for mortars and plaster; fire-resistant masonry with metal roofs."),
 (11, "Limestone: <b>abundant</b> in the Sierra Madre Oriental (Nuevo León, Coahuila, Tamaulipas); caliche; gypsum (Coahuila). Pozzolan: Sierra Madre Occidental tuffs and ignimbrites (Chihuahua, Durango, Zacatecas — <i>cantera</i> stone), Sonoran volcanics. Clay: adobe soils. Sand & gravel: arroyos and rivers.",
     "Heat, drought and water scarcity, monsoon flash floods, freezing nights on the high plateau.",
     "Adobe with bond beams; confined masonry (<i>castillos</i> and <i>dalas</i>); traditional <i>cal</i> (lime) from limestone kilns; lime–tuff mortars. Conserve water for curing."),
 (12, "Limestone: <b>entire Yucatán Peninsula</b> (Maya lime and <i>sascab</i>, a soft weathered limestone used as aggregate), Puebla, Oaxaca, Chiapas. Pozzolan: <b>abundant</b> across the Trans-Mexican Volcanic Belt — <i>tezontle</i> (red scoria), pumice (<i>jal</i>), volcanic ash. Clay: abundant; strong fired-brick (<i>tabique</i>) tradition. Sand & gravel: rivers, volcanic sands.",
     "<b>Earthquakes</b> (1985, 2017), hurricanes on both coasts, rainy-season floods and landslides, heat and humidity on coasts.",
     "Confined masonry with fired brick or block; lime + volcanic ash (Roman-style) mortars and concrete; tezontle lightweight concrete for roofs; Maya-style lime burning in pit kilns."),
 (13, "Limestone and coral: Bahamas, Cuba, Jamaica, Puerto Rico, Hispaniola, Belize, Petén; shells abundant (don’t mine living reefs). Pozzolan: <b>abundant</b> along the Central American volcanic arc (Guatemala, El Salvador, Nicaragua, Costa Rica) and Lesser Antilles volcanoes. Clay: tropical clays and <b>laterite</b> (cut blocks harden in air). Sand & gravel: rivers; beach sand is salty.",
     "Hurricanes, earthquakes, heat and humidity, termites, salt air; <b>using unwashed beach sand is a major cause of failed concrete</b> on islands.",
     "Confined masonry with bond beams and strapped roofs; wash all sand; lime from coral and limestone, lime–ash concrete in volcanic countries; ferrocement cisterns for rainwater; no frost, so shallow footings to firm soil."),
]

SUMMARY = [
 (1, "Local (lowlands, islands)", "Alaska ash", "Glacial silt", "<b>Abundant</b>", "Permafrost"),
 (2, "Islands, NE WA", "<b>Abundant</b>", "Good", "<b>Abundant</b>", "Earthquake, rain"),
 (3, "Chalk, post rock", "Ash beds (NE, KS)", "Expansive", "Rivers", "Frost, tornado"),
 (4, "<b>Abundant</b>", "Brick, fly ash", "<b>Excellent</b>", "<b>Abundant</b>", "Frost"),
 (5, "Marble, limestone", "Brick dust", "Good", "<b>Abundant</b>", "Freeze–thaw"),
 (6, "Limestone, oyster", "Rice husk ash", "<b>Excellent</b>", "Good", "Hurricane, heat"),
 (7, "<b>Everywhere</b>", "None", "Scarce", "Sand only", "Hurricane, flood"),
 (8, "Limestone, caliche", "<b>Abundant</b>", "<b>Adobe</b>", "Good (washes)", "Water scarcity"),
 (9, "Common", "Ash, scoria", "Variable", "<b>Abundant</b>", "Frost, snow"),
 (10, "Limited", "<b>Abundant</b>", "Good", "Good", "<b>Earthquake</b>"),
 (11, "<b>Abundant</b>", "Tuffs", "Adobe", "Arroyos", "Heat, drought"),
 (12, "<b>Abundant</b>", "<b>Abundant</b>", "<b>Excellent</b>", "Good", "<b>Earthquake</b>"),
 (13, "Coral, limestone", "<b>Abundant</b> (arc)", "Laterite", "Rivers", "Hurricane, quake")]

def part9(D):
    h = ['<h1 class="part" id="p9"><small>Part 9</small>Region-by-Region Guide for North America</h1>']
    h.append('<p>Where you live decides which binder you can make, which aggregate you’ll dig and what the weather will do to your work. Use the map to find your region, then read its card for <b>materials</b> (lime sources, pozzolans, clay, sand and gravel), <b>climate challenges</b> and the <b>best approaches</b>. Geology is patchy — the USGS karst map (Open-File Report 2014-1156) shows carbonate rock in the US; state and provincial geological surveys have local maps. Always verify with the vinegar, jar and pat tests.</p>')
    h.append(fig(D.region_map(), "<b>Figure 16. Regions used in this guide</b> (the same regions as the Water, Food and Electricity volumes).", "max-width:54%"))
    h.append('<div class="legend">' + "".join(f'<div><span class="c" style="background:{c}"></span>{k} {n}</div>' for k, (n, c) in REGIONS.items()) + '</div>')
    h.append(table(["#", "Region", "Lime sources", "Pozzolan", "Clay / brick", "Sand & gravel", "Main hazard"],
        [[str(k), REGIONS[k][0], a, b, c, d, e] for k, a, b, c, d, e in SUMMARY], cls="brk"))
    h.append('<div class="regions">')
    for k, mat, chall, best in R:
        nm, col = REGIONS[k]
        h.append(f'<div class="region"><div class="rh" style="background:{col}"><span class="n">{k}</span>{nm}</div><div class="rb"><p><b>Materials:</b> {mat}</p><p><b>Climate challenges:</b> {chall}</p><p><b>Best approaches:</b> {best}</p></div></div>')
    h.append('</div>')
    return "\n".join(h)
