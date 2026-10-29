from PIL import Image
Image.MAX_IMAGE_PIXELS=None
# Buyer tips Oct 29 2026 photo prep (check flood risk before you buy). Full-res Pexels originals in src/ (Pexels License), resized DOWN only.
# One crop per photo: img/NN.jpg 1080x1350 (4:5 carousel). The 1:1 set reuses img/NN.jpg with background-size:cover.
# Grade (fullbleed_tips standard): autocontrast blend 0.35, slight warmth, +5% contrast, UnsharpMask(1.0,70,2).
# No 9:16 set and no Short (Denise Oct 24 2026).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={"01":("p39743605",.58,.5),"03":("p31748131",.5,.5),"04":("p8186515",.35,.5),"05":("p11593489",.45,.5),"06":("p20773072",.3,.5),
   "07":("p39383571",.75,.5),"08":("p12119223",.5,.5),"09":("p3935344",.6,.5),"10":("p7546775",.5,.5)}
LIFT={}
from PIL import ImageDraw
RT={}
# FINAL-crop px (1080x1350): slide 09 porch house number painted out with siding cloned from the left (same rows).
POST={"09":[((428, 843, 444, 870), (41, 0)), ((437, 843, 453, 870), (32, 0)), ((446, 843, 462, 870), (23, 0)), ((455, 843, 471, 870), (14, 0))]}
PRE={}
def retouch(k,im):
    for box,(dx,dy) in RT.get(k,[]):
        patch=im.crop((box[0]+dx,box[1]+dy,box[2]+dx,box[3]+dy))
        m=Image.new("L",patch.size,0); ImageDraw.Draw(m).rectangle((2,2,patch.size[0]-3,patch.size[1]-3),fill=255)
        m=m.filter(ImageFilter.GaussianBlur(1.5)); im.paste(patch,box[:2],m)
    return im
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
import sys
ONLY=sys.argv[1:]  # optional: prep only these slide keys, e.g. python3 prep_photos.py 07
for k,(f,x,y) in M.items():
    if ONLY and k not in ONLY: continue
    im=ImageOps.exif_transpose(Image.open(f"src/{f}.jpg")).convert("RGB")
    im=retouch(k,im)
    if k in PRE: im=im.crop(PRE[k])
    out=grade(crop(im,1080,1350,x,y),k)
    for box,(dx,dy) in POST.get(k,[]):
        patch=out.crop((box[0]+dx,box[1]+dy,box[2]+dx,box[3]+dy)); m=Image.new("L",patch.size,0); ImageDraw.Draw(m).rectangle((2,2,patch.size[0]-3,patch.size[1]-3),fill=255)
        out.paste(patch,box[:2],m.filter(ImageFilter.GaussianBlur(1.5)))
    out.save(f"img/{k}.jpg",quality=95); print(k,f,"ok")
