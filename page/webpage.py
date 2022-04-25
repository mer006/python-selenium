#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
selenium基类
本文件存放selenium基类的封装方法
'''
from http.server import executable
import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from config.conf import cm
from utils.times import sleep
from utils.logger import log
from selenium import webdriver


class WebPage():
    '''selenium基类'''
    def __init__(self, driver):
        #self.driver = webdriver.Chrome(executable_path='')
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)
    
    def get_url(self, url):
        '''打开网址并验证'''
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时,请检查网络或者网址服务器" %url)
        
    @staticmethod
    def element_locator(func, locator):
        '''元素定位器'''
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        '''寻找单个元素'''
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)
    
    def find_elements(self, locator):
        '''获取多个相同的元素'''
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        '''获取相同元素的个数'''
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number
    
    def input_text(self, locator, txt):
        '''输入(输入前先清空)'''
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(locator))
    
    def is_click(self, locator):
        '''点击'''
        self.find_element(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))
    
    def element_text(self, locator):
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text
    
    @property
    def get_source(self):
        '''获取页面源代码'''
        return self.driver.page_source
    
    def refresh(self):
        '''刷新页面'''
        self.driver.refresh()
        self.driver.implicitly_wait(30)