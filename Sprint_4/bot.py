# pip install pytelegrambotapi
#------Bibliotecas------#
import telebot
import pandas as pd
#-----------------------#

# t.me/Fluffyapi_bot   caminho para o bot
CHAVE_API = "2068198957:AAE46QIHyUk3AEy5hPcXR-_M0f-duqP_NZg"

df = pd.read_csv("docs\df_estadotratado.csv")
df_vs = pd.read_csv("docs\df_vacinastratado.csv")
df_reg = pd.read_csv("docs\df_regiao_tratado.csv")


df_vs.loc["Total"] = df_vs.sum()
column_sum = df_vs["Total_imunizados"] = df_vs["doseunica"] + df_vs["segundadose"]
column_tt = df_vs["Total_imunizados"]
max_vs = column_tt.max()


date_column = df["datahora"]
max_value = date_column.max()
row = df.loc[df["datahora"] == max_value]

#Tratamento df_regiao
df_nreg = df_reg.loc[7181]
df_reg = df_reg.drop(df_reg.columns[[0]], axis=1)

# Dados mais atualizados Covid19
lastDate = row["datahora"].values[0]
cases = row["casos"].values[0]
new_cases = row["casos_novos"].values[0]
deaths = row["obitos"].values[0]
new_deaths = row["obitos_novos"].values[0]
population = row["pop"].values[0]
ocupation_7d = df_nreg["ocupacao_leitos"]
ocupation = df_nreg["ocupacao_leitos_ultimo_dia"]
uti = df_nreg["total_covid_uti_ultimo_dia"]
inter = df_nreg["internacoes_ultimo_dia"]
inter_7d = df_nreg["internacoes_7d"]
date_reg = df_nreg["datahora"]

# Formatação Numerica
form_cases = (f"{cases:_}")
form_cases = form_cases.replace("_",".")
form_ncases = (f"{new_cases:_}")
form_ncases = form_ncases.replace("_",".")
form_deaths = (f"{deaths:_}")
form_deaths = form_deaths.replace("_",".")
form_ndeaths = (f"{new_deaths:_}")
form_ndeaths = form_ndeaths.replace("_",".")
form_pop = (f"{population:_}")
form_pop = form_pop.replace("_",".")
form_vs = (f"{max_vs:_}")
form_vs = form_vs.replace("_",".")
form_uti = (f"{uti:_}")
form_uti = form_uti.replace("_",".")
form_inter = (f"{inter:_}")
form_inter = form_inter.replace("_",".")
form_inter7 = (f"{inter_7d:_}")
form_inter7 = form_inter7.replace("_",".")


bot = telebot.TeleBot(CHAVE_API)

#Departamento nacional de saude
@bot.message_handler(commands=["drs"])
def drs(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {date_reg}\n  \nOcupação de Leitos:  {ocupation}%\nOcupação de Leitos Ultimos 7 dias:   {ocupation_7d}%\n------------------------------------------------------------------\nLeitos de UTI para a COVID: {form_uti}\n------------------------------------------------------------------\nInternações confirmadas/suspeita: {form_inter}\nInternações nos ultimos 7 dias: {form_inter7}\n------------------------------------------------------------------\nPara ver dados da Covid19: /dados\nPara ver dados sobre a população: /pop\nPara ver sobre o projeto: /sobre. ")

#obitos
@bot.message_handler(commands=["obitos"])
def obitos(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \nÓbitos Totais:  {form_deaths}\n \nNovos óbitos:  {form_ndeaths}.\n------------------------------------------------------------------\nPara ver dados da Covid19: /dados\nPara ver dados sobre a população: /pop\nPara ver dados do Departamento Regional de Saúde /drs\nPara ver sobre o projeto: /sobre. ")

#imunizados
@bot.message_handler(commands=["imunizados"])
def imunizados(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \n Atualmente foram imunizadas: {form_vs} pessoas.\n-----------------------------------------------------------------------\n Para ver dados da Covid19: /dados\nPara ver dados sobre a população: /pop\nPara ver dados do Departamento Regional de Saúde /drs\nPara ver sobre o projeto: /sobre.")

#novos casos no periodo
@bot.message_handler(commands=["casos"])
def casos(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \nCasos Totais:  {form_cases}\n \nNovos casos: {form_ncases}\n---------------------------------------------------------------\nPara ver dados da Covid19: /dados\nPara ver dados sobre a população: /pop\nPara ver dados do Departamento Regional de Saúde /drs\nPara ver sobre o projeto: /sobre.")

#população do estado de SP
@bot.message_handler(commands=["pop"])
def casos(mensagem):
    bot.send_message(mensagem.chat.id, f" Atualmente a população do estado de \nSão Paulo é de {form_pop} pessoas.\n-----------------------------------------------------------------------\nPara ver dados da Covid19: /dados\nPara ver dados do Departamento Regional de Saúde /drs\nPara ver sobre o projeto: /sobre.  ")


@bot.message_handler(commands=["dados"])
def opcao1(mensagem):
    texto =  f"O que você quer visualizar? (Clique em uma opção)\n-----------------------------------------------------------------------\n /obitos Óbitos\n/imunizados Imunizados\n/casos Casos"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["sobre"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, f" SPanel é um projeto de estudantes da FATEC SJC que visa informar dados atualizados sobre a Covid19 no estado de São Paulo. Para mais informações entrar em contato via E-mail.\n ------------------------------------------------------------------ \n E-mail (fluffyfatec@gmail.com)\nGitHub (https://github.com/fluffyfatec)\n\nPara ver dados da Covid19: /dados\nPara ver dados sobre a população: /pop \nPara ver dados do Departamento Regional de Saúde /drs\n ------------------------------------------------------------------ \n")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Olá, eu sou o Bot do SPanel que te atualiza sobre os resultados da Covid19 no estado de São Paulo.

     Escolha uma opção para continuar (clique no item)
    
    /dados Visualizar dados da Covid19
    /drs Visualizar dados do Departamento Regional de Saúde
    /pop População do estado de São Paulo
    /sobre Sobre
    
    Qualquer outra opção não vai funcionar"""
    bot.reply_to(mensagem, texto)
print("\n\n\033[32m-------Em execução-------\033[0;0m\n\n")
bot.polling()





    




    

