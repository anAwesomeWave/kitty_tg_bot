import requests

from log_conf import create_logger


logger = create_logger(__name__, '../logs/utils.log')


def get_random_cat_photo():
    image = None
    logger.debug('Serve new cat photo')
    try:
        image = requests.get(
            'https://api.thecatapi.com/v1/images/search'
        ).json()[0]['url']
    except requests.exceptions.RequestException as err:
        # логи этого
        logger.error('CANT GET PHOTO OF A CAT')
        logger.error(err)
        ...
    return image


def get_info_text():
    return (
        '''
--------------------------------------------        
Этот бот способен растопить сердце каждого ❗
Работа? Учеба? Стресс? МАТАН???
Ответ найден! КОТЫ!
/info - выводит служебную (эту) информацию
/get_cat_photo - выдает случайное фото котэ
/start - запускает бота.
--------------------------------------------
        '''
    )

def get_random_sticker_from_db():
    # TODO
    ...
