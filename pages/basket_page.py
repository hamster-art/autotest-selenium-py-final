from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket should be empty"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty basket message should be present"
