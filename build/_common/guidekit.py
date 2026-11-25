"""Shared kit for new Survival Info guides (Nov 17 2026). HTML -> PDF via headless Chrome, two-pass TOC."""
import sys, os, re, html, csv, subprocess, math
sys.path.insert(0, '/workspace/survival-info/build-elec'); sys.path.insert(0, '/workspace/survival-info/_common')
from part_css import CSS as _CSS
from readable import CSS_OVERRIDE
import fitz

REGIONS = {
 1: ("Arctic & Subarctic", "#b3e5fc"), 2: ("Pacific NW & BC", "#4db6ac"), 3: ("Prairies & Great Plains", "#ffe082"),
 4: ("Great Lakes & Midwest", "#aed581"), 5: ("Northeast & Atlantic Canada", "#81c784"), 6: ("Southeast & Gulf", "#ffab91"),
 7: ("Florida", "#f48fb1"), 8: ("Desert SW & Great Basin", "#ffcc80"), 9: ("Rocky Mountains", "#bcaaa4"),
 10: ("California", "#ce93d8"), 11: ("Northern Mexico", "#e6c07a"), 12: ("Central & Southern Mexico", "#c5e1a5"),
 13: ("Central America & Caribbean", "#80deea")}

BIG = r"""
/* new-guide readability: larger text, single column */
body { font-size: 11.5pt !important; line-height: 1.5 !important; }
.box, .check { font-size: 11pt !important; line-height: 1.5; }
table { font-size: 10.5pt !important; }
td { padding: 5px 7px !important; }
h2 { font-size: 20pt !important; } h3 { font-size: 15pt !important; }
.box b.t, .check b.t { font-size: 13pt !important; }
figcaption { font-size: 10.5pt !important; }
.region .rb { font-size: 11pt !important; line-height:1.5 !important; }
.region .rh { font-size: 15pt !important; }
.src li { font-size: 10.5pt !important; }
.toc .ts { font-size: 11.5pt !important; } .toc .tp { font-size: 15pt !important; }
.cite { font-size: 8.5pt; vertical-align: super; color:#1d5d8f; }
ol.steps li { margin-bottom: 5px; }
"""

def danger(t, b): return f'<div class="box danger"><b class="t">{t}</b>{b}</div>'
def caution(t, b): return f'<div class="box caution"><b class="t">{t}</b>{b}</div>'
def tip(t, b): return f'<div class="box tip"><b class="t">{t}</b>{b}</div>'
def check(t, items): return f'<div class="check"><b class="t">{t}</b><ul>' + "".join(f"<li>{i}</li>" for i in items) + '</ul></div>'
def table(head, rows):
    cls = "brk" if len(rows) > 5 else ""
    h = "<thead><tr>" + "".join(f'<th>{x}</th>' for x in head) + "</tr></thead>"
    r = "".join("<tr>" + "".join(f'<td>{x}</td>' for x in row) + "</tr>" for row in rows)
    return f'<table class="{cls}">{h}<tbody>{r}</tbody></table>'
def steps(items): return '<ol class="steps">' + "".join(f"<li>{i}</li>" for i in items) + '</ol>'
def ul(items): return '<ul>' + "".join(f"<li>{i}</li>" for i in items) + '</ul>'

