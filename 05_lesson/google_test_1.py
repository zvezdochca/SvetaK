from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(5):
    addButton = driver.find_element(By.XPATH,
                                    ("//button[text()='Add Element']"))
    addButton.click()
    sleep(2)

delButton = driver.find_elements(By.XPATH, ("//button[text()='Delete']"))
print(len(delButton))

driver.quit()
