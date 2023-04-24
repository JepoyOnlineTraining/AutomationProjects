from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.ID, "dob").click()
month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
sel_month = Select(month)
sel_month.select_by_visible_text("Oct")

year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
sel_year = Select(year)
sel_year.select_by_visible_text("2011")

days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for day in days:
    if day.text == "21":
        day.click()
        break


