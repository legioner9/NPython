# pip install pyTelegramBotAPI
# bot: https://t.me/elrwegBot
# send message in bot /weather or /get_weather or /pogoda

import telebot
from telebot import types

import requests
import json

import os
import sys
import subprocess
from pprint import pprint

output2 = subprocess.check_output(
    'echo $(curl https://api.open-meteo.com/v1/forecast\?latitude=52.52\&longitude=13.41\&current_weather=true)', shell=True)

print("output2 :", output2)

data = json.loads(output2)
cw = data["current_weather"]
print("temperature: ", cw["temperature"])
print("windspeed: ", cw["windspeed"])
print("time: ", cw["time"])

temperature = cw["temperature"]
windspeed = cw["windspeed"]
mess = "temperature: " + f"{temperature}" + " windspeed: " + f"{windspeed}"

print(mess)

list_text_message = [['hello', 'И тебе hello'], ['33', '2']]


# os.system('date +"Today is: %A %d %B"')
# os.system('curl https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true')

TKN = '5812655786:AAF6wr3qY5USkYRgDET2dKq1vaDHz_oYkzI'

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true'

bot = telebot.TeleBot(TKN)

# Тут работаем с командой start


def bot_prn_message(arg_message, arg_str):
    bot.send_message(arg_message.chat.id, arg_str)


@bot.message_handler(commands=['1'])
def welcome_start(message):
    bot_prn_message(message, '1')


@bot.message_handler(commands=['start'])  # создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button0 = types.InlineKeyboardButton(
        "Сайт gismeteo Divnogorsk 10 days", url='https://www.gismeteo.ru/weather-divnogorsk-11843/10-days/')
    markup.add(button0)
    button1 = types.InlineKeyboardButton(
        "Сайт yandex Divnogorsk 10 days", url='https://yandex.ru/pogoda/divnogorsk')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт в браузере)".format(
        message.from_user), reply_markup=markup)
    # print("0")


@bot.message_handler(commands=['pogoda'])
def get_weather(message):
    # bot_prn_message(message, text=f"{mess}")
    bot.send_message(message.chat.id, f"{mess}")


@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot_prn_message(message, 'данный бот создан в учебных целях,\nзапрашивает погоду с сайта api.open-meteo.com для вывода ответа в текстовом режиме в Красноярске по команде /pogoda,\nотображает кнопки перехода на сайт www.gismeteo.ru по команде /start')
    
@bot.message_handler(commands=['menu'])
def welcome_menu(message):
    bot_prn_message(message, '/menu - вывод всех команд\n/start - вывод интерактивных кнопок\n/help - вывод подсказки')

# 'commands' before 'content_types ?


@bot.message_handler(content_types=["text"])
def text(message):
    for item in list_text_message:
        if message.text == item[0]:
            bot_prn_message(message, item[1])


bot.polling(none_stop=True)
