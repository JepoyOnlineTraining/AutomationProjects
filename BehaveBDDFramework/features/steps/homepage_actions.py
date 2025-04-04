from homepage_locatos import HomePageLoc
from common_actions import CommonActions

class HomePageActions:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        common_act = CommonActions(self.driver)
        common_act.click_element(HomePageLoc.my_account_link)
        common_act.click_element(HomePageLoc.login_link)

    def navigate_to_registration(self):
        common_act = CommonActions(self.driver)
        common_act.click_element(HomePageLoc.my_account_link)
        common_act.click_element(HomePageLoc.register_link)

