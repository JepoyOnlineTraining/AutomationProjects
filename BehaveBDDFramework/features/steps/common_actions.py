
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class CommonActions:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator)).send_keys(text)

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator)).click()

    def get_element_text(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator)).text
