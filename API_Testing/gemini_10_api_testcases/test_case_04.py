# POST Request - Missing Required Field:
#
# Description: Verify the API handles a POST request with missing required fields.
# Steps:
# Send a POST request to jsonplaceholder.typicode.com/posts without the "title" field.
# Check for a 400 Bad Request status code.
# Verify the error message in the response body.
import requests


def test_missing_required_field():

    payload = {"body": "Test Body from Geo"}
    response = requests.post(url="https://jsonplaceholder.typicode.com/posts", data=payload)
    print(response.headers.get("Content-Type",""))
    print(response.json())
    assert response.status_code == 400