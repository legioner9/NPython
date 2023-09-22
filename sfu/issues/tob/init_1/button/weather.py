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
    button1 = types.InlineKeyboardButton(
        "Сайт Хабр", url='https://habr.com/ru/all/')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(
        message.from_user), reply_markup=markup)
    # print("0")


@bot.message_handler(commands=['get_weather', 'weather', 'pogoda'])
def get_weather(message):
    # bot_prn_message(message, text=f"{mess}")
    bot.send_message(message.chat.id, f"{mess}")


@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot_prn_message(message, 'Чем я могу тебе помочь')

# 'commands' before 'content_types ?


@bot.message_handler(content_types=["text"])
def text(message):
    for item in list_text_message:
        if message.text == item[0]:
            bot_prn_message(message, item[1])


bot.polling(none_stop=True)
