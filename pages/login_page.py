from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    url = 'https://www.citilink.ru/'

    # locators
    enter_button = "//div[@class='css-1wyvf5z eyoh4ac0']"
    login_field = "//input[@name='login']"
    password_field = "//input[@name='pass']"
    login_button = "//button[@class='e4uhfkv0 css-ajbuym e4mggex0']"
    user_name = "//span[@class='en3k2720 e106ikdt0 css-1rzz8dw e1gjr6xo0']"

    # getters
    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_login_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,  self.login_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,  self.user_name)))

    # actions
    def click_enter_button(self):
        self.get_enter_button().click()
        print('Click Enter Button')

    def input_login(self):
        self.get_login_field().send_keys('test_test_test_00_test@list.ru')
        print('Login Input')

    def input_password(self):
        self.get_password_field().send_keys('eOY1MAd2ycu_')
        print('Password Input')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click Login Button')

    # methods
    def authorization(self):
        """Авторизация на сайте"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_login()
        self.input_password()
        self.click_login_button()
        self.assert_url('https://www.citilink.ru/?_action=login&_success_login=1')
        self.assert_word(self.get_user_name(), 'Иван')


