import requests
import random
from data import nsfw_tags, versatile_tags


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


def tag_full_info_tags_group_selector(data, tag_name):
    for nsfw_tag in nsfw_tags:
        if nsfw_tag == tag_name:
            return data['nsfw']

    for versatile_tag in versatile_tags:
        if versatile_tag == tag_name:
            return data['versatile']

    return None


def tag_full_info_tag_name_provider(data, tag_name):
    tags_list = tag_full_info_tags_group_selector(data, tag_name)
    if tags_list is None:
        return None

    for tag in range(len(tags_list)):
        if tags_list[tag]['name'] == tag_name:
            return True
    return None


def tag_full_info_id_provider(data, tag_name):
    tags_list = tag_full_info_tags_group_selector(data, tag_name)
    if tags_list is None:
        return None

    for tag in range(len(tags_list)):
        if tags_list[tag]['name'] == tag_name:
            return tags_list[tag]['tag_id']
    return None


def tag_full_info_description_provider(data, tag_name):
    tags_list = tag_full_info_tags_group_selector(data, tag_name)
    if tags_list is None:
        return None

    for tag in range(len(tags_list)):
        if tags_list[tag]['name'] == tag_name:
            return tags_list[tag]['description']
    return None


def tag_full_info_is_nsfw_state_provider(data, tag_name):
    tags_list = tag_full_info_tags_group_selector(data, tag_name)
    if tags_list is None:
        return None

    for tag in range(len(tags_list)):
        if tags_list[tag]['name'] == tag_name:
            return tags_list[tag]['is_nsfw']
    return None


def tag_full_info_provider(data, tag_full_info):
    tags_list = tag_full_info_tags_group_selector(data, tag_full_info['name'])
    if tags_list is None:
        return None

    for list_element in range(len(tags_list)):
        if tags_list[list_element]['name'] == tag_full_info['name']:
            return tags_list[list_element]
    return None


def tag_full_info_comparer(data, tag_full_info):
    tags_list_element = tag_full_info_provider(data, tag_full_info)

    if tags_list_element == tag_full_info:
        return True
    return None


def tag_randomizer():
    list_of_tags = []

    response = requests.get(url='https://api.waifu.im/tags')
    content = response.json()

    for i in range(len(list(content))):
        list_of_tags += list(content.values())[i]
        # Is there something wrong about it https://www.geeksforgeeks.org/python-select-random-value-from-a-list/ ?

    return random.choice(list_of_tags)


def tags_comparer(tag, content):
    for element in content['images'][0]['tags']:
        if element['name'] == tag:
            return True
    return False


def search_data_type_checker(img_field, data_type, possible_none=False):
    if possible_none:
        # TODO: Need to investigate behaviour below..
        return isinstance(img_field, data_type) or img_field is None
    else:
        return isinstance(img_field, data_type)


def query_bool_param_provider(parameter):
    if parameter == "True":
        parameter = True
    if parameter == "False":
        parameter = False
    return parameter


def search_orientation_provider(response_body):
    if response_body['images'][0]['height'] > response_body['images'][0]['width']:
        return ['PORTRAIT', 'RANDOM']
    if response_body['images'][0]['height'] < response_body['images'][0]['width']:
        return ['LANDSCAPE', 'RANDOM']
    if response_body['images'][0]['height'] == response_body['images'][0]['width']:
        return ['PORTRAIT', 'LANDSCAPE', 'RANDOM']
    else:
        return 0


def search_image_id_provider():
    response = requests.get(url=f'https://api.waifu.im/search')
    image_id = response.json()['images'][0]['image_id']

    return image_id


def search_side_size_check(data, operator, size, side):
    value = data['images'][0][side]
    match operator:
        case '>':
            if value > size:
                return True
        case '<':
            if value < size:
                return True
        case '>=':
            if value >= size:
                return True
        case '<=':
            if value <= size:
                return True
        case '!=':
            if value != size:
                return True
        case '==':
            if value == size:
                return True
        case '=':
            if value == size:
                return True
    return False
