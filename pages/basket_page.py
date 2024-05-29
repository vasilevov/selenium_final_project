from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_page_url()

    def should_be_basket_page_url(self):
        assert "basket" in self.browser.current_url, "Должен быть адрес страницы с корзиной"

    def should_be_products_list(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_LIST_TITLE), "Должен быть список товаров"

    def should_not_be_products_list_text(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST_TITLE), "Не должно быть списка товаров"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Должен быть текст что корзина пуста"

