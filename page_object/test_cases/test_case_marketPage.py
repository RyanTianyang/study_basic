# !/usr/bin/env python
# encoding: utf-8
from page_object.pages.mainPage import MainPage


class Test_selected_marketPage(object):

    def test_price(self):
        main=MainPage()
        assert main.ClickSelected("行情").get_PriceByName("深证成指")>8000