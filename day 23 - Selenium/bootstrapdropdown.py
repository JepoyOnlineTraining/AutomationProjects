import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Common import Common

serv = Service(Common.chrome_path)
driver = webdriver.Chrome(service=serv)


driver.get(Common.dummy_ticket)
driver.maximize_window()
time.sleep(2)
# handle dropdown
dd = driver.find_element(By.ID, "select2-billing_country-container")
action = ActionChains(driver=driver)
action.move_to_element(dd).click().perform()

countries = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

for county in countries:
    if county.text == "Norway":
        county.click()
        break


time.sleep(2)
driver.close()
