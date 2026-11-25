import sys; sys.path.insert(0, '/workspace/survival-info/_common'); sys.path.insert(0, '/workspace/survival-info/build-steel')
from guidekit import *
from dg import *
def c(*n): return '<span class="cite">[' + ",".join(str(x) for x in n) + ']</span>'
EXTRA = """<style>
.tierA{border-left:6px solid #2e7d32;background:#eaf6ea;padding:2px 12px;border-radius:5px;margin:8px 0}
.tierB{border-left:6px solid #1565c0;background:#eaf2fb;padding:2px 12px;border-radius:5px;margin:8px 0}
.tierC{border-left:6px solid #6a1b9a;background:#f3eafb;padding:2px 12px;border-radius:5px;margin:8px 0}
.tag{display:inline-block;font-size:9pt;font-weight:700;border-radius:4px;padding:1px 7px;color:#fff;margin-right:4px}
.tag.a{background:#2e7d32}.tag.b{background:#1565c0}.tag.c{background:#6a1b9a}
</style>"""
def tier(code, h, body):
    k = code.lower(); return f'<div class="tier{code}"><h3><span class="tag {k}">TIER {code}</span>{h}</h3>{body}</div>'

TOC = [("p1", "Part 1 · Iron and Steel Basics", [("what", "1.1 What iron and steel are"), ("levels", "1.2 Three tech levels"), ("reality", "1.3 A reality check: what one smelt yields")]),
 ("p2", "Part 2 · Finding and Preparing Iron Ore", [("bog", "2.1 Bog iron"), ("rock", "2.2 Magnetite, hematite, limonite and sand iron"), ("roast", "2.3 Testing, roasting and crushing ore")]),
 ("p3", "Part 3 · Making Charcoal", [("whychar", "3.1 Why charcoal"), ("pit", "3.2 Pit and earth-mound kilns"), ("charsize", "3.3 Sizing and storing charcoal")]),
 ("p4", "Part 4 · The Bloomery Furnace", [("build", "4.1 Building a clay short-shaft furnace"), ("air", "4.2 Bellows, blowers and the tuyere"), ("smelt", "4.3 Running a smelt"), ("bloom", "4.4 Consolidating the bloom")]),
 ("p5", "Part 5 · From Iron to Steel", [("carb", "5.1 Case hardening (pack carburizing)"), ("blister", "5.2 Cementation: blister and shear steel"), ("crucible", "5.3 Crucible steel"), ("fining", "5.4 Finery and puddling: wrought iron from cast iron"), ("bulk", "5.5 Industrial steel: Bessemer to electric arc")]),
 ("p6", "Part 6 · Identifying Steel and Recycling Scrap", [("spark", "6.1 The spark test"), ("filetest", "6.2 File, magnet and hardening tests"), ("scrap", "6.3 Scrap steel: what to keep and what to avoid")]),
 ("p7", "Part 7 · The Forge and Its Tools", [("forge", "7.1 Building a forge"), ("anvil", "7.2 Anvils and anvil substitutes"), ("tools", "7.3 Tongs, hammers, hardies and the post vise")]),
 ("p8", "Part 8 · Forging Techniques", [("colors", "8.1 Reading heat colors"), ("moves", "8.2 Drawing out, upsetting and bending"), ("punch", "8.3 Punching and drifting"), ("weld", "8.4 Forge welding and flux")]),
 ("p9", "Part 9 · Heat Treatment", [("norm", "9.1 Normalizing and annealing"), ("harden", "9.2 Hardening and quenching media"), ("temper", "9.3 Tempering by color")]),
 ("p10", "Part 10 · Making Basic Tools", [("knife", "10.1 A knife blade (a working tool)"), ("chisel", "10.2 Cold chisel and center punch"), ("nails", "10.3 Nails and hooks"), ("hinge", "10.4 Strap hinge and pintle")]),
 ("p11", "Part 11 · Casting, Wire, Rolling and Sheet", [("cast", "11.1 Sand casting iron"), ("wire", "11.2 Drawing wire"), ("roll", "11.3 Rolling and slitting"), ("sheet", "11.4 Simple sheet work and rivets")]),
 ("p12", "Part 12 · Safety at the Furnace and Forge", [("burns", "12.1 Burns, eyes and hearing"), ("gas", "12.2 Carbon monoxide and toxic fumes"), ("quenchfire", "12.3 Quench fires and wet-ground explosions")]),
 ("p13", "Part 13 · Iron and Steel Region by Region", []),
 ("srcs", "Quick Reference & Sources", [])]

