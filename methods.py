
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


def tag_full_info_comparer(tags_group_list, tag_id, name, is_nsfw, description):
    tag_full_info = {'tag_id': tag_id, 'name': name, 'is_nsfw': is_nsfw, 'description': description}
    for list_element in range(len(tags_group_list)):
        if tags_group_list[list_element]['name'] == name:
            if tag_full_info == tags_group_list[list_element]:
                return True
    return None


def tag_full_info_provider(tag_name, tags_group_list):
    for list_element in range(len(tags_group_list)):
        if tags_group_list[list_element]['name'] == tag_name:
            return tags_group_list[list_element]
    return None