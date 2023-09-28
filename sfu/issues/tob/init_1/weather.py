# pip install pyTelegramBotAPI
# bot: https://t.me/elrwegBot
# send message in bot /menu

import telebot
from telebot import types


# токен телеграм бота
TKN = '5812655786:AAF6wr3qY5USkYRgDET2dKq1vaDHz_oYkzI'


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

# обработчик команды /help


@bot.message_handler(commands=['help'])  # создаем команду
def welcome_help(message):
    # вывод ответа на команду
    bot_prn_message(message, 'данный бот создан в учебных целях,\nотображает кнопку перехода на сайт www.gismeteo.ru и кнопку перехода на сайт yandex.ru  по команде /start')

# обработчик команды /menu


@bot.message_handler(commands=['menu'])  # создаем команду
def welcome_menu(message):
    # вывод ответа на команду
    bot_prn_message(
        message, '/menu - вывод всех команд\n/start - вывод интерактивных кнопок\n/help - вывод подсказки')

# контрольное сообщение в консоль
print("start bot")

# запускаем бота в сеть
bot.polling(none_stop=True)


