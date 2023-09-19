import telebot
import requests
import json

TKN = '5812655786:AAF6wr3qY5USkYRgDET2dKq1vaDHz_oYkzI'

ANC = 'https://api.weather.yandex.ru/v2/informers?lat=55.75222&lon=37.61556'

bot = telebot.TeleBot(TKN)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text=f"{message.text}")


bot.polling(none_stop=True)
