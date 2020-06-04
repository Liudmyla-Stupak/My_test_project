from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [0, 1, 2, 3, 4,5, 6, pytest.param(7, marks=pytest.mark.xfail), 8,9])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)    
    page.open()
    page.guest_can_add_product_to_basket()
    

#@pytest.mark.xfail
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
 #   link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  #  page = ProductPage(browser, link)    
   # page.open()
    #page.guest_can_add_product_to_basket()
    #page.should_not_be_success_message()
    
#def test_guest_cant_see_success_message(browser):
 #   link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  #  page = ProductPage(browser, link)    
   # page.open()
    #page.should_not_be_success_message()

#@pytest.mark.xfail
#def test_message_disappeared_after_adding_product_to_basket(browser):
 #   link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  #  page = ProductPage(browser, link)    
   # page.open()
    #page.guest_can_add_product_to_basket()
    #page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.going_to_the_basket()
    page.should_not_be_product_in_basket()
    page.should_be_message_basket_is_empty()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)  
        #self.browser = browser  
        page.open()
        page.go_to_login_page()
        our_email = str(time.time()) + "@fakemail.org"
        our_password = str(time.time())
        page.register_new_user(email=our_email, password=our_password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)    
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review        
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)    
        page.open()
        page.guest_can_add_product_to_basket()
        
    
    

