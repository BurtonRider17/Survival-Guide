import os, diagrams as D
os.makedirs("svg", exist_ok=True)
for name in ["hydro_layout","pelton","head_measure","solar_wiring","series_parallel","biodiesel_flow","turbine_chart","hydro_systems","rocket_stove","region_map"]:
    open(f"svg/{name}.svg","w").write(getattr(D,name)())
