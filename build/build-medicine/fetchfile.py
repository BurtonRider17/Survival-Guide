import json, urllib.request, urllib.parse, re, os, io, time, sys
from PIL import Image
UA={'User-Agent':'SurvivalInfoGuide/1.0 (personal educational PDF; contact none)'}
def get(url): return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30))
strip=lambda s: re.sub('<[^>]+>','',s or '').strip()
out=json.load(open('photos.json'))
jobs={"ginger":("Zingiber officinale","Zingiber officinale fresh rhizome.JPG"),"capsicum":("Capsicum annuum","-2019-09-15 Cayenne pepper (Capsicum annuum), Trimingham (1).JPG"),
      "feverfew":("Tanacetum parthenium","Feverfew.jpg"),"penicillium":("Penicillium","Penicillium_Pengo.jpg")}
for k,(sci,fn) in jobs.items():
    m=get("https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=extmetadata|url&iiurlwidth=960&titles="+urllib.parse.quote("File:"+fn))
    ii=list(m['query']['pages'].values())[0]['imageinfo'][0]; em=ii['extmetadata']
    art=strip(em.get('Artist',{}).get('value')) or strip(em.get('Credit',{}).get('value')) or 'unknown'
    print(k, '| artist:',art[:80],'| credit:',strip(em.get('Credit',{}).get('value'))[:80],'|',strip(em.get('LicenseShortName',{}).get('value')),'|',strip(em.get('ImageDescription',{}).get('value'))[:150])
    for tries in range(5):
        try: data=urllib.request.urlopen(urllib.request.Request(ii['thumburl'],headers=UA),timeout=60).read(); break
        except Exception as e: print('retry',e); time.sleep(10*(tries+1))
    im=Image.open(io.BytesIO(data)).convert('RGB'); im.thumbnail((600,600)); im.save(f"img/{k}.jpg",quality=68,optimize=True)
    out[k]=dict(sci=sci,file=fn,page=ii['descriptionurl'],license=strip(em.get('LicenseShortName',{}).get('value')),artist=art[:120],desc=strip(em.get('ImageDescription',{}).get('value'))[:200],path=os.path.abspath(f"img/{k}.jpg"))
    time.sleep(3)
json.dump(out,open('photos.json','w'),indent=1)
