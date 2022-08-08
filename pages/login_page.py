import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form doesn't exist"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form doesn't exist"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_IN_REGISTER_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_1_IN_REGISTER_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_2_IN_REGISTER_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()