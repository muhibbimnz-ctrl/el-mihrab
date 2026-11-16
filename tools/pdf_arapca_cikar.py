import pdfplumber,sys,unicodedata,re
def isMark(c): return len(c)==1 and unicodedata.category(c)=='Mn'
def page_lines(page):
    chs=[c for c in page.chars if c['text'].strip() and not ('‪'<=c['text']<='‮')]
    base=[c for c in chs if not isMark(c['text'])]
    for c in base:
        w=c['x1']-c['x0']
        if c['text']=='ل' and (7.45<=w<=7.6 or 8.3<=w<=8.8): c['text']='لا'
        elif c['text']=='ل' and 9.0<=w<=9.4: c['text']='ل§'
    marks=[c for c in chs if isMark(c['text'])]
    # group base chars into lines by vertical center
    base.sort(key=lambda c:(c['top']+c['bottom'])/2)
    lines=[]
    for c in base:
        y=(c['top']+c['bottom'])/2
        if lines and abs(lines[-1]['y']-y)<6: lines[-1]['c'].append(c); lines[-1]['y']=(lines[-1]['y']*len(lines[-1]['c'])+y)/(len(lines[-1]['c'])+1)
        else: lines.append({'y':y,'c':[c]})
    import unicodedata as U
    letters=[c for L in lines for c in L['c'] if '\u0621'<=c['text'][0]<='\u064A']
    for m in marks:
        mx=(m['x0']+m['x1'])/2; my=(m['top']+m['bottom'])/2
        cand=[]
        for L in lines:
            if abs(L['y']-my)>14: continue
            for c in L['c']:
                if not ('\u0621'<=c['text'][0]<='\u064A'): continue
                d=abs((c['x0']+c['x1'])/2-mx)+(0 if c['x0']-0.5<=mx<=c['x1']+0.5 else 4)
                cand.append((d,id(c),c))
        cand.sort(key=lambda t:t[0])
        isv=m['text']!='\u0651' and m['text']!='\u0670'
        for d,_,c in cand[:3]:
            ms=c.setdefault('m',[])
            if isv and any(x not in '\u0651\u0670' for x in ms): continue
            if not isv and m['text'] in ms: continue
            ms.append(m['text']);break
        else:
            if cand: cand[0][2].setdefault('m',[]).append(m['text'])
    out=[]
    for L in lines:
        cs=sorted(L['c'],key=lambda c:-c['x0'])
        s='';prev=None
        for c in cs:
            if prev is not None and prev['x0']-c['x1']>2.0: s+=' '
            s+=c['text']+''.join(sorted(set(c.get('m',[])),key=lambda k:k!='ّ'))
            prev=c
        def allah(m):
            mk=m.group(1); v='ُ' if 'ُ' in mk else ('ِ' if 'ِ' in mk else 'َ')
            return 'للّٰه'+v
        s=re.sub(r'ل§([\u064B-\u0652\u0670]*)',allah,s)
        if re.fullmatch(r'[\d\s٠-٩.]+',s): continue
        out.append((L['y'],s))
    return out
pdf=pdfplumber.open(sys.argv[1])
for p in range(int(sys.argv[2]),int(sys.argv[3])+1):
    print(f'### {p}')
    for y,s in page_lines(pdf.pages[p-1]): print(s)
