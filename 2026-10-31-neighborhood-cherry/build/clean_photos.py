# Oct 31 2026 retouch (COMPLIANCE T5: no visible house numbers). Removes the "5 Empire" house-number plaque on the
# Pexels 4061970 bungalow by cloning the siding three boards above (board pitch ~31 px). Output: src/p4061970-clean.jpg
from PIL import Image, ImageDraw, ImageFilter
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
im=Image.open("src/p4061970.jpg").convert("RGB")
box=(2902,1570,2989,1645); dy=94
patch=im.crop((box[0],box[1]+dy,box[2],box[3]+dy))
from PIL import ImageStat
ref=ImageStat.Stat(im.crop((box[0]+6,box[3]+4,box[2]-2,box[3]+40))).mean   # siding just below the plaque (same light)
src=ImageStat.Stat(patch).mean
patch=Image.merge("RGB",[c.point(lambda v,k=ref[i]/src[i]:min(255,int(v*k))) for i,c in enumerate(patch.split())])  # match tone
m=Image.new("L",patch.size,0); ImageDraw.Draw(m).rectangle((3,3,patch.size[0]-1,patch.size[1]-4),fill=255); m=m.filter(ImageFilter.GaussianBlur(2))
im.paste(patch,box[:2],m); im.save("src/p4061970-clean.jpg",quality=96)
