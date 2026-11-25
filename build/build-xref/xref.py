"""Append a one-page 'Companion guides' cross-reference page to existing guides (Nov 17 2026)."""
import sys, subprocess, shutil, html
sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import _CSS, CSS_OVERRIDE, BIG, table
import pymupdf
ROOT = '/workspace/survival-info/'
G = {
 "Medical": ("Survival_Info_Medical.pdf", "Medical &amp; First Aid"),
 "Sanitation": ("Survival_Info_Sanitation.pdf", "Sanitation &amp; Hygiene"),
 "Fire": ("Survival_Info_Fire.pdf", "Fire &amp; Heating"),
 "Radio": ("Survival_Info_Radio.pdf", "Radio &amp; Communications"),
 "Preservation": ("Survival_Info_Preservation.pdf", "Food Preservation &amp; Storage"),
 "Hunting": ("Survival_Info_Hunting.pdf", "Hunting, Trapping &amp; Fishing"),
 "Defense": ("Survival_Info_Defense.pdf", "Defense &amp; Security"),
 "Navigation": ("Survival_Info_Navigation.pdf", "Navigation &amp; Travel"),
 "Weather": ("Survival_Info_Weather.pdf", "Weather &amp; Natural Disasters"),
 "Gardening": ("Survival_Info_Gardening.pdf", "Gardening &amp; Seed Saving"),
 "Livestock": ("Survival_Info_Livestock.pdf", "Livestock &amp; Small Animals"),
 "Medicine": ("Survival_Info_Medicine.pdf", "Medicine &amp; Remedies"),
 "Chemistry": ("Survival_Info_Chemistry.pdf", "Chemistry"),
}
X = {
 "Water": [("Sanitation", "Latrines at least 30 m (100 ft) from wells and springs, pit bottoms 1.5 m above the water table, greywater, and hand-washing"), ("Medical", "Dehydration signs and the WHO home-made oral rehydration solution; diarrhea danger signs"), ("Fire", "Fuel-saving rocket stoves for boiling water; carbon-monoxide safety")],
 "Food": [("Fire", "Rocket stoves, retained-heat (hay box) cooking, firewood and safe outdoor fires"), ("Sanitation", "Hand-washing before food, food waste and garbage pits, fly and rodent control"), ("Medical", "Diarrhea and dehydration care, home-made ORS, and herbal remedies with cautions")],
 "Electricity": [("Radio", "Powering radios from batteries and solar; check-in schedules to save power"), ("Fire", "Wood stoves, chimney care and carbon-monoxide alarms"), ("Medical", "Burns and first aid for shop and electrical injuries")],
 "Concrete": [("Sanitation", "Latrine slabs and pit siting distances"), ("Fire", "Non-combustible stove pads and 3 ft clearances; chimney care"), ("Medical", "Wound care, fractures and burns for building-site injuries")],
 "Tools": [("Fire", "Fire without matches, firewood species and seasoning, rocket stoves"), ("Medical", "Bleeding control, wound cleaning, burns and splinting for shop injuries"), ("Radio", "Building wire dipole antennas and masts")],
 "House": [("Sanitation", "Outhouse and latrine siting (Sphere distances), composting toilets, greywater"), ("Fire", "Stove clearances, do-it-yourself chimney cleaning, chimney fires and CO"), ("Radio", "Antenna masts and wire dipoles for the homestead")],
 "Bunkers": [("Medical", "First aid when no help is coming: bleeding, wounds, fractures, burns, sterilizing tools"), ("Sanitation", "Bucket and composting toilets where pits cannot be dug; waste and pest control"), ("Fire", "Carbon monoxide: never run fuel-burning heaters or generators in a closed space"), ("Radio", "Antennas must be outside and high; listening, FRS/GMRS/CB/ham and signaling")],
}
NEW = {'Water': [('Navigation', 'Crossing rivers safely, and why 6 inches of moving floodwater can knock you down')], 'Food': [('Preservation', 'USDA canning times (water-bath and pressure), botulism safety, drying, curing, smoking, fermenting, root cellars, long-term grain storage'), ('Hunting', 'Snares, deadfalls, fish traps and nets, field dressing, and game diseases (tularemia, CWD, trichinella, brucellosis)')], 'Electricity': [('Defense', 'Outdoor lighting placement, motion and dawn-to-dusk lights, battery alarms')], 'Concrete': [('Preservation', 'Root-cellar temperatures, humidity and ventilation'), ('Defense', 'Reinforcing door frames and strike plates')], 'Tools': [('Hunting', 'Building snares, deadfalls, fishhooks, gill nets and fish traps; butchering'), ('Defense', 'Strike plates with 3-inch screws, pinning windows, barring sliding doors'), ('Navigation', 'Improvised needle compass')], 'House': [('Defense', 'Hardening doors and windows, security bars with quick-release, CPTED landscaping'), ('Preservation', 'Root cellars and cold rooms; storing canned and dry food')], 'Bunkers': [('Defense', 'Watch schedules, OPSEC, lighting and homemade alarms, organizing neighbors'), ('Navigation', 'Map, compass and pace counting to reach a site; the go-bag; river crossings'), ('Preservation', 'Long-term grain storage and canned-food storage temperatures')], 'Medical': [('Hunting', 'Tularemia, brucellosis, trichinella and CWD precautions when handling game'), ('Preservation', 'Botulism: how it grows, spotting bad jars, safe disposal'), ('Navigation', 'Cold-water and floodwater crossing dangers')], 'Sanitation': [('Preservation', 'Disposing of spoiled jars and bleach clean-up of botulism spills'), ('Hunting', 'Gloves and clean knives when field dressing; cooling carcasses')], 'Fire': [('Preservation', 'Smoking fish to 160 °F, dry-curing ham'), ('Hunting', 'Cooking temperatures for game'), ('Defense', 'Security bars must release from inside; keeping fire exits open')], 'Radio': [('Defense', 'Phone and radio trees, patrol base stations, watch check-ins'), ('Navigation', 'Planning routes and meeting points for travel')]}
for k, v in NEW.items(): X[k] = X.get(k, []) + v
W = "Weather"; GA = "Gardening"; L = "Livestock"
NEW3 = {
 "Water": [(W, "Flash floods and 'turn around, don't drown'; hurricane and storm-surge safety"), (GA, "Watering by season; compost and soil that hold water")],
 "Food": [(GA, "Full gardening guide: frost-date planting table, compost, crop rotation, saving open-pollinated seed, cold frames"), (L, "Chickens, rabbits, goats and bees: housing, feed, hatching, breeding, diseases")],
 "Electricity": [(W, "Generators outdoors only, 20 ft from openings; storm preparation"), (L, "Electric goat fencing needs a powered charger")],
 "Concrete": [(W, "Tornado shelter choices: basement or windowless interior room"), (GA, "Cold-frame and hot-bed construction")],
 "Tools": [(GA, "Building compost bins, cold frames and raised beds"), (L, "Coops, rabbit hutches, goat fencing and Langstroth hive boxes")],
 "House": [(W, "Tornado, hurricane, earthquake and wildfire preparation for the homestead"), (L, "Coop design: 3-5 sq ft per bird, nest boxes, predator-proofing")],
 "Bunkers": [(W, "Homemade barometer and sky signs; tornado, earthquake, tsunami and winter-storm responses"), (GA, "Growing food on site; seed saving for the long term"), (L, "Small livestock for a long-term retreat")],
 "Medical": [(W, "Frostbite, hypothermia, heat exhaustion and heat stroke signs and care"), (L, "Poultry and goat diseases; quarantine of new animals")],
 "Sanitation": [(GA, "Backyard composting: what to add and never add"), (L, "Coop and hutch cleaning, poultry biosecurity")],
 "Fire": [(W, "Wildfire: 30 ft fire-resistant zone, smoke room, evacuation"), (GA, "Using wood ash on garden soil safely")],
 "Radio": [(W, "Reading the sky and a homemade barometer when forecasts are gone")],
 "Preservation": [(GA, "Growing the crops you preserve; saving seed"), (L, "Eggs, rabbit and goat meat, honey")],
 "Hunting": [(L, "Raising rabbits, chickens and goats as a steady meat supply")],
 "Defense": [(W, "Disaster responses for tornadoes, floods, wildfire and earthquakes")],
 "Navigation": [(W, "Lightning distance, flash floods in washes, tsunami high ground")],
 "Weather": [("Navigation", "Map, compass and safe river crossings"), ("Fire", "Winter heating and carbon-monoxide safety"), ("Medical", "First aid for injuries after disasters")],
 "Gardening": [("Preservation", "Canning, drying, root cellars for the harvest"), ("Sanitation", "Latrines and greywater; keeping waste away from food beds"), (L, "Manure for compost; chickens in the garden")],
 "Livestock": [("Hunting", "Field dressing, butchering and cooling meat; game diseases"), ("Preservation", "Curing, smoking and canning meat"), (GA, "Growing feed; composting manure")],
}
for k, v in NEW3.items(): X[k] = X.get(k, []) + v
NEW4 = {
 "Medicine": [("Medical", "Wounds, splints, CPR, childbirth, dental care and sterilizing instruments — the hands-on first aid this guide builds on"), ("Sanitation", "Clean water, hand-washing and soap that prevent the infections antibiotics treat"), (GA, "Growing willow, ginger, peppers, feverfew and other medicinal plants"), ("Preservation", "Drying and storing herbs and honey; storing supplies")],
 "Medical": [("Medicine", "Stockpiling and storing medicines; making penicillin (history and limits) and willow-bark and plant painkillers; recognizing sepsis")],
 "Sanitation": [("Medicine", "Preventing infection, honey wound care, and spotting spreading infection and sepsis")],
 "Food": [("Medicine", "The WHO oral rehydration solution, medicinal plants, and stockpiling medicines")],
 "Gardening": [("Medicine", "Growing willow, ginger, peppers and other remedies; cautions and deadly look-alikes")],
 "Preservation": [("Medicine", "Storing medicines and medical-grade honey; what shelf-life studies say about potency past expiry")],
 "Bunkers": [("Medicine", "A medicine chest for a long siege: what to stockpile, storage, expiry, and treating infection when no help is coming")],
 "Hunting": [("Medicine", "Wound infection and sepsis signs; a basic medicine chest")],
 "Weather": [("Medicine", "Treating injuries after disasters; a stocked medicine kit")],
 "Livestock": [("Medicine", "Honey for wound care and infection control around animals")],
}
for k, v in NEW4.items(): X[k] = X.get(k, []) + v

