from selenium import webdriver
from time import sleep
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

for name, value in driver.find_element.items():
    field = driver.find_element(By.NAME, name)
    field.clear()
    field.send_keys(value)

submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

sleep(2)

for id, value in driver.find_element.items():
    field = driver.find_element(By.ID, id)
    border_color = field.value_of_css_property("border-color")

if value:
    assert border_color == "rgb(186, 219, 204)", f"Поле {id} подсвечено зеленым."
    print(f"Поле {id} подсвечено зеленым.")
else:
    assert border_color == "rgb(245, 194, 199)", f"Поле {id} подсвечено красным."
    print(f"Поле {id} подсвечено красным.")
