import telebot
from telebot import types 

# importing types(buttons)

bot = telebot.TeleBot('')
name = ''
age = 0
surname = ""

@bot.message_handler(content_types=["text"]) # в скобках так пишем типы данных, хэндлер - прослушка

# def get_text_message(message): #функция по отправке сообщений
#    if message.text == "Привет":
#       bot.send_message(message.from_user.id, "Привет, чем могу помочь?")
#    elif message.text == '/help':
#       bot.send_message(message.from_user_id, "Напиши привет")
#    else:
#       bot.send_message(message.from_user_id, "Я не понимаю тебя")
def start(message):
   if message.text == '/reg':
      bot.send_message(message.from_user.id, "Как тебя зовут?")
      bot.register_next_step_handler(message, get_name)
   else:
      bot.send_message(message.from_user.id, "Напиши /reg")

def get_name(message):
   global name 
   name = message.text
   bot.send_message(message.from_user.id,"Какая у тебя фамилия?")
   bot.register_next_step_handler(message, get_surname)

def get_surname(message):
   global surname
   surname = message.text
   bot.send_message(message.from_user.id,"Сколько тебе лет?")
   bot.register_next_step_handler(message, get_age)

def get_age(message):
   global age 
   try:
      age = int(message.text)
      bot.send_message(message.from_user.id, 'Тебе'+ ' ' + str(age) + 'лет, тебя зовут ' + name + ' ' + surname + '?' )
   except ValueError :
      bot.send_message(message.from_user.id, 'Цифрами, пожалуйста. Сколько тебе лет?')
      bot.register_next_step_handler(message,get_age)
   keyboard = types.InlineKeyboardMarkup()
   key_yes = types.InlineKeyboardButton(text = "Да", callback_data = 'yes')
   keyboard.add(key_yes)
   key_no = types.InlineKeyboardButton(text = "Нет", callback_data = "no")
   keyboard.add(key_no)
   question = 'Тебе'+ ' ' + str(age) + 'лет, тебя зовут ' + name + ' ' + surname + '?' 
   bot.send_message(message.from_user.id, text = question, reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: True)  # That is gonna repeat often

def callback_worker(call):
   if call.data == 'yes':
      bot.send_message(call.message.chat.id, 'Запомню : )')
   elif call.data == 'no':
      pass

bot.polling(none_stop = True, interval = 0) #чтобы работал нон стопом(прослушка)




