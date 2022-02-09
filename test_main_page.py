import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import UrlLocators


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = UrlLocators.MAIN_URL
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = UrlLocators.MAIN_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


# def test_is_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    login_page = LoginPage(browser, link)
#    login_page.open()
#    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = UrlLocators.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods()
    basket_page.should_be_empty_message()
