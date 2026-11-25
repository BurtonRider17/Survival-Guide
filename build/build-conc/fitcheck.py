"""Pick, per SVG, the largest font scale that introduces no new text overlaps, overflow, or box escapes.
Usage: from fitcheck import best_scales; best_scales({name: svg}) -> {name: (k, issues_at_1)}"""
import re, json, subprocess, html, tempfile, os
KS = [1.35, 1.3, 1.25, 1.2, 1.15, 1.1, 1.05, 1.0]
def scaled(svg, k):
    if k == 1.0: return svg
    return re.sub(r'font-size="([\d.]+)"', lambda m: f'font-size="{float(m.group(1))*k:.2f}"', svg)
JS = r"""
function analyze(svg){
  const sr = svg.getBoundingClientRect();
  const texts=[...svg.querySelectorAll('text')].map(t=>t.getBoundingClientRect());
  const rects=[...svg.querySelectorAll('rect,ellipse,circle')].map(r=>r.getBoundingClientRect());
  const tol=0.6, out=[];
  texts.forEach((a,i)=>{
    if(a.width==0) return;
    const m=0.008*sr.width; if(a.left<sr.left+m||a.right>sr.right-m||a.top<sr.top-tol||a.bottom>sr.bottom+tol) out.push('O'+i);
    texts.forEach((b,j)=>{ if(j<=i||b.width==0) return;
      const ox=Math.min(a.right,b.right)-Math.max(a.left,b.left), oy=Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top);
      if(ox>tol && oy>Math.max(tol, 0.25*Math.min(a.height,b.height))) out.push('T'+i+'-'+j); });
    rects.forEach((r,k)=>{ if(r.width<4) return;
      const inside = a.left>=r.left-tol&&a.right<=r.right+tol&&a.top>=r.top-tol&&a.bottom<=r.bottom+tol;
      if(inside) out.push('I'+i+'-'+k);
      else { const ox=Math.min(a.right,r.right)-Math.max(a.left,r.left), oy=Math.min(a.bottom,r.bottom)-Math.max(a.top,r.top);
             if(ox>1.0 && oy>1.0) out.push('X'+i+'-'+k); } });
  });
  return out;
}
const res={};
document.querySelectorAll('div[data-n]').forEach(d=>{res[d.dataset.n+'|'+d.dataset.k]=analyze(d.querySelector('svg'));});
document.getElementById('out').textContent=JSON.stringify(res);
"""
def best_scales(svgs, ks=KS):
    body = ''
    for n, s in svgs.items():
        for k in ks:
            body += f'<div data-n="{n}" data-k="{k}" style="width:518pt">{scaled(s,k)}</div>'
    doc = f'<html><head><style>body{{font-family:"IBM Plex Sans"}} svg{{width:100%;height:auto;display:block}}</style></head><body>{body}<pre id="out"></pre><script>{JS}</script></body></html>'
    fd, p = tempfile.mkstemp(suffix='.html'); os.write(fd, doc.encode()); os.close(fd)
    r = subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--virtual-time-budget=5000','--dump-dom','file://'+p], capture_output=True, text=True)
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    res = json.loads(html.unescape(m.group(1)))
    best = {}
    for n in svgs:
        base = res[f'{n}|1.0']
        bset = set(x for x in base if not x.startswith('I'))
        inside = set(x for x in base if x.startswith('I'))
        choice = 1.0
        for k in ks:
            cur = res[f'{n}|{k}']
            bad = [x for x in cur if not x.startswith('I') and x not in bset]
            lost = inside - set(x for x in cur if x.startswith('I'))
            if not bad and not lost: choice = k; break
        best[n] = (choice, sorted(bset))
    return best

def debug(svg, k):
    """Return new issues at scale k with text contents."""
    import re as _re
    texts = _re.findall(r'<text[^>]*>(.*?)</text>', svg, _re.S)
    body = ''.join(f'<div data-n="x" data-k="{kk}" style="width:518pt">{scaled(svg,kk)}</div>' for kk in (1.0, k))
    doc = f'<html><head><style>body{{font-family:"IBM Plex Sans"}} svg{{width:100%;height:auto;display:block}}</style></head><body>{body}<pre id="out"></pre><script>{JS}</script></body></html>'
    fd, p = tempfile.mkstemp(suffix='.html'); os.write(fd, doc.encode()); os.close(fd)
    r = subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--virtual-time-budget=5000','--dump-dom','file://'+p], capture_output=True, text=True)
    res = json.loads(html.unescape(re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S).group(1)))
    base = set(res['x|1.0']); cur = set(res[f'x|{k}'])
    out = []
    for x in sorted(cur - base):
        if x.startswith('I'): continue
        idx = [int(v) for v in re.findall(r'\d+', x)]
        out.append((x, texts[idx[0]] if idx else '', texts[idx[1]] if x.startswith('T') else ''))
    for x in sorted(base - cur):
        if x.startswith('I'):
            out.append(('lost-'+x, texts[int(re.findall(r'\d+',x)[0])], ''))
    return out
