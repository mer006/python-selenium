#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from sys import executable
import pytest
from py.xml import html
from selenium import webdriver

driver = None

@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Firefox()
        driver.maximize_window()

    def fn():
        driver.quit()
    
    request.addfinalizer(fn)
    return driver