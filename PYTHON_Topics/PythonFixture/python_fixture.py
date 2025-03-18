import pytest
from ..PythonFixture.python_fixture_from_other_files import *


@pytest.fixture(scope="session", autouse=True)
def open_browser():
    print(f"Openning the browser from fixture")
    yield "Something to pass for each test"
    print(f"Closing the browser from fixture")

def test_login(open_browser):
    print(open_browser)
    print("Login successfully")


def test_logout(open_browser):
    print(open_browser)
    print("Logout successfully")


def test_reservation(open_browser):
    print(open_browser)
    print("Reservation successfully")

def test_something(open_browser, setting_up_browser):
    print("Test fixture from another file")
