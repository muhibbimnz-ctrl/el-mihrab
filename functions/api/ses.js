/* Farsça sesli okuma — Cloudflare Pages Function (GET /api/ses?t=metin&v=f|m).
   iPhone ve birçok telefonda Farsça (fa-IR) cihaz sesi yoktur; uygulama bu durumda sesi buradan alır.
   Ses, Microsoft'un Edge "Sesli oku" hizmetindeki Farsça sinir ağı sesleriyle üretilir (Dilara: kadın, Farid: erkek).
   İki yol denenir: 1) Microsoft Translator uygulamasının jeton yolu (düz HTTPS), 2) Edge'in WebSocket yolu.
   Üretilen her ses Cloudflare önbelleğinde saklanır; aynı cümle ikinci kez Microsoft'a gitmez.
   Bunlar resmî olmayan uç noktalardır; Microsoft değiştirirse 502 döner ve uygulama cihaz sesine geri düşer. */
const SES = { f: 'fa-IR-DilaraNeural', m: 'fa-IR-FaridNeural' };
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0';
const BICIM = 'audio-24khz-48kbitrate-mono-mp3';
const EN_COK = 600;
let JETON = null;

function hata(kod, d) { return new Response(JSON.stringify({ hata: kod }), { status: d, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } }); }
function kacis(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;'); }
function uuid() { return crypto.randomUUID().replace(/-/g, ''); }
function ssml(metin, ses) {
  return `<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="fa-IR"><voice name="${ses}"><prosody rate="+0%" pitch="+0Hz" volume="+0%">${kacis(metin)}</prosody></voice></speak>`;
}
function b64(buf) { let s = ''; const u = new Uint8Array(buf); for (let i = 0; i < u.length; i++) s += String.fromCharCode(u[i]); return btoa(s); }

/* 1. yol: Translator jetonu → {bölge}.tts.speech.microsoft.com */
async function imza(url) {
  const adres = encodeURIComponent(url.split('://')[1]);
  const id = uuid();
  const tarih = new Date().toUTCString().replace(/GMT/, '').trim().toLowerCase() + ' gmt';
  const metin = ('MSTranslatorAndroidApp' + adres + tarih + id).toLowerCase();
  const ham = Uint8Array.from(atob('oik6PdDdMnOXemTbwvMn9de/h9lFnfBaCWbGMMZqqoSaQaqUOqjVGm5NqsmjcBI1x+sS9ugjB55HEJWRiFXYFw=='), c => c.charCodeAt(0));
  const k = await crypto.subtle.importKey('raw', ham, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', k, new TextEncoder().encode(metin));
  return `MSTranslatorAndroidApp::${b64(sig)}::${tarih}::${id}`;
}
async function jeton() {
  if (JETON && JETON.son > Date.now() / 1000 + 180) return JETON;
  const url = 'https://dev.microsofttranslator.com/apps/endpoint?api-version=1.0';
  const r = await fetch(url, { method: 'POST', headers: {
    'Accept-Language': 'en-US', 'X-ClientVersion': '4.0.530a 5fe1dc6c', 'X-UserId': '0f04d16a175c411e',
    'X-HomeGeographicRegion': 'en-US', 'X-ClientTraceId': uuid(), 'X-MT-Signature': await imza(url),
    'User-Agent': UA, 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '0' } });
  if (!r.ok) throw new Error('jeton ' + r.status);
  const j = await r.json();
  let son = Date.now() / 1000 + 540;
  try { son = JSON.parse(atob(j.t.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'))).exp || son; } catch (e) {}
  return (JETON = { t: j.t, r: j.r, son });
}
async function yol1(metin, ses) {
  const j = await jeton();
  const r = await fetch(`https://${j.r}.tts.speech.microsoft.com/cognitiveservices/v1`, { method: 'POST', headers: {
    Authorization: j.t, 'Content-Type': 'application/ssml+xml', 'User-Agent': UA, 'X-Microsoft-OutputFormat': BICIM }, body: ssml(metin, ses) });
  if (!r.ok) { if (r.status === 401) JETON = null; throw new Error('tts ' + r.status); }
  const b = await r.arrayBuffer();
  if (b.byteLength < 500) throw new Error('kısa');
  return b;
}

/* 2. yol: Edge "Sesli oku" WebSocket */
const TOKEN = '6A5AA1D4EAFF4E9FB37E23D68491D6F4';
async function gec() {
  let t = BigInt(Math.floor(Date.now() / 1000)) + 11644473600n;
  t -= t % 300n; t *= 10000000n;
  const h = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t.toString() + TOKEN));
  return [...new Uint8Array(h)].map(x => x.toString(16).padStart(2, '0')).join('').toUpperCase();
}
function zaman() { return new Date().toUTCString().replace('GMT', 'GMT+0000 (Coordinated Universal Time)'); }
async function yol2(metin, ses) {
  const url = `https://speech.platform.bing.com/consumer/speech/synthesize/readaloud/edge/v1?TrustedClientToken=${TOKEN}&ConnectionId=${uuid()}&Sec-MS-GEC=${await gec()}&Sec-MS-GEC-Version=1-143.0.3650.75`;
  const muid = [...crypto.getRandomValues(new Uint8Array(16))].map(x => x.toString(16).padStart(2, '0')).join('').toUpperCase();
  const r = await fetch(url, { headers: { Upgrade: 'websocket', Origin: 'chrome-extension://jdiccldimpdaibmpdkjnbmckianbfold',
    'User-Agent': UA, Pragma: 'no-cache', 'Cache-Control': 'no-cache', 'Accept-Language': 'en-US,en;q=0.9', Cookie: 'muid=' + muid + ';' } });
  const ws = r.webSocket;
  if (!ws) throw new Error('ws ' + r.status);
  ws.accept();
  const parca = [];
  const bitti = new Promise((ok, red) => {
    const sure = setTimeout(() => { try { ws.close(); } catch (e) {} red(new Error('süre')); }, 20000);
    ws.addEventListener('message', ev => {
      const d = ev.data;
      if (typeof d === 'string') { if (d.includes('Path:turn.end')) { clearTimeout(sure); try { ws.close(); } catch (e) {} ok(); } return; }
      const u = new Uint8Array(d), n = (u[0] << 8) | u[1];
      const bas = new TextDecoder().decode(u.subarray(2, 2 + n));
      if (bas.includes('Path:audio')) parca.push(u.subarray(2 + n));
    });
    ws.addEventListener('close', () => { clearTimeout(sure); ok(); });
    ws.addEventListener('error', () => { clearTimeout(sure); red(new Error('ws hata')); });
  });
  ws.send(`X-Timestamp:${zaman()}\r\nContent-Type:application/json; charset=utf-8\r\nPath:speech.config\r\n\r\n` +
    `{"context":{"synthesis":{"audio":{"metadataoptions":{"sentenceBoundaryEnabled":"false","wordBoundaryEnabled":"false"},"outputFormat":"${BICIM}"}}}}\r\n`);
  ws.send(`X-RequestId:${uuid()}\r\nContent-Type:application/ssml+xml\r\nX-Timestamp:${zaman()}Z\r\nPath:ssml\r\n\r\n` + ssml(metin, ses));
  await bitti;
  const top = parca.reduce((a, p) => a + p.length, 0);
  if (top < 500) throw new Error('ses yok');
  const out = new Uint8Array(top); let o = 0;
  for (const p of parca) { out.set(p, o); o += p.length; }
  return out.buffer;
}

export async function onRequestGet({ request, waitUntil }) {
  const u = new URL(request.url);
  const metin = (u.searchParams.get('t') || '').replace(/\s+/g, ' ').trim();
  const ses = SES[u.searchParams.get('v')] || SES.f;
  if (!metin) return hata('bos', 400);
  if (metin.length > EN_COK) return hata('uzun', 413);
  const anahtar = new Request(`${u.origin}/api/ses?v=${ses === SES.m ? 'm' : 'f'}&t=${encodeURIComponent(metin)}`);
  const onb = caches.default;
  const eski = await onb.match(anahtar);
  if (eski) return eski;
  let ses_ = null;
  for (const yol of [yol1, yol2]) { try { ses_ = await yol(metin, ses); break; } catch (e) { console.log('ses', yol.name, String(e)); } }
  if (!ses_) return hata('uretilemedi', 502);
  const cevap = new Response(ses_, { headers: { 'Content-Type': 'audio/mpeg', 'Cache-Control': 'public, max-age=31536000, immutable', 'Access-Control-Allow-Origin': '*' } });
  waitUntil(onb.put(anahtar, cevap.clone()));
  return cevap;
}
