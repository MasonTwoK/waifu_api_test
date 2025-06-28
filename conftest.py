import pytest
import requests


@pytest.fixture(scope='function')
def request_get_tags_status_code():
    response = requests.get(url="https://api.waifu.im/tags")
    yield response.status_code


@pytest.fixture(scope="class")
def request_get_tags_response_data():
    response = requests.get(url="https://api.waifu.im/tags")
    yield response.json()

