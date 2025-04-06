from selenium.webdriver.common.by import By

class SearchLocators:

    search_field = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, "button.btn-default")
    product_results = (By.CSS_SELECTOR, "div[class*='product-layout product-grid']")
    no_product_message = (By.CSS_SELECTOR, "div#content p:last-child")
