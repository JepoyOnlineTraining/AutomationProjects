from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
url = "https://google.com"

my_wait = WebDriverWait(driver, 10)

driver.get(url)
driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("selenium")
search.submit()

selenium_link = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
selenium_link.click()
driver.close()