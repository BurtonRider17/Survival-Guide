def danger(title, body): return f'<div class="box danger"><b class="t">{title}</b>{body}</div>'
def caution(title, body): return f'<div class="box caution"><b class="t">{title}</b>{body}</div>'
def tip(title, body): return f'<div class="box tip"><b class="t">{title}</b>{body}</div>'
def check(title, items): return f'<div class="check"><b class="t">{title}</b><ul>' + "".join(f"<li>{i}</li>" for i in items) + '</ul></div>'
def table(head, rows, numcols=(), cls="", widths=None):
    cg = ""
    if widths: cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    h = "<thead><tr>" + "".join(f'<th class="{"num" if i in numcols else ""}">{x}</th>' for i, x in enumerate(head)) + "</tr></thead>"
    r = "".join("<tr>" + "".join(f'<td class="{"num" if i in numcols else ""}">{x}</td>' for i, x in enumerate(row)) + "</tr>" for row in rows)
    return f'<table class="{cls}">{cg}{h}<tbody>{r}</tbody></table>'
FIG = [0]
def fig(svgsrc, cap, style=""):
    FIG[0] += 1
    return f'<figure style="{style}">{svgsrc}<figcaption><b>Figure {FIG[0]}.</b> {cap}</figcaption></figure>'
def part(pid, n, title): return f'<h1 class="part" id="{pid}"><small>Part {n}</small>{title}</h1>'
def h2(i, s): return f'<h2 id="{i}">{s}</h2>'
