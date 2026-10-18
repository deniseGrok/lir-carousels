# Oct 18 2026: crop builder photos to 1080x1350, light grade + sharpen. Builder photos only (credited on slide).
from PIL import Image, ImageEnhance, ImageFilter
R = "/workspace/lir-ai-team/content-research/carousels/2026-10-18-new-construction-carousel/raw/cand/"
O = "/workspace/lir-ai-team/content-research/carousels/2026-10-18-new-construction-carousel/build/img/"
# out name: (source, center-x 0..1, center-y 0..1, zoom>=1)
J = {
 "01.jpg": ("tms_14-web-or-mls-dsc04378.jpg", .45, .5, 1.0),        # cover: Taylor Morrison Senata kitchen
 "02.jpg": ("tms_4-web-or-mls-004_dji_20251023061940_0362_d.jpg", .62, .5, 1.0),  # TM Senata townhomes exterior
 "03.jpg": ("drhs_hampshire_m3.jpg", .5, .5, 1.0),                 # D.R. Horton Sanctuary at Southgate exterior (replaced tight brick crop + ceiling-heavy living room)
 "04.jpg": ("dfh_CHAR_Moore_Farms_Intrigue_1043_Rocking_Horse_Lot_632_1.jpg", .5, .5, 1.0),  # DFH 1043 Rocking Horse Rd
 "05.jpg": ("drhw_editedwestportexterior.jpg", .5, .5, 1.0),         # D.R. Horton Westport exterior
 "06.jpg": ("drho_oak_grove_model_7009_butternut_oak_ter.jpg", .5, .5, 1.0),  # D.R. Horton Oak Grove Hill model
 "07.jpg": ("sdo_552752c6e18247eceaf5fd5782effb59.jpg", .5, .5, 1.0), # Smith Douglas Cedar Meadows hero
 "08.jpg": ("sdo_fbe6951431673c32e78307b99e7c2ec9.jpg", .5, .5, 1.0), # Smith Douglas Dawson Landing hero
 "10.jpg": ("drho_windsor_c_front.jpg", .5, .5, 1.0),               # D.R. Horton Oak Grove Hill, Windsor exterior (replaced two weak ceiling-heavy interior crops)
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
