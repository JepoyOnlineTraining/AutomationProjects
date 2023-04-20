import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://testautomationpractice.blogspot.com/"

driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()

driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("selenium")
driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()
time.sleep(2)

wiki_result_links = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/a")

parent_window = driver.current_window_handle

for link in wiki_result_links:
    print(link.text)
    link.click()
    time.sleep(2)
    driver.switch_to.window(parent_window)

windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    time.sleep(2)
    print(driver.title)

for window in windows:
    driver.switch_to.window(window)
    if driver.title != "Automation Testing Practice":
        driver.close()

time.sleep(2)
driver.switch_to.window(parent_window)
print(driver.title == "Automation Testing Practice")
