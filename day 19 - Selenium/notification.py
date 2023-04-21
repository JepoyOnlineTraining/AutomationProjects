from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv, options=ops)
url = "https://whatmylocation.com"
driver.get(url)
driver.maximize_window()