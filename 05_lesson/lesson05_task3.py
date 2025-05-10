from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

number_input = driver.find_element(By.XPATH,'//input[@type="number"]')
number_input.send_keys("Sky", Keys.RETURN)
number_input.clear()


number_input = driver.find_element(By.XPATH, '//input[@type="number"]')
number_input.send_keys("Pro", Keys.RETURN)

driver.quit()