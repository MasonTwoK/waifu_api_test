import pytest

tags_groups = ['versatile', 'nsfw']
nsfw_tags = ['ass', 'hentai', 'milf', 'oral', 'paizuri', 'ecchi', 'ero']
versatile_tags = ['maid', 'waifu', 'marin-kitagawa', 'mori-calliope', 'raiden-shogun', 'oppai', 'selfies', 'uniform',
                  'kamisato-ayaka']
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
