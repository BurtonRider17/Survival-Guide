import sys,re
def field(chunk,key):
    m=re.search(r'"'+key+r'":"((?:[^"\\]|\\.)*)"',chunk)
    return m.group(1) if m else ""
def status(chunk):
    states=re.findall(r'"state":"([A-Z_]+)"',chunk)
    if "ACTIVE" in states: return "ACTIVE"
    if states and all(s=="NOT_ACTIVE" for s in states): return "EXPIRED"
    return ",".join(sorted(set(states))) or "?"
seen=set()
for f in sys.argv[1:]:
    txt=open(f,encoding='utf-8',errors='replace').read()
    chunks=re.split(r'"id":"patent/',txt)
    for ch in chunks[1:]:
        n=field(ch,"publication_number")
        if not n or n in seen or not n.startswith("US"): continue
        pdf=field(ch,"pdf")
        if not pdf: continue
        seen.add(n)
        print("\t".join([n,field(ch,"grant_date"),status(ch),pdf,field(ch,"inventor")[:28],field(ch,"title").strip()[:65]]))
