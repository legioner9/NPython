#6832879247:AAEZs9ut0dhIj7xxvWSMpbHj_CHz_HxjQjE
import requests
import telebot

#Импортрируем типы из модели telebot, чтобы создавать кнопки
from telebot import types

# создаем экземпляр бота
bot = telebot.TeleBot('6832879247:AAEZs9ut0dhIj7xxvWSMpbHj_CHz_HxjQjE')

# функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(m, res=False):
     bot.send_message(m.chat.id, 'Привет! Я бот-помощник')
     # Показываем все кнопки сразу и пишем сообщение о выборе
     bot.send_message(m.from_user.id, text='Выбери понравившуюся категорию', reply_markup=keyboard)



#Готовим кнопки
keyboard = types.InlineKeyboardMarkup()
#По очереди готовим текст и обработчик для каждой программы
key_1 = types.InlineKeyboardButton(text='Серьезое чтение', callback_data='data1')
#И добавляем кнопку на экран
keyboard.add(key_1)
key_2 = types.InlineKeyboardButton(text='Психология, мотивация', callback_data='2')
keyboard.add(key_2)
key_3 = types.InlineKeyboardButton(text='Бизнес-книги', callback_data='3')
keyboard.add(key_3)

# Если выбран вариант Серьезное чтение

keyboard1 = types.InlineKeyboardMarkup()
key_1_1 = types.InlineKeyboardButton(text='Русская классическая литератра', callback_data='data1_1')
keyboard1.add(key_1_1)
key_1_2 = types.InlineKeyboardButton(text='Зарубежная классическая литература', callback_data='data1_2')
keyboard1.add(key_1_2)
key_1_3 = types.InlineKeyboardButton(text='Советская литература', callback_data='data1_3')
keyboard1.add(key_1_3)

keyboard2 = types.InlineKeyboardMarkup()
key_2_1 = types.InlineKeyboardButton(text='Русская классическая литератра', callback_data='data2_1')
keyboard1.add(key_2_1)
key_2_2 = types.InlineKeyboardButton(text='Зарубежная классическая литература', callback_data='data2_2')
keyboard1.add(key_2_2)
key_2_3 = types.InlineKeyboardButton(text='Советская литература', callback_data='data2_3')
keyboard1.add(key_2_3)


# Отправляем текст в Телеграм
@bot.callback_query_handler(func=lambda call: True)
def message(call):
     if call.data == "data1":
          bot.send_message(call.message.chat.id, text='Выбери категорию', reply_markup=keyboard1)

     if call.data == "data1_1":
          msg = 'Русская классическая литература'
          #        # Отправляем текст в Телеграм
          bot.send_message(call.message.chat.id, msg)
          bot.send_message(call.message.chat.id, text='Владимир Набоков "Камера обскура"\nФедор Достоевский "Бесы"\nФедор Достоевский "Братья Карамазовы"\nФедор Достоевский "Идиот"\nМихаил Булгаков "Мастер и Маргарита\nМихаил Булгаков "Записки юного врача"\nЛев Толстой "Анна Каренина"', reply_markup=keyboard1)

     if call.data == "data1_2":
          msg = 'Зарубежная классическая литература'
          #        # Отправляем текст в Телеграм
          bot.send_message(call.message.chat.id, msg)
          bot.send_message(call.message.chat.id, text='Эрих Мария Ремарк "Три товарища"\nЭрих Мария Ремарк "Триумфальная арка"\nДжером Дэвид Сэлинджер "Над пропостью во ржи"\nЧарльз Диккенс "Большие надежды"\nГабриэль Гарсиа Маркес "Сто лет одиночества"\nДжордж Оруэлл "1984"\nРэй Брэдбери "Вино из одуванчиков"', reply_markup=keyboard1)

     if call.data == "data1_3":
          msg = 'Советская литература'
          #        # Отправляем текст в Телеграм
          bot.send_message(call.message.chat.id, msg)
          bot.send_message(call.message.chat.id, text='Борис Васильев "А зори здесь тихие"\nБорис Васильев "Завтра была война"\nСергей Довлатов "Чемодан"\nМихаил Шолохов "Тихий дон"\nАркадий и Борис Стругацкие "Трудно быть богом"\nАркадий и Борис Стругацкие "Пикник на обочине\nАлександр Бек "Волоколамское шоссе"', reply_markup=keyboard)








@bot.callback_query_handler(func=lambda call: True)
def message(call):
     if call.data == "data2":
          bot.send_message(call.message.chat.id, text='Выбери категорию', reply_markup=keyboard2)

     if call.data == "data2_1":
          msg = 'Зарубежная психология'
          #        # Отправляем текст в Телеграм
          bot.send_message(call.message.chat.id, msg)
          bot.send_message(call.message.chat.id, text='Владимир Набоков "Камера обскура"\nФедор Достоевский "Бесы"\nФедор Достоевский "Братья Карамазовы"\nФедор Достоевский "Идиот"\nМихаил Булгаков "Мастер и Маргарита\nМихаил Булгаков "Записки юного врача"\nЛев Толстой "Анна Каренина"', reply_markup=keyboard2)

     if call.data == "data2_2":
          msg = 'Саморазвитие/личностный рост'
          #        # Отправляем текст в Телеграм
          bot.send_message(call.message.chat.id, msg)
          bot.send_message(call.message.chat.id, text='Эрих Мария Ремарк "Три товарища"\nЭрих Мария Ремарк "Триумфальная арка"\nДжером Дэвид Сэлинджер "Над пропостью во ржи"\nЧарльз Диккенс "Большие надежды"\nГабриэль Гарсиа Маркес "Сто лет одиночества"\nДжордж Оруэлл "1984"\nРэй Брэдбери "Вино из одуванчиков"', reply_markup=keyboard2)

     if call.data == "data2_3":
          msg = 'Психология управления'
          #        # Отправляем текст в Телеграм
          bot.send_message(call.message.chat.id, msg)
          bot.send_message(call.message.chat.id, text='Борис Васильев "А зори здесь тихие"\nБорис Васильев "Завтра была война"\nСергей Довлатов "Чемодан"\nМихаил Шолохов "Тихий дон"\nАркадий и Борис Стругацкие "Трудно быть богом"\nАркадий и Борис Стругацкие "Пикник на обочине\nАлександр Бек "Волоколамское шоссе"', reply_markup=keyboard1)
          
print('start')
bot.polling(none_stop=True, interval=0)



