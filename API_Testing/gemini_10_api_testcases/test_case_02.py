#  GET Request - Invalid Resource:
#
# Description: Verify the API handles an invalid resource.
# Steps:
# Send a GET request to jsonplaceholder.typicode.com/posts/9999.
# Check for a 404 Not Found status code.
import pytest
import requests
import json


def test_status_404_api():

    base_url = "https://jsonplaceholder.typicode.com/"
    end_point = "posts/9999"
    url = base_url + end_point
    response = requests.get(url=url)

    if response.status_code != 404:
        print(response.json())
        pytest.fail(f"Unexpected status found: {response.status_code}")

