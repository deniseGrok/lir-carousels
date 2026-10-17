# Oct 17 2026: crop builder photos to 1080x1350, light grade + sharpen. Builder photos only (credited on slide).
from PIL import Image, ImageEnhance, ImageFilter
R = "/workspace/lir-ai-team/content-research/carousels/2026-10-17-new-construction-carousel/raw/cand/"
O = "/workspace/lir-ai-team/content-research/carousels/2026-10-17-new-construction-carousel/build/img/"
# out name: (source, center-x 0..1, center-y 0..1, zoom>=1)
J = {
 "01.jpg": ("pulte_682496.jpg", .45, .5, 1.0),   # cover: Pulte Galloway Towns model living/dining
 "02.jpg": ("dfh_redoak2.jpg", .49, .5, 1.0),    # Dream Finders 4009 Grommet Ct
 "03.jpg": ("tm_drone.jpg", .55, .5, 1.0),       # Taylor Morrison Esplanade at Northgate pool
 "04.jpg": ("drhf_950_elston_f.jpg", .42, .5, 1.0), # D.R. Horton 950 Two Brothers Ln
 "05.jpg": ("empire_drone.jpg", .55, .5, 1.0),   # Empire Caswell townhomes
 "06.jpg": ("drhc_1150_comm_amenities-2.jpg", .42, .5, 1.0), # D.R. Horton Cardinal Creek pool
 "07.jpg": ("pulte_682500.jpg", .55, .5, 1.0),   # Pulte Galloway Towns kitchen
 "08.jpg": ("sd_86e4e26adeb9d2392662c923903516684221efcb.jpg", .52, .5, 1.0), # Smith Douglas (Paw Creek page)
 "10.jpg": ("pulte_682497.jpg", .35, .5, 1.0), # Pulte Galloway Towns model dining + kitchen
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
    for o, (s, cx, cy, z) in J.items():
        im, up = prep(s, cx, cy, z); im.save(O + o, quality=93); print(o, s, "upscale %.2fx" % up)
