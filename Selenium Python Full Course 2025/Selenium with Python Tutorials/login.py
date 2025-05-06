import time

from utilities.utilities import Utilities
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    browser = webdriver.Firefox()
    browser.get(Utilities.sauce_demo)
    browser.maximize_window()

    login_field = "user-name"
    password_field = "password"
    login_button = "login-button"

    browser.find_element(By.ID, login_field).send_keys(Utilities.standard_user)
    browser.find_element(By.ID, password_field).send_keys(Utilities.standard_password)
    browser.find_element(By.ID, login_button).click()

    time.sleep(2)
    assert browser.title == "Swag Labs"
    browser.quit()
