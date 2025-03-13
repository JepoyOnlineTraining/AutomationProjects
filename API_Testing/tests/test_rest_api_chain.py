import pytest
import requests
import json


def test_api_chaining():

    try:
        # Get data from API
        response_1 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        response_1.raise_for_status()
        data_1 = response_1.json()

        # Extract data from API
        user_id = data_1.get("userId")

        # User data from API 1 to make a requests to API 2
        response_2 = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        response_2.raise_for_status()
        data_2 = response_2.json()

        # Process the result from API 2
        print(f"User Name: {data_2.get('name')}")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error Request Exception: {e}")
    except json.JSONDecodeError as e:
        pytest.fail(f"JSON decode Error {e}")


def test_complex_api_chaining():

    try:
        post_data = {"title": "Geo Pogi Birthday", "body": "This is a test post from geo", "userId": 121}
        response_1 = requests.post("https://jsonplaceholder.typicode.com/posts", data=post_data)
        response_1.raise_for_status()
        created_post = response_1.json()
        post_id = created_post.get('id')

        update_data = {"title": "Another Birthday", "body": "This is updated data", "userId": 121}
        response_2 = requests.put(f"https://jsonplaceholder.typicode.com/posts/{post_id}", data=update_data)
        response_2.raise_for_status()


        respose_3 = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        respose_3.raise_for_status()
        updated_post = respose_3.json()

        pytest.fail(f"Updated Post Title: {updated_post.get('title')}")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error Request Exception: {e}")
    except json.JSONDecodeError as e:
        pytest.fail(f"JSON decode error {e}")
