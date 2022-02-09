from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT).text

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.COST).text

    def should_be_add_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BTN), "Add btn is not presented, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_ALERT), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Success message should be disappeared"

    def add_product(self, link):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_btn.click()
        if self.is_promo_link(link):
            self.solve_quiz_and_get_code()

    def should_be_same_product_name(self):
        product_name = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        )
        assert product_name.text == self.get_product_name(), "Product is not added, but should be"

    def should_be_same_product_cost(self):
        cost = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_COST)
        )
        assert cost.text == self.get_product_cost(), "Product cost is not the same, but should be"
