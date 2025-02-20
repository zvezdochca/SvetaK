from selenium.webdriver.common.by import By


class FormPage:
        def __init__(self, driver):
            self.driver = driver

        def search_for(self, first_name, last_name, address,
                       e_mail, phone, city, country, position, company):
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
            self.driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']").click()

        def check_red_field(self):
                zip_code = self.driver.find_element(
                    By.ID, "zip-code")
                assert "danger" in zip_code.get_attribute("class")

        def check_green_fields(self):
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
