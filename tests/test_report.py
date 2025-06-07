# Tests for page - https://docs.waifu.im/reference/api-reference/report

import pytest
import requests


@pytest.mark.skip(reason="BUG #1: Error 400. User is enable to create a report")
def test_post_report():
    # auth_token =  # How to get a token https://docs.waifu.im/authorization
    headers = {
        'Accept-Version': 'v5',
        'Authorization': auth_token,
        'Content-Type': 'application/json',
    }

    data = {
        'image_id': 8008,
        'description': 'Lol'
    }

    response = requests.post(url="https://api.waifu.im/report", headers=headers, data=data)
    assert response.status_code == 200
