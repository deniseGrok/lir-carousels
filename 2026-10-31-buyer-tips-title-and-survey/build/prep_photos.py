from PIL import Image
Image.MAX_IMAGE_PIXELS=None
# Buyer tips Oct 31 2026 photo prep (title, survey and easements). Full-res Pexels / Unsplash originals in src/ (Pexels License / Unsplash License), resized DOWN only.
# One crop per photo: img/NN.jpg 1080x1350 (4:5 carousel). The 1:1 set reuses img/NN.jpg with background-size:cover.
# Grade (fullbleed_tips standard): autocontrast blend 0.35, slight warmth, +5% contrast, UnsharpMask(1.0,70,2).
# No 9:16 set and no Short (Denise Oct 24 2026).
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M={"01":("photo-1647579350413-a6ada4e480ed",.45,.5),"03":("p4500474",.5,.5),"04":("p6283960",.5,.5),"05":("p6782369",1.0,.5),"06":("p7914572",.5,.55),
   "07":("p10099333",.5,.5),"08":("p8082229",.5,.5),"09":("p3701434",.5,.5),"10":("photo-1784810801262-d0d27227a480",.75,.5)}
LIFT={"10":1.12}
SAT={"10":1.10}  # slide 10 sits under the dark contact-block fade, so lift and warm it slightly to keep it bright
from PIL import ImageDraw
RT={}
# Oct 31 2026 photo swap (Denise): slides 01, 06, 10 replaced (old cover read as a construction site, old 06 overcast, old 10 plain tract home).
# New: 01 Unsplash 1647579350413 (Eric Ardito), 06 Pexels 7914572 (Josh Hild; src/p7914572.jpg already has its 3 unit-number plaques retouched out), 10 Unsplash 1784810801262 (goodrich kingrey).
# The old POST retouches belonged to the replaced photos and were removed. 01 crop x=.45 keeps the wrapped house at the far left out of frame.
POST={}
PRE={"01":(0,600,4330,3464)}  # 01: trim empty sky above the house so the home reads larger on the cover
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
    if k in SAT: im=ImageEnhance.Color(im).enhance(SAT[k])
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
