from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestChangeLanLink(BaseTest):
    def test_Change_lan_link(self):
        self.homePage = HomePage()
        self.homePage.click_change_lan_button()

