import pandas as pd
import matplotlib.pyplot as plt

df_vacinas_tratado = pd.read_csv('df_vacinastratado.csv')
df_vacinas = pd.read_csv('vacinas.csv', sep=";")

#soma_unica = df_vacinas_tratado.assign(unica=df_vacinas_tratado['doseunica'].sum())
soma_unica = df_vacinas_tratado['doseunica'].sum()
soma_segunda = df_vacinas_tratado['segundadose'].sum()
soma_primeira = df_vacinas_tratado['primeiradose'].sum()

df_vacinas = df_vacinas.append(dict(zip(df_vacinas.columns,['Estado', 'UNICA', soma_unica])), ignore_index=True)
df_vacinas = df_vacinas.append(dict(zip(df_vacinas.columns,['Estado', '2º DOSE', soma_segunda])), ignore_index=True)
df_vacinas = df_vacinas.append(dict(zip(df_vacinas.columns,['Estado', '1º DOSE', soma_primeira])), ignore_index=True)


print(df_vacinas)

#soma_primerira = df.assign(primeira=df['dose' == "1° DOSE"].sum())
#soma_segunda = df.assign(segunda=df['dose' == "2° DOSE"].sum())
#soma_terceira = df.assign(terceira=df['dose' == "3º DOSE"].sum())

#df = df.query('munic == ""')

#plt.pie(df["total"], labels = df["dose"], autopct = "%1.2f%%")

#plt.title('Vacinação em porcentagem(%)')

#plt.show()
