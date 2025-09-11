import pytest
import requests
import os
from dotenv import load_dotenv
from utils import query_bool_param_provider

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


@pytest.fixture(scope="class")
def request_get_search_query_full_false(request, full=False):
    response = requests.get(url=f"https://api.waifu.im/search?full={full}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()
    request.image = response.json()['images'][0]
    request.image_tag_info = response.json()['images'][0]['tags'][0]

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_full_true(request, full=True):
    response = requests.get(url=f"https://api.waifu.im/search?full={full}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()
    request.image = response.json()['images'][0]

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_gif_false(request, gif=False):
    response = requests.get(url=f"https://api.waifu.im/search?gif={gif}", headers=headers)

    request.status_code = response.status_code
    request.image_extension = response.json()['images'][0]['extension']

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_gif(request):
    gif = query_bool_param_provider(request.node.get_closest_marker('query_gif').args[0])
    response = requests.get(url=f'https://api.waifu.im/search?gif={gif}', headers=headers)

    request.status_code = response.status_code
    request.image_extension = response.json()['images'][0]['extension']

    yield request
