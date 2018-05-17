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

    # VIP_GIFT_BUTTON = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st.cat=vipSale"]'
    VIP_GIFT_BUTTON = '//i[@class="tico_img ic ic_nav_vipsale"]'

    CREATE_GIFT_BUTTON = '//a[@hrefattrs="st.cmd=appMain&st.appId=5738496"]'
    # CREATE_GIFT_BUTTON = '//i[@class="gifts-sidebanner_tx"]'

    FIRST_GIFT_BUTTON = '//a[@hrefattrs="st.cmd=giftsFront&st.cat=main&st.fsId=1526495585366&cmd=PopLayer&st.layer.cmd=PopLayerSendPresentSelectFriendComposite&st.layer.sd=7aqlsExHOryS3f6JDcC2A5aFLBcBTZP_YLQCx7c6ZR62sYjoGMQjoBP9ME6sFBL3SbRkRFmjHEbhrE-yvFf1_pjGS05IAFNJRvbQF3w78FjoinnolYmUD6VvPeeCs4XBbg8cfsrPUbKZAmsIVPOCnZ2uuw3qJzMqg9xwEdNL6rPWvoSnh1slM7zmriINiYHL&st.layer.gfPresent=855747528267"]'

    def is_marked(self):
        return self.existence_of_element_by_xpath(self.GIFTS_MARKED_ITEM_NAV_BAR)

    def get_authors_gift_button(self):
        return self.get_button_by_xpath(self.AUTHORS_GIFTS_BUTTON)

    def get_actual_gift_button(self):
        return self.get_button_by_xpath(self.ACTUAL_GIFTS_BUTTON)

    def get_postcard_button(self):
        return self.get_button_by_xpath(self.POSTACARDS_BUTTON)

    def get_vip_gift_button(self):
        return self.get_button_by_xpath(self.VIP_GIFT_BUTTON)

    def get_create_gift_button(self):
        return self.get_button_by_xpath(self.CREATE_GIFT_BUTTON)

    def get_first_gift_button(self):
        return self.get_button_by_xpath(self.FIRST_GIFT_BUTTON)

    def get_send_gift_secretly_button(self):
        return self.get_button_by_xpath(self.CREATE_GIFT_BUTTON)
