# Myers Park spotlight photos, Oct 17 2026. Cover-crop to 1080x1350 (downscale only), refined grade:
# clean-white autocontrast (0.3% clip, 50% blend), +4% contrast, slight warmth, unsharp mask.
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
B="/workspace/lir-ai-team/content-research/carousels/2026-10-17-neighborhood-myers-park/build/"
# slide: (source file, horizontal focus 0-1, vertical focus 0-1, pre-crop box or None, brightness)
P={"01":("8583893.jpg",.45,.5,None,1.02),"02":("36595190.jpg",.5,.5,None,1.0),"03":("27379384.jpg",.5,.45,None,1.03),
   "04":("habs-duke-3k.jpg",.5,.4,(70,80,1850,2575),1.08),"05":("34193020.jpg",.5,.5,None,1.03),"06":("34405086.jpg",.5,.55,None,1.02),
   "07":("35903284.jpg",.5,.45,None,1.04),"08":("18931263.jpg",.55,.5,None,1.02),"09":("37370753.jpg",.5,.6,None,1.0),
   "10":("1570129477492-45c003edd2be.jpg",.5,.5,None,1.0)}
for k,(f,fx,fy,box,br) in P.items():
    im=Image.open(B+"src/"+f).convert("RGB")
    if box: im=im.crop(box)
    w,h=im.size; t=1080/1350
    if w/h>t: nw=int(h*t); l=int((w-nw)*fx); im=im.crop((l,0,l+nw,h))
    else: nh=int(w/t); tp=int((h-nh)*fy); im=im.crop((0,tp,w,tp+nh))
    assert im.width>=1080, (k, im.size)
    im=im.resize((1080,1350),Image.LANCZOS)
    im=Image.blend(im,ImageOps.autocontrast(im,cutoff=0.3),0.5)
    im=ImageEnhance.Contrast(im).enhance(1.04)
    r,g,b=im.split(); r=r.point(lambda v:min(255,int(v*1.015))); b=b.point(lambda v:int(v*.99)); im=Image.merge("RGB",(r,g,b))
    if br!=1.0: im=ImageEnhance.Brightness(im).enhance(br)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=65,threshold=2))
    im.save(B+"img/"+k+".jpg",quality=93)
print("ok")
