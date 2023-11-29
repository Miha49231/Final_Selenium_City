from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    # locators
    smartfony_icon = "//a[@href='/catalog/smartfony/']"

    # getters
    def get_smartfony_icon(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.smartfony_icon)))

    # actions
    def click_smartfony_icon(self):
        self.get_smartfony_icon().click()
        print('Click Smartfony Icon')

    # methods
    def click_smartfony(self):
        """Переход в раздел Смартфоны"""
        self.get_current_url()
        self.click_smartfony_icon()

        self.assert_url('https://www.citilink.ru/catalog/smartfony/')
