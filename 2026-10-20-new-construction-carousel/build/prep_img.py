# Oct 20 2026: crop builder photos to 1080x1350, light grade + sharpen. Builder photos only (credited on slide).
from PIL import Image, ImageEnhance, ImageFilter
R = "/workspace/lir-ai-team/content-research/carousels/2026-10-20-new-construction-carousel/raw/cand/"
O = "/workspace/lir-ai-team/content-research/carousels/2026-10-20-new-construction-carousel/build/img/"
# out name: (source, center-x 0..1, center-y 0..1, zoom>=1)
J = {
 "01.jpg": ("emh_CAR-Harris-Farms-Models-ext.jpg", .38, .5, 1.0),  # cover: Empire Homes Harris Farms model homes, bright daylight (replaced sky-heavy TM lake aerial)
 "02.jpg": ("emh_CAR-Weston-Kitchen-3.jpg", .5, .5, 1.0),  # Empire Homes Harris Farms page, Weston kitchen
 "03.jpg": ("emc_weston-camberwoods-model-ext-edited-2.jpg", .5, .5, 1.0),  # Empire Homes Camber Woods, Weston model exterior
 "04.jpg": ("sds_img48.jpg", .5, .5, 1.0),  # Smith Douglas Homes Sunset Meadows plan exterior (replaced dim dining-room photo)
 "05.jpg": ("dra_lawson_c_exterior.jpg", .5, .5, 1.0),  # D.R. Horton Avalon of Gastonia, Lawson C exterior
 "06.jpg": ("tmc_pisgah-farmhouse.jpg", .5, .5, 1.0),  # Taylor Morrison The Coves on Lake Wylie, Pisgah farmhouse elevation
 "09.jpg": ("emc_car-hamilton-ken0009-family-2.jpg", .5, .5, 1.0),  # Empire Homes Hamilton family room (Camber Woods page), tip slide
 "10.jpg": ("emh_CAR-Weston-Premier-Suite-3.jpg", .5, .5, 1.0),  # Empire Homes Harris Farms page, Weston primary suite (replaced dim porch and umbrella-heavy pool photos)
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
