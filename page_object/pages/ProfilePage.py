# !/usr/bin/env python
# encoding: utf-8
from page_object.pages.BasePage import BasePage
from page_object.pages.LoginPage import LoginPage


class ProfilePage(BasePage):
    def Click_goto_login(self):
        self.findByText("点击登录").click()
        return LoginPage()