import sys, subprocess, importlib
sys.path.insert(0,'.')
mod=sys.argv[1]; names=sys.argv[2].split(','); out=sys.argv[3]
M=importlib.import_module(mod)
from readable import auto_scale as scale_svg
h='<html><head><style>@page{size:letter;margin:0.65in} body{margin:0;font-family:"IBM Plex Sans"} div{break-after:page}</style></head><body>'
for n in names:
    h+=f'<div><p>{n}</p>'+scale_svg(getattr(M,n)())+'</div>'
open('/tmp/gal.html','w').write(h+'</body></html>')
subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--print-to-pdf='+out,'/tmp/gal.html'],capture_output=True)
