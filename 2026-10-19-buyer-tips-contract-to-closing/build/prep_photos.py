# Oct 19 2026 buyer tips (contract to closing). REPHOTOGRAPHED Oct 19 ~7:30 AM ET after Denise's review ("1st graphic too dark",
# "some graphics were used before", "scroll-stopping"): every photo is new, bright and checked against TEMPLATES/photo-registry.csv
# (phash/dhash + source id + Unsplash upload series + visual check) so none was used in any earlier carousel.
# Full-res originals in build/src/ (Unsplash fetched with w=3600&fit=max, Pexels originals), cover-cropped to 4:5 and resized DOWN only
# to 1080x1350, light premium grade + sharpen. P = slide: (source id, x, y, zoom) — x/y place the 4:5 window, zoom>1 crops tighter (still downscaled).
import os, urllib.request
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
B=os.path.dirname(os.path.abspath(__file__)); S=B+"/src/"; O=B+"/img/"
P={"01":("pexels-15334535",.5,1.0,1.55),
   "03":("pexels-6580215",.62,.5,1.0),
   "04":("pexels-36511381",.35,.5,1.0),
   "05":("1580587771525-78b9dba3b914",.55,.5,1.0),
   "06":("pexels-259588",.5,.5,1.0),
   "07":("pexels-4307578",.45,.5,1.0),
   "08":("pexels-38299664",.5,.5,1.0),
   "09":("pexels-5008385",.5,.5,1.0),
   "10":("pexels-8143677",.5,.5,1.0)}
INFO={"pexels-259588":"Pexels (Pixabay upload), stone-and-shingle home with long driveway, sunny","pexels-18559625":"\"A large home with lush green grass and flowers\"","pexels-8143677":"Max Vakhtbovych, \"Frontage of an Estate Under a Cloudy Sky\"","pexels-173229":"Pexels (Pixabay upload), \"White Concrete Building Near Garden\" (white mansion, garden and fountain)","pexels-36511381":"goodinblack images, \"Modern White Kitchen Interior with Elegant Lighting\"","pexels-4307578":"\"An Interior of a Dining Area\"","pexels-38299664":"Vincent Rivaud, \"Luxury Villa with Pool in Greece\"","pexels-5008385":"\"Bright Living Room Interior Design\"","pexels-35758725":"azra melek, \"Elegant White Mansion with Lush Greenery\"","pexels-6580215":"Max Vakhtbovych, \"Stylish apartment with floor to ceiling window\"","pexels-15220867":"Hiba Q. Omar, \"Modern Minimalist Kitchen Interior Design\"",
      "pexels-15334535":"Eric Prouzet, \"White Concrete Building Under Blue Sky\" (waterfront mansion)","pexels-14183030":"Sanne vils axelsen, \"A Dining Table and Chairs Near the Glass Windows\"",
      "pexels-19369803":"Jonas F, \"Sunlit Living Room in House on Sea Coast\"","pexels-15824720":"\"White Mansion Entrance\"","pexels-37736542":"Cihad YILDIZ, \"Modern Luxury Villa with Infinity Pool\""}
LIFT={}   # optional gamma lift per slide
cr=open(O+"CREDITS.txt","w")
cr.write("Photos: Unsplash License / Pexels License (no attribution required). All replaced Oct 19 2026 ~7:30 AM ET; every photo checked against TEMPLATES/photo-registry.csv (never used in an earlier carousel). Originals >=3000px, cropped/resized down only, graded Oct 19 2026.\n02 | no photo (stats)\n")
for k,(pid,x,y,z) in sorted(P.items()):
    f=S+pid+".jpg"; px=pid.startswith("pexels-")
    if not os.path.exists(f):
        n=pid.split("-")[1]
        urllib.request.urlretrieve(f"https://images.pexels.com/photos/{n}/pexels-photo-{n}.jpeg" if px else f"https://images.unsplash.com/photo-{pid}?q=92&w=3600&fit=max", f)
    im=ImageOps.exif_transpose(Image.open(f)).convert("RGB"); w,h=im.size; t=1080/1350
    cw,ch=(h*t,h) if w/h>t else (w,w/t); cw,ch=int(cw/z),int(ch/z)
    l=int((w-cw)*x); tp=int((h-ch)*y); im=im.crop((l,tp,l+cw,tp+ch))
    assert im.width>=1080, "never upscale"
    im=im.resize((1080,1350),Image.LANCZOS)
    if k in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[k])))
    r,g,b=im.split(); r=r.point(lambda v:min(255,int(v*1.02))); b=b.point(lambda v:int(v*.985)); im=Image.merge("RGB",(r,g,b))
    im=ImageEnhance.Contrast(im).enhance(1.05); im=ImageEnhance.Color(im).enhance(1.0); im=ImageEnhance.Brightness(im).enhance(1.02)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=70,threshold=2))
    im.save(O+k+".jpg",quality=93)
    if px: n=pid.split("-")[1]; cr.write(f"{k} | Pexels License (no attribution required) | https://www.pexels.com/photo/{n}/ | {INFO.get(pid,'')} | original {w}x{h}\n")
    else: cr.write(f"{k} | Unsplash License (no attribution required) | https://unsplash.com/photos/{pid} (images.unsplash.com/photo-{pid}) | source file {w}x{h}\n")
cr.close()
