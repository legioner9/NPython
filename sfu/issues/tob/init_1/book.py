# 6034220116:AAGJGPtYhyIq8dkPCygYDMSzUyFzrOdx49A
import requests
import telebot
from telebot import types
TOKEN = '5812655786:AAF6wr3qY5USkYRgDET2dKq1vaDHz_oYkzI'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(
        m.chat.id, 'Добрый день Уважаемый студент! Как вопрос тебя интересует?')
    bot.send_message(m.from_user.id, text='Выбери из списка?',
                     reply_markup=keyboard)


keyboard = types.InlineKeyboardMarkup()

key_1 = types.InlineKeyboardButton(
    text='Психология, мотивация', callback_data='data1')
keyboard.add(key_1)

key_2 = types.InlineKeyboardButton(
    text='Серьезное чтение', callback_data='data2')
keyboard.add(key_2)

key_3 = types.InlineKeyboardButton(text='Бизнес-книги', callback_data='data3')
keyboard.add(key_3)


URL = 'https://api.telegram.org/bot'


def send_photo_file(chat_id, img):
    files = {'photo': open(img, 'rb')}
    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "data1":
        bot.send_message(
            call.message.chat.id, text='Зарубежная психология\nСаморазвитие/личностный рост\nПсихология управления')
    if call.data == "data2":
        bot.send_message(
            call.message.chat.id, text='Зарубежная психология\nСаморазвитие/личностный рост\nПсихология управления')
    if call.data == "data3":
        bot.send_message(
            call.message.chat.id, text='Зарубежная психология\nСаморазвитие/личностный рост\nПсихология управления')


print('Start')

bot.polling(none_stop=True, interval=0)
