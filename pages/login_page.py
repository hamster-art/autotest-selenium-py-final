from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not Login Page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Reg form is not presented"

    def register_new_user(self, email, password):
        reg_email = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPageLocators.REG_EMAIL))
        reg_password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPageLocators.REG_PASSWORD))
        reg_confirm_password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPageLocators.REG_CONFIRM_PASSWORD))
        reg_submit = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPageLocators.REG_SUBMIT))
        reg_email.send_keys(email)
        reg_password.send_keys(password)
        reg_confirm_password.send_keys(password)
        reg_submit.click()
