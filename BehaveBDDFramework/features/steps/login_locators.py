from selenium.webdriver.common.by import By

class LoginLoc:
    email_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.CSS_SELECTOR, "input.btn-primary")
