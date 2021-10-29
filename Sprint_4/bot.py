#------Bibliotecas------#
import telebot
import pandas as pd
#-----------------------#

# t.me/Fluffyapi_bot   caminho para o bot
CHAVE_API = "2068198957:AAFKYaIzYWW8pYmhB1_V5-TorX3pfp1xn7A"

df = pd.read_csv("docs\df_estadotratado.csv")
df_vs = pd.read_csv("docs\df_vacinastratado.csv")


df_vs.loc["Total"] = df_vs.sum()
column_sum = df_vs["Total_imunizados"] = df_vs["doseunica"] + df_vs["segundadose"]
column_tt = df_vs["Total_imunizados"]
max_vs = column_tt.max()


date_column = df["datahora"]
max_value = date_column.max()
row = df.loc[df["datahora"] == max_value]

# Dados mais atualizados Covid19
lastDate = row["datahora"].values[0]
cases = row["casos"].values[0]
new_cases = row["casos_novos"].values[0]
deaths = row["obitos"].values[0]
new_deaths = row["obitos_novos"].values[0]
population = row["pop"].values[0]


bot = telebot.TeleBot(CHAVE_API)

#obitos
@bot.message_handler(commands=["obitos"])
def obitos(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \nÓbitos Totais:  {deaths}\n \nNovos óbitos:  {new_deaths}.\n------------------------------------------------------------------\n Para ver dados da Covid19: /dados\n Para ver dados sobre a população: /pop\n  Para ver sobre o projeto: /sobre. ")

#imunizados
@bot.message_handler(commands=["imunizados"])
def imunizados(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \n Atualmente foram imunizadas: {max_vs} pessoas.\n-----------------------------------------------------------------------\n Para ver dados da Covid19: /dados\n Para ver dados sobre a população: /pop\n  Para ver sobre o projeto: /sobre.")

#novos casos no periodo
@bot.message_handler(commands=["casos"])
def casos(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \nCasos Totais:  {cases}\n \nNovos casos: {new_cases}\n---------------------------------------------------------------\n Para ver dados da Covid19: /dados\n Para ver dados sobre a população: /pop\n  Para ver sobre o projeto: /sobre.")

#população do estado de SP
@bot.message_handler(commands=["pop"])
def casos(mensagem):
    bot.send_message(mensagem.chat.id, f" Atualmente a população do estado de \nSão Paulo é de {population} pessoas.\n-----------------------------------------------------------------------\n Para ver dados da Covid19: /dados\n  Para ver sobre o projeto: /sobre.  ")


@bot.message_handler(commands=["dados"])
def opcao1(mensagem):
    texto =  f"O que você quer vizualizar? (Clique em uma opção)\n-----------------------------------------------------------------------\n /obitos Óbitos\n/imunizados Imunizados\n/casos Casos"
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["sobre"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, """ SPanel é um projeto de estudantes da FATEC SJC que visa informar dados atualizados sobre a Covid19 no estado de São Paulo. Para mais informações entrar em contato via E-mail.\n ------------------------------------------------------------------ \n E-mail (fluffyfatec@gmail.com)\nGitHub (https://github.com/fluffyfatec)\n\n Para ver dados da Covid19: /dados\n Para ver dados sobre a população: /pop \n ------------------------------------------------------------------ \n""")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Olá, eu sou o Bot do SPanel que te atualiza sobre os resultados da Covid19 no estado de São Paulo.

     Escolha uma opção para continuar (clique no item)
    
    /dados Vizualizar dados da Covid19
    /pop População do estado de São Paulo
    /sobre Sobre
    
    Qualquer outra opção não vai funcionar"""
    bot.reply_to(mensagem, texto)

bot.polling()





    

