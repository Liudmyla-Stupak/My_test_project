from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_form = (By.CSS_SELECTOR, "#login_form")
    Register_form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")


