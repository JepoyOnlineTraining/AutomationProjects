import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
url = "https://opensource-demo.orangehrmlive.com/"


# Locators
text_username_css = "input[placeholder='Username']"
text_password_css = "input[placeholder='Password']"
button_login_css = "button[type='submit']"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(url)
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, text_username_css).send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, text_password_css).send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, button_login_css).click()
title = driver.title
print(title)
if title == "OrangeHRM":
    print("Test Pass")
    assert True
else:
    assert False, f"Invalid title. Actual: {title} Expected: 'OrangeHRM'"
driver.close()