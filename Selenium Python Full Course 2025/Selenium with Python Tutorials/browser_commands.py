import time

from utilities.utilities import Utilities
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_browser_commands():

    browser = webdriver.Firefox()
    browser.get(Utilities.orange_site)
    browser.maximize_window()

    time.sleep(10)

    # browser.fullscreen_window()

    login_field = "input[name='username']"
    password_field = "input[name='password']"
    login_button = "button.orangehrm-login-button"

    browser.find_element(By.CSS_SELECTOR, login_field).send_keys(Utilities.username)
    browser.find_element(By.CSS_SELECTOR, password_field).send_keys(Utilities.password)
    browser.find_element(By.CSS_SELECTOR, login_button).click()

    time.sleep(10)

    assert browser.title == "OrangeHRM"

    browser.back()

    time.sleep(3)

    browser.forward()

    time.sleep(3)

    assert browser.title == "OrangeHRM"

    browser.quit()

