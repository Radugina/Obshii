from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

WebDriverWait(driver, 10).until(
 EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_button.click()

add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
add_button.click()

driver.execute_script("window.scrollTo(0, 500)")
add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
add_button.click()

cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert cart_badge.text == "3", "В корзине должно быть 3 товара"

cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_button.click()

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

WebDriverWait(driver, 10).until(
 EC.presence_of_element_located((By.ID, "first-name")))

driver.get("https://www.saucedemo.com/checkout-step-one.html")
first_name_field = driver.find_element(By.ID, "first-name")
last_name_field = driver.find_element(By.ID, "last-name")
postal_code_field = driver.find_element(By.ID, "postal-code")
continue_button = driver.find_element(By.ID, "continue")

first_name_field.send_keys("Mariia")
last_name_field.send_keys("Litvinova")
postal_code_field.send_keys("141260")
continue_button.click()

WebDriverWait(driver, 10).until(
 EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))

total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_text = total_element.text
total_value = float(total_text.split("$")[1])

expected_total = 58.29
assert total_value == expected_total, (
 f"Итоговая сумма составляет ${total_value:.2f}, "
 f"ожидалось ${expected_total:.2f}")

driver.quit()
