# !/usr/bin/env python
# encoding: utf-8
import pytest

from page_object.pages.App import App


class Test_login(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage = App.main().Click_profile()

    def setup_method(self):
        self.loginPage = self.profilePage.Click_goto_login()

    @pytest.mark.parametrize("user,pwd,msg", [
        ("156005347600", "111111", "手机号码"),
        ("15600534760", "33333333", "密码错误")
    ])
    def test_login_pwd(self, user, pwd, msg):
        self.loginPage.loginBy_Pwd(user, pwd)
        assert msg in self.loginPage.error_Msg()

    def teardown_method(self):
        self.loginPage.back()
