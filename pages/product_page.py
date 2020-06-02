from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def guest_can_add_product_to_basket(self):
        name_book = self.browser.find_element(By.CSS_SELECTOR, "#content_inner h1")
        book = name_book.text
        price_book = self.browser.find_element(By.CSS_SELECTOR, "#content_inner p")
        price = price_book.text
        button = self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
        button.click()
        #self.solve_quiz_and_get_code()
        #time.sleep(1500)
        message1 = self.browser.find_element(By.CSS_SELECTOR, ".alertinner strong")
        mes1 = message1.text
        message2 = self.browser.find_element(By.CSS_SELECTOR, ".alertinner p strong")
        mes2 = message2.text
        assert book==mes1, "Product name does not match"
        assert price==mes2, "The cost of the basket does not match the price of the goods"
        #time.sleep(1500)
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
         "Success message is presented, but should not be"


