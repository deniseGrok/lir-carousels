"""Photo-history registry for Denise's carousels.
Registry: TEMPLATES/photo-registry.csv (one row per photo use: carousel, slide, source id/URL, perceptual hashes).
Usage:
  python3 photo_registry.py backfill            # rebuild registry from every carousel folder (local + repo + git history)
  python3 photo_registry.py check IMG [IMG...]  # check candidate photos (originals or 1080x1350 crops) against the registry
  python3 photo_registry.py add CAROUSEL        # append a finished carousel's build/img photos (+ CREDITS ids)
Rule (CAROUSEL_STANDARD.md, PHOTO REGISTRY): every build checks new photos here, never reuses one, and appends its own.
"""
import csv, hashlib, io, os, re, subprocess, sys
from PIL import Image, ImageOps, ImageStat
import imagehash
C = "/workspace/lir-ai-team/content-research/carousels"; REPO = "/workspace/repos/lir-carousels"
REG = C + "/TEMPLATES/photo-registry.csv"
COLS = ["carousel","slide","kind","provider","source_id","source_url","photographer","file","sha1","phash","dhash","zone_phash","zone_dhash","added","notes"]
SKIP_DIRS = ("raw", "cand", "process", "__pycache__", ".git", "TEMPLATES")
UNS = re.compile(r"(?:photo-)?(\d{10,13}-[0-9a-f]{12})"); PEX = re.compile(r"pexels(?:\.com/photos?/(?:[a-z0-9-]*-)?|-photo-|[-_ ]|: ?)(\d{5,9})")
WM = re.compile(r"File:([^,|()\n]+?\.(?:jpe?g|png|tif))", re.I)
# Unsplash ids that share an upload-timestamp prefix are usually the same photographer session/series
def series_key(sid):
    m = re.match(r"(\d{10,13})-", sid or ""); return m.group(1)[:8] if m else ""

def norm45(im):
    im = ImageOps.exif_transpose(im).convert("RGB"); w, h = im.size; t = 1080/1350
    if w/h > t: nw = int(h*t); l = (w-nw)//2; im = im.crop((l,0,l+nw,h))
    else: nh = int(w/t); tp = (h-nh)//2; im = im.crop((0,tp,w,tp+nh))
    return im.resize((1080,1350), Image.LANCZOS)
def zone(im45): return im45.crop((0,130,1080,640))   # the clean photo zone in every theme (below the tag, above the text)
def hashes(im, kind):
    im = ImageOps.exif_transpose(im).convert("RGB")
    is_slide = kind == "slide_render" or im.size == (1080,1350)
    z = zone(im.resize((1080,1350), Image.LANCZOS) if is_slide else norm45(im))
    if sum(ImageStat.Stat(z.convert("L")).stddev) < 12: return None   # flat page (stats slide with no photo)
    return dict(phash=str(imagehash.phash(im)), dhash=str(imagehash.dhash(im)), zone_phash=str(imagehash.phash(z)), zone_dhash=str(imagehash.dhash(z)))
def ids_in(text):
    out = []
    for m in UNS.finditer(text): out.append(("unsplash", m.group(1), f"https://unsplash.com/photos/{m.group(1)}"))
    for m in PEX.finditer(text): out.append(("pexels", m.group(1), f"https://www.pexels.com/photo/{m.group(1)}/"))
    for m in WM.finditer(text): f = m.group(1).strip(); out.append(("wikimedia", f, "https://commons.wikimedia.org/wiki/File:" + f.replace(" ","_")))
    return out
def slide_ids(folder):
    """{slide: (provider,id,url,photographer)} from CREDITS / prep scripts / md lists in a carousel folder."""
    m = {}
    for root, ds, fs in os.walk(folder):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            if not (f.startswith("CREDITS") or f.endswith((".md",".py"))): continue
            for line in open(os.path.join(root,f), errors="ignore"):
                # "01 | url", "1. id (...)", "01 photo-id · 02 photo-id", '"01":("id"'
                for sm in re.finditer(r'(?:^|[\s"·{,])(\d{1,2})(?:\s*\||\.\s|\s+(?=photo-)|"\s*:\s*\(")\s*"?([^·\n]*)', line):
                    n = int(sm.group(1)); found = ids_in(sm.group(2)[:400])
                    if 1 <= n <= 10 and found and n not in m:
                        ph = re.search(r"\b(?:by|\()\s*([A-Z][a-z]+ [A-Z][a-zA-Z]+)", sm.group(2)); m[n] = found[0] + ((ph.group(1) if ph else ""),)
    return m
