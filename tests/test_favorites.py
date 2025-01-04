# Tests for page - https://docs.waifu.im/reference/api-reference/favorites

import pytest
import requests


@pytest.mark.skip(reason="TBD. Q: How to put Bearer Token to requests.get()")
def test_get_favorites():
    auth_token = 'Bearer 8E0O1m-_ebI8TAHe_xlemUmSCvDp0_Ey9sr4TewWq4a1lc_uDf6hr2A-d-oaCXq5_Ta1QPTGZnAMiZZ_nbyjy4zUwY8UVu2cCsGxxaVNEEKEPGB-gPEL7rYhXpy3WDMiZpwyJ36Kdhe8IaLwCqTV8ahTnOx9ArWgezVjIkqRFj0'

    headers = {
        'Accept-Version': 'v5',
        'Authorization': auth_token
    }

    response = requests.get(url="https://api.waifu.im/fav", headers=headers)
    assert response.status_code == 200
