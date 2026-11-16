# Dil sayfalarına (arapca/ingilizce/farsca) program kartları, sade üst çubuk ve sade kontrolleri
# STATİK olarak işler: ilk boyamada doğru ekran görünür, sonradan değişmez (titreme/donma hissi yok).
import re,json
CFG={
'arapca':('Modern Arapça','#0f5d4a',{'basic':['🔤','Temel Arapça','Elifba ve ilk adımlar'],'book':['📖','Hikâye Programı','182 gün · B1–B2'],'pod':['🎧','Podcast','60 bölüm · A1→C2'],'daily':['🗣️','Günlük Hayat','60 metin'],'acad':['🎓','Akademik Metinler','40 metin'],'islam':['🕌','İslami İlimler','40 metin'],'adv':['🏛️','C1–C2 Metinler','40 metin'],'prac':['🔁','Kelime Tekrarı','Öğrendiklerini pekiştir']}),
'ingilizce':('İngilizce','#2d4166',{'basic':['🔤','Temel İngilizce','Alfabe ve ilk adımlar'],'book':['📖','Kitap Programı','182 gün'],'pod':['🎧','Podcast','60 bölüm · A1→C2'],'daily':['🗣️','Günlük Hayat','60 metin'],'acad':['🎓','Akademik Metinler','40 metin'],'islam':['🕌','İslami İlimler','40 metin'],'prac':['🔁','Kelime Tekrarı','Öğrendiklerini pekiştir']}),
'farsca':('Farsça','#55324a',{'basic':['🔤','Temel Farsça','Elifba ve ilk adımlar'],'book':['📖','Hikâye Programı','182 gün · B1–B2'],'pod':['🎧','Podcast','60 bölüm · A1→C2'],'adv':['📚','Seviye Metinleri','80 metin · B1–C2'],'daily':['🗣️','Günlük Hayat','60 diyalog'],'acad':['🎓','Akademik Metinler','40 metin'],'islam':['🕌','İslami İlimler','40 metin'],'prac':['🔁','Kelime Tekrarı','Öğrendiklerini pekiştir']})}
def css(R):
  return ("#mihrabBk,#mihrabHead,main>h1{display:none!important}"
  "body{padding-top:calc(54px + env(safe-area-inset-top,0px))!important}"
  "#mdBar{position:fixed;left:0;right:0;top:0;z-index:60;display:flex;align-items:center;gap:10px;padding:calc(8px + env(safe-area-inset-top,0px)) 12px 8px;background:"+R+";color:#fff;font:700 17px system-ui,sans-serif;box-shadow:0 2px 10px rgba(0,0,0,.2)}"
  "#mdBar a,#mdBar button{color:#fff;text-decoration:none;background:rgba(255,255,255,.2);padding:7px 12px;border-radius:12px;font:600 15px system-ui,sans-serif;border:0;min-height:0}"
  "#mdBar span{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}"
  "html.mdLanding #mdPr{display:none}"
  "html.mdLanding main>*:not(#modes):not(#mdHero){display:none!important}"
  "#mdHero{display:none}html.mdLanding #mdHero{display:block;margin:6px 2px 14px}"
  "#mdHero h2{margin:0 0 4px;font:800 22px system-ui,sans-serif;color:"+R+"}#mdHero p{margin:0;color:#667;font:15px/1.5 system-ui,sans-serif}"
  "html.mdLanding #modes{display:grid!important;grid-template-columns:1fr 1fr;gap:12px}"
  "html.mdLanding #modes .mode{display:flex;flex-direction:column;align-items:flex-start;gap:4px;min-height:118px;padding:14px;margin:0;border-radius:18px;border:0;text-align:left;color:#fff;font:800 16px/1.25 system-ui,sans-serif;box-shadow:0 6px 16px rgba(0,0,0,.12);background:linear-gradient(135deg,var(--c1),var(--c2))}"
  "#modes .mode .mi{font-size:30px;line-height:1}#modes .mode small{font:600 12.5px/1.35 system-ui,sans-serif;opacity:.92}"
  "#modes .mode[data-m=basic]{--c1:#0f766e;--c2:#14b8a6}#modes .mode[data-m=book]{--c1:#1d4ed8;--c2:#3b82f6}#modes .mode[data-m=pod]{--c1:#7c3aed;--c2:#a78bfa}#modes .mode[data-m=daily]{--c1:#c2410c;--c2:#fb923c}#modes .mode[data-m=acad]{--c1:#0369a1;--c2:#38bdf8}#modes .mode[data-m=islam]{--c1:#0f5d4a;--c2:#22a07c}#modes .mode[data-m=adv]{--c1:#9f1239;--c2:#f43f5e}#modes .mode[data-m=prac]{--c1:#a16207;--c2:#eab308}"
  "html:not(.mdLanding) #modes{display:flex!important;flex-wrap:nowrap;overflow-x:auto;gap:6px;padding:4px 0 8px;scrollbar-width:none;-webkit-overflow-scrolling:touch}html:not(.mdLanding) #modes::-webkit-scrollbar{display:none}"
  "html:not(.mdLanding) #modes .mode{flex:none;white-space:nowrap;padding:7px 12px;border-radius:999px;font-size:13.5px;min-height:0;margin:0}"
  "html:not(.mdLanding) #modes .mode small,html:not(.mdLanding) #modes .mode .mi{display:none}"
  "html:not(.mdLanding) #modes .mode[aria-pressed=true]{background:"+R+";color:#fff;border-color:"+R+"}"
  ".bar{position:static!important;display:flex!important;flex-wrap:wrap!important;gap:6px!important;align-items:center;padding:6px 0!important;font-size:12.5px!important}"
  ".bar label,.bar span{font-size:12.5px!important;white-space:nowrap}.bar select{font-size:12.5px!important;padding:5px 6px!important;min-height:0!important;height:auto!important;max-width:130px}"
  ".bar button{font-size:12.5px!important;padding:6px 10px!important;min-height:0!important;white-space:nowrap}"
  ".wks{display:flex!important;flex-wrap:nowrap!important;overflow-x:auto;gap:6px;padding-bottom:4px;scrollbar-width:none;-webkit-overflow-scrolling:touch}.wks::-webkit-scrollbar{display:none}.wks>*{flex:none}"
  ".wks .tab{padding:5px 9px!important;font-size:13px!important;min-height:0!important;margin:0!important}.wks .tab[disabled]{opacity:.45}.wks .mon{align-self:center;font-size:12px}"
  ".days{display:flex!important;flex-wrap:wrap!important;gap:6px;margin-top:8px}.days .tab{margin:0!important;font-size:14px!important;padding:7px 11px!important}"
  ".days .tab[data-les]{flex:1 1 100%;text-align:left;white-space:normal;line-height:1.35}"
  "#modes .mlink{text-decoration:none}html:not(.mdLanding) #modes .mlink{display:none!important}"
  "html.mdLanding #modes .mlink{display:flex;flex-direction:column;align-items:flex-start;gap:4px;min-height:118px;padding:14px;border-radius:18px;color:#fff;font:800 16px/1.25 system-ui,sans-serif;box-shadow:0 6px 16px rgba(0,0,0,.12);background:linear-gradient(135deg,var(--c1),var(--c2))}"
  "#modes .mlink.big{grid-column:1/-1;min-height:96px}#modes .mlink .mi{font-size:30px;line-height:1}#modes .mlink small{font:600 12.5px/1.35 system-ui,sans-serif;opacity:.92}"
  "#modes .ml-metin{--c1:#7c2d12;--c2:#d97706}#modes .ml-diyalog{--c1:#155e75;--c2:#0891b2}#modes .ml-kelime{--c1:#4d7c0f;--c2:#84cc16}")
