import telebot
import time, random
from telebot import types

bot = telebot.TeleBot("")

def create_main_menu():
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

   buttons = [
      types.KeyboardButton('Случайное число🎲'),
      types.KeyboardButton('😊Текущее время'),
      types.KeyboardButton('😎Сегодняшняя дата'),
      types.KeyboardButton('🔝О боте'),
      types.KeyboardButton('Подбери песню из плейлиста разработчика!🎵'),
      types.KeyboardButton("Моя цитата на день🧾"),
      types.KeyboardButton('Поддержи меня!😢')
   ]
   markup.add(*buttons)
   return markup

@bot.message_handler(commands = ['start'])

def start(message):
   bot.send_message(message.chat.id, 
                    "Привет! Я с кнопками🤩\n"
                    "Попробуй нажать на любую кнопку внизу👇\n",
                    reply_markup =create_main_menu())
@bot.message_handler(commands = ['time'])

def send_time(message):
   current_time = time.strftime("%H:%M:%S")
   bot.send_message(message.chat.id,f"🕐Точное время : {current_time}")


@bot.message_handler(func = lambda message: True)

def handle_buttons(message):
   quate =['Извините, что я говорю, когда вы перебиваете',
           'Когда просят убрать в комнате, цитируй Эйнштейна: "Только дурак нуждается в порядке - гений господствует над хаосом',
           'Если дело не клеится, его шьют',
           'Все что ни делается - все к лучшему'
           ]
   support = ['Я понимаю тебя, ты не один',
              'У тебя все получится!',
              'Я тебя люблю',
              'Ты очень красивый человек!',
              'Все будет хорошо!'
              ]
   aiai = random.choices(support)
   tracks = ['https://music.yandex.ru/album/1316543/track/12129075?utm_source=web&utm_medium=copy_link', 
            'https://music.yandex.ru/album/26919972/track/116055755?utm_source=web&utm_medium=copy_link',
            'https://music.apple.com/de/album/%D0%B7%D0%BD%D0%B0%D0%B5%D1%88%D1%8C-%D1%82%D0%B0%D0%BD%D1%8F/1183511039?i=1183511210',
            'https://music.apple.com/ru/album/%D0%BE%D1%84%D0%B8%D1%81%D0%BD%D1%8B%D0%B9-%D1%81%D1%82%D0%B8%D0%BB%D1%8F%D0%B3%D0%B0/1183511039?i=1183511208']
   if message.text == 'Случайное число🎲':
      num = random.randint(1,100)
      bot.send_message(message.chat.id, f'Твое счастливое число на сегодня : {num} 🍀')
   elif message.text == "😎Сегодняшняя дата":
      from datetime import datetime
      now = datetime.now().strftime("%H:%M:%S")
      date = datetime.now().strftime("%d.%m.%Y")
      bot.send_message(message.chat.id, f'Сегодня {date}🥰')
   elif message.text == '😊Текущее время' :
      from datetime import datetime
      now = datetime.now().strftime("%H:%M:%S")
      date = datetime.now().strftime("%d.%m.%Y")
      bot.send_message(message.chat.id,f'Сейчас {now}💓' )
      bot.send_message(message.chat.id, f'Сегодня {date}🥰')
   elif message.text == '🔝О боте':
      bot.send_message(message.chat.id,f'Этот бот был создан при поддержке ДИТ, разработчиком под псевдонимом sleepygir11. На гитхабе у нее много интересных проектов!🚀')
   elif message.text == 'Подбери песню из плейлиста разработчика!🎵':
      bot.send_audio(message.chat.id, random.choices(tracks),
                     title = "Случайный мой любимый трек!", performer = "Медиа-бот")
   elif message.text == 'Моя цитата на день🧾':
      bot.send_message(message.chat.id, f'Твоя цитата:{quate}')
   elif message.text == 'Поддержи меня!😢':
      bot.send_message(message.chat.id, aiai)
   else:
      bot.send_message(message.chat.id, 'Я не понимаю тебя, но со временем меня доработают!')
bot.polling(none_stop=True, interval=0)