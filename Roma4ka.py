import telebot
from requests import get

bot = telebot.TeleBot("5224049167:AAEYm1h5w4hJRH9rgRJ3M9iHbzCimnFKCsA")

@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id, "Иди нахуй")
  bot.send_photo(message.chat.id, get("https://image.rakuten.co.jp/asr/cabinet/watch68/rk-av0006l_12.jpg").content)

bot.polling()