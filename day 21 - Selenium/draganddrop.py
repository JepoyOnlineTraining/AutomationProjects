from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

url = "http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
driver.get(url)
driver.maximize_window()


oslo = driver.find_element(By.ID, "box1")
norway = driver.find_element(By.ID, "box101")

act = ActionChains(driver=driver)
act.drag_and_drop(source=oslo, target=norway).perform()

