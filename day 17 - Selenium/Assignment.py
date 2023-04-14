import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.maximize_window()

speed = driver.find_element(By.ID, "speed")
dd_speed = Select(speed)
dd_speed.select_by_visible_text("Fast")

time.sleep(3)

text = driver.find_element(By.ID, "files")
dd_text = Select(text)
dd_text.select_by_visible_text("Other file")

time.sleep(3)

product = driver.find_element(By.ID, "products")
dd_product = Select(product)
dd_product.select_by_visible_text("Iphone")

time.sleep(3)

animals = driver.find_element(By.ID, "animals")
dd_animals = Select(animals)
dd_animals.select_by_visible_text("Avatar")

time.sleep(3)

driver.close()