from pages.BasePage import BasePage
from testdata.config import *
from utilities.locators import Locators
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class AdsPage(BasePage):

    def __init__(self):
        self.mobile_link = Locators.mobile_link
        self.dhaka_link = Locators.dhaka_link
        self.search_bar_id = Locators.search_bar_id

    def click_on_mobiles_link(self):
        browser.open_available_browser(adsUrl)
        browser.click_element(self.mobile_link)

    def click_on_dhaka_link(self):
        browser.open_available_browser(adsUrl)
        browser.click_element(self.dhaka_link)

    def input_search_bar(self):
        browser.open_available_browser(adsUrl)
        browser.input_text(self.search_bar_id, "dell laptop")
