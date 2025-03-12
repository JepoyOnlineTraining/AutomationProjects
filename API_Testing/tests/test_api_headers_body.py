import requests
import json
from ..utilities.common import Common


def test_api_headers_body():

    response = requests.get(Common.url)

    # Check if header is a json
    assert "application/json" in response.headers.get("Content-Type", "")

    # Check the response body if a json python
    assert isinstance(response.json(),dict)
