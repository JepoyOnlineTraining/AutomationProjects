import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
url = "https://money.rediff.com/gainers/bse/daily/groupa"


# Locators
text_username_css = "input[placeholder='Username']"
text_password_css = "input[placeholder='Password']"
button_login_css = "button[type='submit']"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(url)


# self
text = driver.find_element(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/self::a").text
print(f"self: {text}")

# Parent
parent = driver.find_element(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/parent::td").text
print(f"parent: {parent}")


# Childs
childs = driver.find_elements(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/ancestor::tr/child::td")
print(f"Total number of elements: {len(childs)}")
for child in childs:
    print(f"child element {child.text}")

# Ancestors
ancestor = driver.find_element(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/ancestor::tr").text
print(f"Ancestor element: {ancestor}")

# Descendant
descendant = driver.find_elements(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/ancestor::tr/descendant::*")
print(f"Descendant count: {len(descendant)}")

# Following
following = driver.find_elements(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/ancestor::tr/following::*")
print(f"Following count: {len(following)}")

# Following::Sibling
following_sibling = driver.find_elements(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/ancestor::tr/following-sibling::*")
print(f"Following sibling count: {len(following_sibling)}")

# Preceding
preceding = driver.find_elements(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/ancestor::tr/preceding::*")
print(f"Preceding {len(preceding)}")

# Preceding::Sibling
preceding_sibling = driver.find_elements(By.XPATH, "//a[contains(text(),'Indiabulls Real Esta')]/ancestor::tr/preceding-sibling::*")
print(f"Preceding-sibling {len(preceding_sibling)}")
driver.close()