import pytest
from selenium import webdriver
from lesson_07.website import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_checkout_total(driver):
    website = FormPage(driver)
    website.get_authorization()
    website.get_shopping_cart()
    website.cart()
    website.checkout()
    website.get_personal_data()
    result = website.get_search_results()

assert checkout_page.get_total_amount() == "$58.29"