# !/usr/bin/env python
# encoding: utf-8
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class XueqiuClient(object):
    driver:WebDriver
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
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # "autoGrantPermissions": True,
            "unicodeKeyboard": True,
            # 保留之前执行的数据，可以用于case依赖
            "noReset": True
        }
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver