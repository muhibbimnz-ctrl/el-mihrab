/* Google girişini el-mihrab.com üzerinden geçirir (Firebase "kendi alan adında oturum" yöntemi).
   /__/auth/* istekleri Firebase'in el-mihrab.firebaseapp.com adresine aktarılır; böylece Google ekranında
   "el-mihrab.com" görünür ve yönlendirmeli giriş tarayıcıların üçüncü taraf depolama kısıtlarına takılmaz. */
export async function onRequest({ request }) {
  const u = new URL(request.url);
  const hedef = 'https://el-mihrab.firebaseapp.com' + u.pathname + u.search;
  const r = await fetch(hedef, { method: request.method, headers: request.headers, body: ['GET', 'HEAD'].includes(request.method) ? undefined : request.body, redirect: 'manual' });
  return new Response(r.body, { status: r.status, statusText: r.statusText, headers: r.headers });
}
