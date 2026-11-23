import json,collections,re,unicodedata,sys
sys.path.insert(0,'/home/claude/tools'); from radicals_vi import R,IDC
D='/home/claude/luyen-noi-hsk/data/'; S='/tmp/src/'
H=json.load(open(D+'hanzi.json')); ST=json.load(open(D+'strokes.json')); HSK=json.load(open(D+'hsk.json'))
M={json.loads(l)['character']:json.loads(l) for l in open(S+'mmah/dictionary.txt',encoding='utf-8')}
pa=collections.defaultdict(set)
for l in open(S+'rp/inputs/phienam.txt',encoding='utf-8-sig'):
    if '=' in l: c,v=l.strip().split('=',1); pa[c].add(v.strip().lower())
tc={}; tcd={}
for l in open(S+'rp/inputs/thieuchuu.txt',encoding='utf-8-sig'):
    if '=' in l:
        c,v=l.split('=',1); tc[c]=[x.strip().lower() for x in v.split('[')[0].split(',') if x.strip()]
        m=re.search(r'\\t1\. (.+?)(?:\\n|$)',v) or re.search(r'\]\\n\\t(.+?)(?:\\n|$)',v)
        if m: tcd[c]=re.split(r'(?<=[.;])\s',m.group(1))[0].strip()
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); tone=''.join(ch for ch in s if ch in '\u0300\u0301\u0303\u0309\u0323')
    base=''.join(ch for ch in s if ch not in '\u0300\u0301\u0303\u0309\u0323'); base=unicodedata.normalize('NFC',base)
    base=re.sub(r'y$','i',base); base=base.replace('uy','ui') if base.endswith('uy') else base
    return base+tone
hw={}
for lv,f in [(1,'Elementary'),(2,'Medium'),(3,'Advanced')]:
    for c in set(re.findall(r'[\u4e00-\u9fff]',open(S+f'k3/New HSK (2021)/HSK Handwritten/{f}.txt',encoding='utf-8').read())): hw.setdefault(c,lv)
words=[]; single={}
for G in HSK:
    for L in G['lessons']:
        for it in L['items']:
            words.append((G['lv'],it)); 
            if len(it['hz'])==1: single.setdefault(it['hz'],it)
out={}; nv=collections.Counter()
for c,h in H.items():
    m=M[c]; d=m.get('decomposition') or '？'; idc=d[0] if d[0] in IDC else '？'
    rad=m.get('radical'); rn=R.get(rad)
    refs=set(pa.get(c,set()))|set(tc.get(c,[]))
    hv=h['hv']; ver=[]
    if not refs or not any(norm(x.strip()) in {norm(r) for r in refs} for x in hv.replace('/',',').split(',')): ver.append('hv')
    sw=single.get(c)
    py=sw['py'] if sw else (m.get('pinyin') or [''])[0]
    vi=sw['vi'] if sw else (tcd.get(c) or '')
    if not sw: ver.append('vi')
    if not rn: ver.append('rad')
    ex=[]; lv=9
    for l,it in words:
        if c in it['hz']:
            lv=min(lv,l)
            if len(ex)<4 and it['hz']!=c: ex.append([it['hz'],it['py'],it['vi']])
    e={'py':py,'hv':hv,'vi':vi,'rad':rad,'rn':rn[0] if rn else '','rv':rn[1] if rn else '','idc':idc,'st':IDC[idc],
       'comp':h.get('comp',''),'mn':h.get('mn',''),'n':len(ST[c]['strokes']),'ex':ex,'lv':lv}
    if refs and 'hv' in ver: e['hvRef']='/'.join(sorted(refs))[:40]
    if c in hw: e['hw']=hw[c]
    if ver: e['verify']=ver; nv.update(ver)
    out[c]=e
json.dump(out,open(D+'write.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),nv,collections.Counter(e.get('hw',0) for e in out.values()),collections.Counter(e['lv'] for e in out.values()))
print(out['好'],out['们'],sep='\n')
