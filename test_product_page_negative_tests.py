import time

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page('coders-at-work_207')
    page.click_add_to_cart_button()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) is True


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page('coders-at-work_207')
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) is True


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page('coders-at-work_207')
    page.click_add_to_cart_button()
    time.sleep(5)
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) is True
