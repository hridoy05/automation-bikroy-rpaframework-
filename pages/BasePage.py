from RPA.Browser.Selenium import Selenium

browser = Selenium()

url = "https://bikroy.com/en"
invalid_url = "https://bikroy.net"
class BasePage:

    @classmethod
    def open_site(cls):
        browser.open_available_browser(url)

    def close_site(self):
        browser.close_browser()

    def open_site_invalid_url(self):
        browser.open_available_browser(self.invalid_url)
