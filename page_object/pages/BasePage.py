# !/usr/bin/env python
# encoding: utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.drivers.Xueqiu_client import XueqiuClient


class BasePage(object):

    def __init__(self):
        self.driver = self.get_driver()

    @classmethod
    def get_driver(cls):
        cls.driver = XueqiuClient.driver
        return cls.driver

    @classmethod
    def get_client(cls):
        return XueqiuClient

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)

    def findByText(self, text) ->WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))
