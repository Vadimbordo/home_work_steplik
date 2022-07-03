from time import sleep

import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    pass
    # Открываем страницу товара
    # Добавляем товар в корзину
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_card()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Элемент найден, но его не должно быть"


def test_guest_cant_see_success_message(browser):
    pass
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()

    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Элемент найден, но его не должно быть"


def test_message_disappeared_after_adding_product_to_basket(browser):
    pass
    # Открываем страницу товара
    # Добавляем товар в корзину
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_card()

    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    assert product_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Элемент найден, но его не должно быть"
