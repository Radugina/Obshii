from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, browser):
        self.driver = browser


def get(self):
    self.driver.get("https://www.saucedemo.com/cart.html")


def checkout(self):
    self.checkout_button = self.driver.find_element(By.ID, "checkout")
