# Buyer tips Mon Nov 2 2026: "Insure it before you close" (homeowners insurance for buyers). 10 slides.
# Signature Authority v2 (approved Oct 31 2026): TEMPLATES/signature_authority.py, spec TEMPLATES/SIGNATURE_AUTHORITY.md.
# Mirrors 2026-11-01-seller-tips-what-stays (15e0020) and 2026-10-31-buyer-tips-title-and-survey (4f30971).
# Builds 4:5 (IG), 1:1 slides-1x1/ (FB), 9:16 slides-9x16/ (TikTok). NO PDF: any PDF sa.build writes is deleted right after.
# Images: custom-generated (GenerateImage) raw -> build/src/gen-NN-raw.jpg; upscale 4x: python3 build_slides.py upscale
# Usage: python3 build_slides.py [upscale] [4x5 1x1 9x16]  (default: all three sizes)
# Facts and sources: ../2026-11-02-buyer-tips-homeowners-insurance.md (sources A-F).
import sys, os, subprocess, glob
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-11-02-buyer-tips-homeowners-insurance"; B = os.path.dirname(os.path.abspath(__file__)); D = os.environ.get("OUT_DIR") or os.path.dirname(B)
CONTACT = dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
GEN = dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)
F = {k: dict(xy_1x1=(.5, .5), xy_9x16=(.72, .5)) for k in (1, 3, 4, 5, 6, 7, 8, 9)}
P = dict(xy=(.5, .5), crisp=GEN, bright_all=True)
NV = "14,48,66"
def band(a0, a1, a2, a3, stop):
    return (f".gl{{background:linear-gradient(90deg,rgba({NV},{a0}) 0,rgba({NV},{a1}) 30%,rgba({NV},{a2}) 46%,"
            f"rgba({NV},{a3}) 58%,rgba({NV},0) {stop}%)!important}}")
TALL = (f".gl{{background:radial-gradient(ellipse 92% 36% at 36% 37%,rgba({NV},.84) 0,rgba({NV},.62) 55%,rgba({NV},0) 100%),"
        f"linear-gradient(90deg,rgba({NV},.7) 0,rgba({NV},.52) 40%,rgba({NV},.22) 64%,rgba({NV},0) 78%)!important}}")
STRONG, MILD = band(.9, .84, .66, .32, 70), band(.86, .78, .52, .2, 66)
X = {3: dict(css_4x5=STRONG, css_1x1=STRONG, css_9x16=TALL), 4: dict(css_4x5=STRONG), 7: dict(css_4x5=STRONG)}   # per-slide readability boosts (set Nov 2 after full-size inspection: text over bright counter, phone, sky) (e.g. {6: dict(css_4x5=STRONG, css_9x16=TALL)})
SL = [
 sa.cover("gen-01.jpg", "INSURE IT", "before you close", "Practical advice for<br><b>BUYERS.</b>", **P, **F[1], **X.get(1, {})),
 sa.stats("Charlotte metro|September 2026",
          [("MEDIAN<br>LIST PRICE", "$424,950", "−3.1% YoY"), ("ACTIVE<br>LISTINGS", "11,182", "+10.3% YoY"),
           ("MEDIAN DAYS<br>ON MARKET", "64", "+10.3% YoY"), ("PRICE-REDUCED<br>SHARE", "26.2%", "+0.7 pts YoY")],
          "More homes to compare. Price the insurance on the ones you're serious about.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026"),
 sa.edu("gen-03.jpg", "Your lender|will ask for it.", "Lenders generally require proof of homeowners insurance before they fund your loan.",
        ["Also called hazard insurance", "Often paid through escrow", "Estimated on your Loan Estimate", "Not the same as mortgage insurance"], **P, **F[3], **X.get(3, {})),
 sa.edu("gen-04.jpg", "Shop it|early.", "NC's standard offer form lists insurance availability and cost as a due diligence item.",
        ["Get quotes on the home", "Compare more than one", "You can choose the provider", "In SC, read your contract too"], **P, **F[4], **X.get(4, {})),
 sa.edu("gen-05.jpg", "Ask about|past claims.", "A CLUE report shows up to seven years of insurance claims on a home. Only the owner can order it.",
        ["Ask the seller to request it", "Free once every 12 months", "Insurers may review it", "Ask early, not at closing"], **P, **F[5], **X.get(5, {})),
 sa.edu("gen-06.jpg", "Replacement cost|or cash value?", "Replacement cost pays today's cost to repair. Actual cash value subtracts for age and wear.",
        ["Ask which your policy uses", "Age and wear lower ACV", "Belongings are often ACV", "Ask about a replacement option"], **P, **F[6], **X.get(6, {})),
 sa.edu("gen-07.jpg", "Know your|deductibles.", "A deductible can be a fixed amount or a percentage of your dwelling coverage.",
        ["Read the declarations page", "Wind or hail may be separate", "Higher deductible, lower premium", "Pick one you can cover"], **P, **F[7], **X.get(7, {})),
 sa.edu("gen-08.jpg", "Know what's|not covered.", "Standard homeowners policies don't cover flood or earthquake damage. Some policies exclude wind or hail.",
        ["Flood is a separate policy", "Ask if wind and hail are in", "Ask what each exclusion means", "Read the full policy"], **P, **F[8], **X.get(8, {})),
 sa.edu("gen-09.jpg", "In an HOA?|See its policy.", "On NC's offer form, the seller authorizes release of the HOA's insurance policy, with its coverage and deductible.",
        ["See what the HOA insures", "Note the HOA deductible", "Cover the gaps with your policy", "Ask your insurance agent"], **P, **F[9], **X.get(9, {})),
 sa.cta("gen-10.jpg", CONTACT, xy=(.5, .5), blur=7, grade=dict(bright=1.1, gold=1.2)),
]
def upscale():
    for n in (1, 3, 4, 5, 6, 7, 8, 9, 10):
        raw, out = os.path.join(B, "src", f"gen-{n:02d}-raw.jpg"), os.path.join(B, "src", f"gen-{n:02d}.jpg")
        if os.path.exists(raw) and (not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(raw)):
            subprocess.run([sys.executable, "/workspace/repos/lir-carousels/TEMPLATES/tools/esrgan_upscale.py", raw, out], check=True); print("upscaled", n)
if __name__ == "__main__":
    a = sys.argv[1:]
    if "upscale" in a: upscale(); a = [x for x in a if x != "upscale"]
    for fmt in (a or ["4x5", "1x1", "9x16"]):
        print(fmt, len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="buyer", fmt=fmt)))
    for p in glob.glob(os.path.join(D, "*.pdf")): os.remove(p); print("removed PDF (no-PDF rule)", p)
