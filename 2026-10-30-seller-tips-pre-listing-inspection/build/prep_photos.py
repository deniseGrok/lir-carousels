from PIL import Image
Image.MAX_IMAGE_PIXELS=None
# Seller tips Oct 30 2026 photo prep (pre-listing inspection). Full-res Pexels originals in src/ (Pexels License), resized DOWN only.
# One crop per photo: img/NN.jpg 1080x1350 (4:5 carousel). The 1:1 set reuses img/NN.jpg with background-size:cover.
# Grade (fullbleed_tips standard): autocontrast blend 0.35, slight warmth, +5% contrast, UnsharpMask(1.0,70,2).
from PIL import ImageEnhance, ImageFilter, ImageOps
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={"01":("p7174108",.4,.5),"03":("p10486138",.35,.5),"04":("p7601085",.5,.5),"05":("p15667605",.45,.5),"06":("p37760262",.2,.5),
   "07":("p18038065",.5,.5),"08":("p10486204",.5,.5),"09":("p7214158",.5,.5),"10":("p259593",.55,.5)}
LIFT={}
# FINAL-crop px (1080x1350): slide 08 porch-column house number painted out with clean column cloned from above (same x).
POST={"08":[((813,910,837,970),(0,-58))]}
from PIL import ImageDraw
def grade(im,k):
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.35)
    R,G,B=im.split(); R=R.point(lambda v:min(255,int(v*1.012+1))); B=B.point(lambda v:int(v*0.988)); im=Image.merge("RGB",(R,G,B))
    im=ImageEnhance.Contrast(im).enhance(1.05); im=im.filter(ImageFilter.UnsharpMask(1.0,70,2))
    if k in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[k])))
    return im
def crop(im,W,H,x,y):
    r=max(W/im.width,H/im.height); assert r<1,(im.size,W,H)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS); l=int((im.width-W)*x); t=int((im.height-H)*y)
    return im.crop((l,t,l+W,t+H))
os.makedirs("img",exist_ok=True)
ONLY=sys.argv[1:]
for k,(f,x,y) in M.items():
    if ONLY and k not in ONLY: continue
    im=ImageOps.exif_transpose(Image.open(f"src/{f}.jpg")).convert("RGB")
    out=grade(crop(im,1080,1350,x,y),k)
    for box,(dx,dy) in POST.get(k,[]):
        patch=out.crop((box[0]+dx,box[1]+dy,box[2]+dx,box[3]+dy)); m=Image.new("L",patch.size,0); ImageDraw.Draw(m).rectangle((2,2,patch.size[0]-3,patch.size[1]-3),fill=255)
        out.paste(patch,box[:2],m.filter(ImageFilter.GaussianBlur(1.5)))
    out.save(f"img/{k}.jpg",quality=95); print(k,f,"ok")
