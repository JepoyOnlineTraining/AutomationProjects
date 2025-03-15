#  GET User List (Invalid Page):
#
# Description: Verify the API handles an invalid page number.
# Steps:
# Send a GET request to https://reqres.in/api/users?page=999.
# Check that the response status code is 200 OK (it returns an empty array).
# Verify that the "data" array in the response is empty.
import pytest
import requests
import json


def test_invalid_page_number():

    base_url = "https://reqres.in/"
    end_point = "api/users?page=999111111"
    url = base_url + end_point

    try:
        response = requests.get(url=url)
        print(response.json())
        if len(response.json()) != 0:
           pytest.fail(f"Response is not an empty json/dictionary")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request Exception Error {e}")
    except json.JSONDecodeError as e:
        pytest.fail(f"Invalid json format {e}")