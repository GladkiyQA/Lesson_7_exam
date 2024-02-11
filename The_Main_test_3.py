import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping():
    options = Options()
    # options.add_argument("--window-size=1000,1000") # Если хочется визуала
    options.add_argument("--headless")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.saucedemo.com/")

    # Пачка самых разных локаторов
    USERNAME_FIELD = ('xpath', '//input[@name="user-name"]')
    PASSWORD_FIELD = ('xpath', '//input[@name="password"]')
    LOGIN_BUTTON = ('xpath', '//input[@name="login-button"]')

    SAUCE_LABS_BACKPACK = ('xpath', '//button[@id="add-to-cart-sauce-labs-backpack"]')
    SAUCE_LABS_BOLD_T_SHIRT = ('xpath', '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    SAUCE_LABS_ONESIE = ('xpath', '//button[@id="add-to-cart-sauce-labs-onesie"]')

    SHOPPING_CART_CONTAINER = ('xpath', '//div[@id="shopping_cart_container"]')

    CHECKOUT = ('xpath', '//button[@id="checkout"]')

    FIRST_NAME = ('xpath', '//input[@id="first-name"]')
    LAST_NAME = ('xpath', '//input[@id="last-name"]')
    ZIP_CODE = ('xpath', '//input[@id="postal-code"]')
    CONTINUE_BUTTON = ('xpath', '//input[@id="continue"]')

    TOTAL_PRICE = ('xpath', '//div[@class="summary_info_label summary_total_label"]')

    # Запускаем
    username = driver.find_element(*USERNAME_FIELD)
    username.send_keys('standard_user')
    password = driver.find_element(*PASSWORD_FIELD)
    password.send_keys('secret_sauce')
    button = driver.find_element(*LOGIN_BUTTON)
    button.click()

    add_backpack = driver.find_element(*SAUCE_LABS_BACKPACK)
    add_backpack.click()
    add_shirt = driver.find_element(*SAUCE_LABS_BOLD_T_SHIRT)
    add_shirt.click()
    add_onesie = driver.find_element(*SAUCE_LABS_ONESIE)
    add_onesie.click()

    click_to_cart = driver.find_element(*SHOPPING_CART_CONTAINER)
    click_to_cart.click()

    click_to_checkout = driver.find_element(*CHECKOUT)
    click_to_checkout.click()

    firstname_field = driver.find_element(*FIRST_NAME)
    firstname_field.send_keys("Dan")
    lastname_field = driver.find_element(*LAST_NAME)
    lastname_field.send_keys("Smooth")
    zipcode_field = driver.find_element(*ZIP_CODE)
    zipcode_field.send_keys('1234')
    continue_button = driver.find_element(*CONTINUE_BUTTON)
    continue_button.click()

    total_price = driver.find_element(*TOTAL_PRICE).text
    assert '58.29' in total_price



