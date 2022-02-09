import pytest
import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import UrlLocators


@pytest.mark.register
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = UrlLocators.LOGIN_URL
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = UrlLocators.PRODUCT_URL
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_btn()
        page.add_product(link)
        page.should_be_same_product_name()
        page.should_be_same_product_cost()

    def test_user_cant_see_success_message(self, browser):
        link = UrlLocators.PRODUCT_URL
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize("link", UrlLocators.PROMO_URLS)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_btn()
    page.add_product(link)
    page.should_be_same_product_name()
    page.should_be_same_product_cost()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = UrlLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_btn()
    page.add_product(link)
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = UrlLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = UrlLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_btn()
    page.add_product(link)
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = UrlLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = UrlLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = UrlLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods()
    basket_page.should_be_empty_message()
