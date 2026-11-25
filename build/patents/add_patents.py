"""Add/replace a 'US Patents - schematics by tech level' appendix in a Survival Info guide PDF (Nov 24 2026).
Usage: python3 add_patents.py <Guide> [...]
Data: patents/data_<guide>.py defining INTRO (html), UNPATENTED (list of html), PATENTS (list of dicts:
 num, hash (patentimages pdf path), fig (patentimages drawing png path or 'pdf:N'), tier A/B/C, status, grant, inv, title, teaches, figs).
Steps: download patent PDF -> 'Survival Info Sources/<Guide>/Patents/', verify number appears in PDF text, fetch/render
drawing sheet -> patents/img/, build appendix PDF via Chrome with guidekit CSS, insert into guide before the
Companion Guides page (old appendix pages, marked in footer, are removed first). Re-run xref.py afterwards."""
import sys, os, re, html, subprocess, importlib.util, base64, io, shutil
sys.path.insert(0, '/workspace/survival-info/_common')
from guidekit import _CSS, CSS_OVERRIDE, BIG, caution
import pymupdf
from PIL import Image
ROOT = '/workspace/survival-info/'
HERE = ROOT + 'patents/'
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
MARK = "US Patents appendix"
CSS = """
.tierA{border-left:7px solid #2e7d32;background:#eaf6ea;padding:4px 14px;border-radius:5px;margin:10px 0}
.tierB{border-left:7px solid #1565c0;background:#eaf2fb;padding:4px 14px;border-radius:5px;margin:10px 0}
.tierC{border-left:7px solid #6a1b9a;background:#f3eafb;padding:4px 14px;border-radius:5px;margin:10px 0}
.pat{border:1px solid #c3ccd2;border-radius:7px;padding:9px 12px;margin:0 0 12px;break-before:page;background:#fff;break-inside:avoid;page-break-inside:avoid}
.pat .no{font-weight:800;color:#102027;font-size:14pt}.pat .ti{font-weight:700;font-size:14pt}
.pat .mt{font-size:11pt;color:#37474f;margin:3px 0;line-height:1.45}
.st{display:inline-block;font-size:9pt;font-weight:700;color:#fff;border-radius:4px;padding:1px 7px;margin-left:8px;vertical-align:middle}
.st.exp{background:#546e7a}.st.live{background:#c62828}
.pat img{display:block;width:100%;max-height:6.1in;object-fit:contain;border:1px solid #dde3e6;margin-top:7px;background:#fff}
.pat .cap{font-size:9.5pt;color:#607d8b;margin-top:3px}
.tb{display:inline-block;font-weight:800;color:#fff;border-radius:4px;padding:0 7px;margin-right:6px}
"""
TIERS = [("A", "Tier A — simple, hand-built", "Things one person can make with hand tools, scrap and local materials.", "#2e7d32"),
         ("B", "Tier B — workshop-built", "Needs a forge, lathe, castings, wire, glass or a small machine shop.", "#1565c0"),
         ("C", "Tier C — industrial", "Needs factories, precision parts, refined materials or a rebuilt industry. Kept as the target to rebuild toward.", "#6a1b9a")]

