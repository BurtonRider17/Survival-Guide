from common import *
import dg, math
from spans import span, fmt, SIZES

def pole_equiv():
    rows = []
    for sz in ["2x6", "2x8", "2x10", "2x12"]:
        b, d, _ = SIZES[sz]
        S = b*d*d/6; I = b*d**3/12
        dS = (S*32/math.pi)**(1/3); dI = (I*64/math.pi)**0.25
        dd = max(dS, dI)
        rows.append([sz.replace("x", "×"), f"{dd:.1f} in ({dd*2.54:.0f} cm)"])
    return rows

def build():
    h = [part("p5", 5, "Floors, Roofs &amp; Rainwater")]
    h.append(h2("floors", "5.1 Floors"))
    h.append(table(["Floor", "How", "Best for"], [
        ["Earthen floor", "10–15 cm (4–6 in) gravel capillary break, optional insulation (pumice, scoria, foam board), then 5–8 cm of sandy clay laid in two or three layers, troweled and sealed with several coats of hot linseed oil", "Dry sites; thermal mass for passive solar; cheap. Not for wet ground"],
        ["Flagstone or brick on sand", "Stone or salvaged brick bedded in sand over gravel; joints swept with sand or lime", "Mass floor in sunlit areas, entries, around stoves"],
        ["Wood floor on joists", "Joists on sills/beams at 16–24 in centers, subfloor of boards laid diagonally or plywood, finish boards; insulate between joists in cold climates", "Most climates; termite/humid areas (raised and ventilated); permafrost"],
        ["Puncheon floor", "Split or hewn logs, flat face up, laid on sleepers", "First winter cabin floor when no sawn lumber exists"]]))
    rows = []
    for sz in ["2x6", "2x8", "2x10", "2x12"]:
        rows.append([sz.replace("x", "×"), fmt(span(sz, "DF-L No.2", 16, 40, 10, 360, 1.0)), fmt(span(sz, "DF-L No.2", 24, 40, 10, 360, 1.0)), fmt(span(sz, "SPF No.2", 16, 40, 10, 360, 1.0)), fmt(span(sz, "SPF No.2", 24, 40, 10, 360, 1.0))])
    h.append('<h3>Floor joist spans (living areas, 40 psf live + 10 psf dead load)</h3>')
    h.append(table(["Joist", "Douglas fir-larch No.2 @ 16 in", "DF-L No.2 @ 24 in", "Spruce-pine-fir No.2 @ 16 in", "SPF No.2 @ 24 in"], rows, numcols=(1,2,3,4)))
    h.append('<p class="small">Clear span between supports. Calculated by the author for this guide from NDS reference design values (bending and L/360 stiffness) — slightly more conservative than the American Wood Council span tables. For ungraded salvaged lumber, reduce by about 25%. Use a girder or bearing wall at mid-span for longer rooms.</p>')

    h.append(h2("roofs", "5.2 Roof framing: rafters and trusses"))
    h.append('<p>The roof is the most important part of a survival house: it keeps everything else dry. Rafters push outward at the top of the walls; that thrust must be resisted by <b>ceiling joists or rafter ties</b> across the building (or a structural ridge beam supported by posts at each end). Collar ties high in the roof stop the rafters spreading apart in wind and holding snow but do not replace low rafter ties.</p>')
    h.append(fig(dg.roof_framing(), "Rafter roof and king-post truss (after FM 5-426, ch. 7). Cut a birdsmouth seat so each rafter bears flat on the top plate, no deeper than ⅓ of the rafter depth. Trusses span the whole building with light lumber and leave the floor open."))
    rows = []
    for LL, gs in [(20, "≈ 30"), (30, "≈ 40–45"), (50, "≈ 70"), (70, "≈ 100")]:
        r = [f"{LL} psf ({LL*0.0479:.1f} kPa)", gs]
        for sz in ["2x6", "2x8", "2x10", "2x12"]:
            r.append(f"{fmt(span(sz, 'DF-L No.2', 16, LL, 10, 180, 1.15))} / {fmt(span(sz, 'DF-L No.2', 24, LL, 10, 180, 1.15))}")
        rows.append(r)
    h.append('<h3>Rafter spans by roof snow load (horizontal projection; spacing 16 in / 24 in)</h3>')
    h.append(table(["Roof snow load", "Ground snow (psf)", "2×6", "2×8", "2×10", "2×12"], rows, numcols=(2,3,4,5)))
    h.append('<p class="small">Douglas fir-larch No.2, 10 psf dead load (light metal or shingle roof), ceiling not attached to rafters (L/180). Roof snow load is roughly 0.7 × ground snow load for an ordinary exposed, heated building. Calculated by the author from NDS design values; check against the AWC <i>Span Tables for Joists and Rafters</i> while you can. For a sod roof, add the saturated soil weight (≈ 10 psf per inch of soil) to the dead load and use much shorter spans. Spruce-pine-fir: reduce ~5–10%.</p>')
    h.append(table(["Sawn size", "Round pole of equal strength & stiffness (small-end diameter)"], pole_equiv(), numcols=()))
    h.append('<p class="small">From section modulus and moment of inertia of a circle vs. a rectangle (same species). Poles (lodgepole pine, spruce, fir) peeled and seasoned make excellent rafters, purlins and joists; flatten the top slightly to bear sheathing.</p>')
    h.append(h2("pitch", "5.3 Roof pitch for rain and snow"))
    h.append(fig(dg.roof_pitch(), "Roof pitch guide. Each roofing material has a minimum pitch below which water backs up under the laps; steeper roofs shed snow but catch more wind.", "max-width:62%"))
    h.append(caution("Snow, wind and uplift", "Snow can weigh 5–20 lb/ft³: a meter of wet spring snow on a roof can exceed 100 psf (5 kPa). Shovel or rake roofs before loads exceed what you built for, starting at the eaves, and never stand under a sliding snow load. In hurricane and tornado country the danger is the opposite — wind <b>lifts</b> roofs off. Use hip roofs (4 sloping sides) at 4:12–6:12, keep overhangs modest (≤ 18–24 in), and tie every rafter to the wall and the wall to the foundation with metal straps, wire or bolts (FEMA P-499). A roof is only as strong as its weakest fastener."))
    h.append(h2("roofing", "5.4 Roofing materials"))
    h.append(table(["Material", "Min. pitch", "Life", "How / notes"], [
        ["Salvaged metal (corrugated or ribbed)", "3:12 (lower with sealed laps)", "30–60 yrs", "Over purlins/battens at 2 ft centers. Overlap one corrugation sideways and 6–12 in end-lap; screw through the high ribs (corrugated) or flats (ribbed panels) with rubber-washered screws. Best for rain catchment and fire; noisy in rain"],
        ["Asphalt shingles (salvaged or new)", "4:12 (2:12 with double underlay)", "15–30 yrs", "Need solid deck and underlayment; salvaged ones are brittle — use for sheds"],
        ["Hand-split wood shakes", "4:12; better 6:12+", "20–40 yrs", "Rive cedar or oak bolts with a froe and club; lay over spaced boards with ≤ ⅓ of each shake exposed so every point is covered by 2–3 layers (NPS Brief 19). Fire risk in wildfire zones"],
        ["Bark (birch, cedar, elm)", "6:12+", "5–20 yrs", "Peeled in summer, flattened, weighted with poles; birch bark was the traditional waterproof layer under sod roofs"],
        ["Sod / living roof", "≈ 3:12–6:12 (15–27°)", "20–50 yrs", "Strong deck, waterproof layer (salvaged EPDM, pool liner, layered tarps or birch bark), drainage layer, then 10–15 cm (4–6 in) sod; very heavy when wet (≈ 60 psf for 6 in) — size rafters for it plus snow. Good insulation and fire resistance"],
        ["Thatch (reed, straw, palm, grass)", "45°+ (12:12)", "Reed 25–40 yrs, straw 10–25, palm 3–10", "Bundles tied to battens in courses 30 cm+ thick; steep pitch is essential. Very flammable — wide spark-free zone, spark arrestor on chimney. Traditional in Mexico and the tropics (palapa)"],
        ["Clay tile / slate", "4:12–5:12+", "50–100+ yrs", "Heavy; need strong rafters. See Concrete &amp; Masonry volume for clay tile"],
        ["Membrane / tarp (temporary)", "Any", "1–5 yrs", "Emergency only; protect from UV and abrasion; weight with battens, not rocks"]], cls="brk", widths=["19%", "13%", "11%", "57%"]))
    h.append(h2("gutters", "5.5 Gutters and rainwater catchment"))
    h.append(fig(dg.catchment(), "Roof-to-cistern system. Divert the first flush (about 1–2 US gallons per 100 ft² of roof, per the Texas Manual on Rainwater Harvesting) to carry off dust, droppings and leaves before water enters storage.", "max-width:66%"))
    h.append('<ul><li><b>Gutters</b> can be made from salvaged metal bent into a half-pipe or V-trough, PVC pipe sawn in half, or two boards nailed in a V and tarred. Slope about 1:200 (1/16 in per ft) to the downspout; hang them so the roof edge drips into the middle of the gutter.</li>'
             '<li><b>Size the storage:</b> 1 inch of rain on 1,000 ft² of roof ≈ 623 US gallons (1 mm on 1 m² = 1 L). A 16 × 24 ft cabin with 2 ft overhangs (≈ 560 ft² roof) in 30 in/yr of rain yields about 0.623 × 560 × 30 × 0.8 ≈ 8,400 gal/yr.</li>'
             '<li><b>Roof materials for drinking water:</b> metal, slate, tile and clean membranes are best; avoid lead flashing, treated-wood shakes, old asphalt roofs, and copper for drinking water.</li>'
             '<li>Covered, opaque tanks with screened inlets and overflows stop mosquitoes and algae. Always <b>filter and disinfect</b> rainwater for drinking — see the <i>Water</i> volume.</li></ul>')
    return "\n".join(h)
