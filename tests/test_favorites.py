# Tests for page - https://docs.waifu.im/reference/api-reference/favorites

import pytest
import requests
import os


@pytest.mark.skip(reason="TBD. Q: How to put pictures in favorite?")
def test_get_favorites():

    auth_token = os.environ.get('auth_token')  # How to get a token https://docs.waifu.im/authorization
    headers = {
        'Accept-Version': 'v5',
        'Authorization': f'Bearer {auth_token}'
    }

    response = requests.get(url="https://api.waifu.im/fav", headers=headers)
    assert response.status_code == 404
    print()
