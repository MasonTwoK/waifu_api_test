# Tests for page - https://docs.waifu.im/reference/api-reference/tags

import pytest
import requests

# def tag_contains(searched_tag, list_of_tags):
#     for tag in list_of_tags:
#         if tag == searched_tag:
#             return True
#         else:
#             return None  # Чому я не можу зробити так?


def tag_contains(searched_tag, list_of_tags):
    for tag in list_of_tags:
        if tag == searched_tag:
            return True
    return None


def tag_full_info_provider(tag_name, tags_group_list):
    for list_element in range(len(tags_group_list)):
        if tags_group_list[list_element]['name'] == tag_name:
            return tags_group_list[list_element]
    return None


def test_get_tags():
    response = requests.get(url="https://api.waifu.im/tags")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2, 'Tags group amount is wrong'
    assert data['versatile'] is not None, 'Versatile tag group is missing'
    assert data['nsfw'] is not None, 'NSFW (lewd) tag group is missing'

    assert tag_contains('maid', data['versatile']), 'maid tag is not present in versatile group'
    assert 'maid' in data['versatile'], 'maid tag is not present in versatile group'  # Яка різниця з попереднім рядком?
    # assert ['maid', 'oppai'] in data['versatile'], 'maid & oppai tags are not present in versatile group'  # Чому так воно видає помилку? Проблема порядку?
    assert tag_contains('waifu', data['versatile']), 'waifu tag is not present in versatile group'
    assert tag_contains('marin-kitagawa', data['versatile']), 'marin-kitagawa tag is not present'
    assert tag_contains('mori-calliope', data['versatile']), 'mori-calliope tag is not present'
    assert tag_contains('raiden-shogun', data['versatile']), 'raiden-shogun tag is not present'
    assert tag_contains('oppai', data['versatile']), 'oppai tag is not present'
    assert tag_contains('selfies', data['versatile']), 'selfies tag is not present'
    assert tag_contains('uniform', data['versatile']), 'uniform tag is not present'
    assert tag_contains('kamisato-ayaka', data['versatile']), 'kamisato-ayaka tag is not present'
    assert len(data['versatile']) == 9, 'Amount of versatile group tags is 9'

    assert tag_contains('ass', data['nsfw']), 'ass tag is not present in nsfw'
    assert tag_contains('hentai', data['nsfw']), 'hentai tag is not present in nsfw'
    assert tag_contains('milf', data['nsfw']), 'milf tag is not present in nsfw'
    assert tag_contains('oral', data['nsfw']), 'oral tag is not present in nsfw'
    assert tag_contains('paizuri', data['nsfw']), 'paizuri tag is not present in nsfw'
    assert tag_contains('ecchi', data['nsfw']), 'ecchi tag is not present in nsfw'
    assert tag_contains('ero', data['nsfw']), 'ero tag is not present in nsfw'
    assert len(data['nsfw']) == 7, 'Amount of nsfw group tags is 7'


def test_get_tags_full_info_false():
    response = requests.get(url="https://api.waifu.im/tags?full=false")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2, 'Tags group amount is wrong'
    assert data['versatile'] is not None, 'Versatile tag group is missing'
    assert data['nsfw'] is not None, 'NSFW (lewd) tag group is missing'

    assert tag_contains('maid', data['versatile']), 'maid tag is not present in versatile group'
    assert 'maid' in data['versatile'], 'maid tag is not present in versatile group'
    assert tag_contains('waifu', data['versatile']), 'waifu tag is not present in versatile group'
    assert tag_contains('marin-kitagawa', data['versatile']), 'marin-kitagawa tag is not present'
    assert tag_contains('mori-calliope', data['versatile']), 'mori-calliope tag is not present'
    assert tag_contains('raiden-shogun', data['versatile']), 'raiden-shogun tag is not present'
    assert tag_contains('oppai', data['versatile']), 'oppai tag is not present'
    assert tag_contains('selfies', data['versatile']), 'selfies tag is not present'
    assert tag_contains('uniform', data['versatile']), 'uniform tag is not present'
    assert tag_contains('kamisato-ayaka', data['versatile']), 'kamisato-ayaka tag is not present'
    assert len(data['versatile']) == 9, 'Amount of versatile group tags is 9'

    assert tag_contains('ass', data['nsfw']), 'ass tag is not present in nsfw'
    assert tag_contains('hentai', data['nsfw']), 'hentai tag is not present in nsfw'
    assert tag_contains('milf', data['nsfw']), 'milf tag is not present in nsfw'
    assert tag_contains('oral', data['nsfw']), 'oral tag is not present in nsfw'
    assert tag_contains('paizuri', data['nsfw']), 'paizuri tag is not present in nsfw'
    assert tag_contains('ecchi', data['nsfw']), 'ecchi tag is not present in nsfw'
    assert tag_contains('ero', data['nsfw']), 'ero tag is not present in nsfw'
    assert len(data['nsfw']) == 7, 'Amount of nsfw group tags is 7'


def test_get_tags_full_info_true():
    response = requests.get(url='https://api.waifu.im/tags?full=true')
    assert response.status_code == 200

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

    assert len(data['nsfw']) == 7, 'Amount of nsfw group tags is 7'