INK = "#1f2a33"
def svg(w, h, body): return f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="IBM Plex Sans"><rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>{body}</svg>'
def t(x, y, s, size=13, anchor="start", weight="normal", fill=INK):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}">{html.escape(s)}</text>'
def line(x1, y1, x2, y2, col=INK, w=2, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{d}/>'
def arrow(x1, y1, x2, y2, col=INK, w=2):
    a = math.atan2(y2-y1, x2-x1); L = 10
    p1 = (x2 - L*math.cos(a-0.4), y2 - L*math.sin(a-0.4)); p2 = (x2 - L*math.cos(a+0.4), y2 - L*math.sin(a+0.4))
    return line(x1, y1, x2, y2, col, w) + f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>'
def rect(x, y, w, h, fill="#fff", stroke=INK, sw=2, rx=6): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def label_box(x, y, w, h, lines, fill="#eef4f7", size=14, weight="600"):
    s = rect(x, y, w, h, fill)
    n = len(lines); y0 = y + h/2 - (n-1)*size*0.62 + size*0.35
    for i, l in enumerate(lines): s += t(x + w/2, y0 + i*size*1.24, l, size, "middle", weight if i == 0 else "normal")
    return s
def flow(items, w=720, bh=64, gap=26, fill="#eef4f7"):
    """Vertical flowchart of (lines) boxes."""
    h = len(items)*(bh+gap) + 10; s = ""
    for i, ls in enumerate(items):
        y = 10 + i*(bh+gap); s += label_box(60, y, w-120, bh, ls, fill)
        if i < len(items)-1: s += arrow(w/2, y+bh, w/2, y+bh+gap-2)
    return svg(w, h, s)
def fig(svgsrc, cap): return f'<figure style="max-width:100%">{svgsrc}<figcaption>{cap}</figcaption></figure>'

def part(pid, small, title): return f'<h1 class="part" id="{pid}"><small>{small}</small>{html.escape(title)}</h1>'
def h2(sid, title): return f'<h2 id="{sid}">{html.escape(title)}</h2>'

def regions_html(R):
    out = []
    for n, txt in R.items():
        name, col = REGIONS[n]
        out.append(f'<div class="region"><div class="rh" style="background:{col}"><span class="n">{n}</span>{name}</div><div class="rb">{txt}</div></div>')
    return "\n".join(out)

class Guide:
    def __init__(self, short, title_html, subtitle, footer, toc, cover_art, companions):
        self.short, self.title_html, self.subtitle, self.footer, self.toc, self.art, self.comp = short, title_html, subtitle, footer, toc, cover_art, companions
    def toc_html(self, pages):
        o = ['<div class="toc">']
        for pid, title, subs in self.toc:
            o.append(f'<a href="#{pid}" class="tp"><span>{html.escape(title)}</span><span class="dots"></span><span class="pg">{pages.get(pid,"00")}</span></a>')
            for sid, st in subs:
                o.append(f'<a href="#{sid}" class="ts"><span>{html.escape(st)}</span><span class="dots"></span><span class="pg">{pages.get(sid,"00")}</span></a>')
        return "\n".join(o + ['</div>'])
    def sources_html(self, tsv):
        rows = [r for r in csv.reader(open(tsv), delimiter="\t") if r]
        return '<ol class="src">' + "".join(f'<li>{html.escape(t)}<br><a href="{u}">{html.escape(u)}</a></li>' for u, t in rows) + '</ol>'
    def document(self, pages, body_html):
        css = _CSS.replace("Survival Info · Vol. 1 · Electricity &amp; Fuel", f"Survival Info · {self.footer}").replace("Survival Info · Vol. 1 · Electricity & Fuel", f"Survival Info · {self.footer}")
        cover = f'''<section class="cover"><div class="band"></div><div class="series">Survival Info · Grid-Down Guide Series · North America</div>
<h1>{self.title_html}</h1><div class="sub">{self.subtitle}</div><div class="art">{self.art}</div>
<div class="foot">Companion volumes: {self.comp}. &nbsp;Print this guide and keep a paper copy — it is meant to be used when the internet is not available.</div></section>'''
        return (f'<!doctype html><html><head><meta charset="utf-8"><title>Survival Info: {html.escape(self.short)}</title><style>{css + CSS_OVERRIDE + BIG}</style></head><body>'
                + cover + '<h2 style="margin-top:0">Contents</h2>' + self.toc_html(pages) + body_html + '</body></html>')
    def render(self, pages, body_fn, out):
        open("guide.html", "w").write(self.document(pages, body_fn()))
        subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={out}", "guide.html"], check=True, capture_output=True)
    def build(self, body_fn, out):
        self.render({}, body_fn, "pass1.pdf")
        doc = fitz.open("pass1.pdf"); ids = []
        for pid, _, subs in self.toc: ids.append(pid); ids += [s for s, _ in subs]
        links = []
        for pno in range(min(5, len(doc))):
            for l in doc[pno].get_links():
                if "page" in l and l["page"] >= 0: links.append(l["page"] + 1)
        pages = dict(zip(ids, links))
        self.render(pages, body_fn, out)
        d = fitz.open(out); print(out, d.page_count, "pages", os.path.getsize(out), "bytes")
        os.makedirs("png", exist_ok=True)
        for i in range(d.page_count):
            d[i].get_pixmap(dpi=45).save(f"png/p-{i+1:02d}.png")
