# Lisânü'l-Arab (OpenITI) -> kök maddeleri ve şâhid beyitler: /tmp/lisan_beyit.json
import re,json,sys
H=re.compile('[ً-ٰٟـ]')
def n(w):return re.sub('[إأآٱ]','ا',H.sub('',w)).replace('ى','ي').replace('ؤ','و').replace('ئ','ي').replace('ء','')
src=sys.argv[1] if len(sys.argv)>1 else '/tmp/oiti/lisan.txt'
R=[];cur=None
for line in open(src,encoding='utf-8'):
    line=line.rstrip('\n')
    m=re.match(r'^### \$\s*([^:،\s]+)\s*:',line)
    if m:
        cur=[m.group(1).strip(),[]];R.append(cur);continue
    if line.startswith('### '): cur=None;continue
    if cur is None or not line.startswith('# ') or ' ... ' not in line: continue
    v=re.sub(r'«\d+»|PageV\d+P\d+|ms\d+','',line[2:]).strip()
    a,_,b=v.partition(' ... ')
    a=a.strip(' ،,;؛');b=b.strip(' ،,;؛.')
    if len(a)<12 or len(b)<12 or len(a)>70 or len(b)>70 or ' ... ' in b or re.search(r'[A-Za-z0-9]',v): continue
    cur[1].append(a+' ... '+b)
R=[r for r in R if r[1]]
json.dump(R,open('/tmp/lisan_beyit.json','w'),ensure_ascii=False)
print(len(R),'kök',sum(len(r[1]) for r in R),'beyit')
