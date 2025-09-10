from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def get_buttons(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def get_result(self):
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text
