from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class DeletePage(Base):

    # locators
    delete_product_button = "//div[@data-meta-name='DeleteAction']"
    empty_cart_caption = "//*[@id='__next']/div/main/div[1]/div[2]/div/div[1]"

    # getters
    def get_delete_product_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_button)))

    def get_empty_cart_caption(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart_caption)))

    # actions
    def click_delete_product_button(self):
        self.get_delete_product_button().click()
        print('Click Delete Button')

    # methods
    def delete_product(self):
        """Удаление смартфона из корзины"""
        self.get_current_url()
        self.click_delete_product_button()
        self.assert_word(self.get_empty_cart_caption(), 'В корзине нет товаров')

