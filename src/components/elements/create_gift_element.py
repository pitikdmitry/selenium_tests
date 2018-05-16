from src.components.base_element import BaseElement


class CreateGiftElement(BaseElement):

    # XPATH_GRID = '//div[@id="id-start_choose_photo_btn"]'
    XPATH_GRID = '//div[@class="con-txt __lasco __extralarge pts_string pts_startcaption js-congrat_intro"]'

    def __init__(self, driver):
        super(CreateGiftElement, self).__init__(driver)

    def is_exists_grid(self):
        return self.existence_of_element_in_dom_by_xpath(self.XPATH_GRID)
        # return self.existence_of_element_by_xpath(self.XPATH_GRID)
