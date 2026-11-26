/* /__/firebase/* (init.json) isteklerini Firebase'e aktarır; giriş sayfası (/__/auth/handler) bu dosyayı okur. */
export async function onRequest({ request }) {
  const u = new URL(request.url);
  const hedef = 'https://el-mihrab.firebaseapp.com' + u.pathname + u.search;
  const r = await fetch(hedef, { method: request.method, headers: request.headers, body: ['GET', 'HEAD'].includes(request.method) ? undefined : request.body, redirect: 'manual' });
  return new Response(r.body, { status: r.status, statusText: r.statusText, headers: r.headers });
}
