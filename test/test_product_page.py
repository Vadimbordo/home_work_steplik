from time import sleep

import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage

promo = ["?promo=offer0",
         "?promo=offer1",
         "?promo=offer2",
         "?promo=offer3",
         "?promo=offer4",
         "?promo=offer5",
         "?promo=offer6",
         pytest.param("?promo=offer7", marks=pytest.mark.xfail),
         "?promo=offer8",
         "?promo=offer9"]


@pytest.mark.parametrize("promo", promo)
def test_guest_can_add_product_to_basket(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" + promo
    """
    1 Открываем страницу товара
    2 Нажимаем на кнопку "Добавить в корзину".
    3 Посчитать результат математического выражения и ввести ответ.

    """
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_card()
    product_page.solve_quiz_and_get_code()

    """
    Ожидаемый результат:
    4 Сообщение о том, что товар добавлен в корзину.
    Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    5 Сообщение со стоимостью корзины.
    Стоимость корзины совпадает с ценой товара.

    """
    product_page.check_success_message_add_to_cart()
    product_page.check_success_message_cost_price()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'
    # Гость открывает главную страницу,
    # переходим в корзину по кнопке в шапке сайта
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)

    sleep(3)
    # Ожидаем, что в корзине нет товаров
    basket_page.no_product_in_basket()

    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.have_text_about_basket_empty()
