# !/usr/bin/env python
# encoding: utf-8
from selenium.webdriver.common.by import By
from page_object.pages.BasePage import BasePage


class SearchPage(BasePage):
    _search_input = (By.ID, "search_input_text")
    _cancle_btn = (By.ID, "action_close")

    def input_Search(self, search_detail):
        self.find(self._search_input).click()
        self.find(self._search_input).send_keys(search_detail)
        return self

    def add_toSelected(self, key_code):
        follow_btn = (
        By.XPATH, "//*[contains(@resource-id,'stockCode') and contains(@text, '%s')]/../../.." % key_code +
        "//*[contains(@resource-id, 'follow_btn')]")

        self.find(follow_btn).click()
        return self

    def is_Selected(self, key_code):
        follow_btn = (
        By.XPATH, "//*[contains(@resource-id,'stockCode') and contains(@text, '%s')]/../../.." % key_code +
        "//*[contains(@resource-id, 'follow')]")

        if_follow = self.find(follow_btn).get_attribute("resourceId")
        return "followed_btn" in if_follow

    def remove_Selected(self, key_code):
        followed_btn = (
        By.XPATH, "//*[contains(@resource-id,'stockCode') and contains(@text, '%s')]/../../.." % key_code +
        "//*[contains(@resource-id, 'followed_btn')]")

        self.find(followed_btn).click()
        return self

    def leave_searchPage(self):
        self.find(self._cancle_btn).click()
        from page_object.pages.mainPage import MainPage
        return MainPage()
