from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestLogin(BaseTest):

    def test_login_valid(self):
        self.loginPage = LoginPage()
        self.loginPage.click_log_in_link()
        self.loginPage.click_continue_with_email_button()
        self.loginPage.submit_input_user_email()
        self.loginPage.submit_input_user_password()
        self.loginPage.click_login_button()



