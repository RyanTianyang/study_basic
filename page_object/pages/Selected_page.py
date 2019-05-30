# !/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.mobileby import MobileBy

from page_object.drivers.Xueqiu_client import XueqiuClient
from page_object.pages.BasePage import BasePage


class Selected_Page(BasePage):

    def get_PriceByName(self, name) -> float:
        priceLocator = (MobileBy.XPATH, "//*[contains(@resource-id,'index_name') and @text='%s']" % name +
                 "/..//*[contains(@resource-id,'index_price')]")
        price=self.find(priceLocator).text
        return float(price)
