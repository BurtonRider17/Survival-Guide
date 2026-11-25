from part1 import danger, caution, tip, check, table, fig
from diagrams import REGIONS

R = [
 (1, "Sun: very seasonal — near zero Dec–Jan north of the Arctic Circle, but 18–24 h days in summer (annual avg ~2.5–3.5 peak sun hours). Mount panels steep (60–90°) to catch low sun and shed snow; vertical panels also gain from snow reflection. Wind: excellent on coasts and tundra; turbines must be cold-rated (−40°). Hydro: good in mountain/coastal Alaska and Yukon; streams freeze or drop to a trickle in winter — design for winter low flow, buried/insulated pipe. Wood: boreal spruce, birch, aspen in the subarctic; none on the tundra.",
    "Extreme cold (lead-acid must stay charged; LiFePO4 needs heated enclosure), months of darkness, permafrost (foundations, buried pipe), long resupply distances.",
    "Few crops: Polish canola (B. rapa) and camelina in Alaska’s Matanuska/Tanana valleys and the Peace River country (one of Canada’s big canola regions at 55–57°N). Main feedstocks: fish oil and fish-processing waste, rendered moose/caribou/marine-mammal fat. Store winter-blend diesel or kerosene; animal-fat biodiesel will gel."),
 (2, "Sun: cloudy winters (≈1 peak sun hour in Dec on the coast), sunny dry summers; annual ~3–4 (higher east of the Cascades). Wind: strong on the outer coast and in the Columbia Gorge; weak in forested valleys. Hydro: <b>the best in North America</b> — rain-fed and snow-fed streams with steep drops everywhere west of the Cascades and Coast Mountains. Wood: abundant (fir, cedar, alder, maple).",
    "Winter rain + short days (solar weakest exactly when hydro is strongest — a perfect pairing), earthquakes, landslides that can damage penstocks, damp (corrosion, mold in battery rooms).",
    "Canola and camelina in eastern Washington/Oregon (Palouse) and the BC interior; mustard. West-side valleys are cool and wet (sunflower marginal). Large urban fryer-oil supply."),
 (3, "Sun: very good (annual ~4.5–5.5; clear cold winters). Wind: <b>the best wind resource on the continent</b> — average 6–8 m/s (13–18 mph) in many areas. Hydro: poor (flat; few streams with drop). Wood: scarce — shelterbelts, river bottoms, planted woodlots.",
    "Blizzards, −30 to −40° cold, hail (protect panels), tornadoes (lowerable tilt-up towers), drought, scarce firewood (plan heating early: insulation, passive solar, coal or straw where available).",
    "<b>Canola</b> (Canadian Prairies, North Dakota), <b>sunflower</b> (Dakotas, Kansas, Manitoba), soybean (eastern Plains), camelina and safflower (dry west), flax. The best biodiesel country in North America."),
 (4, "Sun: moderate (annual ~3.5–4.5; cloudy, lake-effect winters ~1.5–2.5). Wind: good in Iowa, Minnesota and lake shores; moderate elsewhere. Hydro: moderate — many old mill-dam sites (low head, high flow: propeller or waterwheel). Wood: good hardwood forests (oak, maple, ash).",
    "Cold snowy winters, gray skies Nov–Feb, ice storms, tornadoes, flat terrain limits high-head hydro.",
    "<b>Soybean</b> (dominant), sunflower, canola in Minnesota/north and Ontario, camelina; corn is poor for pressing (oil is in the germ). Lard and tallow from livestock."),
 (5, "Sun: moderate (annual ~3.5–4.5; Atlantic Canada ~3–4). Wind: good on coasts, islands, ridgelines (Maritimes, Newfoundland, Cape Cod). Hydro: <b>very good</b> — hilly terrain and hundreds of historic mill sites across New England, New York, Pennsylvania, Quebec and the Maritimes. Wood: excellent (mixed hardwood/softwood).",
    "Long cold winters, nor’easters and ice storms (downed trees on lines — bury cables), dense population in the corridor, short growing season in the north.",
    "Canola/rapeseed (Maine, PEI, New Brunswick, Quebec), soybean (Pennsylvania, New York, Ontario/Quebec), sunflower (Vermont farm-scale programs), camelina. Fish oil in coastal Atlantic Canada."),
 (6, "Sun: good (annual ~4.5–5.5; winter ~3–4). Wind: generally weak inland; fair on the coast and Appalachian ridges. Hydro: good in the Appalachians, Ozarks and Piedmont; poor on the flat coastal plain. Wood: excellent and fast-growing (pine, oak, hickory).",
    "Heat and humidity (battery cooling, mold, food spoilage — refrigeration is a top priority), hurricanes and tornadoes (secure panels, lowerable towers), flooding on the coastal plain, mild winters mean less heating fuel needed.",
    "Soybean, <b>peanut</b>, cottonseed, sunflower, winter canola; huge supply of poultry fat from processing plants (summer fuel — gels in cold)."),
 (7, "Sun: very good (annual ~5–5.5; winter ~4). Wind: weak inland, fair on the coast. Hydro: essentially none (flat). Wood: moderate (pine, oak, hardwood hammocks).",
    "Hurricanes (panels and racks rated for high wind; take down portable gear before storms), heat, humidity and salt air (corrosion), flooding, very high cooling and refrigeration needs; no heating fuel required most of the year.",
    "Peanut and soybean (Panhandle/north), sunflower (cool season), coconut (frost-free south only). Castor grows wild — <b>poisonous seeds</b>. Prioritize solar + batteries and waste/animal fats."),
 (8, "Sun: <b>the best in North America</b> (annual ~6–7; winter ~4.5–5.5). Wind: good in mountain passes and on ridges; variable elsewhere. Hydro: rare — few perennial streams; strict water rights. Wood: scarce (pinyon, juniper, mesquite).",
    "Extreme heat (panels lose ~0.4%/°C above 25 °C — mount with airflow; keep batteries shaded and cool, ideally underground or in an insulated room), dust (clean panels), water scarcity, cold desert nights at altitude.",
    "Irrigated safflower and sunflower (Arizona, Utah, Nevada valleys), dryland camelina. Jojoba is a liquid wax, not an ordinary oil — not a simple biodiesel feedstock. With little water, prioritize waste oils and animal fats."),
 (9, "Sun: very good (annual ~5–6; high altitude clear skies; winter ~3.5–4.5, snow reflection helps). Wind: strong on ridges and the Front Range/Wyoming plains (often turbulent). Hydro: <b>excellent high-head potential</b> — snowmelt streams with large drops suit Pelton turbines. Wood: good (pine, fir, aspen).",
    "Cold, long winters at altitude, deep snow (tilt panels steep), streams freezing and peaking hard with snowmelt in May–June (flood-proof intakes), wildfire, thin air (engines and generators lose ~3% power per 1,000 ft).",
    "Camelina, canola and safflower in Montana, Idaho and Wyoming valleys; sunflower on the eastern plains of Colorado. Short seasons at altitude."),
 (10, "Sun: excellent (annual ~5.5–6.5; winter 3–4.5 north, more south). Wind: strong in passes (Altamont, Tehachapi, San Gorgonio) and on the coast. Hydro: good in the Sierra Nevada, Klamath and North Coast ranges; little in the south. Wood: good north and in mountains, poor in the south.",
    "Wildfire (clear brush around equipment; buried lines), drought (seasonal creeks), earthquakes, very dense population and competition for resources in the south.",
    "<b>Safflower</b> (Sacramento Valley — a major U.S. area), sunflower, canola, cottonseed (San Joaquin), olive. Huge urban waste-oil supply."),
 (11, "Sun: excellent (annual ~6–7). Wind: good in some passes and on the Gulf coast of Tamaulipas and in the Isthmus further south. Hydro: limited — Sierra Madre Occidental/Oriental streams, seasonal. Wood: scarce in deserts; pine-oak in the sierras.",
    "Heat, drought, water scarcity, strong seasonal (monsoon) flash floods; 127 V / 60 Hz electrical standard.",
    "<b>Safflower</b> (cártamo) in Sonora, Sinaloa and Tamaulipas; soybean (Tamaulipas, Sinaloa); sunflower; cottonseed (Chihuahua, Coahuila); castor (higuerilla — poisonous seeds)."),
 (12, "Sun: very good (annual ~5–6; sunny dry season Nov–May, cloudier rainy season). Wind: world-class in the Isthmus of Tehuantepec (Oaxaca); moderate elsewhere. Hydro: very good in the mountains of Veracruz, Puebla, Oaxaca, Chiapas and Michoacán (rainy-season peaks; dry-season lows). Wood: good in highlands and tropics (watch deforestation).",
    "Hurricanes on both coasts, heavy rainy-season floods and landslides (protect penstocks), earthquakes, heat and humidity on the coasts.",
    "<b>Oil palm</b> (Chiapas, Tabasco, Campeche, Veracruz), <b>coconut</b> (Guerrero, Colima, Yucatán coasts), jatropha (piñón; some Mexican varieties are non-toxic but treat seeds as toxic), sesame, soybean (Campeche, Chiapas), castor."),
 (13, "Sun: good to excellent year-round (annual ~4.5–6), little seasonal change. Wind: strong steady <b>trade winds</b> on most Caribbean islands and coasts (excellent for small turbines). Hydro: <b>excellent</b> in mountainous countries — Guatemala, Honduras, Costa Rica, Panama, Hispaniola, Jamaica, Puerto Rico (many village micro-hydro schemes already exist). Wood: plentiful on mainland; scarce on some islands.",
    "Hurricanes (lowerable towers, panel tie-downs, stockpile spares), salt-air corrosion (stainless hardware, sealed connectors), heat and humidity, limited land on islands.",
    "<b>Oil palm</b> (Guatemala, Honduras, Costa Rica), <b>coconut</b> everywhere on coasts, jatropha and castor (non-food, poisonous seeds), peanut. Coconut and palm biodiesel gel at ~13–16 °C — no problem in the tropics."),
]

