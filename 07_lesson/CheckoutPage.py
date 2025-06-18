from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.datas = {
            'first-name': "Mariia",
            'last-name': "Litvinova",
            'postal-code': "141260"
        }

    def enter_data(self):
        for data, value in self.datas.items():
            self.wait.until(
                    EC.presence_of_element_located((
                        By.ID, data))).send_keys(value)
        self.driver.find_element(By.ID, "continue").click()

    def get_search_results(self):
        total_element = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        return total_text
