import unittest
from selenium import webdriver
from pages.home_page import HomePage

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.chrome()
        self.home_page = HomePage(self.driver)

    def test_home_page_title(self):
        title = self.home_page.get_title()
        self.assertIn("JPetStoreDemo",title)

    def tearDown(self):
        self.quit()

if __name__ == "__main__":
    unittest.main()
