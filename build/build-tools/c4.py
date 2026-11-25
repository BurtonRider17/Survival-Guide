from helpers import *
from base import REGIONS

R = [
 (1, "Paper birch, willow (small handles), tamarack; spruce and birch for charcoal; driftwood on coasts. Hickory/ash do not grow — stockpile manufactured handles.",
     "Snowmachines and ATVs (springs, axles), fuel drums, mining and oil-field equipment, boat yards, abandoned military/DEW-line sites (often contaminated — be careful).",
     "Obsidian at Batza Tena (Koyukuk River, AK) and Wiki Peak (near the AK–Yukon border); chert in the Brooks Range; basalt and slate.",
     "Steel becomes more brittle in extreme cold: warm axe heads and saws before hard use below −20°F (−29°C), and do not strike frozen tools hard. Handles shrink and loosen in dry heated cabins. Forge in the long summer; store charcoal dry."),
 (2, "Vine maple, Oregon white (Garry) oak, Pacific madrone, ash (Oregon ash); bigleaf maple. Douglas-fir, alder and maple for charcoal — huge supply of wood.",
     "Logging equipment (cable — often galvanized, check; chainsaw bars), sawmills (bandsaw and circular blades), shipyards, railroad lines, farm equipment east of the Cascades.",
     "<b>Obsidian:</b> Glass Buttes, OR (BLM; personal collecting allowed within limits); Newberry Crater and Obsidian Cliffs are protected. BC: Mount Edziza and Anahim Peak obsidian (provincial parks/First Nations lands). Agate and jasper on coastal beaches.",
     "Heavy rain and humidity west of the Cascades: rust is constant — oil tools daily, store under cover with airflow. Dry interior is easier on tools. Wildfire risk in summer east of the mountains."),
 (3, "Green ash, bur oak, hackberry, Osage orange (shelterbelts — superb), black locust; hickory in eastern Kansas/Oklahoma. Wood is scarce: charcoal from shelterbelts, river bottoms, or coal from mines.",
     "<b>Farm machinery everywhere:</b> disc blades, plow shares, tines, leaf springs, harrows; grain-elevator and railroad steel; oil-field pipe (some galvanized) and sucker rods.",
     "<b>Knife River flint</b> (west-central North Dakota), <b>Alibates</b> agatized dolomite (Texas Panhandle — protected monument), <b>Edwards chert</b> (central Texas), Florence chert in the Kansas Flint Hills, Smoky Hill jasper (KS–NE).",
     "Wind spreads forge sparks into grass fires fast — forge in a sheltered, cleared area and never on red-flag days. Extreme cold and heat; tornado-proof storage for tools. Bituminous and lignite coal in ND, Alberta, Saskatchewan."),
 (4, "<b>Hickory, white ash, sugar maple, hop-hornbeam, white oak</b> — some of the best handle wood in the world. Oak, hickory and maple make excellent charcoal.",
     "Rust Belt industry and scrapyards, rail yards, abundant farm machinery, auto plants and junkyards (springs, axles), hardware and farm-supply stores.",
     "<b>Flint Ridge (Vanport) flint</b>, Ohio (protected memorial; similar flint in surrounding outcrops), Upper Mercer chert (OH), Burlington chert (MO, IA, IL), Harrison County/Wyandotte chert (IN), Hixton silicified sandstone (WI), Onondaga and Kettle Point chert (southern Ontario).",
     "Humid summers and freeze-thaw winters: rust and handle swelling/shrinking — store tools in a dry, heated or well-ventilated shed. Long winters are good forging season under a roof."),
 (5, "Hickory (south of New England), white ash, sugar maple, hop-hornbeam, white oak, beech; birch and maple further north. Abundant hardwood for charcoal.",
     "Old mills and factories, railroads, shipyards, large scrapyards; antique tool stores are rich in hand tools (planes, braces, axes) — New England was a center of edge-tool making.",
     "<b>Onondaga chert</b> (western/central NY), Normanskill chert (Hudson Valley), Pennsylvania jasper (Lehigh/Berks Co.), Munsungun chert and Mount Kineo rhyolite (Maine), Scots Bay chalcedony (Nova Scotia), Ramah chert (Labrador — protected).",
     "Cold, damp, snowy winters: rust and frozen gear. Plan a sheltered smithy for winter work (the traditional season for tool making). Short growing season — repair farm tools in winter."),
 (6, "<b>Hickory</b> (the heart of hickory country), white oak, ash, black locust, persimmon (very tough), dogwood (mallets). Oak and hickory charcoal; pine makes lighter, fast charcoal.",
     "Farm and logging equipment, mobile-home axles and springs (salvage), railroads, auto junkyards. Appalachian tradition (Foxfire) of farm smithing — old shops still exist.",
     "<b>Arkansas novaculite</b> (Ouachitas — also the best natural whetstone), Dover chert (TN), Fort Payne chert (TN/AL), Ste. Genevieve/St. Louis chert (KY), Coastal Plain chert (GA/SC); river gravels.",
     "Heat and humidity: rust fast, mold on handles, termites and powder-post beetles in stored wood — oil tools daily, keep wood dry and off the ground. Forge in the cool mornings; hurricanes in coastal areas."),
 (7, "Live oak, laurel oak, hickory (north Florida), mastic and other tropical hardwoods in the far south; Australian pine (Casuarina, invasive) and oak for charcoal.",
     "Boat yards and marinas (stainless and galvanized — sort carefully; never heat galvanized trailers), cars, citrus and farm equipment, construction sites.",
     "<b>Ocala/Suwannee chert</b> (silicified limestone, north-central Florida); <b>agatized coral</b> (Tampa Bay area; Florida’s state stone). Little else — glass is a substitute.",
     "Highest humidity and salt air: rust is the main tool enemy — oil and wax everything, store in sealed boxes with dry rice or silica gel, keep off concrete. Heat: forge early and late; drink water."),
 (8, "Scarce: mesquite (excellent dense charcoal and short handles), desert ironwood, Gambel oak and juniper at elevation, cottonwood along rivers (soft). Stockpile handles.",
     "Mining equipment and drill steel, ranches (springs, axles; barbed wire is galvanized), railroads, military surplus, abandoned vehicles everywhere (dry climate preserves them).",
     "<b>Abundant obsidian and chert:</b> Jemez Mountains (NM; Valles Caldera is protected), Mule Creek (NM), Government Mountain (near Flagstaff, AZ), Apache tears (Superior, AZ), Mineral Mountains/Black Rock area (UT); agate and jasper across Nevada.",
     "Dry air shrinks handles and loosens heads — wedge tightly and oil wood often; tools rarely rust. Wildfire danger is extreme: forge only in cleared, wind-protected spots. Water for quenching and the slack tub is precious — cover it to stop evaporation."),
 (9, "Ash and oak are scarce; Rocky Mountain maple, chokecherry, serviceberry, Gambel oak (south), aspen (soft). Pine, fir and aspen charcoal (light, fast-burning); coal in WY, MT, CO, AB.",
     "Mining towns (rail, drill steel, cable, ore cars), ranches, railroads, logging equipment.",
     "Obsidian in Idaho (Malad, Big Southern Butte, Owyhee country) and Montana; <b>Obsidian Cliff</b> in Yellowstone (protected — no collecting); Spanish Diggings quartzite and Hartville chert (WY), Kremmling chert (CO).",
     "Cold, dry, high altitude: handles shrink; steel brittle in deep cold; thin air — forges and engines need more air. Heavy snow on shop roofs. Short summers for charcoal making."),
 (10, "Oregon/valley/coast live oak, Pacific madrone, California black walnut, ash in the north; eucalyptus (invasive, dense, cracks easily) and oak for charcoal.",
     "Huge urban scrap supply, auto yards, agriculture (vineyard, orchard and field equipment), ports and shipyards, rail.",
     "<b>Obsidian:</b> Glass Mountain/Medicine Lake (Modoc NF), Napa Valley, Bodie Hills; Coso (on a military base — off-limits). <b>Franciscan chert</b> (red radiolarian chert, Coast Ranges) and Monterey chert.",
     "Long dry season with extreme wildfire risk — forge only in cleared areas with water at hand, ideally in the wet season. Coastal fog and salt air cause rust; inland heat."),
 (11, "Mezquite (outstanding charcoal), encino (oak) and pine in the Sierra Madre; palo fierro (desert ironwood) and other dense desert woods for mallets and short handles.",
     "Truck and bus leaf springs (abundant — <i>muelles</i>), farm equipment in irrigated valleys, mining equipment (Sonora, Chihuahua, Zacatecas), railroads.",
     "Chert and chalcedony in the limestone ranges (Coahuila, Nuevo León); rhyolite and some obsidian in the volcanic Sierra Madre Occidental (Chihuahua, Durango). Fewer well-known sources — ask locally.",
     "Heat and drought: work early morning; water is scarce for quenching. Monsoon storms bring flash floods in summer. Dry air loosens handles."),
 (12, "Encino (oak), pine, tropical hardwoods (e.g., guayacán, chicozapote) in the south; oak and mesquite charcoal in the highlands — charcoal is still widely made and sold.",
     "Vehicle springs and axles, sugar mills and agricultural machinery, rebar and construction steel, railroad lines; many working village blacksmiths (herreros) still exist.",
     "<b>World-class obsidian:</b> Sierra de las Navajas near Pachuca (green obsidian, Hidalgo), Otumba (State of Mexico), Ucareo–Zinapécuaro (Michoacán), Tequila/Teuchitlán (Jalisco), Pico de Orizaba (Veracruz–Puebla); chert across the Yucatán.",
     "Rainy-season humidity causes rust; highlands are cooler and drier. Earthquakes — anchor anvils and tool racks. Protect forest: make charcoal from prunings and dead wood."),
 (13, "Tropical hardwoods (guayacán / lignum vitae, very dense; madre de cacao; mahogany) and oak/pine in Guatemala and Honduras highlands; mangrove is traditional charcoal but should be protected — use Leucaena, Gliricidia and coffee prunings.",
     "Vehicles, sugar-mill machinery, rebar, boat hardware (stainless and galvanized), port and plantation equipment; on islands, salvage is limited — stockpile files and saws.",
     "<b>Obsidian:</b> El Chayal, Ixtepeque and San Martín Jilotepeque (Guatemala), Güinope (Honduras). <b>Chert:</b> Colha (Belize), Long Island flint (Antigua), chert in Cuba and Hispaniola.",
     "Constant heat, humidity and salt air: rust and rot are the main enemies — oil, wax and store tools in sealed containers. Hurricanes: secure the shop and tools. Termites attack handles and wooden structures.")]

