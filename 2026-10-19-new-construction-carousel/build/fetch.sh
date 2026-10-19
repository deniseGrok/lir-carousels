#!/bin/bash
# usage: fetch.sh name url  -> raw/name.html (chrome dump-dom), raw/name.txt
cd /workspace/lir-ai-team/content-research/carousels/2026-10-19-new-construction-carousel/raw
timeout ${T:-60} google-chrome --headless=new --user-data-dir=/tmp/chr-$1 --no-sandbox --disable-gpu --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36" --virtual-time-budget=15000 --dump-dom "$2" > "$1.html" 2>/dev/null
python3 - "$1" <<'P'
import re,html,sys
n=sys.argv[1]; t=open(n+'.html',errors='ignore').read()
og=re.findall(r'property="og:image"\s+content="([^"]+)',t)+re.findall(r'content="([^"]+)"\s+property="og:image',t)
ti=re.findall(r'<title[^>]*>(.*?)</title>',t,flags=re.S)
t=re.sub(r'<script.*?</script>|<style.*?</style>|<noscript.*?</noscript>|<svg.*?</svg>','',t,flags=re.S)
t=html.unescape(re.sub(r'<[^>]+>','\n',t)); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(n+'.txt','w').write(t); print(n,'chars',len(t),'title',ti[:1],'og',og[:1])
P
