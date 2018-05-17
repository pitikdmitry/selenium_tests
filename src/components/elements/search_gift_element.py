from src.components.base_element import BaseElement


class SearchGiftElement(BaseElement):

    # XPATH_GRID = '//div[contains(@class, "ugrid")][contains(@class, "__vipSale")]'
    XPATH_GRID_SEARCH_HAS_DONE = '//div[@class="ugrid __xxxl __search __type-search"]'
    # XPATH_GRID_SEARCH_HAS_DONE = '//div[contains(@class, "ugrid")][contains(@class, "__search")][contains(@class, "__type-search"]'
    # XPATH_ROSE = '//div[@class="ugrid_i soh-s posR"]'

    def __init__(self, driver):
        super(SearchGiftElement, self).__init__(driver)

    def is_search_done(self):
        return self.existence_of_element_by_xpath(self.XPATH_GRID_SEARCH_HAS_DONE)
