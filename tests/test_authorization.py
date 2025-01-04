# Test for page https://docs.waifu.im/authorization

import pytest
import requests


def test_get_authorization():
    discord_id: int = 608317829128912907
    params = {'user_id': discord_id, 'permissions':['view_favorites']}
    response = requests.get(url="https://www.waifu.im/authorization", params=params)

    assert response.status_code == 200
