from src.components.base_element import BaseElement


class GiftElement(BaseElement):

    GIFTS_MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st._aid=NavMenu_User_Presents"]' \
                                '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    # AUTHORS_GIFTS_BUTTON = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st.cat=animatedGifts"]'
    AUTHORS_GIFTS_BUTTON = '//i[@class="tico_img ic ic_nav_bear"]'

    def is_marked(self):
        """
        Check for the existence of marked gifts item in nav bar
        :return: Bool
        """
        return self.existence_of_element_by_xpath(self.GIFTS_MARKED_ITEM_NAV_BAR)

    def get_authors_gift_button(self):
        return self.get_button_by_xpath(self.AUTHORS_GIFTS_BUTTON)
