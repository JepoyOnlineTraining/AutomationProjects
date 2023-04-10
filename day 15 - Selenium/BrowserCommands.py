import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/"
serv_obj = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(url)
driver.maximize_window()
time.sleep(3)
orange_link = driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc")
orange_link.click()
time.sleep(3)
parent = driver.window_handles[0]
child = driver.window_handles[1]
driver.switch_to.window(child)
driver.close()
time.sleep(3)
driver.switch_to.window(parent)
driver.close()