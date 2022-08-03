from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[id=login_form]")
    REGISTER_FORM = (By.CSS_SELECTOR, "[id=register_form]")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    # MESSAGE_WITH_BOOK_NAME = (By.CSS_SELECTOR, "[id=messages] .alert-success:first-of-type .alertinner")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "[id=messages] .alert-success:first-of-type strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    
