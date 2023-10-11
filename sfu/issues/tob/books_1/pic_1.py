import telebot
from telebot import types
import time
import math
from urllib.request import urlopen

print('Бот запущен')
# Создаем экземпляр бота
TOKEN = '5812655786:AAF6wr3qY5USkYRgDET2dKq1vaDHz_oYkzI'
bot = telebot.TeleBot(TOKEN)
# Функция, обрабатывающая команду /start


@bot.message_handler(commands=["start"])
def start(message):
    mess = f'Привет, {message.from_user.first_name}!Я формулознайка,наилучший бот- помощник в поиске формул по математике 😇, выбери что ты хочешь:'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    poisk = types.KeyboardButton('Начать поиск🔍:')
    admin = types.KeyboardButton('Связь с разработчиком')
    podderzchka = types.KeyboardButton('Поддержать разработку💸')
    spisoksokr = types.KeyboardButton('Список сокращений:')
    bistriypoisk = types.KeyboardButton('Быстрый поиск🔎:')
    kalculator = types.KeyboardButton('Калькулятор кв. уравнений🧮')
    mess = f'Привет, {message.from_user.first_name}!Я формулознайка,наилучший бот- помощник в поиске формул по математике 😇, выбери что ты хочешь:'
    markup.add(poisk, admin, podderzchka, spisoksokr, bistriypoisk, kalculator)
    bot.send_message(message.chat.id, mess,
                     parse_mode='html', reply_markup=markup)


user_num1 = ''
user_num2 = ''
user_num3 = ''
discr = ''
korni = None


@bot.message_handler(content_types=["text"])
def bot_message(message):
    mess2 = '''Треуг.(Тр.)➡️Треугольник\nКв.➡️Квадрат\nПрямоуг.➡️Прямоугольник(-ый)\nОкр.➡️Окружность(круг)\nВпис.➡️Вписанный\nОпис.➡️Описанный\nПрил.➡️Прилежащая\nРавноб.➡️Равнобедренный\nКат.➡️Катет\nГипот.➡️Гипотенуза\nСтор.➡️Стороны\nИзв.➡️Изввестный(-ая)\nH(h)➡️Высота в общей геометрии\nS(s)➡️Площадь в общей геометрии\nL➡️Сторона в общей геометрии\nM(m)➡️Медиана в общей геометрии\nПроизв.➡️Произвольный(ого)\nПолуп.➡️Полупериметр\nОсн.➡️Основние/основа\nЧ/з➡️Через\nР-но➡️Ровно\nРавтост.➡️Равносторонний'''
    mess1 = 'Поддержите разработку если считаете это нужным, это поможет проэкту существовать и развиваться💥 Карта ПриватБанка: 5168 7559 0884 1170 Спасибо заранее!'
    mess3 = 'Связь с разработчиком: @MarcoPopa'
    mess4 = 'P.s после каждого ответа бота можете сразу продолжать искать другие формулы. Введи название формулы  ниже👇'
    mess5 = 'Введи ниже переменную а'
    mess6 = 'Введи переменную b'
    mess7 = 'Введи переменную с'
    if message.chat.type == 'private':
        if message.text == 'Поддержать разработку💸':
            bot.send_message(message.chat.id, mess1)
        elif message.text == 'Список сокращений:':
            bot.send_message(message.chat.id, mess2)
        elif message.text == 'Связь с разработчиком':
            bot.send_message(message.chat.id, mess3)
        elif message.text == 'Начать поиск🔍:':
            bot.send_message(message.chat.id, mess4)


@bot.message_handler(func=lambda msg: msg.text == 'photo')
def get_user_photo(message: types.Message):
    bot.send_photo(message.chat.id, "https://i.imgur.com/ofwPfHE.png")


bot.polling(none_stop=True)
