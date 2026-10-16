import re,html,sys
KW=r'(incentive|closing cost|buydown|buy-down|\d\.\d\d?%|price reduc|savings|save|flex|design|credit|expire|through|by \d+/\d+|October|Oct\.?|contract|\$\d)'
for f in sys.argv[1:]:
    t=open(f,errors='ignore').read()
    og=re.findall(r'property="og:image"\s+content="([^"]+)',t)+re.findall(r'content="([^"]+)"\s+property="og:image',t)+re.findall(r'name="og:image"\s+content="([^"]+)',t)
    t=re.sub(r'<script.*?</script>|<style.*?</style>|<noscript.*?</noscript>','',t,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    print('=====',f,len(t),'OG:',og[:2])
    seen=0
    for m in re.finditer(r'[^.]{0,220}'+KW+r'[^.]{0,260}',t,flags=re.I):
        print('-',m.group(0).strip()[:480]); seen+=1
        if seen>=int(sys.argv[0:1] and 18): break
