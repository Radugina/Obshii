from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, browser):
        self.driver = browser


def get_personal_data(self):
    self.first_name = self.driver.find_element(By.ID, "first-name").send_keys('Mariia')
    self.last_name = self.driver.find_element(By.ID, "last-name").send_keys('Litvinova')
    self.postal_code = self.driver.find_element(By.ID, "postal-code").send_keys('141260')


def get_search_results(self):
    self.total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
