import telebot

CHAVE_API = "2054963815:AAF-v9jj4Jw8gDiwEXC7OZAMXXn5fy1LZjA"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["obitos"])
def obitos(mensagem):
    bot.send_message(mensagem.chat.id, "Ops ainda não temos dados")

@bot.message_handler(commands=["imunizados"])
def imunizados(mensagem):
    bot.send_message(mensagem.chat.id, "Ops ainda não temos dados")

@bot.message_handler(commands=["novoscasos"])
def novoscasos(mensagem):
    bot.send_message(mensagem.chat.id, "Ops ainda não temos dados")

@bot.message_handler(commands=["dados"])
def opcao1(mensagem):
    texto =  """ 
    O que você quer vizualizar? (Clique em uma opção)
    /obitos Obitos
    /imunizados Imunizados
    /novoscasos Novos Casos"""
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
    /sobre Sobre
    
    Qualquer outra opção não vai funcionar"""
    bot.reply_to(mensagem, texto)

bot.polling()





    

