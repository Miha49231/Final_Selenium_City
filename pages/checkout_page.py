from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CheckoutPage(Base):

    # locators
    checkout_product_name = "//*[@id='__next']/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/span[1]"

    # getters
    def get_checkout_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_product_name)))

    # actions

    # methods
    def final(self):
        """Завершение покупки, проверка модели смартфона и возврат в корзину"""
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/order/checkout/')
        self.assert_word(self.get_checkout_product_name(), 'Смартфон Xiaomi Redmi Note 12S 8/256Gb, черный')
        self.driver.back()

