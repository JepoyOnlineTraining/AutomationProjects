import time

from behave import given, when, then
from selenium import webdriver



@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("http://example.com/login")
    time.sleep(3)


@when('the user enters valid credentials')
def step_impl(context):
    context.driver.find_element_by_id('username').send_keys('user')
    context.driver.find_element_by_id('password').send_keys('pass')
    context.driver.find_element_by_id('login-button').click()

@then('the user should be logged in')
def step_impl(context):
    assert 'Welcome' in context.driver.page_source
    context.driver.quit()