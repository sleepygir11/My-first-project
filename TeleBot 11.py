import telebot
from collections import defaultdict

bot = telebot.TeleBot("")

user_stats = defaultdict(lambda : {'repeat_count' : 0, 'last_message ': ''})

@bot.message_handler(commands = ['start'])
def start(message):
   bot.send_message(message.chat.id,"Я теперь продвинутый попугай! 😋 \n"
   "Я не только повторяю, но и запоминаю,сколько раз ты мне это говорил!")

@bot.message_handler(commands = ['stats'])
def show_stats(message):
   user_id = message.from_user.id
   stats = user_stats[user_id]
   bot.send_message(message.chat.id, 
                    f'📊Твоя статистика:\n'
                    f'Повторений: {stats['repeat_count']}\n'
                    f"Последнее сообщение: '{stats['last_message']}'")


bot.polling()
