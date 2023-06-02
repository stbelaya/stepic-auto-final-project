import pytest
from faker import Faker

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


link = ProductPage.PRODUCT_PAGE1


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        """
        Предусловия: Роль - гость.
        1. Открыть страницу товара
        2. Добавить товар в корзину
        Ожидаемый результат:
        1) Сообщение о том, что товар добавлен в корзину. Название товара в сообщении совпадает с добавленным товаром.
        2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_product_added_to_basket()

    @pytest.mark.xfail(reason="known_issue, user sees success message, probably as designed")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        Предусловия: Роль - гость.
        1. Открыть страницу товара
        2. Добавить товар в корзину
        Ожидаемый результат:
        Нет сообщения об успехе
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Предусловия: Роль - гость.
        1. Открыть страницу регистрации;
        2. Зарегистрировать нового пользователя;
        Ожидаемый результат:
        Пользователь залогинен
        """
        page = LoginPage(browser, LoginPage.LOGIN_URL)
        page.open()
        fake = Faker()
        email = fake.email()
        password = fake.password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Предусловия: Роль - пользователь, зарегистрированный в методе setup.
        1. Открыть страницу товара
        2. Добавить товар в корзину
        Ожидаемый результат:
        1) Сообщение о том, что товар добавлен в корзину. Название товара в сообщении совпадает с добавленным товаром.
        2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_product_added_to_basket()

    @pytest.mark.xfail(reason="known_issue, user sees success message, probably as designed")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        Предусловия: Роль - пользователь, зарегистрированный в методе setup.
        1. Открыть страницу товара
        2. Добавить товар в корзину
        Ожидаемый результат:
        Нет сообщения об успехе
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    Предусловия: Роль - гость
    1. Открыть страницу товара
    Ожидаемый результат:
    Нет сообщения об успехе
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="known_issue, message doesn't disappeared, probably as designed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1. Открыть страницу товара
    2. Добавить товар в корзину
    Ожидаемый результат:
    Нет сообщения об успехе (оно исчезает)
    """
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_be_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Предусловия: Роль - гость
    1. Открыть страницу товара
    Ожидаемый результат:
    На странице есть ссылка логина
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Предусловия: Роль - гость
    1. Открыть страницу товара
    2. Перейти на страницу логина по ссылке в шапке сайта
    Ожидаемый результат:
    1) В адресной строке содержится слово 'login'
    2) На странице есть форма логина
    3) На странице есть форма регистрации
    """
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Предусловия: Роль - гость
    1. Открыть страницу товара
    2. Перейти в корзину по кнопке в шапке сайта
    Ожидаемый результат:
    1) В корзине нет товаров
    2) Есть текст о том что корзина пуста
    """
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_that_basket_is_empty()
