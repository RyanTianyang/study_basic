# !/usr/bin/env python
# encoding: utf-8
from selenium.webdriver.common.by import By

from page_object.drivers.Xueqiu_client import XueqiuClient
from page_object.pages.BasePage import BasePage
from page_object.pages.ProfilePage import ProfilePage
from page_object.pages.SearchPage import SearchPage
from page_object.pages.Selected_page import Selected_Page


class MainPage(BasePage):
    _profile_btn=(By.ID,"user_profile_icon")
    _mainPage_search=(By.ID,"home_search")
    def Click_market(self):
        hangqing = "行情"
        self.findByText(self.hangqing)
        self.findByText(self.hangqing).click()
        return Selected_Page()

    def Click_profile(self):
        self.find(self._profile_btn).click()
        return ProfilePage()

    def Go_MainPage_Search(self):
        self.find(self._mainPage_search).click()
        return SearchPage()