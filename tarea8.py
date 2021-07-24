import os
import telebot

bot=telebot.TeleBot('1946430175:AAE78gZ6rjHw3XvwWkL6Q_wfV3JrDSGO3bI')

@bot.message_handler(commands=['kelvin'])

def kelvin(m):
    cid=m.chat.id
    bot.send_photo(cid,open('celcius-a-kelvin.jpg','rb'))

@bot.message_handler(commands=['celcius'])

def celcius(m):
    cid=m.chat.id
    bot.send_photo(cid,open('kelvin-a-celcius.jpg','rb'))

bot.polling()