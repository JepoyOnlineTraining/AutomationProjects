from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://admin-demo.nopcommerce.com/"
serv_obj = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get(url)
driver.maximize_window()

# Conditional commands return True or False
# is_displayed()   is_enabled()

username = driver.find_element(By.ID, "Email")
remember = driver.find_element(By.ID, "RememberMe")
print("Enable status", username.is_enabled())
print("Display status", username.is_displayed())
print("Checkbox status", remember.is_selected())

remember.click()
print("Checkbox status", remember.is_selected())
print()

driver.close()