R = {
 1: "Bog and lake ores form in boreal wetlands; the Norse smelted bog iron in a bloomery at L'Anse aux Meadows, Newfoundland, around 1000 AD " + c(5) + ". Spruce and birch make workable charcoal. Short summers limit smelting season; dry ore and charcoal under cover all winter. Scrap from abandoned vehicles and machinery is the fastest source of steel.",
 2: "Wet climate: store charcoal under a roof and dry clay furnaces slowly (4.1). Alder, maple and Douglas-fir make charcoal. Black magnetite-rich beach sands occur on some Pacific shores — test with a magnet (2.2) " + c(8, 11) + ". Logging, rail and marine scrap is abundant.",
 3: "Few trees for charcoal; plan woodlots and use river-bottom hardwoods (Fire guide). Farm scrap is the main steel source: leaf springs, plow shares, disc blades, harrow teeth and old implements (6.3). Coal seams in parts of the plains can fuel a forge once you learn to coke it.",
 4: "The Lake Superior ranges (Mesabi and others) hold the largest US iron deposits: historic direct-shipping hematite and today's taconite, a hard rock of about 25–30% iron that needs crushing and magnetic separation " + c(7, 6) + ". Hand-scale smelters should look for richer hematite pockets or bog ore instead. Excellent hardwood charcoal; huge scrap supply in rust-belt cities.",
 5: "Colonial North America ran on bog iron: Saugus Iron Works (1646–1668) in Massachusetts used local bog ore, and New Jersey bog ore made tools and rails " + c(5, 50) + ". In Quebec the Forges du Saint-Maurice near Trois-Rivières (from 1730) used local ore " + c(61) + ". The Adirondacks hold large magnetite deposits " + c(8) + ". Hardwoods for charcoal are plentiful.",
 6: "Bog and limonite ores occur in coastal-plain wetlands; Virginia's Falling Creek ironworks (1619) was the first blast-furnace site in North America " + c(5) + ". Humid air rusts stock fast — oil tools and store charcoal dry. Oak, hickory and pine make charcoal (pine is softer and burns faster).",
 7: "Little workable ore; rely on scrap (vehicles, boat trailers, rebar from storm debris) and careful recycling (6.3). Salt air rusts steel quickly — keep tools oiled. Hurricane debris provides charcoal wood once dried.",
 8: "Dry air is ideal for drying clay furnaces and charcoal. Mesquite, juniper and oak make dense charcoal but grow slowly. Mining districts have hematite and magnetite outcrops, plus abandoned mine scrap (rails, cable, drill steel). Watch fire danger in dry season.",
 9: "Many mining districts with iron-oxide minerals and abandoned rail, cable and machinery. Beetle-killed pine is a large charcoal source. High altitude means less oxygen per breath — pace heavy bellows and hammer work, and keep forges outdoors or well ventilated (12.2).",
 10: "Black sands with magnetite are found in California " + c(8) + "; separate them with a magnet. Oak makes excellent charcoal. Strict wildfire caution: smelt and forge only on cleared mineral ground with water ready.",
 11: "Dry country good for clay and charcoal drying; mesquite charcoal burns hot. Mining districts and ranch scrap supply iron and steel. Shade the work area — heat stress plus forge heat is dangerous.",
 12: "Highland pine-oak forests supply charcoal; fuelwood is scarce in some areas, so use efficient pit or mound kilns (3.2). Village blacksmithing traditions survive; learn from local smiths.",
 13: "Humid tropics: dry charcoal and ore under roofs, and fire clay furnaces slowly to avoid cracking. Volcanic black sands on some coasts may be magnetic — test with a magnet. Vehicle and agricultural scrap is the most practical steel source.",
}

