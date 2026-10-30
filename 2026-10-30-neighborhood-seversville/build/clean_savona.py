# Seversville spotlight (Oct 30 2026): remove the "500" street-number signage from the Savona Mill entrance canopy
# and the "1699 W. TRADE ST" address placard on the Bruns Avenue stop shelter
# (Denise: no visible house/address numbers). Row-wise interpolation between the canopy pixels just outside each box,
# plus faint noise so the fill matches the painted steel. Writes src/<name>-clean.jpg; originals untouched.
from PIL import Image, ImageOps
import numpy as np, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# box = (x0,y0,x1,y1, sample_x0, sample_x1): each row is filled with the mean colour of a clean canopy strip on that row.
JOBS={"cd-savona-entrance":[(1098,2246,1186,2304,1190,1215),(1600,2244,1683,2306,1560,1595)],
      "dc-savona-03":[(1268,2810,1462,2936,1225,1262),(0,2810,30,2936,40,90)],
      "mc-bruns-02":[(3553,1192,3797,1262,3543,3552)]}  # "1699 W. TRADE ST" address placard on the Bruns Avenue shelter
rng=np.random.default_rng(7)
for name,boxes in JOBS.items():
    im=np.asarray(ImageOps.exif_transpose(Image.open(f"src/{name}.jpg")).convert("RGB")).astype(float)
    for (x0,y0,x1,y1,s0,s1) in boxes:
        for y in range(y0,y1):
            im[y,x0:x1]=np.median(im[y,s0:s1],0)+rng.normal(0,2.0,(x1-x0,3))
    Image.fromarray(np.clip(im,0,255).astype("uint8")).save(f"src/{name}-clean.jpg",quality=97); print(name,"cleaned")
