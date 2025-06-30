import pytest
import requests


@pytest.fixture(scope="class")
def request_get_tags_response():
    response = requests.get(url="https://api.waifu.im/tags")
    yield response


@pytest.fixture(scope="class")
def request_get_tags_query_full_false_response():
    response = requests.get(url=f"https://api.waifu.im/tags?full=false")
    yield response
