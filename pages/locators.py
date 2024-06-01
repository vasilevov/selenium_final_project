from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    OPEN_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn-default")


class BasketPageLocators():
    PRODUCT_LIST_TITLE = (By.CSS_SELECTOR, ".basket-title")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    SIGN_IN_EMAIL_FIELD = (By.CSS_SELECTOR, '[name = "login-username"]')
    SIGN_IN_PASSWORD_FIELD = (By.CSS_SELECTOR, '[name = "login-password"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[name = "login_submit"]')
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTER_PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_BASKET_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '.alertinner > strong')
    ADD_TO_BASKET_COST_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
