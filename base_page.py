from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.base_url = "https://petstore.octoperf.com/actions/Catalog.action"

    def find_element(self, *locator):
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))

    def open(self,url):
        self.driver.get(url)