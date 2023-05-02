import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Common import Common

serv = Service(Common.chrome_path)
driver = webdriver.Chrome(service=serv)
driver.get(Common.monster)
driver.maximize_window()

driver.find_element(By.XPATH, "//div[contains(@class,'heroSection-buttonContainer_secondaryBtn ')]").click()
time.sleep(3)
driver.find_element(By.ID, "file-upload").send_keys(Common.resume_path)