from pages.main_page import MainPage
from pages.base_page import PromoLinks
from pages.product_page import ProductPage
import time
import pytest


# this is the test with 10 test cases wich cheking link with a bug
@pytest.mark.parametrize('link', PromoLinks.promo_list)
def test_guest_can_add_product_to_basket_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_button_be_clicked()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

#this is the main test
def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)
    page.open()
    page.should_button_be_clicked()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


