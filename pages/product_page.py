from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_name_of_product(self):
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(book_name_in_basket)
        print(book_name)
        assert book_name == book_name_in_basket

    def should_be_book_price_equals_basket_price(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        print(price_in_basket)
        print(book_price)
        assert book_price == price_in_basket