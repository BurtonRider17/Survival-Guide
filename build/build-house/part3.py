from common import *
import dg

FROST = [
 (1, "Arctic & Subarctic", "Anchorage ≈ 3.5 ft (1.1 m); interior Alaska/Yukon/NWT 6–10+ ft or permafrost", "Gravel pad + posts/pads, adjustable; piles to stable frozen ground"),
 (2, "Pacific NW & BC", "Coast 12–18 in (0.3–0.45 m); interior WA/OR & BC interior 24–48 in (0.6–1.2 m)", "Piers or concrete footings; rubble trench works in wet coast"),
 (3, "Prairies & Great Plains", "OK/S. Kansas 18–24 in; Nebraska 36–42 in; Dakotas 48–60 in; Canadian Prairies 4–6+ ft (1.2–2 m)", "Deep piers, rubble trench, or frost-protected shallow foundation (insulated)"),
 (4, "Great Lakes & Midwest", "Missouri 18–30 in; Ohio/Indiana/Illinois 32–42 in; Michigan/Wisconsin 42–48 in; Minnesota 42–60 in; S. Ontario ≈ 4 ft", "Stone or concrete footings, rubble trench, piers"),
 (5, "Northeast & Atlantic Canada", "MD/DE/NJ 24–36 in; PA/NY 36–48 in; northern New England 48–60 in; Quebec/Maritimes 4–6 ft", "Fieldstone foundation, rubble trench, concrete"),
 (6, "Southeast & Gulf", "6–18 in (0.15–0.45 m); Appalachians 18–30 in", "Piers (brick, stone, treated or durable posts) raising the floor"),
 (7, "Florida", "None (0–6 in) — bear on firm soil ≥ 12 in down", "Raised piers; deep anchors against hurricane uplift"),
 (8, "Desert SW & Great Basin", "Low desert 0–12 in; high desert and Great Basin 24–36 in", "Stone or rubble trench under earthen walls; keep runoff away"),
 (9, "Rocky Mountains", "36–60 in; high valleys deeper (to 6 ft)", "Stone, concrete or deep piers; drain well"),
 (10, "California", "Coast & valleys 0–12 in; Sierra/Cascade/mountain areas 24–36+ in", "Continuous footings with anchor bolts (earthquake)"),
 (11, "Northern Mexico", "Lowlands none; Chihuahua & Sierra Madre highlands 12–24 in", "Stone (cimiento de piedra) under adobe"),
 (12, "Central & Southern Mexico", "None (frost rare even in highlands); go ≥ 12–24 in to firm soil", "Stone footing + reinforced concrete bond beam (dala) — CENAPRED"),
 (13, "Central America & Caribbean", "None; go ≥ 12–24 in to firm soil", "Stone/concrete footing + bond beam; raised piers in flood/hurricane areas")]

def build():
    h = [part("p3", 3, "Foundations")]
    h.append('<p>The foundation does three jobs: it carries the weight of the house to firm ground, it keeps wood and earth walls <b>dry</b> by lifting them above splash and ground moisture, and in cold climates it keeps <b>frost heave</b> from lifting and cracking the building. The companion <i>Survival Info: Concrete &amp; Masonry</i> volume covers mixing concrete and lime, making brick, and laying stone and block in depth; this part gives the basics you need to choose and lay out a foundation.</p>')
    h.append(h2("ftypes", "3.1 Foundation types"))
    h.append(fig(dg.foundations(), "Four foundations that can be built by hand. Footings must rest on firm, undisturbed mineral soil below the topsoil — and below the local frost line in cold climates — unless they are insulated as a frost-protected shallow foundation (HUD guide).", "max-width:64%"))
    h.append(table(["Type", "Best for", "Materials", "Pros", "Cons"], [
        ["Pier / post (stone, brick, concrete, or rot-resistant posts on pads)", "Wood-frame and log cabins, slopes, termite and flood areas, permafrost", "Stone, salvaged block, short concrete piers, durable heartwood posts", "Fast, little material, airflow under floor, easy to level, works on slopes", "Must brace against racking/earthquake; floor needs insulation and skirting; not for earthen walls"],
        ["Rubble trench", "Earthen, straw bale, cordwood walls; wet sites", "Washed stone 2–5 cm, perforated drain pipe, stone or concrete grade beam on top", "Drains water away so it cannot freeze under the house; little or no cement", "Needs a lot of clean stone and a downhill outlet; grade beam still needed"],
        ["Stone foundation wall (dry-laid or mortared)", "All wall types; historic standard", "Fieldstone, lime or cement mortar", "Lasts centuries, local materials, supports heavy walls", "Labor-intensive; dry-laid needs big flat stones and wide base"],
        ["Concrete footing + stem wall or slab", "Heavy walls, seismic zones, permanent homes", "Cement, sand, gravel, rebar, forms", "Strongest; anchor bolts resist earthquakes and wind", "Needs cement (scarce later); 1 m³ ≈ 2.4 tonnes to mix by hand"]]))
    h.append(h2("frost", "3.2 Frost depth by region"))
    h.append('<p>Frost heave happens when water in fine-grained soil freezes into ice lenses that lift whatever is above. Footings must go <b>below the deepest frost penetration</b>, onto soil that drains, or be protected by insulation. Values below are typical design depths for the bottom of a footing; local values vary with soil, snow cover and elevation — ask local builders or look up the adopted code value while you still can, and when in doubt go deeper.</p>')
    h.append(table(["#", "Region", "Typical footing depth for frost", "Practical foundation"], [[str(a), b, c, d] for a, b, c, d in FROST], cls="brk", widths=["4%", "20%", "46%", "30%"]))
    h.append(caution("Footings in every climate", "Even where it never freezes, dig below topsoil and roots to firm, undisturbed soil — at least 12 in (30 cm) — and make the footing about <b>twice as wide as the wall</b> it carries (wider on soft clay). Keep all wood at least 8 in (20 cm) above the soil and 6 in (15 cm) above paving; put a capillary break (metal flashing, tar paper, slate, plastic, or a gravel course) between masonry and wood or earthen walls."))
    h.append(check("Foundation layout and build sequence", [
        "Set batter boards 1–1.5 m outside each corner; stretch string lines; square with 3-4-5 and equal diagonals; level with a water level",
        "Dig footings to firm soil and below the frost line; keep trench bottoms flat and free of loose soil",
        "Lay drain (stone + perforated pipe, or a stone-filled French drain) sloping to daylight at least 1:100",
        "Build footing and wall/piers; bring top at least 8 in (20 cm) above finished grade",
        "Earthquake and hurricane zones: embed anchors — ½ in (12 mm) bolts about every 6 ft (1.8 m) and within 12 in (30 cm) of each corner and end are a common code minimum",
        "Install capillary break and sill gasket; termite shield (sheet metal with a downward lip) in termite areas",
        "Backfill so the ground slopes away ~15 cm in the first 3 m (6 in per 10 ft)"]))
    h.append(tip("Shallow footings in deep-frost country; permafrost", "<b>Frost-protected shallow foundation:</b> instead of digging 4–5 ft down, a 12–16 in footing can be protected with rigid foam (salvaged XPS/EPS) on the outside of the foundation plus horizontal “wings” 2–4 ft out under the soil, wider at corners; ground and house heat keep the soil under the footing from freezing (HUD FPSF guide; heated buildings only). <b>Permafrost:</b> a heated building thaws the ground and sinks unevenly — <i>if it's frozen, keep it frozen</i> (CCHRC): gravel pad, undisturbed moss, floor raised on adjustable posts or piles with cold air flowing underneath, roof water drained far away."))
    return "\n".join(h)