for f,(ad,R,I) in CFG.items():
  s=open(f+'.html',encoding='utf-8').read()
  # 1) eski, sonradan çalışan enjeksiyonları sök
  s=re.sub(r'<script>\(function\(\)\{if\(/medrese=1/\.test\(location\.search\)\)\{var mst=.*?\}\)\(\);</script>','',s,flags=re.S)
  s=re.sub(r'<script>\(function\(\)\{var mst=document\.createElement\("style"\);.*?\}\)\(\);</script>','',s,flags=re.S)
  s=re.sub(r'<style id="dilCss">.*?</style><script id="dilEarly">.*?</script>','',s,flags=re.S)
  s=re.sub(r'<div id="mdBar">.*?</div>','',s,flags=re.S); s=re.sub(r'<div id="mdHero">.*?</div>','',s,flags=re.S)
  s=re.sub(r'<script id="dilLate">.*?</script>','',s,flags=re.S)
  assert 'var mst' not in s and 'mdBar' not in s, f
  # 2) head: stil + erken sınıf (ilk boyamadan önce)
  early='<style id="dilCss">'+css(R)+'</style><script id="dilEarly">document.documentElement.classList.add("mdLanding")</script>'
  assert s.count('</style></head>')==1; s=s.replace('</style></head>','</style>'+early+'</head>')
  # 3) üst çubuk ve başlık statik
  bar='<div id="mdBar"><a id="mdGeri" href="./">‹ el-Mihrâb</a><span>'+ad+'</span><button id="mdPr" type="button">Programlar</button></div>'
  assert s.count('<body><main>')==1; s=s.replace('<body><main>','<body>'+bar+'<main>')
  hero='<div id="mdHero"><h2>'+ad+'</h2><p>Bir program seç; dersler seslendirilir, Türkçesi bir dokunuşla açılır.</p></div>'
  m=re.search(r'<div class="modes" id="modes">(.*?)</div>',s,flags=re.S); assert m
  LINKS=('<a class="mlink big ml-metin" href="medrese.html#/modern/metinler"><span class="mi">📰</span>Okuma Metinleri (Makaleler)<small>120 makale · 12 konu · çeviri, sözlük ve sorular</small></a>'
         '<a class="mlink ml-diyalog" href="medrese.html#/modern/diyaloglar"><span class="mi">💬</span>Diyaloglar<small>Günlük konuşmalar</small></a>'
         '<a class="mlink ml-kelime" href="medrese.html#/modern/kelimeler"><span class="mi">🗂️</span>Kelime Temaları<small>Haber, ekonomi, bilim…</small></a>') if f=='arapca' else ''
  btn=LINKS+''.join('<button class="mode" data-m="'+k+'"><span class="mi">'+v[0]+'</span>'+v[1]+'<small>'+v[2]+'</small></button>\n' for k,v in I.items() if 'data-m="'+k+'"' in m.group(1))
  assert btn.count('data-m=')==m.group(1).count('data-m='),f
  if f!='arapca': assert 'mlink' not in m.group(1)
  s=s[:m.start()]+hero+'<div class="modes" id="modes">\n'+btn+'</div>'+s[m.end():]
  # 4) geç bağlanan küçük davranış (kart tıklanınca derse geç, Programlar'a dön)
  late=('<script id="dilLate">(function(){var H=document.documentElement,m=document.getElementById("modes"),g=document.getElementById("mdGeri");'
   'try{if(/medrese=1/.test(location.search)){g.href="medrese.html";g.textContent="‹ Medrese"}}catch(e){}'
   'if(m)m.addEventListener("click",function(e){if(e.target.closest(".mode")){H.classList.remove("mdLanding");try{scrollTo(0,0)}catch(x){}}});'
   'try{var C=window.COL,M={daily:"d",acad:"a",islam:"i",adv:"c",pod:"p"};if(C)Object.keys(M).forEach(function(k){var c=C[M[k]],b=m&&m.querySelector(".mode[data-m="+k+"] small");if(c&&c.arr&&b)b.textContent=c.arr.length+(k==="pod"?" bölüm":" metin")+" hazır"})}catch(e){}'
   'var p=document.getElementById("mdPr");if(p)p.onclick=function(){try{if(window.speechSynthesis)speechSynthesis.cancel();var st=document.getElementById("stop");if(st)st.click()}catch(e){}H.classList.add("mdLanding");try{scrollTo(0,0)}catch(x){}}})();</script>')
  i=s.rfind('</body>'); s=s[:i]+late+s[i:]
  s=s.replace('</style><<link','</style><link')
  open(f+'.html','w',encoding='utf-8').write(s); print('ok',f,len(s))