NEW5 = {
 "Chemistry": [("Medicine", "Stockpiling and making medicines; the drug syntheses this guide explains in far more depth"), ("Medical", "Hands-on first aid: wounds, burns, and sterilizing instruments"), ("Sanitation", "Using chlorine, hypochlorite, lye and lime as disinfectants"), ("Preservation", "Salt, lye, lime and smoke in food preservation")],
 "Medicine": [("Chemistry", "Much deeper chemistry behind the medicines: making and purifying acids, alkalis and solvents, and the drug syntheses step by step")],
 "Medical": [("Chemistry", "Making antiseptics and the chemicals behind them, from raw materials")],
 "Sanitation": [("Chemistry", "Making chlorine, hypochlorite, lye and lime from salt, wood ash and limestone")],
 "Preservation": [("Chemistry", "Making salt, lye and lime; the chemistry behind curing and smoking")],
 "Bunkers": [("Chemistry", "Rebuilding chemical capability: acids, alkalis, disinfectants, solvents and medicines from scratch")],
}
for k, v in NEW5.items(): X[k] = X.get(k, []) + v

def page_html(name):
    css = _CSS.replace("Survival Info · Vol. 1 · Electricity &amp; Fuel", "Survival Info · Companion guides").replace("Survival Info · Vol. 1 · Electricity & Fuel", "Survival Info · Companion guides")
    css = css.replace("counter(page)", '""')
    rows = [[f"<b>{G[k][1]}</b><br><span class='small'>{G[k][0]}</span>", v] for k, v in X[name]]
    body = ('<h1 class="part" style="break-before:auto"><small>Updated November 18, 2026</small>Companion Guides</h1>'
            '<p>Newer volumes in the Survival Info series cover topics this guide touches on. Look in them for:</p>'
            + table(["Guide", "What to look for"], rows) +
            '<p>The full list of volumes, with page counts and summaries, is in <b>Survival_Info_Index.pdf</b>. Each new guide has its own sources saved as PDFs in <b>Survival Info Sources/&lt;Guide&gt;/</b>.</p>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css + CSS_OVERRIDE + BIG}</style></head><body>{body}</body></html>'

def append(name, target):
    open(f'x_{name}.html', 'w').write(page_html(name))
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf=x_{name}.pdf", f"x_{name}.html"], check=True, capture_output=True)
    x = pymupdf.open(f'x_{name}.pdf'); assert x.page_count == 1, x.page_count
    d = pymupdf.open(target)
    # skip if already appended
    last = d[-1].get_text()
    if 'Companion Guides' in last and ('A D D E D' in last or 'U P D AT E D' in last or 'Updated November 1' in last or 'U P D AT E D N O V E M B E R' in last):
        d.delete_page(-1); print(name, 'replacing old companion page')
    d.insert_pdf(x); tmp = target + '.tmp.pdf'
    d.save(tmp, garbage=3, deflate=True); d.close(); shutil.move(tmp, target)
    print(name, '->', pymupdf.open(target).page_count, 'pages')

if __name__ == '__main__':
    for nm in sys.argv[1:]:
        tgt = ROOT + (f'build-bunk/Survival_Info_Bunkers_vector.pdf' if nm == 'Bunkers' else f'Survival_Info_{nm}.pdf')
        shutil.copy(tgt, f'backup_pre_v3_{nm}.pdf')
        append(nm, tgt)
