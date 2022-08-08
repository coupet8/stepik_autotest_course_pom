from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[id=login_form]")
    REGISTER_FORM = (By.CSS_SELECTOR, "[id=register_form]")
    EMAIL_IN_REGISTER_FORM = (By.CSS_SELECTOR, "[name=registration-email]")
    PASSWORD_1_IN_REGISTER_FORM = (By.CSS_SELECTOR, "[name=registration-password1]")
    PASSWORD_2_IN_REGISTER_FORM = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id=messages] .alert-success:first-of-type .alertinner")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "[id=messages] .alert-success:first-of-type strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_WATCH_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "[id=content_inner] > p")
    POSITION_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
