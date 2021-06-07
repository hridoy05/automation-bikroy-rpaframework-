from pages.BasePage import BasePage


class Test_Url:
    def test_url(self):
        self.basePage = BasePage()
        self.basePage.open_site()
        self.basePage.close_site()
