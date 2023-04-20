import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://demo.automationtesting.in/Frames.html"
driver.get(url)
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()
main_iframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(main_iframe)

sub_frame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(sub_frame)

driver.find_element(By.XPATH, "//input").send_keys("Switch Success!!")

driver.switch_to.parent_frame()

time.sleep(3)
driver.close()