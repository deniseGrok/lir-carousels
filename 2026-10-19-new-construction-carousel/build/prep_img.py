# Oct 19 2026: crop builder photos to 1080x1350, light grade + sharpen. Builder photos only (credited on slide).
from PIL import Image, ImageEnhance, ImageFilter
R = "/workspace/lir-ai-team/content-research/carousels/2026-10-19-new-construction-carousel/raw/cand/"
O = "/workspace/lir-ai-team/content-research/carousels/2026-10-19-new-construction-carousel/build/img/"
# out name: (source, center-x 0..1, center-y 0..1, zoom>=1)
J = {
 "01.jpg": ("emo_CAR-Silverado-Model-OakCreek-Ext-Twilight-Cropped.jpg", .5, .5, 1.0),  # cover: Empire Homes Oak Creek Silverado model, twilight
 "02.jpg": ("dra_1-web-or-mls-hammers_ln-s0206-001.jpg", .45, .5, 1.0),  # D.R. Horton Anderson Street Townhomes, Hammers Ln
 "03.jpg": ("drs_robie_j_front_exterior_model_garage.jpg", .43, .5, 1.0),  # D.R. Horton Sonoma Hills, Robie (5560 Pamplona Way thumbnail)
 "04.jpg": ("drr_2_edited.jpg", .45, .5, 1.0),  # D.R. Horton Reedy Creek Preserve kitchen (replaced hazy living-room photo drr_10)
 "05.jpg": ("drk_lansing_vs_open.jpg", .5, .5, 1.0),  # D.R. Horton Skybrook Corners, Lansing open plan
 "06.jpg": ("tmi_17-web-or-mls-25-print-dsc07610.jpg", .5, .5, 1.0),  # Taylor Morrison Indian Trail Townhomes exterior
 "07.jpg": ("emc_CAR-Delaney-CalicoRidge-PRO-ext-a-scaled.jpg", .5, .5, 1.0),  # Empire Homes Calico Ridge, Delaney exterior
 "08.jpg": ("emo_CAR-Silverado-Model-OakCreek-lot21-Kitchen-Breakfast.jpg", .5, .5, 1.0),  # Empire Homes Oak Creek kitchen
 "10.jpg": ("emo_CAR-Silverado-Model-OakCreek-lot21-Family-a.jpg", .5, .5, 1.0),  # Empire Homes Oak Creek family room (replaced washed-out Calico Ridge dining photo)
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
