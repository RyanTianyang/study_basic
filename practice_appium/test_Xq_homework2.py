#!/usr/bin/env python
# encoding: utf-8

from appium import webdriver
import time
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

# 注释由于测试提交
# dev branch added
# check
# again
# fast forward
# ggod
# ffefefe
# aaa
class TestXueqiu_homework(object):
    driver = WebDriver

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
    def setup_class(cls):
        cls.driver = cls.install_app()

    def setup_method(self):
        self.driver = TestXueqiu_homework.driver
        for i in range(10):
            time.sleep(1)
            if self.driver.find_element_by_id("public_timeline_header_container"):
                print('循环第' + str(i) + '完全加载')
                break

    def test_swipeRepeat(self):
        action_swip = TouchAction(self.driver)
        windowSize = self.driver.get_window_size()

        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='基金']").click()
        time.sleep(1)
        markEndTimes = 0

        # 当未滑动选项剩余大于3时循环结束
        while markEndTimes <= 3:
            time.sleep(1)
            for y in range(5):
                # 纵向滑动
                action_swip.press(x=windowSize['width'] * 0.5, y=windowSize['height'] * 0.8) \
                    .move_to(x=windowSize['width'] * 0.5, y=windowSize['height'] * 0.5).release().perform()
                time.sleep(1)

            # 获取滑动控件区域，并将控件内容存到list
            widgetControl = self.driver.find_elements_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text!='']")
            widget_list = []
            for i in widgetControl:
                widget_list.append(i.text)

            # 横向滑动
            action_swip.press(x=windowSize['width'] * 0.9, y=windowSize['height'] * 0.5) \
                .move_to(x=windowSize['width'] * 0.1, y=windowSize['height'] * 0.5).release().perform()
            # 如果最后一个控件名为'保险'，则再滑动三次执行结束
            if widget_list[-1] == '保险':
                markEndTimes = markEndTimes + 1

    def teardown_method(self):
        self.driver.quit()

    @classmethod
    def teardown_class(cls):
        # 占位用
        pass
