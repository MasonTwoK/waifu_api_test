import pytest

tags_groups = ['versatile', 'nsfw']
nsfw_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero']

versatile_tags = ['maid', 'waifu', 'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai', 'selfies',
                  'uniform', 'kamisato-ayaka']

full_info_tag_names = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero', 'maid', 'waifu', 'marin-kitagawa',
                       'mori-calliope', 'raiden-shogun', 'oppai', 'selfies', 'uniform', 'kamisato-ayaka']

tags_in_group_amount = [
    pytest.param('versatile', 9, id='versatile'),
    pytest.param('nsfw', 7, id='nsfw')
]

tags_full_info = [
        pytest.param({
            'tag_id': 1,
            'name': 'ass',
            'is_nsfw': True,
            'description': 'Girls with a large butt. '
            }, id='ass'
        ),
        pytest.param({
            'tag_id': 2,
            'name': 'ecchi',
            'is_nsfw': True,
            'description': "Slightly explicit sexual content. Show full to partial nudity. Doesn't show any genital."
            }, id='ecchi'
        ),
        pytest.param({
            'tag_id': 3,
            'name': 'ero',
            'is_nsfw': True,
            'description': 'Any kind of erotic content, basically any nsfw image.'
            }, id='ero'
        ),
        pytest.param({
            'tag_id': 4,
            'name': 'hentai',
            'is_nsfw': True,
            'description': 'Explicit sexual content.'
            }, id='hentai'
        ),
        pytest.param({
            'tag_id': 5,
            'name': "marin-kitagawa",
            'is_nsfw': False,
            'description': "One of two main protagonists (alongside Wakana Gojo) in the anime and manga series My "
                           "Dress-Up Darling."
            }, id='marin-kitagawa'
        ),
        pytest.param({
            'tag_id': 6,
            'name': 'milf',
            'is_nsfw': True,
            'description': 'A sexually attractive middle-aged woman.'
            }, id='milf'
        ),
        pytest.param({
            'tag_id': 7,
            'name': "oppai",
            'is_nsfw': False,
            'description': "Girls with large breasts"
            }, id='oppai'
        ),
        pytest.param({
            'tag_id': 8,
            'name': 'oral',
            'is_nsfw': True,
            'description': 'Oral sex content.'
            }, id='oral'
        ),
        pytest.param({
            'tag_id': 9,
            'name': 'paizuri',
            'is_nsfw': True,
            'description': 'A subcategory of hentai that involves breast sex, also known as titty fucking.'
            }, id='paizuri'
        ),
        pytest.param({
            'tag_id': 10,
            'name': "selfies",
            'is_nsfw': False,
            'description': "A photo-like image of a waifu."
            }, id='selfies'
        ),
        pytest.param({
            'tag_id': 11,
            'name': "uniform",
            'is_nsfw': False,
            'description': "Girls wearing any kind of uniform, cosplay etc... "
            }, id='uniform'
        ),
        pytest.param({
            'tag_id': 12,
            'name': 'waifu',
            'is_nsfw': False,
            'description': "A female anime/manga character."
            }, id='waifu'
        ),
        pytest.param({
            'tag_id': 13,
            'name': 'maid',
            'is_nsfw': False,
            'description': 'Cute womans or girl employed to do domestic work in their working uniform.'
            }, id='maid'
        ),
        pytest.param({
            'tag_id': 14,
            'name': 'mori-calliope',
            'is_nsfw': False,
            'description': 'Mori Calliope is an English Virtual YouTuber (VTuber) associated with hololive as part of '
                           'its first-generation English branch of Vtubers.'
            }, id='mori-calliope'
        ),
        pytest.param({
            'tag_id': 15,
            'name': 'raiden-shogun',
            'is_nsfw': False, 'description': "Genshin Impact's Raiden Shogun is a fierce lady in the Genshin ranks."
            }, id='raiden-shogun'
        ),
        pytest.param({
            'tag_id': 17,
            'name': 'kamisato-ayaka',
            'is_nsfw': False,
            'description': 'Kamisato Ayaka is a playable Cryo character in Genshin Impact.'
            }, id='kamisato-ayaka'
        ),
]

tag_full_info_tag_ids = [
    pytest.param('ass', 1, id='ass'),
    pytest.param('ecchi', 2, id='ecchi'),
    pytest.param('ero', 3, id='ero'),
    pytest.param('hentai', 4, id='hentai'),
    pytest.param('milf', 6, id='milf'),
    pytest.param('oral', 8, id='oral'),
    pytest.param('paizuri', 9, id='paizuri'),
    pytest.param('maid', 13, id='maid'),
    pytest.param('waifu', 12, id='waifu'),
    pytest.param('marin-kitagawa', 5, id='marin-kitagawa'),
    pytest.param('mori-calliope', 14, id='mori-calliope'),
    pytest.param('raiden-shogun', 15, id='raiden-shogun'),
    pytest.param('oppai', 7, id='oppai'),
    pytest.param('selfies', 10, id='selfies'),
    pytest.param('uniform', 11, id='uniform'),
    pytest.param('kamisato-ayaka', 17, id='kamisato-ayaka'),
]

