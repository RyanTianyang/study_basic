# !/usr/bin/env python
# encoding: utf-8
from page_object.drivers.Xueqiu_client import XueqiuClient


class Selected_Page(object):

    def get_PriceByName(self, name) -> float:
        price = XueqiuClient.driver.find_element_by_xpath \
            ("//*[contains(@resource-id,'index_name') and @text='" + name + "']" +
             "/..//*[contains(@resource-id,'index_price')]").text

        return float(price)
