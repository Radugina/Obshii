from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, browser):
        self.driver = browser


def get_shopping_cart(self):
    self.backpack = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    self.shirt = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    self.onesie = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
