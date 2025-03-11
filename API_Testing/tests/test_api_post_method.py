import requests
from ..utilities.common import Common

def test_api_post_method():

    payload = {
        "name": "Jann Geo",
        "job": "Pilot"
    }

    response = requests.post(url=Common.url_create_user, data=payload)
    assert response.status_code == 201
    response_body =  response.json()
    assert response_body['name'] == payload['name']
    assert response_body['job'] == payload['job']

    print(response_body)