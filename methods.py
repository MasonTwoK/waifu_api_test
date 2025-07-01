
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
