import allure
import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    """ 
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Тестирование работы электронного магазина")
@allure.description("Тест проверяет коррекность работы сайта для заказов")
@allure.feature("Электронный магазин")
@allure.severity("Critical")

def test_checkout_total(driver):
    """ 
    Тест проверяет работу электронного мазагина
    """
    login_page = LoginPage(driver)
    with allure.step("Открытие сайта"):
    login_page.open()
    with allure.step("Авторизация"):
    login_page.fill_form()
    with allure.step("Нажатие кнопки"):
    login_page.submit_form()

    product_page = ProductPage(driver)
    with allure.step("Добавление товара в корзину"):
    product_page.add_product()

    shopping_cart_page = ShoppingCartPage(driver)
    with allure.step("Переход в корзину"):
    shopping_cart_page.add_cart()
    with allure.step("Нажатие кнопки Checkout"):
    shopping_cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    with allure.step("Заполненеи данных формы"):
    checkout_page.enter_data()

    with allure.step("Проверка итоговой суммы"):
    assert checkout_page.get_search_results() == "Total: $58.29"
