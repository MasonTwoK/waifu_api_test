# Tests for page - https://docs.waifu.im/reference/api-reference/tags

import pytest
import requests

from methods import tag_full_info_provider
from conftest import request_get_tags_query_full_false_response


@pytest.mark.tags
class TestGetTags:

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_tags_status_code(self, request_get_tags_response):
        status_code, data = request_get_tags_response
        assert status_code == 200, "Status code is not 200"

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_groups_amount(self, request_get_tags_response):
        status_code, data = request_get_tags_response
        assert len(data) == 2, 'Tags group amount is wrong'

    tags_groups = ['versatile', 'nsfw']

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name", tags_groups)
    def test_get_tags_groups_presence(self, request_get_tags_response, group_name):
        status_code, data = request_get_tags_response
        assert group_name in data, f'{group_name} tags group is missing'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_group_versatile_amount(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert len(data['versatile']), 'Amount of versatile group tags is not 9'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_maid(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'maid' in data['versatile'], \
            'maid tag is not present in versatile group'
        assert tag_contains('maid', data['versatile']), \
            'maid tag is not present in versatile group'  # Яка різниця з попереднім рядком?

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.xfail(reason="Чому так, воно видає помилку? Проблема порядку?")
    def test_get_tags_contains_maid_and_oppai(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert ['maid', 'oppai'] in data['versatile'], \
            'maid & oppai tags are not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_waifu(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'waifu' in data['versatile'], \
            'waifu tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_marin_kitagawa(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'marin-kitagawa' in data['versatile'], \
            'marin-kitagawa tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_mori_calliope(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'mori-calliope' in data['versatile'], \
            'mori-calliope tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_raiden_shogun(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'raiden-shogun' in data['versatile'], \
            'raiden-shogun tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_oppai(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'oppai' in data['versatile'], \
            'oppai tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_selfies(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'selfies' in data['versatile'], \
            'selfies tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_uniform(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'uniform' in data['versatile'], \
            'uniform tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_kamisato_ayaka(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'kamisato-ayaka' in data['versatile'], \
            'kamisato-ayaka tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_group_nsfw_amount(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert len(data['nsfw']) == 7, 'Amount of nsfw group tags is 7'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_ass(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'ass' in data['nsfw'], \
            'ass tag is not present in nsfw group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_oral(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'oral' in data['nsfw'], 'oral tag is not present in nsfw group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_milf(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'milf' in data['nsfw'], 'milf tag is not present in nsfw group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_paizuri(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'paizuri' in data['nsfw'], 'paizuri tag is not present in nsfw group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_ecchi(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'ecchi' in data['nsfw'], 'ecchi tag is not present in nsfw group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_contains_ero(self, request_get_tags_response):
        data = request_get_tags_response.json()
        assert 'ero' in data['nsfw'], 'ero tag is not present in nsfw group'


class TestGetTagsFullParameterFalse:
    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_status_code(self, request_get_tags_query_full_false_response):
        assert request_get_tags_query_full_false_response.status_code == 200, "Status code is not 200"

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_groups_amount(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert len(data) == 2, 'Tags group amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_group_versatile_presence(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'versatile' in data, 'Versatile tag group is missing'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_group_nsfw_presence(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'nsfw' in data, 'NSFW (lewd) tag group is missing'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_group_versatile_amount(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert len(data['versatile']) == 9, 'Amount of versatile group tags is 9'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_group_nsfw_amount(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert len(data['nsfw']) == 7, 'Amount of nsfw group tags is 7'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_maid(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'maid' in data['versatile'], 'maid tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_waifu(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'waifu' in data['versatile'], 'waifu tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_marin_kitagawa(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'marin-kitagawa' in data['versatile'], 'marin-kitagawa tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_mori_calliope(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'mori-calliope' in data['versatile'], 'mori-calliope tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_raiden_shogun(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'raiden-shogun' in data['versatile'], 'raiden-shogun tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_selfies(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'selfies' in data['versatile'], 'selfies tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_uniform(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'uniform' in data['versatile'], 'uniform tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_contains_kamisato_ayaka(self, request_get_tags_query_full_false_response):
        data = request_get_tags_query_full_false_response.json()
        assert 'kamisato-ayaka' in data['versatile'], 'kamisato-ayaka tag is not present in versatile group'

    nsfw_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero']

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("nsfw_tag", nsfw_tags)
    def test_get_tags_query_full_false_contains_in_nsfw(self, request_get_tags_query_full_false_response, nsfw_tag):
        status_code, data = request_get_tags_query_full_false_response
        assert nsfw_tag in data['nsfw'], f'{nsfw_tag} tag is not present in nsfw'

    def test_get_tags_full_info_true(self):
        response = requests.get(url='https://api.waifu.im/tags?full=true')
        assert response.status_code == 200, "Status code is not 200"

        data = response.json()
        assert len(data) == 2, 'Tags group amount is wrong'
        assert data['nsfw'] is not None
        assert data['versatile'] is not None

        assert tag_full_info_provider('ass', data['nsfw']) is not None, 'ass tag does not have full info'
        tag_full_info = tag_full_info_provider('ass', data['nsfw'])
        assert tag_full_info['tag_id'] == 1
        assert tag_full_info['description'] == "Girls with a large butt. "
        assert tag_full_info['is_nsfw'] is True
        assert len(tag_full_info) == 4, 'Amount of information fields are not equal 4'

        assert tag_full_info_provider('ecchi', data['nsfw']) is not None, 'ecchi tag does not have full info'
        tag_full_info = tag_full_info_provider('ecchi', data['nsfw'])
        assert tag_full_info['tag_id'] == 2
        assert tag_full_info[
                   'description'] == ("Slightly explicit sexual content. Show full to partial nudity. "
                                      "Doesn't show any genital.")
        assert tag_full_info['is_nsfw'] is True
        assert len(tag_full_info) == 4, 'Amount of information fields are not equal 4'

        assert tag_full_info_provider('ero', data['nsfw']) is not None, 'ero tag does not have full info'
        tag_full_info = tag_full_info_provider('ero', data['nsfw'])
        assert tag_full_info['tag_id'] == 3
        assert tag_full_info['description'] == "Any kind of erotic content, basically any nsfw image."
        assert tag_full_info['is_nsfw'] is True
        assert len(tag_full_info) == 4, 'Amount of information fields are not equal 4'

        assert tag_full_info_provider('hentai', data['nsfw']) is not None, 'hentai tag does not have full info'
        tag_full_info = tag_full_info_provider('hentai', data['nsfw'])
        assert tag_full_info['tag_id'] == 4
        assert tag_full_info['description'] == "Explicit sexual content."
        assert tag_full_info['is_nsfw'] is True
        assert len(tag_full_info) == 4, 'Amount of information fields are not equal 4'

        assert tag_full_info_provider('milf', data['nsfw']) is not None, 'hentai tag does not have full info'
        tag_full_info = tag_full_info_provider('milf', data['nsfw'])
        assert tag_full_info['tag_id'] == 6
        assert tag_full_info['description'] == "A sexually attractive middle-aged woman."
        assert tag_full_info['is_nsfw'] is True
        assert len(tag_full_info) == 4, 'Amount of information fields are not equal 4'

        assert tag_full_info_provider('oral', data['nsfw']) is not None, 'oral tag does not have full info'
        tag_full_info = tag_full_info_provider('oral', data['nsfw'])
        assert tag_full_info['tag_id'] == 8
        assert tag_full_info['description'] == "Oral sex content."
        assert tag_full_info['is_nsfw'] is True
        assert len(tag_full_info) == 4, 'Amount of information fields are not equal 4'

        assert tag_full_info_provider('paizuri', data['nsfw']) is not None, 'paizuri tag does not have full info'
        tag_full_info = tag_full_info_provider('paizuri', data['nsfw'])
        assert tag_full_info['tag_id'] == 9
        assert tag_full_info['description'] == ("A subcategory of hentai that involves breast sex, "
                                                "also known as titty fucking.")
        assert tag_full_info['is_nsfw'] is True
        assert len(tag_full_info) == 4, 'Amount of information fields are not equal 4'

        assert len(data['nsfw']) == 7, 'Amount of nsfw group tags is 7'
