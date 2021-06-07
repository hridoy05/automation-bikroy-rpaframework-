import pytest

from pages.LoginPage import LoginPage
from RPA.Browser.Selenium import Selenium


@pytest.fixture(scope='class')
def init_driver():
    lib = Selenium()
    yield lib
    lib.close_all_browsers()
