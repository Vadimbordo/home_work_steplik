from time import sleep

import pytest

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
    sleep(6000)
    product_page.check_success_message_add_to_cart()
    product_page.check_success_message_cost_price()
