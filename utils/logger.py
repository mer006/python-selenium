#! usr/bin/env python3
# -*- coding:utf-8 -*-
from asyncio.log import logger
import os,sys
parentdir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,parentdir)

import logging
from config.conf import cm

class Log:
    '''别人的
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            #设置输出的level
            self.logger.setLevel(logging.INFO)

            #创建一个handle写入文件，并设置写入的level
            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            #创建一个handle输出控制台，并设置写入的level
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            #定义输入格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            #添加到hanler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
    '''
    def my_log(self,msg,level):
        #日志收集器
        self.logger = logging.getLogger()

        #定义日志等级，总开关
        self.logger.setLevel(logging.INFO)

        #创建一个handle写入文件，并设置写入的level
        fh = logging.FileHandler(cm.log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        #创建一个handle输出控制台，并设置写入的level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义输入格式
        formatter = logging.Formatter(self.fmt)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #添加到hanler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        #收集日志
        if level == 'DEBUG':
            self.logger.debug(msg)
        elif level == 'INFO':
            self.logger.info(msg)
        elif level == 'WARNING':
            self.logger.warning(msg)
        elif level == 'ERROR':
            self.logger.error(msg)
        elif level == 'CRITICAL':
            self.logger.critical(msg)
        
        #关闭输出通道
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)

    #重新实现日志方法
    def debug(self,msg):
        self.my_log(msg, 'DEBUG')
        
    def info(self,msg):
        self.my_log(msg, 'INFO')

    def warning(self,msg):
        self.my_log(msg, 'WARNING')

    def error(self,msg):
        self.my_log(msg, 'ERROR')

    def critical(self,msg):
        self.my_log(msg, 'CRITICAL')
        
    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

log = Log()

if __name__ == '__main__':
    mylog = Log()
    mylog.info('s3333')
    Log().my_log('hellword','INFO')
