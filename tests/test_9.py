from pages.AdsPage import AdsPage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestSearchBar(BaseTest):
    def test_search_bar(self):
        self.adsPage = AdsPage()
        self.adsPage.input_search_bar()




