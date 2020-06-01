from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "There are goods in the basket"


    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE ), \
            "Message 'Your basket is empty. Continue shopping' is not presented"


   

    