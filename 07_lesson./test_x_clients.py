import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_total(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_form()
    login_page.submit_form()

    product_page = ProductPage(driver)
    product_page.add_product()

    shopping_cart_page = ShoppingCartPage(driver)
    shopping_cart_page.add_cart()
    shopping_cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_data()

    assert checkout_page.get_search_results() == "Total: $58.29"
