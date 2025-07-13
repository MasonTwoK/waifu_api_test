# Tests for page - https://docs.waifu.im/reference/api-reference/tags

import pytest

from methods import tag_full_info_provider, tag_full_info_comparer
from conftest import request_get_tags_query_full_false_response


@pytest.mark.tags
class TestGetTags:
    tags_groups = ['versatile', 'nsfw']
    versatile_tags = ['maid', 'waifu', 'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai', 'selfies',
                      'uniform', 'kamisato-ayaka']
    nsfw_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero']

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.status_code
    def test_get_tags_status_code(self, request_get_tags_response):
        assert request_get_tags_response.status_code == 200, "Status code is not 200"

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
    tags_groups = ['versatile', 'nsfw']
    versatile_tags = ['maid', 'waifu', 'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai', 'selfies',
                      'uniform', 'kamisato-ayaka']
    nsfw_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero']

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_false_status_code(self, request_get_tags_query_full_false_response):
        assert request_get_tags_query_full_false_response.status_code == 200, "Status code is not 200"

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
        assert len(request_get_tags_query_full_false_response.data[group_name]) == amount, 'Tags group amount is wrong'

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
    def test_get_tags_query_full_false_contains_in_nsfw(self, request_get_tags_query_full_false_response, nsfw_tag):
        assert nsfw_tag in request_get_tags_query_full_false_response.data['nsfw'], \
            f'{nsfw_tag} tag is not present in nsfw group'


class TestGetTagsFullInfoTrue:
    tags_groups = ['versatile', 'nsfw']
    nsfw_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero']
    versatile_tags = ['maid', 'waifu', 'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai', 'selfies',
                      'uniform', 'kamisato-ayaka']

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_true_status_code(self, request_get_tags_query_full_true_response):
        assert request_get_tags_query_full_true_response.status_code == 200

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
    @pytest.mark.parametrize("tag_id, name, is_nsfw, description", [
        pytest.param(1, 'ass', True, 'Girls with a large butt. ', id='ass'),
        pytest.param(2, 'ecchi', True, "Slightly explicit sexual content. Show full to partial nudity. "
                                       "Doesn't show any genital.", id='ecchi'),
        pytest.param(3, 'ero', True, 'Any kind of erotic content, basically any nsfw image.', id='ero'),
        pytest.param(4, 'hentai', True, 'Explicit sexual content.', id='hentai'),
        pytest.param(6, 'milf', True, 'A sexually attractive middle-aged woman.', id='milf'),
        pytest.param(8, 'oral', True, 'Oral sex content.', id='oral'),
        pytest.param(9, 'paizuri', True, 'A subcategory of hentai that involves breast sex, '
                                         'also known as titty fucking.', id='paizuri')
    ])
    def test_get_tags_query_full_true_contains_info_for_nsfw_tags(self, request_get_tags_query_full_true_response,
                                                                  tag_id, name, is_nsfw, description):
        assert tag_full_info_comparer(request_get_tags_query_full_true_response.data['nsfw'],
                                      tag_id, name, is_nsfw, description), f"{name} tag has incorrect full info"

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("tag_id, name, is_nsfw, description", [
        pytest.param(5, "marin-kitagawa", False, "One of two main protagonists (alongside Wakana Gojo) in the anime "
                                                 "and manga series My Dress-Up Darling.", id="marin-kitagawa"),
        pytest.param(7, "oppai", False, "Girls with large breasts", id="oppai"),
        pytest.param(10, "selfies", False, "A photo-like image of a waifu.", id="selfies"),
        pytest.param(11, "uniform", False, "Girls wearing any kind of uniform, cosplay etc... ", id="uniform"),
        pytest.param(12, 'waifu', False, "A female anime/manga character.", id='waifu'),
        pytest.param(13, 'maid', False, "Cute womans or girl employed to do domestic work in their working uniform.",
                     id='maid'),
        pytest.param(14, "mori-calliope", False,
                     "Mori Calliope is an English Virtual YouTuber (VTuber) associated with hololive as part of its "
                     "first-generation English branch of Vtubers.", id="mori-calliope"),
        pytest.param(15, "raiden-shogun", False,
                     "Genshin Impact's Raiden Shogun is a fierce lady in the Genshin ranks.", id="raiden-shogun"),
        pytest.param(17, "kamisato-ayaka", False, "Kamisato Ayaka is a playable Cryo character in Genshin Impact.",
                     id="kamisato-ayaka")
    ])
    def test_get_query_full_true_contains_info_for_versatile_tags(self, request_get_tags_query_full_true_response,
                                                                  tag_id, name, is_nsfw, description):
        assert tag_full_info_comparer(
            request_get_tags_query_full_true_response.data['versatile'], tag_id, name, is_nsfw, description), \
            f'Tag {name} full info is wrong'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_get_tags_query_full_true_amount_of_nsfw_tags(self, request_get_tags_query_full_true_response):
        assert len(request_get_tags_query_full_true_response.data['nsfw']) == 7, 'Amount of nsfw tags is not 7'

    @pytest.mark.tags
    @pytest.mark.positive
    def test_tags_query_full_true_amount_of_versatile_tags(self, request_get_tags_query_full_true_response):
        assert len(request_get_tags_query_full_true_response.data['versatile']) == 9, \
            'Amount of versatile tags is not 9'

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("nsfw_tag", nsfw_tags)
    def test_get_tags_query_full_true_nsfw_tags_info_size(self, request_get_tags_query_full_true_response, nsfw_tag):
        assert len(tag_full_info_provider(nsfw_tag, request_get_tags_query_full_true_response.data['nsfw'])) == 4, \
            f"{nsfw_tag} info fields don't equal 4"

    @pytest.mark.tags
    @pytest.mark.positive
    @pytest.mark.parametrize("versatile_tag", versatile_tags)
    def test_get_tags_query_full_true_versatile_tags_info_size(self, request_get_tags_query_full_true_response,
                                                               versatile_tag):
        assert len(tag_full_info_provider(
            versatile_tag, request_get_tags_query_full_true_response.data['versatile'])) == 4, \
            f"{versatile_tag} info fields don't equal 4"
