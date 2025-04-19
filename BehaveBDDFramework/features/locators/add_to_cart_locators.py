from selenium.webdriver.common.by import By

class AddToCartLoc:

    iphone_add_to_cart_button = (By.XPATH,"//button[@onclick=\"cart.add('40');\"]")
    cart_total = (By.CSS_SELECTOR, "span#cart-total")
    cart_button = (By.CSS_SELECTOR, "button.btn-inverse")
    remove_button = (By.CSS_SELECTOR, "button[title='Remove']")
    iphone_image = (By.CSS_SELECTOR, "img[title='iPhone']")
    quantity_field = (By.CSS_SELECTOR, "input#input-quantity")
    product_add_to_cart_button = (By.CSS_SELECTOR, "button#button-cart")