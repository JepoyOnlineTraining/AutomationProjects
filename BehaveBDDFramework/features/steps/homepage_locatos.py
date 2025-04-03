from selenium.webdriver.common.by import By

class HomePageLoc:

    my_account_link = (By.CSS_SELECTOR, "a[title='My Account']")
    login_link = (By.CSS_SELECTOR, "a[href*='login']")
    register_link = (By.CSS_SELECTOR, "a[href*='register']")
    home_page_content = (By.ID, "content")
    error_message = (By.CSS_SELECTOR, "div.alert")