from src.components.base_element import BaseElement
from src.components.elements.create_gift_element import CreateGiftElement
from src.components.elements.gift_sent_element import GiftSentElement


class CreateGiftPage(BaseElement):

    def __init__(self, driver):
        super(CreateGiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/app/constructor'
        self._element = CreateGiftElement(driver)
        self._gift_sent_element = GiftSentElement(driver)

    def is_loaded(self):
        return self._element.is_exists_grid()

    def is_gift_sent(self):
        return self._gift_sent_element.is_exists_gird()
