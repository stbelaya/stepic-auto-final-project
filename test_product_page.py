import pytest
from faker import Faker

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import LoginPageLocators


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.parametrize('num', [*range(7), pytest.param(7, marks=pytest.mark.xfail), range(8, 10)])
    def test_guest_can_add_product_to_basket(browser, num):
        """
        Тест добавления товара в корзину.
        Ожидаемый результат:
        1)Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        который вы действительно добавили.
        2)Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        # page.solve_quiz_and_get_code()
        page.should_be_product_added_to_basket()


    @pytest.mark.xfail(reason="known_issue, user see success message")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        """
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        В этой функции нужно:
        1. открыть страницу регистрации;
        2. зарегистрировать нового пользователя;
        3. проверить, что пользователь залогинен
        """
        page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
        page.open()
        fake = Faker()
        email = fake.email()
        password = fake.password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        """
        Тест добавления товара в корзину.
        Ожидаемый результат:
        1)Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        который вы действительно добавили.
        2)Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        # page.solve_quiz_and_get_code()
        page.should_be_product_added_to_basket()

    @pytest.mark.xfail(reason="known_issue, user see success message")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    1. Открываем страницу товара
    2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="known_issue")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара
    2. Добавляем товар в корзину
    3. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_be_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    1. Гость открывает страницу товара
    2. Переходит в корзину по кнопке в шапке сайта
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста
    """
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_that_basket_is_empty()