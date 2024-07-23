from selenium.webdriver.common.by import By
from .base_page.py import BasePage

class HomePage(BasePage):
    TITLE = (By.TAG_NAME,"title")

    def __init__(self,driver):
        super().__init__(driver)
        self.open(self.base_url)

    def get_title(self):
        return self.driver.title
