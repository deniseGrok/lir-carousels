# Oct 20 2026 seller tips (net proceeds). Every photo new (Pexels originals >=2600px, checked against TEMPLATES/photo-registry.csv:
# no source-id/series hit, no close hash hit). Cropped to 4:5 and resized DOWN only to 1080x1350, light premium grade + sharpen.
import os, urllib.request
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
B=os.path.dirname(os.path.abspath(__file__)); S=B+"/src/"; O=B+"/img/"
P={"01":("pexels-34270949",.5,.5,1.0),
   "03":("pexels-19227217",.5,.5,1.0),
   "04":("pexels-39775741",.5,.38,1.0),
   "05":("pexels-6301185",.5,.5,1.0),
   "06":("pexels-10779189",.5,.5,1.0),
   "07":("pexels-15743386",.5,1.0,1.0),
   "08":("pexels-6634886",.5,.5,1.0),
   "09":("pexels-22469112",.5,.5,1.0),
   "10":("pexels-38071644",.5,.5,1.0)}
INFO={"pexels-22469112":"Bright bedroom with crisp white bedding and sheer curtains","pexels-38071644":"\"Modern white minimalist kitchen with island\"","pexels-15743386":"\"Spacious living room\" (staged, blue sofa, abstract art)","pexels-10779189":"Bright white living room with ornate plaster ceiling and tall windows","pexels-20130635":"\"Bright living room with view on yard\"","pexels-6634886":"Bright bathroom with freestanding tub by tall windows","pexels-6301185":"Bright white kitchen with island, pendant lights and open shelving","pexels-19227217":"Bright two-story foyer with double wood front doors and herringbone floor","pexels-15743369":"Bright staged bedroom with tray ceiling","pexels-19410750":"Bright sunroom living room with white sofa",
      "pexels-39775741":"White two-story home with double front porches and brick walk",
      "pexels-36774623":"Front entry with arched window, columns and boxwoods",
      "pexels-34270949":"\"Luxury mansion with grand columns in Greenville\" (brick home, white fence, curved drive)",
      "pexels-39772689":"\"Modern white kitchen with island and chandeliers\"",
      "pexels-39590349":"\"Modern Scandinavian living room with elegant decor\" (staircase)",
      "pexels-29012624":"\"Elegant modern living room with natural light\"",
      "pexels-31642449":"\"Luxurious modern marble bathroom interior design\"",
      "pexels-4661635":"Bright dining room with chandelier and stone wall",
      "pexels-30545431":"\"Contemporary white kitchen with natural light\""}
LIFT={"04":1.06}
cr=open(O+"CREDITS.txt","w")
cr.write("Photos: Pexels License (no attribution required). Selected Oct 20 2026 ~4:40 AM ET; every photo checked against TEMPLATES/photo-registry.csv (never used in an earlier carousel). Originals >=2600px, cropped/resized down only, graded Oct 20 2026.\n02 | no photo (stats)\n")
for k,(pid,x,y,z) in sorted(P.items()):
    f=S+pid+".jpg"; n=pid.split("-")[1]
    if not os.path.exists(f):
        rq=urllib.request.Request(f"https://images.pexels.com/photos/{n}/pexels-photo-{n}.jpeg",headers={"User-Agent":"Mozilla/5.0"}); open(f,"wb").write(urllib.request.urlopen(rq).read())
    im=ImageOps.exif_transpose(Image.open(f)).convert("RGB"); w,h=im.size; t=1080/1350
    cw,ch=(h*t,h) if w/h>t else (w,w/t); cw,ch=int(cw/z),int(ch/z)
    l=int((w-cw)*x); tp=int((h-ch)*y); im=im.crop((l,tp,l+cw,tp+ch))
    assert im.width>=1080, "never upscale"
    im=im.resize((1080,1350),Image.LANCZOS)
    if k in LIFT: im=im.point(lambda v:int(255*(v/255)**(1/LIFT[k])))
    r,g,b=im.split(); r=r.point(lambda v:min(255,int(v*1.02))); b=b.point(lambda v:int(v*.985)); im=Image.merge("RGB",(r,g,b))
    im=ImageEnhance.Contrast(im).enhance(1.05); im=ImageEnhance.Brightness(im).enhance(1.02)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=70,threshold=2))
    im.save(O+k+".jpg",quality=93)
    cr.write(f"{k} | Pexels License (no attribution required) | https://www.pexels.com/photo/{n}/ | {INFO.get(pid,'')} | original {w}x{h}\n")
cr.close()
