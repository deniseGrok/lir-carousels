# Oct 23 2026 NC carousel: builder photos only (credited on slide). Crops each original NATIVELY for 4:5 (img/), 1:1 (1x1/img/), 9:16 (9x16/img/).
# Light grade (+5% contrast, +3% brightness) + unsharp; stronger sharpen when upscaled. Originals copied to build/src/.
import os, shutil, sys
from PIL import Image, ImageEnhance, ImageFilter
R = "/workspace/lir-ai-team/content-research/carousels/2026-10-23-new-construction-carousel/raw/cand/"
B = os.path.dirname(os.path.abspath(__file__))
# out: (source, builder, center-x, center-y)
J = {
 "01": ("lro_dover1", "Lennar", .5, .55),           # cover: Lennar Roselyn page, Dover II exterior, bright daylight (replaced tight Canton II crop showing a house number)
 "02": ("trd_terrace", "Toll Brothers", .55, .5),   # Toll Brothers at The River District page, Pamlico rooftop terrace
 "03": ("sdw_3fec70d8", "Smith Douglas Homes", .5, .5),  # Smith Douglas Winecoff page gallery, bright exterior (replaced soft overcast og:image with visible house number)
 "04": ("mbr_daycorner", "Mattamy Homes", .45, .5), # Mattamy Bailey Run page, model exteriors, day corner
 "05": ("miw_4661551r", "M/I Homes", .5, .5),       # M/I Homes Willoughby Park page, front exterior (media 4661551); house number on porch column retouched out
 "06": ("lro_dover13", "Lennar", .5, .5),           # Lennar Roselyn page, Dover II exterior
 "07": ("lvi_tag2r", "Lennar", .5, .5),             # Lennar The Vines page, Taggart townhomes; house number by the door retouched out
 "08": ("mbr_kitg", "Mattamy Homes", .5, .5),       # Mattamy Bailey Run page, Briana model kitchen + gathering room (tip slide)
 "09": ("mbr_kit", "Mattamy Homes", .5, .5),        # Mattamy Bailey Run page, Briana model kitchen (tip slide; replaced washed-out, upscaled Toll kitchen)
 "10": ("miw_2293169", "M/I Homes", .45, .5),       # M/I Homes Willoughby Park page, living room (media 2293169) (CTA; replaced dim kitchen)
}
SIZES = {"img": (1080, 1350), "1x1/img": (1080, 1080), "9x16/img": (1080, 1920)}
def prep(src, cx, cy, W, H):
    im = Image.open(R + src + ".jpg").convert("RGB"); w, h = im.size; t = W / H
    if w / h > t: cw, ch = h * t, h
    else: cw, ch = w, w / t
    x0 = min(max(cx * w - cw / 2, 0), w - cw); y0 = min(max(cy * h - ch / 2, 0), h - ch)
    im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))); up = W / im.size[0]
    im = im.resize((W, H), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.05); im = ImageEnhance.Brightness(im).enhance(1.03)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.6 if up > 1.3 else 1.1, percent=90 if up > 1.3 else 60, threshold=2))
    return im, up
if __name__ == "__main__":
    for o, (s, b, cx, cy) in J.items():
        shutil.copy(R + s + ".jpg", f"{B}/src/{s}.jpg")
        for d, (W, H) in SIZES.items():
            im, up = prep(s, cx, cy, W, H); im.save(f"{B}/{d}/{o}.jpg", quality=93); print(o, d, s, "upscale %.2fx" % up)
