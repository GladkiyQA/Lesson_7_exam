import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fill_form_and_validate():
    options = Options()
    options.add_argument("--window-size=1000,1000") # Если хочется визуала
    options.add_argument("--headless")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",  # Оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field, value in form_data.items():
        input_field = driver.find_element('xpath', f'//input[@name="{field}"]')
        input_field.clear()
        input_field.send_keys(value)

    submit_button = driver.find_element('xpath', '//button[@type="submit"]').click()

    zip_code_field = driver.find_element('xpath', '//div[@id="zip-code"]')
    assert 'alert-danger' in zip_code_field.get_attribute('class')

    other_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field in other_fields:
        input_field_full = driver.find_element('xpath', f'//div[@id="{field}"]')
        assert 'alert-success' in input_field_full.get_attribute('class')


