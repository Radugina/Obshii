import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.datas = {
            'first-name': "Mariia",
            'last-name': "Litvinova",
            'postal-code': "141260"
        }

    @allure.step("Заполнение формы своими данными")
    def enter_data(self) -> str:
        """
        Заполнить поля
        :param first-name: str - Mariia
        :param last-name: str - Litvinova
        :param postal-code: str - 141260
        """
        for data, value in self.datas.items():
            self.wait.until(
                    EC.presence_of_element_located((
                        By.ID, data))).send_keys(value)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Результат")
    def get_search_results(self) -> int:
        """
        Прочитать со страницы итоговую стоимость
        :param summary_total_label: int - итоговая сумма
        """
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        return total_text