def body():
    b = [EXTRA]
    b.append(caution("How to use this guide", "Parts 1–5 explain how iron and steel are made, from ore in a bog to an industrial converter. Parts 6–11 are the hands-on smithing chapters: most people will start by <b>recycling scrap steel</b> (Part 6) in a <b>simple forge</b> (Part 7). Read Part 12 (safety) before lighting any furnace. Patents with drawings, sorted by tech level, are in the appendix. This guide covers tools and building hardware only — no weapons, gun parts or armor."))
    # ---------- Part 1
    b.append(part("p1", "Part 1", "Iron and Steel Basics"))
    b.append(h2("what", "1.1 What iron and steel are"))
    b.append("<p>Iron is almost never found as metal. It occurs as oxides — magnetite, hematite and hydrated oxides such as limonite and bog ore — and must be <b>reduced</b>: the oxygen is stripped off by carbon monoxide from burning charcoal or coke " + c(4, 6) + ". What you get depends on how much carbon ends up dissolved in the iron " + c(29, 18) + ":</p>")
    b.append(fig(d_carbon(), "Figure 1. The carbon scale. Wrought iron and mild steel forge and weld easily; high-carbon steel can be hardened; cast iron melts and pours but cannot be forged."))
    b.append(table(["Material", "Carbon", "Behavior and uses"], [
        ["Wrought iron", "very low, with glassy slag fibers", "Soft, tough, forge-welds easily, resists rust; made in bloomeries and puddling furnaces " + c(18)],
        ["Low-carbon (mild) steel", "about 0.05–0.3%", "Most common steel today; bends, welds; nails, wire, sheet, rebar " + c(29)],
        ["Medium-carbon steel", "about 0.3–0.6%", "Stronger; can be hardened somewhat; axles, hammers, axes " + c(29)],
        ["High-carbon steel", "about 0.6–1.0% (up to ~2%)", "Hardens hard in a quench; springs, files, blades, chisels " + c(29)],
        ["Cast (pig) iron", "about 2–4%", "Melts at a lower temperature; casts well; brittle; made in blast furnaces " + c(24)]]))
    b.append(h2("levels", "1.2 Three tech levels"))
    b.append("<p>This guide is organized by the same tiers used in the patent appendix. Tier A can be done by a small group with clay, wood, stones and hand tools. Tier B needs a workshop: firebrick, a hand-crank blower, crucibles, a lathe or a water wheel. Tier C is a rebuilt industry.</p>")
    b.append(fig(d_tiers(), "Figure 2. The path from hand-built bloomery to industrial steel. You can enter at any level — recycling scrap steel (Part 6) needs no smelting at all."))
    b.append(h2("reality", "1.3 A reality check: what one smelt yields"))
    b.append("<p>Experimental smelters in Virginia (Lee Sauder and Skip Williams) documented a typical efficient smelt: <b>40.5 kg of ore</b> and <b>94 kg of charcoal</b> over <b>5½ hours</b> produced a <b>14 kg bloom</b> — 60% of the iron in the ore " + c(1) + ". Forging a similar bloom down to finished bar by hand cut the yield to about 21% of the iron in the ore, and the whole chain used roughly <b>80 kg of charcoal per kg of finished bar</b> " + c(1) + ".</p>")
    b.append(tip("What this means for a community", ul(["Smelting is a team job: bellows or blower crew, charcoal crew, and smiths.", "Charcoal is the real bottleneck — plan woodlots and kilns first (Part 3).", "Every piece of scrap steel you save is worth many hours of smelting. Collect and sort it now (6.3).", "Learn smithing on scrap before attempting a smelt; the same skills consolidate a bloom."])))
    # ---------- Part 2
    b.append(part("p2", "Part 2", "Finding and Preparing Iron Ore"))
    b.append(h2("bog", "2.1 Bog iron"))
    b.append("<p><b>Bog iron</b> forms where iron-bearing groundwater seeps into wetlands; iron dissolved by acidic bog water is deposited, often with the help of bacteria, as lumps and crusts of hydrated iron oxide (limonite) along stream margins and bog edges " + c(5, 2) + ". It was the ore of the Norse in Newfoundland and of the first colonial ironworks, and it renews itself over decades " + c(5) + ".</p>")
    b.append(check("Finding bog ore", ["Look for orange-brown slime, rusty water and oily-looking sheens on still water below bogs and springs.", "Probe stream banks and wet meadows with a steel rod; ore lumps feel gritty and hard below the turf.", "Good ore is dark brown to rusty, heavy for its size, and leaves a yellow-brown streak.", "Experimental smelters advise at least about 50% iron in the ore; lighter, sandy material wastes charcoal " + c(2) + "."]))
    b.append(h2("rock", "2.2 Magnetite, hematite, limonite and sand iron"))
    b.append(table(["Ore", "Formula", "How to recognize", "Notes"], [
        ["Magnetite", "Fe₃O₄", "Black, heavy, <b>strongly attracted to a magnet</b>, black streak", "Large deposits in the Adirondacks; black sands in California " + c(8)],
        ["Hematite", "Fe₂O₃", "Red to steel-gray, <b>red-brown streak</b> on unglazed tile, weakly magnetic or not", "Main historic Lake Superior ore " + c(9, 7)],
        ["Limonite / bog ore", "FeO(OH)·nH₂O", "Yellow-brown to dark brown, earthy, <b>yellow-brown streak</b>", "Roast before smelting " + c(10, 5)],
        ["Iron sand", "mostly magnetite", "Black grains in beach or river sand; collect with a magnet in a bag", "Smelted historically in many places " + c(11, 8)],
        ["Taconite", "magnetite + hematite in hard rock", "Banded, very hard rock, 25–30% iron", "Industrial only: crushing and magnetic separation " + c(7)]]))
    b.append(tip("The streak test", "Rub the ore on the back of an unglazed ceramic tile. Magnetite leaves a black streak, hematite red-brown, limonite yellow-brown. Combine this with the magnet test and the weight of the lump."))
    b.append(h2("roast", "2.3 Testing, roasting and crushing ore"))
    b.append(steps(["<b>Wash and pick:</b> remove clay, roots and stones by hand.", "<b>Roast:</b> pile the ore on a wood fire or in a shallow pit and keep it red-hot for an hour or more. Roasting drives off water, makes rock ores easier to crush and bakes out some impurities " + c(4) + ". Limonite turns red (hematite) when roasted.", "<b>Crush:</b> break the roasted ore with a hammer on a flat stone. Experimenters aim for <b>pea- to rice-size (about 2–5 mm)</b>, keeping the dust " + c(2) + ".", "<b>Test smelt:</b> try a few kilograms before committing a whole day's charcoal."]))
    # ---------- Part 3
    b.append(part("p3", "Part 3", "Making Charcoal"))
    b.append(h2("whychar", "3.1 Why charcoal"))
    b.append("<p>Charcoal is nearly pure carbon; it burns hot and makes the carbon monoxide that reduces ore in a bloomery " + c(4) + ". It burns above 1,100 °C and its heat can be controlled by controlling the air, which is why smiths still use it " + c(15) + ". Wood dried and heated to about 280 °C breaks down by itself into charcoal, tar and gas; carbonizing at about 500 °C gives charcoal of about 85% fixed carbon at a yield of about a third of the dry wood weight, not counting wood burned to heat the kiln " + c(12) + ".</p>")
    b.append(h2("pit", "3.2 Pit and earth-mound kilns"))
    b.append(tier("A", "Miniature pit (small batches)", "<p>Dig a pit up to about a cubic meter. Light a strong fire in it with dry small fuel, keep adding wood until full, then cover with about <b>20 cm of leaves</b> and <b>20 cm of earth</b>. Leave to finish; it can be opened in about two days. Have water ready — charcoal can re-ignite when unloaded " + c(13) + ".</p>"))
    b.append(tier("A", "Earth mound (larger batches)", "<p>Stack dry wood tightly in a dome around a central flue, cover with leaves or grass and then earth, light it through the flue and control the burn with small vents at the base, closing them as the burn finishes " + c(14) + ". Drier wood gives more charcoal: air-dried wood still holds 12–18% water, fresh wood far more " + c(12) + ".</p>"))
    b.append(fig(d_mound(), "Figure 3. Earth-mound charcoal kiln. Seal any hole where flame breaks through; a mound left unwatched burns to ash."))
    b.append(danger("Charcoal kilns make carbon monoxide", "Never make or store hot charcoal in a closed building, and never burn charcoal indoors for heat. Carbon monoxide is colorless and odorless (12.2) " + c(48) + "."))
    b.append(h2("charsize", "3.3 Sizing and storing charcoal"))
    b.append(ul(["For a 25–30 cm bloomery, break and screen charcoal to <b>walnut-to-pea size (about 25–5 mm)</b>. Large pieces let ore fall through too fast; too many fines choke the air " + c(2) + ".", "For the forge, use slightly smaller pieces and keep a deep bed of coals.", "Store charcoal dry and under cover; wet charcoal wastes heat driving off water.", "Hardwoods give denser charcoal that lasts longer in the fire."]))
    # ---------- Part 4
    b.append(part("p4", "Part 4", "The Bloomery Furnace"))
    b.append("<p>A bloomery is a pit or short chimney of clay, earth or stone with an air pipe (tuyere) near the bottom. Charcoal and ore go in the top; the ore is reduced to solid iron <b>without melting</b>, and the iron particles collect in a pool of slag at the bottom as a spongy lump called the <b>bloom</b> " + c(4) + ". Small teams of North American smiths have refined this to a reliable method over hundreds of smelts " + c(2, 3) + ".</p>")
    b.append(h2("build", "4.1 Building a clay short-shaft furnace"))
    b.append(fig(d_furnace(), "Figure 4. Short-shaft bloomery with dimensions from published North American experimental smelts " + c(2, 3) + "."))
    b.append(table(["Feature", "Proven value", "Why"], [
        ["Inside diameter", "25–30 cm", "Below ~20 cm loses too much heat; above 30 cm uses huge amounts of charcoal " + c(2)],
        ["Walls", "5–10 cm thick; clay + coarse sand (often more sand than clay) or clay + chopped straw about 50/50 by volume", "Sand limits cracking; straw vents steam and reinforces " + c(2)],
        ["Below the tuyere", "15–20 cm", "Room for the slag bowl and bloom " + c(2)],
        ["Above the tuyere", "at least 40 cm (total 65–75 cm)", "Working column of hot reducing gas " + c(2)],
        ["Tuyere", "20–25° down, tip about 5 cm inside the wall", "Too flat drowns in slag; too steep erodes the bloom " + c(2)],
        ["Tap arch", "about 20 cm wide × 15 cm high at the base", "Draining slag; a full-width arch lets you pull the bloom out " + c(2)]]))
    b.append(steps(["Choose a dry, level, sheltered spot with room to work on all sides; clear anything that can burn.", "Mix clay with sand or chopped straw; build the walls up in rings without pressing down (pressing slumps the wall).", "When leather-hard, cut the tuyere hole and the tap arch; wrap the tap block in paper and push it back in place " + c(2) + ".", "Dry completely. Air-dry, then run a small, gentle wood fire inside and out. Wet walls crack or spall when fired " + c(2) + "."]))
    b.append(h2("air", "4.2 Bellows, blowers and the tuyere"))
    b.append("<p>The air blast is the single most critical setting. Sauder and Williams found the best range is about <b>1.2–1.5 liters per minute for each square centimeter</b> of furnace cross-section at tuyere level " + c(1, 2) + " — roughly <b>600–750 L/min for a 25 cm furnace</b> and <b>850–1,050 L/min for a 30 cm furnace</b>. The blast must not stop: a pause of 3–5 minutes can freeze the slag and ruin the smelt " + c(2) + ".</p>")
    b.append(fig(d_bellows(), "Figure 5. Twin bellows worked alternately, and a double-acting box bellows. A hand bellows of thick leather flexes and spares the fragile clay around the tuyere " + c(2) + "."))
    b.append(ul(["<b>Measure your bellows:</b> time how long it takes to fill a large garbage bag of known volume " + c(2) + ". Historic single smith's bellows are often too small for a smelter.", "<b>Tuyere materials</b> that work: copper sheet, ceramic tube, or schedule-40 steel pipe " + c(2) + ".", "<b>Water power:</b> a <b>trompe</b> uses falling water to compress air and once blew Catalan bloomeries in Europe and the United States " + c(55) + ".", "A hand-crank fan blower (Tier B, see appendix) or any electric blower makes long smelts far easier."]))
    b.append(h2("smelt", "4.3 Running a smelt"))
    b.append(steps(["<b>Preheat</b> 60–90 minutes: small wood under natural draft, then gentle air, then rough charcoal with increasing blast " + c(2) + ".", "<b>Fill with sized charcoal</b> at full air until the burning zone reaches about 40 cm above the tuyere (about an hour) " + c(2) + ".", "<b>Burn rate:</b> aim for one 2 kg 'bucket' of charcoal every 8–10 minutes. Faster than about 6 minutes risks making high-carbon cast iron; slower than about 14 minutes is too cold " + c(2) + ".", "<b>Charge ore:</b> start with about 500 g ore per 2 kg charcoal, spread evenly; the first 4–6 kg builds the slag bowl. Then raise ore charges until ore weight matches or exceeds charcoal " + c(2) + ".", "<b>Manage slag:</b> tap slag through the arch if it rises toward the tuyere; Sauder and Williams recharge tapped slag with an equal weight of charcoal to recover its iron " + c(1) + ".", "<b>Burn down</b> after the last ore charge, then break open the tap arch or top and pull the glowing bloom with heavy tongs or a hook."]))
    b.append(caution("Signs of trouble", ul(["Bright sparks of burning iron at the tuyere: too much air for the moment — ease the blast " + c(1) + ".", "Lacy, crumbly iron: not enough air volume or pressure " + c(2) + ".", "Dark smoke and slow burn: blast too low or charcoal too fine."])))
    b.append(h2("bloom", "4.4 Consolidating the bloom"))
    b.append("<p>The bloom is porous and full of slag. While it is still near welding heat, it must be compressed with heavy blows — lightly at first so it does not crumble — to close the voids and squeeze out slag, then reheated and worked repeatedly at welding heat into a bar " + c(4, 1) + ". Sauder and Williams split a 13.5 kg bloom with a splitting maul driven by sledges, then forged a 7.7 kg half to a 50 × 50 mm billet in 3 h 40 min of three-person work " + c(1) + ". The result is wrought iron or, where the bloom picked up more carbon, low-grade steel. Use the spark test (6.1) to sort pieces.</p>")
    # ---------- Part 5
    b.append(part("p5", "Part 5", "From Iron to Steel"))
    b.append("<p>Bloomery iron is usually too soft to hold an edge. Steel needs more carbon, added in controlled amounts. The oldest methods add carbon to solid iron; later methods melt it.</p>")
    b.append(h2("carb", "5.1 Case hardening (pack carburizing)"))
    b.append(tier("A", "Hard skin on a soft, tough core", "<p>Pack wrought iron or mild-steel parts in a sealed box with crushed charcoal (traditionally also ground bone, hoof, horn or leather), heat at red heat for some hours, then quench. Carbon travels into the surface as carbon-monoxide gas, giving a skin that hardens while the core stays tough " + c(19) + ". A few hours gives a thin case, enough for tool faces, pins and wear parts " + c(19) + ".</p>"))
    b.append(fig(d_cement(), "Figure 6. Pack carburizing box. Cementation steelmaking (5.2) is the same idea on whole bars for much longer."))
    b.append(h2("blister", "5.2 Cementation: blister and shear steel"))
    b.append(tier("B", "Blister steel, then shear steel", "<p>Bars of wrought iron and charcoal are packed in alternating layers in sealed stone or clay chests and heated for a week or more, then left about two weeks to cool. The bars gain a little over 1% in mass from carbon and come out blistered and uneven: <b>blister steel</b> " + c(20) + ". Cut the bars, stack, and forge-weld them together; repeating this 3–4 times makes a more uniform <b>shear steel</b> " + c(20) + ". It can be done on a small scale in a forge or small furnace " + c(20) + ".</p>"))
    b.append(h2("crucible", "5.3 Crucible steel"))
    b.append(tier("B", "Melting steel in a closed pot", "<p>Melting iron or steel in sealed clay crucibles gives a uniform steel free of slag. Benjamin Huntsman (Sheffield, 1740s) used a coke furnace reaching about 1,600 °C with clay crucibles holding about 15 kg each " + c(21) + ". Earlier crucible methods co-heated wrought iron with cast iron and fluxes so carbon diffused into the iron " + c(21) + ". You need refractory crucibles, a strong draft or blower, and coke or hard charcoal.</p>"))
    b.append(h2("fining", "5.4 Finery and puddling: wrought iron from cast iron"))
    b.append("<p>Once a blast furnace makes cast iron, it has to be decarburized to forge. A <b>finery forge</b> remelts cast iron in an air blast to burn out carbon " + c(22) + ". <b>Puddling</b> (England, 1780s) stirs molten pig iron in a coal-fired reverberatory furnace until it becomes pasty wrought iron, without charcoal; it spread to North America soon after " + c(23) + ".</p>")
    b.append(h2("bulk", "5.5 Industrial steel: Bessemer to electric arc"))
    b.append(fig(d_industry(), "Figure 7. Modern steel routes in outline. These are Tier C targets to rebuild toward."))
    b.append(table(["Process", "Key idea", "Notes"], [
        ["Blast furnace", "Tall shaft; ore, coke and limestone; hot blast; tapped as liquid pig iron", "Hopewell Furnace (Pennsylvania, from ~1771) ran on charcoal with a cold blast " + c(24, 51)],
        ["Bessemer converter (1856)", "Air blown through molten pig iron burns out carbon; the burning keeps it molten", "Kelly claimed an earlier independent discovery in the US " + c(25)],
        ["Open hearth (Siemens–Martin, 1865)", "Regenerative furnace preheats air and gas; melts pig iron and scrap", "Easier to control than Bessemer; could melt lots of scrap " + c(26)],
        ["Basic oxygen (LD, 1952–53)", "Pure oxygen blown onto molten iron; lime flux", "Main primary steel route today " + c(27)],
        ["Electric arc furnace", "An arc melts the charge, mostly scrap; up to about 1,800 °C", "Ranges from ~1 tonne to ~400 tonnes " + c(28)]]))
    # ---------- Part 6
    b.append(part("p6", "Part 6", "Identifying Steel and Recycling Scrap"))
    b.append(h2("spark", "6.1 The spark test"))
    b.append("<p>Touch the steel lightly to a grinding wheel in dim light and look at the sparks. It is quick and needs no preparation, but it only classifies the metal — it cannot positively identify it " + c(30) + ". Compare against known samples (a new file, a nail, a piece of rebar).</p>")
    b.append(fig(d_spark(), "Figure 8. Spark patterns after the descriptions in " + c(30) + ". More carbon = more forking and bursting."))
    b.append(h2("filetest", "6.2 File, magnet and hardening tests"))
    b.append(ul(["<b>File test:</b> a file bites into soft iron and mild steel; on hardened steel it skates and slides without cutting. Use an old file you do not mind dulling.", "<b>Magnet test:</b> ordinary steels are magnetic; most 300-series stainless and Hadfield manganese steel are not " + c(52, 53) + ". Hot steel stops being magnetic near its hardening heat — iron's Curie point is 770 °C " + c(40, 62) + ".", "<b>Hardening test:</b> heat the end of a sample to cherry red, quench it in water, then try the file. If the file skates and the end snaps with a fine gray grain, it is hardenable (medium- or high-carbon) steel. If it bends, it is mild steel or wrought iron."]))
    b.append(h2("scrap", "6.3 Scrap steel: what to keep and what to avoid"))
    b.append(table(["Scrap item", "Likely steel", "Good for"], [
        ["Leaf springs (vehicles, trailers)", "High-quality spring steel; favored by blacksmiths worldwide " + c(31), "Knives, chisels, punches, springs, scrapers"],
        ["Coil springs", "Spring steel", "Punches, small tools, drifts"],
        ["Old files and rasps", "High-carbon tool steel (often very hard)", "Knives, scrapers — anneal first (9.1)"],
        ["Rebar", "Carbon steel of unknown, variable grade", "Practice, hooks, hardware, tongs; do not trust it for edges"],
        ["Mild-steel bar, angle, plate", "Low carbon", "Hinges, brackets, nails, hooks, forge tools"],
        ["Railroad spikes, bolts, chain", "Usually low-to-medium carbon", "Practice, hooks, hardware"],
        ["Plow shares, disc harrow blades", "Often medium-high carbon", "Chisels, scrapers, hoes"]]))
    b.append(danger("Never forge galvanized (zinc-coated) steel", "Heating zinc coating gives off zinc oxide fumes that cause metal fume fever " + c(49) + ". Strip the coating chemically or by grinding outdoors with a respirator, or don't use it. Also avoid painted and plated scrap, and anything that held fuel or chemicals."))
    b.append("<p>Recycling steel scrap is how most steel is made today: electric arc furnaces melt mainly scrap " + c(28, 32) + ". Sort your scrap by spark and hardening tests and label it with paint.</p>")
    # ---------- Part 7
    b.append(part("p7", "Part 7", "The Forge and Its Tools"))
    b.append(h2("forge", "7.1 Building a forge"))
    b.append(fig(d_forge(), "Figure 9. A side-blast hearth suits charcoal; a bottom-blast firepot (an iron box or old brake drum with an air pipe) suits coal or charcoal."))
    b.append(steps(["Build the hearth table at about hip height from stone, brick, or a steel box filled with clay and sand.", "Bring the air pipe (tuyere) in from the side or bottom. Any steady air works: bellows (4.2), a hand-crank blower (see appendix) or a small fan.", "Make a fire pit about 10–15 cm deep around the tuyere so the work sits in deep, hot coals, not in the oxygen-rich blast that scales the metal.", "Add a water tank or bucket, a slack tub for quenching, and a hood or open-air site. Keep a clear 3 m around the forge."]))
    b.append(h2("anvil", "7.2 Anvils and anvil substitutes"))
    b.append("<p>A blacksmith's anvil has a hardened flat <b>face</b>, a conical <b>horn</b> for bending, a square <b>hardy hole</b> for tools and a round <b>pritchel hole</b> for punching " + c(33) + ". Any big, solid, flat block of steel will do the job — mass under the hammer matters most.</p>")
    b.append(fig(d_anvil(), "Figure 10. Anvil parts, and substitutes when no anvil is available."))
    b.append(h2("tools", "7.3 Tongs, hammers, hardies and the post vise"))
    b.append(fig(d_tools(), "Figure 11. A starter kit: tongs, cross-peen hammer, hardy, punch, drift, swage block and a post vise."))
    b.append(ul(["<b>Tongs:</b> make your first pair from mild steel (two identical halves, punched and riveted). Jaws must grip the stock firmly; refit them hot to each job.", "<b>Hammers:</b> a 1–1.5 kg cross-peen hammer does most work; strikers use sledges. The bloom-smithing team above used a 2 kg hand hammer and 4.5–5.5 kg sledges " + c(1) + ".", "<b>Hardy and punches:</b> a hardy sits in the hardy hole for cutting hot stock; punches and drifts make holes (8.3) " + c(60) + ".", "<b>Swage block:</b> a heavy block with shaped holes and edges for forming and sizing " + c(59) + ".", "<b>Post (leg) vise:</b> its leg carries hammer blows to the floor, so it survives forge work that would crack a cast-iron bench vise."]))
    # ---------- Part 8
    b.append(part("p8", "Part 8", "Forging Techniques"))
    b.append(h2("colors", "8.1 Reading heat colors"))
    b.append(fig(d_heat(), "Figure 12. Heat colors of steel after Chapman, Workshop Technology " + c(36) + ". Judge colors in shade; bright sun makes hot steel look cooler than it is."))
    b.append(ul(["Most forging is done at orange to yellow heat. Stop hammering when the steel falls to dull red — hammering cold steel cracks it.", "High-carbon steel should not be overheated (no sparks or white heat); it burns and crumbles.", "Hardening heat for plain carbon steel is about where it stops being attracted to a magnet " + c(62) + "."]))
    b.append(h2("moves", "8.2 Drawing out, upsetting and bending"))
    b.append("<p>Forging works the metal by compression: <b>drawing out</b> makes stock longer and thinner, <b>upsetting</b> makes it shorter and thicker, and <b>fullering</b> (with the peen or a rounded tool) spreads metal in one direction " + c(34) + ".</p>")
    b.append(fig(d_hammer(), "Figure 13. The basic forging moves. Most objects are a combination of these."))
    b.append(ul(["<b>Drawing out:</b> work on the far edge of the anvil or the horn, turning the bar 90° between blows; keep it square, then octagon, then round.", "<b>Upsetting:</b> heat only the end, stand the bar on the anvil and strike down; straighten any buckling at once.", "<b>Bending:</b> heat only the section to bend; bend over the anvil edge or horn, or in the vise."]))
    b.append(h2("punch", "8.3 Punching and drifting"))
    b.append("<p>At bright heat, drive a punch halfway through, turn the work over, find the dark mark and punch the slug out over the pritchel or hardy hole. Cool the punch in water often. A tapered <b>drift</b> then opens the hole to size and shape — for hammer and axe eyes and hinge holes — without removing metal " + c(60) + ".</p>")
    b.append(h2("weld", "8.4 Forge welding and flux"))
    b.append("<p>Forge welding joins two pieces by heating them to welding heat and hammering them together. The surfaces must be clean, so a flux is used to keep oxides off " + c(35) + ". The oldest flux is <b>fine silica sand</b>; borax was a common later flux " + c(35, 54) + ". Pure iron welds near white heat (about 1,400–1,500 °C); steel with more carbon welds at lower, orange-yellow heats " + c(35) + ".</p>")
    b.append(fig(d_weld(), "Figure 14. The scarf weld. Practice on mild steel; wrought iron welds most easily."))
    b.append(caution("Welding tips", ul(["Keep the fire deep and clean (no clinker); the work must be in reducing coals, not in the air blast.", "Flux at bright red, return to the fire, and bring both pieces to welding heat together.", "Move fast: from fire to anvil to first blow in a few seconds. Hit lightly first, then harder.", "Flux and molten scale spray from the first blows — wear eye protection (12.1)."])))
    # ---------- Part 9
    b.append(part("p9", "Part 9", "Heat Treatment"))
    b.append("<p>Heat treatment decides whether a tool is soft, hard, brittle or tough. The three steps for a hardenable steel tool are: <b>normalize</b>, <b>harden</b> (heat and quench) and <b>temper</b>.</p>")
    b.append(h2("norm", "9.1 Normalizing and annealing"))
    b.append(ul(["<b>Normalizing:</b> heat the finished forging evenly to just above non-magnetic and let it cool in still air. Repeating this two or three times refines the grain and relieves forging stresses.", "<b>Annealing:</b> heat to the same range and cool as slowly as possible (buried in ash or dry lime, or left in a dying fire). Annealing makes steel as soft as it can be for filing, drilling and cold work " + c(39) + ". Anneal old files before reshaping them, and anneal wire between drawings (11.2) " + c(44) + "."]))
    b.append(h2("harden", "9.2 Hardening and quenching media"))
    b.append("<p>Heat the working part evenly to hardening heat (about cherry red, just non-magnetic) and plunge it into the quench, moving it up and down. Quenching freezes the steel into a very hard, brittle structure (martensite) " + c(38) + ". Water quenches fastest; oil is slower and gentler " + c(38) + ".</p>")
    b.append(table(["Quench", "Speed", "Use"], [["Brine (salt water)", "fastest", "Plain high-carbon tools that must be very hard; highest risk of cracking"], ["Water", "fast", "Plain carbon steels (files, older spring steels); quench edge-first, vertically"], ["Oil (vegetable or mineral)", "slower", "Most spring and alloy steels (leaf springs); fewer cracks and less warping"], ["Air", "slowest", "Only special air-hardening steels"]]))
    b.append(caution("Avoiding cracks and warps", ul(["Normalize before hardening.", "Heat evenly — thin edges overheat first.", "Plunge straight in, edge or point first, never flat.", "Temper immediately after hardening; untempered hardened steel can crack while sitting."])))
    b.append(h2("temper", "9.3 Tempering by color"))
    b.append("<p>Tempering reheats hardened steel to trade some hardness for toughness. Polish a bright spot and heat gently (on a hot bar, in the forge's edge or in an oven) and watch the oxide colors move; quench when the right color reaches the working edge " + c(37) + ".</p>")
    b.append(fig(d_temper(), "Figure 15. Tempering colors and typical uses " + c(37) + ". The colors depend on time too — slow heating gives deeper colors at lower temperatures."))
    b.append(tip("Differential tempering", "For a blade or chisel, heat the back or spine, not the edge, and let the colors run toward the edge; stop when straw reaches the edge. The back ends softer and tougher while the edge stays hard " + c(37) + "."))
    # ---------- Part 10
    b.append(part("p10", "Part 10", "Making Basic Tools"))
    b.append(h2("knife", "10.1 A knife blade (a working tool)"))
    b.append(fig(d_knife(), "Figure 16. Forging a utility knife blade from leaf-spring steel."))
    b.append(steps(["Cut a piece of leaf spring or other high-carbon steel (hot-cut with the hardy).", "Forge the point by hammering the corner back toward the spine; draw out the tang.", "Forge the bevels lightly; leave the edge a little thick.", "Normalize three times (9.1). File or grind the bevels to shape.", "Harden the blade in warm oil (leaf spring) or water (file steel), then temper at straw to brown; the spine can go to blue (9.3).", "Sharpen on progressively finer stones and fit a wooden or antler handle."]))
    b.append(h2("chisel", "10.2 Cold chisel and center punch"))
    b.append(ul(["Use round or octagon spring steel, 15–20 cm long. Draw one end to a wedge about 60° included angle; leave the head slightly crowned.", "Harden the last 2–3 cm and temper to brown/purple at the edge (Figure 15). The head must stay soft so it does not chip under the hammer — grind off any mushrooming.", "A center punch is the same process with a conical point; drift punches are left softer."]))
    b.append(h2("nails", "10.3 Nails and hooks"))
    b.append("<p>Hand-forged nails were made by drawing a tapered square pin, then setting it into a <b>nail header</b> — an iron plate with a small hole — and hammering the protruding end into a head " + c(47) + ". Until about 1800 nailers made nails this way; slitting mills later cut bar into rods for them " + c(47) + ".</p>")
    b.append(fig(d_nail(), "Figure 17. Nail and S-hook. Make a nail header from a bar of mild steel with a tapered punched hole."))
    b.append(h2("hinge", "10.4 Strap hinge and pintle"))
    b.append(fig(d_hinge(), "Figure 18. Strap hinge and pintle for doors and gates. A pair of pintles driven into a post carries a heavy door."))
    b.append(steps(["Draw a flat strap (about 5 mm thick) and taper one end decoratively.", "Thin the other end and scroll it back on itself around a rod the size of the pintle pin to form the eye.", "Punch nail holes hot (8.3).", "For the pintle, upset a bar, bend up a short pin and point the other end to drive into the post (or a screw-spike)."]))
    # ---------- Part 11
    b.append(part("p11", "Part 11", "Casting, Wire, Rolling and Sheet"))
    b.append(h2("cast", "11.1 Sand casting iron"))
    b.append(tier("B", "Cast iron needs a real melt", "<p>Sand molds are cheap and refractory enough even for steel. Green sand is sand bonded with clay (about 5–11% bentonite) and moistened with water, rammed around a wooden pattern in a two-part flask; the pattern is removed and the metal poured through a sprue " + c(41) + ". Cast iron is melted in a <b>cupola</b>, a vertical shaft furnace from about 0.5 m upward in diameter, charged with coke, iron and flux " + c(42) + ". Practice the whole sequence with aluminum or bronze first.</p>"))
    b.append(fig(d_sandcast(), "Figure 19. A two-part sand mold. Vents and risers let gas escape and feed shrinkage."))
    b.append(danger("Molten metal and water", "Molten metal contacting water or damp sand explodes into steam and throws metal. Pre-heat ladles and tools, keep molds dry, pour over dry sand, and wear boots, leather and a face shield."))
    b.append(h2("wire", "11.2 Drawing wire"))
    b.append("<p>Wire is made by pulling, not pushing, a rod through a tapering hole that is slightly smaller than the rod " + c(43) + ". A <b>draw plate</b> is a hardened steel plate with a series of tapered holes; point the wire, grease it, and pull it through with draw tongs, moving to smaller holes. Heavy wire needs a draw bench with a crank. The wire work-hardens and typically needs re-annealing after about three draws " + c(44) + ".</p>")
    b.append(fig(d_wire(), "Figure 20. Wire drawing. Make the plate from file or spring steel, punch the holes hot, file the tapers, then harden it."))
    b.append(h2("roll", "11.3 Rolling and slitting"))
    b.append("<p>Rolling squeezes hot metal between turning rolls to make bars, rods and sheet, far faster than hammering " + c(45) + ". Grooved rolls form bars; a 'three-high' stand passes the work back and forth without reversing the mill (see the Fritz patent in the appendix). A slitting mill cuts flat bar into nail rods " + c(47) + ". Rolling needs water power or engines: Tier C.</p>")
    b.append(fig(d_rolling(), "Figure 21. Rolling in principle."))
    b.append(h2("sheet", "11.4 Simple sheet work and rivets"))
    b.append(ul(["Sheet metal is formed by bending, cutting and joining; thin sheet is cut with shears or a chisel on a soft block " + c(46) + ".", "Hammer sheet over a wooden form or a stake to make pans, scoops and buckets; anneal copper or steel when it gets springy.", "Join with folded seams or rivets: punch matching holes, insert a soft iron rivet, and peen the end over (hot rivets shrink and pull tight as they cool).", "Recover sheet from old appliances, barrels (if clean) and vehicle panels. Avoid galvanized sheet near the fire (6.3)."]))
    # ---------- Part 12
    b.append(part("p12", "Part 12", "Safety at the Furnace and Forge"))
    b.append(h2("burns", "12.1 Burns, eyes and hearing"))
    b.append(ul(["Wear natural-fiber clothing (synthetics melt into skin), a leather apron, leather boots and long sleeves.", "Treat all metal near the forge as hot. Mark hot pieces, and never pick up iron with bare hands — black-hot steel is still hot enough to burn badly.", "Wear eye protection whenever hammering, grinding, forge welding or quenching; scale, flux and sparks fly. Work where fumes can escape — OSHA's welding, cutting and heating rule is built around ventilation " + c(56) + ".", "Hammering on an anvil is loud: use ear protection for long sessions.", "Burn first aid: cool with clean running water for many minutes; see the Medical guide."]))
    b.append(h2("gas", "12.2 Carbon monoxide and toxic fumes"))
    b.append("<p>Charcoal fires, smelters and forges all make <b>carbon monoxide</b>, a colorless, odorless gas. Early signs are headache, dizziness, weakness, nausea and confusion; high levels kill " + c(48) + ". Forge outdoors or under a tall hood with an open side; never use a charcoal forge in a closed room or shelter.</p>")
    b.append(danger("Fumes to avoid", ul(["Zinc (galvanized) coatings — metal fume fever " + c(49) + ".", "Paint, plating, oil and plastic on scrap — burn off outdoors, upwind, or remove first.", "Never heat closed containers, pipes with sealed ends, or anything that held fuel."])))
    b.append(h2("quenchfire", "12.3 Quench fires and wet-ground explosions"))
    b.append(ul(["Oil quench tanks can flash into flame: use a metal container with a fitted metal lid, enough oil to cover the work fully, and plunge the piece completely and quickly. Smother an oil fire with the lid — never throw water on burning oil.", "Keep water and a shovel of sand or dirt beside every furnace and forge.", "Smelter slag and blooms stay hot for hours. Mark and fence the area; keep children and animals away.", "Wet ground or water under molten slag or metal can explode into steam — tap slag onto dry sand."]))
    # ---------- Part 13
    b.append(part("p13", "Part 13", "Iron and Steel Region by Region"))
    b.append(regions_html(R))
    # ---------- Quick ref
    b.append(part("srcs", "Appendix", "Quick Reference & Sources"))
    b.append(table(["Item", "Value"], [
        ["Bloomery inside diameter / height", "25–30 cm / 65–75 cm overall " + c(2)],
        ["Air for a bloomery", "1.2–1.5 L/min per cm² of cross-section " + c(1, 2)],
        ["Tuyere", "20–25° down, tip ~5 cm inside " + c(2)],
        ["Charcoal / ore size", "25–5 mm / 5–2 mm " + c(2)],
        ["Burn rate", "2 kg charcoal per 8–10 min " + c(2)],
        ["Typical yield (Sauder & Williams)", "40.5 kg ore + 94 kg charcoal → 14 kg bloom " + c(1)],
        ["Charcoal pit cover", "20 cm leaves + 20 cm earth " + c(13)],
        ["Iron's Curie point", "770 °C (1,420 °F) " + c(40)],
        ["Hardening (plain carbon steel)", "≈ cherry red, just non-magnetic " + c(36, 62)],
        ["Tempering", "light straw 205 °C … brown 260 °C … blue 310 °C " + c(37)],
        ["Green sand", "sand + 5–11% clay + water " + c(41)]]))
    b.append('<p class="small">General information for emergencies and knowledge retention. Sources checked November 2026. Dimensions and air rates are from published experimental smelts; local ore, clay and charcoal differ, so start small and record every smelt.</p>')
    b.append('<h2>Sources</h2>' + G.sources_html("sources.tsv"))
    return "\n".join(b)

G = Guide("Steel", "Survival Info<br>Steel: Making<br>&amp; Forming",
          "Finding iron ore, charcoal, the clay bloomery, turning iron into steel, recycling scrap, the forge and anvil, forging, forge welding, heat treatment, basic tools, casting, wire and rolling — from Stone-Age start to industry.",
          "Steel", TOC, cover_art(), "Tools · Concrete · Fire · House · Chemistry · Medical")
if __name__ == "__main__":
    G.build(body, "/workspace/survival-info/Survival_Info_Steel.pdf")
