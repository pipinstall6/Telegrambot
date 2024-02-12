import os
from telebot import TeleBot
from dotenv import load_dotenv
data = load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TeleBot()


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user}Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"Hi {message.from_user}, what's up")

if __name__ == "__main__":
    bot.infinity_polling()
