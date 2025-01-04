# Tests for page - https://docs.waifu.im/reference/api-reference/report

import pytest
import requests


@pytest.mark.skip(reason="BUG #1: Error 400. User is enable to create a report")
def test_post_report():
    auth_token = 'Bearer 8E0O1m-_ebI8TAHe_xlemUmSCvDp0_Ey9sr4TewWq4a1lc_uDf6hr2A-d-oaCXq5_Ta1QPTGZnAMiZZ_nbyjy4zUwY8UVu2cCsGxxaVNEEKEPGB-gPEL7rYhXpy3WDMiZpwyJ36Kdhe8IaLwCqTV8ahTnOx9ArWgezVjIkqRFj0'

    headers = {
        'Accept-Version': 'v5',
        'Authorization':auth_token,
        'Content-Type': 'application/json',
    }

    data = {
        'image_id': 8008,
        'description': 'Lol'
    }

    response = requests.post(url="https://api.waifu.im/report", headers=headers, data=data)
    assert response.status_code == 200
