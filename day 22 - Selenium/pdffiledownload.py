import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from Common import Common
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

location = os.getcwd()

print(location)


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv = Service(Common.chrome_path)
    pref = {"download.default_directory": location,
            "plugins.always_open_pdf_externally": True}

    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", pref)
    driver = webdriver.Chrome(service=serv, options=ops)
    return driver


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv = Service(Common.edge_path)
    pref = {"download.default_directory": location,
            "plugins.always_open_pdf_externally": True}
    ops = webdriver.EdgeOptions()
    ops.add_argument("--disable-notifications")
    ops.add_experimental_option("prefs", pref)
    driver = webdriver.Edge(service=serv, options=ops)
    return driver


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv = Service(Common.firefox_path)
    # pref = {"download.default_directory": location}
    ops = webdriver.FirefoxOptions()
    ops.add_argument("--disable-notifications")
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0 - desktop , # 1 - download , # 2 - desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(service=serv, options=ops)
    return driver


driver = firefox_setup()
# driver = firefox_setup()
act = ActionChains(driver=driver)
driver.get(Common.prd_dwnld_url)
driver.maximize_window()
time.sleep(4)
doc_1 = driver.find_element(By.XPATH, "//table[@id='table-files']//tbody/tr[1]//a")
driver.execute_script("arguments[0].scrollIntoView();", doc_1)
time.sleep(2)
driver.execute_script("arguments[0].click();", doc_1)

time.sleep(2)

if driver.find_element(By.ID, "aswift_3"):
    driver.switch_to.frame("aswift_3")
    if driver.find_element(By.ID, "ad_iframe"):
        driver.switch_to.frame("ad_iframe")
        element = driver.find_elements(By.ID, "dismiss-button")
        if len(element) > 0:
            driver.find_element(By.ID, "dismiss-button").click()
        else:
            driver.switch_to.default_content()
            driver.switch_to.frame("aswift_3")
            if driver.find_element(By.ID, "dismiss-button"):
                driver.find_element(By.ID, "dismiss-button").click()





time.sleep(10)
driver.close()
