import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    options = Options()
    # options.add_argument("--window-size=1000,1000") # Если хочется визуала
    options.add_argument("--headless")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 60, 1)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    DELAY_FIELD = ('xpath', '//input[@id="delay"]')
    VALUE_OF_SEVEN = ('xpath', '//span[text()="7"]')
    VALUE_OF_EIGHT = ('xpath', '//span[text()="8"]')
    VALUE_OF_ADDITION = ('xpath', '//span[text()="+"]')
    VALUE_OF_EQUALS = ('xpath', '//span[text()="="]')
    APPEARANCE_RESULT = ('xpath', '//div[text()="15"]')

    delay_field = driver.find_element(*DELAY_FIELD)
    delay_field.clear()
    delay_field.send_keys("45")

    click_to_seven = driver.find_element(*VALUE_OF_SEVEN)
    click_to_seven.click()
    click_to_addition = driver.find_element(*VALUE_OF_ADDITION)
    click_to_addition.click()
    click_to_eight = driver.find_element(*VALUE_OF_EIGHT)
    click_to_eight.click()
    click_to_equals = driver.find_element(*VALUE_OF_EQUALS)
    click_to_equals.click()

    output_filed = wait.until(EC.visibility_of_element_located(APPEARANCE_RESULT))
    finally_result = driver.find_element(*APPEARANCE_RESULT).text

    assert '15' in finally_result





