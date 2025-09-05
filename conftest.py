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
def request_get_tags(request):
    response = requests.get(url="https://api.waifu.im/tags", headers=headers)
    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_tags_query_full_false(request, info=False):
    response = requests.get(url=f"https://api.waifu.im/tags?full={info}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


# Чи можна прокинути зміну info= зі значеннями False/True, щоб юзати лише 1 метод?
@pytest.fixture(scope="class")
def request_get_tags_query_full_true(request, info=True):
    response = requests.get(url=f"https://api.waifu.im/tags?full={info}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_tags_query_full_wrong(request, info='Wrong'):
    response = requests.get(url=f"https://api.waifu.im/tags?full={info}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_search_random(request):
    response = requests.get(url='https://api.waifu.im/search', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()
    request.image = response.json()['images'][0]
    request.image_tag_info = response.json()['images'][0]['tags'][0]

    yield request


@pytest.fixture()
def request_get_search_query_full_false(request, is_nsfw=False):
    response = requests.get(url=f"https://api.waifu.im/search?is_nsfw={is_nsfw}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()
    request.image = response.json()['images'][0]

    yield request

