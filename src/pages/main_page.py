from src.components.elements.main_element import MainElement
from src.pages.base_page import BasePage
from src.pages.gift_page import GiftPage


class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.main_element = MainElement(self.driver)

    def open_gifts(self):
        self.main_element.get_gifts_button().click()
        return GiftPage(self.driver)
