# İhtisas sayfası duman testi (sunucusuz; dosyalar route ile diskten verilir): python3 tools/ihtisas/test_ui.py
import asyncio, os, mimetypes
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
from playwright.async_api import async_playwright

U = 'http://app.test/ihtisas.html'


async def ver(route):
    yol = os.path.join(K, route.request.url.split('app.test/', 1)[1].split('#')[0].split('?')[0])
    if os.path.isfile(yol):
        await route.fulfill(path=yol, content_type=mimetypes.guess_type(yol)[0] or 'application/octet-stream')
    else:
        await route.fulfill(status=404, body='')


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': 420, 'height': 900})
        await pg.route('http://app.test/**', ver)
        await pg.route(lambda u: 'app.test' not in u, lambda r: r.abort())
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        for alan in ['tefsir', 'fikih', 'hadis', 'akaid', 'belagat', 'mezhepler']:
            r = []
            for sek in ['tas', 'usl', 'sah', 'kut', 'tar', 'ter', 'met']:
                await pg.goto(f'{U}#{alan}/{sek}')
                await pg.wait_for_timeout(400)
                r.append(f"{sek}:{await pg.evaluate('document.querySelector(\"#ic\")?document.querySelector(\"#ic\").innerText.length:-1')}")
            print(alan, ' '.join(r))
        for alan in ['tefsir', 'fikih', 'hadis', 'akaid']:
            await pg.goto(f'{U}#{alan}/usl')
            await pg.wait_for_timeout(400)
            r = []
            for u in ['tas', 'sah', 'met', 'kut', 'tar']:
                await pg.click(f'[data-u="{u}"]')
                await pg.wait_for_timeout(200)
                r.append(f"{u}:{await pg.evaluate('document.querySelector(\"#ui\").innerText.length')}")
            await pg.click('[data-u="tas"]')
            for t in ['tsn', 'eko', 'tab', 'agc']:
                await pg.click(f'#ui [data-t="{t}"]')
                await pg.wait_for_timeout(150)
                r.append(f"tas-{t}:{await pg.evaluate('document.querySelector(\"#ui #ti\").innerText.length')}")
            print('usul', alan, ' '.join(r))
        await pg.goto(f'{U}#hadis/tas')
        await pg.wait_for_timeout(400)
        await pg.click('[data-t="tab"]')
        await pg.wait_for_timeout(300)
        await pg.screenshot(path='/tmp/hadis_tab.png')
        print('HATALAR', errs[:5])
        await b.close()

asyncio.run(main())
