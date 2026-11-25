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
