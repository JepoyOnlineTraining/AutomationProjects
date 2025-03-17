import pytest


@pytest.fixture()
def setting_up_browser():
    print("Browser setup successfully")
    yield
    print("Browser is closing")