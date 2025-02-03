import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_03_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(30)
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(
        By.CSS_SELECTOR, "input[name='user-name']")
    username.send_keys("standard_user")

    password = driver.find_element(
        By.CSS_SELECTOR, "input[name='password']")
    password.send_keys("secret_sauce")

    login = driver.find_element(
        By.CSS_SELECTOR, "input[name='login-button']")
    login.click()

    # добавить в корзину
    backpack = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    backpack.click()

    t_shirt = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    t_shirt.click()
    onesie = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    onesie.click()

    # перейти в корзину
    cart_link = driver.find_element(
        By.CSS_SELECTOR, "a.shopping_cart_link")
    cart_link.click()

    checkout = driver.find_element(
        By.CSS_SELECTOR, "button[name='checkout']")
    checkout.click()

    first_name = driver.find_element(
        By.CSS_SELECTOR, "input[name='firstName']")
    first_name.send_keys("Svetlana")

    last_name = driver.find_element(
        By.CSS_SELECTOR, "input[name='lastName']")
    last_name.send_keys("Kozlova")

    postal_code = driver.find_element(
        By.CSS_SELECTOR, "input[name='postalCode']")
    postal_code.send_keys("123045")

    green_continue = driver.find_element(
        By.CSS_SELECTOR, "input[name='continue']")
    green_continue.click()

    # Прочитать итоговую стоимость
    total = driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)

    # проверить итоговую стоимость $58.29
    assert total == "Total: $58.29"
