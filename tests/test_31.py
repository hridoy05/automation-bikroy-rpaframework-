from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestContactUsLink(BaseTest):
    def test_contact_us_link(self):
        self.homePage = HomePage()
        self.homePage.click_contact_us_link()

