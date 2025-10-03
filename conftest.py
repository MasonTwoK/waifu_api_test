import pytest
import requests
import os
from dotenv import load_dotenv
from utils import query_bool_param_provider, search_image_id_provider
from data import full_info_tag_names, search_excluded_tags, search_query_size_operators

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
@pytest.fixture(scope="class", params=full_info_tag_names)
def request_get_search_query_included_tags(request):
    tag_name = request.param
    response = requests.get(url=f"https://api.waifu.im/search?included_tags={tag_name}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.tag_name = tag_name

    yield request


@pytest.fixture(scope="class", params=search_excluded_tags)
def request_get_search_query_excluded_tags(request):
    tag_name = request.param
    response = requests.get(url=f"https://api.waifu.im/search?excluded_tags={tag_name}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.tag_name = tag_name

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_included_files(request):
    file_id = search_image_id_provider()
    response = requests.get(url=f"https://api.waifu.im/search?included_files={file_id}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.file_id = file_id

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_excluded_files(request):
    file_id = search_image_id_provider()
    response = requests.get(url=f"https://api.waifu.im/search?excluded_files={file_id}", headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.file_id = file_id

    yield request


@pytest.fixture(scope="class", params=[True, False])
def request_get_search_query_is_nsfw(request):
    nsfw = request.param
    response = requests.get(url=f'https://api.waifu.im/search?is_nsfw={nsfw}', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.nsfw_state = nsfw

    yield request


@pytest.fixture(scope="class")
def request_get_search_query_gif(request):
    gif = query_bool_param_provider(request.node.get_closest_marker('query_param').args[0])
    response = requests.get(url=f'https://api.waifu.im/search?gif={gif}', headers=headers)

    request.status_code = response.status_code
    request.image_extension = response.json()['images'][0]['extension']

    yield request


@pytest.fixture(scope="class", params=['FAVORITES', 'UPLOADED_AT', 'RANDOM'])
def request_get_search_order_by(request):
    order_by = request.param
    response = requests.get(url=f'https://api.waifu.im/search?order_by={order_by}', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.order_by = order_by

    yield request


@pytest.fixture(scope="class", params=['PORTRAIT', 'LANDSCAPE', 'RANDOM'])
def request_get_search_query_orientation(request):
    orientation = request.param
    response = requests.get(url=f'https://api.waifu.im/search?orientation={orientation}', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.orientation = orientation

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


@pytest.fixture(scope="class", params=search_query_size_operators)
def request_get_search_query_width(request):
    operator = request.param
    size = 1000
    response = requests.get(url=f'https://api.waifu.im/search?width{operator}{size}', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.operator = operator
    request.size = size

    yield request


@pytest.fixture(scope="class", params=search_query_size_operators)
def request_get_search_query_height(request):
    size = 1000
    operator = request.param
    response = requests.get(url=f'https://api.waifu.im/search?width{operator}{size}', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()

    request.operator = operator
    request.size = size

    yield request


@pytest.fixture(scope="class", params=search_query_size_operators)
def request_get_search_query_bite_size(request):
    size = 1000
    operator = request.param
    response = requests.get(url=f'https://api.waifu.im/search?bite_size{operator}{size}', headers=headers)

    request.status_code = response.status_code
    request.data = response.json()
    request.size = size
    request.operator = operator

    yield request
