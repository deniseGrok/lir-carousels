# Buyer tips Oct 31 2026: "Know what you're really buying" (title, survey, easements, HOA covenants). 10 slides.
# REDESIGN Oct 31 2026 (Denise): "Buyer & Seller Tips — Signature Authority" template -> TEMPLATES/signature_authority.py (spec: TEMPLATES/SIGNATURE_AUTHORITY.md).
# Renders slide-NN.png 1080x1350 (4:5, IG + LinkedIn) + PDF + slides.zip; slides-1x1/ 1080x1080 (Facebook) + slides-1x1.zip;
# slides-9x16/ 1080x1920 (TikTok, Denise asked for it Oct 31 2026) + slides-9x16.zip. Copy and sources unchanged from the 3f73a85/8c2cb28 draft (see ../*.md).
import sys, os
sys.path.insert(0, "/workspace/repos/lir-carousels/TEMPLATES")
import signature_authority as sa
N = "2026-10-31-buyer-tips-title-and-survey"; B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B)
CONTACT = dict(name="Denise Wilson", title="BROKER/REALTOR®", firm="Lifestyle International Realty — Carolinas",
               phone="704-615-7347", web="denisewilson.lircarolinas.com")
SL = [
 sa.cover("photo-1647579350413-a6ada4e480ed.jpg", "Know what|you're", "really buying",
          "Practical advice for <b>BUYERS</b>", kicker="TITLE · SURVEY · EASEMENTS · HOA",
          pre=(0, 600, 4330, 3464), focus={"4x5": (.45, .5), "1x1": (.5, .5), "9x16": (.42, .5)}),
 sa.stats("photo-1784810801262-d0d27227a480.jpg", "Charlotte metro, [[September 2026.]]",
          [("MEDIAN<br>LIST PRICE", "$424,950", "−3.1% YoY"), ("PRICE PER<br>SQ FT", "$217", "−1.4% YoY"),
           ("NEW<br>LISTINGS", "3,742", "−7.5% YoY"), ("PENDING<br>LISTINGS", "4,681", "−5.9% YoY")],
          "Whatever the price, check the title and boundaries before you close.",
          "Source: Realtor.com Economic Research, Charlotte-Concord-Gastonia, NC-SC metro, September 2026", xy=(.75, .5)),
 sa.edu("p4500474.jpg", "Title means [[ownership.]]",
        "At closing, the deed shows the seller transferred ownership, or \"title,\" to you.",
        ["Old claims can surface later, like unpaid taxes or unpaid contractors",
         "A title search reviews the public records before you close",
         "Title insurance can cover certain claims from before your purchase"]),
 sa.edu("p6283960.jpg", "Lender's policy [[vs. owner's.]]", "Two title policies, two different jobs.",
        ["Most lenders require a lender's title policy",
         "It protects the lender's loan, not your equity",
         "An owner's policy is optional and can help protect your investment"]),
 sa.edu("p6782369.jpg", "You can [[shop for title.]]", "Title services can usually be shopped, so compare before you choose.",
        ["Look at section C, page 2 of your Loan Estimate",
         "Your lender must give you a list of local providers",
         "Buying both policies from one provider usually costs less in total"], xy=(1.0, .5)),
 sa.edu("p7914572.jpg", "Know where [[the lines are.]]", "A survey shows what you're buying on the ground, not just on paper.",
        ["A survey can show boundaries, easements and setbacks",
         "NC's standard offer form lists a survey as a due diligence item",
         "Order it early so results arrive before your deadline"], xy=(.5, .3), lift=1.08),
 sa.edu("p10099333.jpg", "Read the [[land questions.]]", "The seller's disclosure can flag issues on or around the property.",
        ["NC's REC 4.22 asks about easements, shared driveways and encroachments",
         "It also asks about private roads and liens that could affect title",
         "SC's disclosure covers restrictive covenants and encroachments too"]),
 sa.edu("p8082229.jpg", "Read the [[HOA rules.]]", "Covenants and HOA documents can shape how you use the home and lot.",
        ["Covenants can set mandatory rules for the lot or home",
         "NC's standard offer form recommends reviewing covenants, bylaws and rules",
         "Ask if the association charges fees for documents"]),
 sa.edu("p3701434.jpg", "Ask questions|[[before you sign.]]", "Your closing attorney can explain what the title search found.",
        ["Ask your closing attorney to walk you through the title results",
         "Ask what any listed exceptions mean for the home",
         "Compare the survey with what you saw on your tour"]),
 sa.cta("photo-1722247482035-73d55ee3d258.jpg", "Let's [[talk.]]", "Buying in NC or SC?",
        "I recommend reviewing the title search, the survey and any HOA documents during due diligence. For legal questions about title, talk with a real estate attorney.",
        CONTACT, tag="LET'S TALK", xy=(.62, .5)),
]
if __name__ == "__main__":
    out = sa.build(SL, D, B, f"{N}-DRAFT.pdf", series="buyer", formats=("4x5", "1x1", "9x16"))
    print({k: len(v) for k, v in out.items()})
