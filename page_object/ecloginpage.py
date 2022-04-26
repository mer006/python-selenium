#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage
from common.readElement import Element
from utils.times import sleep

login = Element("EClogin")

class ECloginPage(WebPage):
    '''输入用户名密码'''
    def input_username_password(self, username = '', password = ''):
        self.input_text(login['用户名'], txt=username)
        self.input_text(login['密码'], txt=password)
        sleep()

    '''点击登录'''
    def login_click(self):
        self.is_click(login['登录按钮'])