import time

from behave import *
from login_actions import LoginActions
from homepage_actions import HomePageActions

@given(u'I navigated to Login page')
def step_impl(context):
    home_act = HomePageActions(context.driver)
    home_act.navigate_to_login_page()
    expected_title = "Account Login"
    time.sleep(5)
    print(f"Actual Title: {context.driver.title}")
    assert context.driver.title == expected_title

@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.enter_credentials(username="CarlMax@email.com", password="12345")

@then(u'I should get logged in')
def step_impl(context):
    expected_text = "My Account"
    login_act = LoginActions(context.driver)
    login_act.verify_my_account(text=expected_text)


@when(u'I enter invalid email and valid password into the field')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.enter_credentials(username="CarlMax@email_invalid.com", password="12345")


@when(u'I click on Login button')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.click_login_btn()


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_text = "Warning: No match for E-Mail Address and/or Password."
    login_act = LoginActions(context.driver)
    login_act.verify_my_account(text=expected_text)



@when(u'I enter valid email and invalid password into the field')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.enter_credentials(username="CarlMax@email.com", password="12345_invalid")

@when(u'I enter invalid email and invalid password into the field')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.enter_credentials(username="CarlMax@email_invalid.com", password="12345_invalid")

@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.enter_credentials(username="", password="")
