from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER)
        expected_basket_header = "Basket"
        actual_basket_header = self.browser.find_element(*BasketPageLocators.BASKET_HEADER).text
        assert actual_basket_header == expected_basket_header, \
            f"Actual text in basket header '{actual_basket_header}' " \
            f"is not equal to expected header '{expected_basket_header}'"

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        assert "basket" in current_url, f"basket is not in current url {current_url}"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "Message that the basket is empty is not presented"

    def should_be_text_that_basket_empty(self):
        expected_text = "Your basket is now empty"
        actual_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert actual_text == expected_text, \
            f"Actual text in empty basket message '{actual_text}' is not equal to expected text '{expected_text}'"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            f"There are some items in the basket, but they shouldn't be there"
