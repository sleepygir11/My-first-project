import telebot
from collections import defaultdict
import os,random

bot = telebot.TeleBot("")

MEDIA_FOLDER = "bot_media"

if not os.path.exists(MEDIA_FOLDER):
   os.makedirs(MEDIA_FOLDER)
   with open(os.path.join(MEDIA_FOLDER, "test.txt"),"w") as f:
      f.write('Это тестовый файл от вашего бота!')



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

@bot.message_handler(commands = ['pic'])
def send_random_pic(message):
   pics = []
   bot.send_photo(message.chat.id,random.choice(pics),
                  caption = "Вот тебе случайная картинка!")
   
   
@bot.message_handler(func = lambda message : True)
def smart_parrot(message):
   user_id = message.from_user.id
   user_stats[user_id]['repeat_count']+= 1
   user_stats[user_id]['last_message'] = message.text
   print('Пользователь отправил', message.text)

   if '?' in message.text:
      response = f'🦜Ты спросил ({user_stats[user_id]['repeat_count']}): {message.text}'
   elif "!" in message.text:
      response = f'🦜Ты воскликнул ({user_stats[user_id]['repeat_count']}) : {message.text}'
   else:
      response = f'🦜Повторяю ({user_stats[user_id]['repeat_count']}) : {message.text}'

   bot.send_message(message.chat.id, response)

bot.polling()
