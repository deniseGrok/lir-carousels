# Oct 22 2026: crop builder photos to 1080x1350, light grade + sharpen. Builder photos only (credited on slide).
from PIL import Image, ImageEnhance, ImageFilter
R = "/workspace/lir-ai-team/content-research/carousels/2026-10-22-new-construction-carousel/raw/cand/"
O = "/workspace/repos/lir-carousels/2026-10-22-new-construction-carousel/build/img/"
# out name: (source, center-x 0..1, center-y 0..1, zoom>=1)
J = {
 "01.jpg": ("mac_extcorner.jpg", .5, .5, 1.0),  # cover: Mattamy Homes Arbor Chase (Clover SC) model building corner, bright daylight (replaced tight, flat Toll exterior render)
 "02.jpg": ("tbb_great.jpg", .5, .5, 1.0),  # Toll Brothers, The Bluffs at Wesley Chapel page, great room
 "03.jpg": ("lrh_sbkit.jpg", .5, .5, 1.0),  # Lennar Redhawk page, Sweetbay kitchen photo (replaced soft Hunter render)
 "04.jpg": ("tbg_kit.jpg", .5, .5, 1.0),  # Toll Brothers Griffith Lakes, Westview kitchen
 "05.jpg": ("mac_kitg.jpg", .5, .5, 1.0),  # Mattamy Homes Arbor Chase, Sierra model kitchen (exterior moved to cover)
 "06.jpg": ("miw_4739297.jpg", .5, .5, 1.0),  # M/I Homes Whitaker Pointe, front exterior
 "07.jpg": ("drt_col.jpg", .5, .5, 1.0),  # D.R. Horton Twinleaf Meadows, Columbia front elevation
 "09.jpg": ("mac_gath.jpg", .5, .5, 1.0),  # Mattamy Homes Arbor Chase, Sierra gathering room (replaced soft M/I family room), tip slide
 "10.jpg": ("tbg_patio.jpg", .5, .5, 1.0),  # Toll Brothers Griffith Lakes, Westview outdoor patio (replaced darker dining room)
}
def prep(src, cx, cy, z):
    im = Image.open(R + src).convert("RGB"); W, H = im.size
    ch = H / z; cw = ch * 0.8
    if cw > W: cw = W; ch = cw / 0.8
    x0 = min(max(cx * W - cw / 2, 0), W - cw); y0 = min(max(cy * H - ch / 2, 0), H - ch)
    im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))
    up = 1080 / im.size[0]
    im = im.resize((1080, 1350), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.05); im = ImageEnhance.Brightness(im).enhance(1.03); im = ImageEnhance.Color(im).enhance(0.98)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.6 if up > 1.6 else 1.1, percent=85 if up > 1.6 else 60, threshold=2))
    return im, up
if __name__ == "__main__":
    import sys
    for o, (s, cx, cy, z) in J.items():
        if len(sys.argv) > 1 and o not in sys.argv[1:]: continue
        im, up = prep(s, cx, cy, z); im.save(O + o, quality=93); print(o, s, "upscale %.2fx" % up)
