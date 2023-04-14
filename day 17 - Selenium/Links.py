import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
url = "https://demo.nopcommerce.com/"
driver.get(url)
driver.maximize_window()
# Links
wait = WebDriverWait(driver, 10, ignored_exceptions=Exception)
# Internal Links

# Click on the link
# digi_downloads = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Digital downloads")))
# digi_downloads.click()

# # Click Partial link
# digi_down = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Digital")))
# digi_down.click()

# # Count all links on the page
# links = driver.find_elements(By.TAG_NAME, "a")
# print("Total number of links", len(links))

# Print all link text
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print("Link text", link.text)

driver.close()