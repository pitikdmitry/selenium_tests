from src.components.base_element import BaseElement
from src.components.elements.authors_gift_element import AuthorsGiftElement
from src.components.elements.gift_element import GiftElement


class AuthorsGiftPage(BaseElement):

    def __init__(self, driver):
        super(AuthorsGiftPage, self).__init__(driver)
        self._url = 'http://ok.ru/https://ok.ru/gifts/authorGifts'
        self._authors_gift_element = AuthorsGiftElement(driver)
    #
    # def is_loaded(self):
    #     return self._authors_gift_element.is_marked()
    #
    # def open_authors_gifts(self):
    #     self._authors_gift_element.get_authors_gift_button().click()
    #     return