"""Make tap-friendly copies of big guides: downsample images, then split into parts under ~0.95 MB.
Originals are not changed. Output: <Guide>-parts/<Guide>_PartN_pA-B.pdf (cover prepended to parts 2+)."""
import sys, os, shutil
from pathlib import Path
import pymupdf
sys.path.insert(0, '/workspace/survival-info')
from shrink_pdf import shrink_pdf
ROOT = Path('/workspace/survival-info'); LIMIT = 950_000

def size_of(doc, pages):
    d = pymupdf.open(); 
    for p in pages: d.insert_pdf(doc, from_page=p, to_page=p)
    b = d.tobytes(garbage=4, deflate=True, use_objstms=1); d.close(); return len(b)

def split(name):
    src = ROOT / f'Survival_Info_{name}.pdf'
    tmp = Path(f'/tmp/{name}_small.pdf')
    shrink_pdf(src, tmp, dpi=130, quality=72)
    doc = pymupdf.open(tmp); n = doc.page_count
    outdir = ROOT / f'{name}-parts'
    if outdir.exists(): shutil.rmtree(outdir)
    outdir.mkdir()
    def greedy(lim):
        parts = []; start = 0
        while start < n:
            end = start
            base = [] if start == 0 else [0]
            while end + 1 < n and size_of(doc, base + list(range(start, end + 2))) <= lim:
                end += 1
            parts.append((start, end)); start = end + 1
        return parts
    parts = greedy(LIMIT)
    if len(parts) > 1:
        total = size_of(doc, list(range(n)))
        lim = min(LIMIT, total / len(parts) * 1.12)
        p2 = greedy(lim)
        if len(p2) == len(parts): parts = p2
    res = []
    for i, (a, b) in enumerate(parts, 1):
        d = pymupdf.open()
        if a > 0: d.insert_pdf(doc, from_page=0, to_page=0)
        d.insert_pdf(doc, from_page=a, to_page=b)
        fn = outdir / (f'{name}_Part{i}_p{a+1}-{b+1}.pdf' if len(parts) > 1 else f'Survival_Info_{name}_compact.pdf')
        d.save(fn, garbage=4, deflate=True, use_objstms=1); d.close()
        res.append((fn.name, b - a + 1 + (1 if a > 0 else 0), fn.stat().st_size))
    print(name, n, 'pages ->', res, flush=True)

for nm in sys.argv[1:]: split(nm)
