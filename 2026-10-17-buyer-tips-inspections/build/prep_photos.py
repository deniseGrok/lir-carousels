# Crop Unsplash originals (3200px) down to 1080x1350 cover, light premium grade + sharpen. Oct 17 2026.
from PIL import Image, ImageEnhance, ImageFilter
C="/tmp/cand/"; O="/workspace/lir-ai-team/content-research/carousels/2026-10-17-buyer-tips-inspections/build/img/"
P={"01":("1570129477492-45c003edd2be",.5),"03":("1600210491892-03d54c0aaf87",.5),"04":("1583608205776-bfd35f0d9f83",.45),
   "05":("1600585152220-90363fe7e115",.5),"06":("1600210492486-724fe5c67fb0",.5),"07":("1600585154084-4e5fe7c39198",.45),
   "08":("1600566753086-00f18fb6b3ea",.5),"09":("1505693416388-ac5ce068fe85",.5),"10":("1564013799919-ab600027ffc6",.5)}
cr=open(O+"CREDITS.txt","w"); cr.write("Photos: Unsplash License (no attribution required). Originals at 3200px wide, cropped/resized down only, graded Oct 17 2026.\n02 | no photo (stats)\n")
for k,(pid,x) in P.items():
    im=Image.open(C+pid+".jpg").convert("RGB"); w,h=im.size; t=1080/1350
    if w/h>t: nw=int(h*t); l=int((w-nw)*x); im=im.crop((l,0,l+nw,h))
    else: nh=int(w/t); tp=int((h-nh)*.5); im=im.crop((0,tp,w,tp+nh))
    im=im.resize((1080,1350),Image.LANCZOS)
    r,g,b=im.split(); r=r.point(lambda v:min(255,int(v*1.02))); b=b.point(lambda v:int(v*.985)); im=Image.merge("RGB",(r,g,b))
    im=ImageEnhance.Contrast(im).enhance(1.05); im=ImageEnhance.Color(im).enhance(.97); im=ImageEnhance.Brightness(im).enhance(1.02)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=70,threshold=2))
    im.save(O+k+".jpg",quality=93); cr.write(f"{k} | https://unsplash.com/photos/{pid.split('-',1)[1] if False else pid} (images.unsplash.com/photo-{pid})\n")
