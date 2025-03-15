# Description: Verify retrieving a single user with a valid ID.
# Steps:
# Send a GET request to https://reqres.in/api/users/2.
# Check that the response status code is 200 OK.
# Verify the response body contains the expected user data (e.g., "email", "first_name", "last_name").
import pytest
import requests
import json
from ..utilities.common import Common


def test_single_user_valid_id():

    try:
        end_point = "api/users/2"
        com = Common()
        url = com.generate_url(endpoint=end_point)
        response = requests.get(url=url)
        print(response.json())
        if response.status_code != 200:
            pytest.fail(f"Not expected response, actual response {response.status_code}")

        response_data = response.json().get('data')

        if "email" not in response_data or "first_name" not in response_data or "last_name" not in response_data:
            pytest.fail("Either email, first_name, or last_name is not in json body")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error message {e}")