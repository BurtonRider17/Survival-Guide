import sys,re
def field(c,k):
    m=re.search(r'"'+k+r'":"((?:[^"\\]|\\.)*)"',c); return m.group(1) if m else ""
for f in sys.argv[1:]:
    txt=open(f,encoding='utf-8',errors='replace').read()
    for ch in re.split(r'"id":"patent/',txt)[1:]:
        n=field(ch,"publication_number")
        if not n.startswith("US"): continue
        st=re.findall(r'"state":"([A-Z_]+)"',ch); s="ACTIVE" if "ACTIVE" in st else "EXP"
        figs=re.findall(r'"full":"([^"]+)"',ch)
        print("\t".join([n,field(ch,"grant_date"),s,field(ch,"pdf"),figs[0] if figs else "-",str(len(figs)),field(ch,"inventor")[:24],field(ch,"title").strip()[:60]]))
