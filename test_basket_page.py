import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import UrlLocators


@pytest.mark.parametrize("link", UrlLocators.PROMO_URLS)
def test_guest_can_add_product_to_basket(browser, link):
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


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = UrlLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
