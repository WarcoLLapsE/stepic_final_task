from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_url_present('basket'), "Basket url link is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FOR_BASKET_ASSERT_IS_NOT_EMPTY), 'Basket is not empty!'
        assert self.is_element_present(*BasketPageLocators.TEXT_FOR_BASKET_IS_EMPTY), 'Empty basket text is not presented!'