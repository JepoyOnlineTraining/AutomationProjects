
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class CommonActions:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        self.locate_element(locator=locator).send_keys(text)

    def click_element(self, locator):
        self.locate_element(locator=locator).click()

    def get_element_text(self, locator):
        return self.locate_element(locator=locator).text

    def locate_element(self, locator):
        return WebDriverWait(self.driver, 50).until(ec.presence_of_element_located(locator=locator))