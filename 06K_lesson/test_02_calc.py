import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_02_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(30)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Задержка
    driver.find_element(
        By.CSS_SELECTOR, "input[id='delay']").clear()
    driver.find_element(
        By.CSS_SELECTOR, "input[id='delay']").send_keys("45")

    # расчет 7 + 8
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "div.screen"), "15"))

    # проверить результат
    result = driver.find_element(
        By.CSS_SELECTOR, "div.screen").text
    assert int(result) == 15
