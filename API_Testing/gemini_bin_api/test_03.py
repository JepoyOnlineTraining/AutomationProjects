# DELETE Request with Custom Headers:
#
# Description: Verify that a DELETE request with custom headers is correctly processed.
# Steps:
# Send a DELETE request to https://httpbin.org/delete with custom headers (e.g., X-Custom-Header: Test).
# Check that the response status code is 200 OK.
# Verify that the response body (JSON) contains the sent custom header in the "headers" field.
import pytest
import requests
import json


def test_delete_request():

    try:
        base_url = "https://httpbin.org/delete"
        header = {'X-Geo-Heder': 'Geo'}
        response = requests.delete(url=base_url, headers=header)
        assert response.status_code == 200

        response_headers = response.json().get('headers')
        print(response_headers)
        assert 'X-Geo-Heder' in response_headers
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request Exception Error {e}")
    except json.JSONDecodeError as e:
        pytest.fail(f"JSON Error {e}")