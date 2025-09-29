# Tests for page - https://docs.waifu.im/reference/api-reference/search

import pytest
import requests
from utils import tag_randomizer, tags_comparer, search_data_type_checker, search_orientation_provider
from data import search_random_fields_name, search_random_fields_name_or_none, search_random_fields_name_tags


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_random
class TestGetSearchRandom:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_search_random_img_status_code(self, request_get_search_random):
        assert request_get_search_random.status_code == 200, "Status code is not 200"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_search_random_img_property_single(self, request_get_search_random):
        assert len(request_get_search_random.data) == 1, 'Response data contains only one name value pair'

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_random_img_single(self, request_get_search_random):
        assert len(request_get_search_random.data['images']) == 1, "Random search contains more than single image"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_random_img_param_amount(self, request_get_search_random):
        assert len(request_get_search_random.image) == 16, 'Amount of parameters is not 16'

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    @pytest.mark.parametrize("field_name, data_type", search_random_fields_name)
    def test_get_search_random_img_fields_data_type(self, request_get_search_random, field_name, data_type):
        assert search_data_type_checker(request_get_search_random.image[field_name], data_type), \
            f"Property '{field_name}' data type is not {data_type}"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    @pytest.mark.parametrize("field_name, data_type", search_random_fields_name_or_none)
    def test_get_search_random_img_fields_data_type_or_none(self, request_get_search_random, field_name, data_type):
        assert search_data_type_checker(
            request_get_search_random.image[field_name], data_type, possible_none=True), \
            f"Property '{field_name}' data type is not {data_type}"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_random_img_param_is_nsfw_default(self, request_get_search_random):
        assert request_get_search_random.image['is_nsfw'] is False, "Image is not nsfw"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    @pytest.mark.parametrize("field_name, data_type", search_random_fields_name_tags)
    def test_search_random_img_fields_name_tags_data_type(self, request_get_search_random, field_name, data_type):
        assert search_data_type_checker(request_get_search_random.image_tag_info[field_name], data_type), \
            f"Tag property '{field_name}' data type is not {data_type}"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_random_img_field_tags_param_is_nsfw_false(self, request_get_search_random):
        assert request_get_search_random.image_tag_info['is_nsfw'] is False, "Parameter is_nsfw is not False by default"


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_included_tags
class TestGetSearchQueryIncludedTags:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_search_query_included_tags_status_code(self, request_get_search_query_included_tags):
        assert request_get_search_query_included_tags.status_code == 200, "Status code is not 200"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_query_included_tags_body(self, request_get_search_query_included_tags):
        assert tags_comparer(request_get_search_query_included_tags.tag_name,
                             request_get_search_query_included_tags.data), \
            f'Tag {request_get_search_query_included_tags.tag_name} is not present for image'


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_excluded_tags
class TestGetSearchQueryExcludedTags:
    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_search_query_excluded_tags_status_code(self, request_get_search_query_excluded_tags):
        assert request_get_search_query_excluded_tags.status_code == 200, "Status code is not 200"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_query_excluded_tags_body(self, request_get_search_query_excluded_tags):
        assert not tags_comparer(request_get_search_query_excluded_tags.tag_name,
                                 request_get_search_query_excluded_tags.data), \
            f"{request_get_search_query_excluded_tags.tag_name} is present in response"


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_included_files
class TestGetSearchQueryIncludedFiles:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.search_query_included_files
    @pytest.mark.status_code
    def test_get_search_query_included_files_status_code(self, request_get_search_query_included_files):
        assert request_get_search_query_included_files.status_code == 200, 'Status code is not 200'

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.search_query_included_files
    @pytest.mark.response_body
    def test_get_search_query_included_files_body(self, request_get_search_query_included_files):
        assert (request_get_search_query_included_files.data['images'][0]['image_id'] ==
                request_get_search_query_included_files.file_id), \
            f'File id is not {request_get_search_query_included_files.file_id}'


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_excluded_files
class TestGetSearchQueryExcludeFiles:
    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.search_query_excluded_files
    @pytest.mark.status_code
    def test_get_search_query_exclude_files_status_code(self, request_get_search_query_excluded_files):
        assert request_get_search_query_excluded_files.status_code == 200, 'Status code is not 200'

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.search_query_excluded_files
    @pytest.mark.response_body
    def test_get_search_query_exclude_files_body(self, request_get_search_query_excluded_files):
        assert (request_get_search_query_excluded_files.data['images'][0]['image_id'] !=
                request_get_search_query_excluded_files.file_id), \
            f'File id is {request_get_search_query_excluded_files.file_id}'


