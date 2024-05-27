from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        basket_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def should_be_add_to_basket_message(self):
        name_is_legit = False
        cost_is_legit = False
        product_name = self.get_product_name()
        product_cost = self.get_product_cost()
        messages = self.browser.find_elements(*ProductPageLocators.ADD_TO_BASKET_MESSAGES)
        for message in messages:
            if product_name in message.text:
                name_is_legit = True
            if product_cost in message.text:
                cost_is_legit = True
        assert name_is_legit, f"Название товара не соответствует, должно быть {product_name}"
        assert cost_is_legit, f"Стоимость товара не соответствует, должно быть {product_cost}"




