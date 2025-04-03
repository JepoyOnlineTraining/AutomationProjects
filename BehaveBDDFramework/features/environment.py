
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities import ConfigReader


def before_scenario(context, scenario):
    browser_name = ConfigReader.read_configuration("basic info", "browser")

    if browser_name == "chrome":
        option = Options()
        option.add_experimental_option("detach", True)
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

def after_scenario(context, scenario):
    context.driver.quit()
