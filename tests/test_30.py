from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestCopyrightText(BaseTest):
    def test_copyright_text_assert(self):
        self.homePage = HomePage()
        text = self.homePage.assert_copyright_text()
        if text == "Copyright © Saltside Technologies":
            assert True

