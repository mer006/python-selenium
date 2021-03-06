#! usr/bin/env python3
# -*- coding:utf-8 -*-
from utils.times import dt_strftime
import os
from selenium.webdriver.common.by import By

class ConfigManager():
    #项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    REPORT_FILE = os.path.join(BASE_DIR, "report", "report.html")
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    @property
    def ini_file(self):
        '''配置文件'''
        ini_file = os.path.join(self.BASE_DIR,'config','config.ini')
        if not os.path.exists(ini_file):
            print("配置文件%s不存在!"%ini_file)
        else:
            return ini_file
    #LOG_FILE
    @property
    def log_file(self):
        '''配置文件'''
        log_dir = os.path.join(self.BASE_DIR,'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        else:
            return os.path.join(log_dir,'{}.log'.format(dt_strftime()))


    #元素定位类型
    LOCATE_MODE = {
        "css" : By.CSS_SELECTOR,
        "id" : By.ID,
        "xpath" : By.XPATH,
        "class" : By.CLASS_NAME,
        "name" : By.NAME
    }

    #邮件信息
    EMAIL_INFO = {
        "username" : "lxl1@test.net",
        "password" : "12345678",
        "smtp_host" : "192.168.20.16",
        "smtp_port" : "25"
    }

    #收件人列表
    ADDRESS = ["lxl4@test.net"]

#其他文件可以直接引用cm
cm = ConfigManager()
if __name__ == '__main__':
    print('BASE_DIR:'+cm.BASE_DIR)