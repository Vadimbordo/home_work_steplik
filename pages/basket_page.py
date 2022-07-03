from pages.base_page import BasePage
from pages.locators import BasketPageLocators, ProductPageLocators


class BasketPage(BasePage):

    # Ожидаем, что в корзине нет товаров
    def no_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_BASKET_EMPTY), \
            "В корзине есть товары"

    # Ожидаем, что есть текст о том что корзина пуста
    def have_text_about_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_BASKET_EMPTY), \
            "Отсутствует сообщение, что корзина пуста"
