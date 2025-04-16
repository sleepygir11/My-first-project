import telebot
import requests
import json
from telebot import types

bot = telebot.TeleBot("")

API = ''


@bot.message_handler(commands = ['start'])
def start(message):
   bot.send_message(message.chat.id, 'Привет, я бот, показывающий погоду!☀ Напиши название города!🏩')


@bot.message_handler(commands = ['bebebe'])
def bebebe(message):
   bot.reply_to(message,"Улыбнись!(Ответь своей фоткой, я сделаю ее незабываемой!)")

@bot.message_handler(content_types=['photo'])
def send_bibizyanka(message):
   a ='сюда джэпэгэ или пнг'
   aka = open(a)
   bot.send_photo(message.chat.id, aka)
   bot.send_message(message.chat.id, "Это ты!)")


@bot.message_handler(content_types = ['text'])
def get_weather(message):
   city = message.text.strip()
   res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
   if res.status_code == 200:
      data = json.loads(res.text)
      temp = data['main']['temp']
      bot.reply_to(message, f'Сейчас погода в городе {city} : {temp}°C')
      image = 'SUN.png' if temp > 10.0 else 'snow.png'
      techo = 'morozik.png'
      file = open(image if temp >0 or temp >10 else techo, 'rb')
      bot.send_photo(message.chat.id, file)
   else:
      bot.reply_to(message, f'Город указан неверно')
      

bot.polling(none_stop=True, interval= 0)



# questions = [
#    {
#       "question": "Сколько планет в Солнечной системе?",
#       "options": ["8", "9","10"],
#       "answer": "8"
#    }
# ]

# @bot.message_handler(commands = ['start'])
# def start_quiz(message):
#    global question_index
#    question_index = 0
#    send_question(message.chat.id)

# def send_question(chat_id):
#    question_data = questions[question_index]
#    markup = types.InlineKeyboardMarkup()
#    for option in question_data["options"]:
#       button = types.InlineKeyboardButton(text = option, callback_data= option)
#       markup.add(button)
#    bot.send_message(chat_id, question_data["question"], reply_markup=markup)


# @bot.callback_query_handler(func = lambda call:True)

# def handle_answer(call):
#    global question_index
#    question_data = questions[question_index]
#    if call.data == question_data["answer"]:
#       bot.answer_callback_query(call.id, text = "Правильно!")
#    else:
#       bot.answer_callback_query(call.id, text = f'Нерправильно! Правильный ответ:{question_data['answer']}')
#    question_index +=1
#    if question_index < len(questions):
#       send_question(call.message.chat.id)
#    else:
#       bot.send_message(call.message.chat.id,"Викторина завершена! Спасибо за участие.")

# bot.polling(none_stop = True, interval = 0)