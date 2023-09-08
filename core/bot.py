import os
import logging

from telegram.ext import Filters, CommandHandler, Updater, MessageHandler
from dotenv import load_dotenv

from utils import get_random_cat_photo

# по угару добавить бд со ввсеми юзерами, которые пользовались когда-либо ботом
# добавлять id стикеров в бд
# на любое сообщение отправлять инфо с подсказками по командам

load_dotenv()


def start_bot(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        # INFO новый чат с юзером {id} и {username}
        chat_id=chat_id,
        text='Спасибо, что выбрали самого эффективного в мире '
             'картинко-кошко-отслылочного бота)'
             '\nмяу!😽'
    )
    context.bot.send_sticker(
        chat_id=chat_id,
        sticker='CAACAgUAAxkBAANbZPsscN_uL03H_2v'
                'nJOQdmQy1ohYAAu4BAAKSHShXrArQVp8VXLIwBA'
    )


def send_cat_photo(update, context):
    image = get_random_cat_photo()
    if image is None:
        ...
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id, image)


def get_id_of_sticker(update, context):
    print(update['message']['sticker']['file_id'])


updater = Updater(token=os.getenv('BOT_API_KEY'))


updater.dispatcher.add_handler(CommandHandler('start', start_bot))
updater.dispatcher.add_handler(CommandHandler('get_cat_photo', send_cat_photo))


if __name__ == '__main__':
    updater.dispatcher.add_handler(
        MessageHandler(Filters.sticker, get_id_of_sticker)
    )

updater.start_polling()
updater.idle()
