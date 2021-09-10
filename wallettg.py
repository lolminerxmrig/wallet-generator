import telebot
import random
bot = telebot.TeleBot("1955874406:AAGFlqV5ZH5e6oXm88mHZYwoY6BPqesrnfw", parse_mode=None)

wallets = []
wallet = ''
variable = ''
f = open("wallets.txt", "r")
for x in f:
  wallets.append(x)

def my_wallet():
    with open("wallets.txt", "w") as f2:
        data = f.readlines()   
        for line in data :
            if line.strip("\n") != wallet : 
                f2.write(line)

@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    if not wallets:
        bot.reply_to(message,"No more wallets serrrr!")
    if len(wallets) == 5:
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


