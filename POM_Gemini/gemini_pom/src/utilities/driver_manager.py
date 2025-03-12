from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def create_webdriver(browser_name="chrome"):

    browser_name = browser_name.lower()

    try:
        if browser_name == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            driver =webdriver.Firefox(service=service)
        elif browser_name == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.maximize_window()
        return driver

    except Exception as e:
        print(f"Error creating driver {e}")
        return None

def close_browser(driver):
    if driver:
        driver.quit()