import pytest
from core.utils import get_random_cat_photo


def test_photo_returning():
    img = get_random_cat_photo()
    assert isinstance(img, str) is True
