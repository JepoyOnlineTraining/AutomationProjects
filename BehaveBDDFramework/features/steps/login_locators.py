from selenium.webdriver.common.by import By

class LoginLoc:
    email_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.CSS_SELECTOR, "input.btn-primary")

    firstname_field = (By.ID, "input-firstname")
    lastname_field = (By.ID, "input-lastname")
    reg_email_field = (By.ID, "input-email")
    phone_field = (By.ID, "input-telephone")
    reg_pass_field = (By.ID, "input-password")
    reg_confirm_pass_field = (By.ID, "input-confirm")

    agree_to_terms_checkbox = (By.CSS_SELECTOR, "input[name='agree']")
    continue_button = (By.CSS_SELECTOR, "input[value='Continue']")

    firstname_error_message = (By.CSS_SELECTOR, "input#input-firstname + div")
    lastname_error_message = (By.CSS_SELECTOR, "input#input-lastname + div")
    reg_email_error_message = (By.CSS_SELECTOR, "input#input-email + div")
    phone_error_message = (By.CSS_SELECTOR, "input#input-telephone + div")
    reg_password_error_message = (By.CSS_SELECTOR, "input#input-password + div")
