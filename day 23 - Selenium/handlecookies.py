from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Common import Common

serv = Service(Common.chrome_path)
driver = webdriver.Chrome(service=serv)
driver.get(Common.demo_nopcommerce)
driver.maximize_window()

cookies = driver.get_cookies()
# print(cookies)
# print(len(cookies))

# # Get cookies values
# for c in cookies:
#     print(c.get('name'), ":", c.get('value'))

# Add Delete cookies
driver.add_cookie({'name':'MyCookie', 'value':'12345'})
cookies = driver.get_cookies()
print(cookies)
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print(cookies)

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))
driver.quit()
