from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def logged_for(self, username, password):
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='user-name']").send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='login-button']").click()

    def add_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "button[name='checkout']").click()

    def form_for(self, first_name,last_name, postal_code):
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='firstName']").send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='lastName']").send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='postalCode']").send_keys(postal_code)
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='continue']").click()

    def total_amount(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
