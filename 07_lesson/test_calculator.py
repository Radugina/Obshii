import pytest
from selenium import webdriver
from calculator import Calculator


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_search(driver):
    calculator = Calculator(driver)
    calculator.set_delay("45")
    result = calculator.get_search_results()

    assert result == "15"
