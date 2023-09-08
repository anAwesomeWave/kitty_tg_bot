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


def get_random_sticker_from_db():
    # TODO
    ...
