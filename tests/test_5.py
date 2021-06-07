from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestAllAdds(BaseTest):
    def test_all_add_links(self):
        self.homePage = HomePage()
        self.homePage.click_all_adds_link()
