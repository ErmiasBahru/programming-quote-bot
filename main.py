from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
import requests

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


reply_keyboard = [['/random']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Type /random to get a new quote everytime!", reply_markup=markup)


def get_random_quote(update, context):
    resp = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = resp.json()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=data['quote'])


if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    quote_handler = CommandHandler('random', get_random_quote)
    dispatcher.add_handler(quote_handler)

    updater.start_polling()
