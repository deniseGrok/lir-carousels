# Oct 15 new construction, rebuilt in nc_style teal/gold (Denise, Oct 15 2026). Offers re-verified on builder sites Oct 15 ~8:40 AM ET.
import sys, os, subprocess; sys.path.insert(0, "/workspace/lir-ai-team/content-research/carousels/TEMPLATES")
from nc_style import PALETTES, page, shot
from PIL import Image
D = "/workspace/lir-ai-team/content-research/carousels/2026-10-15-new-construction-carousel"; B = D + "/build-teal"
P = PALETTES["teal"]; TAG = "NEW BUILD DEALS<br>NC + SC"; # Rule (Oct 15 2026): builder photos only, credited; else img=None (text-only). No stock.
def ul(x): return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"
def deal(name, who, offer, bullets):
    hs = 150 if len(name) <= 11 else 112
    return f"<h1 style='font-size:{hs}px'>{name}</h1><div class='sub'>{who}</div><div class='offer'>{offer}</div>" + ul(bullets)
S = [
 ("img/builder/dfh.jpg", "Photo: Dream Finders Homes", "<h1>8 new-build<br><em>deals.</em><br>Verified Oct 15.</h1><p class='b'>3 in NC, 5 in SC. Each checked on the builder's own website on Oct 15, 2026.</p>" + ul(["Compare the full monthly payment", "Check every deadline and lender rule"])),
 ("img/builder/pulte.jpg", "Photo: Pulte Homes", deal("Kinsdale.", "Pulte Homes · Lancaster, SC", "$75,000<br>price cut.", ["Stonebrook plan, 4 bed / 3.5 bath, 2,804 sq ft", "Now $574,774, was $649,774", "Anticipated completion Oct 2026"])),
 ("img/builder/toll.jpg", "Photo: Toll Brothers", deal("Iron Creek.", "Toll Brothers · Charlotte, NC", "Up to $25,000<br>toward closing.", ["Rooftop-terrace townhomes from $399,000", "Select homes only", "Offer runs Oct 3 – Oct 18, 2026"])),
 ("img/builder/drh.jpg", "Photo: D.R. Horton", deal("Granite Falls.", "D.R. Horton · Lancaster, SC", "$35,665<br>off list.", ["2053 Moorside Ct, 4 bed / 2.5 bath, 1,927 sq ft", "Now $349,000, was $384,665", "Pool, cabana and playground planned"])),
 ("img/builder/sdct.jpg", "Photo: Smith Douglas Homes", deal("Catawba Trace.", "Smith Douglas Homes · Catawba, NC", "Up to $16,000<br>in closing costs.", ["On inventory homes, from $255,990", "Under contract by Oct 31, 2026", "Preferred lender, title and attorney required"])),
 ("img/builder/star.jpg", "Photo: Starlight Homes", deal("Watson Hill.", "Starlight Homes · Summerville, SC", "$0 down<br>6.49% (7.223% APR).", ["30-yr fixed FHA + 3.5% forgivable DPA", "Contract Oct 1–31, close by Nov 30, 2026", "640+ credit, primary residence; limits apply"])),
 ("img/builder/sdeg.jpg", "Photo: Smith Douglas Homes", deal("Ember Glen.", "Smith Douglas Homes · Charlotte, NC", "Half off upgrades<br>up to $15,000.", ["Townhomes from $275,990, every home an end unit", "Quick move-ins $309,960 and $310,755", "Fine print not shown; ask for terms"])),
 ("img/builder/dfh.jpg", "Photo: Dream Finders Homes", deal("McFarland Estates.", "Dream Finders Homes · York, SC", "$11K<br>in savings.", ["Kenzie, 408 Brick House Rd, 3 bed, 1,958 sq ft", "Priced at $348,415", "Pool, cabana and walking trails"])),
 ("img/builder/mungo.jpg", "Photo: Mungo Homes", deal("Mungo Homes.", "Columbia-area communities, SC", "5.49% fixed<br>(6.372% APR).", ["FHA example as of Sep 25, 2026; eligible homes", "Contracts on/after Sep 14; close before Jan 12, 2027", "Until the pool of funds runs out"])),
 (None, "", "<h1 style='font-size:112px'>Want the homes<br>that qualify?<br><em>Let's match you<br>to the deal.</em></h1>"
   "<div class='box'><b>DM or comment \"DEALS\"</b><p>and we'll get started.</p></div>"
   "<div class='me'><b>Denise Wilson, REALTOR®</b><br>704-615-7347 · denise.realty1@gmail.com<br>denisewilson.lircarolinas.com</div>"
   "<div class='fine'>Offers verified on builder websites Oct 15, 2026. Terms, pricing and availability can change.</div>"),
]
assert len(S) == 10
pngs = []
for i, (img, cr, inner) in enumerate(S, 1):
    mode = "light" if i % 2 else "dark"
    for suf, sw in (("", i < 10), ("-video", False)):
        out = f"{D}/slide-{i:02d}{suf}.png"; shot(page(P, mode, i, inner, img, cr, sw, ph=(430 if i == 1 else 540), h1=(132 if i == 1 else 150), tag=TAG), out, B, f"slide-{i:02d}{suf}")
        if not suf: pngs.append(out)
ims = [Image.open(p).convert("RGB") for p in pngs]; ims[0].save(f"{D}/2026-10-15-new-construction-carousel-DRAFT.pdf", save_all=True, append_images=ims[1:], resolution=150)
ins, f, per, fade = [], "", 3.3, 0.5
for i in range(10):
    ins += ["-loop","1","-t",str(per),"-i",f"{D}/slide-{i+1:02d}-video.png"]
    f += f"[{i}:v]scale=1080:1350,pad=1080:1920:0:285:color=0x0F4C5C,setsar=1,fps=30,format=yuv420p[v{i}];"
prev = "v0"
for i in range(1, 10): f += f"[{prev}][v{i}]xfade=transition=fade:duration={fade}:offset={round(i*(per-fade),2)}[x{i}];"; prev = f"x{i}"
subprocess.run(["ffmpeg","-y","-loglevel","error",*ins,"-filter_complex",f.rstrip(";"),"-map",f"[{prev}]","-c:v","libx264","-pix_fmt","yuv420p","-r","30","-movflags","+faststart",f"{D}/2026-10-15-new-construction-carousel-youtube-short.mp4"], check=True)
