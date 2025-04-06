from features.locators.common_actions import CommonActions
from features.locators.search_locators import SearchLocators

class SearchActions:

    def __init__(self, driver):
        self.driver = driver


    def search_product(self, product):
        common_act = CommonActions(self.driver)
        common_act.enter_text(locator=SearchLocators.search_field, text=product)

    def click_search(self):
        common_act = CommonActions(self.driver)
        common_act.click_element(locator=SearchLocators.search_button)

    def verify_search_result(self, product):
        common_act = CommonActions(self.driver)
        assert product in common_act.get_element_text(locator=SearchLocators.product_results)

    def verify_proper_message_for_non_existing_product(self):
        common_act = CommonActions(self.driver)
        expected_message = "There is no product that matches the search criteria."
        assert expected_message in common_act.get_element_text(locator=SearchLocators.no_product_message)