def load(name):
    spec = importlib.util.spec_from_file_location("d", HERE + f"data_{name.lower()}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def fetch(path, out):
    if os.path.exists(out) and os.path.getsize(out) > 1000: return
    subprocess.run(["curl", "-sL", "--max-time", "90", "-A", UA, "-o", out, "https://patentimages.storage.googleapis.com/" + path], check=True)

def safe(s): return re.sub(r'[\\/:*?"<>|]', '', s)[:70].strip()

def prep(name, p):
    pdir = ROOT + f"Survival Info Sources/{name}/Patents/"; os.makedirs(pdir, exist_ok=True); os.makedirs(HERE + "img", exist_ok=True)
    pdf = pdir + f"{p['num']} - {safe(p['title'])}.pdf"
    fetch(p["hash"], pdf)
    d = pymupdf.open(pdf); txt = "".join(pg.get_text() for pg in d)
    digits = re.sub(r"\D", "", p["num"]); withc = f"{int(digits):,}"
    ok = (withc in txt) or (digits in txt.replace(",", "").replace(" ", "").replace(".", ""))
    p["verified"] = ok or bool(p.get("visual")); p["pages"] = d.page_count
    img = HERE + f"img/{p['num']}.png"
    if not os.path.exists(img):
        if p["fig"].startswith("pdf:"):
            pix = d[int(p["fig"][4:]) - 1].get_pixmap(dpi=150); im = Image.open(io.BytesIO(pix.tobytes("png")))
        else:
            raw = HERE + f"img/{p['num']}_raw.png"; fetch(p["fig"], raw); im = Image.open(raw)
        im = im.convert("L")
        from PIL import ImageOps
        import numpy as np
        a = np.array(im); dk = a < 170
        a[dk.mean(axis=1) > 0.35, :] = 255; a[:, dk.mean(axis=0) > 0.35] = 255
        im = Image.fromarray(a)
        a2 = np.array(im) < 160
        rows = np.where(a2.sum(axis=1) > max(4, 0.006 * im.width))[0]; cols = np.where(a2.sum(axis=0) > max(4, 0.006 * im.height))[0]
        bb = (cols[0], rows[0], cols[-1], rows[-1]) if len(rows) and len(cols) else None
        if bb:
            pad = 12; im = im.crop((max(0, bb[0]-pad), max(0, bb[1]-pad), min(im.width, bb[2]+pad), min(im.height, bb[3]+pad)))
        from PIL import ImageFilter
        if p.get("denoise"): im = im.filter(ImageFilter.MedianFilter(5))
        if im.width > 1900 and not p.get("denoise"): im = im.filter(ImageFilter.MinFilter(3))
        if im.width > 1500: im = im.resize((1500, int(im.height * 1500 / im.width)), Image.LANCZOS)
        im = im.quantize(16); im.save(img, optimize=True)
    return pdf

def card(p, name, head=''):
    live = "live" if "force" in p["status"].lower() else "exp"
    b64 = base64.b64encode(open(HERE + f"img/{p['num']}.png", "rb").read()).decode()
    return (f'<div class="pat">{head}<span class="no">{p["num"]}</span> &mdash; <span class="ti">{html.escape(html.unescape(p["title"]))}</span>'
            f'<span class="st {live}">{p["status"]}</span>'
            f'<div class="mt">{html.escape(html.unescape(p["inv"]))} &middot; granted {p["grant"]}</div>'
            f'<div class="mt"><b>What it teaches:</b> {p["teaches"]}</div>'
            f'<div class="mt"><b>Figures worth copying:</b> {p["figs"]}</div>'
            f'<img src="data:image/png;base64,{b64}"' + (' style="max-height:5.0in"' if head else '') + '>'
            f'<div class="cap">Drawing sheet from US patent {p["num"]} (public-domain government record), rendered from the saved PDF in Survival Info Sources/{name}/Patents/. Source: patents.google.com/patent/{p["num"]}</div></div>')

def appendix_html(name, m):
    css = _CSS.replace("Survival Info · Vol. 1 · Electricity &amp; Fuel", f"Survival Info · {name} · {MARK}").replace("Survival Info · Vol. 1 · Electricity & Fuel", f"Survival Info · {name} · {MARK}")
    css = css.replace("counter(page)", '""')
    o = [f'<h1 class="part" style="break-before:auto"><small>Appendix · added November 24, 2026</small>US Patents — schematics by tech level</h1>', m.INTRO,
         '<p>Patents trade protection for full disclosure: every one had to describe the device well enough for a skilled person to build it, with drawings. '
         'Each card below gives the number, inventor, grant date, likely status, what it teaches, which figures to copy, and the key drawing sheet itself. '
         'All patents were retrieved from Google Patents and the full PDFs are saved with this guide\'s sources. "Expired" means the 20-year (older: 14/17-year) term has run out and the design is public domain.</p>']
    if m.UNPATENTED: o.append(caution("Famous inventions that were never patented", "<ul>" + "".join(f"<li>{u}</li>" for u in m.UNPATENTED) + "</ul>"))
    for code, title, desc, col in TIERS:
        ps = [p for p in m.PATENTS if p["tier"] == code]
        if not ps: continue
        head = f'<div class="tier{code}" style="margin:0 0 9px"><h2 style="margin:6px 0 2px">{title}</h2><p style="margin:2px 0 6px">{desc}</p></div>'
        o.append(card(ps[0], name, head)); o += [card(p, name) for p in ps[1:]]
    o.append('<h2 style="break-before:page">Patent sources</h2><ol class="src">' + "".join(
        f'<li>US {p["num"][2:]} — {html.escape(html.unescape(p["title"]))} ({html.escape(html.unescape(p["inv"]))}, {p["grant"]})<br><a href="https://patents.google.com/patent/{p["num"]}/en">https://patents.google.com/patent/{p["num"]}/en</a></li>' for p in m.PATENTS) + '</ol>')
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css + CSS_OVERRIDE + BIG + CSS}</style></head><body>{"".join(o)}</body></html>'

def is_comp(t): return 'Companion Guides' in t and ('Updated November 1' in t or 'U P D AT E D' in t or 'A D D E D' in t)

def run(name):
    m = load(name)
    for p in m.PATENTS: prep(name, p)
    bad = [p["num"] for p in m.PATENTS if not p["verified"]]
    print(name, "patents:", len(m.PATENTS), "unverified-by-text:", bad)
    os.makedirs(HERE + "out", exist_ok=True)
    h = HERE + f"out/app_{name}.html"; out = HERE + f"out/app_{name}.pdf"
    open(h, "w").write(appendix_html(name, m))
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={out}", h], check=True, capture_output=True)
    a = pymupdf.open(out)
    tgt = ROOT + f"Survival_Info_{name}.pdf"
    bk = HERE + f"out/backup_pre_patents_{name}.pdf"
    if not os.path.exists(bk): shutil.copy(tgt, bk)
    d = pymupdf.open(tgt)
    for i in reversed(range(d.page_count)):
        if MARK in d[i].get_text(): d.delete_page(i)
    pos = d.page_count - 1 if is_comp(d[-1].get_text()) else d.page_count
    start = pos
    d.insert_pdf(a, start_at=pos)
    toc = [e for e in d.get_toc() if "US Patents" not in e[1]]
    toc.append([1, "Appendix: US Patents — schematics by tech level", start + 1])
    try: d.set_toc(toc)
    except Exception as e: print("toc skip", e)
    tmp = tgt + ".tmp.pdf"; d.save(tmp, garbage=3, deflate=True); d.close(); shutil.move(tmp, tgt)
    print(name, "appendix", a.page_count, "pages at p", start + 1, "->", pymupdf.open(tgt).page_count, "pages", os.path.getsize(tgt), "bytes")

if __name__ == "__main__":
    for n in sys.argv[1:]: run(n)
