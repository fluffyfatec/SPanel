import pandas as pd

# ==================================================================
# Tratamento dos dados
# Tratando df_state.csv
df_state = pd.read_csv('docs/df_state.csv', sep=";")
df_state = df_state.drop(
    columns=['dia', 'mes', 'casos_pc', 'casos_mm7d', 'obitos_pc', 'obitos_mm7d', 'letalidade', 'nome_ra'
         , 'cod_ra', 'nome_drs', 'cod_drs', "pop_60", 'area', 'map_leg', 'map_leg_s', 'latitude', 'longitude','semana_epidem','codigo_ibge'])
df_state['nome_munic'] = df_state['nome_munic'].str.upper()
df_state['datahora'] = pd.to_datetime(df_state['datahora'],format='%d/%m/%Y')

# Tratando dados estado
df_estadotratado = df_state.drop(
    columns=['nome_munic'])
df_estadotratado = df_estadotratado.assign(estado='SÃO PAULO')
df_estadotratado.sort_values("datahora")
df_estadotratado['casos'] = df_estadotratado.groupby('datahora')["casos"].transform(sum)
df_estadotratado['casos_novos'] = df_estadotratado.groupby('datahora')["casos_novos"].transform(sum)
df_estadotratado['obitos'] = df_estadotratado.groupby('datahora')["obitos"].transform(sum)
df_estadotratado['obitos_novos'] = df_estadotratado.groupby('datahora')["obitos_novos"].transform(sum)
df_estadotratado['pop'] = df_estadotratado.groupby('datahora')["pop"].transform(sum)
df_estadotratado=df_estadotratado.drop_duplicates(subset='datahora', keep='first')


# Tratando df_regiao
df_regiao_tratado = pd.read_csv("docs/df_regiao.csv", sep=';')
df_regiao_tratado = df_regiao_tratado.drop(
    columns= [ 'pacientes_uti_mm7d','total_covid_uti_mm7d','internacoes_7d_l','internacoes_7v7', 'pacientes_uti_ultimo_dia',
        'pacientes_enf_mm7d','total_covid_enf_mm7d','pacientes_enf_ultimo_dia','total_covid_enf_ultimo_dia', 'leitos_pc'])

# Tratando df_gastos

df_gastos = pd.read_csv('docs/COVID.csv', sep=";",dtype='unicode')
df_gastos = df_gastos.drop(columns=['Nome Programa','Código Programa','Data da Movimentação','Código Ação','Nome Açao','Número do Processo','Modalidade de Contratação'
                                    ,'Contratada / Conveniada','CPF / CNPJ / CGC','Descrição Processo','Finalidade/Item','Data de Celebração',
                                    'Prazo Contratual','Período Prazo Contratual','Status Licitação','Quantidade','Valor Unitário',
                                    'Nota de Empenho','Tipo de Pagamento','Número de Pagamento',
                                    'Fonte','Código Nome Fonte Detalhada','Link Evento Licitação/Contrato','Link Licitação','Link Processo','Data de Atualização','Ano Referencia'])

df_gastos['Empenho'] = df_gastos['Empenho'].apply(lambda x: float(x.replace(".","").replace(",",".")))
df_gastos['Valor NP'] = df_gastos['Valor NP'].apply(lambda x: float(x.replace(".","").replace(",",".")))
df_gastos['Valor OB'] = df_gastos['Valor OB'].str.replace('.','',regex=True)
df_gastos['Valor OB'] = df_gastos['Valor OB'].str.replace(',','.').astype(float)
df_gastos['Total Pago'] = df_gastos.apply(lambda x: x['Valor NP']+ x['Valor OB'], axis=1)

df_gastos = df_gastos.drop(columns=['Valor NE','Valor NL','Valor NP','Valor OB'])

df_gastos['Total Pago'] = df_gastos.groupby('Nome Município')["Total Pago"].transform(sum)
df_gastos['Empenho'] = df_gastos.groupby('Nome Município')["Empenho"].transform(sum)

df_gastos=df_gastos.drop_duplicates(subset='Nome Município', keep='first')

decimals = 2
df_gastos['Total Pago'] = df_gastos['Total Pago'].apply(lambda x: round(x, decimals))
df_gastos['Empenho'] = df_gastos['Empenho'].apply(lambda x: round(x, decimals))

# Tratando vacinas.csv
df=pd.read_csv("docs/vacinas.csv", sep=';')
df = df.rename(
    columns={'Município':'nome_munic'})
# ==================================================================
df_unica = df[df['Dose'] =='UNICA']
df_unica = df_unica.rename(
    columns={'Total Doses Aplicadas':'doseunica'})
df_unica = df_unica.drop(
    columns=['Dose'])
# ==================================================================
df_primeira = df[df['Dose'] =='1° DOSE']
df_primeira = df_primeira.rename(
    columns={'Total Doses Aplicadas': 'primeiradose'})
df_primeira = df_primeira.drop(
    columns=['Dose'])
# ==================================================================
df_segunda = df[df['Dose'] =='2° DOSE']
df_segunda = df_segunda.rename(
    columns={'Total Doses Aplicadas':'segundadose'})
df_segunda = df_segunda.drop(
    columns=['Dose'])
# ==================================================================
df_terceira = df[df['Dose'] =='3º DOSE']
df_terceira = df_terceira.rename(
    columns={'Total Doses Aplicadas':'terceiradose'})
df_terceira = df_terceira.drop(
    columns=['Dose'])
df_pop = df_state.drop(
    columns=['datahora', 'casos','casos_novos','obitos','obitos_novos'])
df_pop=df_pop.drop_duplicates(subset='nome_munic', keep='first')

# Junção das doses no df_vacinas
df_vacinastratado = pd.merge(df_unica,df_primeira, how='inner', on='nome_munic')
df_vacinastratado = pd.merge(df_vacinastratado,df_segunda, how='inner', on='nome_munic')
df_vacinastratado = pd.merge(df_vacinastratado,df_terceira, how='inner', on='nome_munic')
df_vacinastratado = pd.merge(df_vacinastratado,df_pop, how='inner', on='nome_munic')
df_vacinastratado.fillna(('-'), inplace=True)


# Junção das vacinas.csv e df_state.csv no df_tratado.csv
df_state.sort_values("datahora")
df_state.to_csv("docs/df_tratado.csv")
df_vacinastratado.to_csv("docs/df_vacinastratado.csv")
df_estadotratado.to_csv("docs/df_estadotratado.csv")
df_regiao_tratado.to_csv("docs/df_regiao_tratado.csv")
df_gastos.to_csv("docs/df_gastos.csv")
