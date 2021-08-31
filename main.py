# IMPORTAÇÕES
import os
import pandas as pd
from tabulate import tabulate
import schedule
import time


# VARIAVEIS EXT
loop=True

# TELA DE APRESENTAÇÃO
print ('\033[1;31m'+'---COVID-19 - SPanel - Estado de São Paulo---'+'\033[0;0m')

while loop==True:
    #  PUXANDO DADO E TRATANDO DATA E HORA DE PTBR PARA EN
    df_tratado = pd.read_csv("df_tratado.csv")
    df_tratado['datahora'] = pd.to_datetime(df_tratado['datahora'], format='%d/%m/%Y')
    df_tratado = df_tratado.assign(estado='São Paulo')  # nova coluna estado de sp

    # INDICE DOS MUNICIPIOS COM FILTRO DE ERRO
    indice_municipio=input('\033[1m'+'\nÍndice de Municípios'+'\033[0;0m'+'\n1. São Paulo\n2. Guarulhos\n3. Campinas\n4. São Bernardo do Campo\n5. São José dos Campos'
                            +'\n6. Santo André\n7. Ribeirão Preto\n8. Osasco\n9. Sorocaba\n10. Mauá\n11. Estado de São Paulo\n'+'\033[1m'+'Digite o número referente a cidade:\n'+'\033[0;0m')

    # CASO ESCOLHA SÃO PAULO FILTRAR E TABELAR
    if indice_municipio == '1':
        df_tratado = df_tratado.query('nome_munic=="São Paulo" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA','casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)","pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA GUARULHOS FILTRAR E TABELAR
    elif indice_municipio == '2':
        df_tratado = df_tratado.query('nome_munic=="Guarulhos" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA CAMPINAS FILTRAR E TABELAR
    elif indice_municipio == '3':
        df_tratado = df_tratado.query('nome_munic=="Campinas" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA SÃO BERNARDO DO CAMPO FILTRAR E TABELAR
    elif indice_municipio == '4':
        df_tratado = df_tratado.query('nome_munic=="São Bernardo do Campo" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA SÃO JOSÉ DOS CAMPOS FILTRAR E TABELAR
    elif indice_municipio == '5':
        df_tratado = df_tratado.query('nome_munic=="São José dos Campos" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA SANTO ANDRÉ FILTRAR E TABELAR
    elif indice_municipio == '6':
        df_tratado = df_tratado.query('nome_munic=="Santo André" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA RIBEIRÃO PRETO FILTRAR E TABELAR
    elif indice_municipio == '7':
        df_tratado = df_tratado.query('nome_munic=="Ribeirão Preto" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA OSASCO FILTRAR E TABELAR
    elif indice_municipio == '8':
        df_tratado = df_tratado.query('nome_munic=="Osasco" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA SOROCABA FILTRAR E TABELAR
    elif indice_municipio == '9':
        df_tratado = df_tratado.query('nome_munic=="Sorocaba" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    # CASO ESCOLHA MAUÁ FILTRAR E TABELAR
    elif indice_municipio == '10':
        df_tratado = df_tratado.query('nome_munic=="Mauá" & datahora=="2021-08-24"')
        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))
        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS',
                     'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'MUNICIPIO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))

    elif indice_municipio == '11':
        estado = "São Paulo"
        data = '24/08/2021'
        data = pd.to_datetime(data, format='%d/%m/%Y')

        df_tratado = df_tratado[df_tratado['datahora'] == data]
        df_tratado = df_tratado.assign(obitos_novos=df_tratado['obitos_novos'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_tratado = df_tratado.assign(obitos=df_tratado['obitos'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_tratado = df_tratado.assign(casos_novos=df_tratado['casos_novos'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_tratado = df_tratado.assign(casos=df_tratado['casos'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_tratado = df_tratado.assign(pop=df_tratado['pop'].sum())  # SOMAR PARA TRAZER ESTADO DE SP

        df_tratado = df_tratado.assign(LETALIDADE=df_tratado['obitos'] / df_tratado['casos'] * 100)
        decimals = 2
        df_tratado['LETALIDADE'] = df_tratado['LETALIDADE'].apply(lambda x: round(x, decimals))

        df_tratado = df_tratado.query('nome_munic=="São Paulo"')

        df_tratado = df_tratado.drop(columns=['codigo_ibge'])
        df_tratado = df_tratado.rename(
            columns={'nome_munic': 'MUNICIPIO', 'estado': 'ESTADO', 'casos': 'CASOS ACUMULADOS', 'datahora': 'DATA',
                     'casos_novos': 'CASOS NOVOS'
                , 'obitos': "OBITOS ACUMULADOS", "obitos_novos": "OBITOS NOVOS", "LETALIDADE": "LETALIDADE(%)",
                     "pop": "POPULAÇÃO"})
        df_tratado = pd.DataFrame(df_tratado,
                                  columns=['DATA', 'ESTADO', 'CASOS ACUMULADOS', 'CASOS NOVOS', 'OBITOS ACUMULADOS',
                                           'OBITOS NOVOS', 'LETALIDADE(%)', 'POPULAÇÃO'])
        df_tratado = df_tratado.set_index('DATA')
        print(tabulate(df_tratado, headers='keys', tablefmt='psql'))
    # FILTRO DE ERRO DO LOOP DE INDICE
    else:
        print('\033[1m'+'ERRO! Não foi digitado um número correto =('+'\033[0;0m')
        #os.system('cls' if os.name=='nt' else 'clear')
        continue

    # LOOP DE NOVA PESQUISA COM FILTRO DE ERRO
    while True:
        voltar_indice = str(input('Deseja realizar uma nova pesquisa?(s/n)\n'))
        if voltar_indice != 's' and voltar_indice != 'sim' and voltar_indice != 'S' and voltar_indice != 'SIM' and voltar_indice != 'n' and voltar_indice != 'nao' and voltar_indice != 'não' and voltar_indice != 'N' and voltar_indice != 'NAO' and voltar_indice != 'NÃO':
            continue
        elif voltar_indice == 's' or voltar_indice == 'sim' or voltar_indice == 'S' or voltar_indice == 'SIM':
            break
        else:
            loop = False
            break
    continue

