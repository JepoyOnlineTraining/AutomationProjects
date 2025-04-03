from behave import *
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@given(u'I navigate to Register Page')
def step_impl(context):
    options = Options()
    options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.get("https://tutorialsninja.com/demo/")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='My Account']"))).click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='register']"))).click()
    expected_text = "Register Account"
    content_text = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#content"))).text
    assert expected_text in content_text


@when(u'I enter mandatory fields')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    email = "carl_" + datetime.datetime.now().strftime("%M%S") + "@email.com"
    phone = "12345678910"
    password = "test@pass1"
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-firstname"))).send_keys(username)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-lastname"))).send_keys(lastname)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys(email)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-telephone"))).send_keys(phone)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys(password)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-confirm"))).send_keys(password)

@when(u'I click on Continue button')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='agree']"))).click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Continue']"))).click()


@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    actual_text = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "content"))).text
    print(actual_text)
    assert expected_text in actual_text
    context.driver.quit()

@when(u'I enter all fields')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    email = "carl_" + datetime.datetime.now().strftime("%M%S") + "@email.com"
    phone = "12345678910"
    password = "test@pass1"
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-firstname"))).send_keys(username)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-lastname"))).send_keys(lastname)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys(email)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-telephone"))).send_keys(phone)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys(password)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-confirm"))).send_keys(password)


@when(u'I enter details into all fields except email filed')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    # email = "carl_" + datetime.datetime.now().strftime("%M%S") + "@email.com"
    phone = "12345678910"
    password = "test@pass1"
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-firstname"))).send_keys(username)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-lastname"))).send_keys(lastname)
    # WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys(email)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-telephone"))).send_keys(phone)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys(password)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-confirm"))).send_keys(password)


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    username = "Carl"
    lastname = "Max"
    email = "CarlMax@email.com"
    phone = "12345678910"
    password = "test@pass1"
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-firstname"))).send_keys(username)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-lastname"))).send_keys(lastname)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys(email)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-telephone"))).send_keys(phone)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys(password)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-confirm"))).send_keys(password)


@then(u'Proper warning message informing about duplicate account should be display')
def step_impl(context):
    expected_text = "Warning: E-Mail Address is already registered!"
    actual_text = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert"))).text
    assert expected_text in actual_text
    context.driver.quit()

@when(u'I dont enter anything into the fields')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-firstname"))).send_keys("")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-lastname"))).send_keys("")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-telephone"))).send_keys("")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-password"))).send_keys("")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "input-confirm"))).send_keys("")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    first_name_error_message = "First Name must be between 1 and 32 characters!"
    last_name_error_message = "Last Name must be between 1 and 32 characters!"
    email_error_message = "E-Mail Address does not appear to be valid!"
    phone_error_message = "Telephone must be between 3 and 32 characters!"
    password_error_message = "Password must be between 4 and 20 characters!"

    assert get_text(context, (By.CSS_SELECTOR, "input#input-firstname + div")) == first_name_error_message
    assert get_text(context, (By.CSS_SELECTOR, "input#input-lastname + div")) == last_name_error_message
    assert get_text(context, (By.CSS_SELECTOR, "input#input-email + div")) == email_error_message
    assert get_text(context, (By.CSS_SELECTOR, "input#input-telephone + div")) == phone_error_message
    assert get_text(context, (By.CSS_SELECTOR, "input#input-password + div")) == password_error_message

    context.driver.quit()


def get_text(context, locator):
    return WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(locator)).text