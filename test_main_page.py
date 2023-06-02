import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = MainPage.MAIN_PAGE_URL


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """
        Предусловия: Роль - гость
        1. Открыть главную страницу
        2. Перейти на страницу логина по ссылке в шапке сайта
        Ожидаемый результат:
        1) В адресной строке содержится слово 'login'
        2) На странице есть форма логина
        3) На странице есть форма регистрации
        """
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """
        Предусловия: Роль - гость
        1. Открыть главную страницу
        Ожидаемый результат:
        На странице есть ссылка логина
        """
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Предусловия: Роль - гость
    1. Открыть главную страницу
    2. Перейти в корзину по кнопке в шапке сайта
    Ожидаемый результат:
    1) В корзине нет товаров
    2) Есть текст о том что корзина пуста
    """
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_that_basket_is_empty()
