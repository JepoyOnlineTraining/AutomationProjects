
from features.locators.login_locators import LoginLoc
from features.locators.common_actions import CommonActions
from features.locators.homepage_locatos import HomePageLoc

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


    def verify_registration_page(self, text):
        common_act = CommonActions(self.driver)
        expected_text = common_act.get_element_text(locator=HomePageLoc.home_page_content)
        print(f"Expected: {text}")
        print(f"Actual: {expected_text}")
        assert text in expected_text


    def enter_registration_details(self, firstname, lastname, email, telephone, password):
        common_act = CommonActions(self.driver)
        common_act.enter_text(locator=LoginLoc.firstname_field, text=firstname)
        common_act.enter_text(locator=LoginLoc.lastname_field, text=lastname)
        common_act.enter_text(locator=LoginLoc.reg_email_field, text=email)
        common_act.enter_text(locator=LoginLoc.phone_field, text=telephone)
        common_act.enter_text(locator=LoginLoc.reg_pass_field, text=password)
        common_act.enter_text(locator=LoginLoc.reg_confirm_pass_field, text=password)

    def continue_registration(self):
        common_act = CommonActions(self.driver)
        common_act.click_element(locator=LoginLoc.agree_to_terms_checkbox)
        common_act.click_element(locator=LoginLoc.continue_button)

    def verify_account_creation(self, text):
        common_act = CommonActions(self.driver)
        expected_text = common_act.get_element_text(locator=HomePageLoc.home_page_content)
        print(f"Expected: {text}")
        print(f"Actual: {expected_text}")
        assert text in expected_text


    def verify_duplicate_account_message(self, text):
        common_act = CommonActions(self.driver)
        expected_text = common_act.get_element_text(locator=HomePageLoc.error_message)
        print(f"Expected: {text}")
        print(f"Actual: {expected_text}")
        assert text in expected_text


    def verify_empty_error_message(self, firstname_err, lastname_err, email_err, phone_err, pass_err):
        common_act = CommonActions(self.driver)
        assert firstname_err in common_act.get_element_text(LoginLoc.firstname_error_message)
        assert lastname_err in common_act.get_element_text(LoginLoc.lastname_error_message)
        assert email_err in common_act.get_element_text(LoginLoc.reg_email_error_message)
        assert phone_err in common_act.get_element_text(LoginLoc.phone_error_message)
        assert pass_err in common_act.get_element_text(LoginLoc.reg_password_error_message)