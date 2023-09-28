# pip install pyTelegramBotAPI
# bot: https://t.me/elrwegBot
# send message in bot /help

import telebot
from telebot import types

import json
import subprocess

# curl запрос
output = subprocess.check_output(
    'echo $(curl https://api.open-meteo.com/v1/forecast\?latitude=56.00\&longitude=92.52\&current_weather=true)', shell=True)

# получение json тела запроса
data = json.loads(output)

# получение объекта current_weather
cw = data["current_weather"]

# получение полей объекта current_weather
temperature = cw["temperature"]
windspeed = cw["windspeed"]
time = cw["time"]

# контрольный вывод в консоль
print(f'temperature: {temperature}')
print(f'windspeed: {windspeed}')
print(f'time: {time}')

# формирование текста ответа на команду /pogoda
mess = f"Погода в Красноярске по версии open-meteo.com:\n     время: (по Гринвичу +7 Красноярск) {time}\n     температура воздуха: {temperature}\n     ветер: {windspeed}"

# токен телеграм бота
TKN = '5812655786:AAF6wr3qY5USkYRgDET2dKq1vaDHz_oYkzI'

# url запроса погоды в Красноярске по высоте и долготе
url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true'

# создание объекта бот
bot = telebot.TeleBot(TKN)

# вспомогательная функция send text message


def bot_prn_message(arg_message, arg_str):
    bot.send_message(arg_message.chat.id, arg_str)

# обработчик команды /start


@bot.message_handler(commands=['start'])  # создаем команду
def start(message):

    markup = types.InlineKeyboardMarkup()

    # формируем кнопку
    button0 = types.InlineKeyboardButton(
        "Сайт gismeteo.ru Krasnoyarsk 10 days", url='https://www.gismeteo.ru/weather-krasnoyarsk-4674/10-days/')

    # добавляем кнопку к выводу
    markup.add(button0)

    # формируем кнопку
    button1 = types.InlineKeyboardButton(
        "Сайт yandex.ru Krasnoyarsk 10 days", url='https://yandex.ru/pogoda/ru-RU/details?lat=56.01056671&lon=92.85256958&lang=ru&via=ms')

    # добавляем кнопку к выводу
    markup.add(button1)

    # вывод ответа на команду
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт в браузере)".format(
        message.from_user), reply_markup=markup)

# обработчик команды /pogoda


@bot.message_handler(commands=['pogoda'])  # создаем команду
def get_weather(message):
    # вывод ответа на команду
    bot.send_message(message.chat.id, f"{mess}")

# обработчик команды /help


@bot.message_handler(commands=['help'])  # создаем команду
def welcome_help(message):
    # вывод ответа на команду
    bot_prn_message(message, 'данный бот создан в учебных целях,\nзапрашивает погоду с сайта api.open-meteo.com для вывода ответа в текстовом режиме в Красноярске по команде /pogoda,\nотображает кнопку перехода на сайт www.gismeteo.ru и кнопку перехода на сайт yandex.ru  по команде /start')

# обработчик команды /menu


@bot.message_handler(commands=['menu'])  # создаем команду
def welcome_menu(message):
    # вывод ответа на команду
    bot_prn_message(
        message, '/menu - вывод всех команд\n/start - вывод интерактивных кнопок\n/pogoda - вывод погоды\n/help - вывод подсказки')


# запускаем бота в сеть
bot.polling(none_stop=True)
