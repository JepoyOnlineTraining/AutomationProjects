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
    pref = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", pref)
    driver = webdriver.Chrome(service=serv, options=ops)
    return driver


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv = Service(Common.edge_path)
    pref = {"download.default_directory": location}
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
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2) # 0 - desktop , # 1 - download , # 2 - desired location
    ops.set_preference("browser.download.dir", location)
    driver = webdriver.Firefox(service=serv, options=ops)
    return driver



# driver = chrome_setup()
driver = firefox_setup()
act = ActionChains(driver=driver)
driver.get(Common.download_url)
driver.maximize_window()
time.sleep(4)
doc_1 = driver.find_element(By.XPATH, "//table[@id='table-files']//tbody/tr[1]//a")
driver.execute_script("arguments[0].scrollIntoView();", doc_1)
time.sleep(2)
driver.execute_script("arguments[0].click();", doc_1)

time.sleep(2)

if driver.find_element(By.ID, "aswift_3"):
    driver.switch_to.frame("aswift_3")
    if driver.find_element(By.ID, "ad_iframe") is not None:
        driver.switch_to.frame("ad_iframe")
    else:
        driver.switch_to.default_content()
        driver.switch_to.frame("aswift_4")
        driver.switch_to.frame("ad_iframe")
else:
    driver.switch_to.frame("aswift_4")
    driver.switch_to.frame("ad_iframe")

# iframe = driver.find_element(By.XPATH, "//iframe[contains(@id, 'aswift_3')]")
# driver.switch_to.frame(iframe)
time.sleep(2)
dismiss = driver.find_element(By.ID, "dismiss-button")
dismiss.click()

# edge setup
# time.sleep(8)
# mul_window = driver.window_handles
# driver.switch_to.window(mul_window[1])
# time.sleep(2)
# driver.switch_to.frame("wacframe")
# driver.find_element(By.XPATH, "//button[@data-unique-id='ViewerToolbar-DownloadADocumentCopy']").click()
# time.sleep(10)

time.sleep(2)