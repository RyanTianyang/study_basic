#!/usr/bin/env python
# encoding: utf-8

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver


class appium_cases():

    def __init__(self):
        caps = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": True,
            "unicodeKeyboard": True,
            "noReset": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_one(self):
        self.driver.implicitly_wait(20)
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView[2]")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/item_add_stock")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("阿里巴巴")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView")
        el4.click()
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative")
        el5.click()
        self.driver.quit()

    def test_two(self):
        closebtn = self.driver.find_element_by_id("com.xueqiu.android:id/action_close")
        closebtn.click()


    def test_three(self):
        self.driver.implicitly_wait(10)
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView[2]")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/item_add_stock")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("阿里巴巴")

if __name__ == "__main__":
    sad = appium_cases()
    sad.test_one()
