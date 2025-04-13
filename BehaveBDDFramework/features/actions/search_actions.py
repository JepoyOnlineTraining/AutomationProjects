from features.actions.common_actions import CommonActions
from features.locators.search_locators import SearchLocators

class SearchActions:

    def __init__(self, driver):
        self.driver = driver
        self.common_act = CommonActions(driver)


    def search_product(self, product):
        self.common_act.enter_text(locator=SearchLocators.search_field, text=product)

    def click_search(self):
        self.common_act.click_element(locator=SearchLocators.search_button)

    def verify_search_result(self, product):
        self.common_act.verify_text(locator=SearchLocators.product_results, actual_text=product)


    def verify_proper_message_for_non_existing_product(self):
        expected_message = "There is no product that matches the search criteria."
        self.common_act.verify_text(locator=SearchLocators.no_product_message, actual_text=expected_message)