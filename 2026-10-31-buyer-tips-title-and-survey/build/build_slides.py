# Buyer tips Oct 31 2026: "Know what you're really buying" (title, survey, easements, HOA covenants). 10 slides.
# Signature Authority v2 (Oct 31 2026, Denise's example slides): TEMPLATES/signature_authority.py, spec TEMPLATES/SIGNATURE_AUTHORITY.md.
# Design APPROVED by Denise Oct 31 2026 (4:5 commit 76dd7d3). Builds 4:5 (IG), 1:1 slides-1x1/ (FB Page), 9:16 slides-9x16/ (TikTok).
# Usage: python3 build_slides.py [4x5 1x1 9x16]  (default: all three)
# Facts and sources unchanged (see ../2026-10-31-buyer-tips-title-and-survey.md, sources A-G); bullets tightened to short lines.
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-10-31-buyer-tips-title-and-survey"; B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B)
CONTACT = dict(name="Denise Wilson", title="Broker/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
# Custom photorealistic generated images (Denise approved Oct 31 2026 ~7:05 PM ET), 4x Real-ESRGAN upscaled; gentler grade than stock photos
GEN = dict(expo=1.04, shadows=.12, clarity=14, vib=1.08, warmth=.35, sharp=70, contrast=1.03)
SL = [
 sa.cover("gen-01.jpg", "KNOW WHAT YOU'RE", "really buying", "Practical advice for<br><b>BUYERS.</b>", xy=(.5, .5), crisp=GEN),
 sa.stats("Charlotte metro|September 2026",
          [("MEDIAN<br>LIST PRICE", "$424,950", "−3.1% YoY"), ("PRICE PER<br>SQ FT", "$217", "−1.4% YoY"),
           ("NEW<br>LISTINGS", "3,742", "−7.5% YoY"), ("PENDING<br>LISTINGS", "4,681", "−5.9% YoY")],
          "Whatever the price, check the title and boundaries before you close.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026"),
 sa.edu("gen-03.jpg", "Title means|ownership.",
        "At closing, the deed shows the seller transferred ownership, or \"title,\" to you.",
        ["Old claims can surface later", "Like unpaid taxes or contractors", "Title search: public records",
         "Title insurance can cover them"], xy=(.5, .5), crisp=GEN),
 sa.edu("gen-04.jpg", "Lender's policy|vs. owner's.", "Two policies, two jobs. An owner's policy can help protect your investment.",
        ["Lender's: usually required", "Protects the lender's loan", "Not your equity",
         "Owner's policy is optional"], xy=(.5, .5), crisp=GEN),
 sa.edu("gen-05.jpg", "You can shop|for title.", "Title services can usually be shopped. Start with your Loan Estimate.",
        ["Check section C, page 2", "Ask for the provider list", "Compare more than one",
         "Bundling usually costs less"], xy=(.5, .5), crisp=GEN),
 sa.edu("gen-06.jpg", "Know where|the lines are.", "A survey shows what you're buying on the ground, not just on paper.",
        ["Boundaries and property lines", "Easements and setbacks", "A due diligence item in NC",
         "Order it early"], xy=(.5, .5), crisp=GEN),
 sa.edu("gen-07.jpg", "Read the|land questions.", "NC's disclosure (REC 4.22) asks about issues on or around the property.",
        ["Easements, shared driveways", "Encroachments, private roads", "Liens that could affect title",
         "SC's form covers covenants too"], xy=(.5, .5), crisp=GEN),
 sa.edu("gen-08.jpg", "Read the|HOA rules.", "Covenants and HOA documents can set mandatory rules for the home and lot.",
        ["Restrictive covenants", "Bylaws and rules", "Ask about document fees", "Review during due diligence"], xy=(.5, .5), crisp=GEN),
 sa.edu("gen-09.jpg", "Ask questions|before you sign.", "Your closing attorney can explain what the title search found.",
        ["Review the title results", "Ask what exceptions mean", "Compare survey to your tour",
         "Bring questions early"], xy=(.5, .5), crisp=GEN),
 sa.cta("photo-1722247482035-73d55ee3d258.jpg", CONTACT, xy=(.55, .5), blur=7, grade=dict(bright=1.1, gold=1.2)),
]
if __name__ == "__main__":
    for fmt in (sys.argv[1:] or ["4x5", "1x1", "9x16"]):
        print(fmt, len(sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="buyer", fmt=fmt)))
