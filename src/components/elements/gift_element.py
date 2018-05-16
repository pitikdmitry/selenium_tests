from src.components.base_element import BaseElement


class GiftElement(BaseElement):

    GIFTS_MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st._aid=NavMenu_User_Presents"]' \
                                '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    # AUTHORS_GIFTS_BUTTON = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st.cat=animatedGifts"]'
    AUTHORS_GIFTS_BUTTON = '//i[@class="tico_img ic ic_nav_bear"]'

    # ACTUAL_GIFTS_BUTTON = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st.cat=main"]'
    ACTUAL_GIFTS_BUTTON = '//i[@class="tico_img ic ic_nav_gifts"]'

    # POSTACARDS_BUTTON = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st.cat=liveGifts"]'
    POSTACARDS_BUTTON = '//i[@class="tico_img ic ic_nav_flower"]'

    def is_marked(self):
        return self.existence_of_element_by_xpath(self.GIFTS_MARKED_ITEM_NAV_BAR)

    def get_authors_gift_button(self):
        return self.get_button_by_xpath(self.AUTHORS_GIFTS_BUTTON)

    def get_actual_gift_button(self):
        return self.get_button_by_xpath(self.ACTUAL_GIFTS_BUTTON)

    def get_postcard_button(self):
        return self.get_button_by_xpath(self.POSTACARDS_BUTTON)
