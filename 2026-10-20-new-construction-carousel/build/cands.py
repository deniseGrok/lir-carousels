import re,sys,os,subprocess,html
from urllib.parse import urljoin
from PIL import Image
R="/workspace/lir-ai-team/content-research/carousels/2026-10-20-new-construction-carousel/raw/"
cfg={
 "tm_coves":("https://www.taylormorrison.com","(?i)cove|wylie|pisgah|web|dsc|mls","tmc"),
 "drh_avalon_home":("https://www.drhorton.com","(?i)avalon|productcatalog","dra"),
 "emp_harris-farms":("https://empirehomes.com","(?i)harris|weston|kingston","emh"),
 "emp_camber-woods":("https://empirehomes.com","(?i)camber|hamilton","emc"),
 "dfh_ribbon":("https://dreamfindershomes.com","(?i)media.dreamfinders","dfr"),
 "lgi_colonial-crossing":("https://www.lgihomes.com","(?i)colonial|sitecorecloud","lgc"),
 "sd_sunset-meadows":("https://www.smithdouglas.com","(?i)cloudfront","sds"),
}
os.makedirs(R+"cand",exist_ok=True)
for page,(base,kw,pre) in cfg.items():
    if len(sys.argv)>1 and page not in sys.argv[1:]: continue
    t=html.unescape(open(R+page+".html",errors="ignore").read()).replace("\\u0026","&")
    urls=set(re.findall(r'((?:https?:)?//[^"\'\s)\\,]+?\.(?:jpe?g|webp|png)(?:\?[^"\'\s)\\,]*)?|/-/media/[^"\'\s)\\,]+?\.(?:jpe?g|webp|png)|https://dlqxt4mfnxo6k\.cloudfront\.net/[^"\'\s)\\,]+)',t,flags=re.I))
    urls=sorted(u for u in urls if re.search(kw,u) and not re.search(r'(?i)logo|icon|floor|plan_|site.?plan|map|favicon|svg',u))
    print("==",page,len(urls))
    for i,u in enumerate(urls[:60]):
        full=urljoin(base+"/",u)
        if "drhorton" in full: full=full.split("?")[0]
        if "cloudfront" in full: full=re.sub(r'/\d+/\d+$','/2000/1400',full)
        if "sitecorecloud" in full: full=full.split("?")[0]
        nm=os.path.basename(u.split("?")[0]) if "cloudfront" not in u else "img%02d.jpg"%i
        fn=R+"cand/"+pre+"_"+nm[-80:]
        if not os.path.exists(fn):
            subprocess.run(["curl","-sL","-m","30","-A","Mozilla/5.0","-o",fn,full])
        try: w,h=Image.open(fn).size; print(w,h,os.path.basename(fn))
        except Exception as e: print("bad",os.path.basename(fn),full[:120]); os.path.exists(fn) and os.remove(fn)
