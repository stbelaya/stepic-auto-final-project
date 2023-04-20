from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def press_button_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def should_be_product_added_to_basket(self):
        self.should_be_message_that_product_added_to_basket()
        self.should_be_product_name_in_message()
        self.should_be_message_with_basket_total()

    def should_be_message_that_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Message that product is added to basket is not presented"

    def should_be_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE_PRODUCT_NAME).text
        assert name_in_message == product_name, \
            f"Name in message '{name_in_message}' is not equal to product name '{product_name}'"

    def should_be_message_with_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Message with basket total is not presented"

    def should_be_total_in_message_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE_PRICE).text
        assert basket_total == product_price, \
            f"Total in message '{basket_total}' is not equal to product price '{product_price}'"
