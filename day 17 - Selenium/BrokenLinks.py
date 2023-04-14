import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
url = "http://www.deadlinkcity.com/"

driver.get(url)
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")
count = 0

for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(f"{url} is a broken link")
        count += 1
    else:
        print(f"{url} is not broken link")

print(f"Total number of broken links are {count}")
driver.close()