/* Fetva asistanı — Cloudflare Pages Function (POST /api/fetva).
   Soru ve uygulamanın telefonda bulduğu en yakın mesele kimlikleri gelir; meseleler sitenin kendi
   data/fikih/meseleler.json dosyasından okunur ve Cloudflare Workers AI modeline yalnız bunlara dayanarak
   cevap vermesi söylenir. Ücretsiz kullanım için Pages projesinde "AI" adlı Workers AI bağlantısı gerekir
   (Settings → Bindings → Add → Workers AI → Variable name: AI). Bağlantı yoksa 503 döner ve uygulama
   cevabı telefonda kendisi kurar. */
const MODEL = '@cf/meta/llama-3.3-70b-instruct-fp8-fast';
const MZ = [['maliki', 'Mâlikî'], ['safii', 'Şâfiî'], ['hanbeli', 'Hanbelî']];
let MS = null, AD = null;

const SISTEM = `Sen el-Mihrâb uygulamasının "Fetva Sor" asistanısın. Kullanıcıların dinî sorularını Türkçe, saygılı, sade ve sıcak bir dille cevaplarsın.
KURALLAR:
1. Yalnızca aşağıda "MESELELER" başlığı altında verilen bilgilere dayan. Orada olmayan hüküm, sayı, delil, hadis veya âyet uydurma.
2. Merkez mezhep Hanefîdir: önce Hanefî hükmünü açıkça söyle, gerekiyorsa diğer mezheplerin görüşünü kısaca ekle.
3. Verilen meseleler soruyu karşılamıyorsa bunu dürüstçe söyle, bildiğin kadarıyla yakın meseleyi belirt ve kişiyi müftülüğe veya Diyanet'in ALO 190 hattına yönlendir.
4. Cevabın sonunda dayandığın meselelerin başlıklarını "Kaynak:" diye yaz.
5. Dinî olmayan, siyasi tartışma isteyen veya zarar verici sorulara girme; kibarca bu asistanın ilmihal ve fıkıh soruları için olduğunu söyle.
6. Kişinin özel durumu (hastalık, yolculuk, âdet hâli vb.) hükmü değiştirebiliyorsa bunu belirt.
7. 120-220 kelimeyi geçme. Madde işareti yerine kısa paragraflar kullan; önemli hükmü **kalın** yaz.`;

function mesele(m) {
  const mez = MZ.map(([k, ad]) => `${ad}: ${m.mez[k][0]}${m.mez[k][1] ? ' — ' + m.mez[k][1] : ''}`).join('\n');
  const del = (m.delil || []).slice(0, 2).map(d => `${d[0] === 'ayet' ? 'Âyet' : 'Hadis'} (${d[1]}): ${String(d[3] || '').slice(0, 300)}`).join('\n');
  return `### ${m.baslik} (${m.yol.join(' › ')})\nHanefî: ${m.hanefi}\n${m.sebep ? 'Gerekçe: ' + m.sebep + '\n' : ''}${mez}\n${del}`;
}
function adim(a) { return `### ${a.baslik} (adım adım, Hanefî)\n${a.giris}\n${a.adim.map((s, i) => `${i + 1}. ${s[0]}${s[1] ? ' (' + s[1] + ')' : ''}`).join('\n')}`; }

function cevap(o, durum) { return new Response(JSON.stringify(o), { status: durum || 200, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' } }); }

export async function onRequestPost({ request, env }) {
  if (!env.AI) return cevap({ hata: 'ai-yok' }, 503);
  let g; try { g = await request.json(); } catch (e) { return cevap({ hata: 'istek' }, 400); }
  const soru = String(g.soru || '').trim().slice(0, 600);
  if (soru.length < 3) return cevap({ hata: 'bos' }, 400);
  try {
    if (!MS) {
      const u = new URL(request.url);
      const [a, b] = await Promise.all([env.ASSETS.fetch(new URL('/data/fikih/meseleler.json', u)), env.ASSETS.fetch(new URL('/data/fikih/adim.json', u))]);
      MS = await a.json(); AD = b.ok ? await b.json() : [];
    }
  } catch (e) { return cevap({ hata: 'veri' }, 500); }
  const ids = (Array.isArray(g.ids) ? g.ids : []).slice(0, 5).map(String);
  const bagl = ids.map(id => { const m = MS.find(x => x.id === id); if (m) return mesele(m); const a = AD.find(x => x.id === id); return a ? adim(a) : null; }).filter(Boolean);
  const gecmis = (Array.isArray(g.gecmis) ? g.gecmis : []).slice(-4).map(x => ({ role: x.r === 'a' ? 'assistant' : 'user', content: String(x.t || '').slice(0, 900) }));
  const messages = [
    { role: 'system', content: SISTEM + '\n\nMESELELER:\n' + (bagl.length ? bagl.join('\n\n') : '(Bu soruya uyan mesele bulunamadı.)') },
    ...gecmis,
    { role: 'user', content: soru }
  ];
  try {
    const r = await env.AI.run(MODEL, { messages, max_tokens: 700, temperature: 0.2 });
    const t = (r && (r.response || r.result && r.result.response) || '').trim();
    if (!t) return cevap({ hata: 'model' }, 502);
    return cevap({ cevap: t, model: MODEL });
  } catch (e) { return cevap({ hata: 'model', ayrinti: String(e).slice(0, 200) }, 502); }
}
export async function onRequestGet({ env }) { return cevap({ hazir: !!env.AI }); }
