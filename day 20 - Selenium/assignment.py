import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


serv = Service("C:\DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"

driver.get(url)
driver.maximize_window()

# Select price details
prices = driver.find_elements(By.XPATH, "//div[@id='opc-product-selection']//li/label")
price_opt = 2
prices[price_opt].click()
selected_price = driver.find_element(By.XPATH, "//div[@id='opc-product-selection']//li["+ str(price_opt + 1) +"]/span[@class='price']")
print(selected_price.text)

driver.find_element(By.ID, "travname").send_keys("Jann")
driver.find_element(By.ID, "travlastname").send_keys("Clay")


driver.find_element(By.ID, "dob").click()
month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
sel_month = Select(month)
sel_month.select_by_visible_text("Oct")

year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
sel_year = Select(year)
sel_year.select_by_visible_text("2011")

days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for day in days:
    if day.text == "21":
        day.click()
        break

driver.find_element(By.ID, "sex_1").click()
driver.find_element(By.ID, "traveltype_2").click()
driver.find_element(By.ID, "fromcity").send_keys("Pasig")
driver.find_element(By.ID, "tocity").send_keys("Pasig")

driver.find_element(By.ID, "departon").click()
month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
sel_month = Select(month)
sel_month.select_by_visible_text("Oct")

year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
sel_year = Select(year)
sel_year.select_by_visible_text("2023")

days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for day in days:
    if day.text == "21":
        day.click()
        break


driver.find_element(By.ID, "returndate").click()
month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
sel_month = Select(month)
sel_month.select_by_visible_text("Oct")

year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
sel_year = Select(year)
sel_year.select_by_visible_text("2023")

days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for day in days:
    if day.text == "25":
        day.click()
        break


driver.find_element(By.ID, "billing_phone").send_keys("12345678910")
driver.find_element(By.ID, "billing_email").send_keys("test@gmail.com")

driver.find_element(By.ID, "select2-billing_country-container").click()
# country = Select(countries)
# country.select_by_visible_text("Philippines")

countries_options = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
for country in countries_options:
    if country.text == "Philippines":
        country.click()
        break


driver.find_element(By.ID, "billing_address_1").send_keys("123445")
driver.find_element(By.ID, "billing_city").send_keys("City")

driver.find_element(By.ID, "select2-billing_state-container").click()
states = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_state-results']/li")
for state in states:
    if state.text == "Albay":
        state.click()
        break


driver.find_element(By.ID, "billing_postcode").send_keys("1602")

time.sleep(4)

total = driver.find_element(By.XPATH, "//td[@class='product-total']").text

if total == selected_price.text:
    print(f"actual: {total}, expected: {selected_price.text}")
    print("Test Passed")
    assert True
else:
    print(f"actual: {total}, expected: {selected_price.text}")
    assert False, "Test Failed"

driver.close()