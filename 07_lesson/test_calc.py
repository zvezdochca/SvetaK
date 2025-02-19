import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


buttons = ['7', '+', '8', '=']
txt = '15'


def test_calculator(driver):
    calculator = CalcPage(driver)
    calculator.locator_for("45")
    calculator.get_buttons()
    calculator.check_result()
    result = calculator.check_result()
    assert result == txt
