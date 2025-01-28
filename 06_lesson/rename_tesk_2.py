from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(25)
driver.get("http://uitestingplayground.com/textinput")

text = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
text.send_keys("SkyPro")
blue_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

form = driver.find_element(By.CSS_SELECTOR, "div.form-group")
text = form.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(text)

driver.quit()
