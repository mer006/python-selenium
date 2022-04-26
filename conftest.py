#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
from py.xml import html
from selenium import webdriver

driver = None

@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()

    '''定义一个清理函数，相当于teardown操作'''
    def fn():
        driver.quit()
    
    ''''注册清理函数'''
    request.addfinalizer(fn)
    return driver