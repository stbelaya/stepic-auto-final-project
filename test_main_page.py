import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = MainPage.MAIN_PAGE_URL


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """
        1. Гость открывает главную страницу
        2. Переходит на страницу логина по ссылке в шапке сайта
        Ожидаемый результат:
        1) Ожидаем, что в адресной строке содержится слово 'login'
        2) Ожидаем, что на странице есть форма логина
        3) Ожидаем, что на странице есть форма регистрации
        """
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """
        1. Гость открывает главную страницу
        Ожидаемый результат:
        Ожидаем, что на странице есть ссылка логина
        """
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    1. Гость открывает главную страницу
    2. Переходит в корзину по кнопке в шапке сайта
    Ожидаемый результат:
    1) Ожидаем, что в корзине нет товаров
    2) Ожидаем, что есть текст о том что корзина пуста
    """
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_that_basket_is_empty()
