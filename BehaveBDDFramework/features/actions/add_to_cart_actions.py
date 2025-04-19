import time

from features.actions.common_actions import CommonActions
from features.locators.add_to_cart_locators import AddToCartLoc

class AddToCartActions:

    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)


    def click_product_cart_button(self):
        self.common_actions.click_element(locator=AddToCartLoc.iphone_add_to_cart_button)
        time.sleep(3)

    def select_iphone(self):
        self.common_actions.click_element(locator=AddToCartLoc.iphone_image)

    def add_multiple_product(self):
        self.common_actions.enter_text(locator=AddToCartLoc.quantity_field, text="2")
        self.common_actions.click_element(locator=AddToCartLoc.product_add_to_cart_button)
        time.sleep(2)

    def verify_product_added(self):
        self.common_actions.verify_text(locator=AddToCartLoc.cart_button, expected_text="1")
        self.empty_cart()
        self.verify_empty_cart()

    def empty_cart(self):
        self.common_actions.click_element(locator=AddToCartLoc.cart_button)
        self.common_actions.click_element(locator=AddToCartLoc.remove_button)

    def verify_empty_cart(self):
        time.sleep(3)
        self.common_actions.verify_text(locator=AddToCartLoc.cart_button, expected_text="0")

    def verify_multiple_product_added(self):
        self.common_actions.verify_text(locator=AddToCartLoc.cart_button, expected_text="2")
        self.empty_cart()
        self.verify_empty_cart()