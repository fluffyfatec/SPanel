def auto_save():
    import asyncio # pip install asyncio
    import os
    from playwright.async_api import async_playwright # pip install --upgrade pip, pip install playwright, playwright install
    import zipfile 


    # Link do site
    site_covid = 'https://www.saopaulo.sp.gov.br/planosp/simi/dados-abertos/'
    site_seade = 'https://www.seade.gov.br/coronavirus/#'
    clicar_botao = '//html/body/section[4]/div/div/article[1]/div/ul/li[1]/div/a/span[1]'
    clicar_botao_vac = '//html/body/section[4]/div/div/article[14]/h3'
    botao_vac_cvs = '//html/body/section[4]/div/div/article[14]/div/ul/li/div/a/span[1]'
    clicar_botao_leit = '//html/body/div[1]/div[1]/a[3]'

    # PLaywright para acesso do COVID.CSV 
    async def baixar_covid():
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
                await download.save_as('docs/df_state.csv')
                print(download.url, path)
                await page.close()
                await browser.close()          

    asyncio.run(baixar_covid())

    # PLaywright para acesso do VACINAS.CSV
    async def baixar_vacina():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page(accept_downloads = True)
            await page.goto(site_covid)
            await page.click(clicar_botao_vac)
            await page.click(botao_vac_cvs)
            
            # Baixar arquivo
            async with page.expect_download() as download_info:
                download = await download_info.value
                path = await download.path()
                await download.save_as('docs/vacinas.csv')
                print(download.url, path)
                await page.close()
                await browser.close()            

    asyncio.run(baixar_vacina())

        # PLaywright para acesso dos LEITOS.CSV
    async def baixar_leito():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page(accept_downloads = True)
            await page.goto(site_seade)
            await page.click(clicar_botao_leit)
            
            # Baixar arquivo
            async with page.expect_download() as download_info:
                download = await download_info.value
                path = await download.path()
                await download.save_as('docs/df_regiao.zip')
                print(download.url, path)
                await page.close()
                await browser.close() 



    asyncio.run(baixar_leito())

    
    def descompacta ():
        zip_ref = zipfile.ZipFile('docs/df_regiao.zip', 'r')
        info = zip_ref.infolist()[0]
        name_arq = str(info.filename)
        print(name_arq)
        zip_ref.extractall('docs')
        os.rename(f'docs/{name_arq}', 'docs/df_regiao.csv')
        os.remove(f'docs/df_regiao.zip')
        
        zip_ref.close()
  

    descompacta()


    

auto_save()
