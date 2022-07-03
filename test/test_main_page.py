from time import sleep

import pytest

from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"
new_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self,browser):
        page = MainPage(browser, link)       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                          # открываем страницу
        page.go_to_login_page()              # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)        # переход на страницу логина (также получаем методы этой страницы)
        login_page.should_be_login_page()                           # проверки для страницы логина


    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_login_page(browser):
    page = LoginPage(browser, login_page_link)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'
    # Гость открывает главную страницу,
    # переходим в корзину по кнопке в шапке сайта
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)

    sleep(3)
    # Ожидаем, что в корзине нет товаров
    basket_page.no_product_in_basket()

    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.have_text_about_basket_empty()
