from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.smartfony_page import SmartfonyPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.delete_page import DeletePage


def test_buy_xiaomi():
    """Покупка смартфона Xiaomi Redmi Note 12S 8/256Gb черного цвета"""
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test Buy Xiaomi')

    enter = LoginPage(driver)
    enter.authorization()

    main = MainPage(driver)
    main.click_smartfony()

    smartfony = SmartfonyPage(driver)
    smartfony.select_phone()

    cart = CartPage(driver)
    cart.checkout()

    final = CheckoutPage(driver)
    final.final()

    delete = DeletePage(driver)
    delete.delete_product()

    print('Finish Test Buy Xiaomi')
