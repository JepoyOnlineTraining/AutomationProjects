# GET Request with Delay:
#
# Description: Verify that the API handles a delayed response correctly.
# Steps:
# Send a GET request to https://httpbin.org/delay/5 (5-second delay).
# Check that the response status code is 200 OK.
# Verify that the response is received after approximately 5 seconds.
import pytest
import requests
import json
import datetime

def test_get_with_delay():
    try:
        initial_time = datetime.datetime.now()
        base_url = "https://httpbin.org/delay/5"
        response = requests.get(url=base_url)
        current_time = datetime.datetime.now()
        response_time = current_time - initial_time
        response_time = response_time
        assert response_time > datetime.timedelta(seconds=5)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request Exception Error {e}")