# POST Request with File Upload:
#
# Description: Verify that a POST request with a file upload is correctly processed.
# Steps:
# Create a text file (e.g., test.txt) with some content.
# Send a POST request to https://httpbin.org/post with the file attached as a form field.
# Check that the response status code is 200 OK.
# Verify that the response body (JSON) contains the file content in the "files" field.a


import requests
import pytest

def test_post_file_upload():
    try:
        base_url = "https://httpbin.org/post"
        file_name = "API_Testing/gemini_bin_api/sample.txt"
        with open(file_name, "rb") as f:
            files = {"file": f}
            response = requests.post(url=base_url, files=files)
            assert response.status_code == 200
            assert "Testing" in response.json().get('files').values()
            print(response.json())
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error {e}")