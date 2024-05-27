from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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
    ADD_TO_BASKET_MESSAGES = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_COST = (By.CSS_SELECTOR, '.product_main .price_color')
