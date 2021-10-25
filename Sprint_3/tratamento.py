import pandas as pd

# ==================================================================
# Tratamento dos dados
# Tratando df_state.csv
df_state = pd.read_csv('docs/df_state.csv', sep=";")
df_state = df_state.drop(
    columns=['dia', 'mes', 'casos_pc', 'casos_mm7d', 'obitos_pc', 'obitos_mm7d', 'letalidade', 'nome_ra'
         , 'cod_ra', 'nome_drs', 'cod_drs', "pop_60", 'area', 'map_leg', 'map_leg_s', 'latitude', 'longitude','semana_epidem','codigo_ibge'])
df_state['nome_munic'] = df_state['nome_munic'].str.upper()
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
df_segunda= df_segunda.rename(
    columns={'Total Doses Aplicadas':'segundadose'})
df_segunda = df_segunda.drop(
    columns=['Dose'])

# Junção das doses no df_vacinas
df_vacinastratado = pd.merge(df_unica,df_segunda , how='inner', on='nome_munic')
df_vacinastratado = pd.merge(df_vacinastratado,df_primeira , how='inner', on='nome_munic')
df_vacinastratado.fillna(('-'), inplace=True)

# Junção das vacinas.csv e df_state.csv no df_tratado.csv
df_state['datahora'] = pd.to_datetime(df_state['datahora'],format='%d/%m/%Y')
df_state.sort_values("datahora")
df_state.to_csv("docs/df_tratado.csv")
df_vacinastratado.to_csv("docs/df_vacinastratado.csv")
