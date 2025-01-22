from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

for x in range(3):
    blye_button = (driver.find_element
                   (By.XPATH, "//button[text()='Button with Dynamic ID']"))

    blye_button.click()
    sleep(2)

driver.quit()
