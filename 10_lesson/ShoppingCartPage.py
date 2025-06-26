import allure
from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, driver):
        """
        Конструктор класса ShoppingCartPage
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Корзина")
    def add_cart(self) -> bool:
        """
        Нажимает на кнопку корзина.
        :return: True, если кнопка нажата успешно.
        :rtype: bool
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Нажать кнопку Checkout")
    def checkout(self) -> bool:
        """
        Нажимает на кнопку Checkout.
        :return: True, если кнопка нажата успешно.
        :rtype: bool
        """
        self.driver.find_element(By.ID, "checkout").click()
