def P(num,h,fig,tier,grant,inv,title,teaches,figs,status="Expired",visual=False):
    d=dict(num=num,hash=h,fig=fig,tier=tier,grant=grant,inv=inv,title=title,teaches=teaches,figs=figs,status=status)
    if visual: d["visual"]=True
    return d
INTRO = "<p>These patents follow iron and steel from a charcoal kiln and a bloomery hearth to the blacksmith's shop, the rolling mill and the modern oxygen and electric steelworks. Tier A can be built by hand, Tier B needs a workshop, and Tier C is industrial and is shown so you know where bulk steel comes from. All are long expired and free to copy.</p>"
UNPATENTED = ["The <b>bloomery furnace, anvil, hammer and tongs</b> are ancient and were never patented.",
 "<b>Cementation</b> (blister steel made by packing wrought iron in charcoal) was in use in Europe by the 1600s, long before modern patent systems.",
 "<b>Benjamin Huntsman's crucible steel</b> (Sheffield, 1740s) was kept as a trade secret, not patented."]
PATENTS = [
P("US607331","50/c0/40/0aa8333f1db767/US607331.pdf","9f/35/76/cba666fb49d620/US607331-drawings-page-1.png","A","1898-07-12","Joseph Berry","Charcoal-kiln",
  "A way of stacking cordwood into a charcoal kiln (Tacoma, Washington) that gives an even draft through the whole pile: a V-shaped space in the stack is the fire-pit for lighting it, sticks are propped for ventilation underneath, and removing or closing these openings regulates the burn. Use it with Part 3 (Making Charcoal).","Sheet 1: the kiln in elevation and section with the stacked wood and air ports"),
P("US3390","54/4e/f6/9196e198a7cd8f/US3390.pdf","d8/3d/4d/fd32d34ba7dd74/US3390-drawings-page-1.png","A","1843-12-27","Simeon Guilford","Improvement in bloomery-forges",
  "A Pennsylvania bloomery forge for turning iron ore, forge cinder or scrap into wrought iron, with a cupola built over the forge fire: chimney draft pulls the heat and flame of the lower fire up through the charge in the cupola, so the waste heat is used. Shows the hearth and chimney layout of a working bloomery (see Part 4).","Sheet 1: section through the forge hearth and cupola"),
P("US1129294","9e/30/51/9aa97e38f4a624/US1129294.pdf","81/11/03/ae34f68a6350f3/US1129294-drawings-page-1.png","A","1915-02-23","Thomas H. Hyde","Blacksmith's tongs",
  "Blacksmith's tongs with a combined flat jaw and V-jaw so one pair grips both flat bar and round or square stock. A pattern you can forge yourself from mild steel (see 7.3).","Sheet 1: the tongs and jaw sections"),
P("US470764","3c/e7/0b/ff47b75a852e3f/US470764.pdf","1e/43/62/6af3ddc063df89/US470764-drawings-page-1.png","A","1892-03-15","George R. Moore","Blacksmith's vise",
  "A foot-powered vise set beside the anvil for making and repairing horseshoes: the smith clamps the hot shoe with his foot, through a double-link lever, while both hands turn the calks. A strong grip without any engine (see Part 8).","Sheet 1: vise, lever and treadle linkage"),
P("US3922","d9/ef/86/d46100195e2b25/US3922.pdf","fa/23/25/aefc264a2836a5/US3922-drawings-page-1.png","B","1845-02-24","Paul A. Sabbaton","Bloomery forge fire (hot blast)",
  "A Reading, Pennsylvania 'hot-blast bloomery forge fire' for making iron direct from ore: the blast air is heated in a system of pipes (Neilson's hot-blast pipes, first used in England) before it reaches the tuyere. A hot blast saves charcoal, the same idea used in blast furnaces.","Sheet 1: forge fire with the air-heating pipes"),
P("US161581","e8/3d/df/364ab9615c6d9f/US161581.pdf","85/47/a8/a056a3f71b7220/US161581-drawings-page-1.png","B","1875-03-30","Lewis H. Watson","Improvement in forge-blowers",
  "A hand-cranked, geared fan blower for a forge: a small crank turned slowly spins the fan fast and gives a steady blast. It replaces bellows for long smelts and forge welding (see 4.2).","Sheet 1: blower casing, fan and gearing"),
P("US846548","30/3e/f4/736ad227105c26/US846548.pdf","66/bd/03/6abb9d61bb7824/US846548-drawings-page-1.png","B","1907-03-12","Laurence F. Clar","Anvil",
  "An anvil with a removable hardened steel face plate fixed to a softer body, so a worn or chipped face can be replaced. The same principle explains why old anvils have a welded-on steel face over a wrought-iron body (see 7.2).","Sheet 1: anvil body and face plate with its fastening"),
P("US855730","c0/22/8f/500b91daca03e0/US855730.pdf","f4/86/ae/fda1edd62be467/US855730-drawings-page-1.png","B","1907-06-04","Oliver B. Reynolds","Power-hammer",
  "A crank-driven power hammer whose stroke can be adjusted, so one machine can deliver light planishing blows or heavy drawing-out blows. (See Part 8.)","Sheet 1: frame, crank, ram and stroke adjustment"),
P("US489588","cc/a1/fd/2076151ffd3fa6/US489588.pdf","ea/97/67/160066f30f8ee6/US489588-drawings-page-1.png","B","1893-01-10","George B. Lamb","Wire-drawing machine",
  "A breaking-down draw bench that pulls rod through a series of dies, making it thinner and longer at each pass. It mechanizes the hand draw plate of 11.2.","Sheet 1: drawing blocks, dies and drive"),
P("US17628","f1/7a/7a/54894f8370589c/US17628.pdf","2c/83/63/5823d72889e044/US17628-drawings-page-1.png","C","1857-06-23","William Kelly","Improvement in the manufacture of iron",
  "The Kentucky ironmaster William Kelly's pneumatic process: air blown through molten iron burns out its carbon with no added fuel. Kelly had worked on the idea independently of Bessemer, and this US patent was granted to him after an interference case (see 5.5).","Sheet 1: the converting vessel and air blast",visual=True),
P("US16082","b5/5b/30/b6793c1001c0fc/US16082.pdf","pdf:2","C","1856-11-11","Henry Bessemer","Improvement in the manufacture of iron and steel",
  "The Bessemer process: air forced up through molten pig iron in a fire-brick-lined vessel burns out the carbon and turns the iron into malleable metal in about thirty minutes. This was the first cheap bulk steel (see 5.5).","Sheet 2: the converting vessel, tuyeres and air supply"),
P("US190915","3a/b9/3b/f9f3ca9cd24391/US190915.pdf","4c/62/f9/77ed5e1db07497/US190915-drawings-page-5.png","C","1877-05-15","C. William Siemens","Improvement in regenerative gas-furnaces",
  "Siemens' regenerative furnace: hot waste gases heat brick checkerwork chambers, which then preheat the incoming gas and air, reaching the temperatures that melt steel. This is the furnace behind the open-hearth process (see 5.5).","Sheet 5: furnace section with regenerator chambers"),
P("US25565","db/37/6f/db83b85e4b254e/US25565.pdf","d4/96/b2/16fb17b8e3504b/US25565-drawings-page-1.png","C","1859-09-27","John Fritz &amp; George Fritz","Improvement in rolling mills",
  "A three-high rolling mill with feed rollers, built at the Cambria works in Johnstown, Pennsylvania: the bar passes forward between the lower pair and back between the upper pair without being lifted over, so rails and bars are rolled faster (see 11.3).","Sheet 1: the three-high stand and feed rollers"),
P("US303150","9e/50/0a/24b164fc77c346/US303150.pdf","pdf:1","C","1884-08-05","Robert A. Hadfield","Manganese steel",
  "Hadfield's manganese steel, with roughly 7&ndash;20% manganese: very tough and wear-hardening, still used for rock crusher jaws, railway crossings and digger teeth. It is non-magnetic, a trap for the magnet test in 6.2.","Page 1 of the specification (text patent; no drawing)"),
P("US707776","51/e9/61/207e14a81f2671/US707776.pdf","be/8c/46/249d6905c550ef/US707776-drawings-page-1.png","C","1902-08-26","Paul Louis Toussaint H&eacute;roult","Electric furnace",
  "An early electric arc furnace that can be tilted to pour, the ancestor of today's electric arc furnaces that melt mostly scrap steel (see 5.5 and 6.3).","Sheet 1: furnace body, electrodes and tilting mount"),
P("US1197256","31/9d/9a/247e5ea7358311/US1197256.pdf","pdf:1","C","1916-09-05","Harry Brearley","Cutlery",
  "Brearley's stainless steel for cutlery: about 9&ndash;16% chromium and no more than about 0.7% carbon, hardened so it resists rust and staining. This is why kitchen knives and many tools no longer rust.","Page 1 of the specification (text patent; no drawing)"),
P("US2800631","12/58/35/4bc17bcbf38010/US2800631.pdf","7c/dc/b9/22359fea173f9c/US2800631-drawings-page-1.png","C","1957-07-23","Theodor Suess et al. (VOEST)","Method of carrying out melting processes",
  "The top-blown oxygen (LD) process: a jet of pure oxygen blown onto molten iron from above refines it into steel in minutes. Basic oxygen furnaces of this kind make most of the world's new steel from iron ore (see 5.5).","Sheet 1: vessel and oxygen lance"),
]
