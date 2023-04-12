from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\DRIVERS\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
url = "https://admin-demo.nopcommerce.com/"

driver.get(url)
driver.maximize_window()

email = driver.find_element(By.ID, "Email")
email.clear()
email.send_keys("abc@gmail.com")
# password = driver.find_element(By.ID, "Password")
print("result text", email.text)
print("result get attribute()", email.get_attribute('value'))

button = driver.find_element(By.XPATH, "//button[@type='submit']")
print(f"Button text: {button.text}")
print(f"Button attribute: {button.get_attribute('value')}")
print(f"Other attribute: {button.get_attribute('class')}")
driver.close()