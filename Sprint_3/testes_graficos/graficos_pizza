import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vacinas.csv', sep=";")

df = df.query('munic == "SANTA BRANCA"')

plt.pie(df["total"], labels = df["dose"], autopct = "%1.2f%%")
plt.title('Vacinação em porcentagem(%)')

plt.show()
