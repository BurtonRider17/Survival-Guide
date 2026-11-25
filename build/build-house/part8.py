from common import *
import dg

def build():
    h = [part("p8", 8, "Sanitation")]
    h.append('<p>Human waste spreads cholera, typhoid, dysentery, hepatitis A and parasites — historically, poor sanitation has killed more people in disasters than the disasters themselves. Separate waste from drinking water, food and flies from day one. The WHO <i>Guidelines on Sanitation and Health</i> stress that every toilet must safely contain waste and keep it away from people, water and insects.</p>')
    h.append(h2("outhouse", "8.1 The outhouse (pit privy)"))
    h.append(fig(dg.outhouse(), "Pit privy section (after University of Alaska Fairbanks Cooperative Extension and Alaska DEC guidance). Locate downhill of and at least 100 ft (30 m) from any well, spring or stream, with the pit bottom at least 4 ft (1.2 m) above the seasonal high water table."))
    h.append(check("Outhouse construction", [
        "Site: well-drained, never in a flood zone or where water collects; 30 m (100 ft) or more from wells and surface water, downhill; 15–30 m from the house (close enough to use at night, far enough for smell and flies)",
        "Pit about 1–1.5 m (3–5 ft) deep, 1 × 1.2 m (3 × 4 ft); line the top 50 cm or more with logs, stone or boards so the edges don't cave in",
        "Mound soil around the base so rain flows away; set the outhouse on a sill or slab larger than the pit",
        "Tight seat with a lid; fly-screened vent pipe from the pit up past the roof (a dark pipe in the sun draws air upward — this is the VIP latrine principle)",
        "After each use add a scoop of wood ash, sawdust, dry soil or lime to cut odor and flies; no trash, no chemicals",
        "When waste is within ~50 cm (18 in) of the top, fill the pit with soil, mound it, plant it with a non-food shrub, and move the house to a new pit",
        "Handwashing station (tippy-tap, soap and water) right outside; this single step prevents much of the disease spread"]))
    h.append(h2("compost", "8.2 Composting toilets"))
    h.append('<p>Where the water table is high, the ground is rocky or frozen, or you want to recover nutrients, use a <b>bucket composting toilet</b> (described in detail in Joseph Jenkins’s <i>Humanure Handbook</i>). A 5-gallon bucket sits under a wooden seat box; after each use, cover the deposit fully with a carbon material — sawdust, peat, chopped leaves or straw — so there is no smell and no flies. Full buckets are emptied into an outdoor compost bin and covered with more carbon material.</p>'
             '<ul><li>Use at least <b>two or three bins</b> (about 1 m³ each), on soil, roofed or covered, away from water sources. Fill one for a year, then leave it to age while you fill the next.</li>'
             '<li>Hot (thermophilic) composting kills most pathogens; a well-built pile reaches 50–65 °C (120–150 °F). Check with a thermometer if you have one. Age finished material <b>at least a further year</b> after the last addition; if unsure, use it only on trees and non-food plants.</li>'
             '<li>Separating urine (a funnel to a separate jug) reduces smell and bulk; urine diluted about 1:5–1:10 with water is a good nitrogen fertilizer for non-leafy crops, applied to soil, not leaves.</li>'
             '<li>Wash buckets with water and a little soap or ash; pour rinse water on the pile.</li></ul>')
    h.append(h2("greywater", "8.3 Greywater"))
    h.append('<p>Greywater is used water from washing, bathing and laundry — not toilets (blackwater). It still contains bacteria, grease, soap and food scraps, but used carefully it can water trees and ornamental plants (NMSU M-106; Oregon DEQ; Utah State Extension).</p>')
    h.append(check("Greywater rules", [
        "Use it within 24 hours — never store it (it goes septic and smells within a day or two)",
        "Discharge below a 5–10 cm layer of mulch or into a mulch-filled basin around trees, not onto the surface or onto lawns where people walk",
        "Never on root crops or leafy vegetables eaten raw; never into streams, wells or ditches; keep well back from wells (30 m / 100 ft is a common setback)",
        "Use plant-friendly soaps: low sodium and boron, no bleach; strain out food and grease (kitchen-sink water is the dirtiest)",
        "Rotate discharge points so the soil never stays saturated; stop in wet weather or when ground is frozen",
        "A simple grease trap (bucket with a baffle) and a gravel-and-sand filter before the mulch basin extends its life"]))
    h.append(caution("Diapers, illness and septic systems", "If someone has diarrheal disease, treat all their waste and washing water as blackwater: compost hot or bury deep, wash hands thoroughly, and keep it far from water and gardens. If you live in a house with an intact septic system, it will keep working without power for gravity-fed systems if you limit water use and keep grease and chemicals out (EPA Septic)."))
    return "\n".join(h)
