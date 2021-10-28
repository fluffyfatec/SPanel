#------Bibliotecas------#
import telebot
import pandas as pd
#-----------------------#

# t.me/Fluffyapi_bot   caminho para o bot
CHAVE_API = "2068198957:AAFKYaIzYWW8pYmhB1_V5-TorX3pfp1xn7A"

df = pd.read_csv("docs\df_estadotratado.csv")

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
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \nÓbitos Totais:  {deaths}\n \nNovos óbitos:  {new_deaths}. ")

#imunizados
@bot.message_handler(commands=["imunizados"])
def imunizados(mensagem):
    bot.send_message(mensagem.chat.id, "Ops ainda não temos dados")

#novos casos no periodo
@bot.message_handler(commands=["casos"])
def casos(mensagem):
    bot.send_message(mensagem.chat.id, f"Dados do dia:  {lastDate}\n  \nCasos Totais:  {cases}\n \nNovos casos: {new_cases}")

#população do estado de SP
@bot.message_handler(commands=["pop"])
def casos(mensagem):
    bot.send_message(mensagem.chat.id, f" Atualmente a população do estado de São Paulo é de {population} pessoas.")


@bot.message_handler(commands=["dados"])
def opcao1(mensagem):
    texto =  """ 
    O que você quer vizualizar? (Clique em uma opção)
    /obitos Óbitos
    /imunizados Imunizados
    /casos Casos"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["sobre"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, """ SPanel é um projeto de estudantes da FATEC SJC que visa informar dados atualizados sobre a Covid19 no estado de São Paulo. Para mais informações entrar em contato via E-mail.

E-mail (fluffyfatec@gmail.com)
GitHub (https://github.com/fluffyfatec)""")



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





    

