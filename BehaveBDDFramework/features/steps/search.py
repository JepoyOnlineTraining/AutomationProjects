from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I got navigated to Home Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo")


@when(u'I enter valid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'I click on Search button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button.btn-default").click()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert "HP" in context.driver.find_element(By.CSS_SELECTOR, "div[class*='product-layout product-grid']").text
    context.driver.quit()

@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("YAKULT")


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    assert "There is no product that matches the search criteria." in context.driver.find_element(By.CSS_SELECTOR, "div#content p:last-child").text
    context.driver.quit()

@when(u'I dont enter anything into Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
