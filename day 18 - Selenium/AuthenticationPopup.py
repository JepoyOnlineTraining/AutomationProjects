from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(3)
url = "http://the-internet.herokuapp.com/basic_auth"
bypass_url = "http://admin:admin@the-internet.herokuapp.com/basic_auth"
# Syntax to inject username and password to bypass javascript authentication
# http://username:password@test.com
driver.get(bypass_url)
welcome_msg = driver.find_element(By.XPATH, "//p")
if welcome_msg.text == "Congratulations! You must have the proper credentials.":
    assert True
else:
    assert False, "User not authorize"
driver.maximize_window()