SUMMARY = [
 (1, "2.5–3.5*", "High (coast)", "Med (frozen winters)", "Med–none", "Fish/animal fat; camelina"),
 (2, "3–4", "Low–high", "<b>Very high</b>", "High", "Canola, camelina"),
 (3, "4.5–5.5", "<b>Very high</b>", "Low", "Low", "Canola, sunflower"),
 (4, "3.5–4.5", "Med–high", "Medium", "High", "Soybean, sunflower"),
 (5, "3.5–4.5", "Med (coast high)", "High", "High", "Canola, soybean"),
 (6, "4.5–5.5", "Low", "Med (hills)", "High", "Soy, peanut, poultry fat"),
 (7, "5–5.5", "Low–med", "None", "Medium", "Peanut, coconut (S)"),
 (8, "<b>6–7</b>", "Medium", "Very low", "Low", "Safflower, sunflower"),
 (9, "5–6", "Med–high", "<b>High (high head)</b>", "High", "Camelina, canola"),
 (10, "5.5–6.5", "Med (passes)", "Med–high (north)", "Med", "Safflower, sunflower"),
 (11, "6–7", "Medium", "Low", "Low", "Safflower, soybean"),
 (12, "5–6", "Med (Isthmus v. high)", "High", "High", "Oil palm, coconut"),
 (13, "4.5–6", "<b>High (trade winds)</b>", "High (mountains)", "Med–high", "Oil palm, coconut"),
]

