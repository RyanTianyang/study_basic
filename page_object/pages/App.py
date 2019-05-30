# !/usr/bin/env python
# encoding: utf-8
from page_object.pages.BasePage import BasePage
from page_object.pages.mainPage import MainPage


class App(BasePage):

    @classmethod
    def main(cls):
        cls.get_client().restart_app()
        return MainPage()