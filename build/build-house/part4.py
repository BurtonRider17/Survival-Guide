from common import *
import dg

def build():
    h = [part("p4", 4, "Wall Systems")]
    h.append('<p>Choose a wall system by what is <b>abundant where you are</b> (trees, straw, clay, stone, salvage), the <b>climate</b> (cold needs insulation; hot-dry likes mass; hot-humid likes light, ventilated walls), and the <b>hazards</b> (earthquake zones punish heavy unreinforced walls; termites punish wood near the ground). All walls share two rules: <b>a good hat and good boots</b> — a wide roof overhang and a foundation that keeps the wall above splash and ground water.</p>')
    h.append(h2("compare", "4.1 Comparing wall systems by climate"))
    h.append(table(["System", "Insulation (approx.)", "Labor / skill", "Best climates", "Weak points"], [
        ["Log (round or hewn)", "Softwood ≈ R-1.0–1.4 per inch; 10 in log ≈ R-12–14 (plus mass)", "High labor, moderate skill; many trees (60–100 for a 16×24)", "Cold forested: Alaska, Canada, Rockies, Great Lakes, Northeast", "Settling, gaps, rot at bottom logs; marginal insulation for −30° winters"],
        ["Timber frame + infill", "Depends on infill (straw-clay, straw bale, stud walls)", "High skill joinery; fewer, larger timbers", "Everywhere; classic in Northeast, PNW", "Needs good joinery; infill/enclosure is a second job"],
        ["Stick frame (salvaged lumber)", "2×4 cavity ≈ R-11–15; 2×6 ≈ R-19–21 (salvaged batts)", "Fastest; low skill; needs nails and lots of lumber", "Everywhere; best with salvage near towns", "Fire, termites, needs sheathing/bracing; poor without insulation"],
        ["Cordwood", "Wood ≈ R-1–1.5/in; insulated core helps — 16–24 in walls", "Moderate; uses short, cheap wood and lots of mortar", "Cold-temperate: Great Lakes, Northeast, Prairies", "Mortar shrinkage gaps, wood swelling, needs lime/cement"],
        ["Straw bale", "≈ R-1.3–1.5 per inch → R-27–33 for 18–23 in bales", "Fast walls; plastering is the big job", "Dry and cold: Plains, Prairies, Great Basin, Rockies valleys, SW", "Rots if wet — big overhangs, raised base, breathable plaster only"],
        ["Cob (clay-sand-straw)", "Poor ≈ R-0.2–0.3/in (mass only)", "Very slow; low skill", "Mild climates: Pacific coast, California, Southeast uplands, Mexico", "Cold, heavy, slow; erodes; earthquake risk unless reinforced"],
        ["Adobe / fired brick", "Poor ≈ R-0.2–0.3/in (mass)", "Moderate; brick making by season", "Hot-dry: SW, N. Mexico, Great Basin; brick everywhere with clay", "Unreinforced masonry collapses in earthquakes; needs bond beam"],
        ["Earthbag", "Soil fill poor; pumice/scoria fill better", "Moderate; few tools; quick", "Hot-dry, hurricane coasts, tropics; domes/vaults", "UV-degrades bags (plaster quickly); damp-rises if not on gravel"],
        ["Rammed earth", "Poor (mass) unless insulated", "Heavy labor; forms needed", "Hot-dry, mild: SW, California, Mexico", "Needs right soil (sandy, ~10–30% clay), forms, often cement; seismic reinforcement"],
        ["Stone", "Very poor ≈ R-0.1/in", "Very slow; skilled", "Anywhere stone is plentiful; foundations everywhere", "Cold and damp unless insulated inside; earthquake collapse if unreinforced"]], cls="brk", widths=["15%", "21%", "20%", "22%", "22%"]))
    h.append('<p class="small">R-values are approximate ranges from published tests and building-science sources; real performance depends on moisture, air leaks and workmanship. Heavy (“mass”) walls help in climates with big day–night swings but do not substitute for insulation in long cold winters.</p>')

    h.append(h2("log", "4.2 Log cabins: notching and chinking"))
    h.append('<p>The log cabin is the classic North American wilderness home because it needs nothing but trees, an axe and a saw. The USDA Forest Service’s <i>Building with Logs</i> (1945) is still a good free manual. Choose straight, evenly sized logs; alternate butt ends and top ends on each course so the walls rise level; and keep the bottom logs (sill logs) on a stone or concrete foundation at least 8 in (20 cm) above the ground — rot starts at the bottom.</p>')
    h.append(fig(dg.log_notches(), "Common corner notches. Saddle notches are easiest for beginners with round logs; dovetails suit hewn (squared) logs; full-scribe walls fit each log to the one below and need no chinking but take much longer."))
    h.append('<ol><li><b>Sill course:</b> lay the two side sills, then the two end logs notched over them. Flatten the bottom of sill logs; set on a capillary break.</li>'
             '<li><b>Raise courses:</b> roll logs up skids with ropes (parbuckling) or a gin pole. Notch each log to fit the one below; check the wall for plumb and level every course.</li>'
             '<li><b>Openings:</b> build the wall solid, then saw out door and window openings, and spike or peg vertical boards (bucks) to the log ends to hold them.</li>'
             '<li><b>Settling space:</b> leave a gap of about 2–3 in (5–8 cm) above every door and window frame (more for very green logs), filled loosely with insulation and covered with trim attached to the frame only — never nail the frame to the logs above.</li>'
             '<li><b>Roof:</b> extend the top logs (plates) as overhangs; use rafters, purlins on log gables, or ridge-pole construction (Part 5).</li>'
             '<li><b>Chink and finish:</b> after the first summer of drying, chink gaps and treat log ends; re-chink as needed. Oils and borate treatments slow decay.</li></ol>')
    h.append(tip("How many logs?", "A 16 × 24 ft cabin with 8 ft walls of 10 in logs needs about 10–12 courses × 4 walls ≈ 45–50 wall logs, plus gable logs or framing, rafters, joists and purlins: plan on <b>60–100 trees</b>. Cut in winter, peel, and let them season for a few months off the ground if you can."))

    h.append(h2("timber", "4.3 Timber framing basics"))
    h.append('<p>A timber frame is a skeleton of large posts and beams (typically 6×6 to 8×10 in) locked together with wooden joints and pegs, and braced diagonally. It needs fewer trees than a log house and lasts for centuries; the walls between the posts can be filled with whatever you have — straw-clay, straw bales, stud walls, brick nogging or wattle and daub. Frames are laid out on the ground in <b>bents</b> (cross-sections), raised with ropes and pike poles by a crew, then tied together with girts and plates.</p>')
    h.append(fig(dg.timber_joints(), "Basic timber-frame joints. The pegged mortise and tenon is the workhorse; offset (“drawbore”) the peg hole in the tenon about 3 mm (⅛ in) toward the shoulder so driving the peg pulls the joint tight. Knee braces stop the frame racking sideways in wind or earthquakes."))
    h.append(check("Timber-frame rules of thumb", ["Bents at 8–12 ft (2.4–3.7 m) spacing; keep spans modest for the timber you have",
        "Mortises no wider than ⅓ of the timber thickness; tenons 1½–2 in thick; leave 4 in+ of wood beyond a peg hole",
        "Pegs of straight-grained, dry oak or locust, ¾–1 in (19–25 mm), split rather than sawn",
        "Brace every post in both directions at corners; in earthquake country add hold-downs to the foundation",
        "Cut joints green; dry timbers shrink — keep critical surfaces where shrinkage tightens rather than loosens the joint"]))

    h.append(h2("stick", "4.4 Stick framing with salvaged lumber"))
    h.append('<p>Light wood framing with 2×4s and 2×6s (“stick framing”) is the fastest way to build if you have nails and a supply of lumber from abandoned buildings. It is described step by step in U.S. Army FM 5-426 <i>Carpentry</i> and CMHC’s <i>Canadian Wood-Frame House Construction</i>.</p>')
    h.append(fig(dg.wall_section(), "Wall section of a stick-frame wall from foundation to roof. Water is shed outside, air is stopped by sheathing and the interior finish, insulation fills the cavity, and moisture that gets in must be able to dry out (Building Science Corp. BSD-106).", "max-width:64%"))
    h.append(table(["Item", "Typical practice (one-story house, light roof)"], [
        ["Studs", "2×4 at 16 in (406 mm) centers or 2×6 at 24 in (610 mm); 2×6 holds more insulation. Max height ~10 ft"],
        ["Plates", "Single bottom (sole) plate; doubled top plate with joints offset ≥ 4 ft"],
        ["Corners", "Three studs per corner (or two plus blocking) to give nailing on the inside"],
        ["Headers over openings (doubled, on edge)", "2×6 to ~4 ft (1.2 m); 2×8 to ~5 ft (1.5 m); 2×10 to ~6 ft (1.8 m); 2×12 to ~7 ft (2.1 m). Halve these under heavy snow or a second floor"],
        ["Bracing", "Sheathe with plywood/OSB, or diagonal boards at 45°, or let in 1×4 diagonal braces at each corner. Without it, walls rack and fold"],
        ["Nails", "16d (3½ in) common for framing; 8d for sheathing every 6 in at edges, 12 in in the field. Straighten and reuse salvaged nails; screws work too"],
        ["Salvaged lumber", "Old 2× lumber is often full-sized (a true 2 × 4 in); mix sizes only if you plane or shim to a common face. Discard rotten or insect-damaged pieces"]]))
    h.append(caution("Salvaged lumber strength", "Grade stamps are usually gone and the species unknown. Use the conservative span tables in Part 5 and reduce spans a further ~25% for doubtful wood. Inspect for rot (soft when probed with a knife), splits through the depth, big knots on the bottom edge of beams, and notches cut by old plumbing."))

    h.append(h2("cordwood", "4.5 Cordwood masonry"))
    h.append('<p>Cordwood walls are built like a stack of firewood laid in mortar: short, debarked log rounds (typically 12–24 in / 30–60 cm long) set crosswise in the wall. Each mortar bed is split into an outer and inner bead with a core of insulation (sawdust treated with lime, or loose insulation) between them. They use wood too small or crooked for log building and are popular in Wisconsin, Ontario and the Northeast.</p>'
             '<ul><li>Use dry, debarked, rot-resistant softwood (cedar, tamarack, pine, spruce); dry for a year so the wood shrinks before it is set — wet wood shrinks away from the mortar and leaves gaps.</li>'
             '<li>Typical mortar: sand, sawdust (soaked), lime and Portland cement — e.g., roughly 9 sand : 3 sawdust : 3 lime : 2 cement by volume. Sawdust slows curing and reduces shrinkage cracking. See the Concrete &amp; Masonry volume for lime.</li>'
             '<li>Build within a post-and-beam frame or use stacked “cordwood corners” (crisscrossed squared timbers). Protect with a wide overhang; keep the first course well above splash.</li></ul>')

    h.append(h2("straw", "4.6 Straw bale"))
    h.append('<p>Straw — the dry stalks left after a grain harvest, not hay — baled tightly makes a thick, well-insulated wall for very little money. Straw bale construction has had its own appendix in the U.S. International Residential Code since 2015 (Appendix S/AS; Appendix BJ in 2024). Bales are either <b>load-bearing</b> (the roof sits on a wooden box beam on top of the bales) or <b>infill</b> in a post-and-beam frame (safer for beginners and heavy snow).</p>')
    h.append(check("Straw bale essentials", [
        "Bales: wheat, rice, oat, barley or rye straw, dense and dry — moisture content below about 20% when built; reject moldy or hot bales",
        "Raise bales on a foundation at least 8 in (20 cm) above grade, on a toe-up (wood sill with gravel between) and a moisture barrier underneath only",
        "Stack in running bond; pin and compress; stuff gaps with loose straw or straw-clay",
        "Plaster both sides with clay or lime plaster (2–3 coats, 1–2 in total); <b>never</b> use plastic sheeting or cement-only stucco that traps moisture",
        "Roof overhang 18–24 in (45–60 cm) or more; gutters; flash window sills carefully — most failures start at leaky sills",
        "Fire: plastered bale walls perform well in fire tests; loose straw on site is a major fire hazard — keep it swept and no smoking"]))

    h.append(h2("earth", "4.7 Earthen walls: cob, adobe, earthbag, rammed earth"))
    h.append('<p>Earthen walls use the subsoil under your feet. They are fireproof, pest-resistant, cool in hot-dry climates and nearly free — but heavy, slow, poor insulators, and dangerous in earthquakes if unreinforced. Test your soil: shake a jar one-third full of subsoil with water and a pinch of salt, let it settle a day, and read the layers (sand at the bottom, silt, then clay on top). A good building soil is roughly <b>15–30% clay</b> with the rest sand and silt; too much clay cracks, too little crumbles.</p>')
    h.append(table(["Method", "How it's made", "Key details"], [
        ["Cob", "Clay subsoil, sand and long straw mixed wet (by foot on a tarp) and built up by hand in “lifts” of 30–45 cm, pared to shape", "Walls 45–60 cm thick at base, tapering; let each lift firm before the next; sculptural, no forms. Best in mild, dry-summer climates"],
        ["Adobe", "Sun-dried bricks of sandy clay + straw or manure cast in wooden molds (e.g., 10 × 14 × 4 in), dried 2–4 weeks, laid in mud mortar", "Classic of the Southwest and Mexico (NPS Brief 5; NM Earthen Building Code). Brick making and firing are covered in the Concrete &amp; Masonry volume"],
        ["Earthbag", "Polypropylene sacks or tubes filled with damp soil (gravel at the base), laid in courses and tamped flat, with two strands of barbed wire between courses", "Few tools; good for domes, vaults and walls. Plaster within weeks — bags fail in sunlight (UV)"],
        ["Rammed earth", "Damp sandy-clay soil tamped in 15–20 cm layers inside strong forms to make monolithic walls 30–60 cm thick", "Needs sturdy forms and heavy tamping; often stabilized with 5–10% cement; very durable"]]))
    h.append(danger("Earthquakes and heavy walls", "Unreinforced adobe, cob, stone and brick walls are the deadliest kind of building in earthquakes. In seismic zones (Pacific coast, Alaska, Utah/Nevada, the Mississippi Valley’s New Madrid zone, Mexico, Central America and the Caribbean), use light wood framing instead — or build heavy walls short and thick, with buttresses at corners, a continuous wood or reinforced concrete <b>bond beam</b> on top tying all walls together, vertical reinforcement (bamboo, steel, or wood), small openings away from corners, and a light roof tied down to the bond beam. Mexico’s CENAPRED guide shows “confined masonry” with concrete tie-columns (castillos) and beams (dalas). Getty’s adobe retrofit guidelines show how straps and bond beams keep walls from falling apart."))

    h.append(h2("stone", "4.8 Stone walls"))
    h.append('<p>Stone lasts forever and is often free in New England, the Ozarks, the Appalachians, the Rockies and much of Mexico. Lay stone with the longest dimension into the wall, break joints (each stone covering a joint below), use frequent “through stones” that cross the full wall thickness, and keep walls at least 45 cm (18 in) thick. Lime mortar is traditional and kinder to soft stone (NPS Brief 2); details are in the Concrete &amp; Masonry volume. Stone is a poor insulator and feels cold and damp — in cold climates insulate the inside (a stud wall with insulation, or a straw-clay lining), or use stone for the foundation, chimney and a sun-warmed mass wall only.</p>')
    return "\n".join(h)
