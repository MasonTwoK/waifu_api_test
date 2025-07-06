import pytest
import requests


@pytest.fixture(scope="class")
def request_get_tags_response(request):
    response = requests.get(url="https://api.waifu.im/tags")

    request.status_code = response.status_code
    request.data = response.json()

    yield request


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