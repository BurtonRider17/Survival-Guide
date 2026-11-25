import math, json

FONT = "IBM Plex Sans, Arial, sans-serif"
INK = "#1f2a33"; BLUE = "#2f7fbf"; LBLUE = "#cfe6f7"; RED = "#c0392b"; GRN = "#2e7d32"
GROUND = "#e6dfc8"; GSTROKE = "#8a7d5a"; STEEL = "#7d8b96"; AMBER = "#e69b00"

TSCALE = 1.0
def svg(w, h, body, title=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" '
            f'style="font-family:{FONT};max-height:100%" role="img" aria-label="{title}">'
            '<defs>'
            f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            f'<marker id="arb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>'
            f'<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
            '<pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#b9ad8a" stroke-width="1.2"/></pattern>'
            '<pattern id="ins" width="5" height="5" patternUnits="userSpaceOnUse"><circle cx="2.5" cy="2.5" r="1" fill="#b8a27a"/></pattern>'
            f'</defs>{body}</svg>')

def t(x, y, s, size=11, anchor="start", weight="normal", fill=INK, italic=False):
    size = size * TSCALE
    st = ' font-style="italic"' if italic else ''
    lines = s.split("\n")
    out = ""
    for i, ln in enumerate(lines):
        out += f'<text x="{x}" y="{y + i*size*1.2:.1f}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}"{st}>{ln}</text>'
    return out

def lead(x1, y1, x2, y2, col=INK):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="0.8"/><circle cx="{x2}" cy="{y2}" r="2" fill="{col}"/>'

