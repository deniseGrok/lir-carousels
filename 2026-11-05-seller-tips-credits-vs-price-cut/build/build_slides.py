# Seller tips Wed Nov 5 2026: "Credits vs. a price cut" (seller concessions). Signature Authority. NO PDF.
import sys, os, subprocess, glob
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-11-05-seller-tips-credits-vs-price-cut"; B = os.path.dirname(os.path.abspath(__file__)); D = os.environ.get("OUT_DIR") or os.path.dirname(B)
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
X = {k: dict(css_4x5=STRONG, css_1x1=STRONG, css_9x16=TALL) for k in (3, 4, 5, 6, 7, 8, 9)}
for k in (3, 6, 8, 9): F[k]['xy_9x16'] = (.95, .5)
SL = [
 sa.cover("gen-01.jpg", "CREDITS VS. A", "price cut", "Practical advice for<br><b>SELLERS.</b>", **P, **F[1], **X.get(1, {})),
 sa.stats("Charlotte metro|October 2026",
          [("MEDIAN<br>LIST PRICE", "$419,900", "−4.1% YoY"), ("ACTIVE<br>LISTINGS", "11,547", "+13.2% YoY"),
           ("MEDIAN DAYS<br>ON MARKET", "65", "+11.1% YoY"), ("PRICE-REDUCED<br>SHARE", "27.1%", "+0.0 pts YoY")],
          "More listings and more price cuts. Know how a credit compares to cutting the list price.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, October 2026"),
 sa.edu("gen-03.jpg", "A credit is|not a cut.", "A seller credit helps with the buyer's closing costs. A price cut changes the purchase price itself.",
        ["Credit = help at closing", "Cut = lower sale price", "They change different lines", "Ask which one you mean"], **P, **F[3], **X.get(3, {})),
 sa.edu("gen-04.jpg", "Run both|net sheets.", "I recommend comparing your estimated net with a credit and with a price cut before you choose.",
        ["Start from the offer price", "Add the credit amount", "Compare a lower price", "Look at your net, not the sticker"], **P, **F[4], **X.get(4, {})),
 sa.edu("gen-05.jpg", "Lender caps|apply.", "Loan programs limit how much a seller can contribute. The buyer's lender sets the ceiling.",
        ["Ask the buyer's lender", "Caps vary by loan type", "Unused credit can be lost", "Get the limit in writing"], **P, **F[5], **X.get(5, {})),
 sa.edu("gen-06.jpg", "Put it in|writing.", "In NC and SC, changes to an offer need a signed written agreement. Verbal deals don't close the gap.",
        ["Use the right addendum", "Name the dollar amount", "Say what it pays toward", "Sign before you rely on it"], **P, **F[6], **X.get(6, {})),
 sa.edu("gen-07.jpg", "Appraisal|still matters.", "A price cut can change what the appraiser sees. A credit usually does not change the contract price.",
        ["Price cuts affect comps", "Credits stay off the price", "Ask how your lender treats it", "Plan for either path"], **P, **F[7], **X.get(7, {})),
 sa.edu("gen-08.jpg", "Timing and|optics.", "Sometimes a credit keeps your list history cleaner. Sometimes a cut brings more showings. Context decides.",
        ["Look at days on market", "Weigh showings vs. net", "Match the buyer's need", "Don't guess—compare"], **P, **F[8], **X.get(8, {})),
 sa.edu("gen-09.jpg", "My|recommendation.", "Before you answer a credit request, compare both nets, check lender limits, and put the choice in writing.",
        ["Compare both nets", "Confirm lender caps", "Choose credit or cut", "Sign the change"], **P, **F[9], **X.get(9, {})),
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
        print(fmt, len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="seller", fmt=fmt)))
    for p in glob.glob(os.path.join(D, "*.pdf")): os.remove(p); print("removed PDF (no-PDF rule)", p)
