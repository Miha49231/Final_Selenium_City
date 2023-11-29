from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class SmartfonyPage(Base):

    # locators
    min_price = "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/input[1]"
    max_price = "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/input[2]"
    xiaomi_checkbox = "//input[@id='xiaomi']"
    cookie = "//button[@class='e4uhfkv0 css-1lxdbiq e4mggex0']"
    xiaomi_redmi_note12s = "//a[@href='/product/smartfon-xiaomi-redmi-note-12s-256gb-8gb-chernyi-3g-4g-2sim-6-43-amole-1924736/']"
    add_to_curt = "//*[@id='__next']/div/main/div[1]/div[2]/div/div[4]/div/div[3]/div/div[4]/div/div[1]/div/div/button"
    close_add_window = "//button[@class='e1nu7pom0 css-ony2li e4mggex0']"
    go_to_cart_button = "//*[@id='__next']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/a[2]"

    # getters
    def get_min_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_xiaomi_checkbox(self):
        return self.driver.find_element(By.XPATH, self.xiaomi_checkbox)

    def get_cookie_agree(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cookie)))

    def get_xiaomi_redmi_note12s(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xiaomi_redmi_note12s)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_curt)))

    def get_close_add_window(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.close_add_window )))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    # actions
    def set_min_price(self):
        self.get_min_price().click()
        self.get_min_price().clear()
        self.get_min_price().send_keys('19000')
        self.get_min_price().send_keys(Keys.ENTER)
        print('Set Minimum Price')

    def set_max_price(self):
        self.get_max_price().click()
        self.get_max_price().send_keys(Keys.BACKSPACE * 7)
        self.get_max_price().send_keys(2200)
        self.get_max_price().send_keys(Keys.ENTER)
        print('Set Maximum Price')

    def click_xiaomi_checkbox(self):
        self.get_xiaomi_checkbox().click()
        print('Click Xiaomi Checkbox')

    def scroll_to(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        print('Scroll')

    def scroll_down(self, pxs):
        self.driver.execute_script(f"window.scroll(0,{pxs})")
        print('Scroll')

    def click_cookie_agree(self):
        self.get_cookie_agree().click()
        print('Click Cookie Button')

    def click_xiaomi_redmi_note12s(self):
        self.get_xiaomi_redmi_note12s().click()
        print('Select Xiaomi Redmi Note 12s')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Add Phone To Cart')

    def click_close_add_window(self):
        self.get_close_add_window ().click()
        print('Close Add Phone Window')

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print('Go To Cart')

    # methods
    def select_phone(self):
        """Выбор смартфона и переход в корзину"""
        self.get_current_url()
        self.set_min_price()
        self.set_max_price()
        self.scroll_to(self.get_xiaomi_checkbox())
        self.click_cookie_agree()
        self.click_xiaomi_checkbox()
        self.scroll_to(self.get_xiaomi_redmi_note12s())
        self.click_xiaomi_redmi_note12s()
        self.click_cart_button()
        self.click_close_add_window()
        self.click_go_to_cart_button()



