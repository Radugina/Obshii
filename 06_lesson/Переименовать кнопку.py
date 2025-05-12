from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, ".form-control")
input.send_keys("SkyPro")
input.click()

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton") 
button.click()

print(button.text)
driver.quit()