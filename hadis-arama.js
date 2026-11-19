/* el-Mihrâb hadis araması — ayrı iş parçacığında (Web Worker) çalışır; ana ekran donmaz.
   Gelen: {q:[kelimeler], arap:bool, kitaplar:[{k,u}], sinir}
   Giden: {tur:'ilerle',k,i,n} · {tur:'sonuc',k,r:[[ref,metin],...]} · {tur:'bitti',n} */
var DUR=false;
function getir(u,dene){return fetch(u).then(function(r){if(!r.ok)throw new Error(r.status);return r.json()}).catch(function(e){if((dene||0)<1)return getir(u,1);throw e})}
self.onmessage=function(e){var d=e.data;if(d.tur==='dur'){DUR=true;return}
  DUR=false;var W=d.q,arap=d.arap,L=d.kitaplar,sinir=d.sinir||1500,top=0,i=0;
  function es(t){if(!t)return false;for(var j=0;j<W.length;j++)if(t.indexOf(W[j])<0)return false;return true}
  function sonraki(){if(DUR)return;if(i>=L.length||top>=sinir){self.postMessage({tur:'bitti',n:top});return}
    var b=L[i++];self.postMessage({tur:'ilerle',k:b.k,i:i,n:L.length});
    getir(b.u).then(function(D){if(DUR)return;var R=[];
      for(var j=0;j<D.length&&top<sinir;j++){var r=D[j],t=arap?r[1]:r[2];if(es(t)){var p=t.indexOf(W[0]),s=Math.max(0,p-70);R.push([r[0],(s?'…':'')+t.slice(s,p+170)+(p+170<t.length?'…':'')]);top++;
          if(R.length>=40){self.postMessage({tur:'sonuc',k:b.k,r:R});R=[]}}}
      if(R.length)self.postMessage({tur:'sonuc',k:b.k,r:R});D=null;setTimeout(sonraki,0)})
    .catch(function(){self.postMessage({tur:'hata',k:b.k});setTimeout(sonraki,0)})}
  sonraki()};
