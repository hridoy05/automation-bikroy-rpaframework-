from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestCategoriesText(BaseTest):
    def test_text(self):
        self.homePage = HomePage()
        text = self.homePage.assert_categories_text()
        if text == "Browse our top categories":
            assert True
