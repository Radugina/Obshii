from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID, "ajaxButton")
button.click()

green_label = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "ajaxContebt")).text
)
text = green_label.text
print(text)
driver.quit()
