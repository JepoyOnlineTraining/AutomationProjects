import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)
driver.maximize_window()

# get browser window
curr_win_id = driver.current_window_handle
print(curr_win_id)
#  1) 6667E916E4D6E787C5EC8EFF069337A7
#  2) F736747D5CA9B86F8058192FBA4A1EF3
time.sleep(3)
print(driver.title)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(2)
mul_win_id = driver.window_handles
parent_win = mul_win_id[0]
child_win = mul_win_id[1]

driver.switch_to.window(child_win)
print(driver.title)

time.sleep(3)
driver.switch_to.window(parent_win)
print(driver.title)

time.sleep(3)
for id in mul_win_id:
    driver.switch_to.window(id)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
        driver.close()

# page titles
# page 1 OrangeHRM
# page 2 OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM
# driver.close()