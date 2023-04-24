import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick"
driver.get(url)
driver.maximize_window()

driver.switch_to.frame("iframeResult")
dclick = driver.find_element(By.XPATH, "//button[text()='Double-click me']")

act = ActionChains(driver=driver)
act.double_click(dclick).perform()

time.sleep(2)
demo = driver.find_element(By.ID, "demo")

if demo:
    print("Passed")
    print(f"{demo.text} is display")
else:
    assert False, "Hello World is not display"

driver.close()