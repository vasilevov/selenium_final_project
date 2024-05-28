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
        product_name = self.get_product_name()
        product_cost = self.get_product_cost()
        product_name_message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_PRODUCT_MESSAGE).text
        product_cost_message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_COST_MESSAGE).text
        assert product_name_message == product_name, f"Название товара не соответствует, должно быть {product_name}, получилось {product_name_message}"
        assert product_cost_message == product_cost, f"Стоимость товара не соответствует, должно быть {product_cost}, получилось {product_cost_message}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but did not"


