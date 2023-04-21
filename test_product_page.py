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
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        Ожидаемый результат:
        1) Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        который вы действительно добавили.
        2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_product_added_to_basket()

    @pytest.mark.xfail(reason="known_issue, user sees success message, probably as designed")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        Ожидаемый результат:
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        1. Открываем страницу регистрации;
        2. Регистрируем нового пользователя;
        Ожидаемый результат:
        Проверяем, что пользователь залогинен
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
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        Ожидаемый результат:
        1) Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        который вы действительно добавили.
        2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_product_added_to_basket()

    @pytest.mark.xfail(reason="known_issue, user sees success message, probably as designed")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        Ожидаемый результат:
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    1. Открываем страницу товара
    Ожидаемый результат:
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="known_issue, message doesn't disappeared, probably as designed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара
    2. Добавляем товар в корзину
    Ожидаемый результат:
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_be_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    1. Гость открывает страницу товара
    Ожидаемый результат:
    Ожидаем, что на странице есть ссылка логина
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    1. Гость открывает страницу товара
    2. Переходит на страницу логина по ссылке в шапке сайта
    Ожидаемый результат:
    1) Ожидаем, что в адресной строке содержится слово 'login'
    2) Ожидаем, что на странице есть форма логина
    3) Ожидаем, что на странице есть форма регистрации
    """
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    1. Гость открывает страницу товара
    2. Переходит в корзину по кнопке в шапке сайта
    Ожидаемый результат:
    1) Ожидаем, что в корзине нет товаров
    2) Ожидаем, что есть текст о том что корзина пуста
    """
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_that_basket_is_empty()
