from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    # locators
    cart_product_name = "//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']"
    checkout_button = "//button[@class='e4uhfkv0 css-ch34l1 e4mggex0']"

    # getters
    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_name)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button )))

    # actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click Checkout Button')

    # methods
    def checkout(self):
        """Подтверждение покупки и переход к оформлению товара"""
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/order/')
        self.assert_word(self.get_cart_product_name(), 'Смартфон Xiaomi Redmi Note 12S 8/256Gb, черный')
        self.click_checkout_button()