tag_full_info_tag_descriptions = [
    pytest.param('ass', 'Girls with a large butt. ', id='ass'),
    pytest.param('ecchi', "Slightly explicit sexual content. Show full to partial nudity. "
                          "Doesn't show any genital.", id='ecchi'),
    pytest.param('ero', 'Any kind of erotic content, basically any nsfw image.', id='ero'),
    pytest.param('hentai', 'Explicit sexual content.', id='hentai'),
    pytest.param('milf', 'A sexually attractive middle-aged woman.', id='milf'),
    pytest.param('oral', 'Oral sex content.', id='oral'),
    pytest.param('paizuri', 'A subcategory of hentai that involves breast sex, '
                            'also known as titty fucking.', id='paizuri'),
    pytest.param('maid', 'Cute womans or girl employed to do domestic work in their working uniform.', id='maid'),
    pytest.param('waifu', "A female anime/manga character.", id='waifu'),
    pytest.param('marin-kitagawa', "One of two main protagonists (alongside Wakana Gojo) "
                                   "in the anime and manga series My Dress-Up Darling.", id='marin-kitagawa'),
    pytest.param('mori-calliope', 'Mori Calliope is an English Virtual YouTuber (VTuber) associated with '
                                  'hololive as part of '
                                  'its first-generation English branch of Vtubers.', id='mori-calliope'),
    pytest.param('raiden-shogun', "Genshin Impact's Raiden Shogun is a fierce lady "
                                  "in the Genshin ranks.", id='raiden-shogun'),
    pytest.param('oppai', "Girls with large breasts", id='oppai'),
    pytest.param('selfies', "A photo-like image of a waifu.", id='selfies'),
    pytest.param('uniform', "Girls wearing any kind of uniform, cosplay etc... ", id='uniform'),
    pytest.param('kamisato-ayaka', 'Kamisato Ayaka is a playable Cryo character '
                                   'in Genshin Impact.', id='kamisato-ayaka')
    ]

tag_full_info_tag_is_nsfw_states = [
    pytest.param('ass', True, id='ass'),
    pytest.param('ecchi', True, id='ecchi'),
    pytest.param('ero', True, id='ero'),
    pytest.param('hentai', True, id='hentai'),
    pytest.param('milf', True, id='milf'),
    pytest.param('oral', True, id='oral'),
    pytest.param('paizuri', True, id='paizuri'),
    pytest.param('maid', False, id='maid'),
    pytest.param('waifu', False, id='waifu'),
    pytest.param('marin-kitagawa', False, id='marin-kitagawa'),
    pytest.param('mori-calliope', False, id='mori-calliope'),
    pytest.param('raiden-shogun', False, id='raiden-shogun'),
    pytest.param('oppai', False, id='oppai'),
    pytest.param('selfies', False, id='selfies'),
    pytest.param('uniform', False, id='uniform'),
    pytest.param('kamisato-ayaka', False, id='kamisato-ayaka'),
]

search_random_fields_name = [
    pytest.param('signature', str, id='signature'),
    pytest.param('extension', str, id='extension'),
    pytest.param('dominant_color', str, id='dominant_color'),
    pytest.param('uploaded_at', str, id='uploaded_at'),
    pytest.param('url', str, id='url'),
    pytest.param('preview_url', str, id='preview_url'),
    pytest.param('image_id', int, id='image_id'),
    pytest.param('favorites', int, id='favorites'),
    pytest.param('width', int, id='width'),
    pytest.param('height', int, id='height'),
    pytest.param('byte_size', int, id='byte_size'),
    pytest.param('is_nsfw', bool, id='is_nsfw'),
    pytest.param('tags', list, id='tags')
]

search_random_fields_name_or_none = [
    pytest.param('source', str, id='source'),
    pytest.param('artist', dict, id='artist'),
    pytest.param('liked_at', str, id='liked_at')
]

search_random_fields_name_tags = [
    pytest.param('tag_id', int, id='tag_id'),
    pytest.param('name', str, id='name'),
    pytest.param('description', str, id='description'),
    pytest.param('is_nsfw', bool, id='is_nsfw'),
]

# https://docs.pytest.org/en/stable/how-to/fixtures.html#using-marks-with-parametrized-fixtures
search_excluded_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero', 'maid',
                        pytest.param('waifu', marks=pytest.mark.xfail(reason="No response without 'waifu' tag")),
                        'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai', 'selfies',
                        'uniform', 'kamisato-ayaka']

search_query_size_operators = [
    pytest.param('<=', marks=pytest.mark.xfail(reason="Bug: Operator doesn't work as expected. Repro: 50%")),
    pytest.param('>=', marks=pytest.mark.xfail(reason="Bug: Operator doesn't work as expected. Repro: 50%")),
    pytest.param('<', marks=pytest.mark.xfail(reason="Bug: Operator doesn't work as expected. Repro: 50%")),
    pytest.param('>', marks=pytest.mark.xfail(reason="Bug: Operator doesn't work as expected. Repro: 50%")),
    pytest.param('!=', marks=pytest.mark.xfail(reason="Bug: Operator doesn't work as expected. Repro: 50%")),
    pytest.param('=', marks=pytest.mark.xfail(reason="Bug: Issue of the documentation")),
    '==',
]
