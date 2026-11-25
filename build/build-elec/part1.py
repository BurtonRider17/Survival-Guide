import math
def danger(title, body): return f'<div class="box danger"><b class="t">{title}</b>{body}</div>'
def caution(title, body): return f'<div class="box caution"><b class="t">{title}</b>{body}</div>'
def tip(title, body): return f'<div class="box tip"><b class="t">{title}</b>{body}</div>'
def check(title, items): return f'<div class="check"><b class="t">{title}</b><ul>' + "".join(f"<li>{i}</li>" for i in items) + '</ul></div>'
def table(head, rows, numcols=(), cls=""):
    if len(rows) > 6 and "brk" not in cls: cls = (cls + " brk").strip()
    h = "<thead><tr>" + "".join(f'<th class="{"num" if i in numcols else ""}">{x}</th>' for i, x in enumerate(head)) + "</tr></thead>"
    r = "".join("<tr>" + "".join(f'<td class="{"num" if i in numcols else ""}">{x}</td>' for i, x in enumerate(row)) + "</tr>" for row in rows)
    return f'<table class="{cls}">{h}<tbody>{r}</tbody></table>'
from readable import auto_scale
def fig(svgsrc, cap, style=""):
    return f'<figure>{auto_scale(svgsrc)}<figcaption>{cap}</figcaption></figure>'

APPLIANCES = [
 ("LED light bulb (60 W-equivalent)", "8–10", "—", "0.05 (5 h)"),
 ("Phone / tablet charging", "5–20", "—", "0.02–0.05"),
 ("Laptop computer", "30–65", "—", "0.2–0.4"),
 ("Wi-Fi router / radio receiver", "5–15", "—", "0.1–0.3"),
 ("LED TV, 40–50 in", "50–100", "—", "0.2–0.4"),
 ("Refrigerator, modern ENERGY STAR", "100–200 (cycling)", "600–1,200", "1.0–1.5"),
 ("Chest freezer, 7–15 cu ft", "60–120 (cycling)", "500–800", "0.6–1.2"),
 ("CPAP (no heated humidifier)", "30–60", "—", "0.3–0.5 (8 h)"),
 ("Furnace blower (gas/oil furnace)", "300–800", "1,000–2,000", "2–6 (cold days)"),
 ("Well pump, ½–1 hp, 240 V", "700–1,500", "2,000–4,000", "1–2"),
 ("Sump pump, ⅓–½ hp", "500–1,000", "1,300–2,500", "0.5–1"),
 ("Washing machine", "400–1,000", "1,200–2,000", "0.3–1 per load"),
 ("Microwave oven (input power)", "1,000–1,500", "—", "0.2–0.4"),
 ("Electric kettle / coffee maker", "800–1,500", "—", "0.2–0.4"),
 ("Hair dryer / toaster", "800–1,800", "—", "0.1–0.2"),
 ("Space heater", "750–1,500", "—", "6–12 (8 h)"),
 ("Window air conditioner", "500–1,500", "1,500–3,000", "4–10"),
 ("Central AC, 3 ton", "3,000–3,500", "7,000–10,000", "15–30"),
 ("Electric range: one burner / oven", "1,200–2,500 / 2,000–5,000", "—", "1.5–3"),
 ("Electric water heater (tank)", "3,000–4,500", "—", "8–15"),
 ("Electric clothes dryer", "3,000–5,000", "—", "2.5–4 per load"),
 ("Circular saw / drill", "1,200–1,800 / 300–700", "2,000–3,000", "intermittent"),
]

