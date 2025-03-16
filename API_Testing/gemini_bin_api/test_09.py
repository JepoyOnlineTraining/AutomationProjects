# GET Request with Redirect:
#
# Description: Verify that the API handles a redirect correctly.
# Steps:
# Send a GET request to https://httpbin.org/redirect/3 (3 redirects).
# Check that the final response status code is 200 OK.
# Verify that the final url is https://httpbin.org/get.
import pytest
import requests
import json


def test_get_redirect():

    try:
        base_url = "https://httpbin.org/redirect/3"
        response = requests.get(url=base_url)
        print(response.json())
        assert response.status_code == 200
        assert response.json().get('url') == 'https://httpbin.org/get'
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request Exception Error {e}")