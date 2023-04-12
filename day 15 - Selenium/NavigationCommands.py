import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


serv_obj = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
url = "https://www.snapdeal.com"
other_url = "https://amazon.com"

driver.get(url)
driver.get(other_url)
driver.maximize_window()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
driver.close()
# Navigational Commands