/* Hız ölçümü: her sayfayı 4 kat yavaşlatılmış işlemciyle açar.
   Kullanım: python3 -m http.server 8123 & ; node tools/hiz/olc.mjs [sayfa…]
   Çıktı: açılış (load) süresi, toplam bloklama (50 ms üstü uzun görevlerin fazlası), en uzun görev, indirilen veri, DOM düğüm sayısı. */
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const SAY = process.argv.slice(2).length ? process.argv.slice(2) : ['index.html','index.html#okuma','index.html#2-255','index.html#namaz','hadis.html','fikih.html','fikih.html?ilmihal','akaid.html','ahlak.html','siyer.html','arapca.html','farsca.html','ingilizce.html','medrese.html','elifba.html','roman.html','sozluk.html','ihtisas.html','kadem.html','kadem.html#s=mbsts','cocuk.html','soru.html','hac.html','kible.html','kaza.html','ozel.html','hatim.html','haber.html','zikir.html','delail.html'];
const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome', args: ['--no-sandbox'] });
const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
await c.addInitScript(() => { try { ['app','hadis','fikih','akaid','ahlak','siyer','arapca','farsca','ingilizce','medrese','elifba','roman','ihtisas','kadem','kuran'].forEach(x => localStorage.setItem('mihrab.nasil.' + x, '1')); localStorage.setItem('mihrab.tanitim','1'); } catch (e) {}
  window.__lt = []; new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lt.push([Math.round(e.startTime), Math.round(e.duration)]); }).observe({ type: 'longtask', buffered: true }); });
await c.route(/^https?:\/\/(?!localhost)/, r => r.abort());
const p = await c.newPage(); const cdp = await c.newCDPSession(p); await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
const hata = []; p.on('pageerror', e => hata.push(p.url().split('/').pop() + ': ' + e.message.slice(0, 120)));
console.log('sayfa'.padEnd(24), 'açılış', 'blok(ms)', 'en uzun', 'veri(KB)', 'DOM');
for (const s of SAY) {
  await p.goto('about:blank'); const t = Date.now();
  try { await p.goto('http://localhost:8123/' + s, { waitUntil: 'load', timeout: 60000 }); } catch (e) { console.log(s, 'AÇILMADI'); continue; }
  const ac = Date.now() - t; await p.waitForTimeout(5000);
  const r = await p.evaluate(() => ({ lt: window.__lt || [], kb: Math.round(performance.getEntriesByType('resource').reduce((a, x) => a + (x.transferSize || x.encodedBodySize || 0), 0) / 1024), dom: document.getElementsByTagName('*').length,
    buyuk: performance.getEntriesByType('resource').filter(x => (x.transferSize || x.encodedBodySize) > 150000).map(x => x.name.split('/').slice(-2).join('/').split('?')[0] + ':' + Math.round((x.transferSize || x.encodedBodySize) / 1024) + 'k') }));
  const blok = r.lt.reduce((a, x) => a + Math.max(0, x[1] - 50), 0), uz = r.lt.reduce((a, x) => Math.max(a, x[1]), 0);
  console.log(s.padEnd(24), String(ac).padStart(6), String(blok).padStart(8), String(uz).padStart(7), String(r.kb).padStart(8), String(r.dom).padStart(5), r.buyuk.join(' '));
}
if (hata.length) console.log('HATALAR:\n' + hata.join('\n'));
await b.close();
