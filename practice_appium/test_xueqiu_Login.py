#!/usr/bin/env python
# encoding: utf-8
import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueQiu(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print("此处为setup-class，仅执行一次")
        cls.driver = cls.install_app()

        # 进入"我的"页面（使用intallapp的driver时需要取消注释）
        # el1 = cls.driver.find_element_by_id("user_profile_icon")
        # el1.click()

    # def setup_method(self):
    #     #使用install-app的driver
    #     print("此处为setup-method,执行每个用例之前执行一次")
    #     self.driver = TestXueQiu.driver
    #
    #     # 每次执行之前进行"点击登录"操作
    #     el2 = self.driver.find_element_by_id("tv_login")
    #     el2.click()

    def setup_method(self):
        print("此处为setup-method,执行每个用例之前执行一次")
        # 使用restart-app的driver
        self.driver = self.restart_app()

        # 进入"我的"页面
        el1 = self.driver.find_element_by_id("user_profile_icon")
        el1.click()

        # 每次执行之前进行"点击登录"操作
        el2 = self.driver.find_element_by_id("tv_login")
        el2.click()

    def test_loginPhone(self):
        # self.driver=TestXueQiu.driver
        el3 = self.driver.find_element_by_id("tv_login_by_phone_or_others")
        el3.click()

    def test_loginMailOther(self):
        el3 = self.driver.find_element_by_id("tv_login_by_phone_or_others")
        el3.click()
        # el4 = self.driver.find_element_by_id("tv_login_with_account")
        # el4.click()
        self.driver.find_element_by_xpath("//*[@text='邮箱手机号密码登录']").click()


    def teardown_method(self):
        print("此处为teardown_method,每个用例执行之后执行一次")
        self.driver.back()
        self.driver.quit()

    @classmethod
    def teardown_class(cls):
        pass

    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": True,
            # 跳过键盘权限
            # "unicodeKeyboard": True
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # "autoGrantPermissions": True,
            # "unicodeKeyboard": True
            # 保留之前执行的数据，可以用于case依赖
            "noReset": True
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
