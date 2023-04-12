from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(executable_path="C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
url = "https://demo.nopcommerce.com/"

driver.get(url)
driver.maximize_window()

# find_element()
# return single web element

# Scenario 1) Locator matching single web element
#
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook")

# Scenario 2) Locator matching multiple web elements

# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text)

# Scenario 3) Locator not matching any elements then throw NoSuchElementException
#
# element = driver.find_element(By.LINK_TEXT, "Log")
# element.click()


# find_elements()
# # Scenario 1) Locator matching single web element
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))
# print(elements[0].send_keys("Apple MacBook"))
# for element in elements:
#     element.send_keys("Apple MacBook")

# # Scenario 2) Locator matching multiple web element
# elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements))
# for element in elements:
#     print(element.text)

# Scenario 3) Locator not matching
elements = driver.find_elements(By.LINK_TEXT, "Log")
print(f"elements returned: {len(elements)}")

driver.close()