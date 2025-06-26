import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce"
        }

    @allure.step("Открытие страницы сайта")
    def open(self):
        self.driver.get("https://www.saucedemo.com")

    @allure.step("Авторизация")
    def fill_form(self) -> None:
        """
        Подождать пока откроется страница
        :param user-name: str - standard_user
        :param password: str - secret_sauce
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажатие кнопки авторизоваться")
    def submit_form(self) -> bool:
        """
        Нажимает кнопку авторизоваться.
        :return: True, если кнопка нажата успешно.
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.ID, "login-button"))).click()
