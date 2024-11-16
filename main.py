import os

import allure
from assertpy import assert_that
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# https://www.chitai-gorod.ru/

# Загружаем переменные окружения из файла .env
load_dotenv()

UI_BASE_URL = os.getenv("UI_BASE_URL")
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT"))


@allure.feature('ID: Kurs 2')
@allure.title('Поле для поиска принимает ввод данных')
def test_search_input():
    driver = set_up()
    test_data_search_input = "Математика"

    input_search_element = wait_element(driver, (By.CSS_SELECTOR, "[class=header-search__input]"))
    fill_input(input_search_element, test_data_search_input)
    assert_input_value_equal(input_search_element, test_data_search_input)
    tear_down(driver)


def assert_input_value_equal(input_search_element, expected):
    # Проверяем, что поле поиска содержит ожидаемый текст "Математика"
    assert_that(input_search_element.get_attribute('value')).is_equal_to(expected)


def fill_input(element, text):
    element.send_keys(text)


def wait_element(driver, locator):
    return WebDriverWait(driver, EXPLICIT_WAIT).until(EC.visibility_of_element_located(locator))


def tear_down(driver):
    # Закрываем браузер
    driver.quit()


def set_up():
    # Настройка опций для Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.page_load_strategy = 'eager'
    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, EXPLICIT_WAIT)
    # Открываем главную страницу
    driver.get(UI_BASE_URL)
    return driver
