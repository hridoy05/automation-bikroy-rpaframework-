from pages.BasePage import BasePage
import requests


class Test_2:
    def test_invalid_url(self):
        basePage = BasePage()
        res = requests.head((basePage.open_site_invalid_url()))
        print(res)
        if res.status_code != 200:
            assert True