def vdrop_table():
    R = [("14", 2.525, 15), ("12", 1.588, 20), ("10", 0.999, 30), ("8", 0.628, 50), ("6", 0.395, 65), ("4", 0.249, 85), ("2", 0.156, 115), ("1/0", 0.0983, 150)]
    amps = [5, 10, 20, 30, 50, 100]
    rows = []
    for g, r, amp in R:
        row = [f"{g} AWG <span class='small'>({ {'14':'2.1','12':'3.3','10':'5.3','8':'8.4','6':'13.3','4':'21.2','2':'33.6','1/0':'53.5'}[g]} mm²)</span>", f"{r:.3f}"]
        for I in amps:
            if I > amp: row.append("<span style='color:#b0b8bf'>too small</span>")
            else:
                L = 0.36*1000/(2*I*r)
                row.append(f"{L:.0f}")
        rows.append(row)
    return table(["Copper wire", "Ω per 1000 ft"] + [f"{a} A" for a in amps], rows, numcols=(1,2,3,4,5,6,7))

def wind_table():
    rows = []
    for d_m, d_ft in [(1.5, 5), (2.0, 6.5), (3.0, 10), (4.0, 13)]:
        A = math.pi*(d_m/2)**2
        row = [f"{d_m:g} m ({d_ft:g} ft)"]
        for v in [4, 6, 8, 10, 12]:
            P = 0.5*1.225*A*v**3*0.25
            row.append(f"{P:,.0f}")
        rows.append(row)
    return table(["Rotor diameter", "4 m/s (9 mph)", "6 m/s (13 mph)", "8 m/s (18 mph)", "10 m/s (22 mph)", "12 m/s (27 mph)"], rows, numcols=(1,2,3,4,5))

