import pytest
import requests


@pytest.fixture(scope="class")
def request_get_tags_response(request):
    response = requests.get(url="https://api.waifu.im/tags")

    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_tags_query_full_false_response(request, param=False):
    response = requests.get(url=f"https://api.waifu.im/tags?full={param}")

    request.status_code = response.status_code
    request.data = response.json()

    yield request


# Чи можна прокинути зміну param= зі значеннями False/True, щоб юзати лише 1 метод?
@pytest.fixture(scope="class")
def request_get_tags_query_full_true_response(request, param=True):
    response = requests.get(url=f"https://api.waifu.im/tags?full={param}")

    request.status_code = response.status_code
    request.data = response.json()

    yield request
