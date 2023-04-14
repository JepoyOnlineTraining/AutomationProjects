from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
url = "https://itera-qa.azurewebsites.net/home/automation"

driver.get(url)
driver.maximize_window()

# 1) Select specific checkbox
# checkbox1 = driver.find_element(By.ID, "tuesday")
# checkbox1.click()


# 2) Select multiple checkboxes
# # Approach 1
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input' ]")
# for check in checkboxes:
#     check.click()
#
# for uncheck in checkboxes:
#     uncheck.click()

# # 3) select multiple checkboxes by choice
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input' ]")
# for check in checkboxes:
#     if check.get_attribute('id') in ['monday', 'tuesday']:
#         check.click()

# 4) select last 2 checkboxes
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input' ]")
# for i in range(len(checkboxes) - 2, len(checkboxes)):
#     checkboxes[i].click()

# driver.close()
# # 5) select first 2 checkboxes
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input' ]")
# for i in range(0, 2):
#     checkboxes[i].click()

# 6) Clearing all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='form-check-input' ]")
for check in checkboxes:
    if check.is_selected():
        check.click()