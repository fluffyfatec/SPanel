import asyncio # pip install asyncio
from playwright.async_api import async_playwright # pip install --upgrade pip, pip install playwright, playwright install

# Link do site
site_covid = 'https://www.saopaulo.sp.gov.br/planosp/simi/dados-abertos/'
clicar_botao = '//html/body/section[4]/div/div/article[1]/div/ul/li[1]/div/a/span[1]'

# PLaywright para acesso do CSV
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(accept_downloads = True)
        await page.goto(site_covid)
        await page.click('h3')
        await page.click(clicar_botao)
        
        # Baixar arquivo
        async with page.expect_download() as download_info:
            download = await download_info.value
            path = await download.path()
            await download.save_as('./docs/df_state.csv')
            print(download.url, path)
            await page.close()
            await browser.close()

asyncio.run(main())



