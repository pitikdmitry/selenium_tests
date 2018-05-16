from src.components.base_element import BaseElement
from src.components.elements.gift_element import GiftElement
from src.pages.authors_gifts_page import AuthorsGiftPage


class GiftPage(BaseElement):

    def __init__(self, driver):
        super(GiftPage, self).__init__(driver)
        self._url = 'http://ok.ru/gifts'
        self._gift_element = GiftElement(driver)

    def is_loaded(self):
        return self._gift_element.is_marked()

    def open_authors_gifts(self):
        self._gift_element.get_authors_gift_button().click()
        return AuthorsGiftPage(self.driver)
