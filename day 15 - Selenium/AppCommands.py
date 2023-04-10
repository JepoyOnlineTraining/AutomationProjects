from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

url = "https://opensource-demo.orangehrmlive.com/"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(url)

title = driver.title
current_url = driver.current_url
page_source = driver.page_source

print(f"Title: {title}")
print(f"Current title: {current_url}")
print(f"Page source: {page_source}")

driver.close()
