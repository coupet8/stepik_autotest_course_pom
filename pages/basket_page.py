from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
         assert self.is_not_element_present(*BasketPageLocators.POSITION_IN_BASKET), \
           "Basket isn't empty, but should be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), \
           "No message about empty basket, but it should be"

