from selenium.webdriver.common.by import By


class LoginPageLocators:

    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    items = (By.CSS_SELECTOR, "div.inventory_item")