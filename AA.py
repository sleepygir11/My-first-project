import telebot
import time

bot = telebot.TeleBot("")

@bot.message_handler(commands =['help'])

def send_help(message):
   help_text = """ 
   Список моих команд:
   /start - начать общение
   /help - подсказка  
   /time - покажу точное время
   /date - скажу какое сегодня число
   /secret - 
   """
   bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands = ['time'])

def send_time(message):
   current_time = time.strftime("%H:%M:%S")
   bot.send_message(message.chat.id,f"🕐Точное время : {current_time}")
   
@bot.message_handler(commands = ['date'])

def send_date(message):
   month = ['января', "февраля", "марта", "апреля", "мая", "июня", "июля", "августа",
            "сентября","октября", "ноября","декабря"]
   today = time.localtime()
   bot.send_message(message.chat.id,
                    f'🌸Сегодня {today.tm_day} {month[today.tm_mon-1]}')

@bot.message_handler(commands = ['secret'])

def send_message(message):
   bot.send_message(message.chat.id,"о я крутой программист, я умею печатать хелло ворлд")

print("Бот запущен!")
bot.polling()

   


