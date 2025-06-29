import pytest
import requests


@pytest.fixture(scope="class")
def request_get_tags_response():
    response = requests.get(url="https://api.waifu.im/tags")
    yield response
