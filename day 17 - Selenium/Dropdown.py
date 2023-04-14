import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"

driver.get(url)
driver.maximize_window()
time.sleep(1)
dd = driver.find_element(By.TAG_NAME, "select")
dd_country = Select(dd)
# dd_country.select_by_visible_text("Philippines")
# time.sleep(1)
# dd_country.select_by_value("ALA")
# time.sleep(1)
# dd_country.select_by_index(20)
#
# # Capture all options
dd_options = dd_country.options
# print(len(dd_options))
# for d in dd_options:
#     print(f"Options: {d.text}")


# Select option without using built in function
time.sleep(2)
for d in dd_options:
    if d.text == "Philippines":
        d.click()
        break
# driver.close()

