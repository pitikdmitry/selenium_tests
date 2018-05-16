import os
import unittest
from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote

from src.auth_factory import AuthFactory
from src.pages.auth_page import AuthPage
from src.pages.gift_page import GiftPage
from src.pages.main_page import MainPage


class GiftsPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.gift_page = GiftPage(self.driver)
        self.gift_page.open()

    def tearDown(self):
        self.driver.quit()


    def test_open_authors_gifts(self):
        authors_gift_page = self.gift_page.open_authors_gifts()
        ok = authors_gift_page.is_loaded()
        self.assertTrue(ok)

