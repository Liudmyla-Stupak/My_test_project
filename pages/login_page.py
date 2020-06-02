from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

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

    def register_new_user(email, password):
        input1 = (By.CSS_SELECTOR, '[name="registration-email"]')
        input1.send.keys(email)
        input2 = (By.CSS_SELECTOR, '[name="registration-password1"]')
        input2.send.keys(password)
        input3 = (By.CSS_SELECTOR, '[name="registration-password2"]')
        input3.send.keys(password)
        button = (By.CSS_SELECTOR, '[name="registration_submit"]')
        button.clic()
     