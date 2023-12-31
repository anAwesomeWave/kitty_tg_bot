import os
from telegram.ext import Filters, CommandHandler, Updater, MessageHandler
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv

from core.utils import get_random_cat_photo, get_info_text
from core.log_conf import create_logger
import core.analysis_and_statistics as aas
# по угару добавить бд со ввсеми юзерами, которые пользовались когда-либо ботом
# добавлять id стикеров в бд
# на любое сообщение отправлять инфо с подсказками по командам

load_dotenv()

logger = create_logger(__name__, 'bot.log')


def start_bot(update, context):
    chat_id = update.effective_chat.id
    username = update['message']['chat']['username']
    buttons = ReplyKeyboardMarkup([
        ['/info', '/get_cat_photo', '/start']
    ], resize_keyboard=True)

    logger.info(f'New user - [{chat_id}, {username}]')
    if aas.add_user(chat_id, username) == 1:
        logger.error('CANNOT ADD USER TO DATABASE. CHECK db.log FILE.')
    context.bot.send_message(
        # INFO новый чат с юзером {id} и {username}
        chat_id=chat_id,
        text='Спасибо, что выбрали самого эффективного в мире '
             'картинко-кошко-отслылочного бота)'
             '\nмяу!😽',
        reply_markup=buttons
    )
    context.bot.send_sticker(
        chat_id=chat_id,
        sticker='CAACAgUAAxkBAANbZPsscN_uL03H_2v'
                'nJOQdmQy1ohYAAu4BAAKSHShXrArQVp8VXLIwBA'
    )
    send_info(update, context)


def send_info(update, context):
    context.bot.send_message(update.effective_chat.id, get_info_text())


def send_cat_photo(update, context):
    image = get_random_cat_photo()
    if image is None:
        logger.error('error with getting an image of a cat, see "utils" logs"')
    chat_id = update.effective_chat.id
    logger.debug(f'send new photo to {chat_id}')
    context.bot.send_photo(chat_id, image)


def send_all_users(update, context):
    chat_id = update.effective_chat.id
    all_users = aas.get_all_users()
    message = []
    for i, user in enumerate(all_users):
        s = f'{i+1}. {user[0]}-{user[1]}'
        message.append(s)
    message = '\n'.join(message)
    context.bot.send_message(chat_id, message)

def get_id_of_sticker(update, context):
    print(update['message']['sticker']['file_id'])


updater = Updater(token=os.getenv('BOT_API_KEY'))

updater.dispatcher.add_handler(CommandHandler('start', start_bot))
updater.dispatcher.add_handler(CommandHandler('get_cat_photo', send_cat_photo))
updater.dispatcher.add_handler(CommandHandler('info', send_info))
updater.dispatcher.add_handler(CommandHandler('adm_get_all', send_all_users))
# updater.dispatcher.add_handler(CommandHandler('adm_get_five', send_five_users))
updater.dispatcher.add_handler(MessageHandler(Filters.all, send_info))


def serve():
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    updater.dispatcher.add_handler(
        MessageHandler(Filters.sticker, get_id_of_sticker)
    )
    serve()
