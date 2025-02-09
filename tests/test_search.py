# Tests for page - https://docs.waifu.im/reference/api-reference/search

import pytest
import requests
import random

url="https://api.waifu.im/search"
auth_token = 'Bearer 8E0O1m-_ebI8TAHe_xlemUmSCvDp0_Ey9sr4TewWq4a1lc_uDf6hr2A-d-oaCXq5_Ta1QPTGZnAMiZZ_nbyjy4zUwY8UVu2cCsGxxaVNEEKEPGB-gPEL7rYhXpy3WDMiZpwyJ36Kdhe8IaLwCqTV8ahTnOx9ArWgezVjIkqRFj0'

def tag_randomizer():
    list_of_tags = []

    response = requests.get(url='https://api.waifu.im/tags')
    content = response.json()

    for i in range(len(list(content))):
        list_of_tags += list(content.values())[i]  # Is there something wrong about it https://www.geeksforgeeks.org/python-select-random-value-from-a-list/?

    return random.choice(list_of_tags)


def tags_comparer(tag, content):
    for element in content['images'][0]['tags']:
        if element['name'] == tag:
            return True
    return False


def test_get_search_random():

    headers = {'Authorization': auth_token}

    response = requests.get(url=url, headers=headers)
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


def test_search_is_nsfw_false_by_default():
    headers = {'Authorization': auth_token}

    for test in range(5):
        response = requests.get(url=url, headers=headers)
        assert response.status_code == 200

        content = response.json()
        assert content['images'][0]['is_nsfw'] == False


def test_get_search_single_tag_included():
    random_tag = tag_randomizer()
    response = requests.get(url=f"https://api.waifu.im/search/?included_tags={random_tag}")
    content = response.json()

    assert tags_comparer(random_tag, content), 'Tags are not equal.'


@pytest.mark.skip(reason="BUG #2: Request does not require Bearer token")
def test_get_search_random_without_header():
    response = requests.get(url="https://api.waifu.im/search")
    assert response.status_code == 401
