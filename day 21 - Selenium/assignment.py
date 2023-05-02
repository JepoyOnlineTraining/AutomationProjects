import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://testautomationpractice.blogspot.com/"

driver.get(url)
driver.maximize_window()
acts = ActionChains(driver=driver)

field1 = driver.find_element(By.ID, "field1")
field2 = driver.find_element(By.ID, "field2")

copy_text_button = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
acts.double_click(copy_text_button).perform()

if field1.get_attribute("value") == field2.get_attribute("value"):
    print(f"field 1: {field1.get_property('value')} field 2: {field2.get_property('value')}")
    assert True, "Passed"
else:
    assert False, f"field 1: {field1.get_property('value')} field 2: {field2.get_property('value')}"

drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")

time.sleep(2)
acts.drag_and_drop(source=drag, target=drop).perform()
time.sleep(2)

slider = driver.find_element(By.ID, "slider")
driver.execute_script("arguments[0].scrollIntoView();", slider)
time.sleep(2)
acts.drag_and_drop_by_offset(slider, 0, 200).perform()
time.sleep(2)

driver.close()