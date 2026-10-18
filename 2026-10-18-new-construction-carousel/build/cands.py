import re,sys,os,subprocess,html
from urllib.parse import urljoin
from PIL import Image
R="/workspace/lir-ai-team/content-research/carousels/2026-10-18-new-construction-carousel/raw/"
cfg={ # page, base, keyword regex, prefix
 "tm_senata":("https://www.taylormorrison.com","senata","tms"),
 "drh_southgate":("https://www.drhorton.com","southgate","drhs"),
 "drh_westport":("https://www.drhorton.com","westport","drhw"),
 "drh_oakgrove":("https://www.drhorton.com","oak-grove|cherrybark","drho"),
 "dfh_moore":("https://dreamfindershomes.com","(?i)moore|puddle|intrigue","dfh"),
 "lgi_stage":("https://www.lgihomes.com","(?i)stagecoach","lgi"),
}
for page,(base,kw,pre) in cfg.items():
    t=html.unescape(open(R+page+".html",errors="ignore").read()).replace("\\u0026","&")
    urls=set(re.findall(r'((?:https?:)?//[^"\'\s)\\]+?\.(?:jpe?g|webp|png)|/-/media/[^"\'\s)\\]+?\.(?:jpe?g|webp|png))',t,flags=re.I))
    urls=sorted(u for u in urls if re.search(kw,u) and not re.search(r'(?i)logo|icon|floor|plan_|site.?plan|map',u))
    print("==",page,len(urls))
    for i,u in enumerate(urls[:40]):
        full=urljoin(base+"/",u)
        if "dreamfindershomes" in full: full=full.split("?")[0]
        fn=R+"cand/"+pre+"_"+os.path.basename(u.split("?")[0])
        if not os.path.exists(fn):
            subprocess.run(["curl","-sL","-m","30","-A","Mozilla/5.0","-o",fn,full])
        try: w,h=Image.open(fn).size; print(w,h,os.path.basename(fn))
        except Exception as e: print("bad",fn,full[:120])
