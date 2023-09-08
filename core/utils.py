import logging

import requests


def get_random_cat_photo():
    image = None
    try:
        image = requests.get(
            'https://api.thecatapi.com/v1/images/search'
        ).json()[0]['url']
    except requests.exceptions.RequestException:
        # логи этого
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
