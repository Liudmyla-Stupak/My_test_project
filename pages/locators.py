﻿from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_form = (By.CSS_SELECTOR, "#login_form")
    Register_form = (By.CSS_SELECTOR, "#register_form")
