import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.severity("blocker")
class CalcPage:
    """
    Этот класс представляет сущность "Калькулятор".
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.story("Ввод значений по локатору")
    @allure.epic("Локатор")
    @allure.feature("READ")
    def locator_for(self, query):
        """
        Эта функция запрашивает поле ввода по локатору и вводит значение.
        """
        with allure.step("Запрос поле ввода"):
            delay = self.driver.find_element(
                By.CSS_SELECTOR, "input[id='delay']")
        with allure.step("Ввод значения"):
             delay.clear()
             delay.send_keys(query)

    @allure.description("Сложение чисел в калькуляторе")
    @allure.title("Числа")
    @allure.feature("CREATE")
    def get_buttons(self, param_1:int, param_2:int, param_3:int, param_4:int):
        """
        Эта функция берет первые два параметра, складывает их.
        """
        with allure.step("Создать пример"):
            param_1 = self.driver.find_element(By.XPATH, "//span[text()='7']").click()
            param_2 = self.driver.find_element(By.XPATH, "//span[text()='+']").click()
            param_3 = self.driver.find_element(By.XPATH, "//span[text()='8']").click()
            param_4 = self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.description("Результат сложения чисел")
    @allure.title("Итоговая сумма")
    @allure.feature("UPDATE")
    def check_result(self) -> str:
        """
        Эта функция осуществляет задержку и отображает в окне результат.
        """
        with allure.step("Получение результата с задержкой."):
            WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div[class="screen"]'), "15"))
            return self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text