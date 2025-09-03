# Tests for page - https://docs.waifu.im/reference/api-reference/tags

import pytest

from utils import (tag_full_info_provider, tag_full_info_comparer, tag_full_info_id_provider,
                   tag_full_info_tag_name_provider, tag_full_info_description_provider,
                   tag_full_info_is_nsfw_state_provider)
from data import (tags_full_info, tags_groups, nsfw_tags, versatile_tags, tags_in_group_amount, tag_full_info_tag_ids,
                  tag_full_info_tag_names, tag_full_info_tag_descriptions, tag_full_info_tag_is_nsfw_states)


@pytest.mark.tags
@pytest.mark.positive
class TestGetTags:

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_tags_status_code(self, request_get_tags):
        assert request_get_tags.status_code == 200, \
            f"Status code {request_get_tags.status_code} is not 200"

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_groups_amount(self, request_get_tags):
        assert len(request_get_tags.data) == 2, 'Tags group amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name", tags_groups)
    def test_get_tags_groups_presence(self, request_get_tags, group_name):
        assert group_name in request_get_tags.data, f'{group_name} tags group is missing'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name, amount", tags_in_group_amount)
    def test_get_tags_in_group_amount(self, request_get_tags, group_name, amount):
        assert len(request_get_tags.data[group_name]) == amount, \
            f'Amount of tags in {group_name} group are not {amount}'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("versatile_tag", versatile_tags)
    def test_get_tags_contains_versatile_tags(self, request_get_tags, versatile_tag):
        assert versatile_tag in request_get_tags.data['versatile'], \
            f'{versatile_tag} tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("nsfw_tag", nsfw_tags)
    def test_get_tags_contains_nsfw_tags(self, request_get_tags, nsfw_tag):
        assert nsfw_tag in request_get_tags.data['nsfw'], f'{nsfw_tag} tag is not present in nsfw group'


@pytest.mark.tags
@pytest.mark.positive
class TestGetTagsFullInfoFalse:

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_status_code(self, request_get_tags_query_full_false):
        assert request_get_tags_query_full_false.status_code == 200, \
            f"Status code {request_get_tags_query_full_false.status_code} is not 200"

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_groups_amount(self, request_get_tags_query_full_false):
        assert len(request_get_tags_query_full_false.data) == 2, 'Tags group amount is wrong'

    # Maybe we don't need this test?
    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name", tags_groups)
    def test_get_tags_query_full_false_groups_presence(self, request_get_tags_query_full_false, group_name):
        assert group_name in request_get_tags_query_full_false.data, f'{group_name} tags group is missing'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name, amount", tags_in_group_amount)
    def test_get_tags_query_full_false_in_group_amount(self, request_get_tags_query_full_false, group_name, amount):
        assert len(request_get_tags_query_full_false.data[group_name]) == amount, \
            f'Tags group {group_name} amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("versatile_tag", versatile_tags)
    def test_get_tags_query_full_false_contains_in_versatile(self, request_get_tags_query_full_false, versatile_tag):
        assert versatile_tag in request_get_tags_query_full_false.data['versatile'], \
            f'{versatile_tag} tag is not present in versatile group'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("nsfw_tag", nsfw_tags)
    def test_get_tags_query_full_false_contains_in_nsfw(self, request_get_tags_query_full_false, nsfw_tag):
        assert nsfw_tag in request_get_tags_query_full_false.data['nsfw'], \
            f'{nsfw_tag} tag is not present in nsfw group'


@pytest.mark.tags
@pytest.mark.positive
class TestGetTagsFullInfoTrue:

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_true_status_code(self, request_get_tags_query_full_true):
        assert request_get_tags_query_full_true.status_code == 200, \
            f'Status code {request_get_tags_query_full_true.status_code} is not 200'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_true_groups_amount(self, request_get_tags_query_full_true):
        assert len(request_get_tags_query_full_true.data) == 2, 'Tags group amount is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_name", tags_groups)
    def test_get_tags_query_full_true_groups_presence(self, request_get_tags_query_full_true, group_name):
        assert group_name in request_get_tags_query_full_true.data, f'{group_name} is not present'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("group_tag, amount", tags_in_group_amount)
    def test_get_tags_query_full_true_amount_of_tags_in_group(self, request_get_tags_query_full_true, group_tag, amount):
        assert len(request_get_tags_query_full_true.data[group_tag]) == amount, \
            f'Amount of {group_tag} tags is not {amount}'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_full_info", tags_full_info)
    def test_get_tags_query_full_true_tags_info_size(self, tag_full_info, request_get_tags_query_full_true):
        assert len(tag_full_info_provider(request_get_tags_query_full_true.data, tag_full_info)) == 4, \
            f"{tag_full_info['name']} info fields don't equal 4"

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_name", tag_full_info_tag_names)
    def test_tags_query_full_true_contains_info_name(self, request_get_tags_query_full_true, tag_name):
        assert tag_full_info_tag_name_provider(request_get_tags_query_full_true.data, tag_name), \
            f"Tag name {tag_name} is not present in full info"

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_name, tag_description", tag_full_info_tag_descriptions)
    def test_get_tags_query_full_true_contains_info_description(self, request_get_tags_query_full_true,
                                                                tag_name, tag_description):
        assert (tag_full_info_description_provider(request_get_tags_query_full_true.data, tag_name) ==
                tag_description), \
            f"Tag's {tag_name}  tag description: {tag_description} is wrong"

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_name, tag_id", tag_full_info_tag_ids)
    def test_get_tags_query_full_true_contains_info_id(self, request_get_tags_query_full_true, tag_name, tag_id):
        assert tag_full_info_id_provider(request_get_tags_query_full_true.data, tag_name) == tag_id, \
            f"Tag's {tag_name}  tag id: {tag_id} is wrong"

    @pytest.mark.parametrize("tag_name, is_nsfw_state", tag_full_info_tag_is_nsfw_states)
    def test_get_tags_query_full_true_contains_info_is_nsfw_state(self, request_get_tags_query_full_true,
                                                                  tag_name, is_nsfw_state):
        assert (tag_full_info_is_nsfw_state_provider(request_get_tags_query_full_true.data, tag_name) ==
                is_nsfw_state), f"Tag's {tag_name}  is_nsfw state: {is_nsfw_state} is wrong"

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_full_info", tags_full_info)
    def test_get_tags_query_full_true_contains_info(self, tag_full_info, request_get_tags_query_full_true):
        assert tag_full_info_comparer(request_get_tags_query_full_true.data, tag_full_info), \
            f"{tag_full_info['name']} tag has incorrect full info"


@pytest.mark.tags
@pytest.mark.negative
class TestGetTagsErrorCodes:
    def test_get_tags_query_full_error_code_400(self, request_get_tags_query_full_wrong):
        assert request_get_tags_query_full_wrong.status_code == 400, \
            f"Status code {request_get_tags_query_full_wrong.status_code} is not 400"

    def test_get_tags_query_full_error_code_400_details(self, request_get_tags_query_full_wrong):
        assert (request_get_tags_query_full_wrong.data['detail'] ==
                'Bad Request, error on full, failed to bind field value to bool'), 'Detail message is wrong'


@pytest.mark.xfail(reason="Чому так, воно видає помилку? Проблема порядку?")
@pytest.mark.tags
@pytest.mark.positive
def test_get_tags_contains_maid_and_oppai(request_get_tags):
    assert ['maid', 'oppai'] in request_get_tags.data['versatile'], \
        'maid & oppai tags are not present in versatile group'
