import time

from ..src.pages.login_page import LoginPage



def test_login_success(driver):
    login_page = LoginPage(driver=driver)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    time.sleep(1)
    assert "inventory" in driver.current_url
    login_page.verify_text(text='Sauce Labs Backpack')

