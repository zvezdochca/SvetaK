import allure
from selenium.webdriver.common.by import By

@allure.severity("blocker")
class FormPage:
    """
    Этот класс представляет сущность "Типы данных"
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.description("Форма для заполнения пользователя")
    @allure.title("Пользователь")
    @allure.feature("CREATE")
    def search_for(self, first_name:str, last_name:str, address:str,
                   e_mail:str, phone:str, city:str, country:str, position:str, company:str):
            """
            Эта функция заполняет форму значениями.
            """
            with allure.step("Заполнить форму пользователя"):
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='address']").send_keys(address)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='e-mail']").send_keys(e_mail)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='city']").send_keys(city)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='country']").send_keys(country)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='job-position']").send_keys(position)
             self.driver.find_element(
                By.CSS_SELECTOR, "input[name='company']").send_keys(company)

            with allure.step("Нажать на кнопку Submit"):
             self.driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']").click()

    @allure.description("Проверка полей красного цвета")
    @allure.title("Красные поля")
    @allure.feature("UPDATE")
    def check_red_field(self) -> str:
           """
           Эта функция проверяет поля красного цвета.
           """
           with allure.step("Проверка полей красного цвета"):
            zip_code = self.driver.find_element(
                By.ID, "zip-code")
            assert "danger" in zip_code.get_attribute("class")

    @allure.description("Проверка полей зеленого цвета")
    @allure.title("Зеленые поля")
    @allure.feature("UPDATE")
    def check_green_fields(self) -> str:
         """
            Эта функция проверяет поля зеленного цвета.
            """
         with allure.step("Проверка полей зеленого цвета"):
           first_name = self.driver.find_element (
                    By.ID, 'first-name')
           assert "success" in first_name.get_attribute("class")
           last_name = self.driver.find_element(
                    By.ID, 'last-name')
           assert "success" in last_name.get_attribute("class")
           address = self.driver.find_element(
                    By.ID, 'address')
           assert "success" in address.get_attribute("class")
           mail = self.driver.find_element(
                    By.ID, 'e-mail')
           assert "success" in mail.get_attribute("class")
           phone = self.driver.find_element(
                    By.ID, 'phone')
           assert "success" in phone.get_attribute("class")
           city = self.driver.find_element(
                    By.ID, 'city')
           assert "success" in city.get_attribute("class")
           country = self.driver.find_element(
                    By.ID, 'country')
           assert "success" in country.get_attribute("class")
           job_position = self.driver.find_element(
                    By.ID, 'job-position')
           assert "success" in job_position.get_attribute("class")
           company = self.driver.find_element(
                    By.ID, 'company')
           assert "success" in company.get_attribute("class")