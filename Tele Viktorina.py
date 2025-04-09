import telebot
from telebot import types

bot = telebot.TeleBot("")

questions = [
   {
      "question": "Сколько планет в Солнечной системе?",
      "options": ["8", "9","10"],
      "answer": "8"
   }
]

@bot.message_handler(commands = ['start'])
def start_quiz(message):
   global question_index
   question_index = 0
   send_question(message.chat.id)

def send_question(chat_id):
   question_data = questions[question_index]
   markup = types.InlineKeyboardMarkup()
   for option in question_data["options"]:
      button = types.InlineKeyboardButton(text = option, callback_data= option)
      markup.add(button)
   bot.send_message(chat_id, question_data["question"], reply_markup=markup)


@bot.callback_query_handler(func = lambda call:True)

def handle_answer(call):
   global question_index
   question_data = questions[question_index]
   if call.data == question_data["answer"]:
      bot.answer_callback_query(call.id, text = "Правильно!")
   else:
      bot.answer_callback_query(call.id, text = f'Нерправильно! Правильный ответ:{question_data['answer']}')
   question_index +=1
   if question_index < len(questions):
      send_question(call.message.chat.id)
   else:
      bot.send_message(call.message.chat.id,"Викторина завершена! Спасибо за участие.")

bot.polling(none_stop = True, interval = 0)