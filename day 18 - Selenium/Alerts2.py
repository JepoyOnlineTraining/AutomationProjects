import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://mypage.rediff.com/login/dologin"
driver.get(url)
driver.maximize_window()


login = driver.find_element(By.XPATH, "//input[@value='Login']")
login.click()

login_prompt = driver.switch_to.alert
print(login_prompt.text)
time.sleep(2)
login_prompt.accept()
