from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
driver.maximize_window()

alert = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
confirm = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
prompt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")

prompt.click()
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
# alertwindow.accept()
alertwindow.dismiss()

