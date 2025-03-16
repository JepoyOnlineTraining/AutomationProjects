# Response Image Verification:
#
# Description: Verify that the API returns an image.
# Steps:
# Send a GET request to https://httpbin.org/image/png
# Verify that the response status code is 200 OK.
# Verify that the Content-Type header is image/png.
# Verify that the response body contains binary image data.
import pytest
import requests
import json

def test_get_img():

    try:
        base_url = "https://httpbin.org/image/png"
        response = requests.get(url=base_url)
        assert response.status_code == 200
        assert response.headers.get('Content-Type') == 'image/png'

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request Exception Error {e}")