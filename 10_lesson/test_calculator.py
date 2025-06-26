import pytest
import allure
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    """
    Открытие страницы сайта
    """
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет коррекность работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity("Critical")
def test_calculator(driver):
    """ 
    Тест проверяет работу калькулятора
    """
    calculator_page = CalculatorPage(driver)
    with allure.step("Установка задержки"): 
    calculator_page.set_delay("45")
    with allure.step("УНажатие кнопок"):
    calculator_page.get_buttons()
    with allure.step("Ожидание результата"):
    calculator_page.get_result()
    with allure.step("Ожидание результата"):
    result = calculator_page.get_result()
т   with allure.step("Проверка результата"):
    assert result == "15"
