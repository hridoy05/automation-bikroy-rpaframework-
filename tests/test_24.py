from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class TestChatLink(BaseTest):
    def test_chat_link(self):
        self.homePage = HomePage()
        self.homePage.do_click_chat_link()

