from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_cart_button()

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_url_present('handbook_209/?promo=newYear'), "Url link is not presented"

    def should_be_add_to_cart_button(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"

    def click_add_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_button.click()