SUMMARY = [
 (1, "Birch (stockpile)", "Spruce, birch", "Equipment, drums", "Obsidian (AK)"),
 (2, "Vine maple, Garry oak", "Fir, alder, maple", "Logging, sawmills", "Obsidian (OR)"),
 (3, "Osage orange, ash", "Shelterbelt, coal", "<b>Farm machinery</b>", "<b>Knife River, Edwards</b>"),
 (4, "<b>Hickory, ash</b>", "<b>Oak, hickory</b>", "Industry, farms", "Flint Ridge, Burlington"),
 (5, "Hickory, ash, maple", "Hardwoods", "Mills, rail, antiques", "Onondaga chert"),
 (6, "<b>Hickory</b>, persimmon", "Oak, hickory, pine", "Farm, logging", "<b>Novaculite</b>, Dover"),
 (7, "Live oak", "Oak, Casuarina", "Boats, cars", "Ocala chert, coral"),
 (8, "Mesquite (stockpile)", "<b>Mesquite</b>, juniper", "Mines, ranches", "<b>Obsidian, chert</b>"),
 (9, "Maple, serviceberry", "Pine, aspen, coal", "Mines, rail", "Obsidian (ID)"),
 (10, "Oak, madrone", "Oak, eucalyptus", "Urban, ag, ports", "Obsidian, Franciscan chert"),
 (11, "Mesquite, encino", "<b>Mezquite</b>", "Truck springs, mines", "Chert, some obsidian"),
 (12, "Encino, guayacán", "Oak, mesquite", "Springs, sugar mills", "<b>Obsidian (Pachuca)</b>"),
 (13, "Guayacán, mahogany", "Leucaena, prunings", "Vehicles, mills", "Obsidian (Guatemala)")]

