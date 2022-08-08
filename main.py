import telebot
from token_info import token

bot = telebot.TeleBot(token)

@bot.message_handler()
def start(message:telebot.types.Message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()