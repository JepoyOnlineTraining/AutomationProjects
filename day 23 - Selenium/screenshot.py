import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Common import Common

serv = Service(Common.chrome_path)
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)
driver.get(Common.demo_nopcommerce)
driver.maximize_window()
print(os.getcwd())
driver.save_screenshot(os.getcwd() + "\\homepage.png")
driver.get_screenshot_as_file(os.getcwd() + "\\homepage_save_as_file.png")
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_png()
driver.close()