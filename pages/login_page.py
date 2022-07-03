from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_from = self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert login_from

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"
        assert register_form

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.FILED_EMAIL_FOR_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FILED_FIRST_PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FILED_SECOND_PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON_FOR_REGISTRATION).click()
        assert self.is_element_present(*LoginPageLocators.ACCOUNT_ICON), "Пользователь не создан"

    def check_user_sing_in(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT), "Пользователь не авторизован"
