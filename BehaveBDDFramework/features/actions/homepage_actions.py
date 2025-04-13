from features.locators.homepage_locatos import HomePageLoc
from features.actions.common_actions import CommonActions

class HomePageActions:

    def __init__(self, driver):
        self.driver = driver
        self.common_act = CommonActions(driver)

    def navigate_to_login_page(self):
        self.common_act.click_element(HomePageLoc.my_account_link)
        self.common_act.click_element(HomePageLoc.login_link)

    def navigate_to_registration(self):
        self.common_act.click_element(HomePageLoc.my_account_link)
        self.common_act.click_element(HomePageLoc.register_link)

