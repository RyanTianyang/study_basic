# !/usr/bin/env python
# encoding: utf-8
from page_object.pages.App import App
from page_object.pages.mainPage import MainPage


class Test_selected_marketPage(object):

    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()

    def test_price(self):
        assert self.mainPage.Click_market().get_PriceByName("深证成指")>8000