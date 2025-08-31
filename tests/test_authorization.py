# Test for page https://docs.waifu.im/authorization

import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def test_get_authorization():
    # How to get ID: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID
    discord_id = os.environ['discord_id']
    params = {'user_id': discord_id, 'permissions': ['view_favorites']}
    response = requests.get(url="https://www.waifu.im/authorization", params=params)

    assert response.status_code == 200
