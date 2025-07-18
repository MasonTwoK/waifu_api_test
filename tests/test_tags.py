# Tests for page - https://docs.waifu.im/reference/api-reference/tags

import pytest

from methods import tag_full_info_provider, tag_full_info_comparer
from conftest import request_get_tags_query_full_false_response
from data import tags_full_info, tags_groups, nsfw_tags, versatile_tags


@pytest.mark.tags
class TestGetTags:

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_tags_status_code(self, request_get_tags_response):
        assert request_get_tags_response.status_code == 200, \
            f"Status code {request_get_tags_response.status_code} is not 200"

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_groups_amount(self, request_get_tags_response):
        assert len(request_get_tags_response.data) == 2, 'Tags group amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name", tags_groups)
    def test_get_tags_groups_presence(self, request_get_tags_response, group_name):
        assert group_name in request_get_tags_response.data, f'{group_name} tags group is missing'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name, amount", (
            pytest.param('versatile', 9, id='versatile'),
            pytest.param('nsfw', 7, id='nsfw')
    ))
    def test_get_tags_in_group_amount(self, request_get_tags_response, group_name, amount):
        assert len(request_get_tags_response.data[group_name]) == amount, 'Amount of versatile group tags is not 9'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("versatile_tag", versatile_tags)
    def test_get_tags_contains_versatile_tags(self, request_get_tags_response, versatile_tag):
        assert versatile_tag in request_get_tags_response.data['versatile'], \
            f'{versatile_tag} tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("nsfw_tag", nsfw_tags)
    def test_get_tags_contains_nsfw_tags(self, request_get_tags_response, nsfw_tag):
        assert nsfw_tag in request_get_tags_response.data['nsfw'], f'{nsfw_tag} tag is not present in nsfw group'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.xfail(reason="Чому так, воно видає помилку? Проблема порядку?")
    def test_get_tags_contains_maid_and_oppai(self, request_get_tags_response):
        assert ['maid', 'oppai'] in request_get_tags_response.data['versatile'], \
            'maid & oppai tags are not present in versatile group'


class TestGetTagsFullInfoFalse:

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_status_code(self, request_get_tags_query_full_false_response):
        assert request_get_tags_query_full_false_response.status_code == 200, \
            f"Status code {request_get_tags_query_full_false_response.status_code} is not 200"

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_groups_amount(self, request_get_tags_query_full_false_response):
        assert len(request_get_tags_query_full_false_response.data) == 2, 'Tags group amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name", tags_groups)
    def test_get_tags_query_full_false_groups_presence(self, request_get_tags_query_full_false_response, group_name):
        assert group_name in request_get_tags_query_full_false_response.data, f'{group_name} tags group is missing'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name, amount", [
        pytest.param("nsfw", 7, id='nsfw'),
        pytest.param("versatile", 9, id='versatile')
    ])
    def test_get_tags_query_full_false_in_group_amount(self,
                                                       request_get_tags_query_full_false_response, group_name, amount):
        assert len(request_get_tags_query_full_false_response.data[group_name]) == amount, \
            f'Tags group {group_name} amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("versatile_tag", versatile_tags)
    def test_get_tags_query_full_false_contains_in_versatile(self,
                                                             request_get_tags_query_full_false_response, versatile_tag):
        assert versatile_tag in request_get_tags_query_full_false_response.data['versatile'], \
            f'{versatile_tag} tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("nsfw_tag", nsfw_tags)
    def test_get_tags_query_full_false_contains_in_nsfw(self,
                                                        request_get_tags_query_full_false_response, nsfw_tag):
        assert nsfw_tag in request_get_tags_query_full_false_response.data['nsfw'], \
            f'{nsfw_tag} tag is not present in nsfw group'


class TestGetTagsFullInfoTrue:

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_true_status_code(self, request_get_tags_query_full_true_response):
        assert request_get_tags_query_full_true_response.status_code == 200, \
            f'Status code {request_get_tags_query_full_true_response.status_code} is not 200'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_true_groups_amount(self, request_get_tags_query_full_true_response):
        assert len(request_get_tags_query_full_true_response.data) == 2, 'Tags group amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name", tags_groups)
    def test_get_tags_query_full_true_groups_presence(self, request_get_tags_query_full_true_response, group_name):
        assert group_name in request_get_tags_query_full_true_response.data, f'{group_name} is not present'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_tag, amount", [
        pytest.param('nsfw',  7, id='nsfw'),
        pytest.param('versatile', 9, id='versatile')
    ])
    def test_get_tags_query_full_true_amount_of_tags_in_group(self, request_get_tags_query_full_true_response,
                                                              group_tag, amount):
        assert len(request_get_tags_query_full_true_response.data[group_tag]) == amount, \
            f'Amount of {group_tag} tags is not {amount}'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_full_info", tags_full_info)
    def test_get_tags_query_full_true_contains_info(self, tag_full_info, request_get_tags_query_full_true_response):
        assert tag_full_info_comparer(request_get_tags_query_full_true_response.data, tag_full_info), \
            f"{tag_full_info['name']} tag has incorrect full info"

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_full_info", tags_full_info)
    def test_get_tags_query_full_true_tags_info_size(self, tag_full_info, request_get_tags_query_full_true_response):
        assert len(tag_full_info_provider(request_get_tags_query_full_true_response.data, tag_full_info)) == 4, \
            f"{tag_full_info['name']} info fields don't equal 4"
