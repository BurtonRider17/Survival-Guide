from common import *
import dg

def build():
    h = [part("p7", 7, "Heating, Cooking &amp; Lighting")]
    h.append(h2("stoves", "7.1 Wood stoves"))
    h.append('<p>A cast-iron or steel wood stove with a proper chimney is the core of a grid-down home in most of North America — heat, cooking, hot water and drying in one appliance. Salvage the best one you can (EPA-certified stoves burn far cleaner and use roughly a third less wood than old box stoves), along with stovepipe, a chimney, and a spare gasket and glass. A cookstove with an oven and water reservoir is ideal for a family.</p>')
    h.append(table(["Climate", "Typical seasonal firewood (small, well-insulated house)", "Poorly insulated / drafty"], [
        ["Very cold (Prairies, Alaska, northern Canada)", "6–10 cords", "12–20+ cords"],
        ["Cold (Great Lakes, Northeast, Rockies)", "4–6 cords", "8–12 cords"],
        ["Mixed (mid-Atlantic, PNW, Ohio Valley)", "2–4 cords", "5–8 cords"],
        ["Mild / hot (South, California, Mexico)", "≤ 1–2 cords (mostly cooking)", "2–4 cords"]]))
    h.append('<p class="small">A cord is 128 ft³ (4 × 4 × 8 ft, 3.6 m³) of stacked wood. Rough planning ranges only — they depend on the house, the stove and the wood species. Dense hardwoods (oak, hickory, maple, locust, ash) give about twice the heat per cord of light softwoods. Burn <b>seasoned</b> wood — split and stacked under cover for 6–12 months, below about 20% moisture (cracks on the ends, hollow knock when two pieces strike) — wet wood wastes heat and builds creosote fast (EPA Burn Wise).</p>')
    h.append(h2("chimney", "7.2 Chimney safety and clearances"))
    h.append(fig(dg.chimney(), "Clearances for an unlisted (unlabeled) wood stove and the 3-2-10 chimney height rule, from NFPA 211 as summarized by University of Maryland Extension FS-940. Not to scale. Listed stoves and chimneys may allow less — read the label and manual."))
    h.append(check("Stovepipe and chimney checklist", [
        "Stovepipe 24-gauge or heavier; male (crimped) ends point <b>down toward the stove</b> so creosote runs back inside; three sheet-metal screws per joint",
        "Pipe rises toward the chimney at least ¼ in per foot; keep horizontal runs short (≤ ~75% of the vertical height) with no more than two 90° elbows",
        "Pass through walls and ceilings only with a listed thimble or insulated Class A chimney section — never bare single-wall pipe through wood",
        "Chimney 3 ft above the roof penetration and 2 ft higher than anything within 10 ft; spark-arrestor cap (essential in wildfire country and under thatch or shakes)",
        "Install a damper or barometric control; never close it fully while a fire is burning",
        "Inspect monthly in heating season and sweep when creosote is ⅛ in (3 mm) thick or at least yearly (CSIA). Keep a brush, rods and ladder",
        "Battery-powered <b>carbon monoxide alarm</b> and smoke alarm in every sleeping area; fire extinguisher or water and a bucket of sand by the stove",
        "Store ashes in a lidded metal can outdoors, away from the house, for several days — they stay hot"]))
    h.append(danger("Chimney fires and carbon monoxide", "A roaring sound, shaking pipe, sparks or flames from the chimney top mean a chimney fire: close the stove air inlets and damper, get everyone out, and spray the roof around the chimney. Afterward inspect for cracks before using it again. CO from a smoldering or back-drafting stove is odorless — headache, nausea, dizziness or confusion that improve outdoors mean CO poisoning (EPA). Never use a charcoal grill, camp stove, gas oven or generator for heat indoors."))
    h.append(h2("rocket", "7.3 Rocket mass heaters"))
    h.append(fig(dg.rocket(), "J-tube rocket mass heater. Wood burns hot in the insulated burn tunnel and riser; the exhaust then passes through a long duct buried in a cob or stone bench that stores the heat and releases it for many hours."))
    h.append('<p>A rocket mass heater (RMH) burns small sticks very completely and stores the heat in a massive bench, so it can heat a small house on a fraction of the wood of an ordinary stove. Masonry heaters (Russian/Finnish stoves) work on the same principle and are proven over centuries. RMHs are home-built, experimental appliances: Oregon’s Alternative Technology Advisory Committee found they are not covered by recognized codes and recommended applying masonry-heater and wood-stove safety requirements. Learn from an experienced builder, follow a published design exactly (e.g., Ianto Evans &amp; Leslie Jackson; Ernie &amp; Erica Wisner), use clean firebrick and insulating refractory in the burn area, provide clean-outs, test the draft with the bench open, and install a CO alarm.</p>')
    h.append(h2("cooking", "7.4 Cooking without power"))
    h.append(table(["Method", "Notes"], [
        ["Wood cookstove", "Heat, oven and hot water in one; ideal in cold climates. Summer heat is a problem — have an outdoor kitchen"],
        ["Outdoor (summer) kitchen", "Roofed open shed with a stove or hearth keeps heat, smoke and fire risk out of the house; traditional across the South and Mexico"],
        ["Earth / cob oven", "Dome of clay-sand on a stone base, insulated with straw-clay; fire inside, rake out, bake bread and roasts in stored heat"],
        ["Rocket stove", "Very efficient small cook fire from sticks (see Electricity &amp; Fuel volume, Fig. 3); use outdoors or under a ventilated roof"],
        ["Haybox / retained-heat cooker", "Bring a pot to the boil, then nest it in a box of hay, wool or blankets to finish cooking for hours — saves 50% or more of fuel"],
        ["Solar oven", "Box or panel cookers; sunny climates (deserts, Plains, Mexico) — see solarcookers.org"]]))
    h.append(h2("lighting", "7.5 Lighting basics"))
    h.append('<p><b>Daylight first:</b> south windows, a skylight or a clerestory over the work area, light-colored interior walls (whitewash — lime and water — is cheap, bright and mildew-resistant), and a work table by a window. Schedule tasks for daylight. For night, small solar panels with LED lights are by far the safest and cheapest light (see the <i>Electricity &amp; Fuel</i> volume). Flame lighting:</p>'
             '<ul><li><b>Oil lamps</b> burn kerosene, or vegetable oil and rendered fat with a simple floating or crock wick; a glass chimney gives steady, brighter light. <b>Candles</b> from tallow (rendered beef/sheep fat) or beeswax; rushlights (peeled rush pith dipped in fat).</li>'
             '<li>Use a reflector (polished tin) behind a lamp to double usable light on a work surface.</li></ul>')
    h.append(danger("Flame lighting is a major fire risk", "Candles start thousands of home fires every year (NFPA). Keep flames 12 in (30 cm) from anything that can burn, in a stable holder with a guard, never near curtains, bedding, straw or thatch, never unattended or in a room where people sleep, and out of reach of children and pets. Store fuel outside the living space. Keep a fire extinguisher or bucket of water ready and plan a fire escape route (Ready.gov)."))
    return "\n".join(h)
