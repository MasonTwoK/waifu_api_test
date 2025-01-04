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

    assert isinstance(content['images'][0]['byte_size'], int)
    assert isinstance(content['images'][0]['dominant_color'], str)
    assert isinstance(content['images'][0]['extension'], str)
    assert isinstance(content['images'][0]['favorites'], int)
    assert isinstance(content['images'][0]['height'], int)
    assert isinstance(content['images'][0]['image_id'], int)
    assert isinstance(content['images'][0]['is_nsfw'], bool)
    assert (content['images'][0]['liked_at'] is None) or (isinstance(content['images'][0]['is_nsfw'], str))
    assert isinstance(content['images'][0]['signature'], str)
    assert isinstance(content['images'][0]['source'], str)

    assert isinstance(content['images'][0]['artist'], dict) or content['images'][0]['artist'] is None
    assert len(content['images'][0]['artist']) == 6
    assert isinstance(content['images'][0]['artist']['artist_id'], int)
    assert isinstance(content['images'][0]['artist']['deviant_art'], str) or content['images'][0]['artist']['deviant_art'] is None
    assert isinstance(content['images'][0]['artist']['name'], str)
    assert isinstance(content['images'][0]['artist']['patreon'], str) or content['images'][0]['artist']['patreon'] is None
    assert isinstance(content['images'][0]['artist']['pixiv'], str)
    assert isinstance(content['images'][0]['artist']['twitter'], str)

    assert isinstance(content['images'][0]['tags'], list)
    assert len(content['images'][0]['tags']) == 4
    assert isinstance(content['images'][0]['tags'][0]['tag_id'], int)
    assert isinstance(content['images'][0]['tags'][0]['name'], str)
    assert isinstance(content['images'][0]['tags'][0]['description'], str)
    assert isinstance(content['images'][0]['tags'][0]['is_nsfw'], bool)
