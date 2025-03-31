from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@given(u'user navigate to QA Practice')
def step_impl(context):
    option = Options()
    option.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    context.driver.get("https://qa-practice.netlify.app/")
    context.driver.maximize_window()

    # raise NotImplementedError(u'STEP: Given user navigate to QA Practice')


@when(u'user is in homepage')
def step_impl(context):
    assert context.driver.title == "QA Practice | Learn with RV"


@then(u'user will see a welcome message')
def step_impl(context):
    expected = "Welcome"
    actual = context.driver.find_element(By.CSS_SELECTOR, "h1.display-4").text
    print(expected, actual)
    assert  actual == "Welcome!"
    context.driver.quit()
