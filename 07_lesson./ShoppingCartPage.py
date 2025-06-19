from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
