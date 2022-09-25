import random
import telebot
import requests
from bot_token import bot_one
from telebot import types as ty


#Работа с текстом
@bot_one.message_handler(content_types=['text']) #указываем что конкрето работаем с текстомб если user отправляет текст ,то работает этот метод
def get_user_textt(message):
    if message.text== message.text == "Hello":
        bot_one.send_message(message.chat.id, "Привет странник", parse_mode='html')
    elif message.text == "id":
        bot_one.send_message(message.chat.id,f"Твой Id: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo kiski" or "kiski":
        photo = open('kotr.jpg','rb')
        bot_one.send_photo(message.chat.id, photo, parse_mode='html')
    else:
        bot_one.send_message(message.chat.id, "Напиши еще разочек другое)", parse_mode='html')
        
        
#КНОПКИ
@bot_one.message_handler(commands = ['get_info','info'])
def get_info(message):
    markup_inline = ty.InlineKeyboardMarkup(row_width= 2); #row_width=сколько кнопок в ряд
    itemp1_yes = ty.InlineKeyboardButton(text='Да', callback_data='yes_1')
    itemp2_no = ty.InlineKeyboardButton(text='No', callback_data='no_1')
    itemp3_yes = ty.InlineKeyboardButton(text='Надор подумать', callback_data='yes_2')
    itemp4_yes = ty.InlineKeyboardButton(text='Нет-нет', callback_data='yes_3')
    itemp5_yes = ty.InlineKeyboardButton(text='Воздержусь от ответа)', callback_data='yes_4')
    markup_inline.add(itemp1_yes, itemp2_no, itemp3_yes, itemp4_yes, itemp5_yes)
    bot_one.send_message(message.chat.id,'Хотите задать вопрос?', reply_markup = markup_inline) #текстом и ниже кнопки перечисленные вверху
        
        
bot_one.polling(none_stop=True)
