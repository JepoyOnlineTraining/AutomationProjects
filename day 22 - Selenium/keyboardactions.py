from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://text-compare.com/"
driver.get(url)
driver.maximize_window()

input1 = driver.find_element(By.ID, "inputText1")
input2 = driver.find_element(By.ID, "inputText2")

input1.send_keys("Welcome to Selenium")

# Ctrl + A
action = ActionChains(driver=driver)

# action.key_down(Keys.CONTROL)
# action.send_keys("a")
# action.key_up(Keys.CONTROL)
# action.perform()

action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

action.key_down(Keys.TAB).perform()

action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

