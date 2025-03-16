# PATCH Request with Query Parameters:
#
# Description: Verify that a PATCH request with query parameters is correctly processed.
# Steps:
# Send a PATCH request to https://httpbin.org/patch?param1=value1&param2=value2.
# Check that the response status code is 200 OK.
# Verify that the response body (JSON) contains the sent query parameters in the "args" field.
import json

import pytest
import requests


def test_patch_query_parameters():

    try:
        value1 = "water"
        value2 = "pencil"
        base_url = f"https://httpbin.org/patch?liquid={value1}&solid={value2}"
        response = requests.patch(url=base_url)
        print(response.json().get('args').values())
        print(response.json().get('args').keys())
        assert value1 in response.json().get('args').values()
        assert value2 in response.json().get('args').values()
    except requests.exceptions.RequestException as e:
        pytest.fail(e)