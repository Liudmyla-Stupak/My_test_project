from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "there is no 'login' substring in the current browser url"
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Login_form), "NO LOGIN FORM"
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Register_form), "NO REGISTER FORM"
        