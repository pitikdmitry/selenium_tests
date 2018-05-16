import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.auth_factory import AuthFactory
from src.pages.auth_page import AuthPage
from src.pages.main_page import MainPage


class GiftsPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self._auth = AuthFactory.create(username='technopark8')

        self.auth_page = AuthPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.gift_page = self.main_page.open_gifts()
        _ = self.gift_page.is_loaded()

        self._open_gifts()

    def tearDown(self):
        self.driver.quit()

    def _open_gifts(self):
        self.auth_page.sign_in(self._auth.username, self._auth.password)
        return self.main_page.open_gifts()

    def test_open_authors_gifts(self):
        authors_gift_page = self.gift_page.open_authors_gifts()

        # ok = gifts_page.is_loaded()
        # self.assertTrue(ok)

