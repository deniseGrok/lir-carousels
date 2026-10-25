# University City spotlight (Oct 25 2026) photo prep, theme fullbleed_teal. Full-res originals in src/, resized DOWN only.
# Crops per photo: img/NN.jpg 1080x1350 (4:5 IG/LinkedIn), 1x1/img/NN.jpg 1080x1080 (square Facebook),
# and 9:16 1080x1920 frames for the Short ONLY in the temp scratch dir /tmp/uc-v916/img (deleted after the Short renders).
# Grade (fullbleed_teal standard): autocontrast blend 0.45, slight warmth, +4% contrast, UnsharpMask(1.0,70,2); LIFT = gamma brighten.
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
M={"01":("wm-unc-charlotte-8617213059",.5,.5),"02":("wm-unc-charlotte-kenlund-47492518832",.5,.5),"03":("wm-harwood-garden",.5,.5),
   "04":("wm-mcmillan-white-orchid",.55,.4),"05":("wm-unc-charlotte-main-platform",.62,.5),"06":("wm-mallard-creek-greenway",.5,.5),
   "07":("wm-jw-clay-station-03",.4,.5),"08":("p32980001",.5,.5),"09":("wm-unc-charlotte-8617216301",.5,.5),"10":("p33607464",.5,.8)}
LIFT={}
X916={}; X11={}
T="/tmp/uc-v916/img"
def grade(im,k):
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.45)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.012+1))); B=B.point(lambda v:int(v*0.988)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.04); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2))
    if k=="06": im=ImageEnhance.Contrast(im).enhance(1.12); im=ImageEnhance.Color(im).enhance(1.12)  # hazy backlit source
    if k in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[k])))
    return im
def crop(im,W,H,x,y):
    r=max(W/im.width,H/im.height); assert r<1,(im.size,W,H)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-W)*x); t=int((im.height-H)*y)
    return im.crop((l,t,l+W,t+H))
os.chdir(os.path.dirname(os.path.abspath(__file__))); os.makedirs("img",exist_ok=True); os.makedirs("1x1/img",exist_ok=True); os.makedirs(T,exist_ok=True)
for k,(f,x,y) in M.items():
    im=ImageOps.exif_transpose(Image.open(f"src/{f}.jpg")).convert("RGB")
    grade(crop(im,1080,1350,x,y),k).save(f"img/{k}.jpg",quality=95)
    grade(crop(im,1080,1080,X11.get(k,x),y),k).save(f"1x1/img/{k}.jpg",quality=95)
    grade(crop(im,1080,1920,X916.get(k,x),y),k).save(f"{T}/{k}.jpg",quality=95); print(k,f,"ok")
