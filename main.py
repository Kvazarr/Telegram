import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot('6351529503:AAEibhaANITRmYvu3w3VgS-g8KQ5v65nKrk')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
                 
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()