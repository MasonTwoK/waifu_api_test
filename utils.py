
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
