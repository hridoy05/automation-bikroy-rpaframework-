from pages.BasePage import BasePage
from testdata.config import *
from utilities.locators import Locators
from RPA.Browser.Selenium import Selenium

browser = Selenium()


class LoginPage(BasePage):

    def __init__(self):
        self.log_in_link = Locators.log_in_link
        self.continue_with_email_button = Locators.continue_with_email_button
        self.user_email_id = Locators.user_email_id
        self.user_password_id = Locators.user_password_id
        self.login_button_id = Locators.login_button_id

    def click_log_in_link(self):
        browser.open_available_browser(baseUrl)
        browser.click_element(self.log_in_link)

    def click_continue_with_email_button(self):
        browser.click_element(self.continue_with_email_button)

    def submit_input_user_email(self):
        browser.input_text(self.user_email_id, valid_email, True)

    def submit_input_user_password(self):
        browser.input_text(self.user_password_id, valid_password, True)

    def submit_input_user_invalidemail(self):
        browser.input_text(self.user_email_id, invalid_email, True)

    def submit_input_user_invalidpassword(self):
        browser.input_text(self.user_password_id, invalid_password, True)

    def click_login_button(self):
        browser.click_button(self.login_button_id)
