from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestPostADDText(BaseTest):
    def test_post_add_text_assert(self):
        self.homePage = HomePage()
        text = self.homePage.assert_post_add_text()
        if text == "POST YOUR AD":
            assert True

