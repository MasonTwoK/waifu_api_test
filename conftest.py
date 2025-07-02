import pytest
import requests


@pytest.fixture(scope="class")
def request_get_tags_response():
    response = requests.get(url="https://api.waifu.im/tags")
    data = response.json()

    yield response.status_code, data


@pytest.fixture(scope="class")
def request_get_tags_query_full_false_response():
    response = requests.get(url="https://api.waifu.im/tags?full=false")
    data = response.json()

    yield response.status_code, data


# Чи можна прокинути зміну param= зі значеннями False/True щоб юзати лише 1 метод?
@pytest.fixture(scope="class")
def request_get_tags_query_full_true_response():
    response = requests.get(url="https://api.waifu.im/tags?full=false")
    data = response.json()

    yield response.status_code, data