def part8(D):
    h = ['<h1 class="part" id="p8"><small>Part 8</small>Region-by-Region Guide for North America</h1>']
    h.append('<p>Tools and steel are much the same everywhere, but the wood for handles and charcoal, the best salvage sources, the stone for primitive tools and the climate challenges change across the continent. Find your region on the map, then read its card. Stone sources listed are known geological sources — many famous quarry sites are protected archaeological or park lands where collecting is illegal; collect only where allowed (for example BLM land with personal-use limits), or from creek gravels and private land with permission.</p>')
    h.append(fig(D.region_map(), "<b>Figure 12. Regions used in this guide</b> (the same 13 regions as the rest of the series).", "max-width:72%"))
    leg = '<div class="legend">' + "".join(f'<div><span class="c" style="background:{c}"></span>{k} {n}</div>' for k, (n, c) in REGIONS.items()) + '</div>'
    h.append(leg)
    h.append(table(["#", "Region", "Best handle wood", "Charcoal fuel", "Salvage steel", "Knapping stone"],
        [[str(k), REGIONS[k][0], a, b, c, d] for k, a, b, c, d in SUMMARY], cls="brk"))
    h.append('<div class="regions">')
    for k, wood, steel, stone, clim in R:
        nm, col = REGIONS[k]
        h.append(f'<div class="region"><div class="rh" style="background:{col}"><span class="n">{k}</span>{nm}</div><div class="rb"><p><b>Wood (handles, charcoal):</b> {wood}</p><p><b>Salvage steel:</b> {steel}</p><p><b>Knapping stone:</b> {stone}</p><p><b>Climate:</b> {clim}</p></div></div>')
    h.append('</div>')
    return "\n".join(h)
