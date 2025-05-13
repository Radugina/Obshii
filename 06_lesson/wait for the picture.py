from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
award_element = wait.until(EC.presence_of_element_located((By.ID, "award")))
src = award_element.get_attribute("src")
print(src)

driver.quit()
