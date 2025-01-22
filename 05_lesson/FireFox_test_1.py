from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

close_button = driver.find_element(By.XPATH, "//div[@id='modal']").click()

sleep(3)

driver.quit()
