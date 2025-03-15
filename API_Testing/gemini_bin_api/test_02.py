# PUT Request with Form Data:
#
# Description: Verify that a PUT request with form data is correctly processed.
# Steps:
# Send a PUT request to https://httpbin.org/put with form data (e.g., key1=value1&key2=value2).
# Check that the response status code is 200 OK.
# Verify that the response body (JSON) contains the sent form data in the "form" field
import pytest
import requests
import json

def test_put_request_with_form_data():

    base_url = "https://httpbin.org/put"
    pay_load = {
        "name":"Makulit Liit",
        "role":"Poging Baby"
    }

    try:
        response = requests.put(url=base_url, data=pay_load)
        assert response.status_code == 200
        print(response.json())
    except json.JSONDecodeError as e:
        pytest.fail(f"JSON error {e}")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request exception error")


def test_json():

    invalid_json = '{"name":"invalid", "age": 9"}'
    try:
        new_json = json.loads(invalid_json)
        print(new_json)
    except json.JSONDecodeError as e:
        pytest.fail(f"JSON error {e}")