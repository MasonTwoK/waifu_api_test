import pytest
import requests
import os
from dotenv import load_dotenv
from utils import query_bool_param_provider
from data import full_info_tag_names

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
def request_get_tags_query_full(request):
    info = query_bool_param_provider(parameter=request.node.get_closest_marker('query_param').args[0])
    response = requests.get(url=f"https://api.waifu.im/tags?full={info}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


# TODO: Redo conftest methods which reach objects inside json() since in error code case this objects won`t initialize!
@pytest.fixture(scope="class")
def request_get_search_random(request):
    response = requests.get(url='https://api.waifu.im/search', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()
    request.image = response.json()['images'][0]
    request.image_tag_info = response.json()['images'][0]['tags'][0]

    yield request


# The way of implementation https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-parametrize
@pytest.fixture(params=full_info_tag_names)
def request_get_search_query_included_tags(request):
    tag_names = request.param
    response = requests.get(url=f"https://api.waifu.im/search?included_tags={tag_names}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_full(request):
    full = query_bool_param_provider(request.node.get_closest_marker('query_param').args[0])
    response = requests.get(url=f"https://api.waifu.im/search?full={full}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()
    request.image = response.json()['images'][0]
    request.image_tag_info = response.json()['images'][0]['tags'][0]

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_gif(request):
    gif = query_bool_param_provider(request.node.get_closest_marker('query_param').args[0])
    response = requests.get(url=f'https://api.waifu.im/search?gif={gif}', headers=headers)

    request.status_code = response.status_code
    request.image_extension = response.json()['images'][0]['extension']

    yield request


@pytest.fixture()
def request_get_search_query_is_nsfw(request):
    nsfw = request.node.get_closest_marker('query_param').args[0]
    response = requests.get(url=f'https://api.waifu.im/search?is_nsfw={nsfw}', headers=headers)

    request.status_code = response.status_code
    request.image = response.json()['images'][0]

    yield request
