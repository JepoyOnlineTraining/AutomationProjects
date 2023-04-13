import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\DRIVERS\chromedriver.exe")
# url = "https://opensource-demo.orangehrmlive.com/"
url = "https://google.com"

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("selenium")
search.submit()
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
driver.close()