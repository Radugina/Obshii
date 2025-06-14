from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.driver = browser


def get(self):
    self.driver.get("https://www.saucedemo.com/")


def get_authorization(self):
    self.username = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    self.password = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
