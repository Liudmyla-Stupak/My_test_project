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

    def register_new_user(self, email, password):
        #our_email = str(time.time()) + "@fakemail.org"
        #our_password = str(time.time())
        input1 = self.browser.find_element(By.CSS_SELECTOR, '[name="registration-email"]')
        button = self.browser.find_element(By.CSS_SELECTOR, '[name="registration_submit"]')
        input1.send_keys(email)
        input2 = self.browser.find_element(By.CSS_SELECTOR, '[name="registration-password1"]')
        input2.send_keys(password)
        input3 = self.browser.find_element(By.CSS_SELECTOR, '[name="registration-password2"]')
        input3.send_keys(password)
        button = self.browser.find_element(By.CSS_SELECTOR, '[name="registration_submit"]')
        button.click()
     