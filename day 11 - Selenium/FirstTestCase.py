import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
url = "https://opensource-demo.orangehrmlive.com/"


# Locators
text_username_xpath = "//input[@placeholder='Username']"
text_password_xpath = "//input[@placeholder='Password']"
button_login_xpath = "//button[@type='submit']"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(url)
time.sleep(4)
driver.find_element(By.XPATH, text_username_xpath).send_keys("Admin")
driver.find_element(By.XPATH, text_password_xpath).send_keys("admin123")
driver.find_element(By.XPATH, button_login_xpath).click()
title = driver.title
print(title)
if title == "OrangeHRM":
    assert True
else:
    assert False, f"Invalid title. Actual: {title} Expected: 'OrangeHRM'"
driver.close()