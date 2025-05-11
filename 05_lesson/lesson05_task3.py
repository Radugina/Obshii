from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

number_input = driver.find_element(By.XPATH,'//input[@type="number"]')
number_input.send_keys("Sky", Keys.RETURN)
sleep(2)
number_input.clear()

number_input = driver.find_element(By.XPATH, '//input[@type="number"]')
number_input.send_keys("Pro", Keys.RETURN)
sleep(2)

driver.quit()