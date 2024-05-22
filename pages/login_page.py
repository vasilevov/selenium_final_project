from .base_page import BasePage
from .locators import LoginPageLocators
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Должна быть страница логина"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_EMAIL_FIELD), "Должно быть поле ввода email"
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_PASSWORD_FIELD), "Должно быть поле ввода пароля"
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_BUTTON), "Должна быть кнопка 'Войти'"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD), "Должно быть поле ввода email"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD), "Должно быть поле ввода пароля"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_FIELD), "Должно быть поле повтора пароля"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_BUTTON), "Должна быть кнопка 'Зарегистрироваться'"