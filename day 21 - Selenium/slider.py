import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)


url = "https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/"
driver.get(url)
driver.maximize_window()

span_left = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
span_right = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")

act = ActionChains(driver=driver)

print(span_left.location)
print(span_right.location)
act.drag_and_drop_by_offset(source=span_left, xoffset=10, yoffset=0).perform()
time.sleep(1)
act.drag_and_drop_by_offset(source=span_right, xoffset=-20, yoffset=0).perform()
print("Location after moving")
print(span_left.location)
print(span_right.location)
driver.close()

