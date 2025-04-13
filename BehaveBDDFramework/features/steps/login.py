import time

from behave import *
from features.actions.login_actions import LoginActions
from features.actions.homepage_actions import HomePageActions
from features.actions.common_actions import CommonActions


@given(u'I navigated to Login page')
def step_impl(context):
    context.home_act = HomePageActions(context.driver)
    context.common_act = CommonActions(context.driver)
    context.login_act = LoginActions(context.driver)
    context.home_act.navigate_to_login_page()
    expected_title = "Account Login"
    time.sleep(5)
    print(f"Actual Title: {context.driver.title}")
    print(f"Expected Title: {expected_title}")
    assert context.driver.title == expected_title

@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_act.enter_credentials(username="CarlMax@email.com", password="12345")

@then(u'I should get logged in')
def step_impl(context):
    expected_text = "My Account1"
    context.login_act.verify_my_account(text=expected_text)


@when(u'I enter invalid email and valid password into the field')
def step_impl(context):
    context.login_act.enter_credentials(username="CarlMax@email_invalid.com", password="12345")


@when(u'I click on Login button')
def step_impl(context):
    context.login_act.click_login_btn()


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_text = "Warning: No match for E-Mail Address and/or Password."
    context.login_act.verify_my_account(text=expected_text)

@when(u'I enter valid email and invalid password into the field')
def step_impl(context):
    context.login_act.enter_credentials(username="CarlMax@email.com", password="12345_invalid")

@when(u'I enter invalid email and invalid password into the field')
def step_impl(context):
    context.login_act.enter_credentials(username="CarlMax@email_invalid.com", password="12345_invalid")

@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login_act.enter_credentials(username="", password="")
