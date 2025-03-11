import requests




def test_rest_api():
    base_url = "https://reqres.in/"
    endpoint = "api/users/"
    url = base_url + endpoint

    parameters = {
        "page":"2"
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        print(f"PASSED, {response.json()}")
    else:
        print(f"FAILED")