from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn.btn-default[href]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    ADDED_TO_BASKET_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    BASKET_TOTAL_MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")



