import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)

url = "https://www.countries-ofthe-world.com/flags-of-the-world.html"
driver.get(url)
driver.maximize_window()

# Scroll by pixels
# driver.execute_script("window.scrollBy(0, 3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print(f"Number of pixels moved.  {value}")

# Scroll to view element
# time.sleep(3)
# country = driver.find_element(By.XPATH, "//img[@alt='Flag of Philippines']")
# driver.execute_script("arguments[0].scrollIntoView();", country)
# value = driver.execute_script("return window.pageYOffset;")
# print(f"Number of pixels moved.  {value}")

# Scroll to end
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(3)
driver.close()