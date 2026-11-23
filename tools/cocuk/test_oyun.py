# Çocuk Köşesi büyük oyunlar + İhtisas liste duman testi (sunucusuz)
import asyncio, os, mimetypes
from playwright.async_api import async_playwright
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
async def ver(route):
    yol = os.path.join(K, route.request.url.split('app.test/', 1)[1].split('#')[0].split('?')[0])
    if os.path.isfile(yol): await route.fulfill(path=yol, content_type=mimetypes.guess_type(yol)[0] or 'application/octet-stream')
    else: await route.fulfill(status=404, body='')
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 400, 'height': 860})
        await pg.route('http://app.test/**', ver); await pg.route(lambda u: 'app.test' not in u, lambda r: r.abort())
        err = []; pg.on('pageerror', lambda e: err.append(str(e)))
        await pg.goto('http://app.test/ihtisas.html'); await pg.wait_for_timeout(600)
        print('ihtisas kartlar', await pg.evaluate("[...document.querySelectorAll('.alan b')].map(x=>x.textContent).join(' | ')"), 'kutu:', await pg.evaluate("!!document.querySelector('.kutu')"))
        await pg.screenshot(path='/tmp/ih_list.png', full_page=True)
        await pg.goto('http://app.test/ihtisas.html#hadis/sah'); await pg.wait_for_timeout(500)
        print('kaynak notu', (await pg.evaluate("document.querySelectorAll('.not')[0].innerText"))[:90])
        await pg.goto('http://app.test/cocuk.html#oyunlar'); await pg.wait_for_timeout(700)
        await pg.screenshot(path='/tmp/oyunlar.png')
        await pg.goto('http://app.test/cocuk.html#oyun/balon'); await pg.wait_for_timeout(500)
        await pg.click('[data-s="0"]'); await pg.wait_for_timeout(2500); print('hash', await pg.evaluate('location.hash'))
        print('balon sayısı', await pg.evaluate("document.querySelectorAll('.hb-b').length"), await pg.evaluate("document.getElementById('hn').textContent"))
        await pg.screenshot(path='/tmp/balon.png')
        # hedef balonları vur
        for _ in range(90):
            await pg.evaluate("""(()=>{const h=document.getElementById('hh');if(!h)return;[...document.querySelectorAll('.hb-b:not(.pat)')].filter(b=>b.querySelector('span').textContent===h.textContent).forEach(b=>b.click())})()""")
            await pg.wait_for_timeout(500)
            if await pg.evaluate("!!document.querySelector('.score')"): break
        print('balon sonuç', await pg.evaluate("document.querySelector('.score')&&document.querySelector('.score').textContent"))
        await pg.goto('http://app.test/cocuk.html#oyun/yolculuk'); await pg.wait_for_timeout(500)
        await pg.screenshot(path='/tmp/yol.png')
        for _ in range(6):
            await pg.click('#yk [data-v="1"]'); await pg.wait_for_timeout(200); await pg.click('#yi'); await pg.wait_for_timeout(300)
        print('yolculuk', await pg.evaluate("document.querySelector('.score').textContent"))
        await pg.goto('http://app.test/cocuk.html#oyun/tren'); await pg.wait_for_timeout(400)
        await pg.click('#t2'); await pg.wait_for_timeout(300); print('hash', await pg.evaluate('location.hash'))
        for j in range(8):
            await pg.click(f'#ord [data-j="{j}"]'); await pg.wait_for_timeout(120)
        print('tren', await pg.evaluate("document.querySelector('.score').textContent"))
        await pg.screenshot(path='/tmp/tren.png')
        await pg.goto('http://app.test/cocuk.html#oyun/tren'); await pg.wait_for_timeout(300); await pg.click('#t1'); await pg.wait_for_timeout(300)
        for _ in range(6):
            await pg.evaluate("(()=>{const p=document.querySelector('[data-p]:not(.bitti)');p.click();document.querySelector('[data-k=\"'+p.dataset.p+'\"]').click()})()")
            await pg.wait_for_timeout(150)
        await pg.wait_for_timeout(700)
        print('eşleştir', await pg.evaluate("document.querySelector('.score').textContent"))
        print('HATALAR', err[:5]); await b.close()
asyncio.run(main())
