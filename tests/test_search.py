# Tests for page - https://docs.waifu.im/reference/api-reference/search

import pytest
import requests

def test_get_search_random():
    auth_token = 'Bearer 8E0O1m-_ebI8TAHe_xlemUmSCvDp0_Ey9sr4TewWq4a1lc_uDf6hr2A-d-oaCXq5_Ta1QPTGZnAMiZZ_nbyjy4zUwY8UVu2cCsGxxaVNEEKEPGB-gPEL7rYhXpy3WDMiZpwyJ36Kdhe8IaLwCqTV8ahTnOx9ArWgezVjIkqRFj0'

    headers = {
        'Authorization': auth_token
    }

    response = requests.get(url="https://api.waifu.im/search", headers=headers)
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


@pytest.mark.skip(reason="TBD")
def test_get_search_single_tag_included():
    response = requests.get(url="https://api.waifu.im/search/?included_tags=maid")
    result = response.json()

    # need a loop to add for searching of type: 'name':'maid' in result['images'][0]['tags']
    # assert result['images'][0]['tags']


@pytest.mark.skip(reason="BUG #2: Request does not require Bearer token")
def test_get_search_random_without_header():
    response = requests.get(url="https://api.waifu.im/search")
    assert response.status_code == 401