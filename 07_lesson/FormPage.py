from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
    
def get_authorization(self):
    self.username = self.driver.find_element(By.ID, "user-name").send_keys('standard_user')
    self.password = self.driver.find_element(By.ID, "password")..send_keys('secret_sauce')
    self.button = self.find_element(By.ID, "login-button").click()

def get_shopping_cart(self):
    self.backpack = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    self.shirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    self.onesie = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")

def cart(self):
    input = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

def checkout(self):
    input = self.driver.find_element(By.ID, "checkout")  

def get_personal_data(self):
    self.first_name = self.driver.find_element(By.ID, "first-name").send_keys('Mariia')
    self.last_name = self.driver.find_element(By.ID, "last-name").send_keys('Litvinova')
    self.postal_code = self.driver.find_element(By.ID, "postal-code").send_keys('141260')

def get_search_results(self):
    return WebDriverWait(driver, 45).until(
          EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))
 
expected_total = 58.29
assert total_value == expected_total, (
 f"Итоговая сумма составляет ${total_value:.2f}, "
 f"ожидалось ${expected_total:.2f}")

driver.quit()
  
    assert checkout_page.get_total_amount() == "$58.29"
