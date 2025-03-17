import allure
from selenium.webdriver.common.by import By

@allure.severity("blocker")
class ShopPage:
    """
    Этот класс представляет сущность "Интернет-Магазин".
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.description("Авторизация пользователя")
    @allure.title("Пользователь")
    @allure.feature("CREATE")
    def logged_for(self, username:str, password:str):
        """
        Эта функция заполняет поля и проводится авторизация пользователя.
        """
        with allure.step("Заполнить поля и нажать кнопку для авторизации."):
            self.driver.find_element(
            By.CSS_SELECTOR, "input[name='user-name']").send_keys(username)
            self.driver.find_element(
            By.CSS_SELECTOR, "input[name='password']").send_keys(password)
            self.driver.find_element(
            By.CSS_SELECTOR, "input[name='login-button']").click()

    @allure.description("Наполнения корзины и просмотр результата")
    @allure.title("Товар")
    @allure.feature("CREATE")
    def add_cart(self) -> list:
     """
        Эта функция выбирает и наполняет корзину товаром.
        Просмотр результата выбранного товара в корзине.
     """
     with allure.step("Добавить товар"):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
     with allure.step("Перейти в корзину"):
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "button[name='checkout']").click()

    @allure.description("Заполнение формы данными о покупателе")
    @allure.title("Покупатель")
    @allure.feature("CREATE")
    def form_for(self, first_name:str,last_name:str, postal_code:str):
        """
        Функция заполняет форму данными покупателя.
        """
        with allure.step("Заполнить форму покупателя"):
         self.driver.find_element(
            By.CSS_SELECTOR, "input[name='firstName']").send_keys(first_name)
         self.driver.find_element(
            By.CSS_SELECTOR, "input[name='lastName']").send_keys(last_name)
         self.driver.find_element(
            By.CSS_SELECTOR, "input[name='postalCode']").send_keys(postal_code)
         self.driver.find_element(
            By.CSS_SELECTOR, "input[name='continue']").click()

    @allure.description("Получение итоговой суммы")
    @allure.title("Результат")
    @allure.feature("UPDATE")
    def total_amount(self) -> str:
        """
         Функция проверяет итоговую сумму покупки.
        """
        with allure.step("Получение итоговой суммы товара."):
           return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text