def all_ids(folder):
    s = set()
    for root, ds, fs in os.walk(folder):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            if f.startswith("CREDITS") or f.endswith((".md",".py",".txt")): s.update(ids_in(open(os.path.join(root,f), errors="ignore").read()))
    return s
def kind_of(rel):
    b = os.path.basename(rel)
    if re.fullmatch(r"slide-\d\d\.png", b): return "slide_render"
    if "/src/" in "/"+rel: return "src_original"
    if re.search(r"/img(-hq)?(/builder)?/[^/]+\.jpe?g$", "/"+rel): return "photo"
    return None
def slide_no(rel):
    m = re.search(r"(?:slide-|/)(\d\d)(?:[-_.])", "/"+os.path.basename(rel) if "src" not in rel else "x"); return int(m.group(1)) if m else ""

def backfill(today_skip=None):
    rows, seen = [], set()
    def add(carousel, rel, data, origin):
        k = kind_of(rel)
        if not k: return
        sha = hashlib.sha1(data).hexdigest()
        if (carousel, sha) in seen: return
        seen.add((carousel, sha))
        try: im = Image.open(io.BytesIO(data))
        except Exception: return
        h = hashes(im, k)
        if not h: return
        n = slide_no(rel); sid = SID.get(carousel, {}).get(n) if n else None
        if k == "src_original":
            fid = ids_in(os.path.basename(rel).replace("p","pexels-",1) if re.fullmatch(r"p\d+\.jpe?g", os.path.basename(rel)) else os.path.basename(rel))
            if os.path.basename(rel).startswith("wm-"): fid = [("wikimedia", os.path.basename(rel)[3:], "")]
            sid = fid[0] + ("",) if fid else None
        sid = sid or ("", "", "", "")
        rows.append(dict(carousel=carousel, slide=n, kind=k, provider=sid[0], source_id=sid[1], source_url=sid[2], photographer=sid[3],
                         file=rel, sha1=sha, added="backfill 2026-10-19", notes=origin, **h))
    folders = sorted(set(os.listdir(C)) | set(os.listdir(REPO)))
    SID = {}
    for f in folders:
        for base in (C, REPO):
            p = os.path.join(base, f)
            if os.path.isdir(p) and f not in SKIP_DIRS and not f.startswith("."):
                d = slide_ids(p); [SID.setdefault(f, {}).setdefault(k, v) for k, v in d.items()]
    for f in folders:
        if f == today_skip or f in SKIP_DIRS or f.startswith("."): continue
        for base, origin in ((C, "local"), (REPO, "repo HEAD")):
            p = os.path.join(base, f)
            if not os.path.isdir(p): continue
            for root, ds, fs in os.walk(p):
                ds[:] = [d for d in ds if d not in SKIP_DIRS and d not in ("cand",)]
                for fn in sorted(fs):
                    full = os.path.join(root, fn); rel = os.path.relpath(full, base)
                    if kind_of(rel): add(rel.split("/")[0], rel, open(full,"rb").read(), origin)
    # every earlier version in git history (slides and build photos that were later replaced)
    log = subprocess.run(["git","-C",REPO,"log","--all","--format=@%H","--name-only","--diff-filter=AM"], capture_output=True, text=True).stdout
    h = None
    for line in log.splitlines():
        if line.startswith("@"): h = line[1:]; continue
        rel = line.strip()
        if not rel or not kind_of(rel) or rel.split("/")[0] == today_skip: continue
        data = subprocess.run(["git","-C",REPO,"show",f"{h}:{rel}"], capture_output=True).stdout
        if data: add(rel.split("/")[0], rel, data, "git " + h[:7])
    # source ids named in a carousel's notes but not tied to a hashed file
    have = {(r["carousel"], r["source_id"]) for r in rows}
    for f in folders:
        if f == today_skip or f in SKIP_DIRS or f.startswith("."): continue
        ids = set()
        for base in (C, REPO):
            if os.path.isdir(os.path.join(base,f)): ids |= all_ids(os.path.join(base,f))
        for prov, sid, url in sorted(ids):
            if (f, sid) not in have:
                rows.append(dict(carousel=f, slide=next((k for k,v in SID.get(f,{}).items() if v[1]==sid), ""), kind="source_id_only", provider=prov, source_id=sid, source_url=url,
                                 photographer="", file="", sha1="", phash="", dhash="", zone_phash="", zone_dhash="", added="backfill 2026-10-19",
                                 notes="id named in the carousel's notes/scripts (may be a rejected candidate)")); have.add((f, sid))
    return rows
def load():
    return list(csv.DictReader(open(REG))) if os.path.exists(REG) else []
