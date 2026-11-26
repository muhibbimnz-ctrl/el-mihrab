/* Kadem ve YDS Arapça paket anahtarları (tools/kadem/sifre.py ile aynı kural).
   localStorage "kadem.anahtar"   : ana anahtar (Max üyeliği ya da şifre) — alt anahtarlar bundan türetilir
   localStorage "kadem.anahtarlar": {mbsts, yds} — Pro üyeliklerde yalnız alınan paketin anahtarı
   alt(p) = HMAC-SHA256(ana, 'kadem:'+p) */
(function(){
  var AK = 'kadem.anahtar', AL = 'kadem.anahtarlar', K = null;
  function b64(s){ var b = atob(s), u = new Uint8Array(b.length); for(var i = 0; i < b.length; i++) u[i] = b.charCodeAt(i); return u }
  function b64e(u){ var s = ''; u = new Uint8Array(u); for(var i = 0; i < u.length; i++) s += String.fromCharCode(u[i]); return btoa(s) }
  function oku(k){ try{ return localStorage.getItem(k) }catch(x){ return null } }
  function aes(bits){ return crypto.subtle.importKey('raw', bits, 'AES-GCM', false, ['decrypt']) }
  function alt(ana, p){
    return crypto.subtle.importKey('raw', ana, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign'])
      .then(function(h){ return crypto.subtle.sign('HMAC', h, new TextEncoder().encode('kadem:' + p)) })
  }
  /* Bu cihazdaki anahtarlar: { ana?, mbsts?, yds? } (CryptoKey) */
  function anahtarlar(){
    if(K) return Promise.resolve(K);
    if(!window.crypto || !crypto.subtle) return Promise.resolve({});
    var a = oku(AK), L = {}; try{ L = JSON.parse(oku(AL) || '{}') || {} }catch(x){}
    var R = {};
    var is = a ? Promise.all([aes(b64(a)), alt(b64(a), 'mbsts').then(aes), alt(b64(a), 'yds').then(aes)]).then(function(k){ R.ana = k[0]; R.mbsts = k[1]; R.yds = k[2] })
               : Promise.all(['mbsts', 'yds'].filter(function(p){ return L[p] }).map(function(p){ return aes(b64(L[p])).then(function(k){ R[p] = k }) }));
    return is.then(function(){ return K = R }, function(){ return K = {} });
  }
  function var_(p){ var a = oku(AK); if(a) return true; if(!p) return !!oku(AL); try{ return !!(JSON.parse(oku(AL) || '{}') || {})[p] }catch(x){ return false } }
  /* Şifreli metni eldeki anahtarlarla dener. Hata: 'yok' (hiç anahtar yok), 'kilit' (bu içerik alınan pakette değil), 'sifre' (ana anahtar yanlış) */
  function coz(txt, tek){
    var u = b64(txt.trim());
    return (tek ? Promise.resolve({ x: tek }) : anahtarlar()).then(function(R){
      var L = Object.keys(R).map(function(k){ return R[k] });
      if(!L.length) throw 'yok';
      var i = 0;
      function dene(){
        if(i >= L.length) throw (R.ana ? 'sifre' : 'kilit');
        return crypto.subtle.decrypt({ name: 'AES-GCM', iv: u.slice(0, 12) }, L[i++], u.slice(12)).then(null, dene);
      }
      return dene();
    }).then(function(b){ return JSON.parse(new TextDecoder().decode(b)) });
  }
  function kaydet(ana, paketler){
    try{
      if(ana){ localStorage.setItem(AK, b64e(ana)); localStorage.removeItem(AL) }
      else{ localStorage.removeItem(AK); localStorage.setItem(AL, JSON.stringify(paketler || {})) }
    }catch(x){}
    K = null;
  }
  function sil(){ try{ localStorage.removeItem(AK); localStorage.removeItem(AL); localStorage.removeItem('kadem.kaynak') }catch(x){} K = null }
  window.Kilit = { anahtarlar: anahtarlar, coz: coz, var: var_, kaydet: kaydet, sil: sil, alt: alt, aes: aes, b64: b64, b64e: b64e };
})();
