from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(25)
driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

content = driver.find_element(By.CSS_SELECTOR, '#content')
tet = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(tet)

driver.quit()
