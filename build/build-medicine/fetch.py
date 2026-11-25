import json, urllib.request, urllib.parse, re, os, io, time
from PIL import Image
UA={'User-Agent':'SurvivalInfoGuide/1.0 (personal educational PDF; contact none)'}
def get(url): return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30))
species={"blackwillow":"Salix nigra","whitewillow":"Salix alba","feverfew":"Tanacetum parthenium","ginger":"Zingiber officinale",
 "cranberry":"Vaccinium macrocarpon","wildginger":"Asarum canadense","capsicum":"Capsicum annuum","penicillium":"Penicillium",
 "redelder":"Sambucus racemosa"}
out=json.load(open('photos.json')) if os.path.exists('photos.json') else {}
strip=lambda s: re.sub('<[^>]+>','',s or '').strip()
for k,tt in species.items():
    if k in out: continue
    d=get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&piprop=original|name&redirects=1&titles="+urllib.parse.quote(tt))
    p=list(d['query']['pages'].values())[0]
    if 'pageimage' not in p: print("NOIMG",k); continue
    fn=p['pageimage']
    m=get("https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=extmetadata|url&iiurlwidth=960&titles="+urllib.parse.quote("File:"+fn))
    pg=list(m['query']['pages'].values())[0]
    if 'imageinfo' not in pg: print("NOTCOMMONS",k,fn); continue
    ii=pg['imageinfo'][0]; em=ii['extmetadata']
    rec=dict(sci=tt,file=fn,thumb=ii.get('thumburl'),page=ii['descriptionurl'],license=strip(em.get('LicenseShortName',{}).get('value')),
             artist=strip(em.get('Artist',{}).get('value'))[:120],desc=strip(em.get('ImageDescription',{}).get('value'))[:200])
    data=None
    for tries in range(5):
        try: data=urllib.request.urlopen(urllib.request.Request(rec['thumb'],headers=UA),timeout=60).read(); break
        except Exception as e: print('retry',k,e); time.sleep(10*(tries+1))
    if data is None: continue
    im=Image.open(io.BytesIO(data)).convert('RGB'); im.thumbnail((600,600)); path=f"img/{k}.jpg"; im.save(path,quality=68,optimize=True)
    rec['path']=os.path.abspath(path); out[k]=rec
    print(k,'|',fn,'|',rec['license'],'|',rec['artist'][:50],'|',rec['desc'][:120]); time.sleep(3); json.dump(out,open('photos.json','w'),indent=1)
# reuse from Food guide
fp=json.load(open('/workspace/survival-info/build/photos.json'))
for k in ['elderberry','waterhemlock','poisonhemlock']:
    r=dict(fp[k]); im=Image.open('/workspace/survival-info/build/'+r['path']).convert('RGB'); im.thumbnail((600,600)); path=f"img/{k}.jpg"; im.save(path,quality=68,optimize=True); r['path']=os.path.abspath(path); out[k]=r
json.dump(out,open('photos.json','w'),indent=1)
