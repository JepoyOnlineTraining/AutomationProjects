import time

from selenium import webdriver


def test_browser():
        browser = webdriver.Firefox()
        browser.get("https://selenium.dev")
        browser.maximize_window()
        time.sleep(3)
        assert browser.title == "Selenium1"
        browser.quit()