# Seller tips Sun Nov 1 2026: "What stays, what goes" (fixtures, exclusions, smart devices, leased items, personal property). 10 slides.
# Signature Authority v2 (approved Oct 31 2026): TEMPLATES/signature_authority.py, spec TEMPLATES/SIGNATURE_AUTHORITY.md.
# Matches the approved reference 2026-10-31-buyer-tips-title-and-survey (4:5 @ 4f30971). Builds 4:5 (IG), 1:1 slides-1x1/ (FB), 9:16 slides-9x16/ (TikTok).
# Images: custom-generated (GenerateImage) raw 864x1152 -> build/src/gen-NN-raw.jpg; upscale 4x: python3 build_slides.py upscale
# Usage: python3 build_slides.py [upscale] [4x5 1x1 9x16]  (default: all three sizes)
# Facts and sources: ../2026-11-01-seller-tips-what-stays.md (sources A-D).
import sys, os, subprocess
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-11-01-seller-tips-what-stays"; B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B)
CONTACT = dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
GEN = dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)   # gentler grade for generated images
F = {k: dict(xy_1x1=(.5, .5), xy_9x16=(.72, .5)) for k in (1, 3, 4, 5, 6, 7, 8, 9)}
P = dict(xy=(.5, .5), crisp=GEN, bright_all=True)
SL = [
 sa.cover("gen-01.jpg", "WHAT STAYS,", "what goes", "Practical advice for<br><b>SELLERS.</b>", **P, **F[1]),
 sa.stats("Charlotte metro|September 2026",
          [("MEDIAN<br>LIST PRICE", "$424,950", "−3.1% YoY"), ("ACTIVE<br>LISTINGS", "11,182", "+10.3% YoY"),
           ("MEDIAN DAYS<br>ON MARKET", "64", "+10.3% YoY"), ("PRICE-REDUCED<br>SHARE", "26.2%", "+0.7 pts YoY")],
          "With more homes to compare, clear terms matter. Spell out what stays.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026"),
 sa.edu("gen-03.jpg", "Fixtures|usually stay.",
        "On NC's standard offer form, existing fixtures are included in the price unless excluded in writing.",
        ["Light fixtures, ceiling fans", "Built-in appliances", "Blinds, shades, curtain rods", "Mirrors and TV wall mounts"], **P, **F[3]),
 sa.edu("gen-04.jpg", "The list goes|outside, too.", "The NC form's list also covers items around the home and yard.",
        ["In-ground plants and trees", "Storage sheds", "Mailboxes, outdoor lighting", "EV chargers, solar systems"], **P, **F[4]),
 sa.edu("gen-05.jpg", "Smart devices|count, too.", "Smart versions of listed items stay. Before closing, the NC form asks you to clear them.",
        ["Thermostats, doorbells", "Security cameras, sensors", "Unpair from phones and apps", "Delete data, factory reset"], **P, **F[5]),
 sa.edu("gen-06.jpg", "Taking it?|Put it in writing.", "Plan to keep something that would normally stay? List it as excluded in the contract.",
        ["A favorite light fixture", "When in doubt, list it", "Or swap it before you list", "Repair any removal damage"], **P, **F[6]),
 sa.edu("gen-07.jpg", "Leased items|don't convey.", "Anything leased or not owned by you must be identified in the contract.",
        ["Leased alarm systems", "Leased fuel tanks", "Liens on solar or HVAC", "Ask your attorney early"], **P, **F[7]),
 sa.edu("gen-08.jpg", "Personal items|are separate.", "Freestanding items, like a refrigerator, are personal property. If one is part of the sale, list it.",
        ["Freestanding refrigerator", "Curtains and draperies", "Listed at no value in NC", "Buyer's lender may weigh in"], **P, **F[8]),
 sa.edu("gen-09.jpg", "Match the listing|to the contract.", "The NC form says not to assume an item stays or goes based on an ad.",
        ["Walk the home room by room", "Note what you plan to take", "Tell your broker before listing", "In SC, read your contract too"], **P, **F[9]),
 sa.cta("gen-10.jpg", CONTACT, xy=(.5, .5), blur=7, grade=dict(bright=1.1, gold=1.2)),
]
def upscale():
    sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES/tools")
    for n in (1, 3, 4, 5, 6, 7, 8, 9, 10):
        raw, out = os.path.join(B, "src", f"gen-{n:02d}-raw.jpg"), os.path.join(B, "src", f"gen-{n:02d}.jpg")
        if os.path.exists(raw) and (not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(raw)):
            subprocess.run([sys.executable, "/workspace/repos/lir-carousels/TEMPLATES/tools/esrgan_upscale.py", raw, out], check=True); print("upscaled", n)
if __name__ == "__main__":
    a = sys.argv[1:]
    if "upscale" in a: upscale(); a = [x for x in a if x != "upscale"]
    for fmt in (a or ["4x5", "1x1", "9x16"]):
        print(fmt, len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="seller", fmt=fmt)))
