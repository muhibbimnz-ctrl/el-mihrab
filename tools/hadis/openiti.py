# OpenITI mARkdown metnini numaralı hadislere böler (ahsanz89/Islamic openiti-parse.mjs'in Python uyarlaması, MIT)
import re
D={c:str(i) for i,c in enumerate('٠١٢٣٤٥٦٧٨٩')}
def toint(s): return int(''.join(D.get(c,c) for c in s))
def clean(s):
    s=re.sub(r'PageV\d+P\d+',' ',s);s=re.sub(r'\bms\d+\b',' ',s);s=re.sub(r'\bAUTO\b',' ',s)
    s=re.sub(r'\(¬?[0-9٠-٩]{1,3}\)',' ',s);s=re.sub(r'«[0-9٠-٩]{1,3}»',' ',s);s=re.sub(r'[|#~]+',' ',s)
    return re.sub(r'\s+',' ',s).strip()
NUM=re.compile(r'^\s*[\[(]?\s*([0-9٠-٩]{1,5})\s*[\])]?\s*(?:[-–ـ]\s*|\s+(?=[؀-ۿ]))')
HNUM=re.compile(r'^\s*\[?\s*([0-9٠-٩]{1,5})\s*\]?\s*[-–ـ]\s*')
def parse(raw,minrun=20):
    body=raw.split('#META#Header#End#')[-1];paras=[]
    for line in body.splitlines():
        if line.startswith('~~'):
            if paras: paras[-1][1]+=' '+line[2:]
            continue
        if line.startswith('### '): paras.append(['h',re.sub(r'^###\s*\|*','',line)])
        elif line.startswith('# '): paras.append(['p',line[2:]])
    c=[]
    for i,(k,t) in enumerate(paras):
        t=re.sub(r'^\s*\|+\s*','',t);m=(HNUM if k=='h' else NUM).match(t)
        if m: c.append((i,toint(m.group(1)),t[m.end():]))
        elif k=='h' and re.match(r'^\s*[\[(]?\s*[0-9٠-٩]{1,5}\s*[\])]?\s*$',t): c.append((i,toint(t.strip(' []()')),''))
    runs=[];cur=[]
    for x in c:
        if cur and cur[-1][1]<x[1]<=cur[-1][1]+60: cur.append(x)
        else:
            if cur: runs.append(cur)
            cur=[x]
    if cur: runs.append(cur)
    keep={x[0]:x for r in runs if len(r)>=minrun for x in r}
    out=[];ch='';curh=None
    for i,(k,t) in enumerate(paras):
        if i in keep:
            curh={'p':keep[i][1],'ch':ch,'t':clean(keep[i][2]),'fn':False};out.append(curh);continue
        if k=='h':
            h=clean(t)
            if h and not re.match(r'^[0-9٠-٩\s\-–]+$',h): ch=h[:200]
            continue
        if curh:
            if re.match(r'^_{5,}',t): curh['fn']=True;continue
            tt=clean(t)
            if not curh['fn'] and tt: curh['t']+=' '+tt
    return [dict(p=h['p'],ch=h['ch'],t=h['t']) for h in out if len(h['t'])>15]
