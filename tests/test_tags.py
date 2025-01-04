# Tests for page - https://docs.waifu.im/reference/api-reference/tags

import pytest
import requests


def test_get_tags():
    response = requests.get(url="https://api.waifu.im/tags")
    assert response.status_code == 200
