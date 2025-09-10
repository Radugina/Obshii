import pytest
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.set_delay("45")
    calculator_page.get_buttons()
    calculator_page.get_result()
    result = calculator_page.get_result()

    assert result == "15"
