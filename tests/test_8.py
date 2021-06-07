from pages.AdsPage import AdsPage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestDhakaLink(BaseTest):
    def test_dhaka_link(self):
        self.adsPage = AdsPage()
        self.adsPage.click_on_dhaka_link()



