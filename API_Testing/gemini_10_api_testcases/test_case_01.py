

# 1. GET Request - Basic Success:
#
# Description: Verify a successful GET request to retrieve data.
# Steps:
# Send a GET request to jsonplaceholder.typicode.com/posts/1.
# Check for a 200 OK status code.
# Verify the response body contains the expected data (e.g., "userId": 1, "id": 1, etc.).

import requests
import json
from ..utilities.common import Common

def test_get_request():

    base_url = "https://jsonplaceholder.typicode.com/"
    end_point = "posts/1"
    response = requests.get(url=base_url + end_point)

    try:
       if "application/json" in response.headers.get("Content-Type", ""):
           print("PASSED")
       else:
           print("FAILED")
    except requests.exceptions.RequestException as e:
        print(f"Error message {e}")


    if isinstance(response.json(), dict):
        print(f"PASSED json response body is a json")
    else:
        print(f"FAILED response is not a json body")

    assert 1 == response.json()['userId']
    assert 1 == response.json()['id']
