from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
driver.get(url)
driver.maximize_window()

button = driver.find_element(By.XPATH, "//span[text()='right click me']")
act = ActionChains(driver=driver)
act.context_click(button).perform()

edit = driver.find_element(By.XPATH, "//li[contains(@class,'context-menu-icon-edit')]")
act.context_click(edit).perform()
alrt = driver.switch_to.alert
alrt.accept()

act.context_click(button).perform()