def build(D):
    h = []
    h.append('<h1 class="part" id="p1"><small>Part 1</small>Electricity Basics &amp; Safety</h1>')
    h.append('<h2 id="units">1.1 The four numbers you need: volts, amps, watts, watt-hours</h2>')
    h.append('<p>Think of electricity like water in a pipe. <b>Voltage (V)</b> is pressure. <b>Current (A, amps)</b> is the flow rate. <b>Power (W, watts)</b> is how hard the electricity is working at a given moment — pressure times flow. <b>Energy (Wh or kWh)</b> is power multiplied by time: how much work has been done, like the total gallons that went through the pipe. Batteries store energy (Wh); generators and solar panels produce power (W) for some number of hours.</p>')
    h.append('<div class="formula"><span class="eq">Watts = Volts × Amps &nbsp;&nbsp;&nbsp; P = V × I</span><span class="eq">Watt-hours = Watts × Hours &nbsp;&nbsp;&nbsp; 1 kWh = 1,000 Wh</span><span class="eq">Volts = Amps × Ohms &nbsp;&nbsp;&nbsp; V = I × R &nbsp;(Ohm’s law)</span><span class="eq">Battery Wh = Volts × Amp-hours &nbsp;&nbsp; (12 V × 100 Ah = 1,200 Wh)</span>Examples: a 60 W load on a 12 V battery draws 60 ÷ 12 = <b>5 A</b>. The same 60 W on a 120 V household circuit draws only <b>0.5 A</b>. Running that load for 10 hours uses <b>600 Wh = 0.6 kWh</b>. Higher voltage moves the same power with less current, which is why long wire runs and bigger systems use 24 V, 48 V, or higher.</div>')
    h.append('<div class="kpi"><div><b>~29 kWh/day</b>average U.S. home (all-electric, normal times)</div><div><b>3–6 kWh/day</b>a careful essential-loads-only home</div><div><b>~0.1 kWh</b>what one fit adult can pedal in an hour</div><div><b>~40 kWh</b>energy in 1 US gallon of diesel (heat value)</div></div>')
    h.append('<h2 id="load">1.2 Sizing your household load</h2>')
    h.append('<p>Every energy system starts with a <b>load list</b>: what you will run, how many watts each draws, and how many hours a day. Read the nameplate (watts, or volts × amps) or measure with a plug-in meter (e.g., Kill-A-Watt) while the grid is up. Motors (fridge, freezer, pumps, power tools) briefly draw <b>surge</b> power 2–5× their running watts when starting — your inverter or generator must handle that surge.</p>')
    h.append(table(["Appliance", "Running watts", "Starting surge (W)", "Typical kWh/day"], APPLIANCES))
    h.append('<p class="small">Typical ranges compiled from manufacturer nameplates and U.S. DOE Energy Saver appliance-energy guidance. Your appliances will differ — measure them.</p>')
    h.append('<h3>Essential-loads-only plan (example)</h3>')
    h.append(table(["Essential load", "Watts", "Hours/day", "Wh/day"], [
        ["Refrigerator (cycling, average)", "~55 avg", "24", "1,300"], ["Chest freezer (average)", "~35 avg", "24", "850"],
        ["LED lights, 6 bulbs", "60", "5", "300"], ["Well pump (¾ hp)", "1,100", "1", "1,100"],
        ["Furnace blower (winter only)", "500", "4", "2,000"], ["Laptop, phones, radio", "80", "4", "320"],
        ["CPAP or medical device", "40", "8", "320"], ["Washing machine (1 load)", "500", "1", "500"],
        ["<b>Total</b> (summer / winter)", "", "", "<b>~4,700 / ~6,700</b>"]], numcols=(1,2,3)))
    h.append(tip("How to cut the load", "Switch heating, cooking, hot water and clothes drying to <b>non-electric</b> sources (wood, propane, sun, clothesline) — these are the giant loads. Keep electricity for what only electricity can do: refrigeration, water pumping, lights, communications, medical devices and small tools. Run big loads (washer, pump, power tools) <b>in the middle of a sunny day</b> or while the generator is already running."))
    h.append('<h2 id="dcac">1.3 DC vs AC</h2>')
    h.append('<p><b>Direct current (DC)</b> flows one way — batteries, solar panels, car electrical systems (12 V), USB (5 V). <b>Alternating current (AC)</b> reverses direction 60 times a second in the U.S., Canada and Mexico (60 Hz; 120/240 V split-phase in U.S./Canada homes, 127/220 V in Mexico). Much of Central America and the Caribbean also uses 60 Hz at 110–120 V. AC is easy to transform to high voltage for long-distance transmission; DC is what batteries store. An <b>inverter</b> turns battery DC into household AC; a <b>charger/rectifier</b> turns AC into DC.</p>')
    h.append(table(["", "DC (12/24/48 V)", "AC (120/240 V)"], [
        ["Best for", "Small cabins, RVs, lights, radios, pumps, battery storage", "Running ordinary household appliances and long wire runs"],
        ["Pros", "No inverter losses (5–15%); simpler; low-voltage DC is safer to touch", "Uses standard appliances, wire and breakers; easy to transmit"],
        ["Cons", "High current at 12 V needs very thick wire; DC arcs are harder to break — use DC-rated switches/breakers", "Needs inverter (or generator); lethal voltage"]]))
    h.append('<h2 id="safety">1.4 Safety: shock, arc flash, batteries and carbon monoxide</h2>')
    h.append(danger("Electric shock kills", "As little as <b>50–100 milliamps</b> through the chest can stop a heart; ~10 mA can cause muscles to lock so you can't let go. Treat anything above <b>50 V DC or 30 V AC</b> as dangerous, especially when wet. <b>Solar panels produce full voltage whenever light hits them</b> — cover them with an opaque tarp before working on wiring. Work one-handed on live circuits where possible, use insulated tools, and verify ‘dead’ with a meter you have just tested on a known live source."))
    h.append(danger("Never backfeed a house", "Never plug a generator into a wall outlet with a ‘double male’ cord. It can electrocute you, your family, and line workers when the grid returns. Use a <b>transfer switch</b> or a breaker <b>interlock kit</b> that physically prevents the main breaker and generator breaker from being on at the same time."))
    h.append(caution("Arc flash and battery short circuits", "A battery bank can deliver <b>thousands of amps</b> into a short circuit — enough to vaporize a wrench, weld a ring to a terminal, and throw molten metal. Remove rings and watches; insulate tools; put a correctly rated <b>fuse or DC breaker on the battery positive</b>, as close to the terminal as possible (marine practice: within 7 in / 18 cm). Use lithium-rated (Class T) fuses on large lithium banks. Connect the final cable last and with care."))
    h.append(caution("Battery hazards", "<b>Lead-acid</b> batteries vent hydrogen while charging (explosive at 4% in air) and contain sulfuric acid. Ventilate the battery box to the outside at the top, keep sparks and flames away, wear goggles and gloves, and keep baking soda and water nearby for spills. <b>Lithium</b> batteries can go into thermal runaway if crushed, overcharged, or shorted; LiFePO4 is far more stable than the lithium-ion (NMC) chemistry used in most EVs and power tools. Never charge LiFePO4 below 0 °C (32 °F) unless it has a built-in heater."))
    h.append(danger("Carbon monoxide (CO) — the silent killer of power outages", "Generators, wood-gas units, charcoal grills, camp stoves and poorly-vented heaters produce CO, which is odorless and kills within minutes. <b>Never run a generator indoors, in a garage, basement, crawlspace or shed — even with the door open.</b> Keep it at least <b>20 ft (6 m)</b> from the house with the exhaust pointed away from doors, windows and vents (CDC guidance). Install battery-powered CO alarms on every level and near sleeping areas. Headache, dizziness, nausea or confusion in several people at once = get everyone into fresh air immediately."))
    h.append(check("Basic electrical safety kit", ["Digital multimeter (DC + AC volts, DC amps) and a non-contact voltage tester", "Insulated screwdrivers, wrenches and crimpers; quality hydraulic or ratchet lug crimper", "Fuses/breakers rated for DC and for your voltage; spare fuses of each size", "Safety glasses, acid-resistant gloves, baking soda, eyewash", "Battery-powered CO alarms and smoke alarms (+ spare batteries); ABC fire extinguisher (Class C rated for electrical)", "Opaque tarps for covering solar panels; lockout tags; a written wiring diagram of your system"]))
    return "\n".join(h)

