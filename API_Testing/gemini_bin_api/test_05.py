# Description: Verify that a GET request with cookies is correctly processed and reflected in the response.
# Steps:
# Send a GET request to https://httpbin.org/cookies with cookies (e.g., cookie1=value1; cookie2=value2).
# Check that the response status code is 200 OK.
# Verify that the response body (JSON) contains the sent cookies in the "cookies" field.
import pytest
import requests
import json


def test_get_with_cookies():

    try:
        cookies = {'cookie1':'oreo', 'cookie2':'rebisco'}
        base_url = f"https://httpbin.org/cookies"
        response = requests.get(url=base_url, cookies=cookies)
        print(response.json())
        print(response.json().get('cookies').values())
        assert cookies.get('cookie1') in response.json().get('cookies').values()
        assert cookies.get('cookie2') in response.json().get('cookies').values()
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error {e}")