# IMPORTAÇÕES
import pandas as pd
import numpy as np
from tabulate import tabulate

# Cuidando do CSV, puxando o dado bruto e retirando as colunas que não tem serventia e jogando no df_tratado
# DF_TRATADO.CSV
df_state = pd.read_csv('df_state.csv',sep=";")
df_state = df_state.drop(
    columns=['dia', 'mes', 'casos_pc', 'casos_mm7d', 'obitos_pc', 'obitos_mm7d', 'letalidade', 'nome_ra'
         , 'cod_ra', 'nome_drs', 'cod_drs', "pop_60", 'area', 'map_leg', 'map_leg_s', 'latitude', 'longitude','semana_epidem'])
df_state['nome_munic'] = df_state['nome_munic'].str.upper()

# VACINAS.CSV
df=pd.read_csv("vacinas.csv",sep=';')
df_unica = df[df['Dose'] =='UNICA']
df_segunda = df[df['Dose'] =='2° DOSE']
vacinadostotal=pd.concat([df_unica,df_segunda],axis=0 )
vacinadostotal = vacinadostotal.rename(
    columns={'Município':'nome_munic'})
vacinadostotal.fillna(('-'), inplace=True)

# JUNÇÃO DAS VACINAS NO DF_TRATADO.CSV E ATUALIZAÇÃO DA TABELA
df_state = pd.merge(df_state, vacinadostotal, how='inner', on='nome_munic')
df_state.to_csv("df_tratado.csv")
