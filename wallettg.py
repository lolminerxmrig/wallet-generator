import telebot
import random
bot = telebot.TeleBot("1976035765:AAFEj2UkVit8a42vxDpGK_CGpQ5rs4XE8R4", parse_mode=None)

wallets = []
wallet = ''
variable = ''
f = open("pajeetwallets.txt", "r")
for x in f:
  wallets.append(x)

def my_wallet():
    with open("pajeetwallets.txt", "w") as f2:
        data = f.readlines()   
        for line in data :
            if line.strip("\n") != wallet : 
                f2.write(line)

@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    if not wallets:
        bot.reply_to(message,"No more wallets serrrr!")
    if len(wallets) == 100:
        mensagem = bot.send_message('-1001548697096','Restam '+ str(len(wallets)) + ' wallets!')
        bot.pin_chat_message('-1001548697096',mensagem.id)
        variable = random.choice(wallets)
        wallets.remove(variable)
        bot.reply_to(message, variable)
        my_wallet() 
    else:
        variable = random.choice(wallets)
        wallets.remove(variable)
        bot.reply_to(message, variable)
        my_wallet()
      
bot.polling()


