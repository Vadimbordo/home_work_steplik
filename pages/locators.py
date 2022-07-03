from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_PRODUCT_TO_CART_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_page .product_main h1')
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_page .product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success .alertinner ')
    SUCCESS_MESSAGE_ADD_PRODUCT_TO_CART = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    SUCCESS_MESSAGE_COST_PRDDUCT = (By.CSS_SELECTOR, '.alertinner p strong')

