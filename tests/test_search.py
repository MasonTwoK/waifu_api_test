# Tests for page - https://docs.waifu.im/reference/api-reference/search

import pytest
import requests
import os
from utils import tag_randomizer, tags_comparer
from data import search_random_fields_name, search_random_fields_name_or_none


url = "https://api.waifu.im/search"
auth_token = os.environ['AUTH_TOKEN']  # How to get a token https://docs.waifu.im/authorization
headers = {'Authorization': auth_token}


class TestGetSearch:
    def test_get_search_random_img_status_code(self, request_get_search_random_response):
        assert request_get_search_random_response.status_code == 200, "Status code is not 200"

    def test_search_random_img_property_single(self, request_get_search_random_response):
        assert len(request_get_search_random_response.data) == 1, \
            'Response data contains only one name value pair'

    def test_get_search_random_img_single(self, request_get_search_random_response):
        assert len(request_get_search_random_response.data['images']) == 1, \
            "Random search contains more than single image"

    def test_get_search_random_img_param_amount(self, request_get_search_random_response):
        assert len(request_get_search_random_response.image) == 16, \
            'Amount of parameters is not 16'

    @pytest.mark.parametrize("field_name, data_type", search_random_fields_name)
    def test_get_search_random_img_fields_data_type(self, request_get_search_random_response, field_name, data_type):
        assert isinstance(request_get_search_random_response.image[field_name], data_type), \
            f"Property '{field_name}' data type is not {data_type}"

    @pytest.mark.parametrize("field_name, data_type", search_random_fields_name_or_none)
    def test_get_search_random_img_fields_data_type_or_none(self, request_get_search_random_response,
                                                            field_name, data_type):
        assert (
            # TODO: Need to investigate behaviour below..
            isinstance(request_get_search_random_response.image[field_name], data_type) or
            request_get_search_random_response.image[field_name] is None
        )

    def test_get_search_random_img_param_is_nsfw_default(self, request_get_search_random_response):
        assert request_get_search_random_response.image['is_nsfw'] is False, "Image is not nsfw"


class TestCasesPositive:
    def test_get_search_single_tag_included(self):
        random_tag = tag_randomizer()

        response = requests.get(url=f"https://api.waifu.im/search/?included_tags={random_tag}", headers=headers)
        assert response.status_code == 200

        content = response.json()
        assert tags_comparer(tag=random_tag, content=content), 'Included tag is not present.'

    @pytest.mark.skip(reason="BUG #3: Get search does not return picture with multiple searched tags. Repro rate 50%")
    def test_get_search_multiple_tag_included(self):
        random_tag_1 = tag_randomizer()
        random_tag_2 = tag_randomizer()

        response = requests.get(url=f"https://api.waifu.im/search/?included_tags={random_tag_1}&{random_tag_2}")
        assert response.status_code == 200, 'Wrong status code'

        content = response.json()
        assert tags_comparer(random_tag_1, content)
        assert tags_comparer(random_tag_2, content)

    @pytest.mark.skip(reason='BUG #5: Need to be fixed')
    def test_get_search_single_tag_excluded(self):
        random_tag = tag_randomizer()

        response = requests.get(url=f'https://api.waifu.im/search/?{random_tag}', headers=headers)
        assert response.status_code == 200, 'Wrong status code'

        content = response.json()
        assert not tags_comparer(tag=random_tag, content=content), 'Image returned with excluded tag.'

    @pytest.mark.skip(reason='BUG #6: Fails time to time. Need to be fixed')
    def test_get_search_multiple_tag_excluded(self):
        random_tag_1 = tag_randomizer()
        random_tag_2 = tag_randomizer()

        response = requests.get(url=f"{url}/?excluded_tags={random_tag_1}&{random_tag_2}", headers=headers)
        assert response.status_code == 200

        content = response.json()
        assert not tags_comparer(tag=random_tag_1, content=content), f'Excluded tag - {random_tag_1} is present'
        assert not tags_comparer(tag=random_tag_2, content=content), f'Excluded tag - {random_tag_2} is present'


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
