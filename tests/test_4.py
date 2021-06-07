
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestInValidLogin(BaseTest):

    def test_login_invalid(self):
        self.loginPage = LoginPage()
        self.loginPage.click_log_in_link()
        self.loginPage.click_continue_with_email_button()
        self.loginPage.submit_input_user_invalidemail()
        self.loginPage.submit_input_user_invalidpassword()
        self.loginPage.click_login_button()



