from ..pages.base_page import BasePage
from ..pages_locators.login_page import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.enter_text(LoginPageLocators.username_field, username)

    def enter_password(self, password):
        self.enter_text(LoginPageLocators.password_field, password)

    def click_login(self):
        self.click(LoginPageLocators.login_button)


