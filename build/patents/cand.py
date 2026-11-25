import sys,subprocess,os,re,pymupdf
A="/cursor/stores/user/grok-bot/agents/C954393F-DDBC-4575-BA31-7DAC28CDF9C5/assets/"
want=set(a if a.endswith("A") else a+"A" for a in sys.argv[2:])
rows=subprocess.run(["python3","parse.py"]+[A+f+".txt" for f in sys.argv[1].split(",")],capture_output=True,text=True).stdout.splitlines()
os.makedirs("/tmp/cand",exist_ok=True)
for r in rows:
    c=r.split("\t")
    if c[0] not in want: continue
    want.discard(c[0])
    out=f"/tmp/cand/{c[0]}.pdf"
    if not os.path.exists(out): subprocess.run(["curl","-sL","--max-time","60","-o",out,"https://patentimages.storage.googleapis.com/"+c[3]])
    d=pymupdf.open(out); t=" ".join(p.get_text() for p in d)
    t=re.sub(r"\s+"," ",t)
    i=t.find("UNITED STATES"); 
    print("|".join(c[:6]+[c[7]]))
    print("   ", t[max(0,i):max(0,i)+260])
print("MISSING",want)
