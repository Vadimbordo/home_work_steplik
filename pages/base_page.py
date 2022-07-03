import math
from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException
# Remote используется для типизации объекта драйвера, это даёт возможность видеть методы
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from pages.basket_page import BasketPage
# from pages.basket_page import BasketPage
from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET)
        link.click()

    # проверка отображения элемента
    def is_element_present(self, how_search, what_search):
        try:
            self.browser.find_element(how_search, what_search)
        except NoSuchElementException:
            return False
        return True

    ## Проверка появления и исчезновения элемента
    # Упадет, как только увидит искомый элемент в течении 4х секунд. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how_search, what_search, timeout=4):
        try:
            WebDriverWait(self.browser, timeout). \
                until(expected_conditions.presence_of_element_located((how_search, what_search)))
        except TimeoutException:
            return True
        return False

    # будет ждать 4 секунды, пока элемент не исчезнет.
    def is_disappeared(self, how_search, what_search, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located((how_search, what_search)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
