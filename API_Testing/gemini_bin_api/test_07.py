# GET Request with Basic Authentication:
#
# Description: Verify that a GET request with Basic Authentication is correctly processed.
# Steps:
# Send a GET request to https://httpbin.org/basic-auth/user/passwd with Basic Authentication credentials (username: "user", password: "passwd").
# Check that the response status code is 200 OK.
# Verify that the response body (JSON) contains the "authenticated": true field.
import pytest
import requests
import json

def test_get_request_with_authentication():

    try:
        base_url = "https://httpbin.org/basic-auth/user/passwd"
        username = 'user'
        password = 'passwd'
        response = requests.get(url=base_url, auth=(username, password))

        assert response.status_code == 200
        print(response.json())
        assert response.json().get('authenticated') == True
        assert response.json().get('user') == 'user'

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request Exception Error: {e}")