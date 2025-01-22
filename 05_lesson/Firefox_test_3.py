from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.NAME, "username")

username.send_keys("tomsmith")

sleep(2)

password = driver.find_element(By.NAME, "password")

password.send_keys("SuperSecretPassword!")

Login = driver.find_element(By.TAG_NAME, "i")

driver.quit()
