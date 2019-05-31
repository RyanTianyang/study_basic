# !/usr/bin/env python
# encoding: utf-8

import pytest

from page_object.pages.App import App


class Test_search(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        self.searchPage = self.mainPage.Go_MainPage_Search()

    @pytest.mark.parametrize("key,keycode", [
        ("汽车之家", "ATHM"),
        ("宝宝树集团", "01761"),
    ])
    def test_is_selected(self, key, keycode):
        self.searchPage.input_Search(key)
        assert self.searchPage.is_Selected(keycode) == True

    def test_addStock(self):
        key = "招商银行"
        keycode = "SH600036"
        searched = self.searchPage.input_Search(key)
        if searched.is_Selected(keycode) == True:
            searched.remove_Selected(keycode)
            searched.add_toSelected(keycode)
        else:
            searched.add_toSelected(keycode)
        assert searched.is_Selected(keycode) == True

    @pytest.mark.parametrize("key,keycode", [
        ("中国平安", "SH601318"),
        ("平安银行", "SZ000001"),
        ("pingan", "02318")
    ])
    def test_isNot_selected(self, key, keycode):
        self.searchPage.input_Search(key)
        assert self.searchPage.is_Selected(keycode) == False

    def teardown_method(self):
        self.searchPage.leave_searchPage()
