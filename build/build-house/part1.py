from common import *
import dg

def build():
    h = [part("p1", 1, "Planning: Shelter First, Then a Home")]
    h.append(h2("stages", "1.1 From emergency shelter to permanent home"))
    h.append('<p>In a grid-down emergency, people die of exposure long before they die of hunger. Hypothermia can kill in hours in wet, windy weather at temperatures well above freezing; heat stroke can kill in a day in the desert. So housing is built in <b>stages</b>: get out of the wind and wet tonight, get a warm, dry, defended room this season, and build a durable house over one to three years. Each stage buys time to do the next one properly.</p>')
    h.append(table(["Stage", "Time frame", "Typical shelter", "Goal"], [
        ["0 · Survival shelter", "Hours", "Vehicle, tent, tarp A-frame, debris hut, snow cave (quinzhee), lean-to with a fire", "Stay dry; insulate from the ground; block wind"],
        ["1 · Improved shelter", "Days–weeks", "Wall tent with a stove, half-dugout, pole-and-tarp hut, one heated room of an existing building", "Safe heat, cooking, sleep, storage"],
        ["2 · Core cabin", "One season", "12×16 ft to 16×24 ft (3.7×4.9 m to 4.9×7.3 m) cabin: log, stick frame from salvage, or straw bale", "Warm, weather-tight, defensible base"],
        ["3 · Permanent home", "1–3 years", "Expand the core: added rooms, root cellar, porch, sheds, better foundation, insulation, water and sanitation", "Comfort and durability for decades"]]))
    h.append(tip("Fix before you build", "The fastest permanent home is usually an <b>existing building</b>. A sound house with a good roof can be made livable by heating one or two rooms (close off the rest, hang blankets over doorways, add a wood stove with a proper chimney), fixing the roof, and adding insulation to the ceiling. Build new when no safe building exists, when the location is wrong (flood plain, too exposed, no water), or once you have time and materials."))
    h.append(fig(dg.shelters(), "Fast survival shelters (after U.S. Army FM 21-76, ch. 5). The most important layer is the insulation <i>under</i> you: 15–30 cm (6–12 in) of dry leaves, boughs or a foam pad — the ground pulls heat out faster than air."))
    h.append(check("Survival shelter checklist", [
        "Site: dry, out of the wind, not in a gully or dry wash (flash floods), not under dead trees or limbs (“widow-makers”)",
        "Insulate from the ground first; then roof; then walls. Small is warm — just big enough to lie down",
        "Ventilate any shelter with a fire or stove; never burn charcoal or run a generator or camp stove in a closed tent (carbon monoxide)",
        "Snow shelters: keep a vent hole open, keep a shovel inside, mark the outside so others can find you",
        "Upgrade daily: thicker roof, door plug, raised bed, drainage trench around the outside"]))

    h.append(h2("site", "1.2 Choosing a site"))
    h.append('<p>A good site makes every later job easier; a bad site cannot be fixed by good carpentry. Walk the land in the worst weather you can, and talk to anyone who knows its history of floods, fires and drifts. Rank the factors below — water and safety from floods come first.</p>')
    h.append(table(["Factor", "What you want", "Avoid"], [
        ["Water", "Spring, well or stream within a short walk (ideally uphill so it can flow to you); roof area for rain catchment", "Sites where water must be hauled long distances; downstream of mines, farms, industrial sites"],
        ["Drainage", "Gentle slope (2–10%) or a rise; soil that drains (sand, gravel, loam); dig a test hole — no standing water after rain", "Valley bottoms, wet clay, springs under the house site, low spots where cold air pools (frost pockets)"],
        ["Flood", "Well above the highest flood marks (debris lines, silt on trees); check FEMA flood maps while available", "Floodplains, river bends, dry washes in deserts, coastal surge zones"],
        ["Sun", "Clear view of the southern sky (N. hemisphere) from 9 a.m.–3 p.m. in winter; south- or southeast-facing slope", "North-facing slopes and deep valleys in cold climates — they can lose weeks of winter sun"],
        ["Wind", "Shelter from prevailing winter wind (hill, forest edge, windbreak); summer breezes in hot climates", "Exposed ridge tops (wind, lightning) in cold climates; still, airless hollows in hot-humid climates"],
        ["Fire", "Cleared ground or green, irrigated vegetation around the house; flat or gentle slope", "Tops of steep brushy slopes and narrow canyons (fire runs uphill fast); dense conifers touching the house"],
        ["Ground", "Firm, undisturbed mineral soil or bedrock; good building stone, clay and timber nearby", "Fill, peat, organic muck; landslide scars; expansive clay; known sinkholes; permafrost if avoidable"],
        ["Security", "Low visibility from main roads; one controllable approach; good sight lines from the house; neighbors you trust within reach", "Next to highways and large towns; visible ridge-line silhouettes; dead-end isolation with no help nearby"]]))
    h.append(caution("Defensibility without a fortress", "Concealment and community protect you better than walls. Keep the house out of sight from main routes, screen it with trees, avoid lights visible at night, and control the approach with a gate and a clear field of view. Thick earth, stone, cob and adobe walls and earth berms stop far more than thin wood-frame walls do. A solid door with a good bar, shutters that close from inside, and a second exit are worth more than anything elaborate."))
    h.append(fig(dg.site_plan(), "Example homestead layout. House on the sunny mid-slope above the flood line; water source uphill of the outhouse and at least 30 m (100 ft) from it; windbreak on the winter-wind side; fire-defensible zones (after NFPA Firewise home ignition zones)."))

    h.append(h2("size", "1.3 Sizing a small house and simple floor plans"))
    h.append('<p>Every square foot must be built, roofed, heated and maintained with hand tools. Build small, build it well, and design so you can add on later. A useful rule is <b>100–200 ft² (9–19 m²) per person</b> for the heated core, plus unheated storage, porch and sheds. A loft under a steep roof adds sleeping space almost for free.</p>')
    h.append(table(["Footprint", "Area", "Fits", "Notes"], [
        ["12 × 16 ft (3.7 × 4.9 m)", "192 ft² (18 m²)", "1–2 people", "One room + loft; a season's work for one person; easy to heat"],
        ["16 × 24 ft (4.9 × 7.3 m)", "384 ft² (36 m²)", "2–4 people", "Rafters/joists span 16 ft with standard sizes — good core cabin (Fig. 3)"],
        ["20 × 30 ft (6.1 × 9.1 m)", "600 ft² (56 m²)", "4–6 people", "Needs a center beam or interior bearing wall for floor/ceiling joists"],
        ["24 × 32 ft + loft", "768 ft² + loft", "6–8 people", "Two-story or loft; consider two cores joined by a breezeway"]], numcols=()))
    h.append(fig(dg.floor_plan(), "Core cabin, 16 × 24 ft. Stove in the center so heat reaches every room; kitchen, pantry and storage along the cold north wall; most windows face south; an unheated airlock entry keeps winter wind out. Expand later by adding a room to the east or west.", "max-width:68%"))
    h.append(check("Floor-plan rules of thumb", [
        "Rectangle about 1.5:1, long side facing south (within ~15–30° of true south)",
        "One central heat source and chimney; rooms open to it or with doors that can be left open",
        "Wet rooms (kitchen, wash area, toilet) together on one wall to share drains and greywater lines",
        "Two exits (door + escape window) from every sleeping area",
        "Entry vestibule/mudroom in cold or wet climates; shaded porch or breezeway in hot climates",
        "Keep spans to what your timber can carry (see span tables, Part 5); 12–16 ft (3.7–4.9 m) is easy with salvaged lumber or poles"]))

    h.append(h2("solar", "1.4 Passive solar orientation"))
    h.append('<p>A well-oriented house heats itself partly with winter sun and stays cooler in summer — free energy you never have to cut, haul or split. The U.S. DOE’s passive solar guide lists five elements: <b>aperture</b> (south windows within 30° of true south, unshaded 9 a.m.–3 p.m. in winter), <b>absorber</b> (a dark surface the sun hits), <b>thermal mass</b> (masonry, earth, stone or water that stores heat), <b>distribution</b> (natural airflow to other rooms), and <b>control</b> (overhangs, shutters, vents).</p>')
    h.append(fig(dg.passive_solar(40), "Passive solar section at 40°N. The overhang lets in low winter sun and blocks high summer sun. Find true south with a shadow stick: the shortest shadow of the day points true north (local solar noon)."))
    rows = []
    import math
    for lat in (20, 30, 40, 50, 60):
        w = 90-lat-23.45; s = 90-lat+23.45
        # overhang projection to shade a window whose bottom is 1.5 m below overhang at summer noon? use ratio: projection per metre of drop for full summer shade
        rows.append([f"{lat}°N", f"{w:.0f}°", f"{min(s,90):.0f}°", f"{1/math.tan(math.radians(min(s,89.9))):.2f}", f"{1/math.tan(math.radians(w)):.1f}"])
    h.append(table(["Latitude", "Winter noon sun height", "Summer noon sun height", "Overhang depth per 1 m (or ft) of window height for full summer shade", "Shadow length per 1 m height in winter (spacing to avoid shading)"], rows, numcols=(1,2,3,4)))
    h.append('<p class="small">Calculated from sun angle = 90° − latitude ± 23.45°. Example at 40°N: a window 1.2 m tall below the eave needs an overhang about 1.2 × 0.30 ≈ 0.4 m deep to be fully shaded at midsummer noon; at the winter solstice a 10 m tree casts a shadow ~20 m long, so keep tall trees well south of the house. In practice make overhangs a little deeper in hot climates and use deciduous trees or vines to shade the east and west sides.</p>')
    h.append(table(["Climate", "Glazing", "Mass", "Other"], [
        ["Cold (most of Canada, northern U.S., Rockies)", "South glass ≈ 7–12% of floor area; little glass north, east, west; insulated night shutters", "Masonry or earth floor/wall in sunlit area, insulated from ground", "Compact shape, airlock entry, earth berm on north"],
        ["Mixed / temperate", "South glass 7–10%; summer shading essential", "Moderate", "Cross-ventilation; deciduous trees south, evergreens north"],
        ["Hot-dry (deserts, N. Mexico)", "Small, shaded windows; high vents", "Heavy mass walls and floors (adobe, rammed earth) to ride out day–night swings", "Courtyards, light-colored roof, night ventilation"],
        ["Hot-humid (Gulf, Florida, tropics)", "Shaded windows on all sides for airflow", "Light construction — mass stores unwanted heat", "Raised floor, high ceilings, deep porches, wide eaves, roof ventilation"]]))
    return "\n".join(h)
