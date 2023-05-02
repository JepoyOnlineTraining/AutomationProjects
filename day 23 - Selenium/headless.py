from selenium import webdriver
from selenium.webdriver.common.by import By
from Common import Common


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv = Service(Common.chrome_path)
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv, options=ops)
    return driver


def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv = Service(Common.edge_path)
    ops = webdriver.EdgeOptions()
    ops.headless = True
    driver = webdriver.Edge(service=serv, options=ops)
    return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    serv = Service(Common.firefox_path)
    ops = webdriver.FirefoxOptions()
    ops.headless = True
    driver = webdriver.Firefox(service=serv, options=ops)
    return driver


# driver = headless_chrome()
# driver = headless_edge()
driver = headless_firefox()
driver.get(Common.demo_nopcommerce)
print(driver.title)
print(driver.current_url)
driver.close()
