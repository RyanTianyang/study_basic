#!/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_webView(object):
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        cls.driver = cls.install_app()

    def setup_method(self):
        self.driver = Test_webView.driver
        WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='交易']")))
        self.driver.find_element_by_xpath("//*[@resource-id='android:id/tabs']//*[@text='交易']").click()

    def test_webView_A(self):
        WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "A股开户")))
        self.driver.find_element_by_accessibility_id("A股开户").click()

    def teardown_method(self):
        self.driver.back()

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
        driver.implicitly_wait(20)
        return driver