def build(D):
    h = ['<h1 class="part" id="p5"><small>Part 5</small>Region-by-Region Guide for North America</h1>']
    h.append('<p>The right energy mix depends on where you live. Use the map to find your region, then read its card for the best energy sources, the climate problems to design around, and the best oil crops for homemade diesel. “Peak sun hours” are the daily average hours of full-strength sunlight on a tilted panel (from NREL solar resource data, rounded); multiply by panel watts × ~0.75 for daily Wh.</p>')
    h.append(fig(D.region_map(), "<b>Figure 10. Regions used in this guide.</b>", "max-width:74%"))
    leg = '<div class="legend">' + "".join(f'<div><span class="c" style="background:{c}"></span>{k} {n}</div>' for k, (n, c) in REGIONS.items()) + '</div>'
    h.append(leg)
    h.append(table(["#", "Region", "Peak sun h/day (annual)", "Wind", "Hydro potential", "Firewood", "Top oil crops"],
        [[str(k), REGIONS[k][0], a, b, c, d, e] for k, a, b, c, d, e in SUMMARY], cls="brk"))
    h.append('<p class="small">* Arctic annual average hides an extreme swing: near zero in midwinter, very high in early summer. Values are approximate regional ranges; local terrain, elevation and microclimate dominate — measure your own site.</p>')
    h.append('<div class="regions">')
    for k, energy, chall, crops in R:
        nm, col = REGIONS[k]
        h.append(f'<div class="region"><div class="rh" style="background:{col}"><span class="n">{k}</span>{nm}</div><div class="rb"><p><b>Energy:</b> {energy}</p><p><b>Climate challenges:</b> {chall}</p><p><b>Oil crops &amp; diesel feedstocks:</b> {crops}</p></div></div>')
    h.append('</div>')
    return "\n".join(h)
