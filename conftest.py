import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()
headers = {
    'x-geo-blocking-bypass': os.getenv('X-GEO-BLOCKING-BYPASS'),
    'Authorization': os.environ['AUTH_TOKEN']
}


@pytest.fixture(scope="class")
def request_get_tags_response(request):
    response = requests.get(url="https://api.waifu.im/tags", headers=headers)
    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_tags_query_full_false_response(request, info=False):
    response = requests.get(url=f"https://api.waifu.im/tags?full={info}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


# Чи можна прокинути зміну info= зі значеннями False/True, щоб юзати лише 1 метод?
@pytest.fixture(scope="class")
def request_get_tags_query_full_true_response(request, info=True):
    response = requests.get(url=f"https://api.waifu.im/tags?full={info}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_tags_query_full_wrong_response(request, info='Wrong'):
    response = requests.get(url=f"https://api.waifu.im/tags?full={info}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_search_random_response(request):
    response = requests.get(url='https://api.waifu.im/search', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request

