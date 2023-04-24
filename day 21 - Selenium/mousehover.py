import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://testsigma.com/"

driver.get(url)
driver.maximize_window()
time.sleep(3)

product = driver.find_element(By.XPATH, "//a[@class='nav_link' and text()='Product']")
resources = driver.find_element(By.XPATH, "//a[@class='nav_link' and text()='Resources']")
open_source = driver.find_element(By.XPATH, "//a[@class='nav_link' and text()='Open Source ']")

# Mouse hover actions

actions = ActionChains(driver=driver)
actions.move_to_element(product).move_to_element(resources).move_to_element(open_source).perform()