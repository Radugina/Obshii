from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

zip_code_element = driver.find_element(By.ID, "zip-code")
border_color = zip_code_element.value_of_css_property("border-color")
assert border_color == "rgb(255, 0, 0)", "Поле Zip code не подсвечено красным"

fields = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]

for field_id in fields:
field_element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
border_color = field_element.value_of_css_property("border-color")
assert border_color == "rgb(132, 32, 41)", f"Поле {field_id} не подсвечено зеленым"
