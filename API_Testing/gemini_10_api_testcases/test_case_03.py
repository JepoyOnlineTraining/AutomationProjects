#
# POST Request - Create Resource:
#
# Description: Verify creating a new resource with a POST request.
# Steps:
# Send a POST request to jsonplaceholder.typicode.com/posts with a JSON payload (e.g., {"title": "Test Post", "body": "Test Body", "userId": 1}).
# Check for a 201 Created status code.
# Verify the response body contains the created resource.

import requests


def test_create_resource():

    base_url = "https://jsonplaceholder.typicode.com/"
    end_point = "posts"
    url = base_url + end_point
    payload = {"title": "Test Post from Geo", "body": "Test Body from Geo", "userId": 11}
    response = requests.post(url=url, data=payload)

    print(response.json())
    post_id = response.json().get("id")
    post_id = 3

    response_2 = requests.get(url=f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    actual_title = response_2.json().get('title')
    print(actual_title)
    # assert actual_title == "Test Post from Geo"

    # Need to delete other users to create

