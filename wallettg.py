import telebot
import random
bot = telebot.TeleBot("1946845356:AAEnbZ8V-o5YfCjpg0zOjfPU-DDN0p3IGQ8", parse_mode=None)

wallets = []
walletsrandom = []
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
    if len(wallets) == 50 or len(wallets) == 100 or len(wallets) == 500 or len(wallets) == 1000:
        mensagem = bot.send_message('-1001548697096','Restam '+ str(len(wallets)) + ' wallets!')
        bot.pin_chat_message('-1001548697096',mensagem.id)
        variable = random.choice(wallets)
        walletsrandom.append(variable)
        wallets.remove(variable)
        bot.reply_to(message, variable)
        my_wallet() 
    else:
        variable = random.choice(wallets)
        wallets.remove(variable)
        bot.reply_to(message, variable)
        my_wallet()

@bot.message_handler(commands=['randomwallet'])
def send_message(message):
    for i in range(len(walletsrandom)):
        bot.reply_to(message,walletsrandom[i])
      
bot.polling()