def save(rows):
    w = csv.DictWriter(open(REG,"w",newline=""), fieldnames=COLS); w.writeheader(); [w.writerow({k: r.get(k,"") for k in COLS}) for r in rows]
def check(path, rows=None, src_id="", thr_zone=22, thr_full=20):
    """Returns matches [(score, row, why)] for a candidate photo. Loose thresholds; inspect hits visually."""
    rows = rows if rows is not None else load(); im = Image.open(path); h = hashes(im, "photo"); hits = []
    H = lambda s: imagehash.hex_to_hash(s)
    for r in rows:
        why = []
        if src_id and r["source_id"] == src_id: why.append("same source id")
        if src_id and series_key(src_id) and series_key(r["source_id"]) == series_key(src_id): why.append(f"same Unsplash upload series {series_key(src_id)}")
        if r["zone_phash"]:
            dz = min(H(h["zone_phash"]) - H(r["zone_phash"]), H(h["zone_dhash"]) - H(r["zone_dhash"]))
            df = min(H(h["phash"]) - H(r["phash"]), H(h["dhash"]) - H(r["dhash"]))
            if dz <= thr_zone: why.append(f"zone hash dist {dz}")
            if df <= thr_full: why.append(f"full hash dist {df}")
            score = min(dz, df)
        else: score = 99
        if why: hits.append((score if score < 99 else 0, r, "; ".join(why)))
    return sorted(hits, key=lambda x: x[0])
def add(carousel, note="", date=None):
    """Append a finished carousel's photos: build/img/NN.jpg (+ final slide PNG and the src original) with source ids from CREDITS.txt."""
    import datetime
    date = date or datetime.date.today().isoformat()
    rows = load(); have = {(r["carousel"], r["sha1"]) for r in rows}; d = os.path.join(C, carousel); new = []
    ids = {}
    cp = os.path.join(d, "build/img/CREDITS.txt")
    if os.path.exists(cp):
        for line in open(cp):
            m = re.match(r"(\d\d)\s*\|", line)
            if m and ids_in(line): ids[int(m.group(1))] = ids_in(line)[0]
    pmap = {}
    pp = os.path.join(d, "build/prep_photos.py")
    if os.path.exists(pp):
        for m in re.finditer(r'"(\d\d)":\("([^"]+)"', open(pp).read()): pmap[m.group(2)] = int(m.group(1))
    for n, (prov, sid, url) in sorted(ids.items()):
        files = [(f"build/img/{n:02d}.jpg", "photo"), (f"slide-{n:02d}.png", "slide_render")]
        for f in os.listdir(os.path.join(d, "build/src")) if os.path.isdir(os.path.join(d, "build/src")) else []:
            if pmap.get(f.rsplit(".",1)[0]) == n: files.append((f"build/src/{f}", "src_original"))
        for rel, kind in files:
            fp = os.path.join(d, rel)
            if not os.path.exists(fp): continue
            data = open(fp, "rb").read(); sha = hashlib.sha1(data).hexdigest()
            if (carousel, sha) in have: continue
            h = hashes(Image.open(fp), kind)
            if not h: continue
            new.append(dict(carousel=carousel, slide=n, kind=kind, provider=prov, source_id=sid, source_url=url, photographer="",
                            file=f"{carousel}/{rel}", sha1=sha, added=date, notes=note, **h)); have.add((carousel, sha))
    save(rows + new); return new

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "backfill":
        rows = backfill(sys.argv[2] if len(sys.argv) > 2 else None); save(rows); print(len(rows), "rows ->", REG)
    elif cmd == "check":
        rows = load()
        for p in sys.argv[2:]:
            hits = check(p, rows); print(p, "OK (no match)" if not hits else f"{len(hits)} possible match(es)")
            for s, r, why in hits[:8]: print("   ", s, r["carousel"], r["slide"], r["kind"], r["source_id"], r["file"], "|", why)
    elif cmd == "add":
        new = add(sys.argv[2], " ".join(sys.argv[3:])); print(len(new), "rows added ->", REG)

def open_row(r):
    """Open the image a registry row points at (local folder, repo HEAD, or the git commit in notes)."""
    for base in (C, REPO):
        p = os.path.join(base, r["file"])
        if os.path.exists(p) and hashlib.sha1(open(p,"rb").read()).hexdigest() == r["sha1"]: return Image.open(p)
    m = re.match(r"git (\w+)", r["notes"])
    if m: return Image.open(io.BytesIO(subprocess.run(["git","-C",REPO,"show",f"{m.group(1)}:{r['file']}"],capture_output=True).stdout))
    for base in (C, REPO):
        p = os.path.join(base, r["file"])
        if os.path.exists(p): return Image.open(p)
