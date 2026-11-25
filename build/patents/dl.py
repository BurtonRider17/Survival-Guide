# usage: dl.py NUM pdfhashpath  -> download to /tmp/cand/NUM.pdf, print number check + text head
import sys,subprocess,os,re,pymupdf
n,h=sys.argv[1],sys.argv[2]; os.makedirs("/tmp/cand",exist_ok=True); out=f"/tmp/cand/{n}.pdf"
if not os.path.exists(out): subprocess.run(["curl","-sL","--max-time","60","-o",out,"https://patentimages.storage.googleapis.com/"+h])
d=pymupdf.open(out); t=re.sub(r"\s+"," "," ".join(p.get_text() for p in d))
dg=re.sub(r"\D","",n); ok=(f"{int(dg):,}" in t) or (dg in t.replace(",","").replace(" ","").replace(".",""))
i=t.find("UNITED STATES"); print(n,"pages",d.page_count,"numOK",ok); print("  ",t[max(0,i):max(0,i)+int(sys.argv[3] if len(sys.argv)>3 else 500)])
