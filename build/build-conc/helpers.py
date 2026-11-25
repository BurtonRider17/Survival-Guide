from elecpart1 import danger, caution, tip, check
from readable import auto_scale as scale_svg
def fig(svgsrc, cap, style=""):
    return f'<figure>{scale_svg(svgsrc)}<figcaption>{cap}</figcaption></figure>'
def table(head, rows, numcols=(), cls=""):
    if len(rows) > 6 and "brk" not in cls: cls = (cls + " brk").strip()
    h = "<thead><tr>" + "".join(f'<th class="{"num" if i in numcols else ""}">{x}</th>' for i, x in enumerate(head)) + "</tr></thead>"
    r = "".join("<tr>" + "".join(f'<td class="{"num" if i in numcols else ""}">{x}</td>' for i, x in enumerate(row)) + "</tr>" for row in rows)
    return f'<table class="{cls}">{h}<tbody>{r}</tbody></table>'
