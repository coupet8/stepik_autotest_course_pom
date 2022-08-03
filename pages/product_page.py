from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_name_of_product(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_IN_BASKET) == self.is_element_present(*ProductPageLocators.BOOK_NAME)

    def should_be_book_price_equals_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET) == self.is_element_present(*ProductPageLocators.BOOK_PRICE)