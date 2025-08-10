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


def tag_full_info_comparer(data, tag_full_info):
    if tag_full_info['is_nsfw']:
        tags_list = data['nsfw']
    else:
        tags_list = data['versatile']

    for list_element in range(len(tags_list)):
        if tags_list[list_element]['name'] == tag_full_info['name']:
            if tags_list[list_element] == tag_full_info:
                return True
    return None


def tag_full_info_provider(data, tag_full_info):
    if tag_full_info['is_nsfw']:
        tags_list = data['nsfw']
    else:
        tags_list = data['versatile']

    for list_element in range(len(tags_list)):
        if tags_list[list_element]['name'] == tag_full_info['name']:
            return tags_list[list_element]
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
