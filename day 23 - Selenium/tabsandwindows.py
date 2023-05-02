from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Common import Common

serv = Service(Common.chrome_path)
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)
# driver.get(Common.demo_nopcommerce)
# driver.maximize_window()
# reglink = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(reglink)

# # New Tab Selenium - 4
# driver.get(Common.open_cart)
# driver.switch_to.new_window('tab')
# driver.get(Common.orange_hrm)
# driver.maximize_window()


# New Window Selenium - 4
driver.get(Common.open_cart)
driver.switch_to.new_window('window')
driver.get(Common.orange_hrm)
driver.maximize_window()
