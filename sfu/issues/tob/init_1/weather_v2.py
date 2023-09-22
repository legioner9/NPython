# pip install pyTelegramBotAPI
# bot: https://t.me/elrwegBot
# send message in bot /weather or /get_weather or /pogoda

import telebot
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


# os.system('date +"Today is: %A %d %B"')
# os.system('curl https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true')

TKN = '5812655786:AAF6wr3qY5USkYRgDET2dKq1vaDHz_oYkzI'

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true'

bot = telebot.TeleBot(TKN)

# Тут работаем с командой start


@bot.message_handler(commands=['1'])
def welcome_start(message):
    bot.send_message(message.chat.id, '1')


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == '33':
        bot.send_message(message.chat.id, '2')


@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(message.chat.id, 'Приветствую тебя user')



@bot.message_handler(commands=['get_weather', 'weather', 'pogoda'])
def get_weather(message):
    bot.send_message(message.chat.id, text=f"{mess}")




@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Чем я могу тебе помочь')




@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'И тебе hello')

pprint(bot.message_handlers)

# [{'filters': {'commands': ['1'], 'content_types': ['text']},
#   'function': <function welcome_start at 0x7ff88f01ddc0>,
#   'pass_bot': False},
#  {'filters': {'content_types': ['text']},
#   'function': <function text at 0x7ff88f01de50>,
#   'pass_bot': False},
#  {'filters': {'commands': ['start'], 'content_types': ['text']},
#   'function': <function welcome_start at 0x7ff88f01dee0>,
#   'pass_bot': False},
#  {'filters': {'commands': ['get_weather', 'weather', 'pogoda'],
#               'content_types': ['text']},
#   'function': <function get_weather at 0x7ff88f01df70>,
#   'pass_bot': False},
#  {'filters': {'commands': ['help'], 'content_types': ['text']},
#   'function': <function welcome_help at 0x7ff88f027040>,
#   'pass_bot': False},
#  {'filters': {'content_types': ['text']},
#   'function': <function text at 0x7ff88f0270d0>,
#   'pass_bot': False}]

bot.polling(none_stop=True)
