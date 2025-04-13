from execnet.gateway_base import serve
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class CommonActions:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        self.locate_element(locator=locator).send_keys(text)

    def click_element(self, locator):
        self.locate_element(locator=locator).click()

    def right_click_element(self, locator):
        actions = ActionChains(self.driver)
        actions.context_click(on_element=self.locate_element(locator=locator)).perform()

    def get_element_text(self, locator):
        return self.locate_element(locator=locator).text

    def locate_element(self, locator):
        return WebDriverWait(self.driver, 50).until(ec.presence_of_element_located(locator=locator))


    def verify_text(self, locator, expected_text):
        actual_text = self.get_element_text(locator=locator)
        print(f"Actual Text: {actual_text}")
        print(f"Expected Text: {expected_text}")
        assert expected_text in actual_text, f"Expected Text {expected_text} is not in {actual_text}"