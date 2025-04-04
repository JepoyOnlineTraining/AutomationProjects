from behave import *
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homepage_actions import HomePageActions
from login_actions import LoginActions


@given(u'I navigate to Register Page')
def step_impl(context):
    home_page_act = HomePageActions(context.driver)
    login_act = LoginActions(context.driver)
    home_page_act.navigate_to_registration()
    expected_text = "Register Account"
    login_act.verify_registration_page(text=expected_text)


@when(u'I enter mandatory fields')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    email = "carl_" + datetime.datetime.now().strftime("%M%S") + "@email.com"
    phone = "12345678910"
    password = "test@pass1"
    login_act = LoginActions(context.driver)
    login_act.enter_registration_details(firstname=username, lastname=lastname, email=email, telephone=phone, password=password)

@when(u'I click on Continue button')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.continue_registration()


@then(u'Account should get created')
def step_impl(context):
    login_act = LoginActions(context.driver)
    expected_text = "Your Account Has Been Created!"
    login_act.verify_account_creation(text=expected_text)


@when(u'I enter all fields')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    email = "carl_" + datetime.datetime.now().strftime("%M%S") + "@email.com"
    phone = "12345678910"
    password = "test@pass1"
    login_act = LoginActions(context.driver)
    login_act.enter_registration_details(firstname=username, lastname=lastname, email=email, telephone=phone,
                                         password=password)


@when(u'I enter details into all fields except email filed')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    email = ""
    phone = "12345678910"
    password = "test@pass1"
    login_act = LoginActions(context.driver)
    login_act.enter_registration_details(firstname=username, lastname=lastname, email=email, telephone=phone,
                                         password=password)


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    email = "CarlMax@email.com"
    phone = "12345678910"
    password = "test@pass1"
    login_act = LoginActions(context.driver)
    login_act.enter_registration_details(firstname=username, lastname=lastname, email=email, telephone=phone,
                                         password=password)


@then(u'Proper warning message informing about duplicate account should be display')
def step_impl(context):
    login_act = LoginActions(context.driver)
    expected_text = "Warning: E-Mail Address is already registered!"
    login_act.verify_duplicate_account_message(text=expected_text)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    login_act = LoginActions(context.driver)
    login_act.enter_registration_details(firstname="", lastname="", email="", telephone="",
                                         password="")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    login_act = LoginActions(context.driver)
    first_name_error_message = "First Name must be between 1 and 32 characters!"
    last_name_error_message = "Last Name must be between 1 and 32 characters!"
    email_error_message = "E-Mail Address does not appear to be valid!"
    phone_error_message = "Telephone must be between 3 and 32 characters!"
    password_error_message = "Password must be between 4 and 20 characters!"

    login_act.verify_empty_error_message(firstname_err=first_name_error_message,
                                         lastname_err=last_name_error_message,
                                         email_err=email_error_message,
                                         phone_err=phone_error_message,
                                         pass_err=password_error_message)
