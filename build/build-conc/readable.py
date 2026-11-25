import re
CONTENT_PT = 518.0  # Letter width minus 0.65in margins each side, in pt

CSS_OVERRIDE = r"""
/* ---- readability overrides (Nov 2026) ---- */
table.brk { break-inside: auto !important; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
body { font-size: 10pt !important; line-height: 1.45 !important; }
p, li { orphans: 2; widows: 2; }
table { font-size: 9.4pt !important; margin: 8px 0 12px !important; }
th { padding: 5px 7px !important; }
td { padding: 4px 7px !important; line-height: 1.38; }
.box, .check { font-size: 10pt !important; line-height: 1.45; }
.formula { font-size: 10pt !important; }
figure { max-width: 100% !important; width: 100% !important; margin: 10px 0 14px !important; }
figcaption { font-size: 9.5pt !important; line-height: 1.4; }
.small { font-size: 9.3pt !important; }
.kpi div { font-size: 9.3pt !important; }
.legend { font-size: 9.6pt !important; gap: 4px 14px !important; }
.toc .ts { font-size: 10pt !important; margin: 2px 0 2px 12px !important; }
.toc .tp { font-size: 12.5pt !important; }
.regions { gap: 12px 14px !important; }
.regions .rb, .region .rb { font-size: 9.5pt !important; line-height: 1.42 !important; }
.region .rb p { margin: 0 0 5px !important; }
.srccols { column-count: 1 !important; }
.src li { font-size: 9.6pt !important; line-height: 1.4 !important; margin-bottom: 5px !important; }
.srccols h3 { font-size: 12.5pt !important; margin-top: 12px !important; }
"""

def scale_svg(svg, target_pt=8.0, cap=1.35):
    """Scale all font sizes in an SVG so the smallest label prints at >= target_pt at full content width."""
    m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) [\d.]+"', svg)
    if not m: return svg
    vbw = float(m.group(1))
    unit = CONTENT_PT / vbw
    sizes = [float(x) for x in re.findall(r'font-size="([\d.]+)"', svg)]
    if not sizes: return svg
    mn = min(sizes) * unit
    k = min(cap, max(1.0, target_pt / mn))
    if k <= 1.001: return svg
    return re.sub(r'font-size="([\d.]+)"', lambda mm: f'font-size="{float(mm.group(1))*k:.2f}"', svg)

import hashlib, json, os
_CACHE = '.fitcache.json'
def auto_scale(svg, target_pt=8.6):
    """Scale SVG fonts toward target_pt min (at full width), but never beyond the largest overlap-free scale."""
    from fitcheck import best_scales, scaled
    key = hashlib.md5(svg.encode()).hexdigest()
    cache = json.load(open(_CACHE)) if os.path.exists(_CACHE) else {}
    if key not in cache:
        cache[key] = best_scales({'s': svg})['s'][0]
        json.dump(cache, open(_CACHE, 'w'))
    m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) [\d.]+"', svg)
    sizes = [float(x) for x in re.findall(r'font-size="([\d.]+)"', svg)]
    if not m or not sizes: return svg
    need = target_pt / (min(sizes) * CONTENT_PT / float(m.group(1)))
    k = min(cache[key], max(1.0, need), leading_cap(svg))
    return scaled(svg, round(k, 3))

def leading_cap(svg, ratio=1.12):
    """Largest scale keeping stacked lines (same x) at >= ratio x font size apart."""
    items = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', svg, re.S):
        a = m.group(1)
        if not m.group(2).strip(): continue
        g = lambda k: (re.search(k + r'="([^"]+)"', a) or [None, None])[1]
        try: items.append((float(g('x')), float(g('y')), float(g('font-size')), g('text-anchor') or 'start'))
        except (TypeError, ValueError): pass
    cap = 9.0
    for i, (x1, y1, f1, a1) in enumerate(items):
        for (x2, y2, f2, a2) in items[i+1:]:
            dy = abs(y2 - y1); fs = max(f1, f2)
            if abs(x1 - x2) < 1.5 and a1 == a2 and 0 < dy < 1.6 * fs:
                cap = min(cap, dy / (ratio * fs))
    return max(1.0, cap)
