import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://jqueryui.com/datepicker/"
driver.get(url)
driver.maximize_window()

frame1 = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(frame1)

# mm/dd/yyyy
# driver.find_element(By.ID, "datepicker").send_keys("05/30/2020")

# specific month without send_keys
month = "October"
day = "21"
year = "2019"
driver.find_element(By.ID, "datepicker").click()

while True:
    mon = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    yr = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
    if mon == month and yr == year:
        break
    else:
        # Select Preivous Date
        driver.find_element(By.XPATH, "//a[contains(@class,'ui-datepicker-prev')]").click()
        # Select Future Date
        # driver.find_element(By.XPATH, "//a[contains(@class,'ui-datepicker-next')]").click()


cal_day = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody//a")

for i in cal_day:
    if i.text == day:
        i.click()
        break

