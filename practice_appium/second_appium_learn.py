#!/usr/bin/env python
# encoding: utf-8


from appium import webdriver

caps = {
    "platformName": "android",
    "deviceName": "hogwarts",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "autoGrantPermissions": True,
    "unicodeKeyboard": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.find_element_by_
