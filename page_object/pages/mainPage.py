# !/usr/bin/env python
# encoding: utf-8
from page_object.drivers.Xueqiu_client import XueqiuClient
from page_object.pages.Selected_page import Selected_Page


class MainPage(object):

    def __init__(self):
        XueqiuClient.restart_app()

    def ClickSelected(self,SelectedName):
        XueqiuClient.driver.find_element_by_xpath("//*[@text='"+SelectedName+"']")
        XueqiuClient.driver.find_element_by_xpath("//*[@text='" + SelectedName + "']").click()

        return Selected_Page()