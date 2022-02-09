import pytest
from selenium.webdriver.common.by import By


class UrlLocators:
    PROMO_URLS = [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                     marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ]
    MAIN_URL = "http://selenium1py.pythonanywhere.com"
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[href*='/basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p:first-child")


class ProductPageLocators:
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    COST = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:first-child")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    MESSAGE_COST = (By.CSS_SELECTOR, ".alert-info strong")
