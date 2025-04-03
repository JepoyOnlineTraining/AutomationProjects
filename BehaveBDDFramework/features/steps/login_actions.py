
from login_locators import LoginLoc
from common_actions import CommonActions
from homepage_locatos import HomePageLoc

class LoginActions:

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self, username, password):
        common_act = CommonActions(self.driver)
        common_act.enter_text(locator=LoginLoc.email_field, text=username)
        common_act.enter_text(locator=LoginLoc.password_field, text=password)

    def verify_my_account(self, text):
        common_act = CommonActions(self.driver)
        expected_text = common_act.get_element_text(locator=HomePageLoc.error_message)
        print(f"Expected: {text}")
        print(f"Actual: {expected_text}")
        assert text in expected_text

    def click_login_btn(self):
        common_act = CommonActions(self.driver)
        common_act.click_element(locator=LoginLoc.login_button)



