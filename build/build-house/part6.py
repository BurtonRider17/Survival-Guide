from common import *
import dg

def build():
    h = [part("p6", 6, "Doors, Windows, Insulation &amp; Moisture")]
    h.append(h2("doors", "6.1 Doors"))
    h.append('<p>The simplest strong door is a <b>board-and-batten (ledged and braced) door</b>: vertical tongue-and-groove or butted boards held by two or three horizontal ledges and a diagonal brace in a Z. The diagonal must run <b>upward from the bottom hinge side toward the latch side</b> so it is in compression and holds the door from sagging. Hang it on long strap hinges with bolts or clinched nails. In cold climates, double up the boards with felt or insulation between them, and add weatherstrip (felt, rubber, leather) around the stop.</p>')
    h.append(check("Door and entry checklist", [
        "Outswing doors resist wind-driven rain and forced entry better in hurricane areas; inswing doors can't be blocked by snow drifts — choose for your climate",
        "Solid door + steel bar in brackets on the inside for security; hinges on the inside or with non-removable pins",
        "Airlock/mudroom entry (two doors) in cold climates cuts heat loss and keeps snow out",
        "Every bedroom has a second way out: a window at least ~20 in wide × 24 in high (5.7 ft² clear opening is the U.S. code size) with a sill no higher than 44 in"]))
    h.append(h2("windows", "6.2 Windows, salvaged glass and shutters"))
    h.append('<p>Glass is one of the few building materials you cannot practically make by hand, so salvage every intact window and pane you can: from abandoned houses, cars (tempered glass — cannot be cut), shower doors, picture frames, and greenhouse panels. Keep salvaged sashes whole and build the rough opening to fit them; the frame is easier to make than the window.</p>'
             '<ul><li><b>Install:</b> rough opening ½ in (12 mm) larger than the window; sloped sill; flashing or tar-paper “shingled” so water runs out over the siding; header above (see 4.4). In log walls, allow settling space above.</li>'
             '<li><b>Double glazing:</b> two salvaged panes in one frame with a 12–20 mm (½–¾ in) sealed air gap roughly halves heat loss compared with a single pane. A storm sash or tight plastic film on the inside does nearly as well.</li>'
             '<li><b>Cutting glass:</b> score once with a wheel cutter along a straightedge, tap under the score, snap over a dowel. Wear gloves and eye protection. Tempered glass shatters into cubes — use it whole.</li>'
             '<li><b>No glass?</b> Oiled paper or muslin, polycarbonate or clear plastic film.</li></ul>')
    h.append(tip("Insulating shutters", "Windows lose 5–10 times more heat than an insulated wall. Interior shutters or panels of 1–2 in rigid foam, wool or straw-filled boxes, fitted tightly into the window frame at night, can cut window heat loss dramatically and also keep lamplight from showing outside at night. Exterior plank shutters with a bar protect glass from hurricanes, hail and intruders; in hurricane zones use plywood ≥ ⅝ in (16 mm) fastened to the framing."))
    h.append(h2("insulation", "6.3 Insulation from natural and salvaged materials"))
    h.append('<p>Insulation works by trapping still, dry air. Anything fluffy, dry and pest-proof insulates; anything dense (stone, earth, concrete) does not. The <b>ceiling/roof comes first</b> (warm air rises), then walls, then floors and foundations. Stop air leaks before adding insulation — a gap the width of a pencil around a window can lose as much heat as the wall around it.</p>')
    h.append(table(["Material", "R per inch (approx.)", "Notes"], [
        ["Rigid foam boards (salvaged XPS / EPS / polyiso)", "4–6.5", "Best salvage for roofs, foundations (FPSF) and under slabs; protect from sun and fire; polyiso loses R in deep cold"],
        ["Wool (sheep)", "3.5–3.8", "Wash, treat with borax against moths; handles damp well"],
        ["Cellulose (newspaper shredded and treated)", "3.2–3.8", "Treat with borax/boric acid (~15–20% by weight) for fire and pests; dense-pack in walls"],
        ["Fiberglass or mineral wool (salvaged batts)", "3.0–4.0", "Wear mask, gloves, long sleeves; discard wet or rodent-soiled"],
        ["Wood shavings / sawdust (dry)", "2.0–2.4", "Mix with ~5–10% lime (pests, mold, fire); settles 10–20% — top up attics; keep dry"],
        ["Straw bales / loose straw", "1.3–1.5 (bale); ~1–1.5 loose", "Must stay dry; use with breathable plaster (straw-clay ‘light clay’ ≈ R-1)"],
        ["Dry moss, leaves, cattail fluff", "≈ 1–2 (varies)", "Emergency/chinking; compacts and harbors pests"],
        ["Snow (fresh, dry)", "≈ 1", "Bank snow against walls in winter; build snow shelters"],
        ["Softwood / hardwood", "≈ 1.0–1.4 / 0.7–0.9", "Logs are only moderate insulators"],
        ["Earth, adobe, cob, brick, concrete", "0.1–0.3", "Thermal mass, not insulation"],
        ["Stone", "≈ 0.05–0.1", "Insulate the inside if you live within it"]], cls="brk", widths=["32%", "18%", "50%"]))
    h.append(table(["Climate", "Ceiling/roof target", "Walls", "Floor"], [
        ["Very cold (Alaska, Yukon/NWT, Prairies, N. Minnesota, N. Quebec)", "R-49 to R-60 (12–18 in of loose fill)", "R-25 to R-40", "R-30 + skirting"],
        ["Cold (Great Lakes, Northeast, Rockies, BC interior)", "R-49", "R-20 to R-30", "R-25 to R-30"],
        ["Mixed (mid-Atlantic, Ohio Valley, PNW coast, Great Basin)", "R-38 to R-49", "R-13 to R-21", "R-19 to R-25"],
        ["Hot (Gulf, Florida, deserts, Mexico lowlands)", "R-30 to R-38 + light roof color, attic ventilation or radiant barrier", "R-13 (or mass walls)", "Little needed; raise floor"]]))
    h.append('<p class="small">Targets follow the U.S. DOE/ENERGY STAR recommendations by climate zone (rounded). In a grid-down situation every point of R-value saves firewood you would otherwise have to cut.</p>')
    h.append(h2("moisture", "6.4 Ventilation and moisture control"))
    h.append('<p>Most old houses rot from water, not age. Moisture comes from <b>rain</b> (the largest source), <b>ground</b> moisture, and <b>indoor air</b> — people, cooking, drying clothes and unvented heaters all add water vapor. Building Science Corporation’s rule: keep water out, and when it does get in, let it dry out (BSD-106, BSD-013).</p>')
    h.append(check("Moisture control checklist", [
        "Wide roof overhangs, gutters, and ground sloping away from the house; splash blocks under downspouts",
        "Foundation top ≥ 8 in (20 cm) above grade; capillary break under sills and earthen/bale walls",
        "Rainscreen gap behind siding; flashing at every window, door and roof penetration — lap every layer like shingles",
        "Ground cover in crawl spaces: overlapping plastic sheet or a thick gravel layer; vents (about 1 ft² per 150 ft² of crawl area) or a sealed, insulated crawl",
        "Cold climates: air-tight, vapor-retarding layer on the warm (inside) face; hot-humid climates: no interior plastic — let walls dry inward",
        "Ventilate roofs or attics (eave + ridge vents) to remove moisture and prevent ice dams",
        "Keep indoor relative humidity about 30–50% (EPA): vent cooking and bathing moisture, dry clothes outdoors or near the stove with a window cracked",
        "Fix leaks within 24–48 hours; dry or discard anything moldy (EPA)"]))
    h.append(caution("Fresh air and radon", "A tight house with a wood stove, oil lamps and several people needs fresh air: open windows briefly twice a day (a few minutes of cross-draft), and give the stove its own outside combustion-air inlet if possible. Radon, a radioactive soil gas and the second-leading cause of lung cancer in the U.S. (EPA), builds up in tight basements and earth-sheltered rooms — ventilate them and seal floor cracks."))
    return "\n".join(h)