# TODO: Can be optimized with replace main logic to utils.py
@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_is_nsfw
@pytest.mark.query_param('false')
class TestGetSearchQueryIsNsfwFalse:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_search_is_nsfw_true_status_code(self, request_get_search_query_is_nsfw):
        assert request_get_search_query_is_nsfw.status_code == 200, 'Status code is not 200'

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_is_nsfw_true(self, request_get_search_query_is_nsfw):
        assert request_get_search_query_is_nsfw.image['is_nsfw'] is False, 'is_nsfw parameter is not False'


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_is_nsfw
@pytest.mark.query_param('true')
class TestGetSearchQueryIsNsfwTrue:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_search_is_nsfw_true_status_code(self, request_get_search_query_is_nsfw):
        assert request_get_search_query_is_nsfw.status_code == 200, 'Status code is not 200'

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_is_nsfw_true(self, request_get_search_query_is_nsfw):
        assert request_get_search_query_is_nsfw.image['is_nsfw'] is True, 'is_nsfw parameter is not True'


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_gif
@pytest.mark.query_param('False')
class TestGetSearchQueryGifFalse:
    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_search_query_gif_false_status_code(self, request_get_search_query_gif):
        assert request_get_search_query_gif.status_code == 200, "Status code is not 200"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_search_query_gif_false_param(self, request_get_search_query_gif):
        assert request_get_search_query_gif.image_extension != '.gif', "Extension parameter is .gif"


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_gif
@pytest.mark.query_param('True')
class TestGetSearchQueryGifTrue:
    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_search_gif_true_status_code(self, request_get_search_query_gif):
        assert request_get_search_query_gif.status_code == 200, 'Status code is not 200'

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_search_query_gif_true_param(self, request_get_search_query_gif):
        assert request_get_search_query_gif.image_extension == '.gif', "Image extension is not equal .gif"


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_orientation
class TestGetSearchQueryOrientation:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.search_query_orientation
    @pytest.mark.status_code
    def test_get_search_query_orientation_status_code(self, request_get_search_query_orientation):
        assert request_get_search_query_orientation.status_code == 200, "Status code is not 200"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.search_query_orientation
    @pytest.mark.response_body
    def test_get_search_query_orientation_body(self, request_get_search_query_orientation):
        assert request_get_search_query_orientation.orientation in search_orientation_provider(
            request_get_search_query_orientation.data), \
            f"Picture is not {request_get_search_query_orientation.orientation}"


@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_full
@pytest.mark.query_param('False')
class TestGetSearchQueryFullFalse:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_search_query_full_false_status_code(self, request_get_search_query_full):
        assert request_get_search_query_full.status_code == 200, "Status code is not 200"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_query_full_false_is_nsfw_param(self, request_get_search_query_full):
        assert request_get_search_query_full.image['is_nsfw'] is False, "Image parameter is_nsfw is not False"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_query_full_false_field_tags_param_is_nsfw_false(self, request_get_search_query_full):
        assert request_get_search_query_full.image_tag_info['is_nsfw'] is False, \
            "Parameter is_nsfw in tags field is not False"


# TODO: Redo conftest methods which reach objects inside json() since in error code case this objects won`t initialize!
@pytest.mark.skip(reason="To remove in negative scenarios section")
@pytest.mark.search
@pytest.mark.positive
@pytest.mark.search_query_full
@pytest.mark.query_param('True')
class TestGetSearchQueryFullTrue:

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_search_query_full_true_status_code(self, request_get_search_query_full):
        assert request_get_search_query_full.status_code == 401, "Status code is not 401"

    @pytest.mark.search
    @pytest.mark.positive
    @pytest.mark.response_body
    def test_get_search_query_full_true_param(self, request_get_search_query_full):
        assert request_get_search_query_full.data['detail'] == "Missing or malformed token", \
            "Image parameter is_nsfw is not True"


class TestCasesNegative:
    @pytest.mark.skip(reason="BUG #2: Request does not require Bearer token")
    def test_get_search_random_without_header(self):
        response = requests.get(url="https://api.waifu.im/search")
        assert response.status_code == 401

    @pytest.mark.skip(reason="BUG #4: Get search returns random tag while to similar included tags requested added")
    def test_get_search_same_multiple_tag_included(self):
        random_tag = tag_randomizer()

        response = requests.get(url=f"https://api.waifu.im/search/?{random_tag}&{random_tag}")
        assert response.status_code == 200, 'Wrong status code returned.'

        content = response.json()
        assert tags_comparer(tag=random_tag, content=content)
