# pip install pyTelegramBotAPI
# bot: https://t.me/elrwegBot
# send message in bot /weather or /get_weather or /pogoda

import telebot
import requests
import json

import os
import sys
import subprocess

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


@bot.message_handler(commands=['get_weather', 'weather', 'pogoda'])
def get_weather(message):
    bot.send_message(message.chat.id, text=f"{mess}")


bot.polling(none_stop=True)
