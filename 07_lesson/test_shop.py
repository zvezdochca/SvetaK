import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ShopPage import ShopPage

txt = 'Total: $58.29'


@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    driver.get("https://www.saucedemo.com/")

    driver.implicitly_wait(30)
    yield driver
    driver.quit()


def test_shop(driver):
    shop = ShopPage(driver)
    shop.logged_for('standard_user','secret_sauce')
    shop.add_cart()
    shop.form_for('Svetlana', 'Kozlova', '12345')
    result = shop.total_amount()
    assert result == txt
