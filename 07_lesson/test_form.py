import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FormPage


@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


def test_search(driver):
    page = FormPage(driver)
    page.search_for('Иван', 'Петров',
                    'Ленина, 55-3', 'test@skypro.com', '+7985899998787',
                    'Москва',  'Россия', 'QA', 'SkyPro')


def check_red_field(driver):
    field = FormPage(driver)
    field.check_red_field()


def check_green_fields(driver):
    fields = FormPage(driver)
    fields.check_green_fields()
