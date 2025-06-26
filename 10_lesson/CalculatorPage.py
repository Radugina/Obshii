import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay: int):
        """
        Устанавливает задержку для выполнения операций на калькуляторе
        :param delay: int - время задержки в секундах
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажатие кнопок")
    def get_buttons(self) -> str:
        """
        Нажимаем несколько кнопок калькулятора по очереди
        :param: driver: WebDriver - объект драйвера, переданный фикстурой
        :param: delay: int - зарержка в секундах для выполнения операции
        :param: str  - первое число для операции
        :param: str  - операция "+"
        :param: str  - второе число для операции
        :param: str  - операция "="
        :param: result: str - ожидание результата операции
        """
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step("Получения результата")
    def get_result(self) -> str:
        """
       Ожидание появления ожидаемого результата на экране калькулятора
        :param: str - результат
        """
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text
