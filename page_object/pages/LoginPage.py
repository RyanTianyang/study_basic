# !/usr/bin/env python
# encoding: utf-8
from selenium.webdriver.common.by import By

from page_object.pages.BasePage import BasePage



class LoginPage(BasePage):
    _phone_or_otherLocator=(By.ID,"tv_login_by_phone_or_others")
    _mailOr_phoneLoginType=(By.ID,"tv_login_with_account")
    _inputLogin_account=(By.ID,"login_account")
    _inputLogin_pwd=(By.ID,"login_password")
    _accountLogin_btn=(By.ID,"button_next")
    _back_btn=(By.XPATH,"//*[contains(@resource-id,'iv_action_back') or contains(@resource-id,'iv_close')]")
    _Login_errorMsg=(By.ID,"md_content")


    def loginBy_WX(self):
        return self

    def loginBy_Msg(self,phone,verify_code):
        return self

    def loginBy_Pwd(self,accuont,pwd):
        self.find(self._phone_or_otherLocator).click()
        self.find(self._mailOr_phoneLoginType).click()
        self.find(self._inputLogin_account).click()
        self.find(self._inputLogin_account).send_keys(accuont)
        self.find(self._inputLogin_pwd).click()
        self.find(self._inputLogin_pwd).send_keys(pwd)
        self.find(self._accountLogin_btn).click()
        return self

    def back(self):
        self.find(self._back_btn).click()
        from page_object.pages.ProfilePage import ProfilePage
        return ProfilePage()

    def error_Msg(self):
        msg_error=self.find(self._Login_errorMsg).text
        self.findByText("确定").click()
        return msg_error



