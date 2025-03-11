
from ..utilities.common import Common
import requests

def test_api_get_method():

    response = requests.get(Common.url)
    if response.status_code == 200:
        print(f"Request is successfull and status is 200, {response.json()}")
    else:
        print(f"Request is not successful")

    response_data = response.json()['data']
    assert response_data['id'] == 3
