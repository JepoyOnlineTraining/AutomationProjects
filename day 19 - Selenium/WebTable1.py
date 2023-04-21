import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://testautomationpractice.blogspot.com/"

driver.get(url)
driver.maximize_window()

# Count number of rows and columns
time.sleep(3)
num_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
num_of_col = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))

col = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th")
row = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")

print(f"Number of columns: {num_of_col}")
print(f"Number of rows: {num_of_rows}")

# Read specific data in the table
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(f"Specific data in the table --> {data}")

# Read all the rows and column data
print("Printing all data")
for r in range(2, num_of_rows + 1):
    for c in range(1, num_of_col + 1):
        data = driver.find_element(By.XPATH,
                                   "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(data, end="           ")
    print()


# Read data base on conditions
for r in range(2, num_of_rows + 1):
    author = driver.find_element(By.XPATH,
                                   "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if author == "Mukesh":
        book = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(f"This is Mukesh book: {book} and price is {price}")


driver.close()