def build2(D):
    h = []
    h.append('<h1 class="part" id="p2"><small>Part 2</small>Simple Energy: Solar, Batteries, Small Generators &amp; Non-Electric Options</h1>')
    h.append('<h2 id="solar">2.1 Solar: salvaging and building small systems</h2>')
    h.append('<p>Photovoltaic (PV) panels have no moving parts, last 25–30+ years, and lose only about 0.5% of output per year. After a collapse, panels will be the easiest generating equipment to scavenge: rooftops, RVs and boats, off-grid cabins, highway message signs and call boxes, farm electric-fence chargers, and warehouses of solar installers.</p>')
    h.append('<h3>What to look for when salvaging</h3>')
    h.append('<ul><li><b>Read the label on the back</b>: rated watts (Pmax), Vmp (voltage at max power), Voc (open-circuit voltage), Isc (short-circuit current). Test in full sun with a multimeter: Voc should be close to the label; Isc (meter on 10 A range, briefly) should be 70–100% of the label in strong sun.</li><li><b>Reject</b> panels with shattered glass that lets water in, burned spots or brown “snail trails” with hot spots, delaminated backsheets, or melted junction boxes. Cracked glass panels often still work for a while if you seal them with clear silicone.</li><li><b>Old “12 V” panels</b> (36 cells, Vmp ≈ 17–18 V) charge a 12 V battery directly through a simple PWM controller. <b>Modern rooftop panels</b> (60/72/120/144 cells, Vmp ≈ 30–42 V, 300–550 W) need an <b>MPPT</b> controller to charge a 12/24/48 V battery efficiently.</li><li><b>Grid-tie inverters and microinverters will NOT work without the grid</b> — they shut off by design (anti-islanding). You need an off-grid inverter or hybrid inverter-charger and a battery. Some hybrid inverters with a battery can run in off-grid mode.</li><li>Take the <b>mounting rails, MC4 connectors, PV wire, combiner boxes and DC disconnects</b> too.</li></ul>')
    h.append(danger("Removing panels from a roof", "Rooftop strings run at <b>300–600 V DC</b> (up to 1,000 V on commercial roofs) — lethal and arc-prone. Cover every panel with an opaque tarp or work at night, open the DC disconnect, then unplug MC4 connectors one string at a time without pulling them under load. Falls from roofs kill more installers than shocks: use a harness and anchor."))
    h.append('<h3>Charge controllers</h3>')
    h.append(table(["Type", "How it works", "Use when", "Sizing"], [
        ["PWM", "Switch that connects panel to battery in pulses; panel voltage is pulled down to battery voltage", "Small systems; ‘12 V’ panels with 12 V battery; cheap and simple", "Controller amps ≥ panel Isc × 1.25"],
        ["MPPT", "DC-DC converter that runs panels at their best voltage and converts excess voltage into extra current (10–30% more energy, more in cold)", "Any rooftop panel; long wire runs; 24/48 V banks", "Amps ≥ array watts ÷ battery volts × 1.25; array cold Voc must stay below controller max input V"]]))
    h.append(caution("Cold raises panel voltage", "Voc rises in cold weather (≈ +0.3% per °C below 25 °C). At −20 °C (−4 °F) a panel can make ~12–15% more voltage than its label. Exceeding the controller’s maximum input voltage destroys it — add this margin when you put panels in series."))
    h.append('<h3>A small, reliable starter system</h3>')
    h.append('<p><b>2 × 200 W panels → 30 A MPPT controller → 12 V 200 Ah LiFePO4 battery (2.5 kWh) → 1,000 W pure-sine inverter.</b> In 4 peak sun hours this produces roughly 400 W × 4 h × 0.75 (real-world losses) ≈ <b>1.2 kWh/day</b> — enough for LED lights, phones, a laptop, a radio, a CPAP and a very efficient chest freezer in summer. Double the panels and batteries (or go to 24 V) to add a refrigerator.</p>')
    h.append(fig(D.solar_wiring(), "<b>Figure 1. Simple off-grid solar wiring.</b> Fuse every positive conductor at its source (battery side). Connect battery to controller first so it can sense system voltage, then connect panels. Size cables for the inverter’s full current: a 1,000 W inverter at 12 V draws ~95 A."))
    h.append('<h2 id="batteries">2.2 Battery banks</h2>')
    h.append(table(["", "Flooded lead-acid (golf cart, forklift)", "Sealed lead-acid (AGM/gel)", "LiFePO4 (lithium iron phosphate)"], [
        ["Usable depth of discharge", "50% for long life", "50%", "80–90%"],
        ["Cycle life (to 80% capacity)", "500–1,500 (forklift up to 2,000+)", "300–800", "3,000–6,000"],
        ["Maintenance", "Add distilled water; equalize monthly", "None — but can't be refilled", "None; needs a BMS (battery management system)"],
        ["Cold tolerance", "Good (freezes only when discharged)", "Good", "Can't charge below 0 °C (32 °F)"],
        ["Abuse tolerance", "Ruined by sitting discharged (sulfation)", "Ruined by over/undercharge", "Fine sitting partly charged; BMS protects"],
        ["Salvage sources", "Golf carts, forklifts, floor scrubbers, telecom sites (2 V cells)", "UPS units, alarm panels, wheelchairs", "RVs, boats, home batteries; EV packs (experts only)"]]))
    h.append(table(["12 V lead-acid state of charge (resting 2+ h, ~25 °C)", "100%", "75%", "50%", "25%", "0%"], [
        ["Open-circuit voltage", "12.7", "12.4", "12.2", "12.0", "11.8"],
        ["Specific gravity (flooded, hydrometer)", "1.265", "1.225", "1.190", "1.155", "1.120"]], numcols=(1,2,3,4,5)))
    h.append('<p><b>Car starting batteries</b> are built for short bursts, not deep cycling; they survive only a few dozen deep cycles. Use them only as a stopgap. <b>6 V golf-cart batteries</b> wired in series pairs are the classic affordable deep-cycle bank. <b>LiFePO4</b> costs more up front but usually costs less per kWh delivered over its life. For lead-acid, charge at about 14.4–14.8 V (bulk/absorb) and 13.2–13.5 V (float) at 25 °C, adjusted for temperature; LiFePO4 at about 14.2–14.6 V with no float required (follow the maker). Multiply 12 V figures by 2 or 4 for 24 V or 48 V banks.</p>')
    h.append(fig(D.series_parallel(), "<b>Figure 2. Series, parallel and series-parallel battery wiring.</b> Same four batteries, same stored energy (4.8 kWh); only the voltage and amp-hour rating change."))
    h.append(check("Battery care", ["Lead-acid: recharge to 100% as often as possible; never leave below 50% for long", "Check flooded cells monthly: water level above plates, distilled water only, after charging", "Keep terminals clean and tight; coat with petroleum jelly or terminal grease", "Keep batteries off bare concrete floors in cold climates (insulate the box) and out of direct sun in hot ones; ideal 10–25 °C (50–77 °F)", "Log voltage, specific gravity and temperature weekly; one weak cell drags down the whole string", "LiFePO4: let the BMS do its job; store at 40–60% if unused for months"]))
    h.append('<h2 id="inverters">2.3 Inverters and wiring</h2>')
    h.append('<p>Choose a <b>pure (true) sine-wave</b> inverter: modified-sine units are cheaper but make motors, refrigerator compressors, CPAPs, chargers and some electronics run hot, buzz, or fail. Size the inverter’s <b>continuous</b> rating for the largest combination of loads you will run at once and its <b>surge</b> rating for the biggest motor start (a well pump may need 3× its running watts). Inverters draw 10–50 W just being on (idle draw) — switch off or use ‘search mode’ at night. An <b>inverter-charger</b> can also charge the batteries from a generator.</p>')
    h.append('<p><b>Rule of thumb for system voltage:</b> up to ~1,000–1,500 W of inverter → 12 V; up to ~3,000 W → 24 V; above that → 48 V. Low-voltage DC wiring must be short and thick. Keep voltage drop under 3% for important circuits. The table below gives the <b>maximum one-way distance (feet)</b> for 3% drop on a <b>12 V</b> circuit; double it for 24 V, multiply by 4 for 48 V. (Metres = feet × 0.305.)</p>')
    h.append(vdrop_table())
    h.append('<p class="small">Calculated as distance = (allowed volts drop × 1000) ÷ (2 × amps × Ω per 1000 ft). “Too small” = exceeds typical 75 °C copper ampacity; always check local electrical code (NEC/CEC) ampacity tables.</p>')
    h.append('<h2 id="mechanical">2.4 Car alternators, bicycle generators and salvaged motors</h2>')
    h.append('<p><b>Your vehicle as a generator.</b> A running car or truck can charge house batteries or run a 300–1,000 W inverter clamped to its battery. It burns roughly 0.2–0.5 gal (0.8–2 L) of fuel per hour at idle — inefficient, but useful in a pinch. Run it outdoors only (CO) and don’t exceed the alternator’s rating.</p>')
    h.append('<p><b>Automotive alternators</b> (12–14 V, 40–200 A) are everywhere and easy to drive with a belt from a small engine, water wheel, or turbine. Drawbacks: they need about <b>1,000–2,500 alternator rpm</b> to produce useful output (so wind or water drives need pulley step-up of 3:1 to 10:1), they consume 2–5 A to excite their own field, brushes wear, and efficiency is only 50–65%. Externally-regulated (older 1-wire/3-wire) units are easiest to adapt. Good for engine-driven battery chargers; poor for direct-drive wind.</p>')
    h.append('<p><b>Better generators to salvage:</b> permanent-magnet DC treadmill motors (high-voltage DC, good for small hydro and pedal power), Fisher &amp; Paykel ‘SmartDrive’ direct-drive washing-machine motors (multi-pole permanent-magnet, made for low rpm — a favorite for homemade wind and hydro), large stepper motors, and wind/hydro alternators from abandoned cabins. An ordinary 3-phase <b>induction motor can be run as a generator</b> with capacitors across its windings (the ‘IMAG’ method used in many village hydro schemes).</p>')
    h.append('<p><b>Bicycle generators</b> are best for morale and emergency communications, not for running a household: a fit adult sustains 75–100 W, so an hour of hard pedaling yields ~0.1 kWh — about one phone charge per few minutes, or a few hours of LED lighting. Use a PM DC motor driven by the rear tire or chain, a blocking diode, and a charge controller into a 12 V battery.</p>')
    h.append('<h2 id="wind">2.5 Small wind turbines</h2>')
    h.append('<p>Wind energy rises with the <b>cube</b> of wind speed: double the speed and you get 8× the power. Wind only pays where the <b>annual average wind speed is at least ~4–5 m/s (9–11 mph)</b> at hub height — the Great Plains, coastlines, ridges, Arctic coasts and Caribbean trade-wind islands. Turbulence from trees and buildings kills output and turbines: the rotor should be at least <b>30 ft (9 m) above anything within 300–500 ft (90–150 m)</b>.</p>')
    h.append('<div class="formula"><span class="eq">P (W) = ½ × 1.225 × A × v³ × efficiency</span>A = swept area in m² (π × radius²), v = wind speed in m/s, 1.225 kg/m³ = air density at sea level (about 15–20% less at 1,500–2,000 m elevation). Realistic overall efficiency for small turbines is 20–30%. <b>DOE estimate of annual energy:</b> kWh/yr ≈ 0.01328 × D² × V³ (D = rotor diameter in feet, V = average wind speed in mph). A 10 ft rotor at a 10 mph average: 0.01328 × 100 × 1,000 ≈ 1,330 kWh/yr ≈ 3.6 kWh/day.</div>')
    h.append('<p><b>Instantaneous power (W) at 25% overall efficiency, sea level:</b></p>' + wind_table())
    h.append('<p>Homebuilt turbines (e.g., Hugh Piggott-style axial-flux designs with hand-carved wooden blades) are proven and documented. Every turbine needs: a way to <b>furl</b> (turn out of the wind) or brake in storms; a <b>dump-load controller</b> — never let a wind turbine spin unloaded, it will overspeed and destroy itself; a tower guyed with properly anchored cables and tilt-up design so you can lower it for repair; and lightning grounding.</p>')
    h.append(danger("Towers and spinning blades", "Most small-wind injuries happen while raising or climbing towers. Use a tilt-up (gin-pole) tower so work is done at ground level. Stay out of the tower’s fall zone during raising. Short the turbine’s output (brake switch) before approaching it."))
    h.append('<h2 id="teg">2.6 Thermoelectric generators</h2>')
    h.append('<p>Thermoelectric (Peltier/Seebeck) modules make a small DC voltage from a temperature difference — one side on a wood stove, the other on a heat sink or water jacket. They are silent and have no moving parts, but they are only about 3–5% efficient: stove-top units deliver <b>5–30 W</b>, enough to charge phones, run LED lights or a stove fan. Use modules rated for high temperature (bismuth-telluride modules fail above ~250–320 °C) and keep the cold side cool. Handy in winter in the North, when solar is weakest and the stove runs all day anyway.</p>')
    h.append('<h2 id="gen">2.7 Generators and fuel storage</h2>')
    h.append(table(["Generator", "Typical fuel use (½ load)", "Notes"], [
        ["2 kW inverter generator (gasoline)", "0.1–0.25 gal/h (0.4–1 L/h)", "Quiet, efficient at light loads; ideal battery charger"],
        ["5–7 kW portable (gasoline)", "0.4–0.8 gal/h (1.5–3 L/h)", "Runs well pump & fridge; thirsty; short engine life (~1,000–2,000 h)"],
        ["5–7 kW portable (propane)", "~0.6–1.0 gal/h propane", "Fuel never goes stale; ~10% less power than gasoline"],
        ["6–10 kW diesel (slow-speed, 1,800 rpm)", "0.3–0.6 gal/h (1.1–2.3 L/h)", "Longest life (10,000+ h); can run on biodiesel; some on SVO (Part 4)"]]))
    h.append(tip("Generator strategy", "Generators are most efficient near 60–80% load. Instead of running one lightly all day, run it <b>1–3 hours</b> at high load to charge batteries (through an inverter-charger) and to do laundry and pumping at the same time, then shut it off and live on the batteries. This can cut fuel use by half or more."))
    h.append(table(["Fuel", "Shelf life (sealed, cool)", "With stabilizer / care", "Storage notes"], [
        ["Gasoline (E10)", "3–6 months", "1–2 years", "Ethanol absorbs water and phase-separates; ethanol-free (E0) stores better. Stabilize when fresh."],
        ["Diesel (#2)", "6–12 months", "Several years", "Add stabilizer + biocide; keep tank full (less condensation); drain water from bottom; filter before use."],
        ["Kerosene (K-1)", "Years", "Years", "Very stable; blue containers. Also a winter diesel thinner."],
        ["Propane", "Indefinite", "—", "Steel cylinders; keep valves capped. U.S. DOT cylinders need requalification 12 years after manufacture."],
        ["Biodiesel (B100)", "~6 months", "~1 year with antioxidant", "Oxidizes faster than diesel; store dark, cool, full. See Part 4."]]))
    h.append(caution("Fuel storage safety", "Use approved containers (red = gasoline, yellow = diesel, blue = kerosene). Store fuel in a detached, ventilated shed away from the house, ignition sources and well-heads; check local fire code limits in normal times (many residences are limited to about 25 gal / 95 L of gasoline). Place cans on the ground when filling — never in a truck bed or car trunk (static sparks). Rotate: use the oldest fuel first and replace it."))
    h.append('<h2 id="nonelec">2.8 Non-electric alternatives (the biggest energy savers)</h2>')
    h.append('<p>Heating, cooking and hot water are where most household energy goes. Doing them without electricity lets a small electric system cover everything else.</p>')
    h.append('<div class="cols2">')
    h.append('<div><h3>Wood heat</h3><p>A cord of wood is a stacked pile 4 × 4 × 8 ft (3.6 m³). Seasoned oak or maple holds about 20–26 million BTU per cord; pine and poplar 13–17 million. A well-insulated house in a cold climate may burn 3–8 cords per winter. Season wood 6–12 months (oak 1–2 years) to below 20% moisture. Use an EPA-certified or masonry stove, clean the chimney at least yearly (creosote fires), and keep CO and smoke alarms working.</p></div>')
    h.append('<div><h3>Rocket stoves</h3><p>An insulated L-shaped combustion chamber burns small sticks hot and nearly smokeless, cooking a pot of food with a fraction of the wood of an open fire. Build from steel cans, firebrick, or clay mixed with perlite. Larger ‘rocket mass heaters’ heat rooms but are only safe if built carefully with a proper chimney and CO alarm.</p></div>')
    h.append('<div><h3>Solar cookers</h3><p>Box cookers reach 120–150 °C (250–300 °F) on sunny days — enough to bake bread, cook beans and rice slowly, and pasteurize water. Panel cookers are cheaper; parabolic cookers are fast but can burn skin and eyes (never look at the focal point). Best in the Southwest, Mexico and the South; usable anywhere on clear days roughly March–October.</p></div>')
    h.append('<div><h3>Oil lamps and candles</h3><p>A flat-wick kerosene hurricane lantern burns about 1 fl oz (30 mL) per hour. Lamps can also burn vegetable oil or rendered fat with a thicker cotton wick (olive-oil lamps, tallow candles). Keep away from curtains; never fill a lit lamp; ventilate — open flames make soot and CO.</p></div>')
    h.append('</div>')
    h.append(fig(D.rocket_stove(), "<b>Figure 3. Rocket stove cross-section.</b> Fuel and air enter horizontally; the insulated vertical riser makes a strong draft and a hot, clean burn. The pot skirt keeps hot gas against the pot sides.", "width:72%;margin-left:auto;margin-right:auto"))
    return "\n".join(h)
