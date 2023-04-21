import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://opensource-demo.orangehrmlive.com"

driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(5)
driver.find_element(By.XPATH, "//a[contains(@href,'AdminModule')]").click()

num_rows = len(
    driver.find_elements(By.XPATH, "//div[@class='oxd-table']//div[@class='oxd-table-body']//div[@role='row']"))
# name = driver.find_elements(By.XPATH, "//div[@class='oxd-table']//div[@class='oxd-table-body']/div[1]//div[@role='row']/div[2]")
# status = driver.find_elements(By.XPATH, "//div[@class='oxd-table']//div[@class='oxd-table-body']/div[1]//div[@role='row']/div[5]")
time.sleep(5)
for i in range(1, num_rows + 1):
    status = driver.find_element(By.XPATH,
                                 "//div[@class='oxd-table']//div[@class='oxd-table-body']/div[" + str(
                                     i) + "]//div[@role='row']/div[5]/div").text
    if status == "Enabled":
        name = driver.find_element(By.XPATH,
                                   "//div[@class='oxd-table']//div[@class='oxd-table-body']/div[" + str(
                                       i) + "]//div[@role='row']/div[2]/div").text
        print(f"{name} status is {status}")