def arrow(x1, y1, x2, y2, col=INK, w=1.4, m="ar", dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" marker-end="url(#{m})"{d}/>'

def box(x, y, w, h, label, fill="#ffffff", stroke=INK, size=11, sw=1.3, weight="600", sub=None, rx=5):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    lines = label.split("\n")
    n = len(lines) + (len(sub.split("\n")) if sub else 0)
    y0 = y + h/2 - (n-1)*size*0.6 + size*0.35
    for i, ln in enumerate(lines):
        s += f'<text x="{x+w/2}" y="{y0+i*size*1.2:.1f}" font-size="{size}" text-anchor="middle" font-weight="{weight}" fill="{INK}">{ln}</text>'
    if sub:
        for j, ln in enumerate(sub.split("\n")):
            s += f'<text x="{x+w/2}" y="{y0+(len(lines)+j)*size*1.2:.1f}" font-size="{size-1.5}" text-anchor="middle" fill="#44525e">{ln}</text>'
    return s

# ---------------------------------------------------------------- 1 micro-hydro layout
# ---------------------------------------------------------------- 7 map
def albers(lon, lat, lon0=-100, lat0=40, p1=20, p2=60):
    r = math.radians
    n = (math.sin(r(p1)) + math.sin(r(p2)))/2
    C = math.cos(r(p1))**2 + 2*n*math.sin(r(p1))
    rho0 = math.sqrt(C - 2*n*math.sin(r(lat0)))/n
    rho = math.sqrt(C - 2*n*math.sin(r(lat)))/n
    th = n*r(lon - lon0)
    return rho*math.sin(th), rho0 - rho*math.cos(th)

def clip(poly, test, inter):
    out = []
    for i in range(len(poly)):
        a, b2 = poly[i-1], poly[i]
        ia, ib = test(a), test(b2)
        if ib:
            if not ia: out.append(inter(a, b2))
            out.append(b2)
        elif ia:
            out.append(inter(a, b2))
    return out

def clip_lat(poly, lat, keep_above):
    test = (lambda p: p[1] >= lat) if keep_above else (lambda p: p[1] < lat)
    def inter(a, b2):
        f = (lat - a[1])/(b2[1]-a[1]); return (a[0]+f*(b2[0]-a[0]), lat)
    return clip(poly, test, inter)

def clip_lon(poly, lon, keep_east):
    test = (lambda p: p[0] >= lon) if keep_east else (lambda p: p[0] < lon)
    def inter(a, b2):
        f = (lon - a[0])/(b2[0]-a[0]); return (lon, a[1]+f*(b2[1]-a[1]))
    return clip(poly, test, inter)

REGIONS = {
 1: ("Arctic & Subarctic", "#b3e5fc"), 2: ("Pacific NW & BC", "#4db6ac"), 3: ("Prairies & Great Plains", "#ffe082"),
 4: ("Great Lakes & Midwest", "#aed581"), 5: ("Northeast & Atlantic Canada", "#81c784"), 6: ("Southeast & Gulf", "#ffab91"),
 7: ("Florida", "#f48fb1"), 8: ("Desert SW & Great Basin", "#ffcc80"), 9: ("Rocky Mountains", "#bcaaa4"),
 10: ("California", "#ce93d8"), 11: ("Northern Mexico", "#e6c07a"), 12: ("Central & Southern Mexico", "#c5e1a5"),
 13: ("Central America & Caribbean", "#80deea")}

US = {1:["Alaska"],2:["Washington","Oregon"],3:["North Dakota","South Dakota","Nebraska","Kansas","Oklahoma"],
      4:["Minnesota","Wisconsin","Michigan","Iowa","Illinois","Indiana","Ohio","Missouri"],
      5:["Maine","New Hampshire","Vermont","Massachusetts","Rhode Island","Connecticut","New York","New Jersey","Pennsylvania","Delaware","Maryland","District of Columbia"],
      6:["Virginia","West Virginia","Kentucky","Tennessee","North Carolina","South Carolina","Georgia","Alabama","Mississippi","Louisiana","Arkansas"],
      7:["Florida"],8:["Nevada","Utah","Arizona","New Mexico"],9:["Montana","Idaho","Wyoming","Colorado"],10:["California"]}
CA = {1:["Yukon","Northwest Territories","Nunavut"],2:["British Columbia"],5:["New Brunswick","Nova Scotia","Prince Edward Island"]}
CA_SPLIT = {"Alberta":3,"Saskatchewan":3,"Manitoba":3,"Ontario":4,"Québec":5,"Newfoundland and Labrador":5}
CAM = ["GTM","BLZ","SLV","HND","NIC","CRI","PAN","CUB","JAM","HTI","DOM","PRI","BHS","TTO","VIR","VGB","AIA","KNA","ATG","MSR","DMA","LCA","VCT","GRD","BRB","CYM","TCA","ABW","CUW","MAF","SXM","BLM"]

def rings(geom):
    if geom["type"] == "Polygon": return [geom["coordinates"][0]]
    return [p[0] for p in geom["coordinates"]]

def region_map():
    import os
    d = os.path.dirname(os.path.abspath(__file__))
    S = json.load(open(os.path.join(d, "states.geojson")))
    K = json.load(open(os.path.join(d, "countries.geojson")))
    shapes = []  # (region, ring lonlat)
    def fix(ring):
        return [((lo-360) if lo > 0 else lo, la) for lo, la in ring]
    for f in S["features"]:
        p = f["properties"]; nm = p["name"]; a3 = p["adm0_a3"]
        if a3 == "USA":
            if nm == "Hawaii": continue
            for rg, names in US.items():
                if nm in names:
                    for r_ in rings(f["geometry"]): shapes.append((rg, fix(r_)))
            if nm == "Texas":
                for r_ in rings(f["geometry"]):
                    r_ = fix(r_)
                    shapes.append((3, clip_lon(r_, -97.5, False))); shapes.append((6, clip_lon(r_, -97.5, True)))
        elif a3 == "CAN":
            for rg, names in CA.items():
                if nm in names:
                    for r_ in rings(f["geometry"]): shapes.append((rg, fix(r_)))
            if nm in CA_SPLIT:
                for r_ in rings(f["geometry"]):
                    r_ = fix(r_)
                    shapes.append((1, clip_lat(r_, 55.5, True))); shapes.append((CA_SPLIT[nm], clip_lat(r_, 55.5, False)))
    for f in K["features"]:
        a3 = f["properties"]["ADM0_A3"]
        if a3 == "MEX":
            for r_ in rings(f["geometry"]):
                shapes.append((11, clip_lat(r_, 23.0, True))); shapes.append((12, clip_lat(r_, 23.0, False)))
        elif a3 in CAM:
            for r_ in rings(f["geometry"]): shapes.append((13, r_))
        elif a3 == "GRL":
            for r_ in rings(f["geometry"]): shapes.append((1, r_))
        elif a3 in ("COL","VEN","ECU","RUS","SPM","BMU"):
            for r_ in rings(f["geometry"]): shapes.append((0, fix(r_)))
    proj = []
    for rg, ring in shapes:
        if len(ring) < 3: continue
        proj.append((rg, [albers(lo, la) for lo, la in ring]))
    # view window in projected coords
    xs = [albers(-168, 60)[0], albers(-52, 50)[0]]
    x0, x1 = albers(-170, 55)[0]-0.02, albers(-52, 47)[0]
    y0, y1 = albers(-100, 4.0)[1], albers(-100, 75)[1]
    W, H = 780, 640
    sc = min(W/(x1-x0), H/(y1-y0))
    def P(x, y): return ((x-x0)*sc, H-(y-y0)*sc)
    body = f'<rect width="{W}" height="{H}" fill="#e8f1f8"/><g stroke="#ffffff" stroke-width="0.6" stroke-linejoin="round">'
    for rg, pts in proj:
        col = REGIONS[rg][1] if rg else "#d6d6d6"
        body += '<path d="M' + " L".join(f"{P(x,y)[0]:.1f},{P(x,y)[1]:.1f}" for x,y in pts) + f'Z" fill="{col}"/>'
    body += '</g>'
    labels = {1:(-125,64),2:(-123.5,49.5),3:(-102,46),4:(-89,43),5:(-71,46),6:(-86,34),7:(-81.6,28),8:(-113,36),9:(-108,43),10:(-120,37.5),11:(-106,28),12:(-99,19),13:(-82,14.5)}
    for k, (lo, la) in labels.items():
        x, y = P(*albers(lo, la))
        body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="#fff" stroke="{INK}" stroke-width="1.3"/>' + t(x, y+4, str(k), 11, "middle", "700")
    body += t(10, H-10, "Boundaries simplified along state/province lines (Texas split at ~97.5°W; Canada & Mexico split by latitude). Albers equal-area projection.", 9, italic=True)
    return svg(W, H, body, "Region map of North America")

# ======================= revised versions (override earlier defs) =======================
