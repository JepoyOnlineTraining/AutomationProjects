# POST with JSON Data and Verification:
#
# Description: Verify that a POST request with JSON data is correctly processed and reflected in the response.
# Steps:
# Send a POST request to https://httpbin.org/post with a JSON payload (e.g., {"key": "value", "number": 123}).
# Check that the response status code is 200 OK.
# Verify that the response body (JSON) contains the sent JSON data in the "json" field.
# Verify that the "Content-Type" header in the response is "application/json".
import pytest
import requests
import json

def test_post_with_json_data_and_verification():
    base_url = "https://httpbin.org/post"
    pay_load = {"key":"value", "number":'123'}

    try:
        response = requests.post(url=base_url, data=pay_load)
        assert response.status_code == 200

        contents = response.json().items()
        for key, value in contents:
            print(key, value)

        form =  response.json()['form']

        if pay_load != form:
            print(f"FAILED payload: {type(pay_load)}, form: {type(form)}")
            print(f"FAILED payload: {pay_load}, form: {form}")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error Request Exception {e}")
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON")