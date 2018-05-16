from src.components.base_element import BaseElement
from src.components.elements.gift_element import GiftElement
from src.pages.actual_gift_page import ActualGiftPage
from src.pages.auth_page import AuthPage
from src.pages.authors_gift_page import AuthorsGiftPage
from src.pages.postcard_page import PostCardPage
from src.pages.vip_gift_page import VipGiftPage


class GiftPage(BaseElement):

    def __init__(self, driver):
        super(GiftPage, self).__init__(driver)
        self._url = 'http://ok.ru/gifts'
        self._gift_element = GiftElement(driver)
        self._auth_page = AuthPage(driver)

    def is_loaded(self):
        return self._gift_element.is_marked()

    def open_authors_gifts(self):
        btn = self._gift_element.get_authors_gift_button()
        btn.click()
        return AuthorsGiftPage(self.driver)

    def open_actual_gifts(self):
        btn = self._gift_element.get_actual_gift_button()
        btn.click()
        return ActualGiftPage(self.driver)

    def open_postcards(self):
        btn = self._gift_element.get_postcard_button()
        btn.click()
        return PostCardPage(self.driver)

    def open_vip_gifts(self):
        btn = self._gift_element.get_vip_gift_button()
        btn.click()
        return VipGiftPage(self.driver)

    def open(self):
        self._auth_page.open_and_sign_in()
        self.driver.get(self._url)
