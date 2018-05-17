from src.components.base_element import BaseElement
from src.components.elements.search_gift_element import SearchGiftElement


class SearchGiftPage(BaseElement):

    def __init__(self, driver):
        super(SearchGiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts'
        self._element = SearchGiftElement(driver)

    def is_search_done(self):
        return self._element.is_search_done()
