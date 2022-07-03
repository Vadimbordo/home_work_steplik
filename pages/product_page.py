from pytest_check import check_func
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    # добавить товар в корзину
    def add_product_to_card(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON)
        login_link.click()

    @check_func
    def check_success_message_add_to_cart(self):
        name_product = (self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)).text
        name_product_in_success_msg = (self.browser.find_element(*ProductPageLocators.
                                                                 SUCCESS_MESSAGE_ADD_PRODUCT_TO_CART)).text
        assert name_product == name_product_in_success_msg, \
            f'Наименование товара: "{name_product}" несоответствует ' \
            f'наименование товара в сообщении о добавлении в корзину: "{name_product_in_success_msg}"'

    @check_func
    def check_success_message_cost_price(self):
        product_cost = (self.browser.find_element(*ProductPageLocators.PRODUCT_COST)).text
        cost_in_message = (self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_COST_PRDDUCT)).text
        assert cost_in_message == product_cost, \
            f'Стоимость товара: "{cost_in_message}" несоответствует ' \
            f'стоимости товара в сообщении о добавлении в корзину: "{product_cost}" '

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе отображается, но не должно"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе должно исчезнуть, но отображаться"
