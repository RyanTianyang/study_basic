# !/usr/bin/env python
# encoding: utf-8
from appium.webdriver.common.mobileby import MobileBy
import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_webView_homeWork(object):
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        cls.driver = cls.install_app()

    def setup_method(self):
        self.driver = Test_webView_homeWork.restart_app()
        WebDriverWait(self.driver, 20, 1).until(
            EC.presence_of_element_located((MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='交易']")))
        self.driver.find_element_by_xpath("//*[@resource-id='android:id/tabs']//*[@text='交易']").click()

    # A股开户Webview
    def test_webView_A(self):
        WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "A股开户")))
        self.driver.find_element_by_accessibility_id("A股开户").click()

    # 蛋卷基金错误手机号密码登录
    def test_danjuan(self):
        WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "基金开户")))
        self.driver.find_element_by_accessibility_id("基金开户").click()

        WebDriverWait(self.driver, 20, 1).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "已有蛋卷基金账户登录")))
        self.driver.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()

        WebDriverWait(self.driver, 20, 1).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "使用密码登录")))
        self.driver.find_element_by_accessibility_id("使用密码登录").click()

        self.driver.find_element_by_id("telno").send_keys("0909")
        self.driver.find_element_by_id("pass").send_keys("xxxxxxxx")

        self.driver.find_element_by_accessibility_id("安全登录").click()

        alterMessage = self.driver.find_element_by_id("message").get_attribute("text")
        assert "手机号码或者密码有误" in alterMessage

    def teardown_method(self):
        self.driver.back()
        self.driver.quit()

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
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
