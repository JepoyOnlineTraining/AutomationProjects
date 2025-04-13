
from features.locators.login_locators import LoginLoc
from features.actions.common_actions import CommonActions
from features.locators.homepage_locatos import HomePageLoc

class LoginActions:

    def __init__(self, driver):
        self.driver = driver
        self.common_act = CommonActions(self.driver)

    def enter_credentials(self, username, password):
        self.common_act.enter_text(locator=LoginLoc.email_field, text=username)
        self.common_act.enter_text(locator=LoginLoc.password_field, text=password)

    def verify_my_account(self, text):
        self.common_act.verify_text(locator=HomePageLoc.home_page_content, expected_text=text)


    def click_login_btn(self):
        self.common_act.click_element(locator=LoginLoc.login_button)


    def verify_registration_page(self, text):
        self.common_act.verify_text(locator=HomePageLoc.home_page_content, actual_text=text)


    def enter_registration_details(self, firstname, lastname, email, telephone, password):
        self.common_act.enter_text(locator=LoginLoc.firstname_field, text=firstname)
        self.common_act.enter_text(locator=LoginLoc.lastname_field, text=lastname)
        self.common_act.enter_text(locator=LoginLoc.reg_email_field, text=email)
        self.common_act.enter_text(locator=LoginLoc.phone_field, text=telephone)
        self.common_act.enter_text(locator=LoginLoc.reg_pass_field, text=password)
        self.common_act.enter_text(locator=LoginLoc.reg_confirm_pass_field, text=password)

    def continue_registration(self):
        self.common_act.click_element(locator=LoginLoc.agree_to_terms_checkbox)
        self.common_act.click_element(locator=LoginLoc.continue_button)

    def verify_account_creation(self, text):
        self.common_act.verify_text(locator=HomePageLoc.home_page_content, actual_text=text)

    def verify_duplicate_account_message(self, text):
        self.common_act.verify_text(locator=HomePageLoc.error_message, actual_text=text)

    def verify_empty_error_message(self, firstname_err, lastname_err, email_err, phone_err, pass_err):
        self.common_act.verify_text(locator=LoginLoc.firstname_error_message, actual_text=firstname_err)
        self.common_act.verify_text(locator=LoginLoc.lastname_error_message, actual_text=lastname_err)
        self.common_act.verify_text(locator=LoginLoc.reg_email_error_message, actual_text=email_err)
        self.common_act.verify_text(locator=LoginLoc.phone_error_message, actual_text=phone_err)
        self.common_act.verify_text(locator=LoginLoc.reg_password_error_message, actual_text=pass_err)

