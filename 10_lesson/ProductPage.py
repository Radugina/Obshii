import allure
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        """
        Конструктор класса ProductPage
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Добавление товара в корзину")
    def add_product(self) -> str:
        """
        Перемещаем по очереди товар в корзину
        :param: str  - первый товар
        :param: str  - второй товар
        :param: str  - третий товар
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def add_cart(self) -> bool:
        """
        Нажимает на кнопку корзина.
        :return: True, если кнопка нажата успешно.
        :rtype: bool
        """
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link").click()
