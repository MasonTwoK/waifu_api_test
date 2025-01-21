# Tests for page - https://docs.waifu.im/reference/api-reference/search

import pytest
import requests


def test_get_search():
    response = requests.get(url="https://api.waifu.im/search")
    assert response.status_code == 200

    content = response.json()
    assert content is not None
    assert len(content) == 1 # Do we need to check length of content?

    assert len(content['images']) == 1
    assert len(content['images'][0]) == 16

    assert isinstance(content['images'][0]['signature'], str)
    assert isinstance(content['images'][0]['extension'], str)
    assert isinstance(content['images'][0]['image_id'], int)
    assert isinstance(content['images'][0]['favorites'], int)
    assert isinstance(content['images'][0]['dominant_color'], str)
    assert isinstance(content['images'][0]['source'], str)
    assert isinstance(content['images'][0]['artist'], dict) or content['images'][0]['artist'] is None # TODO: Need to investigate behaviour here..
    assert isinstance(content['images'][0]['uploaded_at'], str)
    assert (content['images'][0]['liked_at'] is None) or (isinstance(content['images'][0]['liked_at'], str))  # TODO: Need to investigate behaviour here..
    assert isinstance(content['images'][0]['is_nsfw'], bool)
    assert isinstance(content['images'][0]['width'], int)
    assert isinstance(content['images'][0]['height'], int)
    assert isinstance(content['images'][0]['byte_size'], int)
    assert isinstance(content['images'][0]['url'], str)
    assert isinstance(content['images'][0]['preview_url'], str)

    print()


