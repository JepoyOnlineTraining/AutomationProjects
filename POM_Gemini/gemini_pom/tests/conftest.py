import pytest
from ..src.utilities.driver_manager import create_webdriver, close_browser


@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    driver = create_webdriver(request.param)
    if driver is None:
        pytest.skip(f"Skipping test for browser {request.param} due to driver creation failure")
    yield driver
    close_browser(driver)

