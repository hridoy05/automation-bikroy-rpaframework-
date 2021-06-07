from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestFacebookLink(BaseTest):
    def test_facebook_link(self):
        self.homePage = HomePage()
        self.homePage.click_facebook_link()

