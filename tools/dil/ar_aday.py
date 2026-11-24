import re
PR=['وال','فال','بال','كال','لل','ال','وب','ول','فب','فل','وك','فك','وس','فس','و','ف','ب','ل','ك','س']
SF=['تموها','تموه','تما','هما','كما','تم','تن','هم','هن','ها','كم','كن','نا','ني','ون','ين','ات','ان','وا','ه','ك','ي','ت','ن','ة','ا']
OZEL={'ابا':'اب','ابي':'اب','ابو':'اب','اخا':'اخ','اخي':'اخ','اخو':'اخ','ذي':'ذو','ذا':'ذو','فا':'فو'}
def cand(n):
    out=[]
    def add(x):
        if x and len(x)>=2 and x not in out:out.append(x)
    bases=[n]
    for p in PR:
        if n.startswith(p) and len(n)-len(p)>=2:
            r=n[len(p):];bases.append(r)
            if r.startswith('ال') and len(r)>4:bases.append(r[2:])
    for b in bases:
        add(b);add('ال'+b) if not b.startswith('ال') else None
    stems=[]
    for b in bases:
        t=b[2:] if b.startswith('ال') and len(b)>4 else b
        stems.append(t)
        lv=[t]
        for _ in range(2):
            nx=[]
            for u in lv:
                for s in SF:
                    if u.endswith(s) and len(u)-len(s)>=2:
                        st=u[:-len(s)];nx.append(st)
                        if st.endswith('ت'):stems.append(st[:-1]+'ة')
                        if st[-1:] in 'ئؤ':stems.append(st[:-1]+'ء')
                        if st.endswith('و') and len(st)>=4:stems.append(st[:-1])
                        if st.endswith('ا') and len(st)>=3:stems.append(st[:-1]+'ى')
            stems+=nx;lv=nx
    v=[]
    for s in stems:
        v.append(s)
        if len(s)>=4 and s[0] in 'يتناأإ':
            v.append(s[1:])
            if s[1:].startswith('ست') and len(s)>=6:v.append('ا'+s[1:])
        if len(s)==3 and s[0] in 'يتنأ':
            r=s[1:];v+=[r+'ى',r+'ا',r[0]+'ا'+r[1],r+r[1]]
        if len(s)==2:v+= [s+'ى',s+'ا',s+'ي',s[0]+'ا'+s[1]]
    for s in v:
        add(s);add('ال'+s);add(s+'ة')
        if s in OZEL:add(OZEL[s])
    if n in OZEL:out.insert(0,OZEL[n])
    return out
