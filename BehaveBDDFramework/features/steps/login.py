import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given(u'I navigated to Login page')
def step_impl(context):
    context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    context.driver.maximize_window()

@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("CarlMax@email.com")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys("12345")

@then(u'I should get logged in')
def step_impl(context):
    expected_text = "My Account"
    actual_text = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "content"))).text
    print(actual_text)
    assert expected_text in actual_text



@when(u'I enter invalid email and valid password into the field')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("CarlMax@email_invalid.com")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys("12345")


@when(u'I click on Login button')
def step_impl(context):
   context.driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
   time.sleep(5)


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_message = "Warning: No match for E-Mail Address and/or Password."
    actual_message = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.alert'))).text
    print(f"Actual: {actual_message}")
    assert expected_message.__eq__(actual_message)



@when(u'I enter valid email and invalid password into the field')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("CarlMax@email.com")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys("12345_invalid")


@when(u'I enter invalid email and invalid password into the field')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("CarlMax@email_invalid.com")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys("12345_invalid")


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys("")
