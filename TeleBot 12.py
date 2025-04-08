import telebot
import time
from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
   markup = types.InlineKeyboardMarkup()
   btn1 = types.InlineKeyboardButton('Перейти на сайт', url ="")
   markup.row(btn1)
   btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
   btn3 = types.InlineKeyboardButton('Изменить текст', callback_data = 'edit')
   markup.row(btn2, btn3)
   bot.reply_to(message,"Вау, какая фотка!", reply_markup = markup)

@bot.message_handler(content_types = ['text']) 
def calculator(message):
      try:
         result = eval(message.text)
         bot.reply_to(message, f'{result}')
      except:
         bot.reply_to(message, "Извини, я не понимаю!")
      
bot.polling(none_stop = True, interval = 0)