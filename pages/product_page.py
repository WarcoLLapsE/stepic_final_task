from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self, value):
        self.should_be_product_url(value)
        self.should_be_add_to_cart_button()

    def should_be_equal_product_price_and_name(self):
        self.should_be_equal_price()
        self.should_be_equal_product_name()

    def should_be_product_url(self, value):
        # реализуйте проверку на корректный url адрес
        assert self.is_url_present(value), "Url link is not presented"

    def should_be_add_to_cart_button(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"

    def click_add_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_button.click()

    def should_be_equal_price(self):
        product_page_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_page_price = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        assert product_page_price in basket_page_price, "Prices aren't equal"

    def should_be_equal_product_name(self):
        product_page_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_alert_name = self.browser.find_element(*ProductPageLocators.PRODUCT_INNER_ALERT_NAME).text
        assert product_page_name == product_alert_name, "Product names aren't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
