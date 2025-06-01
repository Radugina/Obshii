from selenium import webdriver
from selenium.webdriver.common.by import By

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

submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

field_locators = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "company"]
for locator in field_locators:
  field = driver.find_element(By.Name, locator)
background_color = field.value_of_css_property("background-color")
assert background_color == "rgb(186, 219, 204)"

pole_z = driver.find_element(By.ID, "zip-code").get_attribute("class")
assert pole_z == "alert py-2 alert-danger"
