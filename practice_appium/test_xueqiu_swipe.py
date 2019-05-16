#!/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.touch_action import TouchAction
import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import time


class Test_swipe(object):
    driver=WebDriver

    @classmethod
    def setup_class(cls):
        cls.driver=cls.install_app()


    def setup_method(self):
        self.driver=Test_swipe.driver
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")

    def test_swipe(self):
        rect=self.driver.get_window_rect()
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='基金']").click()
        time.sleep(2)
        action_swipe = TouchAction(self.driver)
        for i in range(5):
            # action_swipe.press(x=rect['width']*0.2, y=rect['height']*0.8).move_to(x=rect['width']*0.2, y=rect['height']*0.6).release().perform()
            self.driver.swipe(rect['width']*0.2, rect['height']*0.8,rect['width']*0.2, rect['height']*0.6)
            time.sleep(2)

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