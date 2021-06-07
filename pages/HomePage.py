from pages.BasePage import BasePage
from RPA.Browser.Selenium import Selenium
from testdata.config import *
from utilities.locators import Locators

browser = Selenium()


class HomePage(BasePage):
    def __init__(self):
        self.all_adds_link = Locators.all_ads_link
        self.categories_text_class = Locators.categories_text_class
        self.chat_class = Locators.chat_class
        self.post_add_text = Locators.post_add_text
        self.copyright_text_class = Locators.copyright_text_class
        self.contact_us_link = Locators.contact_us_link
        self.facebook_link = Locators.facebook_link
        self.change_lan_link = Locators.change_lan_link

    def click_all_adds_link(self):
        browser.open_available_browser(baseUrl)
        browser.click_element(self.all_adds_link)

    def assert_categories_text(self):
        browser.open_available_browser(baseUrl)
        elementText = browser.get_text(self.categories_text_class)
        return elementText

    def do_click_chat_link(self):
        browser.open_available_browser(baseUrl)
        browser.click_element(self.chat_class)

    def assert_post_add_text(self):
        browser.open_available_browser(baseUrl)
        ele = browser.get_text(self.post_add_text)
        return ele

    def assert_copyright_text(self):
        browser.open_available_browser(baseUrl)
        ele = browser.get_text(self.copyright_text_class)
        return ele

    def click_contact_us_link(self):
        browser.open_available_browser(baseUrl)
        browser.execute_javascript("window.scrollTo(0,document.body.scrollHeight)")
        browser.click_element(self.contact_us_link)

    def click_facebook_link(self):
        browser.open_available_browser(baseUrl)
        browser.execute_javascript("window.scrollTo(0,document.body.scrollHeight)")
        browser.click_element(self.facebook_link)

    def click_change_lan_button(self):
        browser.open_available_browser(baseUrlBn)
        browser.click_element(self.change_lan_link)
